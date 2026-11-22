# 🎬 AI Video Stars

从 [wenlong66 的 GitHub 公开星标](https://github.com/wenlong66?tab=stars)中整理的 AI 视频项目中文索引。
覆盖短剧与影片创作、Agent 视频制作、剪辑、视频理解与增强，以及直接参与制作流程的配音、音乐、渲染和动作工具。

**元数据快照：2026-11-23 00:33 UTC+8**。项目用途由人工核对上游 README / 文档后归类；功能说明来自项目文档，未做逐项安装测试。

## 统计

| 指标 | 数量 |
| --- | ---: |
| 扫描的公开星标仓库 | 187 |
| 当前收录的相关仓库 | 22 |
| 核心视频项目 | 12 |
| 配套工具 | 10 |
| 已不在公开星标中的历史收录 | 0 |

每个仓库只统计一次，按主要用途归类。Star 数和最近推送日期是快照数据；Star 数不代表生成质量。

## 文件入口

- [完整目录与逐项说明](docs/catalog.md)：用途、标签、运行依赖说明、官方证据链接。
- [CSV 统计表](data/projects.csv)：可导入 Excel、Numbers 或其他数据工具。
- [JSON 数据](data/projects.json)：人工分类和公开元数据的统一数据源。
- [收录范围与核对方法](docs/methodology.md)：核心 / 配套的边界及排除示例。
- [维护说明](docs/maintenance.md)：手动刷新元数据、审核候选与重新生成目录。

## 核心视频项目（12）

### 短剧、漫剧与整片创作（4）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | 可自部署的 AI 短剧与漫剧工作台，把剧本分镜、角色场景资产、3D 预演和按镜头视频生成组织在同一画布。 | 22,521 | 2026-11-20 |
| [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama) | AI 短剧生产平台，完成小说或剧本解析、角色与场景设计、分镜视频生成以及整集拼接导出。 | 17,812 | 2026-11-21 |
| [yi1108/printfilm](https://github.com/yi1108/printfilm) | 面向 AI 漫剧和短视频的分步创作平台，支持文案分镜、参考图生图、图生视频与静图配音两条成片流程。 | 7,195 | 2026-11-20 |
| [modelscope/ms-agent](https://github.com/modelscope/ms-agent) | 内含 Singularity Cinema：从主题或文本生成脚本、分镜、旁白、图像及可选视频片段，再合成为讲解短视频。 | 4,430 | 2026-11-22 |

### Agent 视频制作与剪辑（3）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | 面向编程 Agent 的视频生产系统，串联资料研究、脚本、素材生成或检索、剪辑、配音字幕及最终合成。 | 82,343 | 2026-11-16 |
| [browser-use/video-use](https://github.com/browser-use/video-use) | 通过编程 Agent 剪辑已有素材，依据词级转录和按需视觉帧处理口头填充词、停顿、调色、字幕及动画覆盖层。 | 31,436 | 2026-10-08 |
| [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | 让编程 Agent 从参考视频、模板或文字需求建立可编辑的视频工作流，组合镜头、字幕、B-roll 和特效并制作变体。 | 31,077 | 2026-11-20 |

### 代码动画与可编辑视频（2）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 面向人和 AI Agent 的可编辑视频框架，把 HTML、CSS、JavaScript、媒体与可定位动画渲染为 MP4，适合产品演示、字幕和动效视频。 | 88,140 | 2026-11-22 |
| [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | 面向 Codex 的无限画布插件，可把提示词和参考图生成带分镜、运动及音效的 HTML/JS 动效影片，并预览、编辑和导出 MP4。 | 6,085 | 2026-10-08 |

### 视频理解与镜头拆解（2）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | 多模态模型系列，支持视频内容理解；仓库同时包含可接收连续音视频输入的 MiniCPM-o。 | 27,180 | 2026-11-09 |
| [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) | 为编程 Agent 拆解视频镜头、字幕、剪辑与音轨，输出 VIDEO.md、可读报告和按目标模型组织的重制计划。 | 12,098 | 2026-11-22 |

### 视频增强与后处理（1）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [Baiyuetribe/paper2gui](https://github.com/Baiyuetribe/paper2gui) | AI 桌面工具箱，包含视频超分、RIFE/DAIN 补帧、无绿幕视频抠像和字幕相关工具。 | 10,693 | 2024-09-20 |

## 配套工具（10）

### 综合创作工作台（1）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 综合 AI 设计工作台，集成 HyperFrames 视频与产品动效模板，可由编程 Agent 生成并导出 MP4，也可接入视频生成模型。 | 108,942 | 2026-11-22 |

### 视频合成与渲染（2）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 用 React 和网页技术以代码制作视频的框架，可作为 AI Agent 视频制作的合成、预览和批量渲染基础。 | 74,920 | 2026-11-20 |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 多媒体命令行与库工具，可处理音视频编码、格式转换、滤镜、字幕与最终合成。 | 67,947 | 2026-11-22 |

### 配音与音乐生成（3）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 本地 AI 语音工作台，支持视频翻译配音、声音克隆、声音设计和转写，可用于视频旁白与多语言制作。 | 116,367 | 2026-11-22 |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 文本转语音模型系列，支持多语言语音、声音设计与克隆，可为 AI 视频提供旁白和角色配音。 | 42,874 | 2026-11-09 |
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | 歌曲与音乐生成项目，当前 YuE2 支持歌词/风格驱动、可编辑旋律和和弦规划，以及翻唱与音乐编辑。 | 13,667 | 2026-11-01 |

### 动作捕捉与动画素材（3）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [freemocap/freemocap](https://github.com/freemocap/freemocap) | 动作捕捉系统与 GUI，可采集动作数据，为角色动画及相关视频制作提供动作素材。 | 10,873 | 2026-11-14 |
| [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | Agent 动画素材工具，通过母图生成动作视频，再抠像、抽帧、选择循环和重定时，导出可用于 Godot 等引擎的动画素材。 | 5,915 | 2026-11-13 |
| [aldegad/sprite-gen](https://github.com/aldegad/sprite-gen) | Codex/Claude 技能与 Python CLI，含单图生成动作视频、抽帧和自动循环裁切流程，输出透明 GIF、WebP 或条带动画。 | 4,180 | 2026-11-21 |

### 剧本与分镜（1）

| 项目 | 用途 | Stars | 最近推送（UTC） |
| --- | --- | ---: | --- |
| [Narcooo/inkos](https://github.com/Narcooo/inkos) | 故事创作 Agent，包含独立的剧本与分镜 Skills 及生产管线，可作为 AI 短剧制作的前期内容工具。 | 11,387 | 2026-10-24 |

## 数据来源与更新

基础数据来自 [GitHub Stars REST API](https://api.github.com/users/wenlong66/starred?per_page=100)；逐项归类依据见[完整目录](docs/catalog.md)。
此次覆盖接口可见的公开星标，不包含私有仓库，也不加入未打星的外部推荐。仅保存入选项目的公开元数据。

```bash
python scripts/refresh.py
python scripts/render.py
```

刷新脚本仅更新已收录项目的元数据并生成待审核候选；新增项目须人工核对后加入 JSON。刷新不会自动提交、推送或建立定时任务。

本仓库仅整理项目索引与原创中文摘要，不包含原项目代码或模型权重。各原项目的代码、模型及服务以其自身条款为准。
