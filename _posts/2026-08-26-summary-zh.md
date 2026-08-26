---
layout: default
title: "Horizon 每日速递：2026-08-26"
description: "AI 精选的技术与研究日报"
date: 2026-08-26
lang: zh
locale: zh-CN
---

> 从 55 条内容中筛选出 8 条重要资讯。

---

1. [Ramp 自研编程智能体 Inspect，超越前沿 AI 实验室工具](#item-1) ⭐️ 8.0/10
2. [LangChain 与 Airbyte 推出生产级数据摄取集成](#item-2) ⭐️ 7.0/10
3. [OpenWorker 新版发布，内置网络安全智能体](#item-3) ⭐️ 7.0/10
4. [Claude 记忆功能统一聊天与 Cowork，支持逐条查看和编辑](#item-4) ⭐️ 7.0/10
5. [苹果推出搭载 M5 Max 与 M5 Ultra 的全新 Mac Studio](#item-5) ⭐️ 6.0/10
6. [GitHub Copilot CLI v1.0.81-10 新增插件仪表盘与自动模型选择](#item-6) ⭐️ 5.0/10
7. [pydantic-ai v2.34.0 新增 LangChain 迁移技能与 GLM-5.3 支持](#item-7) ⭐️ 4.0/10
8. [生产前评估 LLM：GitHub 密钥扫描经验总结](#item-8) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Ramp 自研编程智能体 Inspect，超越前沿 AI 实验室工具](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect) ⭐️ 8.0/10

**级别**: 核心必看

Ramp 没有依赖前沿 AI 实验室的智能体，而是自研了内部编程智能体 Inspect。目前 Inspect 编写了 Ramp 超过一半的合并拉取请求，Inspect 自身超过 80%的代码是在 Inspect 会话中完成的，工程师还在该平台上构建了 200 多个内部智能体。 这表明企业可以构建出针对自身工程工作流、表现优于前沿 AI 实验室通用工具的定制编程智能体，或许会有更多公司选择自研 AI 工具以获取竞争优势。 Inspect 通过完整的工程上下文和工具来闭环验证工作——比如运行测试、查看遥测数据、查询功能开关以及访问脱敏的只读生产数据库副本——从而像 Ramp 工程师一样证明自己的产出是可靠的。

rss · The Pragmatic Engineer · 8月25日 15:20

**背景**: 编程智能体是能够自主编写和修改软件的 AI 工具。Ramp 没有直接使用 Claude Code 等现成工具，而是选择在 OpenCode 框架上自建 Inspect，团队起初有 2 名工程师，后来扩展到 5.5 人。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect">Why Ramp built its own in-house coding agent, Inspect</a></li>
<li><a href="https://builders.ramp.com/post/why-we-built-our-background-agent">Why We Built Our Own Background Agent — Ramp Builders Blog</a></li>
<li><a href="https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal">How Ramp built a full context background coding agent on Modal | Modal Blog</a></li>

</ul>
</details>

**标签**: `#coding-agent`, `#in-house-ai`, `#engineering-practice`, `#ai-tooling`, `#fintech`

---

<a id="item-2"></a>
## [LangChain 与 Airbyte 推出生产级数据摄取集成](https://www.langchain.com/blog/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination) ⭐️ 7.0/10

**级别**: 核心必看

LangChain 与 Airbyte 宣布了一项新集成，通过调度、文本拆分和 50 多种嵌入模型，自动实现面向检索应用的生产级数据摄取。该集成旨在帮助开发者将数据管道从原型扩展到生产环境。 该集成打通了 AI 应用框架与数据集成平台，让团队在生产环境中构建可靠、可扩展的 RAG 与检索管道变得更加容易。 该集成以 LangChain 驱动的 Airbyte Destination（目标连接器）形式实现，使 Airbyte 的调度和连接器生态能够将数据直接送入 LangChain 的文本拆分与嵌入流程。

rss · AI 热榜 · 8月25日 21:12

**背景**: LangChain 是一个用于构建大语言模型应用的开源框架，Airbyte 是一个支持 ELT 管道并提供数百个连接器的开源数据集成平台。检索增强生成（RAG）应用通常需要先将源文档摄取、切分、嵌入并存入向量库，之后才能进行查询。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.langchain.com/blog/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination">LangChain 与 Airbyte 集成：让数据摄取达到生产级就绪</a></li>
<li><a href="https://docs.langchain.org.cn/oss/python/integrations/providers/airbyte">Airbyte 集 成 - LangChain 文档 - LangChain 教程</a></li>
<li><a href="https://airbyte.com/">Airbyte | The Context Layer for AI Agents | Open-Source Data Integration</a></li>

</ul>
</details>

**标签**: `#LangChain`, `#Airbyte`, `#Data Ingestion`, `#RAG`, `#Production Pipelines`

---

<a id="item-3"></a>
## [OpenWorker 新版发布，内置网络安全智能体](https://x.com/AndrewYNg/status/2092315079576555806) ⭐️ 7.0/10

**级别**: 核心必看

OpenWorker（吴恩达旗下的开源 AI 智能体）发布新版，内置三类网络安全智能体：代码漏洞扫描、依赖供应链注入检测和云安全配置检查。新版本还支持本地运行开放权重模型，避免敏感代码离开本机。 这很重要，因为它直接回应了企业在采用 AI 编程智能体时对安全性与隐私的担忧，让团队既能运行自动化安全检查，又能将专有代码保留在本地设备上。 值得一提的是，OpenWorker 的 harness 完全开源，安全团队可审计是否存在后门；不过“开放权重”模型未必公开训练数据，团队需逐一核实各模型的许可证才能确保真正的透明性。

rss · AI 热榜 · 8月25日 18:16

**背景**: OpenWorker 是由吴恩达联合推出的免费、开源、本地优先的 AI 智能体，可连接 Slack、Gmail、Notion 等日常工具，将任务推进到最终成果，并在重要操作前请求确认。本次新版在此基础上增加了以安全为核心的工作流层。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/AndrewYNg/status/2092315079576555806">OpenWorker 新版发布，内置网络安全智能体</a></li>
<li><a href="https://openworker.com/">OpenWorker — AI that gets your everyday tasks done</a></li>
<li><a href="https://www.stork.ai/blog/andrew-ngs-new-ai-does-your-work-for-you">OpenWorker : Andrew Ng&#x27;s Open -Source AI Agent That... | Stork. AI</a></li>

</ul>
</details>

**标签**: `#OpenWorker`, `#AI agents`, `#cybersecurity`, `#open-source`, `#coding tools`

---

<a id="item-4"></a>
## [Claude 记忆功能统一聊天与 Cowork，支持逐条查看和编辑](https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 今日将 Claude 的聊天与 Claude Cowork 记忆统一，在一个场景积累的上下文可在另一场景调用，记忆会在对话过程中实时更新。用户可以在 Memory 设置中按主题查看、编辑或删除每一条记忆。 这一改动让用户无需反复重新说明项目和偏好，使 Claude 对在聊天与智能体任务之间切换的开发者和团队更有价值。 尽管记忆功能在 Free、Pro 和 Max 套餐的网页、桌面和移动端默认开启，但健康、信仰等敏感话题仅在用户明确开启后才会存储，敏感识别号和犯罪记录则永远不会被保存。

rss · AI 热榜 · 8月25日 18:02

**背景**: Claude Cowork 是 Anthropic 推出的计算机操作代理，可直接处理用户的文件、文件夹和应用，而聊天是对话界面。记忆功能让 Claude 能跨会话携带偏好、项目和上下文，此前用户需要在新对话中反复交代这些信息。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it">Claude 记忆功能全面打通聊天与 Cowork，用户可逐条查看和编辑</a></li>
<li><a href="https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/">Claude Cowork finally remembers what you told the app in chat | TechCrunch</a></li>
<li><a href="https://www.zdnet.com/article/anthropic-claude-and-cowork-share-memories-now-unless-you-opt-out/">Anthropic&#x27;s Claude and Cowork will share memories about... | ZDNET</a></li>

</ul>
</details>

**标签**: `#Claude`, `#memory`, `#AI agent`, `#product update`, `#privacy`

---

## 更多动态

<a id="item-5"></a>
### [苹果推出搭载 M5 Max 与 M5 Ultra 的全新 Mac Studio](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) ⭐️ 6.0/10

苹果今日发布新款 Mac Studio，搭载 M5 Max 与全新 M5 Ultra，AI 性能最高提升 4.3 倍，图形性能提升 1.8 倍，存储速度提升 2 倍。M5 Ultra 配置支持最高 1.2TB/s 内存带宽与 256GB 统一内存，现已开启预购，9 月 22 日起发售。

hackernews · AI 热榜 · 8月25日 13:03 · [社区讨论](https://news.ycombinator.com/item?id=49433316)

<a id="item-6"></a>
### [GitHub Copilot CLI v1.0.81-10 新增插件仪表盘与自动模型选择](https://github.com/github/copilot-cli/releases/tag/v1.0.81-10) ⭐️ 5.0/10

GitHub Copilot CLI v1.0.81-10 将插件仪表盘（通过 /plugin、/mcp 和 /skills 命令）向所有用户开放，改进自动模式使其在对话过程中动态调整模型选择，并修复了插件激活导致的启动挂起问题。

github · copilot-cli-release-app\[bot\] · 8月25日 21:15

<a id="item-7"></a>
### [pydantic-ai v2.34.0 新增 LangChain 迁移技能与 GLM-5.3 支持](https://github.com/pydantic/pydantic-ai/releases/tag/v2.34.0) ⭐️ 4.0/10

Pydantic-ai v2.34.0 新增了 LangChain 迁移技能，并为 ZaiModel 增加了 GLM-5.3 支持，同时修复了涉及 Cohere、Groq、Cerebras、Vercel、Bedrock 等多个提供方的多项 bug。

github · dsfaccini · 8月25日 01:47

<a id="item-8"></a>
### [生产前评估 LLM：GitHub 密钥扫描经验总结](https://github.blog/ai-and-ml/llms/how-to-evaluate-llms-before-production/) ⭐️ 4.0/10

GitHub 发布了一篇博客文章，分享了在生产前以真实密钥扫描场景评估 LLM 的经验教训。文章强调要基于产品决策和严格测试，而不是依赖基准测试。

rss · GitHub AI &amp; ML · 8月25日 21:35