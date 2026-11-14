---
layout: default
title: "Horizon 每日速递：2026-11-14"
description: "AI 精选的技术与研究日报"
date: 2026-11-14
lang: zh
locale: zh-CN
---

> 从 64 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [browser-use 1.0.4 优化截图缓存与浏览器隔离](#item-tech-news-1) ⭐️ 8.0/10
2. [Cloudflare 将 Kitesurf 浏览器引擎开源](#item-tech-news-2) ⭐️ 7.0/10
3. [Claude Code 用退出码 2 实现失败自动重试](#item-tech-news-3) ⭐️ 7.0/10
4. [Sierra 发布 Poppy v1.0 协议](#item-tech-news-4) ⭐️ 7.0/10
5. [Claude for Manufacturing 接入三款制造与业务系统](#item-tech-news-5) ⭐️ 6.0/10
6. [腾讯混元发布 Hy Realtime 实时语音模型](#item-tech-news-6) ⭐️ 6.0/10
7. [谷歌称编码小模型 Token 用量降 24%](#item-tech-news-7) ⭐️ 4.0/10
8. [ChatGPT Wallet 向美国 Pro 用户开放 dot 代购](#item-tech-news-8) ⭐️ 4.0/10
9. [llama.cpp 发布 v1.0.0 稳定大版本](#item-tech-news-9) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [browser-use 1.0.4 优化截图缓存与浏览器隔离](https://github.com/browser-use/browser-use/releases/tag/1.0.4) ⭐️ 8.0/10

**级别**: 核心必看

browser-use 1.0.4 已发布，可通过 \`pip install &\#x27;browser-use==1.0.4&\#x27;\` 安装。该版本将旧截图清理改为每累计 20 条工具结果后批量执行，避免原先每出现一张新截图就重写早期消息、导致模型提供方的 prompt cache 失效；当 Chrome 无法使用时，设置 \`BU\_NAME\` 的调用方会获得独立的 Chromium，CLI 和 MCP 在浏览器初始化错误可能由新版修复时也会提示代理升级。项目方称，在包含 200 项任务的 BU Bench v2.1 中，1.0.4 相比 1.0.3 的得分基本持平（76.1 对 76.0），单任务模型成本从 0.434 美元降至 0.208 美元；该数据来自项目方基准，并非独立测量。

github · gregpr07 · 11月13日 20:50

**「此前的缓存失效问题」** 此前的 1.0.3 会在每次新截图出现时删除旧截图，而每次清理都会改写更早的消息，破坏模型提供方对既有上下文的缓存复用。项目方给出的一个 705 步任务共读取 27.8M 个输入令牌，其中仅 1.6M 个来自缓存，反映出截图密集型任务会反复承担未缓存输入的成本。

**「对部署与升级的影响」** 使用 \`BU\_NAME\` 的部署在 Chrome 不可用时会获得独立的 Chromium 实例，从而避开浏览器实例冲突；经 CLI 或 MCP 启动的部署若遇到可由新版解决的浏览器初始化错误，应按代理提示检查并升级版本，而不是在原配置上反复重试。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/browser-use/browser-use/releases/tag/1.0.4">browser-use/browser-use released 1.0.4</a></li>

</ul>
</details>

**标签**: `#browser-use`, `#AI agents`, `#MCP`, `#prompt caching`, `#developer tools`

---

<a id="item-tech-news-2"></a>
### [Cloudflare 将 Kitesurf 浏览器引擎开源](https://blog.cloudflare.com/kitesurf-open-source/) ⭐️ 7.0/10

**级别**: 核心必看

Cloudflare 已将面向 AI 智能体的实验性浏览器引擎 Kitesurf 开源，开发者现在可以查看代码、在本地运行，或在 Cloudflare Workers 上部署自己的实例。官方仍将 Kitesurf 定位为实验性项目，原始公告未说明许可证、依赖项、部署要求或生产环境适用性。

rss · Cloudflare AI · 11月13日 20:20

**「此前的技术基础」** Kitesurf 此前于今年早些时候被 Cloudflare 公布为一款面向 AI 智能体的无状态浏览器，此次开源兑现了当时开放代码的承诺。Cloudflare 官方说明其运行架构完全基于 Cloudflare Workers，源码采用 Apache 2.0 许可证。

**「提供本地运行与自部署路径」** 开发者获得了检查实现、本地运行以及通过 Cloudflare Workers 自建实例的具体选项，可以据此评估是否将 Kitesurf 用于代理浏览器基础设施；采用前仍需核实公告未涵盖的许可证、依赖和部署条件。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.cloudflare.com/kitesurf-open-source/">Kitesurf is now open source</a></li>
<li><a href="https://www.phoronix.com/news/Cloudflare-Kitesurf-Open-Source">Cloudflare Open Sources Kitesurf: Their Web Browser For AI ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser automation`, `#open source`, `#Cloudflare Workers`

---

<a id="item-tech-news-3"></a>
### [Claude Code 用退出码 2 实现失败自动重试](https://x.com/lydiahallie/status/2121313048820617645) ⭐️ 7.0/10

**级别**: 核心必看

Lydia Hallie 分享了一项 Claude Code 自动化技巧：在检查失败时，让 Stop hook 以退出码 2 退出，Claude 就会收到该 hook 的 stderr 并自动发起新一轮尝试。相比之下，退出码 1 是非阻塞错误，即使检查未通过，Claude 仍可能直接结束任务。

rss · AI 热榜 · 11月13日 18:43

**「Stop hook 的作用与重试保护」** Claude Code 的 Stop hook 是生命周期钩子，会在 Claude 准备结束当前回合时运行，可执行测试、代码检查和构建，并将未通过的结果反馈给代理。配置自动重试时还需检查 stop\_hook\_active 并设置重试次数上限，以免检查持续失败导致无限循环。

**「把失败检查变成质量门」** Claude Code 开发者可以把测试或代码检查接入 Stop hook，并以退出码 2 将失败作为阻断反馈，使代理在检查未通过时继续迭代，而不是以正常状态结束。实际配置时应把退出码 2 保留给需要阻断的失败，并设置明确的停止条件，避免持续失败导致反复重试。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/lydiahallie/status/2121313048820617645">Claude Code Stop hook 技巧：用 exit code 2 让 Claude 在检查失败时自动重试</a></li>
<li><a href="https://agentpromptsatoz.com/guides/done-gate/">Claude Code Stop Hook : Block a Fake &#x27;Done&#x27; Until Checks Pass...</a></li>
<li><a href="https://amitkoth.com/claude-code-stop-hooks/">How Claude Code stop hooks work - Amit Kothari</a></li>
<li><a href="https://en.aobaworks.com/claude-code-stop-hook-block-early-exit-without-loops/">Claude Code Stop Hook : Block Early Exit Without Loops</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>
<li><a href="https://code.claude.com/docs/en/hooks-guide">Automate actions with hooks - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding agents`, `#hooks`, `#AI engineering workflows`

---

<a id="item-tech-news-4"></a>
### [Sierra 发布 Poppy v1.0 协议](https://sierra.ai/blog/releasing-poppy) ⭐️ 7.0/10

**级别**: 核心必看

Sierra 宣布 Personal Agent Protocol（Poppy）v1.0 正式可用，面向需要让个人智能体代表用户接入企业智能体、网站和 API 的开发与企业部署场景。该协议基于 MCP、OpenAPI 和 UCP 等现有标准构建，并使用 OAuth 由客户控制访问权限；现有材料未提供更广泛生态兼容性或实际部署效果的验证数据。

rss · AI 热榜 · 11月13日 17:00

**「互操作与授权基础」** 个人智能体若要代表用户访问企业智能体、网站和 API，关键前提是统一调用方式并划定清晰的授权边界。Poppy v1.0 因此复用 MCP、OpenAPI、UCP 等既有规范，并通过 OAuth 让客户控制权限，定位在连接与授权层，而非提供新的模型或智能体运行时。

**「部署与兼容影响」** 开发者和 Shopify 商家现在可以围绕同一套 Poppy 规范接入个人智能体：Sierra 称该版本已面向所有使用 Meta Muse 的用户开放，并为每一家 Shopify 商家启用，Lorikeet 也已宣布支持该协议。实施方仍需兼容 MCP、OpenAPI、UCP 等调用路径，并使用客户可控的 OAuth 权限模型，在接入商户 API 或企业智能体时明确授权边界。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://sierra.ai/blog/releasing-poppy">Sierra 发布 Personal Agent Protocol（Poppy）v1.0</a></li>
<li><a href="https://www.lorikeetcx.ai/blog/personal-agent-protocol">Lorikeet supports the Personal Agent Protocol ( Poppy ) | Lorikeet</a></li>

</ul>
</details>

**标签**: `#agent interoperability`, `#MCP`, `#OpenAPI`, `#OAuth`, `#enterprise agents`

---

### 更多动态

<a id="item-tech-news-5"></a>
#### [Claude for Manufacturing 接入三款制造与业务系统](https://the-decoder.com/anthropics-claude-for-manufacturing-plugs-ai-directly-into-factory-software-to-automate-industrial-workflows/) ⭐️ 6.0/10

Anthropic 宣布 Claude for Manufacturing 插件，将 Claude 接入 Autodesk Fusion、Oracle NetSuite 和 Infor，并通过 17 项专用技能起草报价、比较供应商，以及在交付延迟时下达备选订单。相关动作均须人工批准；插件目前不能控制物理机器，Anthropic 正另行开发 Model Hardware Standard。报道未说明普遍可用时间、部署方式或实施范围，因此目前可确认的是厂商公布的集成与工作流能力，而非这些细节已全面落地。

rss · The Decoder · 11月13日 16:37

<a id="item-tech-news-6"></a>
#### [腾讯混元发布 Hy Realtime 实时语音模型](https://mp.weixin.qq.com/s/bFxAT04ohJs9hPcjjin3bg) ⭐️ 6.0/10

腾讯混元发布... 新增...。该模型已在元宝语音通话和腾讯客服上线；腾讯云 API 则仍计划于近期提供，公告尚未说明接口文档、工具协议、延迟、可靠性、价格或部署方式。

rss · AI 热榜 · 11月13日 08:32

<a id="item-tech-news-7"></a>
#### [谷歌称编码小模型 Token 用量降 24%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247943733&amp;idx=3&amp;sn=745bfc3f58406752d2d63db1306d234c) ⭐️ 4.0/10

据量子位报道，谷歌在 Carbon 发布后推出一款面向编码代理场景的小模型，称其速度提升 2.5 倍、代码能力提升 3 倍、幻觉率降至原来的五分之一，并能为旗舰模型节省 24% 的 Token 消耗。报道未提供模型名称、基准方法、样本范围、可用性、定价或兼容方式，也未说明结果是否来自厂商测试，因此这些指标仍待验证。

rss · 量子位 · 11月13日 02:54

<a id="item-tech-news-8"></a>
#### [ChatGPT Wallet 向美国 Pro 用户开放 dot 代购](https://x.com/ChatGPT/status/2121283151729496235) ⭐️ 4.0/10

ChatGPT 官方宣布推出 ChatGPT Wallet，面向美国的 Pro 订阅用户开放 dot 代为购买的能力，并称该功能自公告日起推出。官方称，dot 只有在用户批准后才能完成购买，执行支付时不会接触用户的实际卡号，而且每笔购买都必须通过安全检查。公告没有说明开发者 API、集成指南、配额、兼容性或工程实现。原文为 https://x.com/ChatGPT/status/2121283151729496235，官方详情页为 https://openai.com/index/introducing-chatgpt-wallet/。

rss · AI 热榜 · 11月13日 16:44

<a id="item-tech-news-9"></a>
#### [llama.cpp 发布 v1.0.0 稳定大版本](https://x.com/ClementDelangue/status/2121260104913768931) ⭐️ 4.0/10

Hugging Face CEO Clément Delangue 与 @ggerganov 宣布 llama.cpp v1.0.0 发布，这是该项目首个“完全稳定”的大版本，面向希望在手机、笔记本和工作站本地运行 AI 模型的用户。发布方宣称，用户可免费掌控本地智能、无需向任何人发送数据，并承诺支持所有硬件、平台和模型类型，让 AI 分布式运行而非集中于少数机构。当前条目未提供 v1.0.0 的变更日志、兼容性或迁移说明、性能数据及具体新增能力，因此“全支持”仍应视为公告承诺，无法据此判断实际覆盖范围或升级影响。

rss · AI 热榜 · 11月13日 15:13