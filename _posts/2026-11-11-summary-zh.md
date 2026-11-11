---
layout: default
title: "Horizon 每日速递：2026-11-11"
description: "AI 精选的技术与研究日报"
date: 2026-11-11
lang: zh
locale: zh-CN
---

> 从 84 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [browser-use 1.0.0 以持久 Python REPL 直连 CDP](#item-tech-news-1) ⭐️ 8.0/10
2. [AlphaProof Code 用 AI 代理验证软件实现](#item-tech-news-2) ⭐️ 8.0/10
3. [Modern Web Guidance 1.0：用原生 Web API 引导编码代理](#item-tech-news-3) ⭐️ 8.0/10
4. [Goose v1.59.0 新增延迟 MCP 与代理钩子](#item-tech-news-4) ⭐️ 7.0/10
5. [Meta 发布 Muse Ember 1.0，主打低成本代理任务](#item-tech-news-5) ⭐️ 7.0/10
6. [Gemini 4 Carbon 全面开放并预览 /swarm](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenRouter 正式并入 Stripe](#item-tech-news-7) ⭐️ 7.0/10
8. [ChatGPT Business 登录扩展至第三方工具](#item-tech-news-8) ⭐️ 7.0/10
9. [Lovable 引入发布前安全扫描与 Agent 修复](#item-tech-news-9) ⭐️ 7.0/10
10. [n8n Labs 发布 Nod 本地个人智能体研究预览版](#item-tech-news-10) ⭐️ 7.0/10
11. [Cursor Projects 新增多人协作](#item-tech-news-11) ⭐️ 7.0/10
12. [Glasswing 七个月漏洞实验暴露报告筛选难题](#item-tech-news-12) ⭐️ 6.0/10
13. [AI 生成代码库的脆弱性争议](#item-tech-news-13) ⭐️ 6.0/10
14. [Resend 谈面向编码代理的邮件 API 工具设计](#item-tech-news-14) ⭐️ 6.0/10
15. [NaiveAI 宣称每秒 2,100 Token 的编码表现](#item-tech-news-15) ⭐️ 6.0/10
16. [Sean Allen 谈软件正确性与供应链安全](#item-tech-news-16) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [browser-use 1.0.0 以持久 Python REPL 直连 CDP](https://github.com/browser-use/browser-use/releases/tag/1.0.0) ⭐️ 8.0/10

**级别**: 核心必看

browser-use 1.0.0 已发布，核心架构改为让代理在持久 Python REPL 中直接通过 Chrome DevTools Protocol（CDP）操作浏览器；项目方称此次重写删去 136,866 行代码，约占原代码库的 80%，并移除了 DOM 序列化器和动作 schema 中间层。默认配置也发生变化：未指定模型时使用 Browser Use 网关的 \`bu-fast\`，\`Browser\(\)\` 启动 Browser Use Cloud 浏览器，\`max\_steps\` 从 500 降至 100，\`timeout\` 设为 1700 秒；开发者可通过 \`uv add &\#x27;browser-use==1.0.0&\#x27;\` 安装，0.x 仍可用 \`pip install &\#x27;browser-use&lt;1&\#x27;\` 获取。项目方称，在相同模型下其得分最高提高 33 分、成本便宜 2.7–5.2 倍、速度快 2–3 倍，但这是自报结果；其列出的 BU Bench v2 测试条件为 60 个任务、每个任务重复 3 次、使用云浏览器，测试日期为 2026-11-09。

github · gregpr07 · 11月10日 02:04

**「代理执行模型」** 理解 1.0 的关键，是 Browser Use 的“代理步骤”本质上为可执行代码，而非调用一组预定义动作：官方文档说明，模型每一步写入一个 Python 单元格，在持久 REPL 中运行并读取输出，单元格可组合使用浏览器辅助函数或原始 CDP。这里的持久 REPL 会延续同一代理运行中的 Python 执行环境，因此 1.0 所取消的 DOM 序列化器和 action schema，本质上是被“模型生成 Python—直接执行—返回输出”这一接口取代的中间层。

**「升级者需要调整配置」** 从 0.x 升级的代码需要逐项核对 \`MIGRATING.md\`：\`Browser\(\)\` 从本地 Chromium 改为云浏览器，访问 localhost 或私有 IP 必须显式使用 \`Browser\(&\#x27;chromium&\#x27;\)\`；已删除的导入会抛出 \`ImportError\`，无法兑现的配置项则会在浏览器启动或计费前抛出 \`TypeError\`。建议先用 \`uv add &\#x27;browser-use==1.0.0&\#x27;\` 固定版本并测试自有模型、密钥和工作区配置，因为默认网关和云浏览器会改变依赖及成本口径；\`result.cost\_usd\` 包含模型和网页搜索费用，但不含云浏览器及其代理费用。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/browser-use/browser-use/releases/tag/1.0.0">browser-use/browser-use released 1.0.0</a></li>
<li><a href="https://docs.browser-use.com/open-source/agent">Agent - Browser Use</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser automation`, `#Chrome DevTools Protocol`, `#open-source tools`, `#developer workflows`

---

<a id="item-tech-news-2"></a>
### [AlphaProof Code 用 AI 代理验证软件实现](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

**级别**: 核心必看

Google DeepMind 宣布 AlphaProof Code，这是一种将 AI 证明代理用于现有软件实现形式化验证的编程代理式系统。据项目介绍，它会围绕代码库迭代，并为实现生成 Lean 或 Rocq 证明，使正确性论证能够由机器检查。所给信息未说明可验证范围、公开可用时间、基准表现或实际发现的缺陷数量，因此尚不能据此判断其是否能可靠验证完整软件。

hackernews · ilreb · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「形式化验证的证明边界」** Lean 与 Rocq 的机器检查机制验证的是已明确陈述、并与实现建立逻辑对应关系的定理；形式化证明通过并不自动说明规格完整，也没有把针对真实需求的安全审计自动化。AlphaProof Code 所称验证 Signal，重点是发布实现中的核心加密保护乃至机器指令层的选定保证，而非证明整个客户端或协议不存在任何缺陷。

**「评估时需明确证明边界」** 对采用 Lean 或 Rocq 的开发团队，AlphaProof Code 提供了一个由代理辅助生成实现证明的候选流程；实际评估时应限定规格、待证明属性和依赖范围，并审查生成的定理，因为证明通过并不代表覆盖了完整需求或排除了所有缺陷。

**「评论者质疑证明范围与完整性」** 评论者质疑所谓“零缺陷”是否源于证明范围过窄或定理本身有误；另有观点认为，该系统主要验证实现而不挑战规格，因此与经典迭代式编程代理的差异尚不清楚。一名用户还称代理曾在重构后给出全绿测试，却把实现方向做反，凸显测试通过与完整正确性之间的差距。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-alphaproof-code/">AlphaProof Code</a></li>
<li><a href="https://codingislove.com/alphaproof-code-signal/">DeepMind&#x27;s AlphaProof Code formally verifies Signal&#x27;s ...</a></li>
<li><a href="https://aiweekly.co/alerts/google-deepminds-alphaproof-code-formally-verifies-signal-protocol-guarantees">Google DeepMind&#x27;s AlphaProof Code Formally Verifies Signal ...</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#formal-verification`, `#theorem-proving`, `#software-correctness`, `#Lean`

---

<a id="item-tech-news-3"></a>
### [Modern Web Guidance 1.0：用原生 Web API 引导编码代理](https://github.com/GoogleChrome/modern-web-guidance) ⭐️ 8.0/10

**级别**: 核心必看

Chrome 团队联合 Firefox、MDN 与 Edge 发布开源的 Modern Web Guidance 1.0，包含 200 多篇由 Web 专家编写的实施指南，并以可安装的代理技能和 Agentic RAG CLI 提供给编码代理，用于纠正其默认采用旧式 \`&lt;div&gt;\` 加 JavaScript 模式的倾向。项目方称，在使用 Codex、Claude 和 agy 完成的 200 项任务评测中，代理未使用该技能时通过率为 55%，使用后为 92%，测试共包含约 1,700 项基于 Playwright/AST 的断言。CLI 提供 \`search\` 与 \`legacy-scan\`：项目方称整个纯 JavaScript 包约 7 MB、本地 CPU 搜索约 10 毫秒，其中 \`legacy-scan\` 以 30,000 个 GitHub 仓库训练，在留出仓库上达到 92% 的平均精确率。开发者可运行 \`DISABLE\_TELEMETRY=1 npx modern-web-guidance@latest install\` 安装，并通过 \`search\` 和 \`legacy-scan\` 子命令检索指南或扫描旧式实现。

hackernews · paulirish · 11月10日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50443812)

**「解决的问题」** 该项目针对一个具体缺口：模型可能知道现代浏览器 API 的名称，却仍选择既有的 \`&lt;div&gt;\` 加 JavaScript 实现。CSS.highlights 可在没有大量 \`&lt;span&gt;\` 的情况下高亮文本范围，\`&lt;dialog&gt;\` 与 \`showModal\(\)\` 可提供原生遮罩和焦点管理，\`field-sizing\` 则能随输入自动增高 textarea；这些能力过去往往需要约 50 行 JavaScript 或一个依赖。

**「代码现代化的落地方式」** 开发者可在合并代理生成的重构前，对 \`./src\` 运行 \`npx modern-web-guidance@latest legacy-scan\` 定位旧式实现，再通过 \`search\` 取得对应指南并审核替换方案。对于代理建议的新 API，仍应按项目的目标浏览器逐项查询支持表（如 Can I Use）并准备兼容路径，因为项目方的 92% 受控评测通过率并不能证明所有推荐特性都具备跨浏览器兼容性。

**「兼容性顾虑」** 评论者 \[surround\] 提醒，指南涉及的一些特性虽已在 Chrome 稳定，却尚未被 Firefox 和 Safari 支持，代理生成代码后仍需按目标浏览器核验兼容性；simonw 还建议发布可搜索的 Markdown 索引，让用户无需安装即可访问内容。\[advisedwang\] 则以 Chrome 在 Web 标准中的影响力为由，担忧让 LLM 普遍采用该团队的指导会加剧浏览器生态失衡；这是评论者的观点，而非项目评测结论。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/GoogleChrome/modern-web-guidance">Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives</a></li>
<li><a href="https://caniuse.com/">Can I use... Support tables for HTML5, CSS3, etc</a></li>

</ul>
</details>

**标签**: `#coding agents`, `#AI-assisted development`, `#web development`, `#browser APIs`, `#developer tools`

---

<a id="item-tech-news-4"></a>
### [Goose v1.59.0 新增延迟 MCP 与代理钩子](https://github.com/aaif-goose/goose/releases/tag/v1.59.0) ⭐️ 7.0/10

**级别**: 核心必看

Goose v1.59.0 已发布，为使用编码代理和工具编排的开发者新增 ToolExecutionOperation 中的“Minimal deferred MCP tools”、goose-agent（GDK）的停止、审批和工具钩子操作，以及通过后续指令恢复已完成 subagent delegate 的能力。ACP 的 session/list 接口现在可按 client tags 过滤会话，live-voice 则支持配置每次启动时的语音指令，以及设置 GPT-Live endpoint、model 和 key。同一版本还修复了 HTTP\(S\) 文档根目录处理、会话关键词查询、数据库连接池初始化隔离、Databricks OAuth 令牌提前刷新和 Gemini thinking level 传递等问题。

github · github-actions\[bot\] · 11月10日 17:17

**「变更范围与限制」** 此次更新扩展了 Goose 现有的 MCP 工具调用、GDK 代理控制、ACP 会话管理、live-voice 和 subagent 委派工作流，而不是引入新的独立子系统。发布说明只列出功能、修复项和对应 PR，未说明延迟 MCP 工具的加载条件、GDK 钩子的触发语义、ACP client tags 的匹配规则或配置字段名。

**「开发者影响」** 升级到 v1.59.0 后，GDK 集成可使用停止、审批和工具钩子操作控制代理流程，ACP 客户端可按 client tags 筛选 session/list 结果，live-voice 用户也能按每次启动调整语音指令并指定 GPT-Live endpoint、model 和 key。由于发布说明未交代配置格式及向后兼容情况，升级前应查阅 \#13375、\#13360、\#13169 和 \#13173 等对应 PR，确认现有部署需要修改的配置。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/aaif-goose/goose/releases/tag/v1.59.0">aaif-goose/goose released v1.59.0</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#MCP`, `#agent-workflows`, `#open-source`

---

<a id="item-tech-news-5"></a>
### [Meta 发布 Muse Ember 1.0，主打低成本代理任务](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

**级别**: 核心必看

Meta 发布 Muse Ember 1.0，称其是公司最小、最高效的模型，面向代理反复执行的工具调用、编码子任务、路由、信息提取和长文档解析，并提供 minimal、low、medium、high、xhigh、max 六档推理强度。输入不超过 20 万 token 时，每百万输入 token 收费 0.10 美元、缓存输入 0.004 美元、输出 0.50 美元，其短提示输入和输出价格与 GPT-6 Luna、Claude Haiku 5.5 相同。超过 20 万 token 后，对应价格升至每百万输入 token 0.30 美元、缓存输入 0.012 美元、输出 1.50 美元；模型最高支持 100 万输入 token。Simon Willison 引用的 Artificial Analysis 图表显示，Muse Ember xhigh 和 max 的每项任务成本约为 0.12 美元和 0.14 美元，Intelligence Index 约为 34 和 36，均位于帕累托线上；Meta 据此宣称其处于效率前沿，但原文未提供代理子任务专项基准或实现指引。

rss · Simon Willison · 11月10日 07:28

**「Muse 系列的低价下探」** Meta 的 Muse 系列此前已有 Muse Wonder；Simon Willison 在同一项 SVG 渲染测试中发现两者质量相近，但 Wonder 的价格约为 Ember 的 40 倍。由此，Ember 是同一系列中更偏重成本效率的高频代理执行档位，而非 Muse 家族的单一顶级型号。

**「选型与成本影响」** 开发者和组织可以把 Muse Ember 作为重复性代理子任务的经济型候选，并根据自身任务评测选择推理强度，因为单看每 token 价格无法反映不同模型实际消耗的推理 token 差异。长上下文负载在超过 20 万输入 token 后需要按更高费率重算成本；报道缺少代理子任务专项基准和接入说明，因此不宜仅凭“效率前沿”直接替换现有模型。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Nov/10/muse-ember/">Introducing Our Smallest, Most Efficient Model: Muse Ember</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#coding models`, `#model pricing`, `#long context`, `#Meta AI`

---

<a id="item-tech-news-6"></a>
### [Gemini 4 Carbon 全面开放并预览 /swarm](https://the-decoder.com/gemini-4-carbon-arrives-just-in-time-to-feel-like-yesterdays-news-in-the-fastest-model-cycle-yet/) ⭐️ 7.0/10

**级别**: 核心必看

Google 在两周的测试阶段后让 Gemini 4 Carbon 正式全面可用，开发者现可通过 GitHub Copilot、Gemini API、Google AI Studio 和 Cursor 使用；Antigravity 渠道目前限 Google AI Ultra 订阅者。该模型面向复杂编码、代理式工作流和推理任务；Cursor 官方称其在高 effort 设置下以 60.4% 的得分位居 CursorBench 4.0 榜首，但现有来源未披露完整评测方法。Google 还在 Antigravity 预览了 /swarm 功能，可让多个子代理实时拆分并协调复杂任务。Gemini API 发布价为每百万输入 token 2 美元、每百万输出 token 10 美元，并计划于 12 月 1 日分别上调至 4 美元和 20 美元。

rss · The Decoder · 11月10日 18:19

**「发布背景」** Google 于 2026 年 10 月 28 日首次发布 Gemini 4 Carbon，当时仅向一小部分网络防御人员开放，重点展示网络安全和长时程任务能力。Google 的模型卡显示，Carbon 基于 Gemini 4 Argon 构建，在多语种和多模态内容安全方面优于 Argon，而不合理拒答与语气表现大致相当；此次广泛可用是在该模型限量测试阶段基础上的扩展。

**「开发者影响」** 编码代理用户可以立即在多个开发环境和 Gemini API 中试用 Gemini 4 Carbon，但成本敏感的工作流应按 12 月 1 日每百万输入/输出 token 从 2/10 美元升至 4/20 美元重新核算预算；Cursor 的 60.4% 高 effort 成绩也不能直接外推到其他工具，因为来源未提供评测方法或集成限制。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/gemini-4-carbon-arrives-just-in-time-to-feel-like-yesterdays-news-in-the-fastest-model-cycle-yet/">Gemini 4 Carbon arrives just in time to feel like yesterday&#x27;s news in the fastest model cycle yet</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/">Introducing Gemini 4 Carbon - The Keyword</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-4-carbon/">Gemini 4 Carbon - Model Card — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#Gemini 4 Carbon`, `#AI agents`, `#agent orchestration`, `#model release`, `#cost efficiency`

---

<a id="item-tech-news-7"></a>
### [OpenRouter 正式并入 Stripe](https://x.com/OpenRouter/status/2120234542183395787) ⭐️ 7.0/10

**级别**: 核心必看

OpenRouter 宣布正式并入 Stripe，成为 Stripe 旗下的一部分。OpenRouter 称，其平台的开发者与公司用户超过 1000 万，为多模型、多提供商的 AI 运行提供基础设施，包括访问新模型、在故障期间保持可用，以及执行团队支出和数据策略。公告没有披露交易条款、整合时间表、定价变化、API 或开源项目安排，因此尚不能确认这些能力及使用方式将如何改变。

rss · AI 热榜 · 11月10日 19:18

**「收购此前进展」** 此前，Stripe 与 OpenRouter 已于 2026 年 8 月 19 日确认达成收购协议，但未披露交易财务条款。本次“正式并入”的公告是在该交易基础上进一步明确合并后的归属与定位。

**「现有团队需等待整合说明」** 对依赖 OpenRouter 的现有团队，公告尚不足以判断 API、定价或开源项目会否变化。开发者应以后续官方整合与迁移说明为准，不宜仅凭此次并入公告调整现有集成。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/OpenRouter/status/2120234542183395787">Stripe 收购 OpenRouter，双方宣布合并后定位</a></li>
<li><a href="https://responserift.dev/blog/stripe-acquires-openrouter-ai-infrastructure-deal">Stripe Acquires OpenRouter in $8B AI Infrastructure Deal</a></li>

</ul>
</details>

**标签**: `#OpenRouter`, `#Stripe`, `#AI infrastructure`, `#model routing`, `#M&amp;amp;A`

---

<a id="item-tech-news-8"></a>
### [ChatGPT Business 登录扩展至第三方工具](https://x.com/OpenAIDevs/status/2120212596850663712) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 宣布，ChatGPT Business 用户现可通过“Sign in with ChatGPT”连接并开始使用 Notion、v0、ampcode、kilocode、Warp、NousResearch 的 Hermes、openclaw 和 opencode。该消息确认了 Business 计划的登录范围，但未提供各工具的具体集成实现、兼容性条件或迁移细节。

rss · AI 热榜 · 11月10日 17:50

**「第三方应用中的 ChatGPT 计划复用」** 此前，Vercel 已展示在 v0 中使用 ChatGPT Pro 500 的工作流，另有第三方目录专门收录可复用 ChatGPT 或 Claude 订阅的 AI 应用；这说明订阅权益与账户入口被带入第三方工具的做法并非此次才出现。此次公告的变化是把“Sign in with ChatGPT”的可用计划扩到 ChatGPT Business 并列出受支持工具，但没有说明底层授权协议、套餐细则或各工具的兼容条件。

**「Business 用量将计入现有额度」** 对 ChatGPT Business 团队而言，第三方工具中的使用量会计入该计划现有的 Codex/ChatGPT 工作额度，因此管理员扩大部署前应将这些用量纳入内部额度监控，而不能假定 Business 登录会提供独立额度。用户可通过“Sign in with ChatGPT”创建、关联或访问受支持外部应用的账户，组织则应逐项确认目标工具是否支持该登录方式。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/OpenAIDevs/status/2120212596850663712">OpenAI 开放 ChatGPT Business 计划登录 Notion、v0 等第三方工具</a></li>
<li><a href="https://vercel.com/i/chatgpt-pro-500-use-cases">5 practical ways to use ChatGPT Pro 500 - Vercel</a></li>
<li><a href="https://bringyoursubs.com/">AI apps that use your Claude or ChatGPT subscription</a></li>
<li><a href="https://aicoder.com/news/news-20261110-openai-sign-in-with-chatgpt-business-plan-notion-v0-amp-kilo-warp-hermes-opencode-admin-limits">OpenAI Lets ChatGPT Business Plans Power Notion, v0, Amp ...</a></li>
<li><a href="https://help.openai.com/en/articles/20001410-sign-in-with-chatgpt">Sign in with ChatGPT - OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#ChatGPT Business`, `#coding agents`, `#developer authentication`, `#third-party integrations`

---

<a id="item-tech-news-9"></a>
### [Lovable 引入发布前安全扫描与 Agent 修复](https://lovable.dev/blog/find-it-fix-it-ship-it) ⭐️ 7.0/10

**级别**: 核心必看

Lovable 为其应用构建平台加入发布前安全扫描和编码 Agent 修复机制，主要面向缺乏技术背景的开发者。平台默认提供安全登录、密钥加密和构建时扫描，所有账户（包括免费账户）均可使用；每次发布前会检查代码、应用逻辑、数据库 schema 和行级安全策略，用户可通过 Fix 或启用 Auto-fix 让 Agent 修复问题，其中最常见的问题是数据访问规则过于开放。该功能由 Lovable 自行介绍，源文未提供实现细节、误报率或修复成功率等效果数据。

rss · AI 热榜 · 11月10日 14:00

**「RLS 是自动修复的主要技术边界」** Lovable 的自动安全流程以 Supabase 数据库的行级安全（RLS）配置为关键检查对象；GuardLayer 此前讨论的 Lovable RLS 漏洞 CVE-2025-48757 即说明，访问规则缺口可能造成数据泄露。官方资料区分了发布时自动运行、约需 10–15 秒的基础扫描与按需启动、约需 3 分钟的深度扫描，而 Auto-fix 主要处理可安全自动修复且不会破坏应用的发现，包括常见 RLS 错误、数据库访问模式及存在已知漏洞的依赖项。

**「扫描通过不等于可以安全上线」** 自动扫描和 Agent 修复降低了发布前遗漏安全问题的风险，但不会消除上线风险；Lovable 官方文档明确说明内置扫描不能替代全面安全审查。团队仍应在发布前人工复核行级安全与授权规则、速率限制，以及客户端代码包是否泄露密钥，不能仅凭“扫描通过”判定应用安全。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://lovable.dev/blog/find-it-fix-it-ship-it">Lovable 介绍平台安全机制：自动扫描、一键修复与深度扫描功能</a></li>
<li><a href="https://lovable.dev/security">Security at Lovable | Build Apps Faster</a></li>
<li><a href="https://www.guardlayer.io/blog/lovable-rls-vulnerability-cve-2025-48757">Lovable RLS vulnerability (CVE-2025-48757) and the 2026 leaks</a></li>
<li><a href="https://docs.lovable.dev/features/privacy-and-security-settings">Privacy &amp; security settings - Lovable Documentation</a></li>
<li><a href="https://docs.lovable.dev/features/security">Security overview - Lovable Documentation</a></li>
<li><a href="https://vibeappscanner.com/community/lovable">Lovable Security : What People Actually Say (2026): CVE-2025-48757...</a></li>

</ul>
</details>

**标签**: `#AI 编码工具`, `#编码 agent`, `#应用安全`, `#安全扫描`, `#Lovable`

---

<a id="item-tech-news-10"></a>
### [n8n Labs 发布 Nod 本地个人智能体研究预览版](https://blog.n8n.io/meet-nod/) ⭐️ 7.0/10

**级别**: 核心必看

n8n Labs 发布了首个实验项目 Nod 的研究预览版。这是一款独立于 n8n 运行的开源个人智能体，支持 Mac 和 Windows，可在本机沙盒及浏览器中执行取消订阅、比价和酒店预订等任务，且无需 n8n 账号或云服务。官方尚未提供架构、安全边界、性能数据或基准测试，因此现有材料不足以判断其生产可靠性。

rss · AI 热榜 · 11月10日 12:52

**「产品定位」** Nod 是 n8n Labs 首次单独推出的实验项目，定位为可脱离 n8n 独立运行的开源个人智能体。“本地运行”在这一预览中特指任务由用户本机的沙盒和浏览器环境执行，而不是依赖 n8n 的云端服务。

**「评估与使用」** 开发者可在 Mac 或 Windows 上直接试用 Nod，且无需创建 n8n 账号或连接其云服务，适合评估本地浏览器代理方案。对于取消订阅和酒店预订等涉及真实操作的场景，使用前仍需自行验证权限控制、安全边界与稳定性。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.n8n.io/meet-nod/">n8n Labs 发布本机个人智能体 Nod 研究预览版</a></li>

</ul>
</details>

**标签**: `#个人智能体`, `#本地 AI`, `#浏览器自动化`, `#开源智能体`, `#n8n`

---

<a id="item-tech-news-11"></a>
### [Cursor Projects 新增多人协作](https://cursor.com/blog/projects-multiplayer) ⭐️ 7.0/10

**级别**: 核心必看

Cursor 官方宣布，AI 编程产品 Projects 现已支持多名团队成员加入同一个项目，成员可分别与各自的智能体共同完成规划、构建和交付。此次更新将 9 月推出时由单一协调者调度一组智能体的模式，扩展为多人各自携带智能体参与的协作模式。

rss · AI 热榜 · 11月10日 12:00

**「前序协作模式」** Cursor 于 9 月推出的 Projects 最初采用单一协调者调度一组智能体的结构。此次“多人协作”扩展的是项目层面的参与方式：团队成员可分别调用自己的智能体加入同一个 Project，而不是由多名成员共同驱动同一个智能体。

**「项目协作转向成员共同参与」** 对使用 Cursor 的团队而言，协作可以直接围绕同一个 Project 展开：不同成员各自调用智能体，并以共同的规划和交付过程衔接工作，而不再局限于单一协调者统一调度。官方来源未说明套餐门槛、权限模型或访问范围，团队采用前需确认这些条件。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://cursor.com/blog/projects-multiplayer">Cursor Projects 升级为多人协作模式</a></li>

</ul>
</details>

**标签**: `#AI 编程`, `#智能体协作`, `#团队工作流`, `#Cursor`

---

### 更多动态

<a id="item-tech-news-12"></a>
#### [Glasswing 七个月漏洞实验暴露报告筛选难题](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) ⭐️ 6.0/10

Glasswing 结束为期七个月的漏洞发现实验后，据报道向维护者提交了 37,966 条发现；其中只有 7,349 条（19.4%）已公开，且仅 217 条被标记为已修复。原始报告量与公开、修复结果之间的巨大落差，使这项实验更像是对代理输出噪声、人工复核和披露流程的压力测试，而非可直接采用的大规模漏洞清单。重复、撤回以及仍在保密期内的报告也意味着，仅统计公开案例会形成明显的样本偏差。

hackernews · panic · 11月10日 22:17 · [社区讨论](https://news.ycombinator.com/item?id=50447074)

<a id="item-tech-news-13"></a>
#### [AI 生成代码库的脆弱性争议](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/) ⭐️ 6.0/10

这篇文章主张，AI 参与生成的代码库可能因浅层测试、过度设计、命名不清、架构复杂和人类理解度下降而更容易变得脆弱，主要影响需要长期维护 AI 辅助项目的开发团队。文章讨论用确定性的可维护性门禁和更简单的提示词来控制这些风险，但现有材料没有给出已实现的流程、测量数据或经验证的效果，因此其方案仍主要是概念性建议，不能视为已被证明的通用工作流。

hackernews · plun9 · 11月10日 10:25 · [社区讨论](https://news.ycombinator.com/item?id=50438318)

<a id="item-tech-news-14"></a>
#### [Resend 谈面向编码代理的邮件 API 工具设计](https://latent.space/p/resend/) ⭐️ 6.0/10

Resend 的 Zeno Rocha 在此次访谈中介绍其面向编码代理的设计思路：让 Claude Code 等代理能够从文档中发现并选择合适的邮件 API，再通过工具实际发送邮件。他以 Resend 的文档和邮件发送工具为具体案例，探讨“答案引擎优化”（AEO）与“代理体验”（agent experience）之间的边界。该内容属于工程实践讨论，来源未披露新的 API、协议版本、性能数据或已上线的功能。

rss · Latent Space · 11月10日 20:05

<a id="item-tech-news-15"></a>
#### [NaiveAI 宣称每秒 2,100 Token 的编码表现](https://latent.space/p/naiveai/) ⭐️ 6.0/10

NaiveAI 被宣称可达到每秒 2,100 个 token，Latent Space 认为它可能在 Artificial Analysis 的速度排名中位居领先。其上手测试认为 NaiveAI 的编码质量可与 DeepSeek 相比，但现有材料没有给出测试方法、任务集或逐项结果。由于该吞吐数字尚未由文中所示的独立评测确认，它目前属于速度宣称，而非已核实的生产性能。

rss · Latent Space · 11月10日 18:56

<a id="item-tech-news-16"></a>
#### [Sean Allen 谈软件正确性与供应链安全](https://newsletter.pragmaticengineer.com/p/software-correctness) ⭐️ 4.0/10

《Pragmatic Engineer》于 2026 年 11 月 10 日发布了一段与 Sean Allen 的深度对话，主题是软件开发中的软件正确性与供应链安全，主要面向使用 AI 辅助开发的开发者。节目预告称，对话试图一次也不提“AI”，以转向在这个背景下依然关键的基础工程原则。当前条目仅提供节目介绍和链接，未包含具体工作流、实现细节、实测结果或可立即采用的建议。

rss · The Pragmatic Engineer · 11月10日 15:00