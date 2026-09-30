---
layout: default
title: "Horizon 每日速递：2026-09-30"
description: "AI 精选的技术与研究日报"
date: 2026-09-30
lang: zh
locale: zh-CN
---

> 从 83 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI 在 DevDay 2026 扩展 Codex 与 API：安全扫描、Decisions API 和 Ultrafast](#item-1) ⭐️ 8.0/10
2. [Shopify 放弃 React Native，借 AI 智能体 12 周重写 Shop 应用](#item-2) ⭐️ 7.0/10
3. [OpenRouter 教程：用生产流量构建 golden 评测集并跨模型复测](#item-3) ⭐️ 7.0/10
4. [OpenAI 推出可复用的 Codex 云环境，支持跨设备跟进任务](#item-4) ⭐️ 7.0/10
5. [OpenAI 发布 GPT-6.1 Sol，主打智能体编码与跨应用工作流](#item-5) ⭐️ 7.0/10
6. [OpenAI DevDay 2026：Dots 智能体、GPT-6.1 Sol 与 500 美元订阅](#item-6) ⭐️ 7.0/10
7. [pydantic-ai 1.107.7 修复 web\_fetch 中度拒绝服务漏洞](#item-7) ⭐️ 6.0/10
8. [OpenAI DevDay：ChatGPT 变身平台，推出插件、MCP 与共享工作区](#item-8) ⭐️ 6.0/10
9. [Claude Code v2.1.285 发布：新增 MCP 安装配置与提供商限制](#item-9) ⭐️ 5.0/10
10. [OpenAI 发布 GPT-6.1 Sol：接近 Astra 的智能，价格仅约五分之一](#item-10) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [OpenAI 在 DevDay 2026 扩展 Codex 与 API：安全扫描、Decisions API 和 Ultrafast](https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/) ⭐️ 8.0/10

**级别**: 核心必看

在 DevDay 2026 上，OpenAI 为 Codex 加入了可复用的云环境、针对 GitHub 仓库的自动安全扫描，以及桌面应用中的代码审查视图；Agents API 新增了 Computer Use 支持，并推出了全新的 Decisions API。同时发布的还有高级档位 Ultrafast，官方称最高可达 8 倍速度，价格为原来的 6 倍。 这些更新把 Codex 从代码补全工具推向具备云沙箱、内置安全审查和专用决策层的完整智能体开发平台，对于已经把 AI 编码智能体纳入标准流程、并在速度与成本之间权衡的团队意义重大。 速度的说法需要谨慎对待：The Decoder 称最高 8 倍速度、6 倍价格，而 OpenAI 官方 DevDay 社区帖子的表述是 Codex 中令牌生成最高快 8 倍、API 中快 6 倍；此外，基于小型模型 GPT-6 Luna 构建、约 150 毫秒内返回带置信度的预设答案的 Decisions API 目前仅为限量预览，价格尚未公布。

rss · The Decoder · 9月29日 17:14

**背景**: OpenAI 的年度 DevDay 是其主要的开发者大会，通常会集中发布模型、API 与工具链更新；Codex 是其编码智能体产品，而 Agents API 是开发者用来构建可代表模型调用工具的自主智能体的接口。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/">OpenAI expands Codex and its API at DevDay with security scans, a Decisions API, and Ultrafast</a></li>
<li><a href="https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006">DevDay 2026 announcements and developer resources</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/tools/computer-use">Computer use | OpenAI API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#coding-agents`, `#API`, `#DevDay`

---

<a id="item-2"></a>
## [Shopify 放弃 React Native，借 AI 智能体 12 周重写 Shop 应用](https://newsletter.pragmaticengineer.com/p/shopify-native-mobile) ⭐️ 7.0/10

**级别**: 核心必看

Shopify 宣布原生开发是其移动开发的未来，其 Shop 应用已在 AI 编码智能体的协助下用 12 周时间重写为完全原生的 Swift 和 Kotlin 应用，其余应用也将陆续迁移。而仅仅大约一年前，这家电商平台还公开表示对 React Native 非常满意。 一家大型电商公司公开逆转其跨平台移动战略，并把原因归于 AI 编码智能体，这是一个明确的落地信号，会影响其他工程团队在“用 AI 辅助重写原生”与“继续留在 React Native”之间的权衡。 报道中的成果只涉及 Shop 这一个应用在 12 周内完成重写，而 Shopify 其他应用的迁移目前只是计划而非已完成的事实，因此这一做法的成本、性能与质量取舍在单个案例之外仍未得到验证。

rss · AI 热榜 · 9月29日 15:53

**背景**: React Native 是一个跨平台框架，允许团队用一套 JavaScript/TypeScript 代码同时覆盖 iOS 和 Android；而原生开发则意味着分别维护 Swift（iOS）与 Kotlin（Android）两套代码库，传统上成本更高，但性能更好、与平台特性贴合更紧密。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://newsletter.pragmaticengineer.com/p/shopify-native-mobile">Shopify 宣布放弃 React Native，AI 编码智能体让回归原生开发成为新选择</a></li>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026)</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#React Native`, `#mobile development`, `#native development`, `#engineering case study`

---

<a id="item-3"></a>
## [OpenRouter 教程：用生产流量构建 golden 评测集并跨模型复测](https://openrouter.ai/blog/tutorials/building-a-golden-eval-dataset-from-production-traffic/) ⭐️ 7.0/10

**级别**: 核心必看

OpenRouter 发布了一篇教程，给出了把生产流量转化为 golden 评测集的五步流程：抽样生产流量、去重聚类、添加预期输出、在首轮评估后修正 rubric、提交到 Git 并接入 CI，最终让该评测集充当每次部署前的回归测试。文中还给出了分阶段落地的建议。 这为正在交付 LLM 功能的团队提供了一套可复用、上手成本不高的做法，让他们用真实反映自身用户分布的流量来捕捉模型或提示词变更带来的回归，而不必依赖通用的公开基准或合成提示词。 教程建议先从 20 到 50 条经过人工复审的样本起步，再扩展为 100 到 1,000 条的完整回归集；同时强调应优先使用真实流量而非合成数据，因为合成提示词往往会丢失线上流量的分布特征和具体失败模式。

rss · AI 热榜 · 9月30日 00:00

**背景**: golden 评测集是一组经过人工整理、输入与预期输出配对的样本集合，作为 AI 应用的固定测试集，使不同时间点的评测结果可以相互比较。发布该教程的 OpenRouter 是一个提供统一 API、可访问多家厂商模型的平台。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://openrouter.ai/blog/tutorials/building-a-golden-eval-dataset-from-production-traffic/">OpenRouter 教程：如何从生产流量构建 golden 评测集并跨模型复测</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>
<li><a href="https://arize.com/resources/llm-evaluation/">LLM evaluation : methods, metrics, RAG &amp; agent evals guide | Arize</a></li>

</ul>
</details>

**标签**: `#evaluation`, `#llmops`, `#ci-cd`, `#regression-testing`, `#ai-engineering`

---

<a id="item-4"></a>
## [OpenAI 推出可复用的 Codex 云环境，支持跨设备跟进任务](https://x.com/OpenAIDevs/status/2105073633731461197) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 宣布推出 Codex 云环境（Codex cloud environments），Codex 任务可在可复用的预配置云环境中运行，仓库、依赖、脚本和设置均已预先就位，从而减少配置工作并加快启动。用户合上电脑后智能体仍继续运行，可通过手机或另一台电脑跟进进度并调整任务，相关文档见 learn.chatgpt.com/docs/cloud。 把编码智能体的执行从单台本地机器上解耦，意味着 Codex 正走向持久化、跨设备的智能体工作流，这将直接与 GitHub Codespaces 等成熟云开发环境竞争，并可能改变开发者委派长时任务的方式。 细节仍较为有限：该公告只是一条简短的社交媒体帖子并附上文档链接，未披露基准测试、定价、可用范围或所支持环境镜像的清单。

rss · AI 热榜 · 9月29日 23:13

**背景**: Codex 是 OpenAI 的 AI 编码智能体产品线，最早于 2025 年 4 月以在本地终端运行的开源 CLI 形式发布。云开发环境（如 GitHub Codespaces 这类远程预配置工作区）已成为标准化依赖、保证工作可复现的常见做法。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/OpenAIDevs/status/2105073633731461197">OpenAI 推出 Codex 云环境，可复用配置并跨设备跟进任务</a></li>
<li><a href="https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/">OpenAI gives Codex reusable cloud environments that work across devices | TechCrunch</a></li>

</ul>
</details>

**标签**: `#OpenAI Codex`, `#coding agents`, `#cloud development environments`, `#developer tooling`, `#AI agent workflows`

---

<a id="item-5"></a>
## [OpenAI 发布 GPT-6.1 Sol，主打智能体编码与跨应用工作流](https://x.com/OpenAIDevs/status/2105073621144338660) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 发布 GPT-6.1 Sol，开发者可通过 OpenAI API 以 gpt-6.1-sol 调用该模型，其针对编码、computer use 和跨应用智能体工作流做了优化，面向复杂重构、深度代码库调查和长时间运行的智能体等场景。它的定价低于 GPT-6 Astra——第三方报道称其费用约为 Astra 的五分之一、性能接近 Astra——缓存输入相较标准输入定价享有 95% 的折扣。 OpenAI 把智能体编码和 computer use 能力放进比旗舰 Astra 更便宜的价位，降低了运行长时间编码智能体的成本，这会直接影响开发者在多步骤、跨应用自动化任务上的模型选型。 发布内容本身没有给出基准测试分数、上下文窗口上限或迁移指南，目前唯一披露的评测细节是计算机使用能力在 OSWorld 2.0 的离线集上进行了评估；另外 95% 这个数字针对的是缓存输入相对标准输入定价的折扣，与第三方报道的“整体费用约为 Astra 五分之一”并不是同一件事。

rss · AI 热榜 · 9月29日 23:13

**背景**: GPT-6.1 Sol 在 OpenAI 的产品序列中位于旗舰模型 GPT-6 Astra 之下；“computer use”指让模型通过读取截图和工具返回结果来操作浏览器与桌面界面，而智能体工作流（agentic workflow）指由自主智能体在极少人工干预下规划并执行多步骤任务的 AI 流程。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/OpenAIDevs/status/2105073621144338660">OpenAI 发布 GPT-6.1 Sol，主打智能体编码与跨应用工作流</a></li>
<li><a href="https://openai.com/zh-Hans-CN/index/introducing-gpt-6-1-sol/">推出 GPT - 6 . 1 Sol | OpenAI</a></li>
<li><a href="https://www.ithome.com/1/008/527.htm">同性 能 下最高性价比 AI 模型： OpenAI 发 布 GPT - 6 . 1 Sol ...</a></li>

</ul>
</details>

**标签**: `#openai`, `#gpt-6.1-sol`, `#coding-agents`, `#agentic-workflows`, `#model-release`

---

<a id="item-6"></a>
## [OpenAI DevDay 2026：Dots 智能体、GPT-6.1 Sol 与 500 美元订阅](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&amp;mid=2647686841&amp;idx=1&amp;sn=630c0dc22de47c9c2f58bd5253a91a9a&amp;chksm=f1e33576f80f214c7290b1545cc8bfbb32ac24c3144cd141b7c2dd7cdaaf71f44d3cf319db8b&amp;scene=126&amp;sessionid=1790722837#rd) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 在 DevDay 2026 上发布了一揽子更新：面向 ChatGPT Pro、Business Premium 和 Enterprise 用户推出全天候个人智能体 Dots，支持与 4000 多个应用协作；上线新模型 GPT-6.1 Sol，官方称其智能水平接近 GPT-6 Astra；并新增每月 500 美元订阅档位。与此同时，200 美元 Pro 套餐的额度倍数从 20x 下调至 10x，500 美元档位为 25x。 全天候智能体、更便宜的准旗舰模型与重新设计的额度定价三者叠加，显示 OpenAI 正把 AI 从“回答问题”的工具推进为可持续执行任务的智能体，这直接影响开发者和企业在选型、成本预算上的决策，也使其与 Meta 的 Muse 等对手的竞争更加激烈。 成本说法依据的口径并不一致：这篇微信总结称 GPT-6.1 Sol 约为 Astra 单任务成本的七分之一，而 OpenAI 官方发布稿的表述是其标准 API 输入与输出 token 价格为 Astra 的五分之一；此外该文属于二手汇总，未给出基准测试或实现细节。

rss · AI 热榜 · 9月29日 21:47

**背景**: DevDay 是 OpenAI 每年面向开发者举办的大会，通常集中发布产品与定价更新；GPT-6 Sol 距 GPT-6.1 Sol 发布仅约一周，而 Dots 则是 OpenAI 对 Meta 走红的个人智能体 Muse 的回应。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&amp;mid=2647686841&amp;idx=1&amp;sn=630c0dc22de47c9c2f58bd5253a91a9a&amp;chksm=f1e33576f80f214c7290b1545cc8bfbb32ac24c3144cd141b7c2dd7cdaaf71f44d3cf319db8b&amp;scene=126&amp;sessionid=1790722837#rd">OpenAI DevDay 2026 发布 Dots、GPT-6.1 Sol、500美元订阅等一揽子更新</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT-6.1 Sol | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots | OpenAI</a></li>

</ul>
</details>

**标签**: `#openai`, `#ai-agents`, `#model-release`, `#pricing`, `#devday`

---

## 更多动态

<a id="item-7"></a>
### [pydantic-ai 1.107.7 修复 web\_fetch 中度拒绝服务漏洞](https://github.com/pydantic/pydantic-ai/releases/tag/v1.107.7) ⭐️ 6.0/10

pydantic-ai 发布了 v1 维护线的 v1.107.7 版本，将 v2.52.0 中首次发布的安全修复回移到 v1 分支，对应公告 GHSA-v36g-jcw9-x7cw（中危）：在本地 web\_fetch 工具中转换由攻击者控制的、元素深度嵌套的 HTML 时，可能消耗过多的 CPU 和内存。同一版本还通过 PR \#8842 将 genai-prices 的版本上限限制在 0.1 以下，以保证 token 用量提取和限额功能正常运作。

github · dsfaccini · 9月30日 00:54

<a id="item-8"></a>
### [OpenAI DevDay：ChatGPT 变身平台，推出插件、MCP 与共享工作区](https://the-decoder.com/openais-reveals-a-new-chatgpt-that-looks-less-like-a-chatbot-and-more-like-an-operating-system/) ⭐️ 6.0/10

在 DevDay 活动上，OpenAI 宣布了一系列让 ChatGPT 超越聊天机器人定位的更新：团队共享工作区 Space、文档与幻灯片协作 Pages、包含 MCP Events 与 Team Tasks 工作流自动化的开放 Plugin Extensions 插件系统、可自动生成会议记录的 Meetings 插件、在 Slack 和 Microsoft Teams 中直接通过 @ChatGPT 调用、拥有 32 家合作伙伴的企业市场，以及新的 Pro 500 定价档位。

rss · The Decoder · 9月29日 17:23

<a id="item-9"></a>
### [Claude Code v2.1.285 发布：新增 MCP 安装配置与提供商限制](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) ⭐️ 5.0/10

Claude Code v2.1.285 带来多项 CLI 与配置能力更新：新增 CLAUDE\_CODE\_DISABLE\_WEB\_FETCH 环境变量用于关闭 WebFetch 工具，新增 \`claude --desktop\` 可在当前目录（或通过 \`--continue\` / \`--resume &lt;id&gt;\` 在指定会话上）打开 Claude 桌面应用，新增 \`claude plugin configure &lt;plugin&gt;\` 用于查看插件选项及哪些尚未设置，并可通过 \`--values-stdin\` 从标准输入保存新值。该版本还允许在 \`claude plugin install --config\` 中使用 \`&lt;server&gt;.&lt;key&gt;=&lt;value&gt;\`，从而在安装时配置内置 .mcpb MCP 服务器自身的设置，并新增 allowedProviders 托管设置以限制机器可使用的 API 提供商，以及 CLAUDE\_CODE\_NONSTREAMING\_TIMEOUT\_RETRIES 环境变量来限制超时的非流式回退请求的重发次数；此外还包含大量 bug 修复。

github · ashwin-ant · 9月29日 19:27

<a id="item-10"></a>
### [OpenAI 发布 GPT-6.1 Sol：接近 Astra 的智能，价格仅约五分之一](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 4.0/10

OpenAI 发布了 GPT-6.1 Sol，声称其在 agentic 编码、computer use 和专业工作等任务上接近 GPT-6 Astra 的水平，定价为每百万输入 token 2 美元、每百万缓存输入 token 0.10 美元、每百万输出 token 10 美元，约为 Astra 成本的五分之一。据 Artificial Analysis 报道，该模型距离上一代 GPT-6 Sol 发布仅过去七天就将其取代。

hackernews · AI 热榜 · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)