---
layout: default
title: "Horizon 每日速递：2026-08-13"
description: "AI 精选的技术与研究日报"
date: 2026-08-13
lang: zh
locale: zh-CN
---

> 从 41 条内容中筛选出 6 条重要资讯。

---

1. [Zed 推出 Delta：实时多人协作编码与可审阅的 AI 对话](#item-1) ⭐️ 8.0/10
2. [Agent Plugins 1.0 登陆 VS Code、Copilot CLI 和 Copilot 应用](#item-2) ⭐️ 8.0/10
3. [Goose v1.46.0 发布：新增展开式代理循环、流式 Shell 输出与用量统计](#item-3) ⭐️ 7.0/10
4. [DeepSeek V4 Pro 0813 登陆 OpenRouter，编码智能体价格低廉](#item-4) ⭐️ 7.0/10
5. [AI 生成的代码变得过于复杂，团队无法调试](#item-5) ⭐️ 6.0/10
6. [OpenAI 推出 Linux 版 ChatGPT 桌面应用（预览版）](#item-6) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Zed 推出 Delta：实时多人协作编码与可审阅的 AI 对话](https://zed.dev/blog/introducing-delta) ⭐️ 8.0/10

**级别**: 核心必看

Zed 宣布推出 Delta，这是一种实时协作式多人编码功能，可将 AI 代理的对话变为可审阅的文档。该公告将 Delta 定位为即将推出的 DeltaDB 存储引擎的起点，DeltaDB 之后也会集成到 Zed 主编辑器中。 通过将评审从提交后的拉取请求转移到实时代理对话，Delta 可能重新定义团队监督并信任 AI 辅助开发的方式。 其核心设计论点是：拉取请求过晚才将讨论附加到代码上，因此 Delta 将代理的工作对话本身作为评审单元。

hackernews · khy · 8月12日 18:19 · [社区讨论](https://news.ycombinator.com/item?id=49276574)

**背景**: 传统上，代码评审是在开发人员完成代码并推送之后通过拉取请求进行的。随着 AI 代理越来越多地编写代码，Zed 正在探索新的原语，用来评审的不仅是最终差异，还有其背后的推理和过程。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://zed.dev/blog/introducing-delta">Delta</a></li>
<li><a href="https://runtimewire.com/article/zed-deltadb-version-control-agent-conversations">Nathan Sobo&#x27;s Zed takes aim at pull requests with... - RuntimeWire</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者的观点存在分歧。一些人质疑实时多人编辑的价值，认为编码是单人活动，而且 AI 对代码的总结冗长且不可靠。另一些人则认为这个概念在指导初级开发人员和追踪有问题的 PR 如何产生方面很有前景，因为可以直接检查生成该 PR 的代理对话。

**标签**: `#AI coding tools`, `#Zed`, `#collaborative editing`, `#AI agents`, `#developer tools`

---

<a id="item-2"></a>
## [Agent Plugins 1.0 登陆 VS Code、Copilot CLI 和 Copilot 应用](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app) ⭐️ 8.0/10

**级别**: 核心必看

8 月 6 日，GitHub 与 AWS、Anysphere、Microsoft、OpenAI 和 Vercel 共同发布了 Agent Plugins 1.0 规范。开发者现在可以一次性构建插件，并在 VS Code、Copilot CLI、Copilot 应用及其他兼容的 agent 客户端中使用。 这次发布将 AI 编码 agent 的扩展方式标准化，让工具开发者只需维护一个插件而无需为每个客户端分别集成，从而推动整个 agent 生态的发展。 每个插件包都通过指向 1.0 schema 的 plugin.json 清单来描述，Copilot Business 和 Enterprise 客户可以在 managed-settings.json 中使用 enabledPlugins 来自动安装或阻止特定插件。

rss · GitHub Changelog · 8月12日 18:39

**背景**: Agent 客户端是指 VS Code 和 Copilot CLI 这类编码工具，AI agent 可以在其中自主读取、编写和修改源代码。Agent 插件是给这些 agent 增加技能、hooks 或其他能力的可分发包，新的 1.0 规范为打包这些插件定义了最小标准。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app">Agent Plugins 1.0 in VS Code, Copilot CLI, and the Copilot app</a></li>
<li><a href="https://code.visualstudio.com/docs/agents/overview">Build with agents in VS Code</a></li>
<li><a href="https://github.com/microsoft/vscode/issues/330114">Agent Host doesn&#x27;t discover hooks from installed plugins ...</a></li>

</ul>
</details>

**社区讨论**: 该更新日志没有附带评论区，但发布后有人提交了一个 GitHub issue，报告 VS Code Agent Host 无法发现已安装插件中的 hooks，而 Copilot CLI 能正确加载相同的插件文件。这表明早期用户已经在测试跨客户端行为，并发现了一些尚待完善之处。

**标签**: `#Agent Plugins`, `#Copilot`, `#VS Code`, `#Agent Ecosystem`, `#Developer Tools`

---

<a id="item-3"></a>
## [Goose v1.46.0 发布：新增展开式代理循环、流式 Shell 输出与用量统计](https://github.com/aaif-goose/goose/releases/tag/v1.46.0) ⭐️ 7.0/10

**级别**: 核心必看

Goose v1.46.0 引入了展开式代理循环、采用仅追加轮次上下文与声明式缓存语义的缓存安全请求组装，以及命令运行时的流式 Shell 输出。它还增加了按消息统计用量（token、成本、TTFT、tok/s）的界面，并带来可调整大小侧栏、单选询问交互菜单以及 /goal、/status、/model 等新斜杠命令。 对于把 Goose 当作自主编程代理使用的开发者来说，这些改动意义重大：缓存友好的请求组装让长时间运行的会话更快、更省钱，而新的用量遥测则让用户清楚看到 token 与成本消耗。 在底层实现上，该版本还为 OpenTelemetry 输出补充了 GenAI 语义约定属性，以 Anthropic 和 Google 格式转发图像及 MCP 内嵌资源 blob，并支持通过 ACP session/new 的 \_meta.hidden 标记创建隐藏会话。

github · github-actions\[bot\] · 8月12日 16:05

**背景**: Goose 是一个开源、可扩展的 AI 代理，运行在用户本机上，隶属于 Linux 基金会旗下的 Agentic AI Foundation（AAIF）。“代理循环”（agent loop）是协调用户输入、模型推理与工具执行的核心逻辑，而“展开”（unrolling）该循环通常意味着让反复的工具调用迭代更加显式、更易于优化。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/aaif-goose/goose/releases/tag/v1.46.0">aaif-goose/goose released v1.46.0</a></li>
<li><a href="https://goose-docs.ai/">goose | Your open source AI agent</a></li>
<li><a href="https://openai.com/index/unrolling-the-codex-agent-loop/">Unrolling the Codex agent loop | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI coding agent`, `#release`, `#goose`, `#LLM tooling`, `#telemetry`

---

<a id="item-4"></a>
## [DeepSeek V4 Pro 0813 登陆 OpenRouter，编码智能体价格低廉](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 7.0/10

**级别**: 核心必看

DeepSeek V4 Pro 0813 是 DeepSeek 旗舰模型 V4 Pro 的正式发布版本（GA 版本），现已上线 OpenRouter，输入价格每百万 token 0.435 美元，输出价格每百万 token 0.87 美元。该模型于 2026 年 8 月 12 日发布，支持 1,048,576 token 的上下文窗口，最大输出 384,000 token。 由于社区测试显示，它驱动编码智能体的成本大约只有 Grok 4.6 等竞品的十分之一，因此该发布可能显著改变开发者在对成本敏感的 AI 编程工作流中的选型。 在一项针对同一功能的 Codex CLI 直接对比中，DeepSeek V4 Pro 0813 用时 12 分 02 秒、花费 0.12 美元，但存在 bug；而 Grok 4.6 用时 3 分 18 秒、花费 1.41 美元，且没有 bug。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家以开放权重模型著称的中国 AI 公司；V4 Pro 是其旗舰级大规模混合专家（MoE）模型，参数规模约 1.6T，自 2026 年 4 月底以来一直以预览版运行，直到本次 0813 正式版发布。OpenRouter 是一个通过统一 API 提供多个大模型的平台，方便用户直接对比成本和基准性能。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424/">DeepSeek V 4 Preview Release | DeepSeek API Docs</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek -ai/ DeepSeek - V 4 - Pro · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区整体对性价比持正面评价：一位用户表示在流量模拟/分布式物理引擎上跑了一整天、花费约 12.50 美元，结果令人满意；另一位用户则对之前的 Flash 更新表示赞赏。主要保留意见包括：一项直接对比中 DeepSeek 虽然更便宜但留下了 bug，以及有评论者批评链接指向 OpenRouter 页面信息太少，不如官方 API 文档或基准帖子。

**标签**: `#deepseek`, `#model-release`, `#ai-coding`, `#cost-analysis`, `#openrouter`

---

## 更多动态

<a id="item-5"></a>
### [AI 生成的代码变得过于复杂，团队无法调试](https://simonwillison.net/2026/Aug/12/florian-herrengt/) ⭐️ 6.0/10

Simon Willison 的网站发布了一段引自 Florian Herrengt 博客文章《AI 正在移除软件工程的中产阶级》的摘录，描绘了一个 AI 辅助项目变得极其复杂、以至于没有开发者能理解或修复的场景。这段轶事描述了一个团队反复让 AI 修复反复出现的 bug，结果发现连 AI 助手 Fable 也无法解决。

rss · Simon Willison · 8月12日 15:08

<a id="item-6"></a>
### [OpenAI 推出 Linux 版 ChatGPT 桌面应用（预览版）](https://the-decoder.com/openai-launches-chatgpt-desktop-app-for-linux/) ⭐️ 4.0/10

OpenAI 宣布推出 Linux 版 ChatGPT 桌面应用，目前为预览版本。该应用将 ChatGPT、Work 和 Codex 整合到一个原生的 Linux 客户端中。

rss · The Decoder · 8月12日 11:53