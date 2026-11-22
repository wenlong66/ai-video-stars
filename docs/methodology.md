# 收录范围与核对方法

## 本次范围

来源为 [wenlong66 的公开 GitHub Stars](https://github.com/wenlong66?tab=stars)。首次快照于 **2026-11-23 00:33 UTC+8** 获取，两页分别包含 100 和 87 个仓库，共 **187 个不同仓库**。完整翻页后，再按仓库 ID 去重、检查元数据并核对疑似相关项目的官方 README / 子项目文档。

本次收录 **22 个仓库**：**12 个核心视频项目、10 个配套工具**。这些数字仅描述本次公开星标快照；当前数据见[首页](../README.md)和 [JSON](../data/projects.json)。

## 分类口径

| 范围 | 收录条件 | 示例 |
| --- | --- | --- |
| 核心视频项目 `core` | 官方文档明确提供 AI 视频创作、Agent 视频制作/剪辑、可编辑视频生成、视频理解、视频增强等能力。 | Toonflow、火宝短剧、video-use、MiniCPM-V、paper2gui |
| 配套工具 `supporting` | 为视频制作提供直接的剧本/分镜、配音、配乐、动捕、动画素材、合成渲染能力；或视频是综合工作台中的明确功能。 | VoiceStudio、VoxCPM、YuE、FreeMoCap、FFmpeg、Remotion、OpenDesign |

一个仓库只记一条记录。多个功能可记入标签，但只指定一个主要分类；独立子项目也不重复增加仓库数。

本目录中的“AI 视频相关”范围包括制作工具和工作流，不表示每个项目都是能独立部署的视频生成模型。FFmpeg、Remotion 是制作基础工具，MiniCPM-V 用于理解视频，VoxCPM、YuE 输出音频，均已明确标注。

## 特别核实的项目

- [Cowart](https://github.com/zhongerxin/Cowart/blob/main/README.md)：仓库描述为空，但 README 有 AI 影片、分镜、HTML/JS 动效和 MP4 导出，不能只靠名称或描述关键词检索。
- [MS-Agent 的 Singularity Cinema](https://github.com/modelscope/ms-agent/blob/main/projects/singularity_cinema/README_EN.md)：主仓库是通用 Agent 框架；收录依据为其明确的主题/文本到短视频生产子项目。
- [sprite-gen](https://github.com/aldegad/sprite-gen/blob/main/README.md) 与 [agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge/blob/main/README.md)：因存在图生视频、抽帧与循环动画制作管线而收录；它们的主要产物仍是游戏动画素材，归配套工具。

## 边界与排除示例

| 项目 | 本次未收录原因 |
| --- | --- |
| [HGhubX](https://github.com/zxsos/HGhubX) | 短剧观看客户端，未据此认定具有 AI 短剧制作能力。 |
| [RuView](https://github.com/ruvnet/RuView) | 利用 WiFi 信号进行空间感知，不能因为说明中出现 video 就归为视频工具。 |
| [manga-generator](https://github.com/stockedge/manga-generator/blob/master/README.md) | 核对到的是静态漫画、排版和 PDF 流程。 |
| [cangjie-skill](https://github.com/kangarooking/cangjie-skill/blob/main/README.md) | 侧重字幕/转写文本中的知识提炼，不属于本次视频视觉理解或制作范围。 |
| [PersonaPlex](https://github.com/NVIDIA/personaplex/blob/main/README.md) | 侧重实时语音对话，未按泛音频关联直接纳入。 |
| [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 社交平台内容和评论采集工具。 |

范围不扩展到所有播放器、视频下载/采集器、静态图片或漫画工具、通用写作工具、通用 Agent 平台。也不加入未打星的热门视频项目。

## 字段与证据

| 字段 | 含义 |
| --- | --- |
| `id`、`full_name`、`url` | GitHub 仓库稳定 ID、当前完整名称和地址；ID 用于识别重命名或迁移。 |
| `scope`、`category`、`tags` | 人工核对后的范围、主要分类和用途标签。 |
| `summary_zh`、`usage_notes_zh` | 原创中文用途摘要及影响使用的主要依赖说明。 |
| `evidence_url`、`evidence_zh`、`reviewed_at` | 官方文档地址、归类理由，以及首次人工核对所用快照时间。 |
| `stars`、`forks`、`language`、`archived` | GitHub API 返回的计数、主要语言和归档标志。 |
| `pushed_at` | GitHub 返回的最近推送时间（UTC），不是最后发布版本日期，也不是维护质量评分。 |
| `starred_at` | 当前账号打星的时间（UTC）。 |
| `license` | GitHub API 识别的许可证标识；可能为 `null` 或 `NOASSERTION`，不能据此推断商业使用条件。 |
| `is_starred` | 本次刷新是否仍出现在可见的公开星标列表；缺失也可能是仓库删除或可见性变化。 |
| 顶层 `fetched_at` | 本轮公开元数据抓取时间；不表示用途摘要也在此时重新审核。 |

所有用途说明来自官方仓库文档，未逐项安装验证。完整目录为每个收录项目保留证据链接。许可证以原项目文本为准；模型权重和外部 API 可能使用独立条款。

## 可重复性与局限

- 采用公开 Stars 接口，不能声称覆盖不可见的私有星标。
- 首次进行全列表人工筛选；后续脚本的候选筛选只使用名称、描述和 Topics 关键词，可能漏掉 Cowart 这类描述不足的项目，仍应人工复核新星标。
- Stars 与仓库内容会变化；人工用途说明不会在元数据刷新时被自动改写。
- 仓库不包含原项目源码、模型权重、账号凭据或无关星标的完整快照。
