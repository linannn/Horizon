---
layout: default
title: "Horizon 每日速递：2026-11-18"
description: "AI 精选的技术与研究日报"
date: 2026-11-18
lang: zh
locale: zh-CN
---

> 从 82 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Microsoft Agent Framework 恶意 PyPI 版本窃取凭据](#item-tech-news-1) ⭐️ 8.0/10
2. [Goose v1.60.0 新增代理工作流操作并调整兼容性](#item-tech-news-2) ⭐️ 7.0/10
3. [Pydantic AI v2.70.0 修复两项高危拒绝服务漏洞](#item-tech-news-3) ⭐️ 7.0/10
4. [FrontierHarness Eval v1.1：编码代理组合评测](#item-tech-news-4) ⭐️ 7.0/10
5. [Claude Code 团队如何验证代码变更](#item-tech-news-5) ⭐️ 7.0/10
6. [盲审裁判揭示 Claude 风格指南短板](#item-tech-news-6) ⭐️ 7.0/10
7. [Claude Code 推出实验性 Code Mode](#item-tech-news-7) ⭐️ 7.0/10
8. [Replit 发布 Missions 并开源 DataCat](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenAI 医疗代理自动处理授权与保险申请](#item-tech-news-9) ⭐️ 6.0/10
10. [OpenClaw 结束 ChatGPT 登录测试，支持 Business 与 GPT-6.2 Astra、Sol](#item-tech-news-10) ⭐️ 6.0/10
11. [Microsoft MAI 发布模型与 Licensed Weights 方案](#item-tech-news-11) ⭐️ 6.0/10
12. [微软发布 MAI Code 2 与 Code 2 Flash 编码模型](#item-tech-news-12) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Microsoft Agent Framework 恶意 PyPI 版本窃取凭据](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi) ⭐️ 8.0/10

**级别**: 核心必看

Wiz 报告称，Microsoft Agent Framework 的 PyPI 包 \`agent-framework\` 在 2026 年 11 月 17 日出现恶意版本 1.26.1 和 1.26.2，并于约 21:30 UTC 后下架。恶意版本植入 \`.pth\` 文件，使 Python 启动时执行凭据窃取器，收集环境变量、凭据文件、Azure 与 Azure DevOps 托管标识及 OIDC 令牌，再回传至 \`webhook.site\`。安装过这两个版本的开发者和 CI 环境面临 Azure、Azure DevOps、OIDC 及 CI 凭据暴露风险，但现有材料未说明受影响安装数量或实际外泄规模。

rss · AI 热榜 · 11月17日 22:03

**「此前的正常版本与发布链路」** PyPI 此前公开的 \`agent-framework\` 1.26.0 是 Microsoft Agent Framework 的正常版本。项目维护者在 GitHub issue 中指出，恶意载荷并未存在于源码仓库，因此 1.26.1 很可能是在常规发布流水线之外上传的，指向 PyPI 发布凭据或受信任发布者配置遭滥用，而非仓库源码本身被直接篡改。

**「固定安全版本并轮换凭据」** 安装过 \`agent-framework\` 1.26.1 或 1.26.2 的开发机和 CI 应将依赖固定为 \`agent-framework==1.26.0\`，不要依赖“升级到 latest”完成处置，因为 PyPI 上传凭据是否已撤销尚未确认。由于恶意 \`.pth\` 文件在 Python 启动时即会执行，即使未导入该包也可能触发窃取，相关环境应将 Azure、Azure DevOps、OIDC 和 CI 凭据视为可能暴露并予以轮换。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi">Microsoft agent-framework 1.26.1/1.26.2 恶意版本被发布至 PyPI，窃取 Azure 与 CI 凭据</a></li>
<li><a href="https://github.com/microsoft/agent-framework/issues/10411">[Python]: ⚠️ agent-framework 1.26.1 on PyPI is ... - GitHub</a></li>
<li><a href="https://pypi.org/project/agent-framework/">agent-framework · PyPI</a></li>
<li><a href="https://opensourcemalware.com/blog/agent-framework-pypi-compromised">Official Microsoft agent-framework PyPI package compromised</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#supply-chain security`, `#PyPI`, `#credential theft`, `#Microsoft Agent Framework`

---

<a id="item-tech-news-2"></a>
### [Goose v1.60.0 新增代理工作流操作并调整兼容性](https://github.com/aaif-goose/goose/releases/tag/v1.60.0) ⭐️ 7.0/10

**级别**: 核心必看

Goose v1.60.0 已发布，为开发者新增 SkillOperation、可执行命令、斜杠命令、叹号命令和 steering operation，并加入 Cortecs、Onysoft 两个声明式 provider 以及 GDK 可复用轮次上限。修复覆盖 cron 变更前校验、Ollama XML 工具调用参数、OpenAI 在存在工具时发送 tool\_choice=auto、流错误及提前结束上报，以及会话导出遇到已关闭 stdout 管道等问题。兼容性要求也随之提高：Rust MSRV 升至 1.95.0、macOS 最低版本升至 13、Electron 升至 45.2.3，同时移除了 chat mode 和 goose review 子命令。

github · github-actions\[bot\] · 11月17日 23:08

**「扩展与运行层重构」** 此次重构把平台扩展从 MCP runtime 中分离，将 ExitOnErrorOperation 移入 oi-kit，并移除 GDK hook API，改由 Goose 主运行循环触发 hooks。这意味着采用相关 GDK 接口或依赖原有扩展边界的代码需要同步调整，而 skills 和各类命令则成为新的代理工作流控制点。

**「升级兼容性与权限变化」** 升级构建环境需要使用 Rust 1.95.0 或更高版本，macOS 用户需要 13 或更高版本；依赖 chat mode 或 goose review 的脚本和流程也必须迁移，因为这两个入口已被删除。Unix 上的请求日志以及共享系统中的 Goose 临时目录将按修复后的策略保持私有。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/aaif-goose/goose/releases/tag/v1.60.0">aaif-goose/goose released v1.60.0</a></li>

</ul>
</details>

**标签**: `#coding agents`, `#developer tooling`, `#agent workflows`, `#open source`, `#MCP ecosystem`

---

<a id="item-tech-news-3"></a>
### [Pydantic AI v2.70.0 修复两项高危拒绝服务漏洞](https://github.com/pydantic/pydantic-ai/releases/tag/v2.70.0) ⭐️ 7.0/10

**级别**: 核心必看

Pydantic AI v2.70.0 的发布说明称，Pydantic AI Harness 已修复两项高危拒绝服务漏洞，修复版本为 \`pydantic-ai-harness\` 0.70.0。启用 \`strip\_ansi=True\`（0.13.0 之前名为 \`OverflowingToolOutput\`）且工具结果可受攻击者影响时，旧版 ANSI 转义序列剥离逻辑会随单行长度呈二次时间增长；数百千字节、含大量未终止转义序列的输出可导致事件循环被占用数十秒至数分钟。使用 \`redact\_secrets\` 或 \`secret\_data\(\)\`、并采用默认包含的 \`jwt\` 模式扫描攻击者可影响文本时，旧版 JWT 模式也可能因二次复杂度回溯而造成同类阻塞。使用方应将 Harness 升级至 0.70.0，并注意新版 \`jwt\` 模式不再匹配 header 段含 \`-eyJ\` 的 JWT，这一变化可能影响相关脱敏结果。

github · dsfaccini · 11月17日 22:44

**「工具结果处理机制」** Pydantic AI Harness 可在工具结果进入模型前执行 ANSI 清理和密钥脱敏：ANSI 清理自 0.13.0 起通过 \`strip\_ansi=True\` 启用，此前对应名称为 \`OverflowingToolOutput\`；密钥脱敏可由 \`redact\_secrets\` 或 \`secret\_data\(\)\` 启用，其默认规则包含 \`jwt\` 模式。修复后的 JWT 模式不再匹配 header 段含 \`-eyJ\` 的 JWT，因此使用相关规则的开发者升级后仍需核对预期的凭据识别范围。

**「部署与兼容性处理」** 使用受影响路径的开发团队应核对并升级到 \`pydantic-ai-harness\` 0.70.0：在旧版中，攻击者可影响的工具输出或文本可令单个代理运行占用事件循环数十秒至数分钟。升级后应回归验证 JWT 脱敏规则，因为修复后的 \`jwt\` 模式不再匹配 header 段含 \`-eyJ\` 的 JWT，依赖该特殊格式识别的场景需改用自定义规则或调整预期。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/pydantic/pydantic-ai/releases/tag/v2.70.0">pydantic/pydantic-ai released v2.70.0</a></li>
<li><a href="https://pydantic.dev/articles/pydantic-ai-v2">Pydantic AI v2: capabilities, a leaner core, and the Harness</a></li>

</ul>
</details>

**标签**: `#pydantic-ai`, `#coding-agents`, `#security`, `#denial-of-service`, `#python`

---

<a id="item-tech-news-4"></a>
### [FrontierHarness Eval v1.1：编码代理组合评测](https://runta.com/blog/introducing-frontierharness-eval-v1-1/) ⭐️ 7.0/10

**级别**: 核心必看

FrontierHarness Eval v1.1 在 Terminal-Bench 上比较了不同的编码代理 harness、代理设置与模型组合，为开发者和团队选择配置提供依据。评测方称，在本次运行中，64% 的总支出花在了未通过 Terminal-Bench 验证器的任务上，凸显了任务得分之外的成本差异。该评测强调按具体任务权衡组合，而非给出一个适用于所有场景的单一“最佳”配置。

hackernews · Edward40 · 11月17日 14:53 · [社区讨论](https://news.ycombinator.com/item?id=50532191)

**「模型与 Harness 的评测分层」** 理解这组结果的前提，是把编码模型与 harness 分开：harness 是模型外层负责工具调用、命令执行和迭代的代理框架，因此同一模型在不同 harness 中可能呈现不同行为。FrontierHarness Eval v1.1 在同一组 62 个 Terminal-Bench 任务上重复测试 22 种 harness 与 5 种模型的组合，共进行 27,280 次运行，并比较任务验证结果与成本；因此这里的“最佳”是相对于特定模型、任务集和评测设置的选型结果，而非可无条件套用的统一排名。

**「选型需考虑任务与失败成本」** 开发者不应仅依据模型能力或总体成绩选型，而应结合自身任务领域、工具集和执行约束匹配 harness 与模型，并单独核查验证失败任务造成的支出；本次评测中这一比例达到总支出的 64%。

**「社区质疑统一排名」** 评论者 seize\_thecheese 认为“64% 支出浪费”的叙事在所选模型与基准条件下并不意外，并批评早期标题有迎合“AI 浪费钱”倾向；其随后称标题已被修改。xyzzy\_plugh 认为最佳 harness 取决于具体问题，而 cpeth 则根据个人经验称 Claude Opus 5.5 在 Claude Code 与 Copilot 中表现相近、模型差异更显著，这些都是社区观点而非评测结论。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://runta.com/blog/introducing-frontierharness-eval-v1-1/">What is the best harness for each model?</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#model-harness-evaluation`, `#Terminal-Bench`, `#AI-engineering`

---

<a id="item-tech-news-5"></a>
### [Claude Code 团队如何验证代码变更](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 的 Claude Code 团队公开了其验证编码代理改动的工程思路：使用按变更维护的 skill 文件，借助“chrome-for-Claude”工具进行浏览器回归检查，并让多个代理并行执行验证；这些是团队描述的工作流，而非一项新功能发布。人工复核由验证失败触发，团队同时强调将改动拆成小批次，并指出并行代理、复核工作量与 token 成本之间存在取舍。

hackernews · craigmart · 11月17日 10:20 · [社区讨论](https://news.ycombinator.com/item?id=50529612)

**「验证与人工复核的分工」** 这一思路的前提是，编码代理产生的差异无法全部由人阅读，因此团队把验证失败作为决定哪些差异需要人工介入的信号。是否审阅每一份 diff 被视为项目层面的成本与风险选择，文章给出的实践是把非机械改动拆成足够小、可以逐项复核的批次。

**「落地流程与成本约束」** 采用类似流程的团队可以为每次变更准备专用 skill、用“chrome-for-Claude”执行浏览器回归检查、并行运行验证，并让失败项优先进入人工复核；代价是增加代理调用与 token 消耗。若一次改动涉及数百个文件，仍需先将其拆小，否则依赖失败信号的人工分流难以成立。

**「社区质疑成本与可扩展性」** 评论者主要质疑这套流程的成本与可复制性：OtherShrezzing 认为按变更让 Claude 调用浏览器工具过于昂贵，并主张 Playwright 等工具或可不消耗 LLM token 地完成同类回归检查；girvo 则称自己仅使用一两个代理每月就已花费 2,000 美元，因此不相信该方法能扩展到数十或数百个并行代理。也有评论者支持将变更拆小以便人工审阅，这些均属于用户观点而非独立验证。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/">How the Claude Code team thinks about verification</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#coding-agents`, `#software-verification`, `#ai-development-workflows`

---

<a id="item-tech-news-6"></a>
### [盲审裁判揭示 Claude 风格指南短板](https://blog.qiaomu.ai/write-like-yourself-with-ai) ⭐️ 7.0/10

**级别**: 核心必看

文章提出用“盲审裁判”比较 AI 输出与作者本人文本的风格相似度，为提示词和风格模仿评测提供了一种可复用方法。据文章转述的 Mike Taylor 实验，Claude 读完本人文章后生成的风格指南，在对上三种优化方法时，于 80% 至 95% 的测试文章中均落后；改用 Opus 5.5 后，不加入指南反而更像本人。现有材料未披露测试样本量、三种方法的具体名称或裁判一致性，因此这些结果属于文章报告的实验发现，尚不足以视为对不同模型和评测设置的普遍结论。

rss · 向阳乔木 · 11月17日 18:46

**「盲审裁判的评测基础」** 理解这项实验的前提，是区分两种风格模仿路径：让 Claude 从作者既有文章中归纳风格指南后据此写稿，或直接使用提示词优化方法。盲审裁判依据最终成稿与作者样本的风格相似度进行比较，而不依据候选文本采用了哪种生成方法。

**「保留无风格指南基线」** 对落地个人化写作流程的团队，实际动作是保留“不加载自动生成风格指南”的对照分支，再根据盲审结果决定是否接入指南；文章所述 Opus 5.5 实验表明，增加归纳出的指南未必提升风格相似度。由于材料未披露样本量、三种优化方法名称及裁判一致性，宜先在自身语料上复测，不能将该结果推广为所有模型的定论。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.qiaomu.ai/write-like-yourself-with-ai">让 AI 写得像自己：Every 评测负责人试了六年，最后靠一个&quot;盲审裁判&quot;做到了</a></li>

</ul>
</details>

**标签**: `#AI评测`, `#风格模仿`, `#盲审裁判`, `#提示词优化`

---

<a id="item-tech-news-7"></a>
### [Claude Code 推出实验性 Code Mode](https://x.com/ClaudeDevs/status/2122801681939234950) ⭐️ 7.0/10

**级别**: 核心必看

Claude Devs 宣布，Claude Code 新增实验性 Code Mode：Claude 会编写脚本，以更复杂的方式串联多个工具，并能在长命令仍在运行时继续回复用户。开发者需将环境变量 CLAUDE\_CODE\_EXPERIMENTAL\_CODE\_MODE 设置为 1 才能开启该模式，官方文档见 http://code.claude.com/docs/en/code-mode。

rss · AI 热榜 · 11月17日 21:18

**「工具调用层的新路径」** Code Mode 改变的是 Claude Code 的工具使用层，而不是 Claude 模型本身的版本。官方将其标为实验性替代路径，但公告未说明默认适用范围、支持的工具集合或稳定性承诺，相关兼容性与限制应以随附的 Code Mode 文档为准。

**「多工具工作流改为脚本执行」** 对需要串联多个工具的开发者，Code Mode 可将多项调用合并到一段 JavaScript 中执行，减少逐项发起调用的交互开销。该功能仍属实验性；开发者需设置 \`CLAUDE\_CODE\_EXPERIMENTAL\_CODE\_MODE=1\` 才会启用，并应按官方文档确认当前会话的适用条件。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/ClaudeDevs/status/2122801681939234950">Claude Code 推出实验性 Code Mode 工具调用方式</a></li>
<li><a href="https://code.claude.com/docs/en/code-mode">Run tool calls from code with Code Mode - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding agents`, `#tool orchestration`, `#Code Mode`, `#developer workflows`

---

<a id="item-tech-news-8"></a>
### [Replit 发布 Missions 并开源 DataCat](https://replit.com/blog/introducing-replit-missions) ⭐️ 7.0/10

**级别**: 核心必看

Replit 宣布推出 Missions，面向希望将复杂软件开发任务交给智能体执行的用户：用户先设定目标、预算和边界，再由智能体集群并行完成规划、构建、测试与迭代。系统还设有独立 AI 裁判，依据预先约定的标准验收交付结果，将执行与评判分配给不同角色。公告同时宣布开源 DataCat，但未提供其实现细节、Missions 的具体可用范围或实际效果数据，因此这些能力目前主要属于厂商公告内容，尚无独立实测结论。

rss · AI 热榜 · 11月17日 18:00

**「从 Replit Agent 到 Missions」** Replit 既有的 Replit Agent 主要用于从零到一构建 Web 应用原型，而 Missions 覆盖规划、构建、测试、迭代和独立验收等更完整的项目流程。Replit 将 DataCat 描述为“小团队借助 Missions 可以完成什么”的一个实践示例，但现有材料没有说明它是否承担底层编排功能，以及其架构和可复用范围。

**「采用者需先定义验收与成本边界」** 对开发团队而言，Missions 提供的是在既定预算和边界内推进复杂交付的受控流程，而不是一次运行就保证成功的自动化工单；采用者应在启动前写清结果、验收标准和允许智能体调整的范围。Replit 的套餐页与计费文档分别说明套餐包含不同 AI 用量，Agent 使用量按月计费并涉及额度、结转、充值和折扣，因此团队评估时应核对当前用量规则，不能把公告中的预算约束直接当作完整成本上限。现有材料没有提供成功率、节省工时等实测数据，因而尚不能据此量化生产率收益。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://replit.com/blog/introducing-replit-missions">Replit 发布 Missions，用智能体集群按目标完成复杂工作并开源 DataCat</a></li>
<li><a href="https://www.aihub.cn/tools/coding/replit-agent/">Replit Agent： Replit 推出的AI编程 工 具 - AIHub</a></li>
<li><a href="https://x.com/Replit/status/2122764465804644548">Replit ⠕ on X: &quot;DataCat is just one example of what a small ...</a></li>
<li><a href="https://replit.com/pricing">Pricing and Plans | Replit</a></li>
<li><a href="https://docs.replit.com/help/pricing-and-plans">Pricing and plans - Replit Docs</a></li>

</ul>
</details>

**标签**: `#Replit Missions`, `#coding agents`, `#multi-agent orchestration`, `#AI judge`, `#DataCat`

---

### 更多动态

<a id="item-tech-news-9"></a>
#### [OpenAI 医疗代理自动处理授权与保险申请](https://the-decoder.com/ai-agents-are-starting-to-fill-out-medical-forms-and-file-insurance-requests-in-place-of-human-staff/) ⭐️ 6.0/10

据 The Decoder 报道，OpenAI 正计划让 GPT-6 Astra 和 GPT-6 Luna 通过计算机操作代理，像人工一样使用诊所现有软件和保险门户，自动完成医疗行政事务。其中，Luna 处理事先授权等任务的价格约为每项 8.5 美分，CVS Health 与 Cigna Healthcare 已被报道正在部署这项技术。报道未提供 API、系统架构或具体集成方式，因此尚不能确认这些部署的深度及其是否已完全替代人工流程。

rss · The Decoder · 11月17日 16:55

<a id="item-tech-news-10"></a>
#### [OpenClaw 结束 ChatGPT 登录测试，支持 Business 与 GPT-6.2 Astra、Sol](https://x.com/openclaw/status/2122809472271958517) ⭐️ 6.0/10

OpenClaw 宣布“Sign in with ChatGPT”结束测试，用户现在可在 OpenClaw 内使用自己的 ChatGPT 套餐，其中包括 ChatGPT Business。OpenClaw 方面同时确认支持新模型 GPT-6.2 Astra 和 Sol；被引用的 @OpenAIDevs 信息称，ChatGPT Business 已可通过这一登录方式用于 Notion、v0、OpenClaw 等工具。现有来源未说明具体认证机制、套餐限制、费用或隐私处理方式。

rss · AI 热榜 · 11月17日 21:49

<a id="item-tech-news-11"></a>
#### [Microsoft MAI 发布模型与 Licensed Weights 方案](https://microsoft.ai/news/microsoft-ignite-2026-mai-keynote/) ⭐️ 6.0/10

微软 MAI 在 Ignite 2026 主题演讲中宣布发布一系列强调性价比的模型，并推出 MAI Licensed Weights。该方案允许客户定制模型权重，再部署到自己的 Azure 环境中，由客户掌控权重与数据。当前公开摘要未给出模型名称、基准测试、许可条款、可用区域或部署步骤，因此其性价比表现和实际可定制范围尚无法据此核实。

rss · AI 热榜 · 11月17日 18:14

<a id="item-tech-news-12"></a>
#### [微软发布 MAI Code 2 与 Code 2 Flash 编码模型](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 4.0/10

微软宣布面向日常企业编码任务发布 MAI Code 2 和 MAI Code 2 Flash，并称其定价低于竞品。按发布摘要提供的数据，MAI Code 2 在四项基准的平均成绩上达到 GPT 6.1 Sol 的 98%，成本为后者的 40%；相较 Claude Opus 5.5，其成绩为 96%，成本仅为 5%。另一项盲测前端评审中，MAI Code 2 有 64% 的情况胜过 GPT-6 Sol。现有材料未提供绝对价格、基准测试方法、API 与可用范围，也没有 Code 2 Flash 的独立数据，因此这些结果仍是厂商口径，尚不足以判断实际开发体验或迁移收益。

hackernews · AI 热榜 · 11月17日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=50535885)