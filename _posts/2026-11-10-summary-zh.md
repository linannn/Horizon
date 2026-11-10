---
layout: default
title: "Horizon 每日速递：2026-11-10"
description: "AI 精选的技术与研究日报"
date: 2026-11-10
lang: zh
locale: zh-CN
---

> 从 54 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [browser-use 1.0.0rc5 改用持久化 Python REPL 代理](#item-tech-news-1) ⭐️ 8.0/10
2. [Claude Fable 5.2 与 Mythos 5.2 发布](#item-tech-news-2) ⭐️ 8.0/10
3. [GitHub Copilot CLI v1.0.108 发布](#item-tech-news-3) ⭐️ 7.0/10
4. [Meta 发布可调推理强度的 Muse Ember](#item-tech-news-4) ⭐️ 7.0/10
5. [Claude 构建开源 Beep Locator 定位神秘蜂鸣](#item-tech-news-5) ⭐️ 7.0/10
6. [Claude Mythos 5.2 预测完整 AAV 衣壳](#item-tech-news-6) ⭐️ 7.0/10
7. [用 details/summary 折叠冗长 PR 描述](#item-tech-news-7) ⭐️ 6.0/10
8. [Google 一年内推出四种 TPU，新增 8tx 与 8i Max](#item-tech-news-8) ⭐️ 6.0/10
9. [Anthropic 发布 Claude 开发模型选型指南](#item-tech-news-9) ⭐️ 6.0/10
10. [Opus 5.5 是否在 11 月 3 日后被降智](#item-tech-news-10) ⭐️ 5.0/10
11. [Claude Fable 5.2 实测：视频与 3D 网页一次直出](#item-tech-news-11) ⭐️ 4.0/10
12. [Anthropic 用 1000 个 Fable 5.2 智能体复现费马形式化证明](#item-tech-news-12) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [browser-use 1.0.0rc5 改用持久化 Python REPL 代理](https://github.com/browser-use/browser-use/releases/tag/1.0.0rc5) ⭐️ 8.0/10

**级别**: 核心必看

browser-use 发布第二个 1.0 候选版 1.0.0rc5，将代理引擎改为在持久化 Python REPL 中编写代码，通过 browser-harness 辅助函数和原生 CDP 操作基于 Pydantic AI 的浏览器；常用的 Agent、Browser、Tools、run\(\) 和 final\_result\(\) 接口仍然可用。该版本尚未正式发布，pip install browser-use 和 uv add browser-use 仍会安装 0.13.14，用户必须显式固定 browser-use==1.0.0rc5，且要求 Python 3.11 或更高版本。1.0 的默认行为也有破坏性变化：llm=None 使用 Browser Use 网关的 bu-fast，Browser\(\) 默认指向 Browser Use 云浏览器而非本地 Chromium，run\(\) 的 max\_steps 默认值从 500 降至 100，并设置 timeout=1700 秒；localhost 或私网 IP 任务需改用 Browser\(&\#x27;chromium&\#x27;\)。项目方在本次提交的 BU Bench v2（60 个任务、每个任务运行 3 次、使用云浏览器）上报告默认 ultrafast 模式得分 62.6（95% CI 58.2–67.1）、每任务成本 0.071 美元、每任务耗时 585 秒；这是发布方基准，并非独立测量结果。

github · gregpr07 · 11月9日 23:36

**「理解 1.0 的执行模型变化」** 要理解此次候选版的兼容边界，首先要区分 browser-use 0.x 与 1.0 的代理执行方式：0.x 从 DOM 快照中逐步挑选单个动作，1.0 则让代理在持久 Python REPL 中连续编写 Python，可混用 browser-harness 辅助函数和原始 CDP，并由 Pydantic AI 驱动。由于执行模型已改变，常见的 Agent、Browser、Tools、run\(\) 和 final\_result\(\) 虽仍可调用，0.x 中围绕单步动作编写的配置、终止和错误处理逻辑仍需对照 MIGRATING.md 逐项调整。

**「升级前需迁移配置」** 升级现有 0.x 项目的团队应先按 MIGRATING.md 迁移并显式固定版本：1.0 无法兑现的选项会在浏览器启动或计费前抛出 TypeError，已移除的导入会抛出包含替代项和迁移文档链接的 ImportError；访问 localhost 或私网 IP 时则必须改用 Browser\(&\#x27;chromium&\#x27;\)，而非默认的 Browser\(\)。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/browser-use/browser-use/releases/tag/1.0.0rc5">browser-use/browser-use released 1.0.0rc5</a></li>

</ul>
</details>

**标签**: `#browser-use`, `#AI agents`, `#agent tooling`, `#browser automation`, `#release candidate`

---

<a id="item-tech-news-2"></a>
### [Claude Fable 5.2 与 Mythos 5.2 发布](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 8.0/10

**级别**: 核心必看

Anthropic 的官方发布页列出 Claude Fable 5.2 与 Mythos 5.2，发布重点是智能体工作流与多智能体协作；现有材料未披露 Mythos 5.2 的独立规格。社区贴出的 GitHub 更新记录显示，\`claude-fable-5-2\` 已加入并成为默认 Fable 模型，提供 1M 上下文，标价列为每 Mtok $8/$40，缓存为 $0.20/Mtok。Anthropic 宣称，1,000 个 Fable 5.2 智能体在人类极少干预下，从极少提示出发自行建立协调机制，不使用数学参考资料，仅用一组中间定理陈述进行评分，并在 30 小时内完成费马大定理的形式化。作为对比，厂商称此前未发布的研究版 Claude 完成同一形式化用了 11 天，并依赖专用执行框架和人类研究员指导；这些数字来自厂商案例，材料未提供独立复现。

hackernews · meetpateltech · 11月9日 18:56 · [社区讨论](https://news.ycombinator.com/item?id=50429906)

**「双配置发布与迁移背景」** Anthropic 延续为同一代 Claude 模型提供 Fable 与 Mythos 两种配置的发布方式；官方系统卡称二者是同一新大型语言模型的两种配置，其中 Fable 面向通用使用，并增加了阻止模型在生物安全、网络安全等高风险双用途领域执行部分任务的防护。此次升级还涉及从 Fable 5.1、Mythos 5.1、Opus 5.5 及更早模型迁移，官方迁移指南列出了模型 ID、破坏性变更和迁移检查清单。

**「升级成本与评估要求」** 开发者现在可通过 \`claude-fable-5-2\` 使用 1M 上下文的默认 Fable 模型，但材料未给出它相对 Fable 5.1 的同 token 预算质量对比；升级评估应同时测量 token 用量与按每 Mtok $8/$40、缓存 $0.20/Mtok 计算的成本。

**「实际体验与效率争议」** 实际使用者 postalcoder 认为 Fable 5.2 表现不错，但普通任务中很难与 Opus 5.5 区分，只有把提示目标设得更高才更容易看到差异。motbus3 则质疑，如果 5.2 完成同类任务需要 5.1 的两倍 token，就不能据此断言它更聪明；breakwaterlabs 另对发布材料中的 effort-intel 曲线和若干基准对照提出疑问。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-2">Claude Fable 5.2 and Mythos 5.2</a></li>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-2/migration-guide">Claude Fable 5.2 and Claude Mythos 5.2 migration guide</a></li>
<li><a href="https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf">Claude Fable 5.2 &amp; Claude Mythos 5.2 System Card</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI agents`, `#multi-agent orchestration`, `#model releases`, `#developer workflows`

---

<a id="item-tech-news-3"></a>
### [GitHub Copilot CLI v1.0.108 发布](https://github.com/github/copilot-cli/releases/tag/v1.0.108) ⭐️ 7.0/10

**级别**: 核心必看

GitHub Copilot CLI v1.0.108 为编码代理工作流带来一组增量改进：Windows 可通过 \`settings.json\` 中的 \`sandbox.userPolicy.filesystem.enumeratePaths\` 配置仅枚举目录权限，\`/index\` 命令则默认对符合条件的仓库启用托管共享 tgrep 索引。沙箱开启时，切换目录后会重启本地 MCP 服务器，使其继承新目录的拒绝路径；Grok 4.7 和 Grok 4.6 的 PDF 附件失败时会回退为文件引用，SDK 指向命名管道、套接字或设备的附件则立即报错而非卡住当前轮次。\`/model\` 现在会在收到 421 Misdirected Request 后重新解析账户端点并列出模型，同时修复了重复自定义工具名、OpenAI 兼容提供商的内部消息字段、会话权限提示及多项输入和帮助显示问题。

github · copilot-cli-release-app\[bot\] · 11月9日 16:20

**「此次更新的技术背景」** 此次版本调整建立在 Copilot CLI 既有的沙箱权限与 MCP 会话机制之上：Windows 的 \`sandbox.userPolicy.filesystem.enumeratePaths\` 用于配置仅允许枚举目录的授权，而本地 MCP 服务器此前会在会话切换目录后继续沿用旧目录的拒绝路径。v1.0.108 将目录切换后的 MCP 服务器重启和 \`/mcp enable\` 对仓库禁用配置的尊重纳入这一机制，以避免权限状态与会话位置不一致。

**「对开发者的影响」** 依赖本地 MCP 服务器的开发者升级后，在 \`/cd\` 切换目录时不再需要手动重启服务器；但应检查仓库级 MCP 设置，因为 \`/mcp enable\` 现在不会覆盖禁用服务器的仓库配置。使用 SDK 的集成若注册两个同名自定义工具，升级后会被明确判定为错误，需要在创建或恢复会话前消除重名。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/github/copilot-cli/releases/tag/v1.0.108">github/copilot-cli released v1.0.108</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot CLI`, `#coding agents`, `#MCP`, `#sandboxing`, `#release notes`

---

<a id="item-tech-news-4"></a>
### [Meta 发布可调推理强度的 Muse Ember](https://research.meta.ai/blog/muse-ember) ⭐️ 7.0/10

**级别**: 核心必看

Meta 发布了 Muse Ember（muse-ember-1.0），并将其定位为最小的复杂推理执行模型，面向智能体的工具调用、编码子任务、路由、抽取和长文档解析。它提供 minimal、low、medium、high、xhigh、max 六档推理强度；发布材料以 mini-swe-agent 编码基准展示结果，对比中的所有模型均使用 max 档，Artificial Analysis 数据来自 2026 年 11 月 9 日发布的 Intelligence Index v5，每任务成本按各模型公开标价计算。转述的价格为每百万输入 token 0.10 美元、每百万缓存输入 token 0.004 美元、每百万输出 token 0.50 美元；但权重的获取方式仍不明确，一位评论者称未找到权重，另有实测者称增加推理 token 并未明显提升 SVG 质量。

hackernews · AI 热榜 · 11月9日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=50429024)

**「产品定位与可用范围」** Artificial Analysis 将 Muse Ember 归为 Meta 新推出的“高效档”模型线，并称其输入、输出 token 价格与 Claude Haiku 5.5 和 GPT-6 Luna 相同，这为理解其成本定位提供了参照。Meta 的开发者材料确认，该模型已登陆 Muse Code 和 Meta Model API，并支持文本、图像、音频与视频输入，明确了发布时的可用渠道与多模态范围。

**「在现有代理流程中直接评测」** 编码代理团队可以将 Muse Ember 作为 mini-swe-agent 的候选模型：OpenRouter 提供了 API 接入路径，而 mini-swe-agent 支持在本地命令行中运行和开展基准评测。选型时应结合任务质量、每任务价格与响应时间进行比较，Artificial Analysis 已提供相应的价格和性能对照。

**「更多推理未必带来更好结果」** Simon Willison 称，在其 SVG 样例中，推理档位与视觉质量常见的正相关关系在 Muse Ember 上没有出现，增加推理 token 也未产生显然更好的结果；这是个人实测，不能替代系统性基准测试。评论者还指出，其突出基准结果来自 mini-swe-agent 而非 Meta 自有 agent harness，并表达了对开放权重的期待；另有观点预测智能体模型会像早期 PC 一样分化到法律、编码、会计和设计等专用类别，但这尚非已验证的产品或市场事实。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://research.meta.ai/blog/muse-ember">Our Smallest, Most Efficient Model: Muse Ember</a></li>
<li><a href="https://artificialanalysis.ai/articles/meta-s-muse-ember-is-the-cheapest-model-scoring-36-on-the-intelligence-index">Meta&#x27;s Muse Ember is the cheapest model scoring... | Artificial Analysis</a></li>
<li><a href="https://dev.meta.ai/resources/blog/build-with-muse-ember">Start building with Muse Ember, our smallest, most efficient ...</a></li>
<li><a href="https://openrouter.ai/meta/muse-ember">Muse Ember - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/muse-ember">Muse Ember (max) - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://github.com/SWE-agent/mini-swe-agent">GitHub - SWE - agent / mini - swe - agent : The 100 line AI agent that...</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#small-language-models`, `#reasoning-effort`, `#model-benchmarks`, `#model-efficiency`

---

<a id="item-tech-news-5"></a>
### [Claude 构建开源 Beep Locator 定位神秘蜂鸣](https://simonwillison.net/2026/Nov/9/mysterious-beeps/) ⭐️ 7.0/10

**级别**: 核心必看

Simon Willison 通过 iPhone 上的 Claude Code Cloud 启动项目，使用 Opus 5.5 的 Extra thinking 模式，随后在 Claude Code 中继续开发，并以开源 GitHub 项目发布了 Beep Locator。这套 Web 应用由 Python 服务端通过 WebSocket 协调多个浏览器监听器；监听端使用 WebAudio 保留 60 秒音频缓冲，以快速傅里叶变换和高通滤波检测蜂鸣，再由服务端让往返时延最低的设备发出同步短鸣，以对齐各监听器上传的录音片段。人工确认目标频率并回放匹配声音后，系统会持续监听并结合测距结果在地图上标出最可能的位置。Willison 使用两台 iPad、一部手机、一台 MacBook Pro 和一台 Surface Ultra 测试，称系统将声源定位到约 40 厘米以内，最终找到了需要更换电池的旧一氧化碳探测器；这是他在自家房间中的一次实践结果。

rss · Simon Willison · 11月9日 23:57

**「技术背景」** Beep Locator 的声学测距思路来自 2007 年论文《BeepBeep: A High-Accuracy Acoustic-Based System for Ranging and Localization Using COTS Devices》，该方案结合双向感知、自记录和采样计数，仅依赖扬声器、麦克风及设备间通信，无需预置定位基础设施。Claude 在起草项目的 problem.md 时找到并阅读了这篇论文，Willison 确认其适用性后才让 Claude 继续实现。

**「部署与验证」** 实际部署时，用户需要至少一台能够运行 Python Web 服务的设备，其余手机、平板或笔记本可扫描二维码或通过加入链接连接，并需支持浏览器麦克风、WebAudio、WebSocket 及扬声器输出。由于设备互播声音的自动定位效果不理想，实际版本提供 Rough mode，允许用户拖动图标输入大致位置；用户还可用拍手模式在不同位置测试定位结果，再确认目标蜂鸣。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Nov/9/mysterious-beeps/">Locating the source of a mysterious beep with Claude</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding agents`, `#developer workflow`, `#multimodal audio`, `#open-source tools`

---

<a id="item-tech-news-6"></a>
### [Claude Mythos 5.2 预测完整 AAV 衣壳](https://www.youtube.com/watch?v=FMbXUxn_nBw) ⭐️ 7.0/10

**级别**: 核心必看

Claude 官方视频称，Claude Mythos 5.2 编写了调用开源折叠模型的代码，先预测 5 个相邻 AAV 链，再利用 AAV 衣壳的对称性拼装出包含全部 60 条链的完整衣壳。视频称，在 AAV2 上，预测结果与实验结构的误差约为一个原子宽度。这是官方演示报告的结果；现有条目未提供误差指标定义、提示词、工具链或可复现产物，因此不能视为独立验证或通用精度结论。

rss · AI 热榜 · 11月9日 18:56

**「Mythos 5.2 的定位与访问条件」** Anthropic 将 Claude Mythos 5.2 定位为面向网络安全和生命科学研究的高能力模型，并在 5.2 发布材料中称已升级 Mythos。官方模型指南将一般可用型号与 Mythos 5.2 分开列出，后者通过验证计划提供，因此这项 AAV 衣壳演示应结合其验证计划的访问条件理解，而不能视为已向所有用户普遍开放的常规模型能力。

**「结构预测团队需先独立复现」** 对考虑用编码代理开展蛋白结构预测的团队，这一流程提供了可评估的编排方式：让代理生成并运行五链预测代码，再依据对称性完成全衣壳装配。但在缺少代码、折叠模型版本、运行环境和完整误差统计的情况下，不宜将该结果直接用于基因治疗研发决策，应先独立复现并核对 AAV2 误差的具体计算方法。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=FMbXUxn_nBw">Claude Mythos 5.2 预测基因治疗载体 AAV 衣壳结构</a></li>
<li><a href="https://claude.dev/blog/which-claude-model-should-you-build-with/">Which Claude model should you build with? / claude .dev Blog</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-2">Introducing Claude Fable 5 . 2 and Claude Mythos 5 . 2 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude`, `#coding agents`, `#AI for science`, `#protein structure prediction`

---

### 更多动态

<a id="item-tech-news-7"></a>
#### [用 details/summary 折叠冗长 PR 描述](https://simonwillison.net/2026/Nov/9/details-summary/) ⭐️ 6.0/10

Simon Willison 分享并已在使用一种 GitHub PR 描述排版方案：在人工挑选的高层导语和可选截图之后，用 \`&lt;details&gt;&lt;summary&gt;\` 折叠代理生成的长篇说明。折叠标题会标明所用模型及运行档位，例如“Claude Opus 5.5 Medium”，完整内容仍可展开阅读。GitHub Markdown 原生支持这两个标签，可直接用于 PR 描述和问题评论；这是改善 Claude Code、Codex 等代理所生成 PR 审阅体验的个人工作流技巧，而不是平台或模型的新功能发布。

rss · Simon Willison · 11月9日 04:25

<a id="item-tech-news-8"></a>
#### [Google 一年内推出四种 TPU，新增 8tx 与 8i Max](https://the-decoder.com/google-ships-four-tpu-variants-in-one-year-as-it-ramps-up-competition-with-nvidia/) ⭐️ 6.0/10

Google 在一年内推出四种 TPU 变体，其中 TPU 8tx 通过机密计算让敏感数据在处理期间仍保持加密，TPU 8i Max 则在单个封装内放置两颗芯片，使算力和内存翻倍。报道将这两项能力描述为已经扩展到 TPU 8 家族，而非仅处于计划阶段。目前外部客户已接近 100 家，但报道未给出定价、供货范围、性能基准或开发者接入细节，因此尚不能据此判断实际部署成本。

rss · The Decoder · 11月9日 12:59

<a id="item-tech-news-9"></a>
#### [Anthropic 发布 Claude 开发模型选型指南](https://claude.dev/blog/which-claude-model-should-you-build-with/) ⭐️ 6.0/10

Anthropic 在 Claude.dev 开发者博客发布指南，帮助开发者在 Haiku 5.5、Sonnet 5.5、Opus 5.5 和 Fable 5.2 之间选择。Anthropic 建议多数编码与知识工作先使用 Opus 5.5 的 medium effort，并称其 token 价格为 Fable 5.2 的一半。现有来源未提供具体价格、能力基准、适用边界或迁移细节，因此这属于厂商建议，而非独立测得的选型结论。

rss · AI 热榜 · 11月9日 12:00

<a id="item-tech-news-10"></a>
#### [Opus 5.5 是否在 11 月 3 日后被降智](https://twitter.com/shanemelaugh/status/2119192075505893695) ⭐️ 5.0/10

该 Hacker News 讨论转述的帖子质疑 Claude Opus 5.5 自 11 月 3 日起发生“降智”，包括思考模式、工具使用和输出一致性的变化，但论据主要仍是轶事，未形成已验证的回归。ianberdin 称其当天用与 9 月相同的提示词和设置复跑一个 SVG 基准：空文件任务中，Max 流式模式（128K 上限）在 9 月和当天均为 128,000 tokens、$2.56；Max Batch API（300K）则从 9 月的 255,957 tokens、$2.56 变为当天的 243,707 tokens、$2.44。评论者据此否认行为退化，losvedir 也称其熟悉的 livenerf 纵向评测未显现信号，但这些结果尚未独立验证。

hackernews · rzk · 11月9日 07:04 · [社区讨论](https://news.ycombinator.com/item?id=50422069)

<a id="item-tech-news-11"></a>
#### [Claude Fable 5.2 实测：视频与 3D 网页一次直出](https://mp.weixin.qq.com/s/sKoVHL_oNsik9vtUjr0lHg) ⭐️ 4.0/10

原文称 Anthropic 凌晨正式发布 Claude Fable 5.2，作者随即测试了视频动效、Three.js 3D 场景和苹果静安店 3D 网页等 10 个任务。这些任务均“一次直出”，且作者称未在生成视频中发现事实错误。不过，文章未公开提示词、生成产物、测试方法、版本变更或 API 与可用性信息，因此该结果更接近有限样本的演示性体验，而非可复现的工程评测。

rss · AI 热榜 · 11月9日 23:21

<a id="item-tech-news-12"></a>
#### [Anthropic 用 1000 个 Fable 5.2 智能体复现费马形式化证明](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) ⭐️ 4.0/10

Anthropic 报告称，其玩具实验让 1000 个运行 Claude Fable 5.2 早期版本的智能体在沙箱中、且没有 Prove2Me 平台或研究者指导的情况下，用 28.7 小时复现了费马大定理的形式化证明。相较 9 月的形式化结果，输出 token 降至三分之一，证明长度缩至七分之一。该结果属于厂商自述，来源未披露编排架构、安全机制、提示与工具链、验证流程或可复现细节，因此尚不能视为经过独立验证的模型能力指标。

rss · AI 热榜 · 11月9日 12:00