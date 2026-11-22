---
layout: default
title: "Horizon 每日速递：2026-11-22"
description: "AI 精选的技术与研究日报"
date: 2026-11-22
lang: zh
locale: zh-CN
---

> 从 28 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [Claude 协助的黎曼猜想 Lean 形式化证明](#item-tech-news-1) ⭐️ 9.0/10
2. [Cline SDK v0.2.1 调整文件结果上限与推理兼容](#item-tech-news-2) ⭐️ 7.0/10
3. [论文称 Claude 改进 3SUM 与 APSP](#item-tech-news-3) ⭐️ 7.0/10
4. [Copilot CLI v1.0.115-4 改进 ACP 澄清与稳定性](#item-tech-news-4) ⭐️ 6.0/10
5. [lookatmyquant 宣称 Inkling-2-Mini 可在 5.4 GB 内存运行](#item-tech-news-5) ⭐️ 6.0/10
6. [Axion 1.0 用三阶段训练挑战商业智能体](#item-tech-news-6) ⭐️ 6.0/10
7. [腾讯元宝与 KCL 发布群聊 Agent 记忆基准](#item-tech-news-7) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude 协助的黎曼猜想 Lean 形式化证明](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

**级别**: 核心必看

Lean Prover Community 博客发布消息称，数学家 Levent Alpöge 使用 Claude 协助证明黎曼猜想，并将证明形式化为 Lean 代码。所给材料提到多个独立检查实现可用于额外核验，但未提供足以确认该成果已获数学界独立复核的结果；形式化覆盖范围、人类参与程度，以及“检查器接受证明”与“证明成立”之间的差别仍需审查。

hackernews · g-b-r · 11月21日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**「Lean 证明的验收含义」** 背景上，Lean 是交互式定理证明器：数学家把定义、引理和推导写成机器可检查的形式，再由 Lean 的可信内核核验。因而评估这类声称时，需要区分“生成了形式化代码”“代码通过特定检查器”与“所用假设、依赖和内核实现已经过充分独立审查”；前两项本身不能替代第三项。

**「可复核的形式化产物」** 对 Lean 和形式化数学用户，最直接的影响是这项成果已提供可复核的固定产物，而非只有自然语言论证：验证站记录 175,187 / 175,187 个项目模块均完成编译，并提供验证机与证明审计记录；代码镜像还给出源代码及 SHA-256 校验信息。评估者可用这些材料复现编译、核对定理陈述与证明来源，但应将“全部模块通过编译”视为工程验收证据，而不是数学界已独立确认黎曼猜想成立的替代品。

**「可靠性与贡献之争」** 评论者认为，不同语言的多个内核以及 con-leche、con-ron 各自的一致性证明，大幅降低了证明利用单一内核漏洞蒙混过关的可能性；但也有人以此前虚假的 Collatz 反例曾通过一个检查器为例，提醒这些检查器并非完全独立。另有评论者将成果解读为 Claude 形式化了现代数学的大量内容，并认为 Levent Alpöge 驾驭模型的能力同样关键，不过所给材料没有量化实际范围或各部分贡献。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://leanprover-community.github.io/blog/posts/riemann-hypothesis/">Lean verification of the Riemann Hypothesis</a></li>
<li><a href="https://proveriemannhypothesis.github.io/">Verifying a Riemann Hypothesis Formalization in Lean</a></li>
<li><a href="https://github.com/CocoSgt/riemann-hypothesis-lean">GitHub - CocoSgt/ riemann - hypothesis - lean : Mirror of Levent...</a></li>

</ul>
</details>

**标签**: `#Lean`, `#theorem proving`, `#Claude`, `#AI coding agents`, `#formal verification`

---

<a id="item-tech-news-2"></a>
### [Cline SDK v0.2.1 调整文件结果上限与推理兼容](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.1) ⭐️ 7.0/10

**级别**: 核心必看

Cline 已发布 SDK v0.2.1，面向在编辑器或代理工作流中集成该 SDK 的开发者：\`read\_files\` 结果不再在送入模型前被重新截到 8k 字符，而改用 50k 字符的文件内容上限；命令、搜索、MCP 和自定义工具结果仍保留 8k 上限，并继续受显式工具结果上限约束。发布说明还称，需要交错推理的模型现在会在缺少 \`reasoning\_content\` 的助手消息中收到占位字段，并以 \`ModelInfo.metadata.interleavedReasoningField\` 标记，以修复压缩上下文或切换模型后 Reflection Beam 返回“400 Missing required parameter: &\#x27;messages\[n\].reasoning\_content&\#x27;”的问题。带已保存覆盖配置的自定义模型会默认加入 \`reasoning\` 能力，除非显式设置 \`supportsReasoning: false\`；原生 OpenAI 适配器也会把 \`max\` 和 Extra High 映射到模型公布的 effort 档位。

github · github-actions\[bot\] · 11月21日 05:19

**「模型推理兼容机制」** Cline SDK 按模型能力适配推理请求：模型目录声明可用的 effort 档位，\`ModelInfo.metadata.interleavedReasoningField\` 标记是否要求助手消息携带 \`reasoning\_content\`，未收录的自定义模型则依赖保存的覆盖配置和 \`supportsReasoning\` 声明。此前，目录未收录的模型可能收到 \`reasoning\_effort: &quot;none&quot;\` 而遭端点拒绝，压缩流程也会退回基础摘要器，这构成了此次占位字段、模型能力初始化和档位映射调整的背景。

**「升级影响」** 集成方应在升级后回归测试长文件与推理模型：进入提供商的工具结果不再统一受 8k 字符二次截断，需按最高 50k 字符重新评估上下文长度；依赖完整请求落盘的流程还必须移除对已删除的 \`CLINE\_CAPTURE\_\*\` 捕获机制的引用。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.1">cline/cline released sdk/sdk/v0.2.1</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Cline SDK`, `#agent tool results`, `#reasoning models`, `#MCP`

---

<a id="item-tech-news-3"></a>
### [论文称 Claude 改进 3SUM 与 APSP](https://x.com/rohanpaul_ai/status/2124213113583174076) ⭐️ 7.0/10

**级别**: 核心必看

一则关于哥伦比亚大学与麻省理工学院论文的转述称，Claude 发现的算法将 3SUM 的复杂度推进至 O\(n^1.9992\)，将全对最短路径（APSP）推进至 O\(n^2.9995\)；转述还称这推翻了相关长期假设。所给材料没有提供论文链接、算法描述、正确性证明、实现或复现实验，因此这些结果应被视为论文及其转述的主张，而非已经独立验证的定论。

rss · AI 热榜 · 11月21日 18:47

**「3SUM 与 APSP 的复杂度基准」** 3SUM 要在含 n 个数的集合中寻找三项之和，APSP 则要计算所有点对的最短路径；传统教材级时间基准分别为 O\(n²\) 和 O\(n³\)，因此能否实现真正的次二次 3SUM 与次立方 APSP 长期是精细化复杂度研究的核心障碍。该工作以稀疏三角形为中间问题，并利用已知归约把 Exact Triangle、3SUM 和 APSP 联系起来；其中 APSP 结果针对有向 n 顶点图及多项式有界整数权重。

**「理论界需重新核验相关假设」** 如果完整论文中的证明成立，3SUM 与 APSP 的已知最坏情况渐进上界将发生变化，依赖这些假设的算法研究和理论分析需要重新评估。当前材料缺少常数因子、基准测试与独立复现，开发者不宜据此作生产性能承诺或立即采用相关算法。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/rohanpaul_ai/status/2124213113583174076">Columbia 与 MIT 论文展示 Claude 发现的算法突破 3SUM 与 APSP 长期速度上限</a></li>
<li><a href="https://nitter.rdrama.net/eig/status/2107420544870003022">Thatchaphol Saranurak (@eig): &quot;Another very normal day, lol APSP ...&quot;</a></li>
<li><a href="https://hub.valency.io/works/W_s7c8pz9c">Truly Subquadratic 3 SUM and Truly Subcubic APSP ... — Valency Hub</a></li>
<li><a href="https://headlinesbriefing.com/dev/hacker-news/subquadratic-3sum-and-subcubic-apsp-via-sparse-triangles-289f19fc">Subquadratic 3 SUM and Subcubic APSP via Sparse Triangles</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI coding agents`, `#algorithm discovery`, `#3SUM`, `#APSP`

---

### 更多动态

<a id="item-tech-news-4"></a>
#### [Copilot CLI v1.0.115-4 改进 ACP 澄清与稳定性](https://github.com/github/copilot-cli/releases/tag/v1.0.115-4) ⭐️ 6.0/10

GitHub Copilot CLI 发布 v1.0.115-4，为支持表单的 ACP 编辑器启用结构化澄清问题。新版本修复插件初始化竞态，避免其阻塞新会话或导致现有会话无法恢复；同时改进 Windows 进程清理，可在父进程退出后清理 Git 命令、钩子和语言服务器检查产生的子进程。

github · copilot-cli-release-app\[bot\] · 11月21日 01:53

<a id="item-tech-news-5"></a>
#### [lookatmyquant 宣称 Inkling-2-Mini 可在 5.4 GB 内存运行](https://github.com/ShinMegamiBoson/lookatmyquant) ⭐️ 6.0/10

开源量化项目 ShinMegamiBoson/lookatmyquant 宣称，其量化方案可让 Inkling-2-Mini 在 5.4 GB 内存中运行，为内存受限的本地推理提供了一种选择。该数字目前属于仓库的容量主张；现有材料没有说明具体量化格式、最低硬件配置或可复现的质量与速度基准，因此不能确认所有具备 5.4 GB 内存的设备都能获得实用性能。

hackernews · k\_\_ · 11月21日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50591853)

<a id="item-tech-news-6"></a>
#### [Axion 1.0 用三阶段训练挑战商业智能体](https://the-decoder.com/bytedance-argues-most-ai-training-phases-are-unnecessary-and-backs-it-up-with-a-competitive-open-model/) ⭐️ 6.0/10

据 The Decoder 报道，字节跳动与多所美国大学研究者推出 AI 智能体 Axion 1.0，称其仅经过三个训练阶段，就在相关基准上达到可与 OpenAI、Anthropic 顶级商业模型竞争的表现。研究者将这一结果归因于精心筛选的训练数据，而非持续增加训练步骤；模型、训练数据和代码均已免费开放。来源未列出具体基准名称与分数、模型架构、许可证或复现设置，因此其“竞争性”及数据驱动的解释目前仍主要是研究团队主张，缺少可供独立核验的量化细节。

rss · The Decoder · 11月21日 09:17

<a id="item-tech-news-7"></a>
#### [腾讯元宝与 KCL 发布群聊 Agent 记忆基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947677&amp;idx=3&amp;sn=0797fbd2116a405b44176c97577757d8) ⭐️ 4.0/10

腾讯元宝与 KCL 发布一个基于群聊构建的 Agent 记忆基准，发布信息称其为该方向首个基准，使用的题面材料包含 8 万条群聊消息。基准强调 AI“记得住”并不等于在实际任务中“用得好”，旨在评估聊天信息记忆及其调用能力。现有公开内容未披露数据构建方法、评测任务、指标、模型结果、代码或使用方式，因此尚无法核验其覆盖度、可复现性和区分不同 Agent 记忆能力的效果。

rss · 量子位 · 11月21日 09:52