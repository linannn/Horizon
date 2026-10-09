---
layout: default
title: "Horizon 每日速递：2026-10-09"
description: "AI 精选的技术与研究日报"
date: 2026-10-09
lang: zh
locale: zh-CN
---

> 从 59 条内容中筛选出 8 条重要资讯。

---

1. [JetBrains 开源 Mellum2.1：面向编码智能体的 12B MoE 模型](#item-1) ⭐️ 7.0/10
2. [Zenity 发现：一条提示词即可劫持 AWS 账户内全部 AI 智能体](#item-2) ⭐️ 7.0/10
3. [Claude Haiku 5.5 发布：最高降价 90%，计算机操作能力大幅跃升](#item-3) ⭐️ 7.0/10
4. [OpenAI Codex CLI rust-v0.162.0 发布：新增托管 Git worktree 与任务置顶](#item-4) ⭐️ 6.0/10
5. [OpenHands v1.26.0 发布：新增 verify-openhands CLI 与纠正性提示](#item-5) ⭐️ 6.0/10
6. [Pragmatic Engineer：科技公司内部“氛围编程应用”兴起](#item-6) ⭐️ 4.0/10
7. [LangChain 推出 Restock 演示：智能体可用 Stripe Link 完成支付](#item-7) ⭐️ 4.0/10
8. [Claude 九月回顾：Chat 与 Cowork 合并，5.5 系列模型上线](#item-8) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [JetBrains 开源 Mellum2.1：面向编码智能体的 12B MoE 模型](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 7.0/10

**级别**: 核心必看

JetBrains 发布了 Mellum2.1，这是其 6 月开源的 12B 混合专家（MoE）模型的下一代版本，架构与 2.5B 激活参数规模保持不变，但改为在真实环境中进行强化学习训练。该模型明确定位于编码智能体（coding agents），以及运行在用户自有硬件上的快速子智能体。 这为开发者本地方案提供了一个开放权重、低延迟的新选择，用于智能体编排；对于需要权衡托管式编码智能体 API 的成本、隐私与速度的团队而言，这一选择颇具意义。 目前提供的公告内容被截断，未给出基准测试分数、许可证条款或实测任务表现，因此 Mellum2.1 所宣称的速度与智能体能力尚未得到验证。

rss · JetBrains AI · 10月8日 12:00

**背景**: 混合专家（MoE）架构为每个输入只激活一部分参数，这正是 12B 模型仅以 2.5B 激活参数运行、推理速度较快的原因。Mellum 是 JetBrains 自研的开源编码模型系列，其第 2 版于 6 月发布。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/">Mellum2.1 Gets to Work: A Fast Open Model for Coding Agents</a></li>
<li><a href="https://otf-kit.dev/blog/mellum2-open-source">JetBrains open -sources Mellum 2 for private, high-speed AI coding ...</a></li>
<li><a href="https://deepwiki.com/InterviewReady/ai-engineering-resources/4.1-mixture-of-experts-%28moe%29">Mixture of Experts (MoE) | DeepWiki</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#open-source-models`, `#mixture-of-experts`, `#local-llm`, `#jetbrains`

---

<a id="item-2"></a>
## [Zenity 发现：一条提示词即可劫持 AWS 账户内全部 AI 智能体](https://the-decoder.com/a-single-prompt-was-enough-to-hijack-every-ai-agent-in-an-aws-account-zenity-researchers-found/) ⭐️ 7.0/10

**级别**: 核心必看

Zenity Labs 披露了一条名为 AgentCorruption 的漏洞链：只需向一个公开可访问的 Amazon Bedrock AgentCore 智能体发送一条提示词，攻击者就能滥用 169.254.169.254 元数据服务窃取其 AWS 凭据，进而控制同一 AWS 账户、同一区域内的所有 AgentCore 智能体。研究人员称，攻击者可借此读取私人对话、源代码和已存储的凭据，还能篡改智能体的长期记忆；AWS 随后修复了该问题，并大幅收紧了智能体的默认权限。 这一发现表明，针对单个暴露在外面的智能体实施提示词注入，就可能升级为整个账户层面的云环境失陷，因此对每个智能体单独限定 IAM 权限范围、收紧默认权限，已成为所有在 AWS 上部署智能体的开发者必须立即处理的问题。 The Next Web 在报道末尾附上更正说明：该研究覆盖的是单个 AWS 账户与单个区域内的智能体，而非整个区域中的所有 AgentCore 智能体，因此实际演示的影响范围限于同一账户同一区域，而非整个区域。

rss · The Decoder · 10月8日 13:01

**背景**: Amazon Bedrock AgentCore 是 AWS 用于部署 AI 智能体的托管运行时，智能体通常会带有工具调用能力和各自的 IAM 角色。169.254.169.254 是云工作负载用于获取临时凭据的内部链路本地地址，正因为它可以被无限制访问，单个智能体才会成为攻破整个账户的立足点。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/a-single-prompt-was-enough-to-hijack-every-ai-agent-in-an-aws-account-zenity-researchers-found/">A single prompt was enough to hijack every AI agent in an AWS account, Zenity researchers found</a></li>
<li><a href="https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents">Zenity says one prompt took over every AgentCore agent in an ...</a></li>
<li><a href="https://www.spke.com/en/ai/article/1904">A single prompt was enough to hijack every AI agent in an AWS ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AWS Bedrock AgentCore`, `#prompt injection`, `#agent security`, `#cloud IAM`

---

<a id="item-3"></a>
## [Claude Haiku 5.5 发布：最高降价 90%，计算机操作能力大幅跃升](https://the-decoder.com/claude-haiku-5-5-arrives-with-massive-price-cuts-proving-the-ai-pricing-arms-race-is-far-from-over/) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 发布了 Claude 5.5 家族中最快、最便宜的小模型 Claude Haiku 5.5，其 token 价格相比上一代最高下调 90%。在 OSWorld 计算机操作基准测试中，该模型得分从 15.7% 跃升至 72.4%；Anthropic 同时将其定位为面向数据查询、客户支持等高并发任务的模型。 大幅降价叠加计算机操作能力的跨越式提升，会对竞争对手的小模型定价形成压力，并改变开发者构建浏览器与桌面自动化智能体时的部署成本结构。 实际节省幅度小于宣传数字：Anthropic 采用的新分词器在每个任务上消耗的 token 更多，因此每完成一个任务的实际成本降幅被部分抵消；不同媒体的报道口径也不一致（本文称“最高降低 90%”，另有报道称降价 75% 至每百万 token 0.10 美元）。

rss · The Decoder · 10月8日 10:30

**背景**: Haiku 是 Anthropic 三层模型体系 Opus/Sonnet/Haiku 中最小、最便宜的一档，面向高并发调用而非最强推理能力。OSWorld 是一个成熟的基准测试，用 Ubuntu 和 Windows 上的真实桌面任务来衡量智能体通过虚拟鼠标和键盘操作电脑的能力。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/claude-haiku-5-5-arrives-with-massive-price-cuts-proving-the-ai-pricing-arms-race-is-far-from-over/">Claude Haiku 5.5 arrives with massive price cuts proving the AI pricing arms race is far from over</a></li>
<li><a href="https://finance.yahoo.com/technology/article/anthropic-reveals-haiku-55-model-as-ai-pricing-war-intensifies-180000423.html?fr=sycsrp_catchall">Anthropic reveals Haiku 5.5 model as AI pricing war intensifies</a></li>
<li><a href="https://tech-insider.org/anthropic-claude-haiku-5-5-price-cut-2026/">Claude Haiku 5.5 Slashes Price 75% to $0.10/M [2026]</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude Haiku`, `#LLM pricing`, `#computer use agents`, `#model release`

---

## 更多动态

<a id="item-4"></a>
### [OpenAI Codex CLI rust-v0.162.0 发布：新增托管 Git worktree 与任务置顶](https://github.com/openai/codex/releases/tag/rust-v0.162.0) ⭐️ 6.0/10

OpenAI 发布了 Codex CLI rust-v0.162.0，新增在受信任本地项目中创建和列出托管 Git worktree 的工具、在 agent Command Center 中按 \`p\` 键置顶任务、使用 \`/copy\` 导航转录文本块、让审批头部、提问、MCP 提示、横幅中的 URL 可点击，以及为自定义的 Responses 兼容模型提供商配置实时联网访问与远程压缩（remote compaction）能力。该版本还加入用于流式返回 promise 结果的 JavaScript 辅助函数、Code Mode 中可选择开启的排名式工具搜索，并修复了新 TUI 线程遵循服务器模型/推理默认值、\`apply\_patch\` 保留 CRLF 换行、以及 Linux/Windows 沙箱与安装器等问题。

github · github-actions\[bot\] · 10月8日 18:55

<a id="item-5"></a>
### [OpenHands v1.26.0 发布：新增 verify-openhands CLI 与纠正性提示](https://github.com/OpenHands/OpenHands/releases/tag/v1.26.0) ⭐️ 6.0/10

OpenHands 于 2026-10-08 发布 v1.26.0，新增了 verify-openhands 技能以及配套的 control-openhands CLI，并支持每日检查（daily pass）和带有实时配方（live recipes）的 20 多项行为映射。该版本还把空响应的纠正性提示（corrective nudge）改为信息提示形式展示，新增对已挂起工作空间的说明与切换选项，并收窄了自动化中的“needs review”状态。

github · openhands-release-bot\[bot\] · 10月8日 20:36

<a id="item-6"></a>
### [Pragmatic Engineer：科技公司内部“氛围编程应用”兴起](https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-of-building-internal) ⭐️ 4.0/10

Pragmatic Engineer 的“The Pulse”通讯指出，中型科技公司正出现一股新趋势：搭建内部平台，让非工程人员通过 AI 辅助的“氛围编程”自行构建内部网站和工具，并提到 Ramp 和 Stripe 的相关平台已在公司内部快速普及。同一期通讯还讨论了工程师是否真的热爱“难题”，以及欧盟和美国近期发布的开源模型。

rss · The Pragmatic Engineer · 10月8日 16:55

<a id="item-7"></a>
### [LangChain 推出 Restock 演示：智能体可用 Stripe Link 完成支付](https://www.langchain.com/blog/agents-that-can-pay-with-stripe-link) ⭐️ 4.0/10

LangChain 发布了一个名为 Restock 的示例智能体，它运行在 Managed Deep Agents 之上、以 Slack 为交互界面，能够搜索真实商品、构建购物车，并通过 Stripe Link 完成支付。该项目被定位为演示智能体如何安全地代替用户完成付款。

rss · AI 热榜 · 10月8日 16:21

<a id="item-8"></a>
### [Claude 九月回顾：Chat 与 Cowork 合并，5.5 系列模型上线](https://www.youtube.com/shorts/n9WfoNW2XnE) ⭐️ 4.0/10

一段 YouTube Short 回顾了 Anthropic 九月的 Claude 更新：Chat 与 Cowork 合并为一个统一的 Claude，工作流可放到云端运行、合上笔记本后仍能继续，并推出 Claude 5.5 系列，其中 Opus 5.5 负责重任务、Sonnet 5.5 用于快速修改。同一回顾还提到 Claude Docs 支持团队与 Claude 在同一文档中协作编辑，并可通过 /slides、/docs、/designs 命令直接生成对应格式的内容。

rss · AI 热榜 · 10月8日 15:53