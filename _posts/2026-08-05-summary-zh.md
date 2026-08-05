---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 47 条内容中筛选出 11 条重要资讯。

---

1. [LLM 0.32 新增推理痕迹、服务端工具和 Responses API 支持](#item-1) ⭐️ 8.0/10
2. [解析 ChatGPT Work：对其智能体架构的外部重构](#item-2) ⭐️ 8.0/10
3. [Cloudflare 推出 Agent 开发生命周期及全新原语](#item-3) ⭐️ 8.0/10
4. [Astro 用 AI 软件工厂将 GitHub 问题数削减 85%](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4 Flash 可在单块 AMD MI300X 上运行，速度超 150 tokens/s](#item-5) ⭐️ 7.0/10
6. [llm-anthropic 0.26 新增 Claude 5 模型与服务器端工具](#item-6) ⭐️ 7.0/10
7. [CEO 花 1.3 万美元用 Codex，称“自动化是个谎言”](#item-7) ⭐️ 7.0/10
8. [Claude Code v2.1.222 补丁修复工作树隔离与钩子绕过等问题](#item-8) ⭐️ 6.0/10
9. [Pydantic AI v2.23.0 新增成本追踪与工具可用性更新](#item-9) ⭐️ 6.0/10
10. [Copilot CLI v1.0.79-1 重命名沙箱设置并修复问题](#item-10) ⭐️ 5.0/10
11. [GitHub Spark 将于 2026 年 8 月 31 日前在 github.com 上停用](#item-11) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [LLM 0.32 新增推理痕迹、服务端工具和 Responses API 支持](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

**级别**: 核心必看

Simon Willison 发布了 LLM 0.32，这是该项目自首次发布以来最重要的一次更新，新增了可见的推理痕迹、服务端提供方工具，以及对 OpenAI Responses API 的支持。该版本还加入了 GPT-5.6 模型系列和重新设计的内容寻址 SQLite 日志系统。 LLM 是一个被广泛采用的命令行工具和 Python 库，用于与大型语言模型交互，因此这些功能直接影响 AI 工程工作流。能够查看推理痕迹和使用服务端工具，使该工具在智能体应用和调试方面更加强大。 用户可以通过新增的 -R/--hide-reasoning 参数隐藏推理痕迹，并可直接在命令行中调用 OpenAI 的 CodeInterpreter 和 WebSearch 等服务端工具。更新后的 llm-anthropic 插件新增了 WebSearch、WebFetch、CodeExecution 和 AnthropicMCP 工具，而新的“llm openai endpoint”命令可针对任何兼容 OpenAI 的端点执行一次性提示，且不记录日志。

rss · Simon Willison · 8月4日 23:58

**背景**: LLM 是 Simon Willison 创建的命令行工具和 Python 库，用于对各种大语言模型运行提示，包括远程 API 和本地安装的模型。推理痕迹是推理模型在给出答案之前生成的内部“思维链”输出。服务端工具允许模型使用由提供商托管的功能，如代码执行或网络搜索。内容寻址存储根据内容而非位置来组织数据，从而改进去重和完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm.datasette.io/">LLM: A CLI utility and Python library for interacting with Large Language Models</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content-addressable_storage">Content - addressable storage - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#OpenAI Responses`, `#reasoning traces`, `#CLI tools`, `#developer tools`

---

<a id="item-2"></a>
## [解析 ChatGPT Work：对其智能体架构的外部重构](https://www.latent.space/p/unpacking-chatgpt-work) ⭐️ 8.0/10

**级别**: 核心必看

一篇外部技术分析重构了 ChatGPT Work 的智能体功能的设计与实现，涵盖记忆、主动性、日程安排、浏览器使用、插件、技能和工具。这不是 OpenAI 的官方公告，而是一份独立工程深度分析，探讨该产品在底层可能如何运作。 由于 ChatGPT Work 被定位为面向十亿用户的智能体，理解其架构可以为 AI 编程工具和智能体工程提供具体且可复用的洞察。这项重构有助于开发者和产品团队从这一重要的真实世界智能体系统中学习，并将类似模式应用到他们自己的工作中。 该分析明确涵盖了记忆、主动性、日程安排、浏览器使用、插件、技能和工具，并把这些视为 ChatGPT Work 智能体的核心组件。由于这是一次外部重构，结论基于观察与推断，而非官方内部文档，因此部分实现细节可能只是近似描述。

rss · Latent Space · 8月4日 18:20

**背景**: ChatGPT Work 是 OpenAI 推出的智能体工作产品，于 2026 年 7 月发布，基于 GPT-5.6 构建，旨在跨应用和文件采取行动、自动化任务，并将目标转化为完成的工作。在 AI 智能体系统中，记忆是一个关键的架构问题，通常分为短期记忆和长期记忆；浏览器使用框架则让智能体能够以编程方式与网页交互。这份外部分析所处的大背景是，业界对真实智能体产品如何管理长时间运行任务、工具使用和主动行为越来越感兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://openai.com/index/chatgpt-for-your-most-ambitious-work/">ChatGPT is now a partner for your most ambitious work</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agent-memory">What Is AI Agent Memory? | IBM</a></li>

</ul>
</details>

**标签**: `#ChatGPT Work`, `#AI agents`, `#agent architecture`, `#browser automation`, `#product analysis`

---

<a id="item-3"></a>
## [Cloudflare 推出 Agent 开发生命周期及全新原语](https://blog.cloudflare.com/agent-development-lifecycle/) ⭐️ 8.0/10

**级别**: 核心必看

今日，Cloudflare 正式推出 Agent 开发生命周期（ADLC），这是一个用于构建、部署和维护 AI 代理的完整框架。配套的 Cloudflare 原语包括 Agents SDK，具备内置记忆、调度、邮件处理和实时通信功能，以及 AI Search 搜索原语。 这很重要，因为 AI 编码代理生成代码的速度已经超过团队审查、部署和维护的速度，而 ADLC 正是为了解决这一瓶颈。这标志着 Cloudflare 将代理视为平台的一等客户，并可能重新定义开发者构建和运维 AI 驱动工作流的方式。 ADLC 用代理为中心的流程取代了传统的软件开发生命周期（SDLC）。Cloudflare 将代理视为其客户：代理可以购买域名、创建临时账户并使用整个 Cloudflare API；Agents SDK 提供记忆、调度、邮件处理和实时通信，AI Search 则为代理搜索提供混合检索和相关性增强。

rss · Cloudflare AI · 8月4日 13:00

**背景**: Cloudflare 的开发平台包括 Workers（无服务器执行环境）和 Agents SDK，后者允许开发者构建有状态的 AI 代理。AI 代理是能够自主执行任务（如编写代码）而不需要人类持续指导的程序，管理它们需要从开发到监控的完整生命周期。Cloudflare 现在将 Agent 开发生命周期（ADLC）定位为 SDLC 的继任者，并借助 AI Search、内置代理记忆等原语来支持这一新范式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/agents/runtime/lifecycle/">Lifecycle · Cloudflare Agents docs</a></li>
<li><a href="https://www.cloudflare.com/products/agents/">Cloudflare Agents - Build Stateful AI Agents</a></li>
<li><a href="https://blog.cloudflare.com/ai-search-agent-primitive/">AI Search: the search primitive for your agents</a></li>

</ul>
</details>

**标签**: `#agent development`, `#cloudflare`, `#coding agents`, `#AI infrastructure`, `#agent lifecycle`

---

<a id="item-4"></a>
## [Astro 用 AI 软件工厂将 GitHub 问题数削减 85%](https://blog.cloudflare.com/astro-issue-triage/) ⭐️ 8.0/10

**级别**: 核心必看

Astro 维护者构建了一个软件工厂，利用运行在 GitHub Actions 中的隔离 AI 子代理来自动化问题复现和补丁验证，将未解决问题数量减少了 85%。这一方法用自动化流水线取代了手动问题分类。 这是一个 AI 代理实际处理开源维护工作的具体且可衡量的例子，展示了大幅减轻维护者负担的路径。它可能会启发其他项目在 CI/CD 中采用类似的代理驱动工作流。 该架构使用隔离在 GitHub Actions 中的 AI 子代理来执行自动化 bug 复现、补丁验证和预览发布。文章详细说明了这些子代理是如何编排的，可能包含特定任务的提示词和验证步骤。

rss · Cloudflare AI · 8月4日 13:00

**背景**: 软件工厂是一种有组织的软件开发方法，为团队提供可重复、明确定义的路径来创建和更新软件。AI 子代理是为特定任务设计的专用 AI 助手，它们可以集成到 CI/CD 流水线中来自动化复杂工作流。这条新闻将这两个概念应用于开源问题分类——这历来是维护工作中劳动密集的部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software_factory">Software factory - Wikipedia</a></li>
<li><a href="https://www.vmware.com/topics/software-factory">What’s a software factory? | VMware</a></li>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#issue triage`, `#GitHub Actions`, `#Astro`, `#automation`

---

<a id="item-5"></a>
## [DeepSeek V4 Flash 可在单块 AMD MI300X 上运行，速度超 150 tokens/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 7.0/10

**级别**: 核心必看

ryanzhou 的 GitHub 仓库展示了如何在单块 AMD MI300X 上运行 DeepSeek V4 Flash，在将上下文窗口从完整的 100 万 token 缩减到 25.6 万 token 后，实现了每秒超过 150 token 的生成速度。 这表明大型 MoE 推理模型可以在单块高显存 GPU 上高效运行，降低了自托管 DeepSeek 最新模型所需的硬件门槛。上下文长度与速度之间的取舍，为计划进行本地或边缘推理部署的人提供了实用的参考数据。 DeepSeek V4 Flash 原生支持 100 万 token 的上下文窗口，因此 25.6 万 token 是刻意缩减，以便适配单卡显存并维持高吞吐。仓库注释中提供了技术细节，作者还在 README 中引用了此前在 2 块 MI300X 上完成的相关工作。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是 DeepSeek V4 系列的预览版本，采用混合专家（MoE）架构，总参数量 2840 亿、激活参数量 130 亿，面向 100 万 token 上下文窗口设计高效推理。AMD MI300X 属于 AMD Instinct 数据中心 GPU 产品线，在 AI 推理和高性能计算领域与 Nvidia 的数据中心 GPU 直接竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek - v 4 - flash</a></li>
<li><a href="https://en.wikipedia.org/wiki/Amd_MI300X">Amd MI300X</a></li>

</ul>
</details>

**社区讨论**: 有评论者指出，MI300X 通常不单独零售，而是以约 25 万欧元的 8 卡整机形式出售；同时，由于模型采用 MXFP4 量化，PCIe 接口、144GB 显存的 MI350P 也能运行该模型。还有人提到了 2xMI300X 博客和 DwarfStar 项目等先前工作，另有人评论说缩减到 25.6 万 token 上下文是很实用的取舍，因为在该范围内模型质量仍然保持得不错。

**标签**: `#AMD MI300X`, `#DeepSeek V4 Flash`, `#LLM inference`, `#GPU optimization`, `#open-source`

---

<a id="item-6"></a>
## [llm-anthropic 0.26 新增 Claude 5 模型与服务器端工具](https://simonwillison.net/2026/Aug/4/llm-anthropic/#atom-everything) ⭐️ 7.0/10

**级别**: 核心必看

llm-anthropic 0.26 版本新增了三个 Claude 5 模型（claude-fable-5、claude-sonnet-5、claude-opus-5）和四个服务器端工具（WebSearch、WebFetch、CodeExecution、AnthropicMCP）。这些工具可通过 LLM 的 -T 接口或 Python tools= 参数使用，取代了原先的 -o web\_search\* 选项。 该版本将 Anthropic 最新的 Claude 5 模型引入 LLM 命令行工具，并让用户无需管理执行代码即可运行服务器端工具。这简化了代理工作流的构建，并加强了 LLM 与 Model Context Protocol 生态的集成。 Claude 5 模型默认进行思考；-o thinking 0 可关闭 Sonnet 5 和 Opus 5 的思考，而 Fable 5 始终思考。更新还将扩展思考简化为 thinking 和 thinking\_effort 选项，移除了多个旧选项，并默认将推理输出到标准错误，除非传入 -R/--hide-reasoning。

rss · Simon Willison · 8月4日 22:00

**背景**: Model Context Protocol（MCP）是 Anthropic 推出的开放标准，让 AI 应用通过统一接口连接外部数据源、工具和工作流。LLM 是一个用于访问大语言模型的命令行工具，-T/--tool 选项可将插件提供的工具添加到提示词中。WebSearch 和 CodeExecution 等服务器端工具在 Anthropic 的基础设施上运行，无需用户处理执行即可直接返回结果。该版本要求 LLM 0.32，后者引入了工具调用与结果的类型化事件流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview">Tool use with Claude - Claude Platform Docs</a></li>
<li><a href="https://llm.datasette.io/en/stable/usage.html">Usage - LLM - Datasette</a></li>

</ul>
</details>

**标签**: `#llm`, `#anthropic`, `#mcp`, `#release`, `#coding-tools`

---

<a id="item-7"></a>
## [CEO 花 1.3 万美元用 Codex，称“自动化是个谎言”](https://blog.qiaomu.ai/automation-is-a-lie) ⭐️ 7.0/10

**级别**: 核心必看

Every 的 CEO Dan Shipper 上个月在 OpenAI Codex 上花了 1.3 万美元，现在 Slack 里有 20 个 AI agent 和 20 个人类一起工作，尽管 COO 对此不以为然。他打算继续投入，认为自动化并不会真正取代人类工作。 这一真实使用数据提供了 AI 编程助手的实际成本及其融入日常工作的具体案例，挑战了“AI 完全替代工作”的炒作。对于正在权衡 AI 投入产出比以及人机协作模式的工程管理者而言，很有参考价值。 Every 有 27 名全职员工，目前已将代码编写、写作、客服、邮件和研究备忘录等流程交给 agent 处理。COO 的白眼反映出内部对 AI 成本的争议，而 Dan 则认为这笔花费是值得的。

rss · 向阳乔木 · 8月4日 16:47

**背景**: OpenAI Codex 是一套由 AI 驱动的编程代理，可自动完成拉取请求、重构和代码审查等软件工程任务。Agentic AI 比传统 AI 更进一步，能够自主规划、决策并执行多步骤工作流，正成为企业运营中的一个重要趋势。了解这一背景有助于理解为何像 Every 这样的公司愿意在高成本下大力投资此类 agent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex - OpenAI</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-ai-workflow-automation-building-autonomous-agents-bb9pc">Agentic AI &amp; Workflow Automation: Building Autonomous Agents That...</a></li>
<li><a href="https://kerkt.com/ai-agents-business-workflow-automation-guide/">AI Agents in Business Workflow Automation Guide</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Codex`, `#automation`, `#cost analysis`, `#workflow`

---

<a id="item-8"></a>
## [Claude Code v2.1.222 补丁修复工作树隔离与钩子绕过等问题](https://github.com/anthropics/claude-code/releases/tag/v2.1.222) ⭐️ 6.0/10

**级别**: 值得关注

Anthropic 发布了 Claude Code v2.1.222，这是一个补丁版本，修复了工作树隔离问题、后台代理任务中的 PreToolUse 钩子绕过、HTTPS 代理连接和 MCP 使用量归属等问题。该版本还移除了 ultraplan 功能，并通过权限分类器对 SendMessage 的检查提升了自动模式安全性。 此补丁修复了具有安全意义的缺陷（工作树隔离、钩子绕过）和正确性问题（代理连接、使用量归属），对依赖 Claude Code 进行自动化编码流程的团队尤为重要。它还为自动模式带来了安全性改进，而自动模式正越来越多地用于 CI/CD 和多智能体场景。 值得注意的修复包括：在所有会话类型中对文件编辑和 Bash 强制实施工作树隔离；防止 PreToolUse 自动允许钩子在后台任务中绕过工具限制；以及更改 /usage，使其仅在真正消耗 MCP 服务器工具结果时才归因其使用量。该版本还禁止通过仓库级设置自动启动 Remote Control，并改进了 --ax-screen-reader 模式下屏幕阅读器的行为。

github · ashwin-ant · 8月4日 22:39

**背景**: Claude Code 是 Anthropic 推出的智能编码工具，运行在终端中，可通过 git 工作树（worktree）并行运行彼此隔离的会话，防止改动冲突。PreToolUse 钩子是一种在工具调用执行前进行拦截并允许/拒绝的机制，而 MCP（模型上下文协议）服务器为 AI 模型提供外部工具和数据。本补丁重点修复了这些功能中可能影响工作流安全性和正确性的边界情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/worktrees">Run parallel sessions with worktrees - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#bugfix`, `#security`, `#AI coding tools`

---

<a id="item-9"></a>
## [Pydantic AI v2.23.0 新增成本追踪与工具可用性更新](https://github.com/pydantic/pydantic-ai/releases/tag/v2.23.0) ⭐️ 6.0/10

**级别**: 值得关注

Pydantic AI v2.23.0 已发布，新增了对 ModelSettings.extra\_headers 的 Bedrock 支持、恢复了稳定的 Gemini 网关别名、在 RunUsage 和 UsageLimits 中引入成本追踪，并添加了 ToolAvailabilityDeltaPart。此外还包含多项错误修复和新贡献者。 此版本通过添加成本追踪（帮助开发者管理 LLM 费用）和 ToolAvailabilityDeltaPart（支持在代理执行期间更动态地管理工具），增强了 Pydantic AI 在生产环境中的实用价值。这些增量式改进巩固了该框架在 Python AI 代理生态系统中的地位。 主要变更包括：对 bedrock\_max\_concurrency 进行验证以避免死锁、修复 GoogleCloudProvider 凭据作用域、以及正确处理异步流的关闭。RunUsage 中新增的 cost 字段和 UsageLimits 中的 cost\_limit 允许按运行设置费用上限，而 ToolAvailabilityDeltaPart 支持原生的 tool\_addition 和 additional\_tools 渲染。

github · dsfaccini · 8月4日 01:47

**背景**: Pydantic AI 是一个与模型无关的 Python 框架，用于构建类型安全的 AI 代理，提供结构化输出、验证和可观测性。它支持 OpenAI、Anthropic、Google 等提供商，并提供可组合的能力系统。v2.23.0 版本是该框架持续迭代开发的一部分，重点在于完善和开发者体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pydantic.dev/docs/ai/overview/">Pydantic AI | Pydantic Docs</a></li>
<li><a href="https://pydantic.dev/pydantic-ai">Pydantic AI: Type-Safe Python Framework for AI Agents &amp; LLM ...</a></li>
<li><a href="https://thesurface.ai/">Home — Surface</a></li>

</ul>
</details>

**标签**: `#pydantic-ai`, `#agent-ecosystem`, `#AI tools`, `#release`, `#Python`

---

<a id="item-10"></a>
## [Copilot CLI v1.0.79-1 重命名沙箱设置并修复问题](https://github.com/github/copilot-cli/releases/tag/v1.0.79-1) ⭐️ 5.0/10

**级别**: 值得关注

GitHub Copilot CLI v1.0.79-1 将沙箱设置 allowDevToolCaches 重命名为 allowDevToolAccess，这是一项破坏性变更。同时修复了上下文令牌归因、扩展禁用、提示符暂存和 Linux 沙箱重新运行行为的问题。 设置重命名可能使现有配置静默失效，因此用户必须更新 settings.json 和 MDM 策略以保留其退出选择。这些修复提高了 Free/Student 用户的令牌统计准确性，并让扩展和沙箱交互更加可靠。 旧的设置键不再被读取且被静默忽略，这意味着之前设置为 false 的退出选择会恢复为默认值（开启）。修复的问题包括：按自动解析模型计算上下文归因，以及 Linux 沙箱在命令被阻止时提供在沙箱外重新运行的选项。

github · copilot-cli-release-app\[bot\] · 8月4日 21:16

**背景**: Copilot CLI 是 GitHub 基于终端的 AI 助手，可以在用户定义的权限下读取、写入和运行代码。其沙箱设置控制 Copilot 是否可以访问开发工具的缓存、配置和注册表；这次重命名反映了权限范围不仅限于缓存。上下文归因修复确保了令牌统计的准确性，尤其是对计费方式不同的 Free/Student 用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli">Configuring GitHub Copilot CLI</a></li>
<li><a href="https://deepwiki.com/github/copilot-cli/3.5-tool-execution-and-permissions">Tool Execution &amp; Permissions | github/copilot-cli | DeepWiki</a></li>

</ul>
</details>

**标签**: `#copilot-cli`, `#release`, `#ai-coding`, `#devtools`, `#breaking-change`

---

<a id="item-11"></a>
## [GitHub Spark 将于 2026 年 8 月 31 日前在 github.com 上停用](https://github.blog/changelog/2026-08-04-upcoming-deprecation-of-github-spark-on-github-com) ⭐️ 5.0/10

**级别**: 值得关注

2026 年 8 月 4 日起，GitHub Spark 将不再接受新用户，也禁止创建新应用。现有用户可继续使用至 2026 年 8 月 31 日，此后该服务将完全停止。 此次停用影响了使用 GitHub Spark 以自然语言构建全栈 AI 应用的开发者及非程序员。用户需在 8 月 31 日服务关闭前规划迁移到其他工具。 该公告仅提供了停用时间表，未说明迁移路径或替代工具。2026 年 8 月 4 日之后，现有应用可能仍可访问，但无法再创建新项目。

rss · GitHub Changelog · 8月4日 15:54

**背景**: GitHub Spark 是一个 AI 原生工具，用户可以用纯自然语言创建全栈应用，无需管理云资源。它不仅面向程序员，也面向产品经理、设计师以及其他编码经验有限的人群。借助该工具，用户可以构建集成 AI 功能和外部数据源的实用微应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/features/spark">GitHub Spark · Dream it. See it. Ship it. · GitHub</a></li>
<li><a href="https://apidog.com/blog/github-spark/">Github Spark : The New AI Tool That Lets You Build Apps in Plain...</a></li>

</ul>
</details>

**标签**: `#GitHub Spark`, `#deprecation`, `#AI coding tools`, `#product update`

---