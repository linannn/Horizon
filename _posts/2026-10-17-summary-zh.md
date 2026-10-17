---
layout: default
title: "Horizon 每日速递：2026-10-17"
description: "AI 精选的技术与研究日报"
date: 2026-10-17
lang: zh
locale: zh-CN
---

> 从 58 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Cline SDK v0.0.94 移除进程内插件模式并修复流式重试预算翻倍问题](#item-tech-news-1) ⭐️ 7.0/10
2. [Goose v1.55.0 发布：新增 AIgateway 路由与 W3C 追踪传播](#item-tech-news-2) ⭐️ 7.0/10
3. [Apple 在四台 Mac Studio 集群上以 MLX 运行约 1 万亿参数 Muse Spark Open](#item-tech-news-3) ⭐️ 5.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Cline SDK v0.0.94 移除进程内插件模式并修复流式重试预算翻倍问题](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.94) ⭐️ 7.0/10

**级别**: 核心必看

Cline SDK v0.0.94 强化了插件隔离机制：彻底移除 \`CLINE\_PLUGIN\_MODE=in\_process\` 模式，插件只能在默认的 worker 线程或 \`sandbox\` 子进程中运行；若宿主未提供 \`plugin-sandbox-bootstrap.js\`，插件加载将以 \`PluginBootstrapMissingError\` 失败并提示 \`CLINE\_PLUGIN\_BOOTSTRAP\_PATH\`，不再静默回退到 hub 内执行。该版本修复了模型流中断后的重试预算翻倍问题——流开始后出现的 provider 错误最多重试 3 次，最终失败记录到日志与 Langfuse trace，不再额外触发整轮 agent 重试。失败请求日志新增 provider request id 用于排查，并新增 \`setHubDaemonLauncher\`、\`ensureDetachedHubServer\`（含 \`beforeSpawn\` 钩子）、\`NodeHubClient.resolveConnectionHeaders\` 等面向嵌入宿主的 API。\`AskQuestionExecutor\` 现可返回文本与图像块，\`@cline/shared\` 导出 \`buildTelemetrySelfcheckReport\`。模型目录从 6,862 扩展到 6,952 条，新增 Boundless、Standard Compute 两个 provider，SambaNova 默认模型改为 MiniMax M3；Cline provider 默认模型从 Claude Sonnet 5.5 改为 Gemini 4 Argon，多家 provider 的默认模型同步变更。

github · github-actions\[bot\] · 10月16日 03:51

**「背景」** Cline 是面向 IDE 与终端的 AI 编程助手，其 SDK 让宿主应用通过 hub 守护进程集成模型调用、插件加载与远程运行时。插件执行通过 \`CLINE\_PLUGIN\_MODE\` 环境变量选择隔离级别——\`worker\`（默认，插件运行在独立工作线程中）与 \`sandbox\`（独立子进程）——此前的 \`in\_process\` 模式意味着插件与 hub 共用同一进程，缺乏任何隔离，因此宿主若未提供 \`plugin-sandbox-bootstrap.js\`，插件会直接跑在 hub 内部。

**「影响与迁移」** 依赖 \`in\_process\` 插件模式或基于 hub 静默回退加载插件的宿主页必须升级配套的 \`plugin-sandbox-bootstrap.js\`，否则插件工具将全部报错；SSH remote hub 因尚未提供 bootstrap，相关插件工具会显示缺失。修复后的重试逻辑可避免长任务在网络抖动时被一次 provider 错误消耗 3×N 次调用预算。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.94">cline/cline released sdk/sdk/v0.0.94</a></li>

</ul>
</details>

**标签**: `#ai-coding-agent`, `#cline`, `#sdk-release`, `#plugin-sandbox`, `#error-handling`

---

<a id="item-tech-news-2"></a>
### [Goose v1.55.0 发布：新增 AIgateway 路由与 W3C 追踪传播](https://github.com/aaif-goose/goose/releases/tag/v1.55.0) ⭐️ 7.0/10

**级别**: 核心必看

Goose v1.55.0 是该开源 AI 编码代理的一次功能性更新。该版本新增 AIgateway 声明式 provider 路由、从 ACP prompt 到 MCP 工具调用的 W3C trace context 传播，并优先使用 OpenAI Responses API 及其实时模型元数据；自动压缩的默认上限被调整为 225k tokens。Bug 修复部分包括为 Claude Sonnet 和 Haiku 5.5 加入自适应思考支持、Bedrock converse\_stream 上非上下文 ValidationException 不再被重试，以及 OpenRouter 不再无条件设置 transforms 字段；同时对响应/错误暴露了 provider 的 x-request-id。

github · github-actions\[bot\] · 10月16日 16:58

**「背景」** Goose 是一个支持通过 MCP（Model Context Protocol）等协议与外部工具交互的开源 AI 编码代理；ACP 是 Goose 在代理会话之间传递 prompt 的协议，与面向工具调用的 MCP 形成上下游关系。W3C trace context 是 W3C 制定的分布式追踪上下文传播规范，可将同一条请求在多个服务或调用中产生的追踪记录关联到同一条 trace 上。Auto-compaction 是 Goose 在会话上下文接近模型窗口上限时自动压缩对话历史的机制，其默认 token 阈值决定了长会话在何时被压缩。

**「对使用者的影响」** 对开发者而言，AIgateway 声明式路由降低了多 provider 配置的维护成本，W3C trace context 从 ACP 透传到 MCP 使得跨协议的工具调用可接入统一的可观测性体系。225k tokens 的自动压缩默认上限以及长上下文价格分层计费的引入，会直接影响大上下文会话的成本估算和压缩触发时机；自定义 provider 模型现在会遵循其声明的 supports\_vision，避免视觉能力被误判。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/aaif-goose/goose/releases/tag/v1.55.0">aaif-goose/goose released v1.55.0</a></li>

</ul>
</details>

**标签**: `#ai-coding-agent`, `#mcp`, `#developer-tools`, `#release-notes`, `#open-source`

---

### 更多动态

<a id="item-tech-news-3"></a>
#### [Apple 在四台 Mac Studio 集群上以 MLX 运行约 1 万亿参数 Muse Spark Open](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 5.0/10

Apple 在其机器学习研究博客中演示，通过今日发布的新版 MLX 框架，在四台 Mac Studio 组成的集群上运行参数量约 1 万亿的 Muse Spark Open 模型，单机起步配置最高 512GB 统一内存。博客声称该集群生成速度超过每秒 36 个 token，并以人类平均阅读速度作为对比参照；用于测量的上下文窗口为 8192 token。该结果来自厂商发布的研究博客，属于 Apple 自家基准，而非独立验证；博客未公开精度、功耗或多模型同条件对比等细节。

hackernews · antipaul · 10月16日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)