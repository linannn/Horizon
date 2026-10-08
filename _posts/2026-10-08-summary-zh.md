---
layout: default
title: "Horizon 每日速递：2026-10-08"
description: "AI 精选的技术与研究日报"
date: 2026-10-08
lang: zh
locale: zh-CN
---

> 从 73 条内容中筛选出 13 条重要资讯。

---

1. [Claude Code v2.1.293 发布：Haiku 5.5 成为默认模型并修复 MCP 内存泄漏](#item-1) ⭐️ 7.0/10
2. [Anthropic 发布 Claude Haiku 5.5，采用分级定价并赠送订阅者 API 额度](#item-2) ⭐️ 7.0/10
3. [Anthropic 发布 Claude Haiku 5.5：OSWorld 成绩飙升，token 价格最高降 90%](#item-3) ⭐️ 7.0/10
4. [OpenRouter 上线 GPT-6 Luna Decisions，可路由模型与工具](#item-4) ⭐️ 7.0/10
5. [LangChain 重构 Deep Agents Skills：工具绑定、技能固定与线程内重载](#item-5) ⭐️ 7.0/10
6. [Anthropic 为 Claude Max 和 Team 套餐推出月度 Platform API 额度](#item-6) ⭐️ 7.0/10
7. [Perplexity 开源 pplx-embed-v2-late：9B 与 0.6B 多模态 late-interaction 嵌入模型](#item-7) ⭐️ 7.0/10
8. [Unsloth 开源教程：本地训练决策模型，准确率从 20.7% 提升至 74.3%](#item-8) ⭐️ 7.0/10
9. [OpenAI Codex rust-v0.161.0 发布：默认模型升级并支持终端登录 MCP](#item-9) ⭐️ 6.0/10
10. [OpenAI 推出 Decisions API，实现快速低成本的文本与图像分类](#item-10) ⭐️ 6.0/10
11. [Anthropic 发布 Claude Haiku 5.5：价格对齐 GPT-6 Luna，但分词器更费 token](#item-11) ⭐️ 5.0/10
12. [Docker 开源无代码 AI 代理框架 Docker Agent](#item-12) ⭐️ 4.0/10
13. [Stacklok 推出 Mecatl：面向可靠智能体的云原生执行框架](#item-13) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Claude Code v2.1.293 发布：Haiku 5.5 成为默认模型并修复 MCP 内存泄漏](https://github.com/anthropics/claude-code/releases/tag/v2.1.293) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 发布了 Claude Code v2.1.293，新增 Claude Haiku 5.5（claude-haiku-5-5）并使其成为 Anthropic API 上的默认 Haiku 模型，具备 100 万 token 上下文窗口，价格为每百万 token 输入 0.10 美元、输出 0.50 美元。该版本还为 subagentStatusLine 载荷新增了 agentType 字段，为 mods 的 $.tool.register 新增 isDeferred 选项，并修复了上下文压缩后的状态错误以及 HTTP MCP 连接的内存泄漏。 由于 Haiku 5.5 成为默认 Haiku 模型，并以极低的单 token 价格提供 100 万 token 上下文窗口，使用 Claude Code 子代理和后台任务的开发者将获得成本更低、上下文更长的选择；同时 MCP 内存泄漏与上下文压缩的修复也直接改善了长时间代理会话的稳定性。 上述低价仅适用于 10 万 token 以内的提示词——超过该阈值后价格将升至每百万 token 输入 0.50 美元、输出 2.50 美元，因此超大上下文请求的成本是基础价格的五倍。

github · AI 热榜 · 10月7日 18:10

**背景**: Claude Code 是 Anthropic 推出的代理式编程工具，运行在终端中并直接操作用户的代码库，它依赖 MCP（Model Context Protocol，模型上下文协议）——这是 Anthropic 于 2024 年 11 月提出的开放标准，用于将大语言模型连接到外部工具和数据源。上下文压缩则是代理在对话历史不断增长时将其缩减、以便继续塞进模型有限的上下文窗口中所采用的技术。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code/releases/tag/v2.1.293">anthropics/claude-code released v2.1.293</a></li>
<li><a href="https://github.com/anthropics/claude-code/releases">Releases · anthropics/claude-code - GitHub</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#coding-agents`, `#mcp`, `#model-release`, `#changelog`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Haiku 5.5，采用分级定价并赠送订阅者 API 额度](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 发布了 Claude Haiku 5.5，这是其速度最快、成本最低的 Haiku 系列最新模型：提示词在 10 万 token 以内时，输入为每百万 token 0.10 美元、输出为每百万 token 0.50 美元；一旦提示词超过 10 万 token，价格分别升至 0.50 美元和 2.50 美元。同时，Anthropic 开始向 Max 与 Team 订阅用户发放每月 Claude Platform API 额度：Max 5x 为每月 100 美元，Max 20x 为每月 200 美元，Team 用户可共享最高 500 美元。 10 万 token 的门槛以及超过后 4 至 5 倍的涨价，直接改变了那些经常突破该上下文规模的智能体与编程工作流的成本测算；而捆绑的每月 API 额度则让订阅用户无需额外付费就能把基于 API 的功能上线。 这种分级定价仅适用于 Haiku，Sonnet 和 Opus 并不适用；而且门槛是按提示词长度而非整段对话或输出总量计算的，因此任何长上下文智能体循环都可能仅凭输入就跨入高价档位。

hackernews · sfkgtbor · 10月7日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49996437)

**背景**: 自 Claude 3 以来，Anthropic 通常把每一代 Claude 分为三档：Haiku（最快、最便宜）、Sonnet（中档）和 Opus（能力最强）；其中 Haiku 主要面向高并发、对成本敏感的任务，例如摘要、子智能体和浏览器操作。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-haiku-5-5">Claude Haiku 5.5</a></li>
<li><a href="https://platform.claude.com/docs/en/models/haiku-5-5/overview">Claude Haiku 5.5 - Claude Platform Docs</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-haiku-5.5">Claude Haiku 5.5 - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 讨论者参与度很高，但对定价持批评态度：minimaxir 称 10 万 token 的门槛“低得离谱”，并预测智能体类工作负载很快就会突破它；simonw 的“骑自行车的鹈鹕”基准显示，各思考档位下单项任务成本从低档的 0.0936 美分（耗时 7 秒）到 max 档的 3.3826 美分（耗时 5 分 9 秒）。charlesabarnes 欢迎每月额度，认为这让自己无需额外付费即可上线 AI 功能，但担心这是为了缓和即将到来的对用户不友好的改动；chriddyp 则报告在 Plotly 的 DataAnalyticsBench 上，Haiku 5.5 比 Haiku 4.5 便宜 9 倍、成绩高出“两个字母等级”，同时也是完成速度最快的模型。

**标签**: `#claude`, `#anthropic`, `#llm-pricing`, `#ai-models`, `#coding-agents`

---

<a id="item-3"></a>
## [Anthropic 发布 Claude Haiku 5.5：OSWorld 成绩飙升，token 价格最高降 90%](https://the-decoder.com/claude-haiku-5-5-arrives-with-massive-price-cuts-proving-the-ai-pricing-arms-race-is-far-from-over/) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 发布了 Claude Haiku 5.5，这是其目前速度最快、价格最低的小型模型：在 OSWorld 计算机操作基准测试中，成绩从前代的 15.7% 跃升至 72.4%，同时 token 价格相比 Haiku 4.5 最高下调 90%。Anthropic 还同步下调了 Sonnet 5.5 的价格。 能力大幅提升叠加价格大幅下调，使智能体（agent）与计算机操作类工作流的运行成本显著降低，这不仅加剧了前沿模型厂商之间的价格战，也改变了开发者构建编程与自动化智能体的部署成本结构。 这一大幅降价被部分抵消：新版分词器（tokenizer）在处理同一任务时会消耗更多 token；同时 90% 的降幅仅适用于不超过 100,000 个 token 的请求（该区间覆盖了 Haiku 4.5 约 90% 的请求），更长的请求只降价 50%。

rss · The Decoder · 10月7日 18:49

**背景**: Haiku 是 Anthropic 最小、最便宜的模型层级，定位低于 Sonnet 和 Opus，通常用于大规模、对延迟敏感的任务。OSWorld 是 2024 年提出的基准测试，用于评估多模态 AI 智能体在真实 Ubuntu 桌面环境中完成计算机操作任务的能力。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/claude-haiku-5-5-arrives-with-massive-price-cuts-proving-the-ai-pricing-arms-race-is-far-from-over/">Claude Haiku 5.5 arrives with massive price cuts proving the AI pricing arms race is far from over</a></li>
<li><a href="https://www.anthropic.com/claude-haiku-5-5">Introducing Claude Haiku 5.5 \ Anthropic</a></li>
<li><a href="https://osworld-v1.xlang.ai/">OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in...</a></li>

</ul>
</details>

**标签**: `#Claude`, `#Anthropic`, `#model-pricing`, `#computer-use`, `#LLM-benchmarks`

---

<a id="item-4"></a>
## [OpenRouter 上线 GPT-6 Luna Decisions，可路由模型与工具](https://x.com/OpenRouter/status/2107929204142874759) ⭐️ 7.0/10

**级别**: 核心必看

OpenRouter 已上线 GPT-6 Luna Decisions，该接口通过 OpenAI 的 Decisions API 提供 GPT-6 Luna，应用可将文本、JSON 或图片作为状态传入，并在单次请求中获得对命名问题的带概率类型化答案，定价为每百万输入 token 0.10 美元、输出免费，上下文窗口为 100 万 token。OpenRouter 引用 OpenAI 开发者账号的说法称，其决策速度比通过 Responses API 调用 GPT-6 Luna 最快快 10 倍。 这为智能体开发者提供了一个低价、单次请求即可完成的路由与决策原语——涵盖模型选择、工具选择与动作选择并附带置信度——有望取代自行编写的路由逻辑，并降低经由 OpenRouter 多厂商平台运行的多步智能体流水线的延迟与成本。 10 倍加速是引用 OpenAI 开发者账号的说法，目前没有公开基准测试佐证；而“输出免费”仅适用于 Decisions 返回的类型化答案，常规 GPT-6 Luna 文本生成在别处的标价为每百万输出 token 0.50 美元。

rss · AI 热榜 · 10月7日 20:21

**背景**: OpenRouter 是一个路由平台，把多家厂商的模型统一到一个 API 之下。OpenAI 的 Decisions API 与聊天补全接口不同：模型不生成文本，而是读取传入的状态，对命名问题给出带类型和概率的答案。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/OpenRouter/status/2107929204142874759">GPT-6 Luna Decisions 上架 OpenRouter</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-luna-decisions">GPT-6 Luna Decisions - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://omnitools.ai/news/news_muykxmk7d018d318abb5420d">OpenRouter 上线 GPT-6 Luna Decisions 模型</a></li>

</ul>
</details>

**标签**: `#AI APIs`, `#agent workflows`, `#model routing`, `#OpenRouter`, `#OpenAI`

---

<a id="item-5"></a>
## [LangChain 重构 Deep Agents Skills：工具绑定、技能固定与线程内重载](https://www.langchain.com/blog/revamping-skills-in-deep-agents) ⭐️ 7.0/10

**级别**: 核心必看

LangChain 重构了 Deep Agents 的 Skills 支持，针对企业技能库增长到数千个技能的场景推出三项更新：工具可以绑定到具体技能，并且仅在该技能被读取时才加载；用户可以通过 /meeting-prep 这类显式请求固定技能，让它在首次模型调用之前就加载；长线程可以通过将 skills\_metadata 设为 None 来重载新增或变更的技能。 当企业技能库扩展到数千个技能时，技能如何被发现、如何与工具绑定、如何在对话中途刷新，对运行长时 Agent 的团队来说已经是可靠性与上下文预算的核心问题，而不只是 API 层面的细节。 技能重载并非自动发生：只有在长线程中显式把 skills\_metadata 设为 None，新增或变更的技能才会生效。

rss · AI 热榜 · 10月7日 18:49

**背景**: Deep Agents 是 LangChain 开源的 Agent Harness，用于构建长时运行的 Agent，内置基于文件系统的上下文管理、子 Agent 派生和技能等能力。其技能模式采用渐进式披露：先只呈现简短描述，只有当某个技能真正被需要时才读取完整指令。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.langchain.com/blog/revamping-skills-in-deep-agents">LangChain 重构 Deep Agents 的 Skills 支持，新增工具绑定、固定技能与线程内重载</a></li>
<li><a href="https://docs.langchain.com/oss/python/deepagents/skills">Skills - Docs by LangChain</a></li>
<li><a href="https://docs.langchain.com/oss/python/deepagents/overview">Deep Agents overview - Docs by LangChain</a></li>

</ul>
</details>

**标签**: `#langchain`, `#deep-agents`, `#agent-skills`, `#ai-agents`, `#developer-tools`

---

<a id="item-6"></a>
## [Anthropic 为 Claude Max 和 Team 套餐推出月度 Platform API 额度](https://x.com/ClaudeDevs/status/2107895957933408429) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 正在为 Claude Max 和 Team 订阅推出月度 Claude Platform API 额度：Max 5x 为每月 $100，Max 20x 为每月 $200，Team 最高 $500 且成员之间可共享。这些额度适用于任何模型（包括 Haiku 5.5），既可以在自己写的代码中调用，也可以接入第三方 harness 使用。 把 API 额度直接打包进现有订阅，省去了开发者另行充值的步骤，并降低了在第三方 agent harness 中运行 Claude 的成本，这直接对竞品编码智能体的定价构成压力，也改变了用户衡量订阅价值的方式。 Anthropic 帮助中心说明额度需领取到 Console 组织中，覆盖 Claude API、Claude Managed Agents 和 Claude Agent SDK，但配套帮助页面的标题同时提到 Pro、Max 和 Team 计划的额外用量额度，而公告本身只列出 Max 和 Team，因此 Pro 订阅者是否同样能领取，仅凭该公告无法确定。

rss · AI 热榜 · 10月7日 18:08

**背景**: Claude Max 是 Anthropic 面向个人用户的高价订阅，Team 则是多席位的企业套餐，此前 Claude Platform 的 API 用量需要与这些聊天订阅分开计费。Anthropic 此前还限制第三方 agent harness 直接使用 Claude 订阅，因此这次发放明确可用于第三方 harness 的 API 额度，被视为在外部工具接入方式上的转向。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/ClaudeDevs/status/2107895957933408429">Anthropic 为 Claude Max 和 Team 套餐推出月度 Platform API 额度</a></li>
<li><a href="https://support.claude.com/zh-CN/articles/17154008-max-%E5%92%8C-team-%E8%AE%A1%E5%88%92%E7%9A%84%E6%AF%8F%E6%9C%88-api-%E9%A2%9D%E5%BA%A6">Max 和 Team 计划的每 月 API 额 度 | Anthropic Help Center</a></li>
<li><a href="https://linux.do/t/topic/1894552">【 Anthropic 放福利】 Claude Pro、 Max 和 Team ... - LINUX DO</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#API pricing`, `#developer tools`, `#coding agents`

---

<a id="item-7"></a>
## [Perplexity 开源 pplx-embed-v2-late：9B 与 0.6B 多模态 late-interaction 嵌入模型](https://x.com/AravSrinivas/status/2107871834205196784) ⭐️ 7.0/10

**级别**: 核心必看

Perplexity 开源了 pplx-embed-v2-late，这是一对面向文本与图像的 late-interaction 多向量嵌入模型，参数量分别为 9B 和 0.6B，权重已发布在 Hugging Face 上。两个尺寸共享同一嵌入空间，因此 9B 模型可用于索引多模态数据，0.6B 模型可在设备端执行查询；Perplexity 公布的成绩为 MADQA 92.4%、BrowseComp+ 64%。 这为 RAG、文档索引和智能体记忆等流程提供了一个可直接下载的开源权重检索组件，能够在无需 OCR 的情况下处理图像与 PDF 页面，把 late-interaction 方法从目前多数团队使用的纯文本嵌入模型扩展到了多模态场景。 由于这类 late-interaction 模型会为每个条目保留多个 token 级向量并用 MaxSim 式匹配打分，其索引存储与内存占用通常高于单向量稠密嵌入，这一代价需要与免 OCR 的 PDF 检索收益一并权衡。

rss · AI 热榜 · 10月7日 16:33

**背景**: Late-interaction（ColBERT 式）检索会把查询和文档拆成 token 级向量，而不是各用一个向量表示，通常能提升检索精度但需要更多存储；Perplexity 此前已在同一个 pplx-embed 集合下发布过更小的 pplx-embed-v1-late-0.6b 模型。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/AravSrinivas/status/2107871834205196784">Perplexity 开源 pplx-embed-v2-late 多模态 late-interaction 嵌入模型（9B 与 0.6B）</a></li>
<li><a href="https://huggingface.co/collections/perplexity-ai/pplx-embed">pplx - embed - a perplexity -ai Collection</a></li>
<li><a href="https://weaviate.io/blog/late-interaction-overview">An Overview of Late Interaction Retrieval Models: ColBERT ...</a></li>

</ul>
</details>

**标签**: `#embeddings`, `#multimodal`, `#open-source-models`, `#RAG/retrieval`, `#late-interaction`

---

<a id="item-8"></a>
## [Unsloth 开源教程：本地训练决策模型，准确率从 20.7% 提升至 74.3%](https://x.com/UnslothAI/status/2107868866361930236) ⭐️ 7.0/10

**级别**: 核心必看

Unsloth 发布了一套开源教程与代码仓库，可将 Qwen3.8、Gemma 4 等 LLM 微调为输出各选项概率的决策模型。在 3 个决策基准的合计测试中，Qwen3.5 0.8B 的准确率从 20.7% 提升至 74.3%，且仅需 4GB 显存。 这说明亚 10 亿参数的小模型也能在消费级硬件上被改造成可用的决策组件，从而降低了开发者构建专用任务模型的门槛，减少对云端大模型 API 的成本与隐私依赖。 74.3% 是 3 个决策基准的合计结果而非单一任务成绩，因此各基准上的实际表现可能存在较大差异，不能把它直接理解为通用能力上的准确率。

rss · AI 热榜 · 10月7日 16:21

**背景**: Unsloth 是一个开源微调库，以加速训练、降低显存占用为卖点——Qwen 官方文档就提到它对 Qwen3 模型的微调速度提升约 2 倍、显存占用减少 70%。这里的“决策模型”指的是对一组固定选项输出概率分布的模型，适合用于路由、分类以及智能体工具选择等任务。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/UnslothAI/status/2107868866361930236">Unsloth 开源教程：本地训练 Qwen3.5 0.8B 决策模型，准确率从 20.7% 提升至 74.3%</a></li>
<li><a href="https://unsloth.ai/docs/get-started/fine-tuning-llms-guide">Fine - tuning LLMs Guide | Unsloth Documentation</a></li>
<li><a href="https://qwen.readthedocs.io/zh-cn/latest/training/unsloth.html">Unsloth - Qwen</a></li>

</ul>
</details>

**标签**: `#Unsloth`, `#fine-tuning`, `#Qwen`, `#local LLM`, `#decision models`

---

## 更多动态

<a id="item-9"></a>
### [OpenAI Codex rust-v0.161.0 发布：默认模型升级并支持终端登录 MCP](https://github.com/openai/codex/releases/tag/rust-v0.161.0) ⭐️ 6.0/10

OpenAI Codex rust-v0.161.0 将 GPT-6.1 Sol 设为内置目录和 Amazon Bedrock 目录中的默认模型，为 Bedrock 增加了多智能体 V2 与 Ultra 推理能力，并通过 Bedrock Mantle 支持 AWS GovCloud 区域；同时新增 \`/mcp login &lt;name&gt;\`，让开发者可以直接在活跃的终端会话中登录 MCP 服务器。该版本还为语音对话增加了本地保存的麦克风、扬声器和输入声道偏好设置，并将 Daybreak 网络安全功能改为严格的显式开启。

github · github-actions\[bot\] · 10月7日 15:58

<a id="item-10"></a>
### [OpenAI 推出 Decisions API，实现快速低成本的文本与图像分类](https://the-decoder.com/openai-launches-decisions-api-that-reduces-complex-evaluations-to-yes-no-or-pick-one/) ⭐️ 6.0/10

OpenAI 发布了一款全新的 Decisions API，其对文本和图像进行分类的速度约为 Responses API 的十倍，可返回“是/否”概率、从预设类别中做出选择，或给出量表评分。该接口定价为每百万输入 token 0.10 美元，同时 OpenAI 将付费 API 层级从五档削减至三档。

rss · The Decoder · 10月7日 15:36

<a id="item-11"></a>
### [Anthropic 发布 Claude Haiku 5.5：价格对齐 GPT-6 Luna，但分词器更费 token](https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/) ⭐️ 5.0/10

Anthropic 于 2026 年 10 月 7 日发布 Claude Haiku 5.5，这是一款主打快速、低成本的模型，在 10 万 token 以内定价为每百万输入 token 0.10 美元、每百万输出 token 0.50 美元，超过 10 万 token 后价格上涨 5 倍至 0.50/2.50 美元。它取代了约一年前发布、定价为每百万 token 1/5 美元的 Haiku 4.5，而后者价格约为 OpenAI GPT-6 Luna 的 10 倍。

rss · Simon Willison · 10月7日 20:56

<a id="item-12"></a>
### [Docker 开源无代码 AI 代理框架 Docker Agent](https://github.com/docker/docker-agent) ⭐️ 4.0/10

Docker 在 GitHub 上发布了一个名为 Docker Agent 的开源 AI 代理框架，宣称用户「无需编写代码」即可创建并运行相互协作、共同解决复杂问题的智能代理。该帖在 Hacker News 上引发了规模不小但以质疑为主的讨论（172 分、81 条评论）。

hackernews · saikatsg · 10月7日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49996259)

<a id="item-13"></a>
### [Stacklok 推出 Mecatl：面向可靠智能体的云原生执行框架](https://www.latent.space/p/stacklok) ⭐️ 4.0/10

Kubernetes 联合创始人 Craig McLuckie 和 Joe Beda 通过其公司 Stacklok 主张，智能体执行框架应当以云原生工作负载的方式运行。他们已开源名为 Mecatl 的执行框架，该框架将智能体循环与客户端、模型提供商、状态存储和执行环境分离开来。

rss · Latent Space · 10月7日 14:10