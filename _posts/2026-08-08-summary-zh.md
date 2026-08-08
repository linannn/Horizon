---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> 从 57 条内容中筛选出 14 条重要资讯。

---

1. [亚马逊、Cursor、微软、OpenAI、Vercel 联合发布 Agent Plugins 开放标准](#item-1) ⭐️ 9.0/10
2. [OpenAI Codex v0.147.0 推出便携插件与 MCP 支持](#item-2) ⭐️ 7.0/10
3. [Claude Code v2.1.224 新增自托管运行器、归档插件源与沙箱凭据脱敏](#item-3) ⭐️ 7.0/10
4. [Pydantic AI v2.26.0 新增工具隐藏、运行取消与 DeepSeek V4 Flash 支持](#item-4) ⭐️ 7.0/10
5. [DeepSeek V4 Flash 0731 发布：速度与低成本受好评](#item-5) ⭐️ 7.0/10
6. [规模化管理 AI 编程成本：Databricks 分享策略](#item-6) ⭐️ 7.0/10
7. [Copilot CLI v1.0.79-8 新增企业策略支持并调整沙盒认证设置](#item-7) ⭐️ 6.0/10
8. [GitHub Copilot CLI v1.0.79-7 增加插件扩展、Kimi K3 支持与 plan+autopilot 模式](#item-8) ⭐️ 6.0/10
9. [Cline 桌面版 v0.0.10 为远程 MCP 服务器添加 OAuth 认证](#item-9) ⭐️ 6.0/10
10. [OpenHands v1.11.0 新增 LLM 成本跟踪与子会话操作](#item-10) ⭐️ 6.0/10
11. [Copilot 使用量指标 API 新增代理应用活动统计](#item-11) ⭐️ 6.0/10
12. [Cloudflare 将 Workers AI 与 AI Gateway 统一为单一控制平面](#item-12) ⭐️ 6.0/10
13. [opencode v1.18.15：消息排序修复、清理优化、本地化增强与 JSON 导出](#item-13) ⭐️ 5.0/10
14. [GitHub 代码质量功能不再自动将 Copilot 添加为 PR 审查者](#item-14) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [亚马逊、Cursor、微软、OpenAI、Vercel 联合发布 Agent Plugins 开放标准](https://the-decoder.com/amazon-cursor-microsoft-openai-and-vercel-unite-on-a-shared-standard-for-ai-agent-plugins/) ⭐️ 9.0/10

**级别**: 核心必看

Agent Plugins 1.0.0 已作为开放标准发布，为 AI 智能体扩展定义了统一的软件包格式。它使用 plugin.json 清单文件，同时支持 agent skills 和 MCP 服务器，并获得了 Amazon、Cursor、Microsoft、OpenAI 和 Vercel 的支持。 这是罕见的跨行业合作，旨在标准化 AI 智能体扩展的打包与共享方式，有望提升各大 AI 平台之间的互操作性。开发者可以使用统一格式在 OpenAI、Microsoft、Amazon、Cursor 和 Vercel 的智能体之间复用扩展，从而减少 MCP 与智能体生态快速扩张中的碎片化问题。 1.0.0 版本的核心是定义了一个 plugin.json 清单文件作为软件包格式的基础。该标准统一了两种扩展类型：一种是为智能体添加能力与工作流的 agent skills，另一种是将智能体连接到外部工具和数据源的 MCP 服务器。

rss · The Decoder · 8月7日 08:54

**背景**: MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，用于将 AI 应用连接到本地文件、数据库和工具等外部系统。Agent skills 是一种轻量级、开放的格式，通过专门的知识和工作流扩展 AI 智能体的能力，通常以包含 SKILL.md 文件的文件夹形式呈现。Agent Plugins 旨在将这些概念整合为统一的软件包格式，让用户无需自定义适配即可在不同智能体之间安装扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#MCP`, `#plugin standard`, `#interoperability`, `#developer tools`

---

<a id="item-2"></a>
## [OpenAI Codex v0.147.0 推出便携插件与 MCP 支持](https://github.com/openai/codex/releases/tag/rust-v0.147.0) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 发布了 Codex CLI 的 rust-v0.147.0 版本，新增便携式 agent 插件、持久化会话分区、用于自动批准的 --approve-for-me 标志、Cursor 技能导入，以及对 MCP 2026-07-28 协议的支持。该版本还包含针对机密信息脱敏的修复和终端输入处理改进。 该版本通过集成更新的 MCP 功能和第三方技能，增强了 Codex 作为可扩展、感知策略的编码 agent 的能力，这对构建 agent 工作流的开发者很重要。安全修复和自动批准标志也使大规模 CLI 使用更加安全和高效。 MCP SDK 升级至 3.0.0，Ratatui 升级至 0.30.2，V8 升级至 150.4.0，并为 Amazon Bedrock 启用了缓存网络搜索和远程会话压缩。已弃用的 &\#x27;codex exec --full-auto&\#x27; 标志被移除，改用 &\#x27;--sandbox workspace-write&\#x27;，macOS 公证现在使用 Azure Key Vault。

github · github-actions\[bot\] · 8月7日 01:41

**背景**: Codex 是 OpenAI 的命令行编程 agent，在终端中运行，可以自动化软件工程任务。MCP 2026-07-28 规范是一次重大协议修订，引入了无状态核心、多轮请求和扩展框架。&\#x27;Agent 插件&\#x27;和&\#x27;skills&\#x27;是打包格式，用于在 Codex 和 Cursor 等 AI 代码编辑器之间共享可复用的指令和工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">The 2026-07-28 Specification | Model Context Protocol Blog</a></li>
<li><a href="https://github.com/openai/plugins">GitHub - openai/plugins: OpenAI Plugins · GitHub</a></li>
<li><a href="https://releasebot.io/updates/openai/codex">Codex Updates by OpenAI - August 2026 - Releasebot</a></li>

</ul>
</details>

**标签**: `#codex`, `#agent-plugins`, `#mcp`, `#cli`, `#release`

---

<a id="item-3"></a>
## [Claude Code v2.1.224 新增自托管运行器、归档插件源与沙箱凭据脱敏](https://github.com/anthropics/claude-code/releases/tag/v2.1.224) ⭐️ 7.0/10

**级别**: 核心必看

Claude Code v2.1.224 新增了 \`claude self-hosted-runner\` 命令，让 Team 和 Enterprise 用户可以在自己的机器或容器中运行 Claude Code 会话；同时新增 \`archive\` 插件源，可通过 HTTPS 上的 zip 文件安装插件，并支持可选的 SHA-256 固定。该版本还加入了多项沙箱凭据脱敏选项，覆盖结构化环境变量、JWT 声明以及 AWS SigV4。 自托管运行器让组织可以将代码保留在自己的基础设施内，同时仍使用 Claude Code 作为代理，这对数据控制和合规性具有重要意义。HTTPS zip 插件来源降低了插件分发门槛，而新的凭据脱敏选项则降低了敏感信息在沙箱内泄露的风险，对 AI 编程助手的使用者具有直接价值。 新的脱敏选项需要启用 \`network.tlsTerminate\`，并且仅从用户、管理或 \`--settings\` 设置中生效；\`ANTHROPIC\_BEDROCK\_REGION\_PREFIX\` 可让 Bedrock 优先使用指定的跨区域推理配置。此版本还移除了每会话 200 个子代理的生成上限，并修复了长项目路径解析到错误会话目录、以 \`/\` 结尾的沙箱 deny 规则可被绕过、跨会话消息投递静默失败等问题。

github · ashwin-ant · 8月7日 04:00

**背景**: Claude Code 是 Anthropic 推出的命令行 AI 编程代理，能够在终端中辅助开发者编写、审查和运行代码。自托管运行器让团队可以把代理会话放在自己的机器或容器中执行，这与绑定单个开发者机器的 Remote Control 有所不同。插件系统用于扩展 Claude Code 的能力，而沙箱机制则用来隔离命令执行并保护敏感的凭据信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/sandboxing">Configure the sandboxed Bash tool - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/plugins">Create plugins - Claude Code Docs</a></li>
<li><a href="https://claudcod.com/blog/claude-code-self-hosted-runner/">Claude Code Self - Hosted Runner : Own Infra Guide | Claude Code ...</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#self-hosted-runners`, `#plugins`, `#sandbox-security`, `#AI-coding-agent`

---

<a id="item-4"></a>
## [Pydantic AI v2.26.0 新增工具隐藏、运行取消与 DeepSeek V4 Flash 支持](https://github.com/pydantic/pydantic-ai/releases/tag/v2.26.0) ⭐️ 7.0/10

**级别**: 核心必看

Pydantic AI v2.26.0 新增了原生工具隐藏/显示、通过 AgentRun.cancel\(\) 和 RunContext.cancel\(\) 实现的第一方运行取消、公开的 AgentRunEvents 句柄、模型级提示缓存保留期解析，以及 DeepSeek V4 Flash 支持。此外还修复了 OpenRouter、TemporalModel 和延迟工具状态相关的多个 bug。 这些功能让开发者在构建生产级 LLM 智能体时，对运行过程和工具可见性拥有更精细的控制，而这正是常见的痛点。DeepSeek V4 Flash 支持和公开的事件句柄也让集成和监控更多模型与流式工作流变得更加容易。 工具隐藏/显示利用了各提供商原生的延迟/添加通道，AgentRunEvents 句柄暴露了 cancel\(\) 和运行状态访问。该版本还通过 Model.resolve\_prompt\_cache\_retention\(\) 从模型设置中解析有效的提示缓存保留期，并按索引映射 OpenRouter 流式推理细节。

github · dsfaccini · 8月7日 03:14

**背景**: Pydantic AI 是一个用于构建智能体 AI 应用的 Python 框架，提供结构化工具、类型安全以及与多种 LLM 提供商的集成。工具隐藏与显示让智能体可以将昂贵或上下文密集型工具延迟到需要时再加载，而运行取消对于交互式和长时间运行的智能体任务至关重要。提示缓存通过复用缓存前缀来降低延迟和成本，因此正确解析保留设置对于高效的多轮使用非常重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pydantic.dev/docs/ai/tools-toolsets/tools/">Function Tools | Pydantic Docs</a></li>
<li><a href="https://doc.tonyhub.xyz/openai/api/docs/guides/prompt-caching.html">Prompt caching | OpenAI API</a></li>
<li><a href="https://docs.agno.com/run-cancellation/agent-cancel-run">Agent Run Cancellation - Agno</a></li>

</ul>
</details>

**标签**: `#pydantic-ai`, `#agent-ecosystem`, `#tool-hiding`, `#run-cancellation`, `#DeepSeek`

---

<a id="item-5"></a>
## [DeepSeek V4 Flash 0731 发布：速度与低成本受好评](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 7.0/10

**级别**: 核心必看

DeepSeek 发布了 DeepSeek-V4-Flash-0731，这是其主打效率的 MoE 模型的正式版本，取代了之前的预览版，并大幅增强了智能体（agentic）能力。社区用户反馈，该模型在本地编码工作流中表现强劲，令牌生成速度快且成本极低。 此次发布表明，前沿级别的 AI 编程辅助可以在本地运行，成本仅为主流云 API 的零头，这可能会推动更多开发者转向自托管模型。速度、上下文长度与低成本相结合，或将加剧 AI 编程工具厂商之间的竞争。 DeepSeek-V4-Flash-0731 是一个专家混合（MoE）模型，总参数 284B（激活 13B），上下文窗口为 100 万 token。一位用户测得，在双 RTX Pro 6000 Blackwell GPU 上，预填充速度约 8k token/s，单流生成约 250 token/s；另一位用户则表示，在 5–6 个活跃会话下，每天花费不到 5 美元。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**背景**: DeepSeek 是梁文锋于 2023 年 12 月创立的中国人工智能公司。其 V4 系列采用专家混合（MoE）架构，每个 token 只激活一小部分参数，从而降低计算成本；Flash 变体是该系列中专攻效率的版本。0731 版本是正式版，取代了 4 月的预览版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/DeepSeek-V4-Flash-0731 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V4 Flash 0423 - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区整体评价积极：用户称赞该模型的速度、调试与文档分析能力，以及极低的 API 或本地运行成本。不过，有用户反馈在智能体工具调用中出现死循环和浪费 token 的问题，认为相比上一版 Flash 有所退步；另有用户描述了与其无关的 Anthropic 账号封禁事件。

**标签**: `#DeepSeek`, `#AI coding`, `#local LLM`, `#performance`, `#model release`

---

<a id="item-6"></a>
## [规模化管理 AI 编程成本：Databricks 分享策略](https://www.databricks.com/blog/managing-ai-coding-costs-scale) ⭐️ 7.0/10

**级别**: 核心必看

Databricks 发布了一篇题为《Managing AI Coding Costs at Scale》的博客文章，概述了控制 AI 辅助编程财务影响的策略。该文章引发了社区讨论，共 166 条评论，讨论 AI 生成代码的长期价值与成本。 随着企业越来越多地采用 AI 编程代理，不受控制的 token 成本可能每年增长到数百万美元。这些成本管理策略及围绕它们的讨论，凸显了工程团队和更广泛的 AI 工具生态正在面临的一项日益严峻的运营挑战。 讨论反映出人们对代码库可维护性的担忧——当 50 万行代码库中超过一半由代理生成时——以及对按量付费 AI 工具进行成本监督的必要性。一些评论者指出，小团队仍可从订阅制顶尖模型中受益，而模型路由与切换则表明 AI 模型本身正变得商品化。

hackernews · moonikakiss · 8月7日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=49214468)

**背景**: Databricks 是一家数据与 AI 软件公司，由 Apache Spark 的创始团队于 2013 年创建，提供横跨 AWS、Azure 和 Google Cloud 的云端数据分析与 AI 平台。Claude Code、GitHub Copilot、Cursor 等 AI 编程代理可以自主规划、执行并验证多文件修改，这提升了开发速度，但也带来了基于 token 的可变成本。在规模化场景下管理这些成本，已成为工程组织的一项关键运营课题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Databricks">Databricks</a></li>
<li><a href="https://www.augmentcode.com/tools/8-top-ai-coding-assistants-and-their-best-use-cases">8 Best AI Coding Assistants [Updated May 2026] | Augment Code</a></li>
<li><a href="https://mightybot.ai/blog/coding-ai-agents-for-accelerating-engineering-workflows/">Best AI Coding Agents in 2026, Ranked — MightyBot</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人认为对于复杂代码库，传统编码方式仍然更好，因为代理生成的代码会带来长期维护难题；另一些人则认为，拥有订阅权限的小团队比大公司更具优势。还有几条评论指出，关于 AI 支出意外飙升的文章如此之多，说明成本监督存在缺失；也有人提到，模型商品化意味着没有哪家供应商拥有明显的护城河。

**标签**: `#AI coding`, `#cost management`, `#engineering workflows`, `#Databricks`, `#AI agents`

---

<a id="item-7"></a>
## [Copilot CLI v1.0.79-8 新增企业策略支持并调整沙盒认证设置](https://github.com/github/copilot-cli/releases/tag/v1.0.79-8) ⭐️ 6.0/10

**级别**: 值得关注

GitHub 发布了 Copilot CLI v1.0.79-8，新增了对企业 allow-auto-only 策略的支持，并将沙盒认证设置重新组织到新的 Auth 标签页下。该版本还把 worktreeBaseRef 默认值改为 HEAD，将大型 monorepo 的搜索从 ripgrep 切换到 tgrep，并改进了模型选择器。 对企业团队而言，新的 allow-auto-only 策略让管理员可以允许 /allow-all auto 同时继续阻止完整的 allow-all，为 Copilot 在沙盒中的行为提供更细粒度的控制。沙盒认证配置键的破坏性迁移意味着使用自定义设置的用户必须更新配置，但整合后的 Auth 标签页让认证管理更简便。 配置键从 sandbox.gitAuth/sandbox.ghAuth 移至 sandbox.auth.git/sandbox.auth.gh，并且没有迁移机制：旧键在设置文件中被忽略，在 SDK 请求中会被视为无效而拒绝。worktreeBaseRef 的默认值改为 HEAD，影响 /worktree、/worktree new 和 --worktree；此前 --worktree 从远程默认分支开始。

github · copilot-cli-release-app\[bot\] · 8月7日 21:29

**背景**: GitHub Copilot CLI 是一个 AI 驱动的命令行助手，帮助开发者直接在终端中解释命令、编写代码和执行任务。它随所有 Copilot 套餐提供，通常以 GitHub CLI 扩展的形式安装。沙盒是 Copilot CLI 中经过批准的工具可以运行的安全环境，企业策略允许组织强制规定这些工具和凭据的使用方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/features/copilot/cli">GitHub Copilot CLI · GitHub</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli">Authenticating GitHub Copilot CLI - GitHub Docs</a></li>
<li><a href="https://github.blog/developer-skills/programming-languages-and-frameworks/boost-your-cli-skills-with-github-copilot/">Boost your CLI skills with GitHub Copilot - The GitHub Blog</a></li>

</ul>
</details>

**标签**: `#copilot-cli`, `#AI coding tools`, `#release notes`, `#coding agent`, `#enterprise policy`

---

<a id="item-8"></a>
## [GitHub Copilot CLI v1.0.79-7 增加插件扩展、Kimi K3 支持与 plan+autopilot 模式](https://github.com/github/copilot-cli/releases/tag/v1.0.79-7) ⭐️ 6.0/10

**级别**: 值得关注

GitHub 发布了 Copilot CLI v1.0.79-7，新增了对 com.github.copilot/extensions/ 目录下代理插件扩展的支持、kimi-k3 模型，以及将 --plan 与 --mode autopilot 结合的流程。该版本还改进了子代理 /tasks 导航，并修复了多个 macOS 沙箱问题。 该版本让使用代理插件和外部模型的团队在使用 Copilot CLI 时更加灵活，同时“先计划后自动执行”的模式减少了长编码任务中的人工审批负担。macOS 和 Windows Dev Drive 的修复也让沙箱命令执行在实际开发环境中更加可靠。 新的 plan+autopilot 组合会先制定计划再直接实施，无需等待批准；/tasks 导航新增了嵌套树浏览、当前/全部和已完成任务筛选，以及可操控的实时时间线。/app 命令现在会在 GitHub Copilot 桌面应用（1.1.3 或更高版本）中打开当前会话，沙箱命令也可重新使用 UNIX-domain sockets，修复了 macOS 上 tsx、vite、esbuild 和 jest workers 的问题。

github · copilot-cli-release-app\[bot\] · 8月7日 15:59

**背景**: GitHub Copilot CLI 是一款基于终端的 AI 代理，将 GitHub Copilot 的编码辅助能力带入命令行。代理插件生态系统让开发者可以用可复用的代理操作扩展 CLI；kimi-k3 是 Moonshot AI 推出的开放权重、原生多模态模型，拥有 100 万 token 的上下文窗口，专为长周期编码设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wshobson/agents">GitHub - wshobson/ agents : Multi-harness agentic plugin marketplace...</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents">Custom agents and sub-agent orchestration - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#copilot-cli`, `#GitHub Copilot`, `#AI coding tools`, `#CLI`, `#release`

---

<a id="item-9"></a>
## [Cline 桌面版 v0.0.10 为远程 MCP 服务器添加 OAuth 认证](https://github.com/cline/cline/releases/tag/desktop-v0.0.10) ⭐️ 6.0/10

**级别**: 值得关注

Cline 桌面版 v0.0.10 现在支持远程 MCP 服务器的 OAuth 认证，包括需要预注册 OAuth 客户端（而非动态注册）的服务器。它还在单个服务器上显示 MCP 错误，并对缺少模型凭据的对话回合显示失败原因。 这改善了基于 MCP 的 AI 编码工作流的可用性，减少了静默失败，使认证和错误处理更加透明。OAuth 支持扩大了 Cline 可连接的 MCP 服务器范围，这对依赖经过认证的远程工具的开发者很重要。 该更新在服务器客户端配置变化时会使存储的 OAuth 令牌失效，并允许用户在 Settings → MCP 中授权、重试或取消待处理的授权。它还修复了消息重复渲染、&\#x27;Agent is working…&\#x27; 卡住的问题，并新增了 Cmd/Ctrl+N 新会话等快捷键。

github · github-actions\[bot\] · 8月7日 07:04

**背景**: MCP（模型上下文协议）是由 Anthropic 于 2024 年 11 月推出的开放标准，用于标准化 AI 助手（如 LLM）与外部工具和数据源的连接方式。包括 Cline 在内的许多编码工具使用 MCP 让 AI 代理访问文件系统、数据库或远程 API。OAuth 2.0 动态客户端注册是 MCP 官方授权的标准方式，但有些服务器需要预注册的客户端 ID/Secret，本次更新对此提供了支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://workos.com/blog/dynamic-client-registration-dcr-mcp-oauth">Dynamic Client Registration (DCR) in MCP: What it is, why it ...</a></li>

</ul>
</details>

**标签**: `#cline`, `#MCP`, `#OAuth`, `#AI coding tools`, `#release`

---

<a id="item-10"></a>
## [OpenHands v1.11.0 新增 LLM 成本跟踪与子会话操作](https://github.com/OpenHands/OpenHands/releases/tag/v1.11.0) ⭐️ 6.0/10

**级别**: 值得关注

2026 年 8 月 7 日，OpenHands 发布了 1.11.0 版本，在活动日志和导出中新增了单次运行的 LLM 成本跟踪，增加了用于启动本地或云端子会话的类型化代理操作，以及自动化标签过滤与识别。该版本还包含 Agent Canvas 桌面应用的界面打磨和多项错误修复。 单次运行 LLM 成本跟踪让开发者能够清楚了解每次代理运行的 token 支出，随着 AI 编程代理在生产工作流中日益普及，这一点愈发重要。类型化子会话操作与自动化标签过滤改进了代理编排和工作流管理，惠及越来越多依赖 OpenHands 进行自主软件工程的社区成员。 成本跟踪功能通过 PR \#16351 在活动日志和导出中呈现单次运行的 LLM 成本，新的类型化代理操作（PR \#16380）用于处理本地或云端子会话。自动化标签过滤与识别（PR \#16388）伴随会话界面中的标签块、溢出和悬停卡片标签，同时桌面应用更名为 OpenHands Agent Canvas。

github · openhands-release-bot\[bot\] · 8月7日 18:01

**背景**: OpenHands 是一个开源的 AI 代理平台，用于软件开发，可以执行真实的工程工作，而不仅仅是提供代码建议。它运行自主代理，在代码库中规划、编写并应用更改，并提供协作式 UI 以及终端和无头操作。本次版本通过 Release Please 生成，是一个增量更新，重点关注运维可见性、代理编排和桌面端 UI 打磨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openhands.dev/">OpenHands | The Open Platform for Cloud Coding Agents</a></li>
<li><a href="https://www.openhands.dev/product">OpenHands Product | Autonomous Cloud Coding Agents</a></li>
<li><a href="https://www.blog.brightcoding.dev/2026/04/17/openhands-the-ai-developer-agent-that-actually-works">OpenHands: The AI Developer Agent That Actually Works</a></li>

</ul>
</details>

**标签**: `#OpenHands`, `#AI coding agent`, `#release`, `#LLM cost tracking`, `#automation`

---

<a id="item-11"></a>
## [Copilot 使用量指标 API 新增代理应用活动统计](https://github.blog/changelog/2026-08-07-copilot-usage-metrics-api-adds-agent-app-activity) ⭐️ 6.0/10

**级别**: 值得关注

GitHub 的 Copilot 使用量指标 API 现在包含来自 Claude 和 Codex 等合作伙伴代理应用的活动，使团队能够衡量其在 GitHub 工作流中的代理使用情况。此更新将原有 API 的覆盖范围从聊天和代码补全扩展到 AI 代理。 这让组织能够统一查看 Copilot 功能和第三方代理应用的 AI 编码活动。随着 AI 代理在开发工作流中越来越普遍，这种可见性对于采用跟踪、成本管理和治理至关重要。 Copilot 使用量指标 API 是一个 REST API，需要为企业启用“Copilot 使用量指标”策略。代理应用是 GitHub 应用程序，可展示合作伙伴的 AI 代理，可从 GitHub Marketplace 安装并由 Copilot 订阅提供支持。

rss · GitHub Changelog · 8月7日 18:20

**背景**: 代理应用是来自 GitHub 合作伙伴（如 Claude 和 Codex）的 AI 代理，可直接安装在 GitHub 工作流中使用。Copilot 使用量指标 API 提供有关组织内 Copilot 使用情况的详细数据，GitHub 建议新集成使用该 API。此次变更紧随 2026 年 6 月引入代理应用以及 2026 年 5 月同一 API 增加 AI 采用群体之后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/rest/copilot/copilot-usage-metrics">REST API endpoints for Copilot usage metrics - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/copilot/concepts/agents/agent-apps">About agent apps - GitHub Docs</a></li>
<li><a href="https://github.blog/changelog/2026-06-02-extend-github-with-agent-apps/">Extend GitHub with agent apps</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Copilot`, `#API`, `#agent metrics`, `#AI coding tools`

---

<a id="item-12"></a>
## [Cloudflare 将 Workers AI 与 AI Gateway 统一为单一控制平面](https://blog.cloudflare.com/workers-ai-gateway-unification/) ⭐️ 6.0/10

**级别**: 值得关注

Cloudflare 宣布将 Workers AI 和 AI Gateway 统一为一个 AI 控制平面。这为开发者提供了跨托管 GPU 推理和外部模型提供商的统一可观测性、计费和动态路由能力。 这一整合简化了构建高弹性 AI 应用的过程，开发者无需再分别管理推理和网关流量的工具。对于希望在一个地方监控多个 AI 提供商的成本、性能和路由的开发者来说，这具有重要意义。 统一控制平面引入了统一绑定和模型优先路由，使开发者能够动态地将请求路由到最合适的模型。它同时覆盖 Workers AI 管理的 50 多个开源模型，以及通过 AI Gateway 接入的 OpenAI 或 Anthropic 等外部提供商。

rss · Cloudflare AI · 8月7日 13:00

**背景**: Workers AI 是 Cloudflare 的无服务器边缘推理平台，开发者可以通过一次 API 调用在全球运行 AI 模型，并按实际用量付费。AI Gateway 充当 Worker 与第三方模型 API 之间的代理，提供可观测性、缓存等控制能力。Cloudflare 将两者整合为一个控制平面，旨在为 AI 基础设施提供统一的管理层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/workers-ai/">Cloudflare Workers AI - Edge AI Inference Platform</a></li>
<li><a href="https://developers.cloudflare.com/workers-ai/">Overview · Cloudflare Workers AI docs</a></li>
<li><a href="https://www.cloudflare.com/solutions/ai/">Cloudflare AI Cloud</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#AI Gateway`, `#Workers AI`, `#AI infrastructure`, `#developer tools`

---

<a id="item-13"></a>
## [opencode v1.18.15：消息排序修复、清理优化、本地化增强与 JSON 导出](https://github.com/anomalyco/opencode/releases/tag/v1.18.15) ⭐️ 5.0/10

**级别**: 值得关注

opencode 发布了 v1.18.15，这是一个补丁版本，修复了消息时间顺序、截断清理可靠性、重复压缩行为以及桌面端本地化覆盖问题。桌面应用现在还支持从界面将完整会话记录导出为 JSON。 这些修复提高了长时间编码会话的可靠性，并让桌面应用对非英语用户更友好。在竞争激烈的开源 AI 编程代理领域，稳定性和本地化是吸引并留住用户的关键。 关键技术修复包括：revert/fork 操作改用真实消息时间顺序而非消息 ID 排序；按文件时间戳更可靠地清理过期的截断文件；重复压缩时在摘要中保留更早的工具调用历史。此外，@rexdotsh 为 web UI 贡献了 blob 附件支持，@ayubun 和 @dangooddd 则贡献了两项 TUI 改进。

github · opencode-agent\[bot\] · 8月7日 06:49

**背景**: opencode 是一个开源、模型无关的 AI 编程代理，可在终端、桌面或 IDE 中运行，支持超过 75 家 AI 提供商，包括 Anthropic、OpenAI、Google 以及通过 Ollama 运行的本地模型。编程代理是自主 AI 工具，超越了自动补全，能够执行多步骤的软件工程任务。本次发布是 opencode 在可靠性和桌面体验方面持续迭代的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://opencode.ai/docs/">Intro | AI coding agent built for the terminal - opencode.ai</a></li>
<li><a href="https://nimbalyst.com/blog/what-is-opencode/">What is OpenCode? The Complete 2026 Guide - Nimbalyst</a></li>

</ul>
</details>

**标签**: `#opencode`, `#coding agent`, `#release notes`, `#bugfixes`, `#desktop app`

---

<a id="item-14"></a>
## [GitHub 代码质量功能不再自动将 Copilot 添加为 PR 审查者](https://github.blog/changelog/2026-08-07-github-code-quality-no-longer-adds-copilot-as-a-reviewer) ⭐️ 5.0/10

**级别**: 值得关注

根据 2026 年 8 月 7 日的 GitHub 更新日志，在仓库中启用 GitHub 代码质量功能时，不再自动创建一条要求 Copilot 对拉取请求进行代码审查的规则集。开发者若仍希望 Copilot 担任审查者，需要手动配置。 这一变化减少了团队启用代码质量功能时意外出现的 AI 审查干扰，让审查流程的控制更加明确。这也说明 GitHub 正在持续调整 Copilot 与仓库治理、规则集之间的集成方式。 此前，启用 GitHub 代码质量功能会生成一条规则集，自动将 Copilot 添加为拉取请求审查者。更新日志的开头提到了“已存在该规则集的仓库”，但关于已有配置是否会被移除，当前摘录并未完整说明。

rss · GitHub Changelog · 8月7日 15:07

**背景**: GitHub 代码质量功能结合了确定性静态分析与 AI，在拉取请求和默认分支上发现代码质量问题。它使用 CodeQL 等工具识别可维护性和可靠性缺陷，并提供基于大语言模型的修复建议。规则集是 GitHub 用来定义分支保护和合并策略（包括必需审查者）的机制。此次变更移除了代码质量功能与 Copilot 审查能力之间的一个自动关联。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/devops-by-nature/what-is-github-code-quality-bcb74890ef9e">What Is GitHub Code Quality ?. As software teams grow... | Medium</a></li>
<li><a href="https://docs.github.com/en/code-security/responsible-use/security-and-quality-ai-features">Application card: GitHub security and quality AI features - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets">About rulesets - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Copilot`, `#Code Quality`, `#code review`, `#changelog`

---