---
layout: default
title: "Horizon 每日速递：2026-09-11"
description: "AI 精选的技术与研究日报"
date: 2026-09-11
lang: zh
locale: zh-CN
---

> 从 59 条内容中筛选出 8 条重要资讯。

---

1. [DeepSeek 发布 V4.1-Flash，把智能体 KV 缓存内存降至四分之一](#item-1) ⭐️ 8.0/10
2. [Shopify 将移动应用从 React Native 迁回 Swift 和 Kotlin](#item-2) ⭐️ 7.0/10
3. [Cursor 推出 Projects：协调者智能体调度数千个子智能体](#item-3) ⭐️ 7.0/10
4. [OpenAI Codex Python SDK v0.154.0 新增 max/ultra 推理档位与外部消息注入](#item-4) ⭐️ 6.0/10
5. [Cognition 发布 SWE-2 编程模型，对标 Fable 5.1 与 GPT-Astra](#item-5) ⭐️ 6.0/10
6. [OpenAI 面向开发者发布 GPT-Live-1 全双工语音 API](#item-6) ⭐️ 6.0/10
7. [GitHub 开放 AI Scan 拉取请求 API 公开预览](#item-7) ⭐️ 4.0/10
8. [GitHub Copilot 应用入门教程：用 diff、终端和浏览器审查智能体代码](#item-8) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 V4.1-Flash，把智能体 KV 缓存内存降至四分之一](https://the-decoder.com/new-deepseek-model-v4-1-flash-cuts-memory-needs-for-ai-agents/) ⭐️ 8.0/10

**级别**: 核心必看

DeepSeek 发布了 V4.1-Flash：一个 552B 参数的多模态 MoE 模型，采用 MIT 许可证，支持 1M token 上下文窗口，prefill 阶段约激活 8B 参数、decode 阶段约激活 16B 参数，每 token 的 KV 缓存从 V4-Flash 的 3514 字节降至约 890 字节。官方称其在 DeepSWE 编程基准上以微弱优势超过 Opus 5 和 GPT-5.6 Sol，硅基流动也在 Day 0 同步上线了该模型。 由于 KV 缓存是维持长时间运行的编程与工具调用智能体存活的主要内存开销，缓存降至四分之一会直接降低自托管所需硬件门槛和每 token 的推理成本，从而强化开源权重模型在智能体场景中相对闭源前沿 API 的竞争力。 官方给出的降幅并非单一数字：多个来源分别提到其 HBM 上的 KV 缓存约为 V4-Flash 的四分之一、SSD 占用约为其八分之一；而与 Opus 5、GPT-5.6 Sol 在 DeepSWE 上的对比属于厂商公布的评测，同时激活参数量在 prefill（约 8B）与 decode（约 16B）之间并不相同。

rss · The Decoder · 9月10日 12:40

**背景**: 在 Transformer 推理中，KV 缓存会保存此前每个 token 的 key 和 value 状态，避免模型重复计算；它随上下文长度线性增长，因此长时智能体会话的瓶颈往往是内存而非算力。这类 MoE 模型总参数量很大，但每个 token 只经过少数专家子网络，因此真正决定单 token 计算量的只是激活参数。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/new-deepseek-model-v4-1-flash-cuts-memory-needs-for-ai-agents/">New Deepseek model V4.1-Flash cuts memory needs for AI agents</a></li>
<li><a href="https://www.techtimes.com/articles/327163/20260910/deepseek-v41-flash-cuts-agent-memory-costs-fourfold-new-architecture.htm">DeepSeek V4.1-Flash Cuts Agent Memory Costs Fourfold With New Architecture</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#ai-model-release`, `#kv-cache`, `#open-source`, `#coding-agents`

---

<a id="item-2"></a>
## [Shopify 将移动应用从 React Native 迁回 Swift 和 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 7.0/10

**级别**: 核心必看

Shopify 发布工程博客，宣布将其所有移动应用从 React Native 迁回原生 Swift 和 Kotlin，理由是 AI 编码智能体改变了“把应用构建两遍”的成本。这推翻了该公司 2020 年提出的“React Native 是 Shopify 移动端未来”的立场，而该立场在 2025 年 1 月题为《Shopify 使用 React Native 的五年》的文章中还被再次确认。 这直接挑战了跨平台框架的核心卖点——避免在 iOS 和 Android 上重复开发——并表明编码智能体可能正在改变大型工程团队在“共享代码库”与“双端原生维护”之间的成本权衡。 Shopify 给出的核心理由是：编码智能体能够生成并维护重复实现，从而降低了维护两个原生代码库的成本，因此这次迁址本质上是对 LLM 持续进步的押注，而非对原生平台本身的偏好。

hackernews · AI 热榜 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的跨平台框架，允许开发者用 JavaScript/TypeScript 编写移动应用并在 iOS 和 Android 之间共享代码；Shopify 曾是其生态的重要贡献者，贡献了 React Native Skia、FlashList 和 Restyle 等项目。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Shopify is moving from React Native back to Swift and Kotlin</a></li>
<li><a href="https://dev.to/jamilxt/shopify-is-moving-its-mobile-apps-back-to-native-coding-agents-made-it-cheaper-to-build-twice-than-4bf9">Shopify Is Moving Its Mobile Apps Back to Native. Coding ...</a></li>
<li><a href="https://codewithbeto.dev/blog/is-react-native-dead-shopify-native">Is React Native Dead? What Shopify&#x27;s Move to Native Actually ...</a></li>

</ul>
</details>

**社区讨论**: 讨论整体偏支持原生，一位 iOS 工程师称这条消息让自己“深感认同”，还有评论者表示用 OpenAI 的 Codex 和 Maestro 工具在一晚上就完成了约 15-20 个屏幕的小型应用从 React Native 到原生的迁移，之后只花了几天做细节打磨。也有人反驳“是 LLM 才让迁移变得可行”的说法：一位评论者称自己在 2026 年 1 月之前、未借助 LLM 就完成了中型迁移的大部分技术工作；另一位则认为，跨 JS、C++ 和原生线程调试崩溃的成本高于维护两个代码库。

**标签**: `#React Native`, `#Swift/Kotlin`, `#AI coding agents`, `#mobile development`, `#Codex`

---

<a id="item-3"></a>
## [Cursor 推出 Projects：协调者智能体调度数千个子智能体](https://cursor.com/blog/projects) ⭐️ 7.0/10

**级别**: 核心必看

Cursor 发布 Projects（beta）功能，其中协调者智能体自身不写代码，而是调度数千个子智能体并行执行功能开发、迁移和持续性维护等大型开发工作。 这标志着 AI 编程工具从单次会话辅助转向多智能体协同编排的工作流，会直接影响团队如何界定、审查并信任大规模自动化代码变更。 Cursor 将 Projects 标注为 beta，且公告摘要未给出基准测试结果、定价、上下文窗口限制或可用范围等细节，因此“调度数千个子智能体”这一说法目前尚无法被独立验证。

rss · AI 热榜 · 9月10日 12:00

**背景**: 多智能体编排是一种已有实践模式：由一个中央协调者把复杂任务拆解并分派给专门的智能体，而不是让单一智能体包办全部工作。Cursor 是广泛使用的 AI 编程工具，其智能体此前的运作方式主要局限在单次编辑会话内。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://cursor.com/blog/projects">Cursor 推出 Projects：协调者智能体管理数千个子智能体处理大型开发任务</a></li>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>

</ul>
</details>

**标签**: `#Cursor`, `#coding-agents`, `#multi-agent-orchestration`, `#AI-coding-tools`, `#developer-tools`

---

## 更多动态

<a id="item-4"></a>
### [OpenAI Codex Python SDK v0.154.0 新增 max/ultra 推理档位与外部消息注入](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 6.0/10

OpenAI 发布 openai-codex Python SDK v0.154.0（可通过 \`pip install --upgrade openai-codex==0.154.0\` 安装，需 Python 3.10 及以上，并配套 \`openai-codex-cli-bin==0.154.0\` 运行时），新增 \`max\` 与 \`ultra\` 两档 reasoning-effort 取值，以及在同步和异步 \`run\(\)\`、\`turn\(\)\` 调用中使用的 \`ExternalMessage\` 类型。同一版本还在 resume/fork 上新增 \`include\_turns\`，为单个新启动的 turn 提供 \`turn\_service\_tier\` 选项，并加入 \`source\` 元数据。

github · aibrahim-oai · 9月10日 19:51

<a id="item-5"></a>
### [Cognition 发布 SWE-2 编程模型，对标 Fable 5.1 与 GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 6.0/10

Cognition 于 2026 年 9 月 10 日发布 SWE-2，称其是公司迄今最强的编程模型：它在 Moonshot AI 的 Kimi K3（2.8 万亿参数）基础上做后训练，并在同一次强化学习运行中训练出 medium、high、max 三档推理强度。Cognition 声称在 FrontierCode 1.1 Main 和 DeepSWE 1.1 上，SWE-2 在得分和成本两方面都优于 SWE-1.7 与 Grok 4.6，能以远低于 GPT-5.6 Sol 和 Fable 5/5.1 的价格达到相当水平，并以四分之一的成本逼近 GPT-6 Astra。

hackernews · seelos · 9月10日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49645443)

<a id="item-6"></a>
### [OpenAI 面向开发者发布 GPT-Live-1 全双工语音 API](https://the-decoder.com/openais-gpt-live-1-api-lets-developers-build-apps-that-talk-and-listen-at-the-same-time/) ⭐️ 6.0/10

OpenAI 在其开发者 API 中发布了 GPT-Live-1，这是一款能够同时听与说的全双工语音模型，此前已先行在 ChatGPT 用户中推出。它在交互性测试中得分 80.1%，高于前代模型的 45.4%，定价为每分钟 0.05 美元。

rss · The Decoder · 9月10日 17:47

<a id="item-7"></a>
### [GitHub 开放 AI Scan 拉取请求 API 公开预览](https://github.blog/changelog/2026-09-10-ai-scan-for-pull-request-apis-in-public-preview) ⭐️ 4.0/10

GitHub 发布了处于公开预览阶段的 REST API 端点，允许团队在组织和仓库两个层级上管理拉取请求的 AI Scan 启用状态，从而可以以编程方式而非通过界面开启该功能。该更新日志本身只是简短预告，并未列出端点名称、请求与响应结构、速率限制或迁移指南。

rss · GitHub Changelog · 9月10日 20:20

<a id="item-8"></a>
### [GitHub Copilot 应用入门教程：用 diff、终端和浏览器审查智能体代码](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/) ⭐️ 4.0/10

GitHub 发布了一篇面向初学者的教程（属于其 Copilot 入门系列视频），介绍如何在 GitHub Copilot 应用内并排查看 diff、运行终端命令以及预览 Web 应用，从而无需在多个标签页之间来回切换就能审查 AI 智能体生成的改动。文中并未发布新功能、新版本或配置变更，属于教学类内容。

rss · GitHub AI &amp; ML · 9月10日 21:31