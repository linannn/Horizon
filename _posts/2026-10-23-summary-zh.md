---
layout: default
title: "Horizon 每日速递：2026-10-23"
description: "AI 精选的技术与研究日报"
date: 2026-10-23
lang: zh
locale: zh-CN
---

> 从 69 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [Claude 各端会话默认启用 auto mode](#item-tech-news-1) ⭐️ 8.0/10
2. [Switch 2 越狱与 Codex 硬件控制工作流](#item-tech-news-2) ⭐️ 7.0/10
3. [Anthropic 将 Agent Skills 标准捐赠给 AAIF](#item-tech-news-3) ⭐️ 7.0/10
4. [Replit Monitoring Agent 支持自动修复与部署](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenAI 发布 Decisions API](#item-tech-news-5) ⭐️ 7.0/10
6. [Gemini CLI 夜间版加入容器 IDE 桥接](#item-tech-news-6) ⭐️ 6.0/10
7. [GitHub Copilot CLI v1.0.103 改进沙箱与会话恢复](#item-tech-news-7) ⭐️ 6.0/10
8. [Anthropic 发布常驻代理 Claude Duet](#item-tech-news-8) ⭐️ 6.0/10
9. [Vercel Labs 开源可嵌入的 Zig 编程代理 fx](#item-tech-news-9) ⭐️ 5.0/10
10. [Google 推出 Agent Compute Engine,为每个 Gemini 智能体配备硬件隔离微型虚拟机](#item-tech-news-10) ⭐️ 4.0/10
11. [MiniMax 开源 M3.1 Flash 模型权重](#item-tech-news-11) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude 各端会话默认启用 auto mode](https://x.com/claudeai/status/2113360845409583307) ⭐️ 8.0/10

**级别**: 核心必看

Claude 宣布，下周起，Pro、Max 和 Team 套餐在 Claude 网页、桌面及移动端应用中的会话将默认使用 auto mode，不再要求用户逐步批准操作，用户可随时切回手动模式。其引用的 Claude Code 更新称，auto mode 使用独立分类器审查 shell 命令；官方测试中，89% 的危险命令被拦截，14% 进入手动批准流程。

rss · AI 热榜 · 10月22日 20:04

**「背景」** Anthropic 于 2026 年 8 月 14 日已先在 Claude Code 中为 Pro、Max、Team 套餐默认开启 auto mode，由独立分类器审查 shell 命令、而非逐步请求用户批准；本次公告是将同一默认行为从 Claude Code 扩展到 Claude 网页、桌面和移动端的常规会话，属于同一审批机制覆盖面的扩大，而非审批逻辑的变化。

**「对现有审批流程的影响」** 受影响用户无需再为每一步操作确认授权，但高风险命令仍可能触发拦截或人工批准；依赖逐步审批的团队应检查这一默认行为，并在需要时切换回手动模式。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/claudeai/status/2113360845409583307">Claude 网页、桌面和移动端将默认启用 auto mode</a></li>
<li><a href="https://xiaoan.cc/article/claude-xia-zhou-mo-ren-kai-qi-auto-mode-wang-ye-zhuo-mian-he-ahf">Claude下周默认开启auto mode：网页、桌面和手机端一起变</a></li>
<li><a href="https://claude.com/resources/articles/auto-mode-default-in-claude-code">Auto mode is now the default in Claude Code for Pro, Max, and ...</a></li>
<li><a href="https://the-decoder.com/anthropic-sets-claude-code-to-auto-mode-by-default-to-protect-developers-from-bad-approvals/">Anthropic sets Claude Code to Auto Mode by default to protect ...</a></li>

</ul>
</details>

**标签**: `#claude-code`, `#coding-agents`, `#developer-workflow`, `#ai-safety`, `#product-update`

---

<a id="item-tech-news-2"></a>
### [Switch 2 越狱与 Codex 硬件控制工作流](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ⭐️ 7.0/10

**级别**: 核心必看

一篇个人博客报告声称已实现 Nintendo Switch 2 越狱，并展示了一种面向安全研究的 Codex–JetKVM 工作流：JetKVM 通过 USB 发送手柄输入，并通过 HDMI 回传主机画面，供 Codex 观察屏幕和操作设备。由于 Switch 2 崩溃后需要按电源键重启，作者还使用蓝牙灯开关的杠杆充当物理执行器，开关下压时按住电源键，随后由剩余扭矩将机构抬起。现有材料未说明漏洞细节、适用固件或版本、下载方式及稳定性，且主要依据是个人博客，因此越狱效果与可复现性尚无法独立确认。

hackernews · ledoge · 10月22日 08:01 · [社区讨论](https://news.ycombinator.com/item?id=50192536)

**「背景」** Switch 2 于 2025 年发售，是任天堂推出的新一代游戏主机。ns2jb 报告针对的是系统固件 23.0.1，作者将其描述为软件型、需连线的 userland 越狱（tool-2-2、tool-2-3），需要借助 SmileBASIC 4.4.9 应用触发，并在宿主机（macOS 或 Linux）上运行 Node.js 22+ 才能使用（tool-2-3）。这次越狱工作流将 OpenAI Codex 等 AI 工具与 JetKVM 等硬件控制设备结合，是主机安全研究中出现的一种新范式（tool-1-1、tool-1-3）。

**「对用户和开发者的实际影响」** 如果该漏洞在 Switch 2 的 23.0.1 固件上能够稳定复现，用户和开发者将可用纯软件方式运行自制软件、修改游戏并备份存档。不过，ns2jb 被报道为需要通过连线重新应用的 userland 越狱，重启后需要再次利用，并非永久安装的自定义固件，因此不能视为无需维护的永久解锁方案。

**「社区对后果与工具限制的看法」** 评论者 hturan 认为，如果该方案确实能解密并读写文件系统，Switch 2 游戏镜像可能很快出现，并担忧主机独占游戏因此更容易在其他硬件上运行；这是对潜在后果的推测，并非已验证结果。非 functional 指出评论中描述的电源键执行器是 SwitchBot Bot，rootsudo 则称 Codex 在其 Android 漏洞研究任务中曾因安全策略拒绝操作，显示实际能力仍会受任务场景和访问层级影响。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/">Jailbreaking the Switch 2</a></li>
<li><a href="https://gbatemp.net/news/switch-2-jailbreak-ns2jb-released-software-only-exploit-tethered.685698/">Switch 2 jailbreak &quot;ns2jb&quot; released. Software-only exploit ...</a></li>
<li><a href="https://gitlab.com/pepsipu/ns2jb">Sammy Hajhamid / ns2jb · GitLab</a></li>
<li><a href="https://wccftech.com/nintendo-switch-2-hacked-jailbreak/">The Nintendo Switch 2 Has Been Hacked, As First Jailbreak Blows...</a></li>
<li><a href="https://www.aipulse.it/en/news/nintendo-switch-2-jailbreak-ns2jb-exploit-504293">Switch 2 Jailbroken: First Software Exploit Runs Homebrew and ...</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Codex`, `#computer-use agents`, `#hardware jailbreaking`, `#KVM`

---

<a id="item-tech-news-3"></a>
### [Anthropic 将 Agent Skills 标准捐赠给 AAIF](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 宣布已将 Agent Skills 标准捐赠给 Linux Foundation 旗下的 Agentic AI Foundation（AAIF），并称目标是让该规范保持开放、由社区驱动且厂商中立。AAIF 由 Anthropic、Block 和 OpenAI 共同创立，Anthropic 此前也已向该基金会捐赠 Model Context Protocol（MCP）；本次公告没有提供新的规范版本或实现要求。

rss · Simon Willison · 10月22日 18:09

**「从开放标准声明到基金会治理」** Anthropic 早在 2025 年 12 月便首次将 Agent Skills 称为“开放标准”，Simon Willison 当时也预测它可能进入 Agentic AI Foundation。此次公告是在既有标准上的治理移交，而非新的技术规范发布；所给来源没有列出新的版本、格式或实现要求。

**「开发者面临治理变化」** 对构建 AI 智能体的开发者而言，Agent Skills 的治理归属已进入 AAIF，不再仅由 Anthropic 单方面推动。现有来源未说明新的治理流程、规范版本节奏或兼容性变化，因此没有证据表明现有 Agent Skills 实现需要立即调整。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/22/donating-agent-skills/">Donating Agent Skills to the Agentic AI Foundation</a></li>

</ul>
</details>

**标签**: `#Agent Skills`, `#Agentic AI Foundation`, `#AI agents`, `#Model Context Protocol`, `#open standards`

---

<a id="item-tech-news-4"></a>
### [Replit Monitoring Agent 支持自动修复与部署](https://replit.com/blog/replit-monitoring-agent) ⭐️ 7.0/10

**级别**: 核心必看

Replit 已发布 Monitoring Agent，作为应用监控功能的自主值班智能体；它可读取生产日志和指标，调查错误、变慢和部署失败。用户在应用的 Publishing 设置中启用 autofix 后，智能体会验证修复并通过邮件汇报；进一步启用 auto-publish，还可自动部署修复。该功能建立在先前上线的 App Monitoring 之上，但官方文章未披露其架构、评测结果或安全边界。

rss · AI 热榜 · 10月22日 20:24

**「基于既有应用监控」** Monitoring Agent 建立在 Replit 此前上线的 App Monitoring 之上，因此其运行前提是应用已接入现有的监控与发布工作流；开发者可从应用的 Publishing 设置中启用相关功能。当前来源没有进一步交代 App Monitoring 的具体架构或能力边界，不能据此判断两者在监控范围上的差异。

**「开发者可按风险选择自动化程度」** 开发者可以让 Monitoring Agent 从故障调查延伸到修复验证和部署，而不必只接收告警；是否自动发布修复可分别通过 autofix 和 auto-publish 控制。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://replit.com/blog/replit-monitoring-agent">Replit 发布 Monitoring Agent，为应用提供可自动修复并部署的值班智能体</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Replit`, `#application monitoring`, `#automated deployment`, `#developer tools`

---

<a id="item-tech-news-5"></a>
### [OpenAI 发布 Decisions API](https://openai.com/index/decisions-api) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 已正式提供基于 GPT-6 Luna 的 Decisions API，供开发者处理分类、路由、评分等有界答案问题。OpenAI 称，该 API 的执行速度最高可比通过 Responses API 使用同一模型快 10 倍。消息未披露定价、接口细节或基准测试条件，因此这一数字应视为厂商给出的最高值，而非普遍性能保证。

rss · AI 热榜 · 10月22日 19:00

**「专用接口与通用调用的区别」** 这里的“决策”指分类、路由、评分等答案范围预先受限的任务，而不是开放式内容生成；OpenAI 将 Decisions API 与通过通用 Responses API 调用 GPT-6 Luna 作对照。该接口面向应用或智能体从文本、图像和结构化输入中选择预定义结果，因此其定位是专用决策端点，而非通用模型端点的全面替代。

**「开发者需验证实际收益」** 使用 GPT-6 Luna 的开发者可把 Decisions API 作为有界决策工作负载的专用候选，并在接入前核实接口兼容性、计费标准和自身负载下的延迟；现有材料不足以证明它能带来相应的成本节省。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://openai.com/index/decisions-api">OpenAI 正式发布 Decisions API，面向低延迟低成本小决策</a></li>
<li><a href="https://openai.com/index/decisions-api/">Build more responsive apps with the Decisions API | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Decisions API`, `#GPT-6 Luna`, `#低延迟推理`, `#模型路由`

---

### 更多动态

<a id="item-tech-news-6"></a>
#### [Gemini CLI 夜间版加入容器 IDE 桥接](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0-nightly.20261022.g09d81bf11) ⭐️ 6.0/10

Gemini CLI 发布 v0.67.0-nightly.20261022.g09d81bf11 夜间版，面向使用 IDE 与容器沙箱的开发者。发布说明称，CLI 现在可通过 exec stdio 将 IDE companion 桥接进容器沙箱，并修复工作区为主目录时重复加载 agent、不受信任标志检查范围及已批准标志记忆等问题。A2A 服务端改为在注册 SDK 路由前挂载 express.json\(\)，自定义请求头拆分遵循 RFC 9110，atomic writeTextFile 也会尊重只读文件和硬链接；IDE 设置与 GEMINI.md 则不再纳入打开文件的上下文。

github · gemini-cli-robot · 10月22日 01:23

<a id="item-tech-news-7"></a>
#### [GitHub Copilot CLI v1.0.103 改进沙箱与会话恢复](https://github.com/github/copilot-cli/releases/tag/v1.0.103) ⭐️ 6.0/10

GitHub 已发布 GitHub Copilot CLI v1.0.103，为 ACP 会话、恢复会话和云端重连路径带来增量修复：保存的沙箱设置及 --sandbox/--no-sandbox 参数现在会在恢复时生效，连接中断后重连也会保留云端回复全文。该版本还让 dnx 复用现有 .NET 和 NuGet 沙箱授权，并在启用开发者工具访问时，将同类授权应用到 Windows 上的 npm.cmd 等 shim；GPT-5 默认 Responses verbosity、Gemini 可空及枚举字段的 schema 报错、会话标题和 hash mention 刷新也得到修正。开发者工具方面，MCP 工具快照现可在同一仓库的不同 Git worktree 间复用；远程启动改用含义更清晰的 hosting/connection 选项，旧有 --remote/--no-remote 启动参数被移除，但给定变更摘录未列出具体替代参数。

github · copilot-cli-release-app\[bot\] · 10月22日 16:21

<a id="item-tech-news-8"></a>
#### [Anthropic 发布常驻代理 Claude Duet](https://the-decoder.com/anthropic-takes-on-grok-bot-metas-muse-and-openais-dots-with-its-always-on-agent-claude-duet/) ⭐️ 6.0/10

Anthropic 推出主动型 AI 代理 Claude Duet，即使用户不在线，它也能自行处理任务；Anthropic 据称借此应对 xAI、Meta 和 OpenAI 的类似产品。Duet 基于 Claude Opus 5.5，通过 6,000 多个连接器接入 Gmail、Slack、Stripe 等服务，并在付款等敏感操作前请求用户批准。报道没有说明连接器的具体实现、SDK 可用性、定价、部署模式或扩展方法，因此尚不足以判断其工程可定制性。

rss · The Decoder · 10月22日 08:35

<a id="item-tech-news-9"></a>
#### [Vercel Labs 开源可嵌入的 Zig 编程代理 fx](https://www.infoq.com/news/2026/10/vercel-zig-fx-agent/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news) ⭐️ 5.0/10

Vercel Labs 已开源实验性编程代理 fx；该项目使用 Zig 编写，可作为 CLI、脚本组件或嵌入式库运行，并提供 WebAssembly 构建。Vercel 将 fx 标记为 1.0 之前且仍在快速变化，现有报道没有提供其模型支持范围、架构、基准测试或实现指南。报道还提到，早期反馈质疑 fx 的“模型无关”主张，并指出该名称与现有工具冲突。

rss · InfoQ AI Coding · 10月22日 09:33

<a id="item-tech-news-10"></a>
#### [Google 推出 Agent Compute Engine,为每个 Gemini 智能体配备硬件隔离微型虚拟机](https://the-decoder.com/googles-agent-compute-engine-gives-every-gemini-agent-its-own-hardware-isolated-micro-virtual-machine/) ⭐️ 4.0/10

Google 宣布推出 Agent Compute Engine,据称是一款专为 AI 智能体设计的运行时环境,每个 Gemini 智能体可获得独立的硬件隔离微型虚拟机\(microVM\)。该方案同时扩展了治理能力,支持企业在云、混合云和本地环境中对智能体进行管理。原始来源未提供架构细节、可用性、定价、集成方式或限制条件,目前所披露的能力仍属厂商声明。

rss · The Decoder · 10月22日 17:50

<a id="item-tech-news-11"></a>
#### [MiniMax 开源 M3.1 Flash 模型权重](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ%3D%3D&amp;mid=2247489204&amp;idx=1&amp;sn=bc21e172929a366edfe02c720bef9208) ⭐️ 4.0/10

MiniMax 宣布开源 M3.1 Flash 模型权重；该模型总参数量为 428B，激活参数量为 23B。公司同时宣称，模型上线 72 小时内，真实用户处理的 Token 已超过 100 万亿，但这一使用量数据尚非独立测量结果。现有材料未提供许可证、上下文长度、硬件需求、基准表现及接入方式，开发者暂时难以评估其部署成本和实际能力。

rss · AI 热榜 · 10月23日 00:56