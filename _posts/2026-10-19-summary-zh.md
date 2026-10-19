---
layout: default
title: "Horizon 每日速递：2026-10-19"
description: "AI 精选的技术与研究日报"
date: 2026-10-19
lang: zh
locale: zh-CN
---

> 从 24 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [Together Computer 发布 Hybrid Reasoning Agents：潜空间推理、文本行动的 LLM 智能体](#item-tech-news-1) ⭐️ 7.0/10
2. [DeepSeek 上线搜索抓取 API,千次成功请求 0.75 美元](#item-tech-news-2) ⭐️ 6.0/10
3. [llm-echo 0.5：模拟更真实的 token 用量](#item-tech-news-3) ⭐️ 5.0/10
4. [四台 Gemini 4 Argon 智能体自主击败《我的世界》末影龙](#item-tech-news-4) ⭐️ 4.0/10
5. [DeepSeek-V4.1-Flash 据报登顶 Code Arena WebDev 开源模型榜首](#item-tech-news-5) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Together Computer 发布 Hybrid Reasoning Agents：潜空间推理、文本行动的 LLM 智能体](https://arxiv.org/abs/2610.18861) ⭐️ 7.0/10

**级别**: 核心必看

Together Computer 在 arXiv 发布论文《Hybrid Reasoning Agents: LLM agents that think in latent space, act through text》，提出一种混合推理智能体架构：模型在潜空间中完成推理，但以外部文本形式发出动作。论文同时开源了位于 GitHub 的 HybridAgent 代码库，以及在 HuggingFace 上以集合页形式发布的预训练模型与数据，供后续研究复用。作者还给出了评估结果链接以便查证。

hackernews · allinonai · 10月18日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=50145337)

**「背景」** 现代 LLM 智能体的推理与外部交互通常以文本为媒介，这种基于显式 chain-of-thought 的路径可读性强，但 token 级生成成本较高；「潜空间推理」（latent reasoning）将中间步骤压缩为连续隐向量以降低开销，代价是难以原生调用工具、且推理过程不透明。HybridAgent 据此提出在同一生成流程中让模型动态切换潜空间思考与文本动作，从而在两条路线之间建立显式桥梁。另一条相关的技术线是 looped transformer——通过让隐藏状态在同一 Transformer 块上多次前向来扩充有效深度（在社区讨论中常被与 OpenAI 报告的 Astra 模型联系起来），其思路属于持续加深/循环隐状态本身，与 HybridAgent 依赖 latent/text 双模态显式切换的做法属于不同路线。

**「影响」** 对在 llama.cpp 等第三方推理引擎上试跑 Together Computer 14B 预训练模型的开发者而言，目前存在明显的兼容性问题：已有用户报告在 bartowski 8-bit 量化版本上对常见网页搜索与摘要任务出现长时循环重复生成，预计需要等待推理引擎针对该混合推理架构的更新或自行应用兼容补丁后才能稳定部署。

**「社区讨论」** 讨论沿着架构改进、应用迁移与部署兼容性三条线展开。amluto 认为既然已经支付了潜空间模式模型几乎完整的运行开销，可以加宽输入嵌入以同时容纳“Hybrid Link”后的潜空间向量与 token 嵌入，甚至直接对两者做向量加法来并行推理；notnullorvoid 希望把该方法迁移到 Qwen 3.8 27B，预期其常出现复述的推理输出能被更多地压缩在潜空间中；incognito124 询问该方案与 Astra 的 looped transformer 在潜空间推理上的本质差异。SwellJoe 在实战层面反馈，使用 bartowski 提供的 8-bit 量化 14B 模型在 llama.cpp（昨日版本）上对一个简单的网页搜索加摘要任务，与同体量的 Gemma 4 12B 形成对比，模型对同一段落变体连续生成约 5 分钟直至用完本轮预算，疑似 llama.cpp 需要针对该架构进行适配。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.18861">Hybrid Reasoning Agents: LLM agents that think in latent space, act through text</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and">GPT-6 Astra , Looped Transformers , and Hidden Reasoning</a></li>

</ul>
</details>

**标签**: `#agents`, `#research`, `#open-source`, `#llm-architecture`, `#latent-reasoning`

---

### 更多动态

<a id="item-tech-news-2"></a>
#### [DeepSeek 上线搜索抓取 API,千次成功请求 0.75 美元](https://api-docs.deepseek.com/guides/search/) ⭐️ 6.0/10

DeepSeek 推出托管式&quot;搜索与抓取\(search and fetch\)&quot;API,定价为每 1000 次成功请求 0.75 美元。该价格显著低于 Brave Search API 的 5 美元/千次和 Kagi API 的 12 美元/千次,面向构建搜索增强 AI 应用与代理的开发者。官方文档已在 api-docs.deepseek.com/guides/search/ 发布,但目前可获取的仅含定价信息,尚未披露架构细节或检索质量数据。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

<a id="item-tech-news-3"></a>
#### [llm-echo 0.5：模拟更真实的 token 用量](https://simonwillison.net/2026/Oct/18/llm-echo/) ⭐️ 5.0/10

Simon Willison 发布 llm-echo 0.5，这是他为 LLM CLI 编写的调试插件的最新版本。该插件提供一个不调用真实大模型的 &quot;echo 模型&quot;，仅把传入的提示原样回显，用于本地测试。0.5 版本的主要变化是：模拟的 token 用量统计现在会考虑工具调用（tool calls）、系统提示（system prompts）和推理 token（reasoning tokens），使测试结果更接近真实 API 行为。可通过 \`uvx --with llm-echo llm -m echo &\#x27;hi there&\#x27; -o thinking 1 --usage\` 调用，例如输入 &quot;hi there&quot; 时输出 &quot;Token usage: 2 input, 24 output&quot;。

rss · Simon Willison · 10月18日 23:16

<a id="item-tech-news-4"></a>
#### [四台 Gemini 4 Argon 智能体自主击败《我的世界》末影龙](https://the-decoder.com/four-gemini-4-argon-agents-beat-minecraft-without-any-human-help/) ⭐️ 4.0/10

据 The Decoder 报道，四台运行在 Google Gemini 4 Argon 上的 AI 智能体在无人干预的情况下自主完成了《我的世界》\(Minecraft\) 的通关流程，最终击败末影龙（Ender Dragon）。智能体之间没有预设角色或策略，自行协调分工，并在过程中编写了 2,783 个程序、交换了 229 条聊天消息，死亡 605 次，整次运行成本约 1,620 美元。该报道未提供任何关于协调机制、提示工程、工具链或可复用工程细节的技术说明，且 &quot;Gemini 4 Argon&quot; 这一模型名称目前无法独立验证，发布日期为 2026 年 10 月，超出本模型的知识截止时间，因此上述数字仅为该媒体单方面声明。

rss · The Decoder · 10月18日 12:39

<a id="item-tech-news-5"></a>
#### [DeepSeek-V4.1-Flash 据报登顶 Code Arena WebDev 开源模型榜首](https://x.com/arena/status/2111894091168682086) ⭐️ 4.0/10

Arena 在 X 上发文称，DeepSeek-V4.1-Flash-20261017（Max 版本）成为其 Code Arena: WebDev 榜单上的开源模型第一名，超越了 Kimi K3（Max），并表示运行成本约为后者的十分之一。该公告未给出具体分数、模型卡、API 接入方式或权重发布等可核验的技术细节；版本号中的日期 2026-10-17 为未来日期，排名及“便宜约 10 倍”的比较均为 Arena 的单方声明，目前没有 DeepSeek 官方发布或独立测评加以佐证。

rss · AI 热榜 · 10月18日 18:56