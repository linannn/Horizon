---
layout: default
title: "Horizon 每日速递：2026-11-26"
description: "AI 精选的技术与研究日报"
date: 2026-11-26
lang: zh
locale: zh-CN
---

> 从 63 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Mastra Core 1.86.0 加入持久执行与 Knowledge 导入器](#item-tech-news-1) ⭐️ 8.0/10
2. [GitHub Copilot CLI v1.0.117-0 更新代理工具与会话恢复](#item-tech-news-2) ⭐️ 7.0/10
3. [LLM 辅助 Lean 审计 Clojure 核心类型边界](#item-tech-news-3) ⭐️ 7.0/10
4. [Mellum2.1 Instruct 面向编码代理发布](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenClaw 2026.11.10 新增三项 Agent 功能](#item-tech-news-5) ⭐️ 7.0/10
6. [Pydantic AI 发布插件化终端智能体 Pax beta](#item-tech-news-6) ⭐️ 7.0/10
7. [Claude Ship 发布三类 PR 协作智能体](#item-tech-news-7) ⭐️ 7.0/10
8. [MIT 与微软论文：Copilot 采用与初级工程师需求下降约 40% 相关](#item-tech-news-8) ⭐️ 7.0/10
9. [LLM 编程中的工具、验证与理解流失](#item-tech-news-9) ⭐️ 6.0/10
10. [GitHub Copilot 旧应用现代化安全工作流指南](#item-tech-news-10) ⭐️ 6.0/10
11. [Cloudflare 推出面向 AI 智能体的站点搜索](#item-tech-news-11) ⭐️ 6.0/10
12. [PrismML 将 27B 三值模型压缩至 5.9 GB](#item-tech-news-12) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Mastra Core 1.86.0 加入持久执行与 Knowledge 导入器](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0) ⭐️ 8.0/10

**级别**: 核心必看

面向使用 Mastra 构建 AI 代理和数据集实验的开发者，@mastra/core 1.86.0 加入持久化、事件化执行：实验可向 startExperimentAsync\(\) 及服务端和客户端触发接口传入 durable: true，并按每个数据项拆分步骤；按发布说明，在 Redis Streams 等会重投事件的 pubsub 上，进程崩溃或重新部署后，其他工作进程可接管未确认项并继续执行。代理也可通过 durable.executionEngine 选择原生持久引擎并沿用现有流式和模型输出 API，但预发布版的 executionEngine: &\#x27;durable&\#x27; 已改名为 &\#x27;default&\#x27;。实验性 Knowledge 导入链新增 @mastra/core/knowledge 的 KnowledgeImporter 合约、knowledge.importers.run\(bindingId\) 以及内存、LibSQL、Postgres 存储账本，提供批处理、租约、重放保护和 settle/repair 语义；创建表可调用 knowledge.importers.init\(\) 或使用相应 DDL 导出。该版本还加入 createChannelTools\(\)、Slack createSlackTools\(\)、knowledge\_activity 查询及宿主端 principals/author 支持，同时带来 get\_process\_output 移除 wait: true（改用 1–300 秒的 waitSeconds）、预发布的 @mastra/connect 改用 ConnectEvents 迭代器、MCP 边界字段 projectId 改为 project，以及 Playground UI API 变化等兼容性调整。

github · PaulieScanlon · 11月25日 10:00

**「持久执行与导入器的前置条件」** 要让 Mastra 的持久化执行机制生效，部署环境需提供可在多进程间重投未确认事件的消息代理并启用恢复；不支持多进程的环境会触发警告，而关闭恢复后，\`interrupted\` 可能成为最终状态。Knowledge 导入器还依赖持久化存储中的导入账本，部署前需调用 \`knowledge.importers.init\(\)\` 创建表，或在禁用自动初始化时执行包含 writer-guard 行的导出 DDL。

**「升级与运行影响」** 升级到 1.86.0 的现有项目需要检查破坏性变更：wait: true 会被忽略并应改用 waitSeconds（1–300），预发布的 @mastra/connect 用户需迁移到 ConnectEvents，MCP 边界字段需从 projectId 改为 project，使用预发布持久执行配置的代理则需将 executionEngine: &\#x27;durable&\#x27; 改为 &\#x27;default&\#x27;。对于使用会重投事件的 pubsub 且启用恢复机制的工作进程，持久实验和代理运行可在崩溃或滚动重启后继续处理未确认工作；但 Knowledge 导入器仍属实验功能，并要求先初始化导入器表，生产部署应单独评估这一依赖。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.86.0">mastra-ai/mastra released @mastra/core@1.86.0</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#durable execution`, `#knowledge ingestion`, `#developer tools`, `#open source`

---

<a id="item-tech-news-2"></a>
### [GitHub Copilot CLI v1.0.117-0 更新代理工具与会话恢复](https://github.com/github/copilot-cli/releases/tag/v1.0.117-0) ⭐️ 7.0/10

**级别**: 核心必看

GitHub Copilot CLI v1.0.117-0 为自定义代理加入显式工具暴露机制，开发者可选择代理要使用的工具；该发布页同时列出的 v1.0.117-1 变更还修复了自定义代理文件没有 prompt 时，子代理未遵守其中工具列表的问题。恢复仍在完成 GitHub 登录的 CLI 会话时，现在会加载已连接的 Copilot Connectors；重启 CLI 并恢复会话后，后台代理也能继续原对话。设置 COPILOT\_MCP\_TOOL\_CACHE=false 后，即使发生重载也仍会禁用 MCP 工具缓存，Copilot 不会读取或写入工具快照；此外，成功的非交互运行在会话写入暂时失败但最终保存成功时会以退出码 0 结束，从子目录使用 --trust-folder 和 --add-dir 时也不再运行仓库根目录的 hooks。权限方面，Assisted Permissions 可在后续聊天中重试一次先前失败的操作，且仍须经过权限审查；计划模式会在创建 Git 分支或安装包等动作前询问，/sandbox policy 则会标记指向损坏符号链接的授权，并警告其可能阻止沙箱命令启动。

github · copilot-cli-release-app\[bot\] · 11月25日 21:21

**「背景」** 自定义代理的代理文件既可包含提示词，也可单独声明工具列表；发布说明同时收录的 v1.0.117-1 变更因此专门指出，即使文件没有 prompt，子代理也应遵守该列表。CLI 会话恢复还涉及 GitHub 登录状态、Copilot Connectors、后台会话和 MCP 工具快照的衔接，其中 COPILOT\_MCP\_TOOL\_CACHE=false 可关闭快照的读取与写入，并在配置重载后保持禁用。

**「对 CI 流水线与自定义代理使用者的影响」** 把 Copilot CLI 用于 CI 或脚本化非交互运行的团队不会再因会话写入的一次临时失败而判定任务失败：只要最终保存成功，运行即以退出码 0 结束，因此流水线无需再为此类瞬时错误额外重试或加豁免规则。相应地，依赖自定义代理文件控制工具暴露的团队需要重新验证实际生效的工具集合，因为该版本新增了自定义代理显式选择工具的机制，而 v1.0.117-1 修复了子代理在代理文件没有 prompt 时不遵守工具列表的问题；已设置 COPILOT\_MCP\_TOOL\_CACHE=false 的环境在重载后仍保持禁用、不会读写工具快照，可以继续作为既有基线依赖。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/github/copilot-cli/releases/tag/v1.0.117-0">github/copilot-cli released v1.0.117-0</a></li>
<li><a href="https://github.com/github/copilot-cli/releases">Releases · github/copilot-cli</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-cli">GitHub Copilot CLI</a></li>

</ul>
</details>

**标签**: `#AI coding tools`, `#coding agents`, `#MCP`, `#GitHub Copilot CLI`

---

<a id="item-tech-news-3"></a>
### [LLM 辅助 Lean 审计 Clojure 核心类型边界](https://s.conao3.com/blog/2026/e4f733) ⭐️ 7.0/10

**级别**: 核心必看

作者发布了一次由大语言模型辅助、以 Lean 审核 Clojure core 的实践，并报告了类型错误和强制转换边界方面的候选缺陷。文章将这些结果描述为此前未报告的 bug，同时展示了让语言模型与定理证明器协作的验证流程。现有材料不足以确认清单中的每项都是实际实现缺陷，评论者已对至少两项提出异议。

hackernews · encyclopedism · 11月25日 14:56 · [社区讨论](https://news.ycombinator.com/item?id=50642939)

**「审计方法与复现环境」** 这项工作将 Lean 4 的形式化规格检查与差分测试结合，用于审查 Clojure core 的 HAMT 和 vector-of 实现。后续报道称，审计共列出 17 个候选缺陷，其中 5 个已在标准版 Clojure 1.12.7 和 JDK 21 上复现，复现项还包括一个恰在 65,505 个元素时无限挂起的问题；这并不代表其余 12 项也已得到确认。

**「维护者需逐项复核审计结果」** 对 Clojure 维护者而言，这份结果目前更适合作为逐项复核的候选清单，而不是可直接修复的缺陷列表；复核时需要先对照函数签名、调用参数类型及既有强制转换语义。

**「评论者质疑误报与工具差异」** 评论者 rvprasad 认为，清单中的 \`.indexOf\` 示例可能只是以 Long 参数搜索字节序列时产生了类型误用，而 \`\(get &quot;abc&quot; 1.9\)\` 的行为来自字符串键的整数强制转换，因此这些条目未必是 core 缺陷。networked 则追问 Lean 与 Rocq（原 Coq）在程序正确性验证上的差异，以及语言模型是否显著更擅长 Lean，现有评论没有给出比较结论。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://s.conao3.com/blog/2026/e4f733">I checked Clojure&#x27;s core with Lean and found unreported bugs</a></li>
<li><a href="https://dev.to/frankchu/clojures-core-has-17-unreported-bugs-i-reproduced-5-1764">Clojure&#x27;s core has 17 unreported bugs — I reproduced 5</a></li>

</ul>
</details>

**标签**: `#AI-assisted verification`, `#Lean`, `#Clojure`, `#formal methods`, `#program correctness`

---

<a id="item-tech-news-4"></a>
### [Mellum2.1 Instruct 面向编码代理发布](https://blog.jetbrains.com/ai/2026/11/mellum2-1-instruct-is-out-bringing-faster-answers-for-coding-agents/) ⭐️ 7.0/10

**级别**: 核心必看

JetBrains 已发布开源模型 Mellum2.1 Instruct，主要面向编码代理中的子代理、工具调用循环和聊天场景。该模型总参数量为 12B，采用混合专家（MoE）架构、活跃参数量为 2.5B，与 2026 年 10 月发布的 Mellum2.1 Thinking 架构相同且训练方式一致。JetBrains 将 Instruct 称为 Thinking 版本的“更快兄弟”，但现有材料未提供速度或编码任务基准，无法量化实际性能提升，也未说明许可证和具体集成方式。

rss · JetBrains AI · 11月25日 11:00

**「与 Mellum2.1 Thinking 的关系」** Mellum2.1 Instruct 沿用 JetBrains 于 2026 年 10 月发布的 Mellum2.1 Thinking 架构与训练方式，因此并非另起一套模型基础；其区别在于被定位为面向子代理、工具调用循环和聊天的“更快兄弟”。现有材料未给出二者速度或编码任务基准，无法判断该定位对应的实际性能差距。

**「按任务拆分代理模型」** 开发者在构建编码代理工作流时，可将 Mellum2.1 Instruct 用于需要直接、较快响应的子代理、工具调用循环、小修复和代码问答，并继续用 Mellum2.1 Thinking 处理需要先推理再行动的长期复杂任务。该模型为 12B MoE、每次推理仅激活 2.5B 参数；但 JetBrains 未公布速度基准或集成说明，因此“可更快”仍应视为产品定位，实际延迟和硬件收益需自行测试。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.jetbrains.com/ai/2026/11/mellum2-1-instruct-is-out-bringing-faster-answers-for-coding-agents/">Mellum2.1 Instruct Is Out, Bringing Faster Answers for Coding Agents</a></li>
<li><a href="https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Instruct">JetBrains/ Mellum 2 . 1 -12B-A2.5B- Instruct · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#open-source models`, `#mixture-of-experts`, `#developer tools`

---

<a id="item-tech-news-5"></a>
### [OpenClaw 2026.11.10 新增三项 Agent 功能](https://x.com/openclaw/status/2125591827600531554) ⭐️ 7.0/10

**级别**: 核心必看

OpenClaw 已发布 2026.11.10 版本，为聊天式 AI Agent 用户新增聊天内 Deep Research、OpenClaw Knowledge 记忆系统和 Browser handoff 功能，分别涉及深度研究、知识记忆与浏览器任务交接。官方摘要称，本次版本包含 7,671 个 PR，共有 349 位贡献者参与。现有材料未说明这些功能的 API、配置要求、兼容性或实测效果，因此暂不能据此判断其性能及部署影响。

rss · AI 热榜 · 11月25日 14:05

**「此次更新的产品形态」** 此次更新并非孤立加入三个功能入口：OpenClaw 2026.11.10 还让 Advisor 脱离 Labs，并扩展 Workboard、MCP、ACP、插件建议和 PostgreSQL store 支持，显示该版本同时在推进实验功能正式化和代理工具链整合。官方文档将 Deep Research 描述为带专用 Control UI 面板的随附能力，将 Knowledge 描述为随附的记忆插件，并将 Browser handoff 具体表述为浏览器标签页交接。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/openclaw/status/2125591827600531554">OpenClaw 2026.11.10 发布，新增 Deep Research、Knowledge 记忆系统与 Browser handoff</a></li>
<li><a href="https://docs.openclaw.ai/releases/2026.11.10">v 2026 . 11 . 10 - OpenClaw</a></li>
<li><a href="https://docs.openclaw.ai/">OpenClaw Docs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#OpenClaw`, `#Deep Research`, `#agent memory`, `#browser handoff`

---

<a id="item-tech-news-6"></a>
### [Pydantic AI 发布插件化终端智能体 Pax beta](https://pydantic.dev/articles/pax-harness-beta) ⭐️ 7.0/10

**级别**: 核心必看

Pydantic AI 面向开发者发布终端编码智能体 Pax beta（包名 pydantic-ai-pax），其基于 Harness SDK 构建。Pax 将 coder、sandbox、MCP 和 Logfire 观测等能力组织为插件，可在终端通过 /plugins 开关，并支持用 --agent 切换到代码库中的任意 Pydantic AI Agent。当前信息仅明确了 beta 状态和插件化工作流，未提供 1.0 时间表、成熟度指标或性能基准。

rss · AI 热榜 · 11月25日 09:00

**「Harness 的能力原语」** Pydantic AI v2 于 2026 年 6 月转向以 Harness SDK 为中心的设计，Capability 原语把指令、工具、生命周期钩子和模型设置组合为可复用的能力单元。Pax 延续了这一可组合方向，将终端编码工作流拆成可按需启用的插件；这一前代设计信息来自社区维护的汇总，而非 Pax 原文的独立性能或成熟度验证。

**「开发者可组合并复用现有 Agent」** 对于需要搭建终端编码工作流的开发者，Pax 允许按需启用编码、沙箱、MCP 与 Logfire 观测，同时通过 --agent 复用代码库中已有的 Pydantic AI Agent。由于 Pax 仍处于 beta，且原文未披露兼容性要求或稳定性数据，投入生产前仍需自行验证。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://pydantic.dev/articles/pax-harness-beta">Pydantic AI 发布终端编码智能体 Pax 与 Harness beta，迈向 1.0</a></li>
<li><a href="https://github.com/ai-boost/awesome-harness-engineering">GitHub - ai -boost/awesome- harness -engineering: Awesome list for AI ...</a></li>

</ul>
</details>

**标签**: `#终端编码智能体`, `#Pydantic AI`, `#插件架构`, `#MCP`, `#工程观测`

---

<a id="item-tech-news-7"></a>
### [Claude Ship 发布三类 PR 协作智能体](https://x.com/addyosmani/status/2125492213903978917) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic Claude Code 团队推出 Claude Ship，包含三个面向 PR 协作的智能体：Code Review 已全面开放，PR Steward 与 Claude Approvals 处于 beta。整体工作流可审查 PR、处理失败的 CI、合并冲突和审查意见，并依据仓库策略文件自动批准常规改动；不过来源没有提供配置示例或技术实现细节，除 Code Review 外的能力边界和可用条件仍无法仅凭这条消息确认。

rss · AI 热榜 · 11月25日 07:30

**「功能前提」** Claude Ship 将 PR 审查、后续问题跟进和基于策略的批准纳入同一套智能体工作流；其中自动批准以仓库中的策略文件为前提，而不是由代理无条件放行改动。因此，策略文件实际覆盖的改动范围，是理解 Claude Approvals 使用条件的关键。

**「对团队的影响」** 采用 Claude Ship 后，开发团队可以把 PR 审查、失败 CI 处理、合并冲突处理和审查意见跟进纳入代理流程，并让符合仓库策略的常规改动走自动批准路径。实际启用前应核对策略文件的适用范围；来源没有提供配置示例、集成条件或效果数据，因此不能据此断言它与现有 CI 和合并流程完全兼容，或量化人工工作量的减少。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/addyosmani/status/2125492213903978917">Claude Code 团队发布实用指南讲解 Claude Ship 的 PR 审查与守护用法</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI coding agents`, `#PR review`, `#CI automation`, `#repository policies`

---

<a id="item-tech-news-8"></a>
### [MIT 与微软论文：Copilot 采用与初级工程师需求下降约 40% 相关](https://x.com/rohanpaul_ai/status/2125461932111229203) ⭐️ 7.0/10

**级别**: 核心必看

MIT 与微软的论文《AI-Assisted Programming and Labor Demand》利用 5,414 家跨国公司的 GitHub 合同审查时点构造自然实验，论文称相关数据覆盖约 38% 的美国程序员。研究估计，GitHub Copilot 的采用与初级软件工程师劳动力需求下降约 40% 相关；这一比例针对初级岗位需求，并非整个程序员群体。当前条目未提供论文全文、估计区间、识别假设或潜在局限，因此该数字应视为论文估计，尚不能视为已独立验证的确定性因果结论。

rss · AI 热榜 · 11月25日 05:29

**「从任务能力到劳动力需求」** 此前的研究已展示生成式 AI 在编码等具体技术任务上的能力，但这类任务级提升是否会改变企业技术岗位的招聘与就业，证据仍然有限。为填补这一缺口，论文把 GitHub Copilot 在企业中的分批启用视为自然实验，并以合同审查时点形成的采用节奏作为识别条件，从而考察工具采用与后续劳动力需求之间的关系。

**「重新评估初级工程师招聘」** 论文估计，采用 GitHub Copilot 的企业季度初级软件工程师招聘减少约 40%，而资深软件工程师以及系统和基础设施工程师的招聘未显示变化。因此，部署 Copilot 后仍计划扩招初级工程师或依赖其构建人才梯队的组织，应重新评估初级岗位预算和培养安排，不宜将影响直接外推至所有技术岗位。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/rohanpaul_ai/status/2125461932111229203">MIT 与 Microsoft 论文：GitHub Copilot 使初级软件工程师招聘下降约 40%</a></li>
<li><a href="https://arxiv.org/abs/2611.31083">[2611.31083] AI-Assisted Programming and Labor Demand</a></li>
<li><a href="https://arxiv.org/pdf/2611.31083">AI-Assisted Programming and Labor Demand - arXiv.org</a></li>
<li><a href="https://fourweekmba.com/ai-copilot-cut-junior-coder-hiring-about-40-study-finds/">Copilot Cut Junior Coder Hiring About 40%, Study Finds</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#AI 编程`, `#劳动力市场`, `#自然实验`, `#MIT 与 Microsoft`

---

### 更多动态

<a id="item-tech-news-9"></a>
#### [LLM 编程中的工具、验证与理解流失](https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools) ⭐️ 6.0/10

Ian Duncan 在一篇文章中提出，LLM 与 AI 编程工具带来的变化不只是提高代码产量，而是改变开发者组织工作、调用抽象层和验证结果的方式，因此使用者仍需保留对系统的理解。文章同时质疑“模型写的”能否成为代码审查中的免责理由，并讨论工具杠杆与质量责任之间的张力。现有材料没有提供具体工具、版本、基准数据、实现步骤或可复现实验，因此文中的判断应视为作者观点，而非已经独立验证的结论。

hackernews · matthewsinclair · 11月25日 07:46 · [社区讨论](https://news.ycombinator.com/item?id=50639698)

<a id="item-tech-news-10"></a>
#### [GitHub Copilot 旧应用现代化安全工作流指南](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) ⭐️ 6.0/10

GitHub Blog 发布了一篇面向遗留应用改造开发团队的实践指南，介绍如何评估现有应用、选择范围明确的现代化步骤，并通过可复用的 GitHub Copilot agent skill 重复执行这一方法。当前材料仅概述了这一工作流，未给出具体评估标准、实施步骤、代码示例或量化结果，因此尚不能据此判断其实际效果或适用范围。

rss · GitHub AI &amp; ML · 11月25日 15:00

<a id="item-tech-news-11"></a>
#### [Cloudflare 推出面向 AI 智能体的站点搜索](https://blog.cloudflare.com/search-for-agents/) ⭐️ 6.0/10

Cloudflare 宣布推出面向 AI 智能体的站点搜索功能。据其介绍，网站开启一个开关后即可自动为内容建立索引，并通过可发现的搜索 API 提供检索服务。接口原生支持 HTTP QUERY，但现有材料尚未说明具体实现、接入步骤、定价或可用范围。

rss · Cloudflare AI · 11月25日 14:00

<a id="item-tech-news-12"></a>
#### [PrismML 将 27B 三值模型压缩至 5.9 GB](https://the-decoder.com/prismml-squeezes-an-agent-based-coding-model-with-27-billion-parameters-into-5-9-gb/) ⭐️ 6.0/10

PrismML 发布了面向代理式编程场景的 Ternary Bonsai 2.5 27B，这是其激进压缩语言模型的新版本，采用每个权重仅取三个可能值的三值量化。报道显示，其模型体积从 54 GB 降至 5.9 GB，参数规模为 270 亿（27B）。原文未提供代码能力或整体质量基准、许可证、获取方式、硬件要求及编码代理框架兼容性，因此尚不能据此判断压缩后的实际可用性或运行成本。

rss · The Decoder · 11月25日 11:51