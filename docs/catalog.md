# AI 视频项目完整目录

元数据快照：2026-11-23 00:33 UTC+8。返回 [首页](../README.md)。

核心项目与配套工具分别统计，每组按主要用途归类，组内按 Star 数降序排列。
许可证列为 GitHub API 识别结果；`NOASSERTION` 表示自定义或未识别，`未识别` 表示 API 未返回。具体文本及模型、API 条件请查看原项目。

## 核心视频项目（12）

### 短剧、漫剧与整片创作（4）

#### [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)

可自部署的 AI 短剧与漫剧工作台，把剧本分镜、角色场景资产、3D 预演和按镜头视频生成组织在同一画布。

- **用途标签：** AI短剧、AI漫剧、分镜、无限画布、视频生成、自部署
- **使用说明：** 有桌面客户端与 Docker 部署方式；支持外部模型 API、本地模型和 ComfyUI，模型服务需要单独配置。
- **公开元数据：** 22,521 Stars · 4,088 Forks · 主要语言 TypeScript · 许可证 `MIT` · 未归档。
- **最近推送：** 2026-11-20T11:01:16Z；**星标时间：** 2026-11-22T16:31:53Z（UTC）。
- **归类依据：** README 的亮点和常见问题列出无限画布、白模预演、按镜头视频生成、模型接入与本地部署，创作流程延伸到剪辑下载。 [查看官方文档](https://github.com/HBAI-Ltd/Toonflow-app/blob/master/README.md)。

#### [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)

AI 短剧生产平台，完成小说或剧本解析、角色与场景设计、分镜视频生成以及整集拼接导出。

- **用途标签：** AI短剧、剧本、角色资产、分镜、图生视频、视频合成
- **使用说明：** 当前 README 为 TypeScript 全栈、SQLite 和 Electron 桌面架构；文本、图片、视频模型在设置页配置。README 标示 CC BY-NC-SA 4.0。
- **公开元数据：** 17,812 Stars · 3,327 Forks · 主要语言 TypeScript · 许可证 `NOASSERTION` · 未归档。
- **最近推送：** 2026-11-21T08:22:40Z；**星标时间：** 2026-11-22T16:15:32Z（UTC）。
- **归类依据：** README 的项目简介、功能特性和六步教程逐项说明剧本改写、资产提取、批量视频生成、FFmpeg 单镜头处理及整集导出。 [查看官方文档](https://github.com/chatfire-AI/huobao-drama/blob/master/README.md)。

#### [yi1108/printfilm](https://github.com/yi1108/printfilm)

面向 AI 漫剧和短视频的分步创作平台，支持文案分镜、参考图生图、图生视频与静图配音两条成片流程。

- **用途标签：** AI漫剧、短视频、分镜、图生视频、配音、自部署
- **使用说明：** 提供 Docker 部署；当前 README 明确开源版文字、图片和视频通过 TokenFree New API，未配置 Key 只能用模拟模式看界面。
- **公开元数据：** 7,195 Stars · 835 Forks · 主要语言 Python · 许可证 `MIT` · 未归档。
- **最近推送：** 2026-11-20T08:04:15Z；**星标时间：** 2026-11-14T17:35:27Z（UTC）。
- **归类依据：** README 的核心功能区分 AI 视频模式与静图成片模式，描述分镜编辑、镜头生成、外部 TTS、FFmpeg 合成和下载，并列出模型配置要求。 [查看官方文档](https://github.com/yi1108/printfilm/blob/main/README.md)。

#### [modelscope/ms-agent](https://github.com/modelscope/ms-agent)

内含 Singularity Cinema：从主题或文本生成脚本、分镜、旁白、图像及可选视频片段，再合成为讲解短视频。

- **用途标签：** Agent、脚本分镜、文生视频、旁白字幕、Remotion、视频合成
- **使用说明：** 收录依据是仓库中的 projects/singularity_cinema 子项目；需配置 LLM、视觉与图像/视频服务，并安装 Python、FFmpeg，默认 Remotion 渲染另需 Node.js。官方说明素材输入以纯文本为主，效果随所选模型而异。
- **公开元数据：** 4,430 Stars · 547 Forks · 主要语言 Python · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-22T15:38:46Z；**星标时间：** 2026-04-08T12:20:01Z（UTC）。
- **归类依据：** 子项目 README 明确描述脚本与分镜、配音、可选字幕、图像、可选文生视频和最终合成流程，并列出 final_video.mp4 产物及 Remotion 渲染阶段。 [查看官方文档](https://github.com/modelscope/ms-agent/blob/main/projects/singularity_cinema/README_EN.md)。

### Agent 视频制作与剪辑（3）

#### [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage)

面向编程 Agent 的视频生产系统，串联资料研究、脚本、素材生成或检索、剪辑、配音字幕及最终合成。

- **用途标签：** Agent工作流、视频制作、素材检索、配音字幕、分镜、视频合成
- **使用说明：** 需 Python、Node.js、FFmpeg 和编程 Agent；不同生产路线依赖不同模型或素材服务，README 也提供真实素材剪辑路线。
- **公开元数据：** 82,343 Stars · 11,217 Forks · 主要语言 Python · 许可证 `AGPL-3.0` · 未归档。
- **最近推送：** 2026-11-16T06:55:27Z；**星标时间：** 2026-10-13T02:22:20Z（UTC）。
- **归类依据：** README 介绍完整视频生产流程、参考视频分析和 Backlot 分镜看板；快速开始列明运行依赖，并区分真实素材剪辑与 AI 生成素材。 [查看官方文档](https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md)。

#### [browser-use/video-use](https://github.com/browser-use/video-use)

通过编程 Agent 剪辑已有素材，依据词级转录和按需视觉帧处理口头填充词、停顿、调色、字幕及动画覆盖层。

- **用途标签：** AI剪辑、口播剪辑、字幕、调色、Agent技能、FFmpeg
- **使用说明：** 本地 Python 工具配合 FFmpeg 和编程 Agent；README 当前转录流程需要 ElevenLabs Scribe API Key，可选 HyperFrames、Remotion 等动画工具。
- **公开元数据：** 31,436 Stars · 3,641 Forks · 主要语言 Python · 许可证 `MIT` · 未归档。
- **最近推送：** 2026-10-08T22:17:01Z；**星标时间：** 2026-10-10T07:25:40Z（UTC）。
- **归类依据：** README 的 What it does 列出删口头填充词、自动调色、字幕和动画叠加；How it works 说明词级转录与视觉时间线两层输入。 [查看官方文档](https://github.com/browser-use/video-use/blob/main/README.md)。

#### [hypit-ai/hypit](https://github.com/hypit-ai/hypit)

让编程 Agent 从参考视频、模板或文字需求建立可编辑的视频工作流，组合镜头、字幕、B-roll 和特效并制作变体。

- **用途标签：** Agent技能、视频工作流、短视频、字幕、代码动画、模板复用
- **使用说明：** 提供 Agent Skill 与本地运行工具；生成模型可选，纯代码动画可本地合成，外部视频或音频服务单独配置和计费。
- **公开元数据：** 31,077 Stars · 3,681 Forks · 主要语言 TypeScript · 许可证 `NOASSERTION` · 未归档。
- **最近推送：** 2026-11-20T10:08:47Z；**星标时间：** 2026-10-13T02:46:42Z（UTC）。
- **归类依据：** README 的 Hypit 与 What Hypit Can Build 章节说明可从参考视频、模板或描述起步，重跑和修改合成项目，并明确生成模型不是必选。 [查看官方文档](https://github.com/hypit-ai/hypit/blob/main/README.md)。

### 代码动画与可编辑视频（2）

#### [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

面向人和 AI Agent 的可编辑视频框架，把 HTML、CSS、JavaScript、媒体与可定位动画渲染为 MP4，适合产品演示、字幕和动效视频。

- **用途标签：** AI视频编辑、HTML视频、动效、Agent技能、MCP、视频渲染
- **使用说明：** 本地 CLI 需要 Node.js 和 FFmpeg，提供 Agent Skills 与 Studio 使用方式；使用外部生成模型或托管服务时按相应服务配置。
- **公开元数据：** 88,140 Stars · 8,202 Forks · 主要语言 TypeScript · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-22T16:31:59Z；**星标时间：** 2026-05-15T02:27:09Z（UTC）。
- **归类依据：** README 定义底层为 HTML/CSS/JavaScript 到确定性 MP4 的框架，列出编程 Agent、Studio 和 CLI 路径，以及无头 Chrome 加 FFmpeg 的渲染流程。 [查看官方文档](https://github.com/heygen-com/hyperframes/blob/main/README.md)。

#### [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart)

面向 Codex 的无限画布插件，可把提示词和参考图生成带分镜、运动及音效的 HTML/JS 动效影片，并预览、编辑和导出 MP4。

- **用途标签：** Codex、无限画布、分镜、动效影片、MP4
- **使用说明：** 以 Codex 插件/MCP widget 使用；AI 影片为 HTML/JS 动效工作流，不能据此等同于独立的视频扩散模型。
- **公开元数据：** 6,085 Stars · 455 Forks · 主要语言 JavaScript · 许可证 `MIT` · 未归档。
- **最近推送：** 2026-10-08T12:07:12Z；**星标时间：** 2026-07-09T01:36:19Z（UTC）。
- **归类依据：** README 功能清单明确包含 AI 影片、分镜/运动/音乐/音效、画布内预览、文字编辑及 MP4 导出。 [查看官方文档](https://github.com/zhongerxin/Cowart/blob/main/README.md)。

### 视频理解与镜头拆解（2）

#### [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V)

多模态模型系列，支持视频内容理解；仓库同时包含可接收连续音视频输入的 MiniCPM-o。

- **用途标签：** 视频理解、视觉语言模型、多模态、本地推理
- **使用说明：** 视频理解模型与推理代码，需要下载对应模型权重并选择兼容后端；不直接生成视频画面。
- **公开元数据：** 27,180 Stars · 2,130 Forks · 主要语言 Python · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-09T07:37:30Z；**星标时间：** 2026-05-13T05:37:33Z（UTC）。
- **归类依据：** README 的模型能力对照明确列出 MiniCPM-V 视频理解，以及 MiniCPM-o 接收音视频并生成文本/语音的实时多模态交互。 [查看官方文档](https://github.com/OpenBMB/MiniCPM-V/blob/main/README.md)。

#### [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)

为编程 Agent 拆解视频镜头、字幕、剪辑与音轨，输出 VIDEO.md、可读报告和按目标模型组织的重制计划。

- **用途标签：** 视频分析、镜头拆解、AI视频识别、字幕、重制规划、Agent技能
- **使用说明：** 需 Python 与 FFmpeg；可先用本地分析工具，视频理解模型为可选增强，后续生成工作流另依赖相应模型服务。
- **公开元数据：** 12,098 Stars · 1,787 Forks · 主要语言 Python · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-22T14:52:34Z；**星标时间：** 2026-11-12T06:00:54Z（UTC）。
- **归类依据：** README 的快速开始说明报告与 VIDEO.md 两种输出；视频类型表包含 AI 视频、数字人和代码动画，拆解覆盖字幕、剪辑及音轨，Remakes 章节说明重制计划。 [查看官方文档](https://github.com/JuneYaooo/rea-video/blob/main/README.md)。

### 视频增强与后处理（1）

#### [Baiyuetribe/paper2gui](https://github.com/Baiyuetribe/paper2gui)

AI 桌面工具箱，包含视频超分、RIFE/DAIN 补帧、无绿幕视频抠像和字幕相关工具。

- **用途标签：** 视频超分、补帧、抠像、桌面工具
- **使用说明：** 工具箱内各应用的系统支持、模型与维护情况不同，须按具体子工具核对；当前收录依据为官方说明，未安装运行验证。
- **公开元数据：** 10,693 Stars · 865 Forks · 主要语言 Jupyter Notebook · 许可证 `MIT` · 未归档。
- **最近推送：** 2024-09-20T05:57:52Z；**星标时间：** 2024-03-06T14:35:24Z（UTC）。
- **归类依据：** README 按视频超分、视频补帧、视频抠图分类列出 RealESRGAN、RIFE、DAIN、MODNet 等独立 GUI 工具。 [查看官方文档](https://github.com/Baiyuetribe/paper2gui/blob/main/README.md)。

## 配套工具（10）

### 综合创作工作台（1）

#### [nexu-io/open-design](https://github.com/nexu-io/open-design)

综合 AI 设计工作台，集成 HyperFrames 视频与产品动效模板，可由编程 Agent 生成并导出 MP4，也可接入视频生成模型。

- **用途标签：** 创作工作台、产品视频、HyperFrames、Agent集成、视频模板、MCP
- **使用说明：** 有桌面、Docker 与源码运行方式；属于多用途设计环境，视频是其中一条工作流，模型和编程 Agent 需按所用方案配置。
- **公开元数据：** 108,942 Stars · 12,329 Forks · 主要语言 TypeScript · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-22T04:19:58Z；**星标时间：** 2026-05-15T17:41:14Z（UTC）。
- **归类依据：** README 的 Studio 和 Video & HyperFrames 章节明确写明 Agent 动效制作与 MP4 导出，并给出产品宣传、字幕口播及图表动效模板。 [查看官方文档](https://github.com/nexu-io/open-design/blob/main/README.md)。

### 视频合成与渲染（2）

#### [remotion-dev/remotion](https://github.com/remotion-dev/remotion)

用 React 和网页技术以代码制作视频的框架，可作为 AI Agent 视频制作的合成、预览和批量渲染基础。

- **用途标签：** React、代码视频、视频合成、批量渲染、Agent技能
- **使用说明：** 需要 Node.js；本体属于可编程渲染框架，官方提供 Agent Skills 文档；README 提醒其采用特殊许可，部分公司使用情形需要另行取得许可。
- **公开元数据：** 74,920 Stars · 6,389 Forks · 主要语言 TypeScript · 许可证 `NOASSERTION` · 未归档。
- **最近推送：** 2026-11-20T21:05:57Z；**星标时间：** 2026-04-28T14:49:00Z（UTC）。
- **归类依据：** README 列出 Agent、交互与代码三种视频制作方式，提供 Agent Skills、字幕和渲染文档，并明确说明特殊许可。 [查看官方文档](https://github.com/remotion-dev/remotion/blob/main/README.md)。

#### [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)

多媒体命令行与库工具，可处理音视频编码、格式转换、滤镜、字幕与最终合成。

- **用途标签：** 视频合成、转码、滤镜、字幕、命令行
- **使用说明：** 通用视频基础工具，本身不提供 AI 生成模型；可作为其他 AI 视频项目的后处理和导出依赖。
- **公开元数据：** 67,947 Stars · 14,709 Forks · 主要语言 C · 许可证 `NOASSERTION` · 未归档。
- **最近推送：** 2026-11-22T16:21:22Z；**星标时间：** 2026-10-10T07:39:11Z（UTC）。
- **归类依据：** README 将 FFmpeg 定位为处理音频、视频、字幕和元数据的工具与库，并列出编解码、滤镜、混音、缩放及 ffmpeg/ffprobe。 [查看官方文档](https://github.com/FFmpeg/FFmpeg/blob/master/README.md)。

### 配音与音乐生成（3）

#### [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

本地 AI 语音工作台，支持视频翻译配音、声音克隆、声音设计和转写，可用于视频旁白与多语言制作。

- **用途标签：** 视频配音、语音克隆、转写、本地部署、TTS
- **使用说明：** 需要在模型管理器下载所需语音引擎；README 明确视频配音会按原始时间对齐。代码与模型权重的许可分别适用。
- **公开元数据：** 116,367 Stars · 12,948 Forks · 主要语言 Python · 许可证 `AGPL-3.0` · 未归档。
- **最近推送：** 2026-11-22T16:29:47Z；**星标时间：** 2026-10-09T05:39:54Z（UTC）。
- **归类依据：** README What you can do 中列出 Video dubbing，并描述视频翻译和与原始时间对齐的配音；同时列出本地模型管理、克隆、声音设计与转写。 [查看官方文档](https://github.com/debpalash/VoiceStudio/blob/main/README.md)。

#### [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)

文本转语音模型系列，支持多语言语音、声音设计与克隆，可为 AI 视频提供旁白和角色配音。

- **用途标签：** TTS、配音、声音设计、语音克隆
- **使用说明：** 输出音频，需另接剪辑/合成工具生成视频；本地推理需要安装依赖并下载模型权重。
- **公开元数据：** 42,874 Stars · 4,906 Forks · 主要语言 Python · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-09T07:36:59Z；**星标时间：** 2026-04-09T05:27:16Z（UTC）。
- **归类依据：** README 将 VoxCPM2 定位为多语言 TTS，描述文本生成语音、自然语言设计声音、参考音频克隆与音频输出。 [查看官方文档](https://github.com/OpenBMB/VoxCPM/blob/main/README.md)。

#### [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE)

歌曲与音乐生成项目，当前 YuE2 支持歌词/风格驱动、可编辑旋律和和弦规划，以及翻唱与音乐编辑。

- **用途标签：** 音乐生成、配乐、歌词生成歌曲、音频
- **使用说明：** 可用于视频配乐素材，项目本身输出音频；需独立准备模型权重和项目要求的推理环境。
- **公开元数据：** 13,667 Stars · 1,579 Forks · 主要语言 Python · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-01T05:46:34Z；**星标时间：** 2026-10-23T05:34:13Z（UTC）。
- **归类依据：** README 说明输入歌词与风格提示后先生成旋律/和弦规划，再合成人声与伴奏；另列歌曲编辑、乐谱编辑及器乐生成工作流。 [查看官方文档](https://github.com/multimodal-art-projection/YuE/blob/main/README.md)。

### 动作捕捉与动画素材（3）

#### [freemocap/freemocap](https://github.com/freemocap/freemocap)

动作捕捉系统与 GUI，可采集动作数据，为角色动画及相关视频制作提供动作素材。

- **用途标签：** 动作捕捉、角色动画、动作素材、Python
- **使用说明：** 属于动作数据采集环节，不是文生视频模型；按官方安装入口选择带 tracker 的 CPU/CUDA 依赖，具体采集设置另见原项目。
- **公开元数据：** 10,873 Stars · 1,047 Forks · 主要语言 TypeScript · 许可证 `AGPL-3.0` · 未归档。
- **最近推送：** 2026-11-14T23:04:11Z；**星标时间：** 2026-11-02T16:01:05Z（UTC）。
- **归类依据：** README 将项目定位为动作捕捉系统，提供图形界面与安装流程，并明确依赖用于跟踪的 skellytracker。 [查看官方文档](https://github.com/freemocap/freemocap/blob/main/README.md)。

#### [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge)

Agent 动画素材工具，通过母图生成动作视频，再抠像、抽帧、选择循环和重定时，导出可用于 Godot 等引擎的动画素材。

- **用途标签：** 图生视频、动画素材、抽帧、抠像、Agent Skills
- **使用说明：** 最终目标是游戏精灵和动画素材；需可用的视频生成服务/登录及 FFmpeg，不能把它当作独立短剧生成平台。
- **公开元数据：** 5,915 Stars · 578 Forks · 主要语言 Python · 许可证 `MIT` · 未归档。
- **最近推送：** 2026-11-13T01:41:03Z；**星标时间：** 2026-11-02T03:13:08Z（UTC）。
- **归类依据：** README 开头与 Make the sprite set 明确说明一个母图生成每动作一段图生视频，再用 video2dsprite 管线抽帧、质检、循环、重定时与打包。 [查看官方文档](https://github.com/0x0funky/agent-sprite-forge/blob/main/README.md)。

#### [aldegad/sprite-gen](https://github.com/aldegad/sprite-gen)

Codex/Claude 技能与 Python CLI，含单图生成动作视频、抽帧和自动循环裁切流程，输出透明 GIF、WebP 或条带动画。

- **用途标签：** 图生视频、透明动画、抽帧、循环动画、Agent Skills
- **使用说明：** 最终目标是游戏动画资产；视频管线需 FFmpeg、img2webp 及对应 Grok 登录或 API 配置。另有静态图集流程，不全部归为视频功能。
- **公开元数据：** 4,180 Stars · 445 Forks · 主要语言 Python · 许可证 `Apache-2.0` · 未归档。
- **最近推送：** 2026-11-21T12:10:32Z；**星标时间：** 2026-11-03T07:21:52Z（UTC）。
- **归类依据：** README 的 B·video→loop 流程明确为单张静图经 Grok Imagine 动画生成，再用 video-frames/video-loop 处理为透明循环；说明了所需本地工具和账号。 [查看官方文档](https://github.com/aldegad/sprite-gen/blob/main/README.md)。

### 剧本与分镜（1）

#### [Narcooo/inkos](https://github.com/Narcooo/inkos)

故事创作 Agent，包含独立的剧本与分镜 Skills 及生产管线，可作为 AI 短剧制作的前期内容工具。

- **用途标签：** 剧本、分镜、故事创作、角色一致性、Agent
- **使用说明：** 当前 README 明确支持剧本、分镜，但未据此认定可直接生成或导出完整视频；支持本地 Studio、TUI、CLI，并需配置所用模型服务。
- **公开元数据：** 11,387 Stars · 2,051 Forks · 主要语言 TypeScript · 许可证 `AGPL-3.0` · 未归档。
- **最近推送：** 2026-10-24T05:30:14Z；**星标时间：** 2026-04-21T14:07:43Z（UTC）。
- **归类依据：** README 的 InkOS 2.0 能力列表明确列出剧本、分镜独立 SKILL.md，以及各自状态模型、生产步骤、快照与恢复机制。 [查看官方文档](https://github.com/Narcooo/inkos/blob/main/README.md)。
