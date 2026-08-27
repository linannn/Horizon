---
layout: default
title: "Horizon 每日速递：2026-08-27"
description: "AI 精选的技术与研究日报"
date: 2026-08-27
lang: zh
locale: zh-CN
---

> 从 71 条内容中筛选出 14 条重要资讯。

---

1. [Qwen3.8-Flash 开源，预览 Qwen4 架构](#item-1) ⭐️ 9.0/10
2. [智谱发布 GLM-5.3-Flash：低成本开放权重多模态模型](#item-2) ⭐️ 8.0/10
3. [Qwen3.8-Flash-Next：N-gram MoE 预览 Qwen4，每 token 仅激活 6B 参数](#item-3) ⭐️ 8.0/10
4. [Qwen3.8-Flash-Next：开源权重多模态 MoE 模型，提前预览 Qwen4 架构](#item-4) ⭐️ 8.0/10
5. [Claude in Chrome 正式向所有付费用户全面开放](#item-5) ⭐️ 8.0/10
6. [智谱开源 GLM-5.3-Flash：320B 参数、AA 指数 57 分、定价为 Opus 4.8 的 1/40](#item-6) ⭐️ 8.0/10
7. [Claude Code v2.1.247 新增成本优化命令与反馈工具](#item-7) ⭐️ 7.0/10
8. [Cline 桌面版 v0.0.19 修复内存泄漏并更新模型目录](#item-8) ⭐️ 7.0/10
9. [阿里巴巴推出 Qwen3.8-Flash-Next，主打极致成本效率的混合专家模型](#item-9) ⭐️ 7.0/10
10. [IBM 以 Apache 2.0 许可发布开源权重 Granite 4.2 系列，内置智能体能力](#item-10) ⭐️ 7.0/10
11. [Warp 如何在 Claude 上构建自我改进的智能体](#item-11) ⭐️ 7.0/10
12. [实测豆包工作集成飞书：8 个实用技巧](#item-12) ⭐️ 7.0/10
13. [保罗·迪克斯称赞 AI 能够编写并优化百万行代码库](#item-13) ⭐️ 4.0/10
14. [Lovable CTO：SaaS 的未来是智能体可用的应用](#item-14) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Qwen3.8-Flash 开源，预览 Qwen4 架构](https://x.com/Alibaba_Qwen/status/2092636376990990503) ⭐️ 9.0/10

**级别**: 核心必看

阿里巴巴通义千问发布了 Qwen3.8-Flash（官方资料中也称为 Qwen3.8-Flash-Next），这是一款开放权重的多模态 MoE 模型，作为 Qwen4 架构的早期预览。该模型总参数 125B，每 token 仅激活 6B 参数，训练成本仅为 Qwen3.7-Plus 的 1/9，API 定价为每 1M 输入 tokens $0.16、每 1M 输出 tokens $0.47。 这一发布意义重大，因为它以开放权重模型的形式让开发者提前接触到 Qwen4 架构，而且训练成本大幅降低、API 定价具有竞争力，可能会影响开源 AI 生态中开发者的模型选型决策。 官方公告中该模型名为 Qwen3.8-Flash-Next，原生上下文长度为 262K tokens，可扩展至 1M tokens，并且还计划发布 FP8 版本。

rss · AI 热榜 · 8月26日 15:32

**背景**: 混合专家（MoE）是一种模型架构，每个 token 只激活一部分参数，从而以较低的训练和推理成本实现很大的总参数量。阿里巴巴的通义千问（Qwen）系列是知名的开放权重语言和多模态模型家族，此次发布预览了后续 Qwen4 预计采用的架构。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/Alibaba_Qwen/status/2092636376990990503">Qwen3.8-Flash 开源，Qwen4 架构预览</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next: A New Architecture, Towards ...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#MoE`, `#Open Source Model`, `#AI Pricing`, `#Multimodal`

---

<a id="item-2"></a>
## [智谱发布 GLM-5.3-Flash：低成本开放权重多模态模型](https://z.ai/blog/glm-5.3-flash) ⭐️ 8.0/10

**级别**: 核心必看

智谱（Z.ai）发布了 GLM-5.3-Flash，这是一款开放权重的多模态模型，总参数 320B、激活参数 18B，以极低的成本提供接近 GLM-5.3 的性能。权重已在 Hugging Face 上发布，并支持部署在国产 AI 芯片上。 这次发布使接近前沿的开放权重智能变得前所未有地实惠，为开发者提供了可信赖的低成本替代专有 API 方案，并加剧了编程与智能体 AI 领域的竞争。 GLM-5.3-Flash 采用混合专家（MoE）架构，结合混合 KDA 与稀疏 MLA 注意力机制，原生 FP8 权重，支持多 token 预测，并拥有 100 万 token 的上下文窗口。

hackernews · Philpax · 8月26日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49449507)

**背景**: GLM 是智谱（Z.ai）旗舰级的开放权重大语言模型系列，历史上多采用 MIT 或 Apache 2.0 等宽松许可证。GLM-5.3-Flash 是继 GLM-5.3 之后的又一新作，后者曾在编程与智能体基准上创下开源纪录。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.3-flash">GLM-5.3-Flash</a></li>
<li><a href="https://unsloth.ai/docs/models/glm-5.3">GLM-5.3-Flash | Unsloth Documentation</a></li>
<li><a href="https://recipes.vllm.ai/zai-org/GLM-5.3-Flash">zai-org/ GLM-5.3-Flash | vLLM Recipes</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者大多持热情态度，有评测认为它比 DeepSeek V4 Flash 更聪明更便宜，性能大致与 Sol Medium 相当但成本低得多。也有人对智谱（Z.ai）的服务条款表示担忧，认为其过于宽泛，包括对输入和输出的永久授权以及对内容和讨论的模糊限制。

**标签**: `#GLM-5.3-Flash`, `#model release`, `#open-source`, `#cost-efficiency`, `#AI infrastructure`

---

<a id="item-3"></a>
## [Qwen3.8-Flash-Next：N-gram MoE 预览 Qwen4，每 token 仅激活 6B 参数](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 8.0/10

**级别**: 核心必看

2026 年 8 月 26 日，通义千问发布 Qwen3.8-Flash-Next，一款多模态 MoE 模型，也是 Qwen4 架构的早期预览。该模型总参数 125B，另有 51B N-gram 嵌入，每 token 仅激活 6B 参数，训练成本约为 Qwen3.7-Plus 的 1/9，编码与办公任务能力更强。 这一架构预示着 Qwen4 的发展方向，并让高能力模型的推理成本更低，对构建编码或智能体（agentic）工作流的开发者以及受限于内存带宽的本地用户都很重要。 尽管每 token 只激活 6B 参数，但模型总参数约 176B（125B 主模型 + 51B N-gram 嵌入），量化难度不小；有评论者估计 4-bit 量化版很可能超过 100GB，可能无法放入 128GB 统一内存。

hackernews · AI 热榜 · 8月26日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=49448210)

**背景**: 混合专家（MoE）模型每个 token 只激活一部分参数，用更大的总内存换取更低的计算量。N-gram 嵌入最近在 DeepSeek 的论文中被讨论，Gemma 模型也使用了轻量版本，它能捕捉重复出现的 token 序列模式；Qwen 此前也用“Next”版本来预览架构，例如 Qwen3-Next 预览了 Qwen3.5。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>

</ul>
</details>

**社区讨论**: 评论区讨论热烈且务实：大家争论约 176B 的有效参数量能否被量化以塞进 128GB 统一内存，并请人解释 N-gram 嵌入的直觉。Simon Willison 在 DGX Spark 上用 GGUF 跑了四种推理强度（reasoning level）的实测，表示没有像 Qwen3.8-27B 那样让他满意的输出。也有人认为，一旦 llama.cpp 支持落地，6B 激活参数对内存带宽受限的 Strix Halo 设备将是重大利好。

**标签**: `#Qwen`, `#AI model release`, `#sparse activation`, `#N-gram embeddings`, `#LLM`

---

<a id="item-4"></a>
## [Qwen3.8-Flash-Next：开源权重多模态 MoE 模型，提前预览 Qwen4 架构](https://simonwillison.net/2026/Aug/26/qwen38-flash-next/) ⭐️ 8.0/10

**级别**: 核心必看

Qwen 发布了 Qwen3.8-Flash-Next，这是一个开源权重的多模态 MoE 模型，总参数 125B、激活参数仅 6B，作为 Qwen4 架构的早期预览版本。配套的 Qwen3.8-Flash 则是注重生产环境的官方版本，默认支持 1M 上下文长度并内置工具。 由于这是 Qwen4 架构的开源权重早期预览，它让开源 AI 社区能提前了解 Qwen 的设计方向，同时开发者只需 6B 激活参数即可在本地运行大型 MoE 模型。 Simon Willison 测试了两种 Unsloth GGUF 量化版本——72.5GB 的 UD-IQ1\_S 和 78.9GB 的 UD-Q2\_K\_XL，其中他最喜欢的结果来自较大量化版本的 xhigh 推理力度设置。

rss · Simon Willison · 8月26日 23:52

**背景**: MoE（混合专家）模型每次前向计算只激活一部分参数，因此 125B 参数的模型可以用接近更小模型的计算量来运行。Qwen 官方表示该架构在注意力、残差、嵌入和优化四个方面做了升级，Unsloth 也提供了本地部署用的量化版本。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/26/qwen38-flash-next/">Qwen3.8-Flash-Next</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next: A New Architecture, Towards ...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>

</ul>
</details>

**标签**: `#qwen`, `#open-weights`, `#multimodal`, `#moe`, `#model-release`

---

<a id="item-5"></a>
## [Claude in Chrome 正式向所有付费用户全面开放](https://claude.com/blog/claude-in-chrome-generally-available) ⭐️ 8.0/10

**级别**: 核心必看

Anthropic 宣布 Claude in Chrome 现已面向所有付费 Claude 套餐全面开放。现在 Claude 可以在浏览器中自主执行操作，无需用户逐步审批，并在每次操作前由安全分类器进行验证。 此次发布意义重大，因为它让 AI 助手从对话协助迈向自主浏览器操作，将影响开发者和企业团队构建及信任浏览器自动化工作流的方式。 评测显示，在启用探测与安全分类器后，从 Opus 4.8 起的所有模型均未出现提示注入攻击成功的案例。

rss · AI 热榜 · 8月26日 18:02

**背景**: Claude 是 Anthropic 开发的 AI 助手，采用 Constitutional AI 训练以保证安全与可靠。提示注入是一种攻击手段，攻击者将恶意输入伪装成合法指令，从而操纵大语言模型。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://claude.com/blog/claude-in-chrome-generally-available">Claude in Chrome 正式全面上线</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Claude`, `#browser automation`, `#AI agents`, `#Anthropic`, `#product release`

---

<a id="item-6"></a>
## [智谱开源 GLM-5.3-Flash：320B 参数、AA 指数 57 分、定价为 Opus 4.8 的 1/40](https://mp.weixin.qq.com/s?__biz=MzkyMzI3NzQ0Mg%3D%3D&amp;mid=2247494157&amp;idx=1&amp;sn=6837b15a07d2518842eb6c6b53a3eb3c) ⭐️ 8.0/10

**级别**: 核心必看

智谱发布并开源了 GLM-5.3-Flash（320B-A18B），这是 GLM-5 系列首个原生多模态模型，AA 综合智能指数 57 分，与 Claude Opus 4.8 持平。其定价为 GLM-5.3 的 1/10，限时折扣价为 Opus 4.8 的 1/40，并已接入 ZCode 等平台开放 API 调用。 这一开源发布以旗舰级基准分数和极具竞争力的定价，可能重塑开发者对编程代理和 API 供应商的选择，加剧与 Opus 4.8 等专有前沿模型的竞争。 该模型采用稀疏注意力与线性注意力混合架构，推理服务已运行在国产芯片集群上。

rss · AI 热榜 · 8月26日 14:11

**背景**: GLM（通用语言模型）是中国 AI 公司智谱（Z.ai）开发的开源权重大型语言模型系列。注意力机制在效率上有所不同：稀疏注意力只对选定的 token 子集计算精确注意力，线性注意力以更低复杂度近似完整注意力，而混合设计旨在平衡质量与长上下文效率。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzkyMzI3NzQ0Mg%3D%3D&amp;mid=2247494157&amp;idx=1&amp;sn=6837b15a07d2518842eb6c6b53a3eb3c">GLM-5.3-Flash 开源：320B 总参数、AA 指数 57 分，定价为 Opus 4.8 的 1/40</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_%28AI%29">GLM (AI) - Wikipedia</a></li>
<li><a href="https://z.ai/subscribe">GLM Coding Plan — AI Coding Powered by GLM -5.3, GLM -5.3-Flash, ...</a></li>

</ul>
</details>

**标签**: `#GLM-5.3-Flash`, `#open-source model`, `#AI pricing`, `#ZCode`, `#multimodal`

---

<a id="item-7"></a>
## [Claude Code v2.1.247 新增成本优化命令与反馈工具](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 发布了 Claude Code v2.1.247，新增 SendFeedback 工具，可在会话出错时草拟反馈报告供用户审查并通过 /feedback 发送（可通过 feedbackDrafts 设置关闭）。该版本还引入了 /claude-api cost-optimize 命令，用于分析现有项目的 Claude API 支出并逐一处理缓存、token 卫生、批处理、推理力度和模型选择等成本杠杆，同时扩展了 Admin API 覆盖范围，涵盖组织成员、邀请、工作区、API 密钥、速率限制报告、工作负载身份联合和 CMEK。 该版本为开发者提供了内置的、可量化的 API 支出削减工作流，以及更直接的遥测反馈回路；由于 API 成本是规模化运行智能编码工具的团队面临的主要痛点，这具有重要意义。 除上述主要功能外，本次更新还包含 20 多项错误修复，尤其是子代理在首次调用模型返回 404 时改用会话的备用模型链，以及修复了 kitty 协议终端中非拉丁键盘布局下 Ctrl 快捷键失效的问题。

github · ashwin-ant · 8月26日 23:06

**背景**: Claude Code 是 Anthropic 面向终端和 IDE 的智能编码工具，按 API token 消耗计费。据报道，重度 API 使用每个开发者每月可能花费数百美元，因此内置成本分析功能具有实用价值。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code/releases/tag/v2.1.247">anthropics/claude-code released v2.1.247</a></li>
<li><a href="https://code.claude.com/docs/en/costs">Manage costs effectively - Claude Code Docs</a></li>
<li><a href="https://www.aibuilderclub.com/blog/reduce-claude-code-api-costs">Reduce Claude Code API Costs: Cut Your Bill 73%</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#release notes`, `#coding agent`, `#cost optimization`, `#developer tools`

---

<a id="item-8"></a>
## [Cline 桌面版 v0.0.19 修复内存泄漏并更新模型目录](https://github.com/cline/cline/releases/tag/desktop-v0.0.19) ⭐️ 7.0/10

**级别**: 核心必看

Cline 桌面版 v0.0.19 修复了后台 Cline 进程在长时间会话中的内存膨胀问题，原因是会话状态更新会把完整对话记录副本发给每个连接的客户端；现在状态更新只携带状态信息，并按需获取完整记录。该版本还刷新了模型目录，新增七家提供商（Agnes AI、Aixy、IteraCompute、LLM Tech、NeoSmith、Pendra、Standard Compute），并更改了 ClinePass、Z.ai、Hugging Face、evroc、LLM Gateway、NanoGPT 和 Weights &amp; Biases 的默认模型。 此更新消除了这个被广泛使用的开源 AI 编码工具中的一个严重内存泄漏，使长时间运行的会话稳定得多，同时模型目录刷新也会直接影响 ClinePass、Z.ai、Hugging Face、evroc、LLM Gateway、NanoGPT 和 Weights &amp; Biases 这些提供商的默认模型选择。 修复后的状态更新只包含状态字段（状态、用量、模型、工作区、检查点），而且默认模型变更仅对没有固定模型的用户生效，因此依赖先前默认模型的用户需要手动固定模型以保持原有工作流。

github · github-actions\[bot\] · 8月26日 09:31

**背景**: Cline 是一款开源 AI 编码代理，被超过 800 万开发者使用；它可在 VS Code 等编辑器中运行，能自主读取文件、编写代码并执行终端命令。Cline 桌面版包含一个后台进程来协调会话和状态更新，本次内存问题就发生在这个进程中。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/cline/cline/releases/tag/desktop-v0.0.19">cline/cline released desktop-v0.0.19</a></li>
<li><a href="https://cline.bot/">Cline - AI Coding, Open Source and Uncompromised</a></li>

</ul>
</details>

**标签**: `#Cline`, `#AI coding tools`, `#memory fix`, `#model catalog`, `#desktop release`

---

<a id="item-9"></a>
## [阿里巴巴推出 Qwen3.8-Flash-Next，主打极致成本效率的混合专家模型](https://the-decoder.com/alibaba-releases-qwen3-8-flash-next-targeting-ultimate-cost-efficiency/) ⭐️ 7.0/10

**级别**: 核心必看

阿里巴巴 Qwen 团队正在预览 Qwen3.8-Flash-Next，这是基于即将推出的 Qwen4 架构的混合专家模型，每个 token 仅激活 1250 亿参数中的 60 亿。团队称，该模型以约为 Qwen 3.7-Plus 九分之一的训练成本，在编程和办公基准上超越了 DeepSeek-V4-Flash 和 Claude Opus 4.6。 这表明，以远低于大型模型的训练和推理成本即可实现具有竞争力的编程能力，从而加剧对 OpenAI 和 Anthropic 的价格压力，并让开发者更容易获得前沿级 AI。 根据 Hugging Face 页面，基于 Qwen3.8-Flash-Next 的 Qwen3.8-Flash 是官方正式版本，增加了默认 100 万 token 的上下文长度和内置工具，而本次发布明确被定位为 Qwen4 架构的早期预览。

rss · The Decoder · 8月26日 14:40

**背景**: 混合专家（MoE）是一种机器学习技术，它将问题空间划分为多个同质区域，每个输入只激活部分专家子网络，从而在保持总参数量的同时降低计算成本。Qwen3.8-Flash-Next 正体现了这一设计：每个 token 仅激活 1250 亿参数中的 60 亿。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/alibaba-releases-qwen3-8-flash-next-targeting-ultimate-cost-efficiency/">Alibaba releases Qwen3.8-Flash-Next, targeting &quot;ultimate cost efficiency&quot;</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#mixture-of-experts`, `#cost efficiency`, `#model release`, `#AI benchmarks`

---

<a id="item-10"></a>
## [IBM 以 Apache 2.0 许可发布开源权重 Granite 4.2 系列，内置智能体能力](https://the-decoder.com/ibm-drops-open-weight-granite-4-2-family-with-built-in-agentic-capabilities-under-apache-2-0/) ⭐️ 7.0/10

**级别**: 核心必看

IBM 发布了 Granite 4.2 开源权重语言模型系列，提供 3B、8B 和 30B 三种尺寸，使用约 15 万亿 token 训练，上下文窗口最高达 512,000 token。较大的模型采用智能体强化学习（agentic RL）自主学会工具调用和代码执行，全部模型均以 Apache 2.0 许可证发布。 通过内置工具调用、代码执行以及宽松的 Apache 2.0 许可，Granite 4.2 为开发者构建自主编码智能体和自托管企业级 AI 系统提供了一个实用的开源权重替代方案。 相关报道显示，该系列在 SWE-Bench Verified 上取得 57%的成绩，具备原生思维链推理和可控的思考开关，是 IBM 首个采用智能体强化学习训练的开源权重推理模型。

rss · The Decoder · 8月26日 10:37

**背景**: 开源权重（open-weight）模型公开模型权重，允许开发者自行部署和修改，这与完全封闭的模型不同。智能体 AI（agentic AI）指能够自主设定目标、使用工具并采取行动的系统，而不仅仅是回答问题。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/ibm-drops-open-weight-granite-4-2-family-with-built-in-agentic-capabilities-under-apache-2-0/">IBM drops open-weight Granite 4.2 family with built-in agentic capabilities under Apache 2.0</a></li>
<li><a href="https://www.creativeainews.com/articles/ibm-granite-4-2-open-agentic-coding-models-2026/">IBM Granite 4 . 2 : Open Agentic Coding Models</a></li>
<li><a href="https://overcentral.com/en/ibm-granite-4-2-open-reasoning-models-77917/">IBM Granite 4 . 2 brings native reasoning and agentic RL</a></li>

</ul>
</details>

**标签**: `#IBM Granite 4.2`, `#open-weight models`, `#agentic AI`, `#code execution`, `#Apache 2.0`

---

<a id="item-11"></a>
## [Warp 如何在 Claude 上构建自我改进的智能体](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude) ⭐️ 7.0/10

**级别**: 核心必看

Warp 在一篇博客文章中介绍了如何在 Claude 上构建自我改进的循环：使用 Agent Skills 的“基础技能”和“改进技能”两个文件型技能，把人类反馈转化为持续优化。该模式已应用于其开源仓库，覆盖数百名贡献者和数千次代码审查。 这很重要，因为它提供了一种可复用的工程模式，能把日常代码审查中的人类反馈转化为持续改进的 AI 编码智能体，这对规模化采用 agent-first 工作流的团队尤为关键。 团队建议以原则而非规则来编写技能，并强调低摩擦的反馈机制以及改进技能的可复用性，以便同一技能文件可以在不同仓库或团队间共享。

rss · AI 热榜 · 8月26日 17:02

**背景**: Agent Skills 允许开发者把指令和工作流打包成文件，供 Claude 按需加载。Warp 是一家终端公司，近期将产品开源，并使用其云端智能体编排平台 Oz 管理 agent-first 工作流。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude">Warp 如何在 Claude 上构建自我改进的智能体</a></li>
<li><a href="https://www.warp.dev/blog/warp-is-now-open-source">Warp is now open-source | Warp</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Agent Skills`, `#Self-improving agents`, `#Claude`, `#Engineering practices`

---

<a id="item-12"></a>
## [实测豆包工作集成飞书：8 个实用技巧](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&amp;mid=2247509950&amp;idx=1&amp;sn=18e7ecdceb66058f5ae1681009b4054e) ⭐️ 7.0/10

**级别**: 核心必看

这篇实测文章介绍了豆包工作（豆包 Work）与飞书深度整合后的首个 Agent 产品体验，总结了 8 个使用技巧。实测可远程控制最多 7 台设备、设置定时任务、自动读取本地 skill、在侧边栏直接编辑并同步到飞书，且管理员无法查看聊天记录。 由于作者认为豆包工作是当前企业接入 Agent 门槛最低的路径，其飞书原生生态可能让字节跳动在与 Claude Cowork、Codex Work 等竞品的办公 Agent 竞争中占据关键优势。 需要特别注意的是，用户必须用飞书账号登录才能解锁满血功能，而且作者认为 Work Agent 是 token 消耗倍增器。

rss · AI 热榜 · 8月26日 08:27

**背景**: 字节跳动于 8 月 25 日正式发布「豆包工作」独立 AI 办公 Agent 产品，TRAE 和扣子（Coze）团队并入豆包体系，飞书 Aily 也更名为「豆包工作伙伴」。近期豆包陆续上线远程控电脑、Windows 虚拟桌面、云电脑和侧边工作台，并放入超过 200 个技能和连接器。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&amp;mid=2247509950&amp;idx=1&amp;sn=18e7ecdceb66058f5ae1681009b4054e">实测飞书和豆包合体后第1个Agent：豆包工作的8个使用技巧</a></li>
<li><a href="https://www.yicaiglobal.com/news/bytedance-launches-doubao-work-as-chinas-tech-giants-pivot-to-office-ai-after-costly-consumer-push">ByteDance Launches Doubao Work as China’s Tech Giants Pivot to...</a></li>
<li><a href="https://post.smzdm.com/p/a6zdl9wg/">豆 包 工 作 今天发布，TRAE 和 扣子并入 豆 包 ：AI...</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Doubao Work`, `#Feishu`, `#Practical Tips`, `#Agent Ecosystem`

---

## 更多动态

<a id="item-13"></a>
### [保罗·迪克斯称赞 AI 能够编写并优化百万行代码库](https://simonwillison.net/2026/Aug/26/paul-dix/) ⭐️ 4.0/10

在 2026 年 8 月 26 日发布于西蒙·威利森博客的一段引言中，保罗·迪克斯表示，AI 编写了 100 万行代码，并在接下来的几个月里对其进行完善，最终产出了目前运行在数百万开发者机器上的可靠软件。他认为，只要具备验证系统和正确的指导，AI 就能生成并不断优化高度复杂的软件。

rss · Simon Willison · 8月26日 08:07

<a id="item-14"></a>
### [Lovable CTO：SaaS 的未来是智能体可用的应用](https://www.latent.space/p/lovable-future-of-saas) ⭐️ 4.0/10

在一段新的访谈预告中，Lovable 的 CTO Fabian Hedin 表示，公司正从 AI 驱动的 Web 应用创建扩展到由 MCP 驱动的“能力（capabilities）”，旨在让 SaaS 应用可供 AI 智能体使用。

rss · Latent Space · 8月26日 16:16