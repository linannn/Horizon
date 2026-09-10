---
layout: default
title: "Horizon 每日速递：2026-09-10"
description: "AI 精选的技术与研究日报"
date: 2026-09-10
lang: zh
locale: zh-CN
---

> 从 70 条内容中筛选出 7 条重要资讯。

---

1. [OpenAI Codex rust-v0.154.0 发布：新增实验性 worktree 与 GPT-6-Astra](#item-1) ⭐️ 7.0/10
2. [OpenAI Codex 负责人 Tibo Sottiaux 谈编程智能体的构建](#item-2) ⭐️ 7.0/10
3. [Mistral 复盘用 AI Agent 将 4 万行 Fortran 77 迁移到 C++](#item-3) ⭐️ 7.0/10
4. [OpenAI 发布 GPT-6 Astra，面向专业工作并公布 API 定价](#item-4) ⭐️ 7.0/10
5. [Mastra core 1.65.0 发布：新增高级链路查询与租户级删除](#item-5) ⭐️ 6.0/10
6. [Desert Ant Labs 发布 18 个端侧离线模型及 Swift、Kotlin、JS SDK](#item-6) ⭐️ 6.0/10
7. [OpenAI 称 Astra-next 约 1 万智能体 88 小时找到 Navier-Stokes 奇点](#item-7) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [OpenAI Codex rust-v0.154.0 发布：新增实验性 worktree 与 GPT-6-Astra](https://github.com/openai/codex/releases/tag/rust-v0.154.0) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 发布 Codex rust-v0.154.0，新增实验性 worktree 支持：新会话或分叉会话可通过 \`--worktree\` 或 \`/worktree\` 获得相互隔离的检出目录，并可浏览、恢复这些会话；同时支持在 Codex 继续工作的同时以内联方式回答提问，Windows 会话还可共享后台 Codex 服务器。该版本还让 GPT-6-Astra 出现在模型选择器和 Amazon Bedrock 目录中。 通过把隔离的并行会话、任务中途澄清提问和共享后台服务器变为一等能力，Codex 正把编码智能体从单线程对话推向同时管理多条并行工作流，这直接影响开发者把智能体接入日常代码仓库的方式。 需要注意，worktree 功能被明确标记为实验性；同时已弃用的 \`codex mcp-server\` 入口点在本版本中被移除，任何仍在调用它的脚本或配置都会失效，需要迁移。

github · github-actions\[bot\] · 9月9日 22:35

**背景**: Codex 是 OpenAI 的编码智能体项目，在 GitHub 上以 rust-v\* 形式的版本标签发布，本次版本紧接 rust-v0.153.0。worktree 一词源自 Git：同一个仓库可以同时挂载多个相互独立的工作目录，从而在不同分支上并行开发，而无需暂存改动或来回切换上下文。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/openai/codex/releases/tag/rust-v0.154.0">openai/codex released rust-v0.154.0</a></li>
<li><a href="https://github.com/openai/codex/releases">Releases · openai/codex</a></li>
<li><a href="https://git-scm.com/docs/git-worktree">Git - git - worktree Documentation</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Codex`, `#developer tools`, `#release`, `#worktree`

---

<a id="item-2"></a>
## [OpenAI Codex 负责人 Tibo Sottiaux 谈编程智能体的构建](https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux) ⭐️ 7.0/10

**级别**: 核心必看

《The Pragmatic Engineer》发布了主持人 Gergely Orosz 对 Tibo Sottiaux 的访谈，Tibo 是 Codex 的创建者之一，目前负责 OpenAI 的核心产品与平台（Core Products &amp; Platform）团队，Codex 也在其管理范围之内。本期节目讨论了 Codex 作为一个产品是如何起步的、为什么用 Rust 编写并开源，以及它正在如何改变软件开发的工作方式。 Codex 是目前使用最广泛的生产级编程智能体之一，因此其负责人亲自讲述架构设计与取舍，能为正在自研或引入智能体编程工具的团队提供具体参考，而不是停留在厂商宣传层面。 根据该期节目的简介，讨论中有一部分专门涉及 Codex 为什么选择用 Rust 编写并以开源方式发布，这说明访谈聚焦的是 CLI 背后的具体工程决策，而不只是产品层面的定位。

rss · The Pragmatic Engineer · 9月9日 15:57

**背景**: OpenAI 曾两次使用 Codex 这个名字：一是 2021 年基于 GPT-3、用来自 5400 万个 GitHub 仓库的 159 GB Python 代码训练出的代码模型；二是 2025 年 4 月以 Codex CLI 形式发布的独立编程智能体。如今的 Codex 可通过 ChatGPT 网页版、命令行工具、Windows 与 macOS 桌面应用以及多种 IDE 集成使用。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux">Building Codex with Tibo Sottiaux</a></li>
<li><a href="https://podscripts.co/podcasts/the-pragmatic-engineer/building-codex-with-tibo-sottiaux">The Pragmatic Engineer - Building Codex with Tibo Sottiaux ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28AI_agent%29">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#Codex`, `#OpenAI`, `#AI-engineering`, `#developer-tools`

---

<a id="item-3"></a>
## [Mistral 复盘用 AI Agent 将 4 万行 Fortran 77 迁移到 C++](https://mistral.ai/news/legacy-code-modernization) ⭐️ 7.0/10

**级别**: 核心必看

Mistral 的 Applied AI 团队发布了一篇复盘文章，介绍其如何借助 AI 编码 Agent，帮助一家欧洲能源运营商把一套 4 万行的 Fortran 77 储层模拟器迁移到 C++，而不是靠人工重写。文章同时梳理了所用的方法以及这次项目中的经验教训。 它提供了一个把编码 Agent 用于遗留系统现代化的大规模真实案例；在这一领域，多数企业仍依赖缓慢的人工重写，而单纯的语法转换早已被认为基本被解决。 被迁移的代码库没有测试套件，文档也散落在陈旧的 PDF 中；Mistral 把核心经验总结为“超越代码翻译”，也就是说这类项目真正的难点在于验证与语义等价，而非把语法从一种语言换成另一种语言。

rss · AI 热榜 · 9月9日 18:59

**背景**: Fortran 77 是 Fortran 于 1977 年发布的版本标准，这种编译型语言专为数值计算和科学计算设计，至今仍广泛用于高性能计算以及储层模拟器这类物理密集型仿真软件中。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mistral.ai/news/legacy-code-modernization">Mistral 复盘用 AI Agent 迁移 40000 行 Fortran 77 到 C++ 的经验</a></li>
<li><a href="https://ecosistemastartup.com/mistral-migra-40-000-lineas-de-fortran-a-c-con-agentes-de-ia/">Mistral migra 40.000 líneas de Fortran a C++ con agentes de IA – El Ecosistema Startup</a></li>
<li><a href="https://www.byteseu.com/2351175/">Modernizing complex legacy code with AI agents - Bytes Europe</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#coding agents`, `#legacy code migration`, `#Fortran`, `#Mistral AI`

---

<a id="item-4"></a>
## [OpenAI 发布 GPT-6 Astra，面向专业工作并公布 API 定价](https://openai.com/index/gpt-6-astra-next-generation-work) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 发布了面向专业工作场景的 GPT-6 Astra，并已在 ChatGPT Work、Codex 和 API 中提供，定价为每百万输入 token 10 美元、每百万输出 token 50 美元。第三方资料显示其首次发布是在 2026 年 9 月 3 日，最初以限量预览形式推出。 由于 Astra 同时在 Codex 和按量计费的 API 中提供，构建编码智能体或基于 API 工作流的团队需要重新评估模型选型和 token 成本，而 10 美元/50 美元的输出定价也会给其他前沿模型厂商带来压力，迫使它们解释自身定价的合理性。 需要注意的细节是：据报道 Astra 于 2026 年 9 月 3 日以限量预览起步，并在随后几天逐步扩展到更多 ChatGPT 订阅层级、Azure 和 AWS Bedrock；OpenAI 页面宣称其在 ARC-AGI-3 上取得 99.9%、在 ExploitBench 上取得 100%，但并未公布上下文窗口长度或相对上一代 GPT-5.6 Sol 的变更日志。

rss · AI 热榜 · 9月9日 11:00

**背景**: ChatGPT Work 是 OpenAI 面向团队协作的 ChatGPT 产品，Codex 是它的编程智能体，因此这两者都是 Astra 接入的既有产品入口，而非全新工具。GPT-6 Astra 是 OpenAI 继 GPT-5 系列之后的新一代模型，主打计算机操作、网页浏览、软件工程和网络安全研究等智能体式任务。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra-next-generation-work">OpenAI 发布 GPT-6 Astra，面向专业工作场景</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - 維基百科，自由的百科全書</a></li>

</ul>
</details>

**标签**: `#openai`, `#gpt-6`, `#model-release`, `#api-pricing`, `#codex`

---

## 更多动态

<a id="item-5"></a>
### [Mastra core 1.65.0 发布：新增高级链路查询与租户级删除](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.65.0) ⭐️ 6.0/10

@mastra/core@1.65.0 引入了可移植的“高级链路查询”契约，支持受限时间范围、可递归的 trace/span/score 谓词、按线程分组以及确定性的游标分页，并提供带鉴权的服务端端点，已在 ClickHouse、DuckDB 和 Postgres 中实现。该版本还新增租户级链路删除能力，单次请求最多可删除 1,000 个 trace ID，并级联清理 span 及与 trace 关联的信号，同时为 parallel、branch、循环、foreach、sleep、sleepUntil、map 等控制流块增加了可选的 id、description 和 metadata 字段。

github · PaulieScanlon · 9月9日 09:43

<a id="item-6"></a>
### [Desert Ant Labs 发布 18 个端侧离线模型及 Swift、Kotlin、JS SDK](https://desertant.com/blog/introducing-desert-ant-labs/) ⭐️ 6.0/10

欧洲前沿 AI 实验室 Desert Ant Labs 发布了 18 个面向音频、视觉和文本的小型专用端侧模型，任务涵盖语音转写、PII 脱敏、语言检测和视频剪辑等，并提供基于 Core ML、LiteRT 和 WebAssembly 的 Swift、Kotlin 与 JavaScript SDK。所有模型完全离线运行，月活跃设备在 10 万台以内免费使用，不计 token、无需登录。

hackernews · willwhitedc · 9月9日 11:39 · [社区讨论](https://news.ycombinator.com/item?id=49624823)

<a id="item-7"></a>
### [OpenAI 称 Astra-next 约 1 万智能体 88 小时找到 Navier-Stokes 奇点](https://www.latent.space/p/ainews-openai-reports-navier-stokes) ⭐️ 4.0/10

Latent Space 的 AINews 汇总以头条形式称，OpenAI 用一个名为 Astra-next 的系统在 88 小时内找到了 Navier-Stokes 方程的有限时间奇点，据称动用了约 1 万个协同智能体和 1300 亿 token，成本超过 4000 万美元。搜索结果中还出现了 OpenAI 的官方页面，称已公开该证明的书面说明以及 Lean 形式化，但 AINews 原文本身只是标题级预告，没有方法细节或可验证的测量结果。

rss · Latent Space · 9月9日 05:04