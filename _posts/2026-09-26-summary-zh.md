---
layout: default
title: "Horizon 每日速递：2026-09-26"
description: "AI 精选的技术与研究日报"
date: 2026-09-26
lang: zh
locale: zh-CN
---

> 从 71 条内容中筛选出 10 条重要资讯。

---

1. [Claude Devs 测算 Opus 5.5 在 Claude Code 中的任务成本](#item-1) ⭐️ 7.0/10
2. [Anthropic 开放插件目录提交门户，Plugins 成为 Claude 主要第三方扩展方式](#item-2) ⭐️ 7.0/10
3. [Claude Code v2.1.283 发布：新增企业级模型管控与 prompt-audit 命令](#item-3) ⭐️ 6.0/10
4. [pydantic-ai v2.50.0 发布：新增 DecisionModel 路由与持久化上下文钩子](#item-4) ⭐️ 6.0/10
5. [Cloudflare 推出 Turnstile Spin，用 AI 智能体补齐服务端机器人验证](#item-5) ⭐️ 6.0/10
6. [微软将 Copilot 拆分为 Home、Code 与全新 Autopilot 智能体](#item-6) ⭐️ 6.0/10
7. [Meta 的 Muse 为每位用户提供完整的 Ubuntu 云电脑](#item-7) ⭐️ 6.0/10
8. [GitHub Copilot 教程：用 /create-canvas 构建自定义工作流画布](#item-8) ⭐️ 5.0/10
9. [Ollaya 为开源 Jev 决策模型带来 Ollama 式本地运行时](#item-9) ⭐️ 4.0/10
10. [Latent Space 播客：OpenRouter 从种子轮到被 Stripe 以 70 亿美元收购](#item-10) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Claude Devs 测算 Opus 5.5 在 Claude Code 中的任务成本](https://x.com/ClaudeDevs/status/2103548467729887677) ⭐️ 7.0/10

**级别**: 核心必看

Claude Devs 指出，Opus 5.5 的每输入/输出 token 价格比 Opus 5 低 20%，缓存读取价格低 60%，并据此测算了在 Claude Code 中完成一个任务的实际成本变化。团队同时发布了计算器，读者可以直接从 /usage 运行自己的测算，完整说明见 claude.dev/blog/what-a-task-costs-on-opus-5-5/。 由于 agentic 编码会话中大部分 token 都消耗在反复读取体积庞大且基本不变的上文，缓存读取价格下降 60% 对 Claude Code 选型实际成本的影响，比输入/输出单价的降幅更能改变开发者的决策。 这些只是刊例价的下降，并不等于必然省下同样的比例：单个任务的实际成本取决于会话中缓存 token 与非缓存 token 的构成比例，这也是官方发布计算器的原因；Anthropic 另外声称，在典型工作负载下 Opus 5.5 的运行成本比 Opus 5 低约 40%。

rss · AI 热榜 · 9月25日 18:13

**背景**: Claude Code 是 Anthropic 的 agentic 编码工具，它会读取代码库并执行多步编辑与命令运行，因此会反复向模型发送一份很长且基本不变的上文。Prompt caching（提示缓存）让这些重复前缀按折扣后的缓存读取价格计费，而不是按完整输入 token 价格计费，这使缓存定价成为编码 agent 的一阶成本因素。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/ClaudeDevs/status/2103548467729887677">Claude Devs 测算 Opus 5.5 相比 Opus 5 在 Claude Code 任务中的成本变化</a></li>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 - Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI coding agents`, `#LLM pricing`, `#cost optimization`, `#developer tooling`

---

<a id="item-2"></a>
## [Anthropic 开放插件目录提交门户，Plugins 成为 Claude 主要第三方扩展方式](https://claude.com/blog/build-plugins-for-claude) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 宣布 Plugins 已成为为 Claude 构建第三方扩展的主要方式，一个插件可以打包 MCP 连接器、Agent Skills，或者两者兼有。开发者可通过新上线的目录提交门户提交插件，经审核后上架 Claude 目录。 这让 Claude 的第三方集成有了统一的打包、审核与分发入口，开发者不必再通过零散渠道分发 MCP 连接器和 Agent Skills，用户也能在一个目录中集中发现第三方能力。 根据现有摘要，该公告并未说明插件的审核标准、审核周期以及上架后的分发或变现条款；同时 Plugins 看起来是对现有 MCP 连接器和 Agent Skills 的打包，而非引入新的扩展运行时，因此其实际能力边界仍不清晰。

rss · AI 热榜 · 9月25日 18:09

**背景**: MCP（Model Context Protocol）是 Anthropic 于 2024 年 11 月推出的开放标准，用于把 AI 助手连接到外部系统和数据源；而 Agent Skills 是一种模块化能力封装，把指令、元数据以及脚本等可选资源打包起来，让 Claude 能在合适的任务上自动调用。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://claude.com/blog/build-plugins-for-claude">Claude 开放插件目录提交门户，Plugins 成为第三方扩展的主要方式</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol - Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview">Agent Skills - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#Claude`, `#MCP`, `#plugins`, `#agent ecosystem`, `#Anthropic`

---

## 更多动态

<a id="item-3"></a>
### [Claude Code v2.1.283 发布：新增企业级模型管控与 prompt-audit 命令](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) ⭐️ 6.0/10

Anthropic 发布 Claude Code v2.1.283，新增两项受管设置：\`availableModelsMatch\` 在设为 &quot;exact&quot; 时只允许其精确指定的模型版本，新版本在被列入前会一直处于封禁状态；\`deniedModels\` 则可在 \`availableModels\` 允许的情况下单独屏蔽某些模型。该版本还新增 \`/doctor prompt-audit\`（别名 \`/checkup prompt-audit\`）命令，用于扫描 CLAUDE.md 文件、skills、agents 和 commands 中针对旧模型编写的提示词模式，同时加入可选的 \`x-claude-code-prompt-id\` 网关提示头、OpenTelemetry 工具内容日志，以及大量 MCP、插件和 SDK 缺陷修复。

github · ashwin-ant · 9月25日 21:50

<a id="item-4"></a>
### [pydantic-ai v2.50.0 发布：新增 DecisionModel 路由与持久化上下文钩子](https://github.com/pydantic/pydantic-ai/releases/tag/v2.50.0) ⭐️ 6.0/10

pydantic-ai 发布了 v2.50.0，新增面向 Decisions 协议模型的 DecisionModel 基类（TypeSafeModel 现在也基于它构建），支持按名称询问 DecisionModel 该走哪条路由（每条路由一个标签），并加入只读属性 RunContext.in\_durable\_context，让钩子可以判断自己是否运行在持久化工作流代码中。该版本还在 provider details 中暴露 OpenAI 的 service\_tier，新增对 gemini-3.8-live 与 gemini-3.8-live-extended-thinking 的实时（realtime）支持，并附有三条关于路由 API 的兼容性说明。

github · DouweM · 9月25日 04:47

<a id="item-5"></a>
### [Cloudflare 推出 Turnstile Spin，用 AI 智能体补齐服务端机器人验证](https://blog.cloudflare.com/turnstile-spin/) ⭐️ 6.0/10

Cloudflare 发布了 Turnstile Spin，这是为其 Turnstile 机器人防护组件推出的一套由 AI 智能体驱动的安装流程。开发者不再需要手工接线，只需向自己惯用的 AI 编码智能体输入提示“Use the turnstile-spin skill to add Turnstile to this project”，该技能就会生成组件、在各选定插入点的前端代码片段，以及标准的服务端 siteverify 校验逻辑。

rss · Cloudflare AI · 9月25日 13:00

<a id="item-6"></a>
### [微软将 Copilot 拆分为 Home、Code 与全新 Autopilot 智能体](https://the-decoder.com/microsoft-gives-copilot-another-makeover-adding-an-autopilot-agent-and-usage-based-billing/) ⭐️ 6.0/10

微软正在将其 Copilot 应用重组为三个部分——Home、Code 以及一个名为 Autopilot 的新智能体——其中 Autopilot 基于 OpenClaw 构建，在云端持续运行，可监控 Teams 频道并自行完成任务。Home 和 Code 将在未来几周通过 Frontier 计划开始推出，Autopilot 则于本月底扩大到私有预览，同时 Code 与 Autopilot 从固定费率转为按用量计费。

rss · The Decoder · 9月25日 16:30

<a id="item-7"></a>
### [Meta 的 Muse 为每位用户提供完整的 Ubuntu 云电脑](https://the-decoder.com/metas-muse-agent-gives-every-user-a-full-cloud-computer-running-ubuntu-linux/) ⭐️ 6.0/10

Meta 现在为每一位 Muse 用户免费提供一台运行 Ubuntu Linux 的云电脑，用户可以在其中安装软件、编写代码和浏览网页；名为 Sentinel 的进程会监控工作区之外的敏感操作，用户也能检查系统中的每一个文件。据报道，该产品上线首周用户数已超过 50 万。

rss · The Decoder · 9月25日 12:22

<a id="item-8"></a>
### [GitHub Copilot 教程：用 /create-canvas 构建自定义工作流画布](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/) ⭐️ 5.0/10

GitHub 官方博客发布了一篇面向初学者的教程，介绍如何在 GitHub Copilot app 中构建名为 canvas（画布）的自定义工作流界面：打开一个 agent 会话，输入 /create-canvas 技能，再用自然语言描述想要的界面和工作流即可。随后 agent 会生成一个可供开发者与 agent 共同使用、并可持续迭代更新的实时界面，而不必只在聊天框里交互。

rss · GitHub AI &amp; ML · 9月25日 18:00

<a id="item-9"></a>
### [Ollaya 为开源 Jev 决策模型带来 Ollama 式本地运行时](https://ollaya.dev/) ⭐️ 4.0/10

Ollaya 发布，作为一个开源工具，可在本地拉取、运行并对外提供 Laya、decider、NLI、GLiClass 等开放决策模型，并通过一个兼容 TypeSafe 的 API 暴露服务，自称“决策模型领域的 Ollama”。它被发布到 Hacker News，吸引了约 97 条评论。

hackernews · Ardakilic · 9月25日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=49848269)

<a id="item-10"></a>
### [Latent Space 播客：OpenRouter 从种子轮到被 Stripe 以 70 亿美元收购](https://www.latent.space/p/openrouter) ⭐️ 4.0/10

最新一集 Latent Space 播客邀请了 OpenRouter 联合创始人兼 CEO Alex Atallah 与 AMP 的 Anjney Midha，回顾 OpenRouter 从 Llama、Alpaca、Mistral 等开放权重模型的第一波浪潮起步，成长为中立模型路由层的过程，并讨论了 Stripe 同意以超过 70 亿美元收购该公司一事。

rss · Latent Space · 9月25日 23:14