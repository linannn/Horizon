---
layout: default
title: "Horizon 每日速递：2026-09-22"
description: "AI 精选的技术与研究日报"
date: 2026-09-22
lang: zh
locale: zh-CN
---

> 从 58 条内容中筛选出 8 条重要资讯。

---

1. [小米以 MIT 许可开源 MiMo-V2.6 Pro 与 Flash 两款 MoE 模型](#item-1) ⭐️ 7.0/10
2. [xAI 发布 Grok 4.7，速度与定价引发热议](#item-2) ⭐️ 7.0/10
3. [Cloudflare Python Workers 正式 GA，可在边缘运行 Python](#item-3) ⭐️ 7.0/10
4. [TypeSafe AI 发布 Jev：输出类型化概率决策而非文本](#item-4) ⭐️ 7.0/10
5. [GitHub Copilot CLI v1.0.88-0 发布：新增终端通知与 MCP 修复](#item-5) ⭐️ 5.0/10
6. [GitHub Copilot CLI v1.0.87 新增 worktree 路径模板与提示召回](#item-6) ⭐️ 4.0/10
7. [OpenRouter 解读 NVIDIA Nemotron 3.5 Lightning 的 Agent 高频调用定位](#item-7) ⭐️ 4.0/10
8. [Linear 重构 CI 流程，应对 AI 编码带来的验证瓶颈](#item-8) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [小米以 MIT 许可开源 MiMo-V2.6 Pro 与 Flash 两款 MoE 模型](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 7.0/10

**级别**: 核心必看

小米正式发布并开源 MiMo-V2.6 系列两款原生全模态混合专家（MoE）模型：Flash 为 309B 总参数／15B 激活参数，Pro 为 1.02T 总参数／42B 激活参数，均采用 MIT 许可。在 Code Arena 的 WebDev 榜单上，Pro 以 1628 分（AutoEval）位列约第 10 名、开源权重模型中约第 3 名，相比 MiMo-V2.5-Pro 的 1475 分提升 153 分。 这款以 MIT 许可开放权重、支持 1M token 上下文的模型，在多数 Agent 基准上被认为可与 Claude Opus 5 和 GPT-5.6 Sol 相当，并在 Artificial Analysis 智能指数上位居开源模型首位，为开发者提供了成本更低的开放选择，也凸显出中国实验室在开放权重赛道上的领先势头。 由于采用稀疏 MoE 架构，每个 token 实际只经过 Flash 的 15B 或 Pro 的 42B 激活参数，而非标称的 309B／1.02T，因此推理成本取决于激活参数量而非模型的总规模。

hackernews · volf\_ · 9月21日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: 混合专家（MoE）模型把网络拆分为大量专门的子网络，每个 token 只被路由到其中少数几个，从而在控制单次推理算力的同时大幅扩展总参数量。“开放权重”指训练好的参数可以下载，但并不等于训练数据和训练代码也一并公开。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">Xiaomi MiMo v2.6</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo Home</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上约 500 个赞的讨论高度聚焦于小米在训练透明度上的罕见做法，包括训练期间的实时仪表盘和一份被评论者称为极佳教学材料的详细技术报告。不少人表示如今对中国的模型比美国的更感兴趣，主要理由是价格更实惠；也有人贴出 Flash 与 Pro 的 RL 权重 Hugging Face 链接，并调侃这些模型偏爱“01 - UPPERCASE TEXT”式的前端设计套路。

**标签**: `#AI models`, `#open-source AI`, `#Xiaomi MiMo`, `#LLM`, `#MoE`

---

<a id="item-2"></a>
## [xAI 发布 Grok 4.7，速度与定价引发热议](https://x.ai/news/grok-4-7) ⭐️ 7.0/10

**级别**: 核心必看

xAI 发布了 Grok 4.7，这是一款面向编程、智能体任务和知识工作的前沿模型，具备 50 万 token 上下文窗口，并搭载一整套全新的安全防护栈，官方称其是迄今在拒答与抗越狱方面最强的模型。社区评论者称，此次发布比原定日期晚了约两周，且恰在 Anthropic 传闻中的 Opus 5.5 发布前一天推出。 此次发布恰逢 Anthropic 下一代模型即将登场，进一步加剧了前沿模型之间的竞争，迫使为编程和智能体工作流选型的开发者，在 Grok 4.7 被指出的速度变慢与更耗 token 等问题，和其基准成绩与安全性提升之间进行权衡。 实际提升幅度小于标题给人的印象：Artificial Analysis 测得 Grok 4.7 在 AA-Omniscience 上的准确率与 Grok 4.6 基本持平，为 47% 对 48%，尽管其幻觉率从 34% 降至 29%；同时该模型在 Intelligence Index 每项任务上平均耗时约 7.1 分钟。

hackernews · meetpateltech · 9月21日 15:50 · [社区讨论](https://news.ycombinator.com/item?id=49788838)

**背景**: Grok 是 xAI 的大语言模型系列，自 Grok 4.5 起，这些模型便与 Cursor 团队共同开发，而 xAI 正将 Cursor 这一编程工具纳入麾下。Grok 4.7 是 Grok 4.6 的直接后继版本。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-7">Grok 4.7</a></li>
<li><a href="https://artificialanalysis.ai/articles/benchmarking-grok-4-7">Benchmarking Grok 4.7 | Artificial Analysis</a></li>
<li><a href="https://docs.x.ai/developers/grok-4-7">Grok 4 . 7 | SpaceXAI Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Grok 4.7 的权重 reportedly 比 Grok 4.6 多约 40%，价格却保持不变，发布时间晚了近两周，使用起来更慢也更贵，有开发者怀疑它是“靠狂烧 token 来把基准分数拉上去”。多人质疑基准分数能否反映真实可用性，称 Grok 4.6 在其编程和智能体用例中不合格，而 Sol/Opus 仍高于某种“智能门槛”；不过也有人欢迎更快的发布节奏，并期待 Grok 5 带来更大提升。

**标签**: `#Grok 4.7`, `#AI models`, `#coding agents`, `#xAI`, `#benchmarks`

---

<a id="item-3"></a>
## [Cloudflare Python Workers 正式 GA，可在边缘运行 Python](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 7.0/10

**级别**: 核心必看

Cloudflare 宣布 Python Workers 正式进入 GA（一般可用）阶段，经过约两年的预览期后，Python 成为其开发者平台上被完整支持的一等语言。开发者可以在 Workers 运行时中通过 Pyodide/WebAssembly 原生运行 FastAPI、Django、Flask 等 Python Web 框架以及 AI 编排库，并直接调用 D1、R2 和 Workers AI 等服务，无需编写 JavaScript 胶水代码。 这为以 Python 为主的团队和 AI 工程师提供了一条受生产支持、且无需脱离自身语言生态的边缘部署路径，可用于部署 Python 服务与智能体编排逻辑，也让 Workers 不再局限于 JavaScript/TypeScript。 Workers 上的 Python 打包方式已通过 PEP 783（PyEmscripten）实现标准化，而 Requests 的客户端支持依赖于 urllib3 上游此前加入的 Pyodide/Emscripten 支持以及后续的 JSPI 支持；据一位 urllib3 维护者说明，这些补丁的资助给到了实际实现它们的外部贡献者，而非维护者本人。

hackernews · Cloudflare AI · 9月21日 13:38 · [社区讨论](https://news.ycombinator.com/item?id=49787142)

**背景**: Cloudflare Workers 是一个在 Cloudflare 全球边缘网络上运行代码的无服务器平台，此前主要面向 JavaScript 和 TypeScript。Python Workers 的实现方式是通过 Pyodide 项目运行编译为 WebAssembly 的 CPython，因此仍需遵循面向 WebAssembly 的打包工具链及其限制。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.cloudflare.com/python-workers-ga/">Python Workers are now generally available</a></li>
<li><a href="https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/">Cloudflare Python Workers are now generally available</a></li>
<li><a href="https://www.technobezz.com/news/cloudflare-python-workers-general-availability">Cloudflare Makes Python Workers Generally Available | Technobezz</a></li>

</ul>
</details>

**社区讨论**: 一位 urllib3 维护者澄清了上游历史：Pyodide/Emscripten 补丁以及后来的 JSPI 支持是几年前合入的，相关资助给到了实现这些工作的外部贡献者，而不是 urllib3 的维护者。Wasmer 创始人 Syrus Akbary 虽然承认自己所在公司有竞争产品，但仍称赞了这次进展，尤其是 PyEmscripten 通过 PEP 783 实现标准化，不过他表示首次发布讨论中提出的一些架构层面的担忧依然存在。其余评论多为玩笑或一两句话，其中包括希望未来 Go 在该平台上也能同样易用。

**标签**: `#cloudflare-workers`, `#python`, `#serverless`, `#webassembly`, `#ai-orchestration`

---

<a id="item-4"></a>
## [TypeSafe AI 发布 Jev：输出类型化概率决策而非文本](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 7.0/10

**级别**: 核心必看

TypeSafe AI 发布了 Jev，这是其称为“System One 模型”（Simon Willison 与 Maggie Appleton 更倾向称之为“decision models”，即决策模型）这一新模型类别的首个实例：它接收文本或半结构化的“state”输入以及一个或多个类型化问题，只返回浮点数——针对是/否的“Noul”问题返回伯努利式概率，针对选择问题返回一个置信度分数加上各选项的概率分布，针对评分问题则在给定数值区间内返回一个分数。其技术栈包含新的模型架构、并行采样器，以及一种名为“面向校准决策的强化学习”（RLCD）的训练方法，并且只对输入计费，价格为每百万 token 0.042 美元，输出 token 免费。 一种快速且极其廉价、直接返回机器可用的类型化概率决策而非自然语言的接口，可能让“判断”成为智能体流水线中的常规基础能力——路由、门控、打标与排序——而不再依赖脆弱的“提示再解析”步骤。 Jev 完全不提供自然语言解释——返回的只是一个浮点数——因此 Simon Willison 警告说，它的错误以及可能内置的偏见实际上难以审计，他特别表示希望没有人用它来给求职者排序。

rss · Simon Willison · 9月21日 23:09

**背景**: 传统 LLM（TypeSafe 将其称为“System Two”模型）会逐 token 生成文本，供人阅读，或需要程序再解析。System One 模型则完全跳过文本生成，直接返回代码可在 if 判断、路由表或排序函数中直接使用的值。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/21/jev/">Jev introduces a new shape of LLM - System One, aka Decision Models</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI’s System One Model</a></li>

</ul>
</details>

**社区讨论**: 相关讨论中最主要的争议是命名：Maggie Appleton 提出“decision models”（决策模型）这一说法，Simon Willison 也认为它比“System One 模型”更贴切；同时 TypeSafe 的 CEO 在 Hacker News 上确认“Noul”是伯努利（Bernoulli）的缩写。除此之外，社区反应总体是感兴趣的，但也对该设计所代表的“黑箱化”方向保持警惕。

**标签**: `#llm`, `#decision-models`, `#ai-agents`, `#model-architecture`, `#ai-engineering`

---

## 更多动态

<a id="item-5"></a>
### [GitHub Copilot CLI v1.0.88-0 发布：新增终端通知与 MCP 修复](https://github.com/github/copilot-cli/releases/tag/v1.0.88-0) ⭐️ 5.0/10

GitHub 发布 Copilot CLI v1.0.88-0，新增面向 Ghostty 和 WezTerm 直连会话的可选 OSC 777 终端通知，在技能发现中支持带命名空间的自定义技能和被忽略的技能目录，并在 MCP 与插件视图中显示服务器显示名称和插件描述。该版本还在恢复大型本地会话时限制了 transcript 内存占用，允许在活跃回合中运行 /fork，并让企业管理设置首次作用于通过 ACP 模式（\`copilot --acp\`）、AHP 宿主（\`copilot --ahp-host\`）以及已发布的 \`--server\` 会话启动的会话。

github · copilot-cli-release-app\[bot\] · 9月21日 18:44

<a id="item-6"></a>
### [GitHub Copilot CLI v1.0.87 新增 worktree 路径模板与提示召回](https://github.com/github/copilot-cli/releases/tag/v1.0.87) ⭐️ 4.0/10

GitHub 于 2026-09-21 发布 Copilot CLI v1.0.87，新增可配置的 \`worktreePathTemplate\` 设置，用于决定 \`/worktree\`、\`/move\`、\`/new\` 和 \`--worktree\` 在哪里创建工作树（例如 \`~/src/worktrees/\{repo\}/\{branch\}\`，支持 \`\{repoPath\}\`、\`\{repo\}\`、\`\{branch\}\` 和 \`\{branchSlug\}\` 占位符）。同一版本还为 Auto 路由层新增用户级与受管启动默认值（含强制策略和允许用户覆盖的组织策略），并允许开发者在空聊天输入框中按上方向键，召回已合并为一条待发送消息的连续 steering 提示，以便编辑。

github · copilot-cli-release-app\[bot\] · 9月21日 15:31

<a id="item-7"></a>
### [OpenRouter 解读 NVIDIA Nemotron 3.5 Lightning 的 Agent 高频调用定位](https://openrouter.ai/blog/insights/nemotron-3-5-lightning) ⭐️ 4.0/10

OpenRouter 发文解读 NVIDIA 的 Nemotron 3.5 Lightning：这是一款总参数 30B、激活参数约 3B 的混合专家开源权重模型，定位于工具调用、编码等高频且边界清晰的 Agent 执行步骤。文章将其与负责复杂推理的 Nemotron 3 Ultra（总参数 550B、激活参数 55B）描述为分工关系。

rss · AI 热榜 · 9月22日 00:00

<a id="item-8"></a>
### [Linear 重构 CI 流程，应对 AI 编码带来的验证瓶颈](https://linear.app/now/ci-bottleneck-reworked) ⭐️ 4.0/10

Linear 工程师分享了他们如何重构 CI 流程：在 AI Agent 加快代码产出后，持续集成反而成了瓶颈，改造后 PR 等待时间从 6 分钟以上降到 5 分钟出头，单元测试 runner 耗时约减半。

rss · AI 热榜 · 9月21日 12:26