---
layout: default
title: "Horizon 每日速递：2026-09-01"
description: "AI 精选的技术与研究日报"
date: 2026-09-01
lang: zh
locale: zh-CN
---

> 从 37 条内容中筛选出 5 条重要资讯。

---

1. [OpenClaw 2.0 发布：简化设置、重构浏览器应用并支持多人会话](#item-1) ⭐️ 8.0/10
2. [ChatGPT Work 参考站点突出 Playwright 浏览器控制技能](#item-2) ⭐️ 7.0/10
3. [DoorDash 的 Flux 云平台每月自动执行 130,000 项工程任务](#item-3) ⭐️ 7.0/10
4. [DeepSeek 开源首个多模态模型 V4-Flash-Vision-Exp](#item-4) ⭐️ 7.0/10
5. [Cline 桌面版 Beta 0.0.21 新增云会话移交与环境选择](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenClaw 2.0 发布：简化设置、重构浏览器应用并支持多人会话](https://the-decoder.com/openclaw-2-0-brings-simplified-setup-a-rebuilt-browser-app-and-multiplayer-sessions/) ⭐️ 8.0/10

**级别**: 核心必看

OpenClaw 基金会发布了其开源 AI 平台 2.0 版本，这是迄今为止最大的一次发布，包含超过 16,000 个 pull request。此次更新增加了在租用机器上运行的云会话、实时协作、从零重写的浏览器应用，以及在设置过程中自动检测已有资源（如 API 密钥和 AI 订阅）的功能。 作为一个广受欢迎的开源 AI agent 平台，此次发布降低了上手门槛，并新增了协作和云端工作流，这可能会吸引更多开发者和团队基于 AI agent 进行开发。 OpenClaw 官方博客解释说，他们削减或简化了大量配置项，并将其余配置移出初始设置流程，让用户能更快地进行第一次对话，并通过与 agent 对话来完成配置。

rss · The Decoder · 8月31日 10:46

**背景**: OpenClaw 是一款免费开源的自主任 AI agent，运行在用户自己的设备上，通过大语言模型执行任务，并以 WhatsApp、Telegram、Discord 等消息平台作为主要用户界面。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/openclaw-2-0-brings-simplified-setup-a-rebuilt-browser-app-and-multiplayer-sessions/">OpenClaw 2.0 brings simplified setup, a rebuilt browser app, and multiplayer sessions</a></li>
<li><a href="https://openclaw.ai/blog/openclaw-2-accidentally">OpenClaw 2.0, Accidentally - OpenClaw Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenClaw`, `#AI agents`, `#open-source`, `#release`, `#developer tools`

---

<a id="item-2"></a>
## [ChatGPT Work 参考站点突出 Playwright 浏览器控制技能](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 7.0/10

**级别**: 核心必看

一个新的在线参考站点“ChatGPT Work 工具与技能参考”记录了 ChatGPT Work 的实用工具与技能。其中最有意思的一项技能描述了如何通过 ChatGPT Work 的 Node.js REPL 启动 Playwright，并利用 browser.documentation\(\) 方法动态检索文档来获取后续操作说明。 这意义重大，因为该参考站点为开发者提供了一种具体且可复用的模式，让 ChatGPT Work 真正具备浏览器控制能力，直接推动 AI 编程智能体生态的发展，并支持网站自动化工作流。 一个关键限制是 ChatGPT Work 目前只面向每月 20 美元及以上的订阅用户开放，因此这些已记录的技能对免费用户和每月 8 美元的 Go 用户不可用。

hackernews · ijidak · 8月31日 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49510000)

**背景**: ChatGPT Work 是 ChatGPT 内部的一种智能体模式，由 OpenAI 于 2026 年 7 月 9 日发布，基于 GPT-5.6 驱动。它不再只是返回聊天回复，而是可以接受项目简报并独立工作数分钟或数小时，最终交付电子表格、演示文稿、文档或 Web 应用等成品文件。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://codex-tool-reference.simonw.chatgpt.site/">ChatGPT Work Tool and Skill Reference</a></li>
<li><a href="https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/">Understanding ChatGPT Work | Simon Willison’s Weblog</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区反响不一：Simon Willison 称赞 control-browser 技能最有趣，并解释了其动态文档技巧；另一位评论者质疑它与 Codex 有何不同；还有人对小屏幕下的界面可用性提出意见，并指出 AI 生成的网站在视觉上存在千篇一律的问题。

**标签**: `#ChatGPT Work`, `#Playwright`, `#browser automation`, `#AI coding agents`, `#developer tools`

---

<a id="item-3"></a>
## [DoorDash 的 Flux 云平台每月自动执行 130,000 项工程任务](https://www.infoq.com/news/2026/08/doordash-flux-cloud-agent/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news) ⭐️ 7.0/10

**级别**: 核心必看

DoorDash 已将其工程代理工作负载从开发者笔记本电脑迁移到 Flux 云平台，该平台在一个月内自动完成了 130,000 项工程任务，并每周支持超过 25,000 次自动代码审查。该平台使用 Firecracker microVM、MCP 网关、可复用 playbook 和多种调用方式。 这为在云端运行 AI 编码代理提供了一个生产级参考，可能影响企业如何为委派的工程工作设计安全、可审计的基础设施。 Flux 在多种调用方式上强制实施范围受限的访问和集中式审计，这对于在大规模工程组织中安全地将工程任务委派给代理至关重要。

rss · InfoQ AI Coding · 8月31日 14:28

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年底推出的开放标准，它让 AI 代理能够以一致的方式连接外部工具和数据。像 Flux 这样的基于云的代理平台将基础设施、安全性和可观测性集中起来，使得在生产环境中运行和审计代理工作负载更加容易。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.infoq.com/news/2026/08/doordash-flux-cloud-agent/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news">DoorDash’s Flux Runs 130,000 Engineering Tasks Through Cloud-Based Agents</a></li>
<li><a href="https://careersatdoordash.com/blog/delegating-engineering-work-to-cloud-based-agents/">Delegating Engineering Work To Cloud-Based Agents - DoorDash</a></li>
<li><a href="https://explainx.ai/blog/doordash-flux-cloud-agents-platform-august-2026">DoorDash Flux: 130k Agent Tasks in One Month | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#MCP`, `#cloud infrastructure`, `#engineering workflows`, `#DoorDash`

---

<a id="item-4"></a>
## [DeepSeek 开源首个多模态模型 V4-Flash-Vision-Exp](https://www.ithome.com/0/996/637.htm) ⭐️ 7.0/10

**级别**: 核心必看

8 月 31 日，DeepSeek 在 Hugging Face 上以 MIT License 发布了首个多模态模型 DeepSeek-V4-Flash-Vision-Exp。发布内容包括模型文件、Tokenizer、Prompt Encoding 参考实现以及最小化 PyTorch 推理实现。 此次发布以宽松的 MIT 许可证提供多模态模型，为开发者构建视觉 Agent 工作流提供了新的开源选择，也使开源模型与 Opus-4.8 等专有模型的差距进一步缩小。 据 DeepSeek 介绍，这款实验性模型在需要视觉理解的 Agent 基准测试中相比 DeepSeek-V4-Flash 有大幅提升，多模态 Agent 能力已接近 Opus-4.8。

rss · AI 热榜 · 8月31日 11:35

**背景**: DeepSeek 是一家中国 AI 研究公司，以开源大语言模型（如 DeepSeek-R1 和 DeepSeek-V4）著称。此次发布的 V4-Flash-Vision-Exp 是 DeepSeek 首个多模态（视觉-语言）模型。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.ithome.com/0/996/637.htm">DeepSeek-V4-Flash-Vision-Exp 模型已开源，多模态 Agent 能力接近 Opus-4.8</a></li>
<li><a href="https://finance.sina.com.cn/tech/digi/2026-08-31/doc-iniqfkkr8825960.shtml">DeepSeek - V 4 - Flash - Vision - Exp 模 型 已 开 源 ， 多 模 态 Agent ...</a></li>
<li><a href="https://m.cnmo.com/news/816659.html">DeepSeek V 4 - Flash - Vision - Exp 上线： 多 模 态 API正式 开 放_CNMO</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#multimodal model`, `#open-source`, `#Hugging Face`, `#AI model release`

---

## 更多动态

<a id="item-5"></a>
### [Cline 桌面版 Beta 0.0.21 新增云会话移交与环境选择](https://github.com/cline/cline/releases/tag/desktop-v0.0.21-beta.2) ⭐️ 6.0/10

Cline 发布了 desktop-v0.0.21-beta.2，新增将本地会话移交给 Cline Cloud 的测试功能，可在本地、SSH 远程和云环境之间选择，并内置实验性的实时语音与头像叠加功能。

github · github-actions\[bot\] · 8月31日 21:08