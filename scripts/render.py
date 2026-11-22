#!/usr/bin/env python3
"""Render the curated JSON catalog into Markdown and CSV; no network access."""
import argparse
import csv
import io
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["full_name", "scope", "category", "summary_zh", "stars", "forks",
          "language", "license", "archived", "pushed_at", "starred_at",
          "is_starred", "url", "evidence_url"]


def cell(value):
    return str(value if value is not None else "未识别").replace("|", "\\|").replace("\n", " ")


def link(project):
    return f"[{project['full_name']}]({project['url']})"


def validate(data):
    projects = data["repositories"]
    if data.get("schema_version") != 1 or not isinstance(projects, list):
        raise ValueError("Unsupported catalog schema")
    for key in ("id", "full_name"):
        if len({p[key] for p in projects}) != len(projects):
            raise ValueError(f"Duplicate {key}")
    for project in projects:
        for key in FIELDS:
            if key not in project:
                raise ValueError(f"{project.get('full_name')}: missing {key}")
        if project["scope"] not in {"core", "supporting"}:
            raise ValueError("Unknown scope")
        if not isinstance(project["is_starred"], bool):
            raise ValueError("is_starred must be a boolean")
        if not project["url"].startswith("https://github.com/"):
            raise ValueError("Repository URLs must point to GitHub")
        if not project["evidence_url"].startswith("https://github.com/"):
            raise ValueError("Evidence must link to upstream GitHub documentation")
        if not project["summary_zh"] or not project["category"]:
            raise ValueError("Missing human-reviewed classification")
    datetime.fromisoformat(data["fetched_at"].replace("Z", "+00:00"))


