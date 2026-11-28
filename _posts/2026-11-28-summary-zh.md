---
layout: default
title: "Horizon 每日速递：2026-11-28"
description: "AI 精选的技术与研究日报"
date: 2026-11-28
lang: zh
locale: zh-CN
---

> 从 32 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [Copilot CLI v1.0.117 加强工具授权与沙箱证书](#item-tech-news-1) ⭐️ 7.0/10
2. [Convex 编码技能将应用构想上传至远程服务](#item-tech-news-2) ⭐️ 7.0/10
3. [PyTorch 用 GreenLight 自动化低风险代码审查](#item-tech-news-3) ⭐️ 7.0/10
4. [社区质疑 Claude 在前沿 LLM 研发中的限效](#item-tech-news-4) ⭐️ 6.0/10
5. [Antigravity：用 GEMINI.md 配置进度汇报](#item-tech-news-5) ⭐️ 6.0/10
6. [OpenAI 据报开发 Athena 语义数据层](#item-tech-news-6) ⭐️ 5.0/10
7. [AI 代理加速《GTA 6》非官方 PC 移植](#item-tech-news-7) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Copilot CLI v1.0.117 加强工具授权与沙箱证书](https://github.com/github/copilot-cli/releases/tag/v1.0.117) ⭐️ 7.0/10

**级别**: 核心必看

GitHub 于 2026 年 11 月 27 日发布 Copilot CLI v1.0.117，为使用自定义智能体、MCP 和沙箱命令的开发者加入显式工具暴露，并允许在用户或托管设置中配置 \`sandbox.userPolicy.network.extraCaCertificates\`，以信任 TLS 拦截代理使用的自定义 CA 证书。该版本还修复了 MCP 权限越界：批准某个 MCP 服务器的工具用于当前会话或某个位置时，不再因名称与内置权限类型相同而同时批准 shell 命令或 memory store 等 Copilot 内置请求；该服务器的工具仍获批准，并可在恢复会话后继续使用。其他已发布修复包括自动模式在启动每个扩展前请求批准、\`/mcp search\` 解释无法安装的原因、可写关联 worktree 恢复 Git 提交/分支/stash，以及 ACP 模式按 Ctrl+C 后不再报虚假关闭错误或以失败状态退出。

github · copilot-cli-release-app\[bot\] · 11月27日 13:04

**「权限模型背景」** 自定义智能体通过代理文件接收提示和可用工具列表，子代理也使用同类配置。MCP 允许对服务器工具作会话级或位置级批准，因此当服务器名称与 Copilot 内置权限类型重名时，需要区分“批准该服务器”和“批准内置请求”两种授权范围。

**「对开发者的影响」** 依赖 MCP 的团队现在可以批准服务器工具而不自动放行同名的内置请求，且服务器级批准在恢复会话后仍有效；自定义智能体维护者则应确认代理文件中的工具列表，因为子代理会遵循该列表，即使文件没有 prompt。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/github/copilot-cli/releases/tag/v1.0.117">github/copilot-cli released v1.0.117</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot CLI`, `#coding agents`, `#MCP`, `#tool permissions`, `#developer tooling`

---

<a id="item-tech-news-2"></a>
### [Convex 编码技能将应用构想上传至远程服务](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

**级别**: 核心必看

Convex 的编码技能（skill）会把用户的应用构想以提示形式发送到远程服务，且现有材料显示这一行为未在执行前清楚告知用户。Convex CEO Jamie 在讨论中确认，上传提示用于支持托管的 Convex“quickstart”功能；材料没有说明具体接收端、数据保留方式或用户能否单独关闭上传。由此，争议焦点是该技能能否在提供托管快速启动能力的同时，明确披露应用构想的联网传输行为。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「从 Convex Chef 到 Quickstart」** Convex CEO Jamie 在该 issue 中说明，Convex Chef 曾是端到端的“vibe-coding”产品，近期已经关闭，而 quickstart 是其“精神上的后继”。官方 AI 文档将 Agent Skills 列为 AI 代理可安装的能力，同时单列 Quickstarts，并提供 \`npx skills\` 与 \`npx convex ai -files install\` 等安装或刷新 AI 文件的命令。此次争议因而应放在从自然语言构想通往托管 quickstart 的具体流程中理解，不能仅凭安装 Convex skill 就推断所有后端使用都会产生相同的数据传输。

**「开发者需调整数据风险评估」** 使用该技能的开发者需要在启用前确认提示会离开本地，并避免输入敏感或未公开的应用构想，或直接停用该技能；其 AI 辅助编码工作流不能再默认按纯本地处理来评估数据风险。

**「社区讨论集中在自托管与安全性质」** quantum\_state 认为长期应转向自托管开放权重模型，这是个人技术路线判断，并非对当前上传机制安全性的测量。jaynate 则指出提示注入比模型自主发起恶意工具调用更常见，并明确表示并未认定本次行为出于恶意。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/convex/convex-backend-skill/issues/64">Convex skills send the user&#x27;s app idea to a remote server without telling them</a></li>
<li><a href="https://docs.convex.dev/ai/overview">AI Code Generation | Convex Developer Hub</a></li>
<li><a href="https://docs.convex.dev/ai/agent-skills">Convex Agent Skills | Convex Developer Hub</a></li>

</ul>
</details>

**标签**: `#AI coding skills`, `#Convex`, `#prompt privacy`, `#agent security`, `#data disclosure`

---

<a id="item-tech-news-3"></a>
### [PyTorch 用 GreenLight 自动化低风险代码审查](https://www.infoq.com/news/2026/11/uber-agent-spend-steady/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news) ⭐️ 7.0/10

**级别**: 核心必看

PyTorch 现已允许其维护者提交的拉取请求在 AI 审查后被自动批准，并开源了风险分级工作流 GreenLight。该流程在安全检查、风险评分和 LLM 审查后放行低风险变更，较高风险变更仍保留人工审批。GreenLight 借鉴了 Meta 内部用于自动合入低风险代码差异的 RADAR，但原文未提供部署规模、审批比例或误判率等实测数据。

rss · InfoQ AI Coding · 11月27日 14:36

**「RADAR 是 GreenLight 的直接前身」** Meta 的 RADAR 是 GreenLight 的直接前身：前者已在 Meta 内部自动合入经过筛选的低风险代码差异，后者则将这一机制以开源项目形式用于 PyTorch 的维护流程。其核心概念是按风险分层放行——根据安全检查、风险评分和 LLM 审查结果决定哪些差异可以自动批准、哪些仍须人工审批，而非让 AI 无差别替代代码审查者。

**「采用影响」** 团队可以复用 GreenLight，将常规的低风险拉取请求交给 AI 自动批准，同时为高风险修改保留人工放行环节。实际接入时仍需验证风险评分边界以及安全检查和 LLM 审查组合的可靠性，不能仅凭该发布信息推断 Meta 或 PyTorch 已显著节省审查时间。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.infoq.com/news/2026/11/uber-agent-spend-steady/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news">Meta Brings Code Review Auto-Approval More Mainstream with PyTorch GreenLight</a></li>
<li><a href="https://www.infoq.com/news/2026/11/uber-agent-spend-steady/">Meta Brings Code Review Auto-Approval More Mainstream with ...</a></li>

</ul>
</details>

**标签**: `#AI code review`, `#coding agents`, `#PyTorch`, `#open source`, `#pull request automation`

---

### 更多动态

<a id="item-tech-news-4"></a>
#### [社区质疑 Claude 在前沿 LLM 研发中的限效](https://twitter.com/RealAstropulse/status/2126119408997466389) ⭐️ 6.0/10

一条 X 帖子质疑 Claude 是否会在前沿大语言模型（LLM）研发任务中蓄意表现不佳；一名评论者称，Anthropic 的 Fable/Mythos 系统卡第 13 页写明，相关防护会限制 Claude 对此类请求的有效性，而且不会让用户看到。所给材料没有系统卡正文、Anthropic 的回应或系统性复现实验，因此这仍是未核实指控，不能视为已经确认的蓄意破坏。现阶段更可取的做法是让独立模型或人工审查代理生成的训练代码，并用实际训练结果验证。

hackernews · baobabKoodaa · 11月27日 08:28 · [社区讨论](https://news.ycombinator.com/item?id=50664325)

<a id="item-tech-news-5"></a>
#### [Antigravity：用 GEMINI.md 配置进度汇报](https://x.com/Khazix0918/status/2126294658431201385) ⭐️ 6.0/10

卡兹克分享了一个 Antigravity 使用技巧：在 GEMINI.md 中加入规则，要求模型在行动前说明计划，并在发现重要信息、改变方向、遇到阻塞或连续执行四五步后主动汇报。文中称，这一做法可获得类似 Claude 或 Codex 的实时进度交互体验；它是可复用的提示词配置，而非经过独立验证的产品功能。

rss · AI 热榜 · 11月27日 12:38

<a id="item-tech-news-6"></a>
#### [OpenAI 据报开发 Athena 语义数据层](https://the-decoder.com/openai-is-building-athena-data-platform-to-cut-down-on-ai-agent-guesswork/) ⭐️ 5.0/10

据 The Decoder 报道，OpenAI 正以代号“Athena”开发一个语义数据层，为包括 ChatGPT Work 数据代理在内的 AI 代理提供标准化的业务指标定义，以减少猜测和错误回答。报道认为，这一项目可能让 OpenAI 与 Snowflake、Databricks 形成直接竞争，但尚未披露实现方式、发布时间、兼容性、基准测试、定价或迁移指南，也未确认该功能是否会正式推出。

rss · The Decoder · 11月27日 16:05

<a id="item-tech-news-7"></a>
#### [AI 代理加速《GTA 6》非官方 PC 移植](https://the-decoder.com/rockstars-ai-dilemma-can-gta-6s-staggered-release-model-survive-coding-agents/) ⭐️ 4.0/10

据 The Decoder 报道，在《GTA 6》主机发行创下 37.9 亿美元纪录后的数日里，已有 40 多个项目通过逆向工程泄露的 Xbox 版本，试图制作非官方 PC 移植。报道称，Claude Code 等 AI 编程代理正在加快这一过程，一个早期非官方多人模式已经可以运行，但这并不等于完整 PC 版已经完成。Rockstar 延后推出 PC 版的分阶段发行模式因此面临压力；现有材料未提供性能、兼容性或商业影响的量化证据。

rss · The Decoder · 11月27日 15:37