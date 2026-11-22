#!/usr/bin/env python3
"""Refresh reviewed public-star metadata; never classify, schedule, or push."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYWORDS = (
    "video", "视频", "短剧", "漫剧", "字幕", "filmmak", "motion",
    "dubbing", "tts", "音乐", "配音", "storyboard", "分镜", "lip-sync",
    "talking-head", "frame-interpolation", "super-resolution", "数字人",
)


def fetch_stars(username: str) -> dict[int, dict]:
    """Read every page before returning; only public repositories are retained."""
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", username):
        raise ValueError("Invalid GitHub username")
    headers = {
        "Accept": "application/vnd.github.star+json",
        "User-Agent": "ai-video-stars-catalog",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    result: dict[int, dict] = {}
    for page in range(1, 10001):
        url = f"https://api.github.com/users/{username}/starred?per_page=100&page={page}"
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            rows = json.load(response)
            links = response.headers.get("Link", "")
        if not isinstance(rows, list):
            raise ValueError("Unexpected GitHub response: expected a list")
        for row in rows:
            if not isinstance(row, dict) or not isinstance(row.get("repo"), dict):
                raise ValueError("Unexpected GitHub star record")
            repo = row["repo"]
            if type(repo.get("id")) is not int or not repo.get("full_name"):
                raise ValueError("Missing repository identity in GitHub response")
            if repo.get("private") is not False:
                continue
            result[repo["id"]] = {**repo, "starred_at": row.get("starred_at")}
        if not re.search(r';\s*rel="next"', links):
            return result
        if not rows:
            raise ValueError("GitHub returned an empty page with a next-page link")
    raise ValueError("Pagination exceeded safety limit; nothing was written")


def metadata(repo: dict) -> dict:
    license_info = repo.get("license") or {}
    return {
        "id": repo["id"], "full_name": repo["full_name"],
        "url": repo["html_url"], "stars": repo["stargazers_count"],
        "forks": repo["forks_count"], "language": repo.get("language"),
        "license": license_info.get("spdx_id"),
        "archived": repo.get("archived", False),
        "pushed_at": repo.get("pushed_at"), "starred_at": repo.get("starred_at"),
        "is_starred": True, "description": repo.get("description"),
    }


def build_updates(catalog: dict, stars: dict[int, dict]) -> tuple[dict, dict]:
    entries = catalog.get("repositories")
    if catalog.get("schema_version") != 1 or not isinstance(entries, list):
        raise ValueError("Expected schema_version 1 and a repositories list")
    known: set[int] = set()
    reviewed = []
    for entry in entries:
        repo_id = entry.get("id")
        if type(repo_id) is not int or repo_id in known:
            raise ValueError("Reviewed records require unique integer repository IDs")
        known.add(repo_id)
        # Copy all manual and unknown fields; only public metadata is replaced.
        current = {**entry, "is_starred": False}
        if repo_id in stars:
            current.update(metadata(stars[repo_id]))
        reviewed.append(current)
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    updated = {
        **catalog, "fetched_at": fetched_at,
        "total_public_starred": len(stars), "repositories": reviewed,
    }
    candidates = []
    for repo_id, repo in stars.items():
        if repo_id in known:
            continue
        haystack = " ".join([
            repo["full_name"], repo.get("description") or "",
            " ".join(repo.get("topics") or []),
        ]).casefold()
        matches = [word for word in KEYWORDS if word in haystack]
        if matches:
            candidates.append({**metadata(repo), "matched_keywords": matches})
    candidates.sort(key=lambda entry: (-entry["stars"], entry["full_name"].casefold()))
    pending = {
        "schema_version": 1, "username": catalog["username"],
        "fetched_at": fetched_at, "review_required": True,
        "repositories": candidates,
    }
    return updated, pending


def atomic_write(path: Path, value: dict) -> None:
    """Replace a file only after its entire new JSON document is on disk."""
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data/projects.json")
    parser.add_argument("--dry-run", "--check", dest="dry_run", action="store_true",
                        help="fetch and summarize without writing any files")
    args = parser.parse_args()
    try:
        catalog = json.loads(args.data.read_text(encoding="utf-8"))
        stars = fetch_stars(catalog["username"])
        updated, pending = build_updates(catalog, stars)
        # No disk writes occur until the entire network read and calculation succeed.
        if not args.dry_run:
            atomic_write(args.data, updated)
            atomic_write(args.data.with_name("candidates.json"), pending)
        active = sum(item["is_starred"] for item in updated["repositories"])
        print(json.dumps({
            "dry_run": args.dry_run, "public_stars": len(stars),
            "reviewed": len(updated["repositories"]), "still_starred": active,
            "unreviewed_candidates": len(pending["repositories"]),
        }, ensure_ascii=False))
        return 0
    except urllib.error.HTTPError as error:
        print(f"GitHub HTTP {error.code}; catalog was not refreshed.", file=sys.stderr)
    except (urllib.error.URLError, TimeoutError):
        print("GitHub network request failed; catalog was not refreshed.", file=sys.stderr)
    except (OSError, ValueError, KeyError, TypeError) as error:
        # Exception text may include external data; do not print it or credentials.
        print(f"Refresh failed ({type(error).__name__}); inspect input or disk access.",
              file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
