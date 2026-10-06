---
layout: default
title: "Horizon 每日速递：2026-10-06"
description: "AI 精选的技术与研究日报"
date: 2026-10-06
lang: zh
locale: zh-CN
---

> 从 47 条内容中筛选出 5 条重要资讯。

---

1. [Reflection 发布 501B 开放权重稀疏 MoE 模型 Beam](#item-1) ⭐️ 8.0/10
2. [Cloudflare 推出面向 AI 代理的 Web Search API](#item-2) ⭐️ 7.0/10
3. [GitHub Copilot CLI v1.0.92 发布：新增配置子命令并修复 MCP 认证](#item-3) ⭐️ 6.0/10
4. [Mastra core 1.74.0 发布：工具可读完整对话，记忆历史支持搜索](#item-4) ⭐️ 6.0/10
5. [Anthropic Cowork 将智能体 VM 从本地迁移到每会话云端沙盒](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Reflection 发布 501B 开放权重稀疏 MoE 模型 Beam](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

**级别**: 核心必看

Reflection AI 发布了其首个开放权重模型 Beam，这是一个稀疏混合专家（MoE）架构，总参数 5010 亿、激活参数 230 亿，明确定位于编程、推理和智能体任务。官方称 Beam 在 23.8 万亿个精选 token 上完成预训练，并额外投入了强化学习训练，性能可匹配或超过其他同规模的开源基础模型。 Beam 为开发者提供了一个新的西方开放权重前沿模型选项，其较低的激活参数量使推理成本更接近小模型，从而给目前由中国实验室（如 DeepSeek、Moonshot AI）主导的开放权重格局增加了竞争压力。 与同量级的 DeepSeek V4.1 Flash 相比，Beam 每个 token 激活的参数多得多（230 亿，而后者预填充 80 亿、解码 160 亿），但预训练 token 预算据称更小：博文写的是 23.8 万亿，而 HN 上的对比表把 Beam 记为 28T、DeepSeek V4.1 Flash 为 45T，因此这一数字需谨慎看待。

hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 稀疏 MoE 模型包含许多“专家”子网络，但每个 token 只会被路由到其中少数几个，因此总参数量可以极大，而单 token 推理算力却接近一个小得多的稠密模型；“开放权重”则指公开发布训练好的参数供下载，但修改和再分发的许可条款因模型而异。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://reflection.ai/blog/introducing-beam">Beam: Reflection&#x27;s 501B open-weight model</a></li>
<li><a href="https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/">Reflection debuts Beam, an open-weight AI model to rival Chinese models ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**社区讨论**: HN 评论者欢迎又多了一个开放权重模型，但讨论集中在竞争力上：有人贴出对比表，认为 Beam 的激活参数量远高于 DeepSeek V4.1 Flash 而预训练 token 更少；也有人认为西方开放模型仍落后于更小的中国免费模型，并呼吁出现更多供应商以降低对单一国家的依赖。还有人注意到演示中的泛化测试——一个几天前才出现的 180×90 网格谜题——Beam 据称覆盖率达 95.5%，介于 Opus 5 的 92.5% 与另一模型之间，引发了兴趣与质疑。

**标签**: `#open-weight-models`, `#mixture-of-experts`, `#coding-agents`, `#model-release`, `#llm-benchmarks`

---

<a id="item-2"></a>
## [Cloudflare 推出面向 AI 代理的 Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/) ⭐️ 7.0/10

**级别**: 核心必看

2026 年 10 月 2 日，Cloudflare 推出 Web Search API，为 AI 代理提供单一搜索端点，请求会被转发给 Ceramic.ai、Linkup、Exa 等第三方搜索提供商且不加价，三者的价格分别为每 1000 次请求 0.25 美元、5 美元和 7 美元。 它为代理开发者提供了一个不加价、可在多家搜索后端之间切换的中立入口，但决定代理产品能否实现“可分享的对话记录”这类功能的，可能是服务商关于结果存储与再分发的条款，而不是名义价格。 Simon Willison 指出，Ceramic 的条款据称禁止收集或聚合搜索结果，这会让代理系统即使搜索成本很低，也无法保存返回结果或提供“分享对话记录”按钮。

hackernews · tosh · 10月5日 10:47 · [社区讨论](https://news.ycombinator.com/item?id=49963171)

**背景**: 这类搜索 API 通常通过抓取或授权 Google、Bing 等引擎来实现；Cloudflare 在此扮演聚合与代理角色，本身并不运营搜索索引，此前也已通过 AI Gateway 的提供商代理端点暴露搜索能力。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/">Web Search API</a></li>
<li><a href="https://www.creativeainews.com/articles/cloudflare-web-search-api-agent-search-prices-2026/">Cloudflare Web Search API vs Exa, Brave, Tavily: Prices</a></li>
<li><a href="https://developers.cloudflare.com/ai-gateway/usage/web-search/">Web Search · Cloudflare AI Gateway docs</a></li>

</ul>
</details>

**社区讨论**: 评论区整体偏怀疑：simonw 认为能否存储与再分发结果才是决定性问题；iphonecorridor 认为 Gemini Flash Lite 2.5 每天免费 1000 次 Google 搜索，优于 Flash Lite 3.x 每月 5000 次加按次收费；denkmoon 和 binarymax 质疑 Cloudflare 作为“互联网守门人”的定位以及是否有必要居中代理；qznc 则更倾向于通过 hister CLI 使用本地索引。

**标签**: `#Cloudflare`, `#Web Search API`, `#AI agents`, `#search API`, `#developer tools`

---

## 更多动态

<a id="item-3"></a>
### [GitHub Copilot CLI v1.0.92 发布：新增配置子命令并修复 MCP 认证](https://github.com/github/copilot-cli/releases/tag/v1.0.92) ⭐️ 6.0/10

GitHub Copilot CLI 于 2026-10-05 发布 v1.0.92，新增 \`copilot config\` 子命令，可列出、读取、设置和删除配置，并加入对话前的 Ctrl+E 环境选择器，用于在本地运行与云端运行之间切换。该版本还带来一批 MCP 可靠性与认证修复，例如 Entra 保护的 MCP 服务器可静默续期仅含访问令牌的凭据，以及旧的 HTTP+SSE MCP 连接在消息 POST 始终未被确认时会按服务器配置的超时进行限制，不再无限挂起。

github · copilot-cli-release-app\[bot\] · 10月5日 19:42

<a id="item-4"></a>
### [Mastra core 1.74.0 发布：工具可读完整对话，记忆历史支持搜索](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.74.0) ⭐️ 6.0/10

@mastra/core 1.74.0 在标准与持久化 agent 循环中为工具执行上下文新增了 \`agent.getMessages\(\)\`，使工具能够读取当前完整对话，包括已记住的消息和本次运行中产生的回复。同时 \`getObservationalMemoryHistory\` 新增了 groupId 分组过滤、sortDirection 显式排序和按 recordId 直接查询，而 @mastra/playground-ui 移除了 \`anchorTraceId\` 与 \`ThreadTrace.LoadMoreSentinel\`，属于破坏性变更。

github · PaulieScanlon · 10月5日 09:31

<a id="item-5"></a>
### [Anthropic Cowork 将智能体 VM 从本地迁移到每会话云端沙盒](https://simonwillison.net/2026/Oct/5/felix-rieseberg/) ⭐️ 6.0/10

Anthropic 工程师 Felix Rieseberg 介绍了 Cowork 的架构变更：旧版在云端做模型推理、但工具调用运行在交付到用户电脑上的 Anthropic 提供的 VM 中；新版则把模型推理和 VM 都放到云端，每个会话拥有各自独立的沙盒，会话之间不共享状态。当云端 VM 需要用户设备上的东西（例如某个文件）时，改由桌面应用负责完成该文件访问的工具调用。

rss · Simon Willison · 10月5日 23:56