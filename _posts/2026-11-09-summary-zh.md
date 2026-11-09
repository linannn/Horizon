---
layout: default
title: "Horizon 每日速递：2026-11-09"
description: "AI 精选的技术与研究日报"
date: 2026-11-09
lang: zh
locale: zh-CN
---

> 从 21 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [高盛据报收回 Claude Code 内部权限](#item-tech-news-1) ⭐️ 7.0/10
2. [从 Claude Code 转向 Pi 的编码代理实践](#item-tech-news-2) ⭐️ 7.0/10
3. [Co-Design Bench 显示编码智能体仅完全解决 26.4% 真实任务](#item-tech-news-3) ⭐️ 7.0/10
4. [Llama-modchip：64GB RAM 无 GPU 运行 284B DeepSeek](#item-tech-news-4) ⭐️ 6.0/10
5. [parse\_number SQLite 扩展：C 与 Rust 基准对比](#item-tech-news-5) ⭐️ 6.0/10
6. [斯坦福 CS146S 将开源维护者引入课程](#item-tech-news-6) ⭐️ 4.0/10
7. [未命名 AI 编程代理宣称通过率达 70%](#item-tech-news-7) ⭐️ 4.0/10
8. [Karpathy 用 Claude 将 4,300 万条 HN 评论筛成 6,454 个视频](#item-tech-news-8) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [高盛据报收回 Claude Code 内部权限](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 7.0/10

**级别**: 核心必看

据《The State of AI》报道，高盛正从银行家和交易员处收回 Claude Code，反映编码代理在受监管金融机构中的部署遇到阻力。现有材料将相关问题集中在敏感金融数据访问、代理对终端和内部网络的权限、合规审计与数据授权，以及计费用量失控。由于未提供报道正文，无法核实撤用的具体范围、时间表、是否完全禁用，以及高盛确认了哪些原因。

hackernews · TheWiggles · 11月8日 18:16 · [社区讨论](https://news.ycombinator.com/item?id=50415628)

**「从试验到权限收紧」** 这次调整并非高盛首次限制生成式 AI：报道显示，该行 4 月已禁止香港银行家使用 Claude，而到 7 月，CIO Marco Argenti 仍在公开赞扬非技术员工进行“vibe coding”。高盛随后在 10 月发布内部指引，将 Claude Code、GitHub Copilot 等编码工具限制给该行 12,000 名工程师，结束了面向银行家和交易员的数月试验。

**「非工程岗位的代理权限被收回」** 据外媒转述，高盛已把 Claude Code 和 GitHub AI 工具限制给该行 12,000 名工程师，撤回银行家和交易员此前更广泛的访问权限。其直接影响是，原本由银行家和交易员在装有客户信息的机器上构建市场模型、监控客户流的非技术工作流，必须改由获授权的工程师或受控、审计化流程承接；依赖直接在生产终端运行代理代码的现有做法将无法继续。

**「安全风险与计费压力」** 评论者 lukebuehler 认为，半自动运行的代理若能通过银行家的主终端接触客户或交易信息、邮件、互联网和内部网络，会形成严重的组合风险；legitster 则称其所在组织因持续的 Claude 计费超额而收回访问权限，并提到 Gemini 通过统一计费和限流吸引用户。steveBK123 还强调应用访问授权、数据可审计性和审批链等合规要求，但这些评论均属于个人观点或个案，不能证明高盛撤用权限的具体原因。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers">Goldman Sachs is pulling Claude Code from its bankers and traders</a></li>
<li><a href="https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/">Goldman Sachs pulls AI coding tools from traders and bankers</a></li>
<li><a href="https://www.siliconreport.com/goldman-sachs-cuts-off-most-staff-from-claude-code-and-github">Goldman Sachs cuts off most staff from Claude Code and GitHub</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/goldman-sachs-restricts-ai-coding-150508601.html?fr=sycsrp_catchall">Goldman Sachs Restricts AI Coding Tools to Engineers</a></li>
<li><a href="https://aigovernance.com/news/goldmans-claude-code-ban-exposes-ai-coding-tool-governance-gap">Goldman&#x27;s Claude Code Ban Exposes AI Coding Tool Governance…</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding agents`, `#enterprise security`, `#AI governance`, `#LLM costs`

---

<a id="item-tech-news-2"></a>
### [从 Claude Code 转向 Pi 的编码代理实践](https://caleb.software/posts/claude-to-pi.html) ⭐️ 7.0/10

**级别**: 核心必看

一名开发者在文章中分享把编码代理工作流从 Claude Code 转向 Pi 的实践，比较重点包括多项目会话管理、GUI 与 TUI 的使用方式、代理 harness 的效率，以及 Anthropic 订阅条款和自定义模型 API 带来的集成取舍。这是开发工具与工作流迁移经验，并非 Claude、Anthropic 或 Pi 发布了新的模型或平台能力，因此其中的效果判断应视为作者经验。

hackernews · karagenit · 11月8日 03:11 · [社区讨论](https://news.ycombinator.com/item?id=50410107)

**「此前的代理工作流」** 这里的 Pi 指文章讨论的可定制编码代理 harness；Claude Code 与 Pi 的差异主要发生在代理运行框架和工作流层面，而不是模型发布层面。Caleb 在 Claude Code 随 Claude Pro 订阅出现后便开始使用它，到迁移前已经使用一年多，因此这次转向属于既有工作流的调整，而非初次采用编码代理。

**「迁移前需检查兼容性」** 准备改用 Pi 或其他第三方 harness 的开发者，应把会话管理方式、界面偏好和订阅条款纳入迁移检查；评论者还警告，Anthropic 模型依赖的自定义请求头、隐藏开关和未公开 API 特性未获完整支持时，Claude Code 与替代 harness 可能出现不同的代理行为和 token 消耗。

**「控制力与原生兼容性的争论」** 支持者认为 Pi 的可定制性让用户能从“驾驶代理”转向“编排代理”，并称简洁的系统提示可以减少人工干预；反对者则不建议用 Anthropic 订阅驱动 Pi，认为这可能违反服务条款，且 Claude Code 使用的部分通信机制在第三方 harness 中不会默认保留。另一位用户因项目和会话增多而改用桌面 GUI，称折叠细节后历史记录更容易浏览。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://caleb.software/posts/claude-to-pi.html">Goodbye Claude, hello Pi</a></li>
<li><a href="https://dzen.ru/a/avAVP5i5GAUJV_Pe">Калеб перешёл с Claude Code на Pi ради управляемой среды | Дзен</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Pi`, `#Claude Code`, `#agent harnesses`, `#developer workflows`

---

<a id="item-tech-news-3"></a>
### [Co-Design Bench 显示编码智能体仅完全解决 26.4% 真实任务](https://the-decoder.com/ai-coding-agents-still-need-human-cleanup-on-nearly-three-out-of-four-tasks-in-a-real-world-test/) ⭐️ 7.0/10

**级别**: 核心必看

阿里推出的新基准 Co-Design Bench 使用此前已在实践中导致失败的真实用户请求来测试编码智能体。据 The Decoder 报道，表现最佳的 GPT-6 Astra 也仅完全解决了 26.4% 的任务，而同一批模型在较旧基准上的得分超过 99%。这一差距表明，常用基准可能显著高估编码智能体处理现实开发任务的可靠性。

rss · The Decoder · 11月8日 09:50

**「Co-Design Bench 的评估设计」** Co-Design Bench 是一项“无需参考答案”（reference-free）的基准，从 26,314 次真实用户编程会话的 37,463 条去重查询中筛选出 273 个任务，并设置 Multimodal Editing（ME）和 Repository Editing（RE）两条赛道。其 26.4% 指标衡量智能体是否完整满足任务的全部要求；未完全通过意味着仍需人工补救，并不代表代理没有产出代码或毫无进展。

**「编码智能体仍需人工复核」** 开发团队不应仅凭传统基准中超过 99% 的成绩就取消编码智能体改动的人工复核，而应将 Co-Design Bench 作为发布前的压力测试：在其 273 项真实用户任务中，表现最佳的 GPT-6 Astra 也仅有 26.4% 完整通过。由于这些任务选自曾导致失败的请求，该结果反映的是困难案例，而不能外推为所有生产任务的普遍成功率。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/ai-coding-agents-still-need-human-cleanup-on-nearly-three-out-of-four-tasks-in-a-real-world-test/">AI coding agents still need human cleanup on nearly three out of four tasks in a real-world test</a></li>
<li><a href="https://arxiv.org/abs/2610.35138">[2610.35138] Co-Design Bench: Multimodal Collaborative Coding ...</a></li>
<li><a href="https://creati.ai/ai-news/2026-11-08/real-world-benchmark-finds-coding-agents-still-require-human-cleanup-on-most-tasks/">Real-world benchmark finds coding agents still require human ...</a></li>
<li><a href="https://letsdatascience.com/news/co-design-bench-shows-top-coding-agent-fully-solves-264-of-t-bf2e0c23">Co-Design Bench shows top coding agent fully solves 26.4% of ...</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#benchmarking`, `#evaluation`, `#human-in-the-loop`, `#software engineering`

---

### 更多动态

<a id="item-tech-news-4"></a>
#### [Llama-modchip：64GB RAM 无 GPU 运行 284B DeepSeek](https://github.com/synchopate/llama-modchip) ⭐️ 6.0/10

https://github.com/synchopate/llama-modchip 是开源项目 Llama-modchip 的原始仓库；该项目声称，284B 参数的 DeepSeek 模型可在使用 64GB RAM、且不配备 GPU 的机器上运行，面向希望以本地内存承载超大模型的开发者。现有材料未说明具体 DeepSeek 版本、量化格式、内存占用口径、吞吐量或输出质量评测，也没有提供可复现的基准方法。因此，“模型可装入 64GB 内存并运行”目前仍是项目方主张，尚不能证明其在速度、质量或相较标准 llama.cpp 推理方案方面的优势。

hackernews · joshcsimmons · 11月8日 10:22 · [社区讨论](https://news.ycombinator.com/item?id=50411961)

<a id="item-tech-news-5"></a>
#### [parse\_number SQLite 扩展：C 与 Rust 基准对比](https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/) ⭐️ 6.0/10

Simon Willison 使用 Claude Chat（Opus 5.5）生成并迭代了一个 SQLite 可加载扩展 \`parse\_number\(value\)\`：去掉 \`,\`、\`$\`、\`£\`、\`%\` 并处理前导 \`-\`，把 \`-$1,234.56\` 或 \`&\#x27;12.5%&\#x27;\` 转成数值，无法解析时返回 \`NULL\`，以便在 SQLite 中求和和排序。首轮产物中，C 扩展为 14 KB，而基于 Rusqlite 和 sqlite-loadable-rs 的 Rust 扩展分别为 321 KB 和 298 KB；在超过 200 万行的“每行净成本”测试中，重写后的 C 版在混合数据、纯整数和纯小数上的耗时分别为 19、16、18 ns，两版 Rust 分别为 46、36、55 ns 和 41、32、47 ns，初版 C 则为 67、25、106 ns。该结果来自作者发布的一次 Claude 辅助实验，原文未给出硬件、重复次数或统计分布，因此不能视为独立验证。

rss · Simon Willison · 11月8日 22:26

<a id="item-tech-news-6"></a>
#### [斯坦福 CS146S 将开源维护者引入课程](https://latent.space/p/cs146s/) ⭐️ 4.0/10

斯坦福大学 CS146S 在第二轮运行中将开源项目维护者引入课程，要求学生先学习一个陌生代码库，再提出代码变更。课程由此追问：当编码代理已经能通过一个提示完成上一学年的作业时，教师应如何重新设计作业。本期 Latent Space 对话邀请了 Mihail Eric 和 Monaco 参与，但现有预告尚未披露具体课程结构、代理工作流、工具链或成效数据。

rss · Latent Space · 11月8日 21:41

<a id="item-tech-news-7"></a>
#### [未命名 AI 编程代理宣称通过率达 70%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247940486&amp;idx=1&amp;sn=8678d2fd2fb6c737c7acfdcfd4733b86) ⭐️ 4.0/10

据《量子位》报道，一款未披露名称的 AI 编程代理被用于承担代码编写、任务分派和 Bug 查找，并宣称表现超过 Codex 与 Claude Code，测试通过率为 70%。文章标题还称其“接管”了一家拥有 8 万 Star 的开源项目，但现有正文未说明该系统、基准方法、样本范围、对照设置、限制或复现方式，因此 70%通过率及其比较结论目前只能视为厂商或报道方主张。

rss · 量子位 · 11月8日 14:32

<a id="item-tech-news-8"></a>
#### [Karpathy 用 Claude 将 4,300 万条 HN 评论筛成 6,454 个视频](https://the-decoder.com/andrej-karpathy-built-a-curated-video-platform-in-a-weekend-using-claude-and-20-years-of-hacker-news/) ⭐️ 4.0/10

OpenAI 联合创始人 Andrej Karpathy 据报道用一个周末，借助 Claude Opus 5.5 筛选 20 年间的 4,300 万条 Hacker News 评论，将其整理为 6,454 个策展视频并搭建视频平台。Karpathy 称该平台的推荐效果优于 YouTube 自有推荐，但现有材料没有提供对比评测方法或可复现的实现细节。因此，这目前更接近一个快速完成的原型，尚不能视为经过验证的大规模内容处理方案。

rss · The Decoder · 11月8日 14:23