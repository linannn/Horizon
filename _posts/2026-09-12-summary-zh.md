---
layout: default
title: "Horizon 每日速递：2026-09-12"
description: "AI 精选的技术与研究日报"
date: 2026-09-12
lang: zh
locale: zh-CN
---

> 从 51 条内容中筛选出 6 条重要资讯。

---

1. [OpenAI 发布 Agents API 公测版，开放云端智能体基础设施](#item-1) ⭐️ 8.0/10
2. [DeepSeek V4.1 Flash 大幅降价、原生带视觉，v4-pro 请求将被强制迁移](#item-2) ⭐️ 7.0/10
3. [Claude Code v2.1.269 发布：新增插件评测、输出样式切换与 OTEL vcs 标签](#item-3) ⭐️ 6.0/10
4. [GitHub Copilot CLI v1.0.84-5 新增会话与记忆导入命令](#item-4) ⭐️ 6.0/10
5. [Simon Willison 指出 OpenRouter 自动路由风险，并给出 provider.only 解决方案](#item-5) ⭐️ 6.0/10
6. [Anthropic 的 Boris Cherny：Claude 写的代码应有更高标准](#item-6) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 Agents API 公测版，开放云端智能体基础设施](https://the-decoder.com/openais-new-agents-api-gives-developers-the-infrastructure-behind-codex-and-chatgpt/) ⭐️ 8.0/10

**级别**: 核心必看

OpenAI 以公测形式发布 Agents API，开发者可据此构建能自主运行数小时、执行代码、处理文件并把任务交接给子智能体的云端智能体。除 token 用量之外不收取任何额外费用，Cloudflare、Vercel 和 Oracle 还提供额外的沙箱环境。 OpenAI 把驱动 Codex 和 ChatGPT 的同一套托管智能体基础设施打包成面向开发者的产品，这降低了团队构建长时运行编码与智能体工作流的工程门槛，也加大了对 Anthropic 的 Claude Agent SDK 等竞品智能体平台的压力。 据 OpenAI 说明，该 API 由开源的 Codex harness 驱动：OpenAI 负责运行和维护这一 harness，并托管会话、编排、上下文压缩与恢复，而开发者可以查看其公开代码库，并自行提供工具与执行环境。

rss · The Decoder · 9月11日 08:11

**背景**: 要让自主智能体稳定运行，远不止调用模型那么简单，还需要托管会话、自动上下文管理、并行工具调用、安全的代码执行沙箱，以及在步骤失败时进行恢复。Codex 是 OpenAI 的编码智能体，ChatGPT 是其聊天机器人，而 Agents API 把支撑它们的内部门技术栈变成了可对外调用的服务。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/openais-new-agents-api-gives-developers-the-infrastructure-behind-codex-and-chatgpt/">OpenAI&#x27;s new Agents API gives developers the infrastructure behind Codex and ChatGPT</a></li>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API - developers.openai.com</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Agents API`, `#coding agents`, `#developer tools`, `#agent infrastructure`

---

<a id="item-2"></a>
## [DeepSeek V4.1 Flash 大幅降价、原生带视觉，v4-pro 请求将被强制迁移](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&amp;mid=2247511119&amp;idx=1&amp;sn=0f53b5017e41b16afc9b201966ce2bda) ⭐️ 7.0/10

**级别**: 核心必看

DeepSeek 推出多模态 MoE 模型 V4.1 Flash，骨干参数 552B、上下文最长支持 100 万 token；据实测文章，其缓存命中输入价格降至原先的七分之一以下、输出成本下调三分之二。自 9 月 14 日中午 12 点（04:00 UTC）起，所有发往 deepseek-v4-pro 的请求将被路由到 V4.1 Flash，并按 V4.1 Flash 的价格计费，DeepSeek 正在逐步淘汰 V4-Pro。 现有 DeepSeek API 用户无需改代码就会被迁移到更便宜的新模型，这直接改变了基于 DeepSeek 构建的团队的成本结构，也表明 DeepSeek 正把旗舰多模态能力集中到单一低价模型上，进一步加剧国内大模型 API 的性价比竞争。 第三方实测提醒，单价下降并不等于总花费下降：V4.1 Flash 在复杂任务上倾向多开子 Agent，在相同计费条件下总消耗比旧版 V4 Flash 高约 36%，长上下文能力也仍待提升；另有报道称 9 月 10 日已先对缓存命中输入降价 60%，因此“降价 7 倍多”的确切倍数取决于所比较的轮次与基准价。

rss · AI 热榜 · 9月11日 04:24

**背景**: DeepSeek 是一家位于杭州、由幻方量化支持的人工智能公司，以发布开放权重模型著称；其 API 对命中上下文缓存的输入 token 与未命中的输入 token 采用不同单价，因此缓存命中价格对反复发送长提示词的对话与 Agent 应用而言是关键的成本杠杆。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&amp;mid=2247511119&amp;idx=1&amp;sn=0f53b5017e41b16afc9b201966ce2bda">实测 DeepSeek V4.1 Flash：价格大降、原生带视觉，作者用游戏与城市生成任务验证表现</a></li>
<li><a href="https://deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/DeepSeek-V4.1-Flash · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 从此前内测者的反馈看，大家普遍认为原生视觉理解是本轮最大升级——模型终于能自己看图；但对成本、速度和交付表现的评价较为分化：有人用 3 亿 token、14 组任务测出总花费反而高于上一代，也有人指出复杂任务更容易多开子 Agent，长上下文能力仍是短板。

**标签**: `#DeepSeek`, `#LLM pricing`, `#model release`, `#multimodal`, `#AI engineering`

---

## 更多动态

<a id="item-3"></a>
### [Claude Code v2.1.269 发布：新增插件评测、输出样式切换与 OTEL vcs 标签](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) ⭐️ 6.0/10

Claude Code v2.1.269 发布，新增 \`claude plugin eval\` 命令，可对插件的评测套件运行打分并输出可复现的 JSON 与 HTML 报告；同时加入 \`/output-style \[name\]\` 用于列出和切换输出样式，且支持远程控制、云端及其他无头会话。该版本还新增取值 1–256 的 \`CLAUDE\_CODE\_WORKFLOW\_MAX\_CONCURRENT\_AGENTS\` 以提高 Workflow 工具单次运行的并发代理上限，通过 \`bashEditDiffEnabled\` 在 Bash 工具结果中展示文件改动 diff，加入 \`OTEL\_METRICS\_INCLUDE\_REPOSITORY\` 以输出 \`vcs.\*\` 标签，并提供 \`CLAUDE\_CODE\_GATEWAY\_MODEL\_DISCOVERY\_TIMEOUT\_MS\` 控制网关 \`/v1/models\` 的发现超时。

github · ashwin-ant · 9月11日 19:17

<a id="item-4"></a>
### [GitHub Copilot CLI v1.0.84-5 新增会话与记忆导入命令](https://github.com/github/copilot-cli/releases/tag/v1.0.84-5) ⭐️ 6.0/10

GitHub Copilot CLI 发布了 v1.0.84-5 版本，新增了针对语义化 JSONL 交换格式的会话（session）与记忆（memory）导入命令；同时把命令行解析从 Commander 迁移到 Rust 语法解析器，使 shell 补全与 CLI 解析基于同一套语法；/usage 的用量明细中开始显示按模型划分的 AI Credit 消耗。该版本还修复了子代理（subagent）启动时的问题，使其能够遵循全局与自定义指令中显式指定的模型、推理强度（reasoning effort）和上下文层级偏好。

github · copilot-cli-release-app\[bot\] · 9月11日 21:51

<a id="item-5"></a>
### [Simon Willison 指出 OpenRouter 自动路由风险，并给出 provider.only 解决方案](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) ⭐️ 6.0/10

在 2026 年 9 月 11 日的一篇链接短文中，Simon Willison 转述了 Mohamed Moustafa 的警告：OpenRouter 的自动提供商路由可能把同一个模型 ID 的请求分发到运行不同服务软件、不同优化与配置的后端上，导致模型行为并不一致。Moustafa 还指出，部分提供商对视觉模型甚至不具备视觉能力，而 reasoning effort 选项的处理方式也会因后端不同而存在差异。

rss · Simon Willison · 9月11日 22:49

<a id="item-6"></a>
### [Anthropic 的 Boris Cherny：Claude 写的代码应有更高标准](https://simonwillison.net/2026/Sep/11/boris-cherny/) ⭐️ 5.0/10

Anthropic 的 Claude Code 负责人 Boris Cherny 在 X 上发帖表示，“由 Claude 编写的生产代码应当比人类编写的代码有更高的门槛”，并列举了 Anthropic 用来落实这一点的多重护栏：大量 lint 规则、大量测试、由 Claude 驱动的端到端测试、每天运行的 Claude 驱动的模糊测试（fuzzer）、自动化代码审查与安全审查，以及自动化代码重构。

rss · Simon Willison · 9月11日 17:47