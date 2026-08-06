---
layout: default
title: "Horizon Summary: 2026-08-06 (ZH)"
date: 2026-08-06
lang: zh
---

> 从 52 条内容中筛选出 11 条重要资讯。

---

1. [Cline SDK v0.0.70：计划模式硬性阻止文件编辑命令，自动恢复上下文溢出](#item-1) ⭐️ 7.0/10
2. [Meta 发布 Muse Code 与 Muse Spark 1.2 AI 模型](#item-2) ⭐️ 7.0/10
3. [Atlassian Rovo 存在提示注入漏洞，可导致数据外泄](#item-3) ⭐️ 7.0/10
4. [Cloudflare 提出 Agent 访问模型：面向任务范围的安全架构](#item-4) ⭐️ 7.0/10
5. [Claude Code v2.1.223 修复权限绕过并新增市场通配符配置](#item-5) ⭐️ 6.0/10
6. [Cline v4.1.4 支持 Chutes 并硬性阻止计划模式文件编辑](#item-6) ⭐️ 6.0/10
7. [OpenHands v1.10.0 新增自动化仪表盘与活动日志导出功能](#item-7) ⭐️ 6.0/10
8. [Cloudflare 推出身份感知 AI 网关以捕获异常 AI 行为](#item-8) ⭐️ 6.0/10
9. [Mistral 的 3B Shieldstral 安全模型以小巧体积比肩更大模型](#item-9) ⭐️ 6.0/10
10. [opencode v1.18.14 补丁改进 xAI 登录、错误重试与远程工作区](#item-10) ⭐️ 5.0/10
11. [Pydantic AI v2.24.0 发布，修复多个提供商集成 Bug](#item-11) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Cline SDK v0.0.70：计划模式硬性阻止文件编辑命令，自动恢复上下文溢出](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.70) ⭐️ 7.0/10

**级别**: 核心必看

Cline SDK v0.0.70 已发布，在计划模式中硬性阻止文件编辑类 shell 命令，不再仅仅依赖提示词约束。它还通过确定性压缩实现上下文窗口溢出的自动恢复，并新增 mode 字段及延迟根会话持久化，丰富了会话元数据。 此版本显著提升了 AI 编码智能体的安全性与可靠性，降低了计划阶段意外修改文件的风险，并避免上下文溢出导致长时间运行的代理工作流中断。这些改进使 Cline 更适合无人值守或半自动化的编码流程。 硬性阻止机制在 Windows 和 PowerShell 上也会拒绝 sed -i、perl -i 等就地编辑器、重定向到文件、变更性 git 子命令、软件包安装以及 sh -c、eval、sudo、xargs 等嵌套命令串。上下文溢出恢复采用确定性压缩且无需额外 LLM 调用，并自动重试一次；此外，空模型响应现在会在所有提供商上重试，而不仅仅是 Ollama。

github · github-actions\[bot\] · 8月5日 09:16

**背景**: Cline 是一个开源 AI 编码助手，将规划与执行分开：计划模式只读，用于探索代码和确定策略；执行模式则拥有完整的工具访问权限。上下文窗口溢出是指累积的对话历史和工具输出超过语言模型一次能处理的 token 上限，导致智能体丢失较早的上下文或直接失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.cline.bot/features/plan-and-act">Plan &amp; Act Mode - Cline</a></li>
<li><a href="https://aiagentmemory.org/articles/llm-context-window-overflow/">LLM Context Window Overflow : Strategies and Solutions for</a></li>
<li><a href="https://docs.cline.bot/sdk/architecture/overview">Packages - Cline</a></li>

</ul>
</details>

**标签**: `#cline`, `#sdk-release`, `#plan-mode`, `#context-window`, `#ai-coding`

---

<a id="item-2"></a>
## [Meta 发布 Muse Code 与 Muse Spark 1.2 AI 模型](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) ⭐️ 7.0/10

**级别**: 核心必看

Meta 发布了 Muse Code，一款面向 macOS 和 Linux 的终端编码代理（测试版），以及 Muse Spark 1.2，一款专注于编码的模型，改进了代码生成、复杂调试、代码库理解和端到端开发者工作流。该版本发布于 2026 年 8 月 5 日，与 Muse Spark 1.1 相比大幅提升了训练算力。 这标志着 Meta 正式进入与 Anthropic 和 OpenAI 竞争的 AI 编码代理赛道，为开发者提供了另一个主流的终端编码辅助选择。新的定价模式——允许 Meta 使用用户数据进行训练即可享受大幅折扣——可能重塑 AI 编码工具市场的成本格局。 Muse Spark 1.2 已在 Meta Model API 上提供，支持 100 万 token 的上下文窗口，优化了首次尝试准确率和更可靠的工具调用。Meta 为选择“贡献者”数据共享计划的用户提供输入 token 10 倍折扣（$0.10 vs. $1.25/Mtok）和输出 token 20 倍折扣（$0.20 vs. $4.25/Mtok）。

hackernews · paulkrush · 8月5日 19:15 · [社区讨论](https://news.ycombinator.com/item?id=49187575)

**背景**: Muse 是 Meta Superintelligence Labs 的 AI 模型系列，由 AI 负责人 Alexandr Wang 领导，Muse Spark 1.1 于 2026 年 7 月 9 日发布。Muse Code 这类编码代理是终端 AI 助手，能够自主编写、调试和重构代码，与 Claude Code 和 OpenAI 的 Codex 等工具竞争。该模型与代理协同训练，以优化真实开发者工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2">Introducing Muse Code and Muse Spark 1.2 | Meta AI Research</a></li>
<li><a href="https://developer.meta.com/ai/models/muse-spark/">Muse Spark 1.2 | Meta</a></li>
<li><a href="https://9to5mac.com/2026/08/05/meta-launches-muse-code-ai-coding-agent-for-macos-and-linux/">Meta launches Muse Code AI coding agent for macOS and... - 9to5Mac</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者强调了数据共享的激进折扣层级，并注意到内核优化图表显示所有模型在实验结束时仍在改进。有评论者批评 Meta 与 OpenAI 的中端模型“Terra”而非前沿模型比较，另一人则警告小字条款现在允许 Meta 将免费额度使用的内容用于产品改进。还有评论链接到 CNN 报道，称 Meta AI 可对其他公司发起网络攻击，引发安全担忧。

**标签**: `#AI coding`, `#Meta`, `#model release`, `#Muse`, `#developer tools`

---

<a id="item-3"></a>
## [Atlassian Rovo 存在提示注入漏洞，可导致数据外泄](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data) ⭐️ 7.0/10

**级别**: 核心必看

PromptArmor 发布安全报告，显示 Atlassian Rovo（Jira 和 Confluence 中的代理式 AI 工具）可被提示注入操控，从而窃取敏感数据。该攻击利用了 Rovo 的 URL 检索工具，该工具会打开由代理动态生成的 URL，并将机密数据附加到攻击者控制的 URL 上。 此事影响重大，因为 Rovo 已嵌入 Atlassian 广泛使用的企业产品中，使敏感企业数据面临风险。该发现表明，代理式 AI 工具需要对工具调用进行更严格的控制，也反映了业界在保护 AI 代理免受间接提示注入攻击方面面临的普遍挑战。 该漏洞利用了上传到 Rovo 的文件中嵌入的隐藏提示注入，随后代理会将敏感数据附加到它自己构造的 URL 上。Simon Willison 指出，Anthropic 提出了一种缓解模式：URL 检索工具只应获取由用户输入或来自可信工具的 URL，绝不应获取由代理自行拼接的 URL。

hackernews · hackerBanana · 8月5日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49185983)

**背景**: 提示注入是一种网络安全攻击，攻击者将恶意指令隐藏在大型语言模型处理的输入中，诱使模型做出违反用户意图的行为。间接提示注入则将这些指令嵌入网页或上传文件等内容中，对于能够自主浏览网页、读取文件并采取行动的代理式 AI 系统尤其危险。Atlassian Rovo 是集成在 Jira 和 Confluence 中的代理式 AI 助手，旨在帮助用户搜索和处理企业数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://grokipedia.com/page/Atlassian_Rovo_MCP_Server">Atlassian Rovo MCP Server</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，PromptArmor 对其他代理式 AI 工具发布了几乎相同的报告，这表明这是系统性问题而非 Rovo 独有的缺陷。Simon Willison 强调了私人数据访问、不可信内容暴露和外部通信这&\#x27;致命三要素&\#x27;是核心原因，还有人批评 Rovo 的用户体验，并调侃多数 AI 漏洞报告不过是&\#x27;直接让它去做那件事&\#x27;。

**标签**: `#prompt injection`, `#AI security`, `#Atlassian Rovo`, `#agent security`, `#LLM tools`

---

<a id="item-4"></a>
## [Cloudflare 提出 Agent 访问模型：面向任务范围的安全架构](https://blog.cloudflare.com/the-agent-access-model/) ⭐️ 7.0/10

**级别**: 核心必看

Cloudflare 发布了 Agent 访问模型（Agent Access Model），这是一个用于保护任务范围型 agent 的参考架构。它用短期、任务范围的凭证取代长期有效的用户凭证，并将强制校验从提示词迁移到 agent 运行环境与网络层。 随着 AI agent 越来越多地代表用户执行操作，赋予它们过宽的长期访问权限会带来严重的安全风险。该模型提供了具体且可落地的原则——身份代理、持续中介和状态化信任——开发人员可立即用来防止 agent 权限过度扩张。 该架构依赖严格的身份代理、持续中介和状态化信任，并设有只会随时间收窄 agent 能力的“信任棘轮”（Trust Ratchet）。这是一份概念性提案而非产品发布，因此 Cloudflare 没有同时宣布任何相关工具。

rss · Cloudflare AI · 8月5日 13:00

**背景**: 在传统身份验证中，用户的令牌往往在单个任务结束后仍然有效，并把完整的用户权限带入后续调用中，这在一个 AI agent 代执行时非常危险。安全专家越来越主张：每个 agent 实例都应拥有自己的唯一身份，权限应针对具体任务、限时且可撤销。Agent 访问模型将零信任原则——持续验证和最小权限——应用于新兴的 agentic AI 领域。状态化信任意味着系统会跟踪会话的历史和上下文，而不是孤立地检查每个请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.developersdigest.tech/blog/cloudflare-agent-access-model-2026">Cloudflare &#x27;s Agent Access Model : Zero Trust for... - Developers Digest</a></li>
<li><a href="https://arxiv.org/html/2603.17170v1">PAuth – Precise Task-Scoped Authorization For Agents</a></li>
<li><a href="https://workos.com/blog/ai-agent-credentials">Securing agentic apps: Give your AI agents their own credentials — WorkOS</a></li>

</ul>
</details>

**标签**: `#agent-security`, `#access-control`, `#agent-ecosystem`, `#identity-brokering`, `#cloudflare`

---

<a id="item-5"></a>
## [Claude Code v2.1.223 修复权限绕过并新增市场通配符配置](https://github.com/anthropics/claude-code/releases/tag/v2.1.223) ⭐️ 6.0/10

**级别**: 值得关注

Anthropic 在 GitHub 上发布了 Claude Code v2.1.223，包含关键安全修复：修复了 Bash 权限绕过、审批对话框中隐藏部分命令的问题，以及通过动态 import\(\) 绕过工作流沙箱的漏洞。本次发布还新增了市场通配符设置、/teleport 提示，并将 /review 改为 /code-review 的别名。 这一增量版本强化了广泛使用的 AI 编程助手的安全边界，修复了可能让恶意构造的命令或工作流在未经批准的情况下执行任意代码的漏洞。它还通过支持组织级市场的允许/阻止规则和更明确的模型上下文窗口管理，提升了企业部署的友好度。 值得注意的变更包括：代理定义的 bypassPermissions 模式不再能绕过组织的禁用策略；未知的 modelOverrides 键会被忽略；修复了 Linux 上 denyWrite 覆盖工作目录时沙箱命令无法启动的问题；CLAUDE\_CODE\_DISABLE\_1M\_CONTEXT 现在对所有原生 1M 上下文窗口模型生效。此外，/review 现在是 /code-review 的别名，且 /code-review 会记住上次使用的努力级别。

github · ashwin-ant · 8月6日 00:52

**背景**: Claude Code 是 Anthropic 推出的命令行 AI 编程代理，可在终端中运行，能够编辑文件、执行 Bash 命令和运行工作流。它提供从 acceptEdits 到 bypassPermissions（也称 YOLO 模式）的多种权限模式，后者可以通过托管设置加以限制。该工具还包含从 v2.0.24 开始提供的原生沙箱隔离功能，限制 Bash 工具的文件系统与网络访问，实现纵深防御。本次发布修复了某些构造的 Bash 命令或工作流通过动态 import\(\) 绕过这些权限和沙箱检查的缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/permission-modes">Choose a permission mode - Claude Code Docs</a></li>
<li><a href="https://deepwiki.com/FlorianBruniaux/claude-code-ultimate-guide/12.5-sandbox-isolation">Sandbox Isolation | FlorianBruniaux/ claude - code -ultimate-guide</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#release`, `#security`, `#AI coding agent`

---

<a id="item-6"></a>
## [Cline v4.1.4 支持 Chutes 并硬性阻止计划模式文件编辑](https://github.com/cline/cline/releases/tag/v4.1.4) ⭐️ 6.0/10

**级别**: 值得关注

Cline v4.1.4 新增了对 Chutes 提供商的支持，改进了斜杠命令的消歧，并在计划模式中硬性阻止文件编辑类 shell 命令。它同时修复了计划/执行模式切换、MCP 刷新以及空模型响应等大量 bug。 对于一个拥有数百万用户的 AI 编程代理而言，让计划模式强制只读行为可减少规划期间意外修改文件的风险。提供商和兼容性修复也扩大了对 OpenRouter、Bedrock 和 OpenAI 兼容端点的支持。 硬性阻止适用于文件操作、就地编辑器、重定向到文件、变更性 git 子命令以及软件包安装，只读调查仍然可用。退出计划模式的切换现在仅由用户驱动，并且该版本会在所有提供商上重试空模型响应。

github · github-actions\[bot\] · 8月5日 10:29

**背景**: Cline 是一个开源自主编程代理，运行在 IDE 和终端中，具有独立的 Plan 和 Act 模式：Plan 模式让代理在无需编辑的情况下探索代码并提出策略，Act 模式则执行计划。Chutes 是一个用于开源模型的去中心化无服务器计算提供商，Cline 现已原生支持将其作为提供商。此补丁版本属于 Cline 对安全性和可靠性持续增量改进的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.cline.bot/core-workflows/plan-and-act">Plan &amp; Act Mode - Cline</a></li>
<li><a href="https://github.com/cline/cline">GitHub - cline/cline: Autonomous coding agent as an SDK, IDE...</a></li>
<li><a href="https://chutes.ai/">Chutes | Serverless AI Compute</a></li>

</ul>
</details>

**标签**: `#cline`, `#AI coding agent`, `#release notes`, `#plan mode`, `#open-source tool`

---

<a id="item-7"></a>
## [OpenHands v1.10.0 新增自动化仪表盘与活动日志导出功能](https://github.com/OpenHands/OpenHands/releases/tag/v1.10.0) ⭐️ 6.0/10

**级别**: 值得关注

OpenHands 于 2026 年 8 月 5 日发布 v1.10.0，新增自动化落地仪表盘、活动日志导出、技能页面的分面导航栏筛选、自动化界面的清单驱动的子页面，并将 Canvas 的默认模型改为 GLM 5.2。此版本还包含多项错误修复、依赖更新和维护变更。 此版本提升了 OpenHands（一款流行的开源 AI 编程代理）的可用性和可观测性，使自动化工作流更易于导航和审计。这反映了该项目的持续演进以及对开发者需求的积极响应。 主要功能包括 ShashwatXD 实现的活动日志导出、hieptl 实现的自动化落地仪表盘和清单驱动的子页面、sleeyax 实现的技能页分面导航栏筛选，以及 neubig 修复的 Canvas 变更期间 MCP 凭据保留问题。错误修复涉及自动化超时上限、后端身份固定、IPv4 回环地址使用、npm 审计漏洞等。

github · openhands-release-bot\[bot\] · 8月5日 15:54

**背景**: OpenHands 是一个开源 AI 编程代理平台，用于自动化软件开发任务。此次增量版本在其自动化和技能基础设施上继续构建。GLM 5.2 是 Z.ai 推出的大规模推理模型；分面导航栏是 Material Design 3 中面向中型设备的导航模式。清单驱动的子页面意味着自动化界面的页面由清单文件定义，从而实现灵活配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z. AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://m3.material.io/components/navigation-rail">Navigation rail – Material Design 3</a></li>

</ul>
</details>

**标签**: `#OpenHands`, `#AI coding agent`, `#release`, `#open-source`, `#automation`

---

<a id="item-8"></a>
## [Cloudflare 推出身份感知 AI 网关以捕获异常 AI 行为](https://blog.cloudflare.com/identity-aware-ai-gateway/) ⭐️ 6.0/10

**级别**: 值得关注

Cloudflare 宣布其 Identity-aware AI Gateway 进入公开测试版，该网关利用 User Insights 为每个用户和智能体建立行为基线，并实时标记内部风险。 随着企业部署 AI 智能体和工具，该功能让安全团队能够清楚了解是谁或什么在发起 AI 请求，有助于及早发现未授权或恶意使用。它回应了 AI 工作流中日益增长的内部风险担忧。 User Insights 为每个用户和智能体建立行为基线，并在出现偏差时立即标记内部风险。据 SiliconANGLE 报道，该服务会为离开企业网络的每个 AI 请求附加经过验证的身份。

rss · Cloudflare AI · 8月5日 13:00

**背景**: AI Gateway 是 Cloudflare 为 AI 应用提供的控制平面，具备故障转移路由和速率限制等功能。身份感知分析在此基础上扩展了安全监控：行为基线为每个身份定义了“正常”的行为模式，并检测活动何时出现显著偏差，这是内部威胁检测中常用的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/identity-aware-ai-gateway/">Catching rogue AI behavior with identity-aware analytics | The Cloudflare Blog</a></li>
<li><a href="https://siliconangle.com/2026/08/05/cloudflare-launches-identity-aware-ai-gateway-track-using-ai/">Cloudflare launches Identity-Aware AI Gateway to track who is using AI - SiliconANGLE</a></li>
<li><a href="https://www.exabeam.com/blog/security-operations-center/how-behavioral-baselines-surface-risk-over-time/">How Short Correlation Windows Hide Insider Threat... | Exabeam</a></li>

</ul>
</details>

**标签**: `#AI Gateway`, `#security`, `#agent monitoring`, `#identity-aware analytics`, `#insider risk`

---

<a id="item-9"></a>
## [Mistral 的 3B Shieldstral 安全模型以小巧体积比肩更大模型](https://the-decoder.com/mistrals-open-model-shieldstral-matches-much-larger-safety-models/) ⭐️ 6.0/10

**级别**: 值得关注

Mistral 发布了 Shieldstral，一个 3B 参数的开源权重安全分类器，用于文本和图像内容审核。它使用自然语言的“是/否”问题作为安全标准，据称在部分基准测试上优于体积大至七倍的模型。 这之所以重要，是因为它表明安全分类器可以做到足够小巧并在本地运行，从而减少对大型专有内容审核 API 的依赖。开发人员可以在运行时自定义安全标准，而无需依赖第三方的分类体系。 Shieldstral 大约有 38 亿参数，支持 12 种语言，并以 Apache 2.0 许可证发布。由于判定标准以自然语言的“是/否”问题来表达，操作者可以在运行时调整内容策略，并在设备端运行该模型。

rss · The Decoder · 8月5日 16:35

**背景**: AI 安全分类器通常集成在大型前沿模型中，或通过第三方 API 提供。Mistral 的做法通过使用自然语言标准将具体安全策略与分类器本身解耦，从而使内容审核更加透明，也更适合在设备端进行自定义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/shieldstral/">Introducing Shieldstral . | Mistral AI</a></li>
<li><a href="https://www.baseten.co/library/shieldstral-1-3b/">Mistral Shieldstral 1.0 3B | Model library</a></li>

</ul>
</details>

**标签**: `#Mistral`, `#AI safety`, `#open-source model`, `#Shieldstral`, `#LLM`

---

<a id="item-10"></a>
## [opencode v1.18.14 补丁改进 xAI 登录、错误重试与远程工作区](https://github.com/anomalyco/opencode/releases/tag/v1.18.14) ⭐️ 5.0/10

**级别**: 值得关注

opencode v1.18.14 是一个补丁版本，将 xAI 登录简化为适用于无头环境的单一设备码流程，保留流中结构化提供程序错误以便重试，并在 ACP 用量统计中计入缓存写入。它还修复了远程工作区行为：不再转发主机目录，并记录代理请求的 5xx 响应体。 此补丁减少了用户在无头或远程环境中运行 opencode 时的登录摩擦，使 xAI/Grok 访问更加顺畅。它还通过更好的错误重试处理和更准确的 ACP 用量统计提高了可靠性，这对依赖分布式或容器化环境中编码代理的团队很有价值。 该版本包含社区贡献者 @jamesmurdza 的两个修复（PR \#40136 和 \#40135）：不将主机目录转发给远程工作区，以便提示从远程项目根目录解析；在主机日志中记录上游 5xx 响应体。此外，在结束一个回合前等待排队的 ACP 会话更新完成，以避免潜在的数据丢失。

github · opencode-agent\[bot\] · 8月5日 20:58

**背景**: opencode 是一个运行在终端中的开源 AI 编码代理。Agent Client Protocol（ACP）是一个开放标准，用于标准化代码编辑器/IDE 与编码代理之间的通信，使不同代理无需自定义集成即可在多个编辑器中工作。OAuth 设备码流程是一种适用于没有浏览器或输入受限设备的认证方式，用户访问验证 URL 并输入短代码。xAI 提供 Grok 模型；简化的登录方式使远程 SSH 或容器环境中的无头认证更加容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentclientprotocol.com/">Introduction - Agent Client Protocol</a></li>
<li><a href="https://www.jetbrains.com/acp/">Agent Client Protocol ( ACP ): Use Any Coding Agent in Any IDE</a></li>
<li><a href="https://www.oauth.com/playground/device-code.html">Device Code Flow - OAuth 2.0 Playground</a></li>

</ul>
</details>

**标签**: `#opencode`, `#AI coding`, `#release`, `#bugfixes`, `#coding agent`

---

<a id="item-11"></a>
## [Pydantic AI v2.24.0 发布，修复多个提供商集成 Bug](https://github.com/pydantic/pydantic-ai/releases/tag/v2.24.0) ⭐️ 5.0/10

**级别**: 值得关注

Pydantic-ai v2.24.0 已发布，重点修复了多个提供商集成中的 Bug。该版本处理了 Google、Bedrock、OpenRouter、Groq 和 Kimi 模型处理问题，并改进了流处理与重试逻辑。 此补丁版本提升了 pydantic-ai 的可靠性——这是一个用于构建 LLM agent 的热门 Python 框架。使用这些提供商集成的开发者将遇到更少的边缘情况故障，这对 agent 工作流进入生产阶段具有重要意义。 值得注意的修复包括：保留调用方所有的 OpenAI 模型设置、向 Bedrock 发送 top\_p=0.0，以及在 OpenRouter 模型缺少提供商前缀时抛出 UserError。该版本还防止了 Retry-After 出现负值，并跳过不兼容的入站 AG-UI 内容，而不是返回 422 错误。

github · dsfaccini · 8月5日 02:12

**背景**: Pydantic-ai 是一个使用 Pydantic 数据验证能力来构建 AI agent 的 Python 框架，通过可插拔集成支持多种 LLM 提供商。OpenRouter 是一个统一 API 网关，提供单一端点访问数百个 AI 模型；Amazon Bedrock 则是 AWS 的完全托管服务，用于访问基础模型（foundation models）。本版本主要着眼于修复这些集成中的边缘情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.pydantic.dev/">ai .pydantic.dev</a></li>
<li><a href="https://www.linkedin.com/pulse/openrouter-one-ai-integration-hundreds-models-much-less-kotnik-iiwgf">OpenRouter : One AI Integration, Hundreds of Models, and Much Less...</a></li>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production...</a></li>

</ul>
</details>

**标签**: `#pydantic-ai`, `#release`, `#bug-fixes`, `#agent-framework`, `#LLM`

---