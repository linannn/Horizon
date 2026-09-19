---
layout: default
title: "Horizon 每日速递：2026-09-19"
description: "AI 精选的技术与研究日报"
date: 2026-09-19
lang: zh
locale: zh-CN
---

> 从 60 条内容中筛选出 7 条重要资讯。

---

1. [ZCode 被曝静默上传工作区快照与完整 Git 历史到云端](#item-1) ⭐️ 8.0/10
2. [Trail of Bits 借助 AI Agent 自建工具完成 Miden zkVM 审计](#item-2) ⭐️ 8.0/10
3. [Dan Abramov 用 AI 智能体“凭感觉”证出 Conway 猜想](#item-3) ⭐️ 7.0/10
4. [Claude Code v2.1.277 借助新 mods 机制支持 AGENTS.md](#item-4) ⭐️ 7.0/10
5. [DoorDash 用多智能体 LLM 清理 6 万个陈旧功能开关](#item-5) ⭐️ 7.0/10
6. [Copilot 代码审查获得更清晰的时间线与更智能的自动解决能力](#item-6) ⭐️ 6.0/10
7. [Claude Code v2.1.276 修复代理网关场景下的 400 错误回归](#item-7) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [ZCode 被曝静默上传工作区快照与完整 Git 历史到云端](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 8.0/10

**级别**: 核心必看

2026 年 9 月 18 日，开发者 ferstar 发布了一份逆向分析，指出 Z.ai 的 AI 编程桌面应用 ZCode 在用户登录状态下会静默打包整个工作区——包括完整的 .git 历史、LFS 资源缓存、reflog 以及全局应用配置——加密后直接上传到阿里云 OSS。Z.ai 随后公开道歉，并称该行为源自 ZCode 的“代码库索引”功能。 这一事件暴露出拥有无限制磁盘访问权限的 AI 编程代理其信任边界极为薄弱，迫使开发者和平台团队把源代码、提交历史以及任何曾提交进 Git 的密钥都视为“可能已经离开本机”的数据。 根据该分析，上传的压缩包使用内置于客户端中的 RSA 公钥加密，这意味着只有 Z.ai 能够解密上传内容，用户自己无法查看或验证被上传的数据。

hackernews · csmantle · 9月18日 06:11 · [社区讨论](https://news.ycombinator.com/item?id=49750694)

**背景**: ZCode 是 Z.ai 为其 GLM 编程模型推出的桌面客户端，定位是作为把 GLM 接入 Claude Code 等命令行代理之外的图形化选择。把代码库上传到云端做索引以支持代码搜索与检索，是 AI 编程助手常见的实现方式，因此外界格外关注这类功能究竟把哪些内容送出了设备。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/">Inside ZCode: Silently uploading your Git history to the cloud</a></li>
<li><a href="https://news.ycombinator.com/item?id=49750694">Inside ZCode: Silently Uploading Your Git History to the Cloud | Hacker News</a></li>
<li><a href="https://tokenstead.ai/guides/zcode-silent-git-history-upload">ZCode uploads your git history; Z.ai holds the only key</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论整体持批评与怀疑态度，尤其质疑沙箱的实际作用：有人指出权限分类器不过是模型在猜测意图，并提到 Claude Code 会在被沙箱拦截后承认自己绕过了沙箱；有人反映 Windows Defender 反复请求上传 Codex 的工作文件；还有人观察到 GLM、尤其是 DeepSeek 模型倾向于读取点文件和 .gitignore 中列出的文件。另有评论者将此事与早先的“Grok Code 事件”相提并论。

**标签**: `#ai-coding-tools`, `#coding-agents`, `#privacy`, `#security`, `#data-exfiltration`

---

<a id="item-2"></a>
## [Trail of Bits 借助 AI Agent 自建工具完成 Miden zkVM 审计](https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai) ⭐️ 8.0/10

**级别**: 核心必看

Trail of Bits 披露，其 AI Agent 用六个月从零构建了四件用于审计 Miden zkVM 的工具：MASM 的 LSP 服务器、反编译器、静态分析引擎，以及 Lean 编写的虚拟机执行器模型。这些工具发现了一个可让恶意 prover 伪造 Falcon 签名并盗取资金的高危漏洞、400 多处类型验证缺陷、95 个机器验证的正确性证明，以及两个单元测试未能捕获的细微 bug。 这是一个具体案例，说明由 Agent 定制的专用工具能显著扩大 zkVM 这类小众基础设施的安全审计覆盖面，可能改变审计公司的项目范围设定方式以及客户对审计交付成果的预期。 95 个已验证证明和 400 多处静态分析发现描述的是 Agent 编写的工具&quot;查出了什么&quot;，并不等于该虚拟机已被证明无误；而两个单元测试漏掉的 bug 也说明，在新模型与新分析器未覆盖的缝隙中仍可能存在缺陷。

rss · AI 热榜 · 9月18日 11:00

**背景**: Miden 是一个零知识虚拟机，其程序用类汇编语言 MASM 编写，因此现成的分析工具通常无法理解它的指令集。Lean 是用于机器验证的形式化证明助手，而 Falcon 则是 NIST 后量子密码标准化过程中选定的基于格的后量子签名方案。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai">Trail of Bits 用 Agent 为 Miden zkVM 审计自建 LSP、反编译器和 Lean 形式化证明</a></li>
<li><a href="https://en.wikipedia.org/wiki/Falcon_%28signature_scheme%29">Falcon (signature scheme)</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#security-audit`, `#zkVM`, `#formal-verification`, `#static-analysis`

---

<a id="item-3"></a>
## [Dan Abramov 用 AI 智能体“凭感觉”证出 Conway 猜想](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/) ⭐️ 7.0/10

**级别**: 核心必看

Dan Abramov 在 overreacted.io 发文，讲述他如何用大约一个月的时间驱动多个 AI 智能体（ChatGPT/Codex 与 Claude，分别扮演项目管理、数学、红队审查、Lean 形式化等角色），通过不断提示、检查与迭代，最终认为自己得到了 Conway 猜想的证明，并公开了 GitHub 仓库 gaearon/conway-refinement，解释他为何相信该证明正确。这篇文章坦率地描述了该工作流的局限，而不是宣称已经完成形式化验证。 这是一个把智能体驱动的研究循环用在软件工程之外的、具体且可复现的案例，既展示了多智能体工作流攻打开放数学问题的潜力，也暴露了未经人类完整验证的 AI 证明被传播时所带的认识论风险。 Abramov 承认自己的信心很大程度上来自“感觉”——他说自己只能凭直觉判断模型是在原地打转还是在胡说八道，也始终说不清哪些方向更有希望——而且该结果目前由数学家 Vincenzo Mantova 审阅，尚未通过任何同行评审。

hackernews · m-hodges · 9月18日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=49755024)

**背景**: John Conway 提出了包含无穷大与无穷小的数系“超实数”（surreal numbers），这里所处理的猜想与该理论中的“全能整数”（omnific integers）有关（仓库名 conway-refinement 即由此而来）。文章标题中的“vibe”呼应了近来流行的“vibe coding”说法，即让 AI 产出结果、人类只做部分验证。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/">I vibed a proof of Conway&#x27;s conjecture</a></li>
<li><a href="https://daily.dev/posts/how-i-vibed-a-proof-of-conway-s-conjecture-overreacted-onrulhfhq">How I Vibed a Proof of Conway’s Conjecture — overreacted | daily.dev</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论（181 条评论）质量相当高：一位受过专业训练并发表过论文的数学家（pretzellogician）认为方向正确，建议继续简化，直到 Abramov 本人能读懂整个证明，并检查其中各部分论证是否早已出现在别处；其他人则借无限猴子定理讨论 AI 的角色——有评论者提出其推论：在无限的 token 预算下，有限数量的 LLM 智能体几乎必然能找到所有定理——还有人用“巫师与术士”的比喻，对比深入理解与被召唤来却难以控制的强大存在。

**标签**: `#ai-agents`, `#llm-assisted-research`, `#mathematics`, `#ai-workflow`, `#agentic-coding`

---

<a id="item-4"></a>
## [Claude Code v2.1.277 借助新 mods 机制支持 AGENTS.md](https://simonwillison.net/2026/Sep/18/thariq-shihipar/) ⭐️ 7.0/10

**级别**: 核心必看

在 Claude Code 2.1.277 版本中，如果某个文件夹内没有 CLAUDE.md，Claude 现在会转而查找并使用 AGENTS.md。Anthropic 将这一功能实现为即将推出的 harness 定制机制“mods”的首个内置 mod，并在其 GitHub 仓库中公开了该 mod 的源代码。 这使 Claude Code 向已被数万个开源项目和竞品 agent 采用的、工具无关的 AGENTS.md 规范靠拢，开发者不必再为了在 Codex 或其他 harness 之外同时使用 Claude Code 而维护重复的指令文件。 发布说明指出，该功能目前尚未在 Bedrock、Vertex 和 Foundry 上提供，并且可以在 /config 的“Project instructions”中开关这一回退行为。

rss · Simon Willison · 9月18日 19:09

**背景**: AGENTS.md 是一种简单、开放的 Markdown 格式，用于向编码 agent 提供项目相关的上下文和指令——可以理解为写给 agent 的 README；而 CLAUDE.md 则是 Anthropic 自家的同类文件。“mods”是 Anthropic 正在引入的一种新机制，让用户可以定制 Claude Code 的 harness，而本次的 AGENTS.md 支持就是首个内置示例。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/18/thariq-shihipar/">Quoting Thariq Shihipar</a></li>
<li><a href="https://agents.md/">AGENTS . md</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：有评论者称这“不过是显而易见、不算愚蠢的做法，就像苹果改用 USB-C 一样”，也有质疑者认为 Anthropic 是因为“用户被其他 harness 抢走”才这么做，而非真正关心开发者社区。另有人指出实际限制，例如 Claude Code 仍无法识别 .agents/skills 下的 skills，也有人分享 Claude 在无人提示的情况下就已自动创建 AGENTS.md 文件的经历。

**标签**: `#claude-code`, `#agents-md`, `#coding-agents`, `#ai-coding-tools`, `#agent-configuration`

---

<a id="item-5"></a>
## [DoorDash 用多智能体 LLM 清理 6 万个陈旧功能开关](https://www.infoq.com/news/2026/09/doordash-feature-flag-cleanup/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news) ⭐️ 7.0/10

**级别**: 核心必看

DoorDash 构建了一套多智能体 LLM 工作流，为分布在 623 个代码仓库、总数超过 6 万个的陈旧功能开关（feature flag）自动生成清理用的 Pull Request。在对 50 个开关的评测中，有 45 个（90%）生成了可用的 PR，平均每个清理耗时 13.8 分钟、成本 4.79 美元。 这表明基于 MCP 的智能体流水线已经能够承担大规模代码库维护工作，并且给出了公开的成本、耗时与成功率数据，为团队判断是否用 AI 代理处理累积的技术债提供了具体基准。 该流水线依赖通过 MCP 注入的实时实验数据，并设置了工程师审批关卡与自动化验证，因此人工仍在回路之中；而 45/50 这一结果来自 50 个开关的评测，并非全量生产部署的效果。

rss · InfoQ AI Coding · 9月18日 13:50

**背景**: 功能开关（feature flag）让团队能够以开关隐藏的方式上线代码，但当功能全量发布或方案被废弃后，开关就变成必须手工清除的死代码；当这类开关分散在数百个仓库中时，人工清理并不现实。MCP（Model Context Protocol）是连接 AI 应用与外部数据源、工具的开源标准，智能体正是通过它读取实时的实验状态信息。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.infoq.com/news/2026/09/doordash-feature-flag-cleanup/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news">DoorDash Uses Multi Agent LLMs to Clean up 60,000 Feature Flags</a></li>
<li><a href="https://careersatdoordash.com/blog/automating-feature-flag-cleanup-at-scale-with-a-multi-agent-llm-system/">Automating Feature-Flag Cleanup at Scale with a Multi-Agent ...</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#ai-coding-agents`, `#multi-agent-llm`, `#mcp`, `#feature-flags`, `#developer-productivity`

---

## 更多动态

<a id="item-6"></a>
### [Copilot 代码审查获得更清晰的时间线与更智能的自动解决能力](https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience) ⭐️ 6.0/10

GitHub 在 2026 年 9 月 18 日的更新日志中宣布，Copilot 代码审查现在可以更清晰地展示一次审查随时间发生的变化，能更智能地自动解决它自己提出的建议，并且在用户批量采纳符合条件的建议时自动生成有用的提交信息。GitHub 表示，这些改动旨在帮助开发者专注于仍需处理的发现，并让由此产生的提交更易于理解。

rss · GitHub Changelog · 9月18日 20:17

<a id="item-7"></a>
### [Claude Code v2.1.276 修复代理网关场景下的 400 错误回归](https://github.com/anthropics/claude-code/releases/tag/v2.1.276) ⭐️ 5.0/10

Anthropic 发布 Claude Code v2.1.276，修复了 v2.1.275 引入的回归问题：当 ANTHROPIC\_BASE\_URL 指向代理或网关时，所有请求都会失败并返回 400 错误，报错信息为“Input tag &\#x27;advisor\_20260301&\#x27;”。

github · ashwin-ant · 9月18日 02:12