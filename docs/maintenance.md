# 维护说明

本仓库使用 Python 3.10+ 标准库，无需安装第三方包。维护流程为“刷新公开元数据 → 人工审核候选 → 生成目录 → 查看改动并提交”。

## 1. 刷新公开元数据

在仓库根目录运行：

```bash
python scripts/refresh.py
```

脚本会完整分页读取 `data/projects.json` 中 `username` 对应的公开星标，按仓库 ID 去重，然后：

- 更新已收录项目的 Star / Fork 数、主要语言、许可证识别标签、归档标志、最近推送和打星时间。
- 保留人工分类、中文摘要、标签、使用说明、证据地址及人工核对时间。
- 若原项目已不在公开星标列表中，保留记录并标记 `is_starred=false`。可能是取消星标，也可能是删除或改为私有；不自动断言原因。
- 将关键词命中的未收录仓库写入 `data/candidates.json`，标记为待人工审核。
- 全部分页请求与计算成功后才写文件；每个 JSON 文件采用临时文件替换。网络失败不会用不完整列表覆盖原清单。

只检查而不改动文件：

```bash
python scripts/refresh.py --dry-run
```

公开接口无需令牌。需要提高接口访问额度时，可通过运行环境提供 `GITHUB_TOKEN`；不要把令牌写进仓库文件。刷新命令会访问 GitHub，`--dry-run` 也需要联网。

`candidates.json` 可能包含播放器、爬虫等误命中项；它不会自动加入正式目录，也不参与统计。该文件默认不提交，因为它只是本地审核队列。

## 2. 审核和加入新项目

打开候选仓库的官方 README / 文档，确认是否有实际的视频功能或直接的制作用途，再编辑 `data/projects.json` 中的 `repositories` 数组。为新条目填写与已有项目一致的字段，尤其是：

```json
{
  "scope": "core",
  "category": "Agent 视频制作与剪辑",
  "summary_zh": "基于文档核实的简短用途说明。",
  "tags": ["视频剪辑", "Agent"],
  "usage_notes_zh": "运行方式及关键依赖。",
  "evidence_url": "https://github.com/OWNER/REPO/blob/main/README.md",
  "evidence_zh": "该文档中支持归类的具体功能。",
  "reviewed_at": "2026-11-22T16:33:48+00:00"
}
```

上方仅演示人工字段，完整条目还需包含仓库 ID、URL、计数、语言、许可证、时间、`is_starred` 等元数据。以现有完整条目为模板，不要将示例地址原样加入。

关键词筛选无法保证发现全部新功能；每次较大更新时，应同时检查新增星标以及已收录项目的功能变化。变更功能摘要时更新 `reviewed_at`，仅刷新 Star 数时不改此字段。

## 3. 重新生成并检查

```bash
python scripts/render.py
python scripts/render.py --check
git diff --stat
git diff
```

`render.py` 不联网，使用 JSON 统一生成：

- `README.md`：概览、当前统计和分类表。
- `docs/catalog.md`：逐项说明、用途边界和证据链接。
- `data/projects.csv`：含 UTF-8 BOM 的表格数据，便于 Excel 直接打开中文。

`--check` 会验证基础结构、重复记录和生成文件是否与数据一致，并在发现不一致时返回非零退出码。它不会改动文件。

## 4. 提交

```bash
git add README.md docs/catalog.md data/projects.json data/projects.csv
git commit -m "docs: refresh AI video star catalog"
git push
```

本次只提供手动更新工具，没有启用 GitHub Actions 定时任务或任何后台自动更新。发布统计时，请说明核心项目和配套工具分别有多少；不要把全部项目都称为视频生成模型。