def render(data):
    validate(data)
    projects = data["repositories"]
    current = [p for p in projects if p["is_starred"]]
    history = [p for p in projects if not p["is_starred"]]
    counts = Counter(p["scope"] for p in current)
    fetched = datetime.fromisoformat(data["fetched_at"].replace("Z", "+00:00"))
    stamp = fetched.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M UTC+8")
    source = f"https://github.com/{data['username']}?tab=stars"
    api = f"https://api.github.com/users/{data['username']}/starred?per_page=100"
    intro = [
        "# 🎬 AI Video Stars", "",
        f"从 [{data['username']} 的 GitHub 公开星标]({source})中整理的 AI 视频项目中文索引。",
        "覆盖短剧与影片创作、Agent 视频制作、剪辑、视频理解与增强，以及直接参与制作流程的配音、音乐、渲染和动作工具。", "",
        f"**元数据快照：{stamp}**。项目用途由人工核对上游 README / 文档后归类；功能说明来自项目文档，未做逐项安装测试。", "",
        "## 统计", "",
        "| 指标 | 数量 |", "| --- | ---: |",
        f"| 扫描的公开星标仓库 | {data['total_public_starred']} |",
        f"| 当前收录的相关仓库 | {len(current)} |",
        f"| 核心视频项目 | {counts['core']} |",
        f"| 配套工具 | {counts['supporting']} |",
        f"| 已不在公开星标中的历史收录 | {len(history)} |", "",
        "每个仓库只统计一次，按主要用途归类。Star 数和最近推送日期是快照数据；Star 数不代表生成质量。", "",
        "## 文件入口", "",
        "- [完整目录与逐项说明](docs/catalog.md)：用途、标签、运行依赖说明、官方证据链接。",
        "- [CSV 统计表](data/projects.csv)：可导入 Excel、Numbers 或其他数据工具。",
        "- [JSON 数据](data/projects.json)：人工分类和公开元数据的统一数据源。",
        "- [收录范围与核对方法](docs/methodology.md)：核心 / 配套的边界及排除示例。",
        "- [维护说明](docs/maintenance.md)：手动刷新元数据、审核候选与重新生成目录。", "",
    ]
    catalog = ["# AI 视频项目完整目录", "", f"元数据快照：{stamp}。返回 [首页](../README.md)。", "",
               "核心项目与配套工具分别统计，每组按主要用途归类，组内按 Star 数降序排列。",
               "许可证列为 GitHub API 识别结果；`NOASSERTION` 表示自定义或未识别，`未识别` 表示 API 未返回。具体文本及模型、API 条件请查看原项目。", ""]
    for scope, title in (("core", "核心视频项目"), ("supporting", "配套工具")):
        subset = [p for p in current if p["scope"] == scope]
        intro += [f"## {title}（{len(subset)}）", ""]
        catalog += [f"## {title}（{len(subset)}）", ""]
        for category in dict.fromkeys(p["category"] for p in subset):
            group = sorted((p for p in subset if p["category"] == category), key=lambda p: (-p["stars"], p["full_name"].lower()))
            intro += [f"### {category}（{len(group)}）", "",
                      "| 项目 | 用途 | Stars | 最近推送（UTC） |",
                      "| --- | --- | ---: | --- |"]
            catalog += [f"### {category}（{len(group)}）", ""]
            for p in group:
                intro.append(f"| {link(p)} | {cell(p['summary_zh'])} | {p['stars']:,} | {(p['pushed_at'] or '未返回')[:10]} |")
                status = "已归档" if p["archived"] else "未归档"
                catalog += [f"#### {link(p)}", "", p["summary_zh"], "",
                            f"- **用途标签：** {'、'.join(p['tags'])}",
                            f"- **使用说明：** {p['usage_notes_zh']}",
                            f"- **公开元数据：** {p['stars']:,} Stars · {p['forks']:,} Forks · 主要语言 {cell(p['language'])} · 许可证 `{cell(p['license'])}` · {status}。",
                            f"- **最近推送：** {p['pushed_at']}；**星标时间：** {p['starred_at'] or '未返回'}（UTC）。",
                            f"- **归类依据：** {p['evidence_zh']} [查看官方文档]({p['evidence_url']})。", ""]
            intro.append("")
    if history:
        catalog += ["## 已不在公开星标中的历史收录", "", "不计入当前收录统计；可能为取消星标、仓库删除或可见性变化，保留最后一次可见元数据。", ""]
        for p in history:
            catalog.append(f"- {link(p)}：{p['summary_zh']}")
        catalog.append("")
    intro += ["## 数据来源与更新", "",
              f"基础数据来自 [GitHub Stars REST API]({api})；逐项归类依据见[完整目录](docs/catalog.md)。",
              "此次覆盖接口可见的公开星标，不包含私有仓库，也不加入未打星的外部推荐。仅保存入选项目的公开元数据。", "",
              "```bash", "python scripts/refresh.py", "python scripts/render.py", "```", "",
              "刷新脚本仅更新已收录项目的元数据并生成待审核候选；新增项目须人工核对后加入 JSON。刷新不会自动提交、推送或建立定时任务。", "",
              "本仓库仅整理项目索引与原创中文摘要，不包含原项目代码或模型权重。各原项目的代码、模型及服务以其自身条款为准。", ""]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=FIELDS)
    writer.writeheader()
    for p in sorted(projects, key=lambda p: (not p["is_starred"], p["scope"] != "core", p["category"], -p["stars"])):
        writer.writerow({k: p[k] for k in FIELDS})
    return {"README.md": "\n".join(intro), "docs/catalog.md": "\n".join(catalog),
            "data/projects.csv": "\ufeff" + output.getvalue()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated files without writing")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    rendered = render(data)
    stale = []
    for path, content in rendered.items():
        target = ROOT / path
        encoded = content.encode("utf-8")
        if args.check:
            if not target.exists() or target.read_bytes() != encoded:
                stale.append(path)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(encoded)
    if stale:
        parser.exit(1, "Generated files are stale: " + ", ".join(stale) + "\n")
    print(f"{'Checked' if args.check else 'Rendered'} {len(rendered)} files; {len(data['repositories'])} curated projects.")


if __name__ == "__main__":
    main()
