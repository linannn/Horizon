---
layout: default
title: "Horizon 每日速递：2026-08-25"
description: "AI 精选的技术与研究日报"
date: 2026-08-25
lang: zh
locale: zh-CN
---

> 从 33 条内容中筛选出 6 条重要资讯。

---

1. [OpenAI 推出 ChatGPT Work，面向非工程师普及 AI 智能体](#item-1) ⭐️ 7.0/10
2. [GPT-5.6 登陆 Kiro，开发任务成本降低约 82%](#item-2) ⭐️ 7.0/10
3. [Claude Code v2.1.243 新增用法统计、模型选择器与缓存 TTL 设置](#item-3) ⭐️ 6.0/10
4. [Mastra Core 1.61.0 新增实验、优雅关闭和活动消息投递](#item-4) ⭐️ 6.0/10
5. [文章称 AI 编码依赖可能导致开发者专业技能崩溃](#item-5) ⭐️ 6.0/10
6. [OpenAI 限时下调 GPT-5.6 Sol API 价格](#item-6) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [OpenAI 推出 ChatGPT Work，面向非工程师普及 AI 智能体](https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 推出了 ChatGPT Work，这是一款基于 Codex 改造、面向非工程师的智能体产品，最低订阅档每月 20 美元。内部数据显示，6 月有 98% 的 OpenAI 员工使用 Codex，但组织订阅者中仅 17%、个人订阅者中不足 1% 使用。 这很重要，因为此举标志着 OpenAI 试图把 AI 智能体从开发者群体推广到白领工作流，从而扩大采用率，并为其巨额训练投入提供支撑。 TechCrunch 的报道指出，用户对交出控制权仍有顾虑：OpenAI 桌面应用如今已能访问并控制主管工程师的收件箱、Slack、手机、Notion、Figma 等应用。

rss · AI 热榜 · 8月24日 15:00

**背景**: Codex 是 OpenAI 于 2025 年 4 月以 Codex CLI 形式发布的 AI 编程智能体，可通过 ChatGPT 网页应用、桌面应用和 IDE 集成使用。AI 智能体是一类能自主追求目标、调用工具完成多步骤任务的程序。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them">OpenAI 正为一切构建 AI 智能体，但用户会愿意交出控制权吗？</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28AI_agent%29">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://help.openai.com/zh-hans-cn/articles/11752874-chatgpt-agent">ChatGPT 智能体 | OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI agents`, `#ChatGPT Work`, `#product launch`

---

<a id="item-2"></a>
## [GPT-5.6 登陆 Kiro，开发任务成本降低约 82%](https://openai.com/index/gpt-5-6-in-kiro) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 已将 GPT-5.6 模型家族（Sol、Terra、Luna）引入软件开发智能体 Kiro，并宣布在 Terminal-Bench 2.1 测试中，GPT-5.6 Terra 在 Kiro 内完成任务的成本降低约 82%。此次上线由 OpenAI 与 AWS 合作优化，旨在让每个 token 产生更多有效工作。 这为开发团队在智能体编程工具中带来了具体可衡量的性价比提升，随着 AI 辅助开发对成本越来越敏感，该更新可能影响团队的工具选型决策。 82% 的成本降低是针对 GPT-5.6 Terra 在 Kiro 内、于 Terminal-Bench 2.1 基准上的表现；公告虽然将 Sol 和 Luna 列为同一家族，但未披露两者的单独基准结果。

rss · AI 热榜 · 8月24日 12:00

**背景**: Kiro 是一款基于规格驱动开发的智能体 IDE 和命令行工具，智能体负责编写代码、运行测试并验证正确性，开发者则负责审查与决策。Terminal-Bench 是一个用于评测 AI 智能体在真实终端环境中完成任务能力的基准。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6-in-kiro">GPT-5.6 登陆 Kiro，为开发者提升性价比</a></li>
<li><a href="https://kiro.dev/">Kiro: Move beyond AI coding to agentic engineering</a></li>
<li><a href="https://github.com/kirodotdev/Kiro">GitHub - kirodotdev/Kiro: Kiro is an agentic IDE that works ...</a></li>

</ul>
</details>

**标签**: `#GPT-5.6`, `#Kiro`, `#coding-agent`, `#cost-reduction`, `#OpenAI`

---

## 更多动态

<a id="item-3"></a>
### [Claude Code v2.1.243 新增用法统计、模型选择器与缓存 TTL 设置](https://github.com/anthropics/claude-code/releases/tag/v2.1.243) ⭐️ 6.0/10

Anthropic 发布了 Claude Code v2.1.243，在 \`/usage\` 中新增每轮循环的用量统计，为 \`/model\` 选择器新增 \`modelPicker\` 配置，并新增 \`promptCacheTtl\`、\`subagentPromptCacheTtl\` 设置、\`modelPricing\` 受管设置，以及 \`/login\` 下“使用 Console 账户登录”的无密钥登录方式。该版本还修复了远程 MCP 服务器重连、auto 模式重试、\`/resume\` 分页等问题。

github · ashwin-ant · 8月24日 23:40

<a id="item-4"></a>
### [Mastra Core 1.61.0 新增实验、优雅关闭和活动消息投递](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.61.0) ⭐️ 6.0/10

Mastra 发布了 @mastra/core@1.61.0，新增了供外部编排器使用的调用方驱动实验 API、可配置的服务器关闭与排空控制、会话中自动的“while-active”消息投递、并发安全的工作流恢复，以及用于评估的多轮 LLM 评判器。该更新日志未列出任何破坏性变更。

github · PaulieScanlon · 8月24日 09:02

<a id="item-5"></a>
### [文章称 AI 编码依赖可能导致开发者专业技能崩溃](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 6.0/10

2026 年 7 月 22 日，开发者 Lars Faye 发表文章称，对 AI 编码工具的依赖将导致开发者专业技能崩溃，因为程序员不再经历能够锤炼能力的深度问题解决过程。该文章在 Hacker News 上引发广泛讨论，评论者就智能体式『vibe coding』与引导式 AI 辅助开发之间的取舍各抒己见。

hackernews · larsfaye · 8月24日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

<a id="item-6"></a>
### [OpenAI 限时下调 GPT-5.6 Sol API 价格](https://developers.openai.com/api/docs/pricing) ⭐️ 5.0/10

2026 年 8 月 21 日，OpenAI 宣布对 GPT-5.6 Sol 进行促销降价：输入价格降至每百万 token 4 美元（降幅 20%），输出价格降至每百万 token 20 美元（降幅 33.3%），该价格至少持续到 2026 年 11 月 21 日。

hackernews · tosh · 8月24日 15:22 · [社区讨论](https://news.ycombinator.com/item?id=49421074)