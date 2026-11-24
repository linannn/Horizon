---
layout: default
title: "Horizon 每日速递：2026-11-24"
description: "AI 精选的技术与研究日报"
date: 2026-11-24
lang: zh
locale: zh-CN
---

> 从 51 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [OpenCode v2.4.0 增加桌面浏览、自动化与视频生成](#item-tech-news-1) ⭐️ 8.0/10
2. [GLM-5.4 引入首个循环 Transformer 编码模型](#item-tech-news-2) ⭐️ 8.0/10
3. [Codex rust-v0.172.0 更新终端、MCP 与审批体验](#item-tech-news-3) ⭐️ 7.0/10
4. [Gemini 4 智能体结合 Lean 改进量子算法](#item-tech-news-4) ⭐️ 7.0/10
5. [Claude 将连接器与技能统一为插件](#item-tech-news-5) ⭐️ 6.0/10
6. [a16z 实测 11,307 次购物智能体运行](#item-tech-news-6) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenCode v2.4.0 增加桌面浏览、自动化与视频生成](https://github.com/anomalyco/opencode/releases/tag/v2.4.0) ⭐️ 8.0/10

**级别**: 核心必看

OpenCode v2.4.0 为桌面端加入内置浏览器，可从 Chrome、Edge、Firefox 或 Safari 导入登录状态和浏览历史，并在持久化配置中让代理读取和控制页面，标签页可在重启后保留。新版还支持代理按一次性、定时器、cron 或 MCP 事件运行提示词、Code Mode 脚本或固定 shell 命令，可通过 \`/automation\` 管理，并用 \`&quot;automations&quot;: false\` 关闭；shell 操作在创建时请求一次批准。当连接的提供商提供视频模型时，\`generate\_video\` 可在后台生成视频、跨服务器重启继续执行并将成品保存到工作区。升级兼容性方面，旧 \`experimental\_image\_generate\` 已更名为 \`generate\_image\`，但已保存的“始终允许”许可不会迁移；GitHub Copilot 不再读取 \`GITHUB\_TOKEN\`，须改用 \`COPILOT\_GITHUB\_TOKEN\` 或 OAuth，TUI 插件依赖的 \`@opentui/core\` 与 \`@opentui/solid\` 须为 0.9.4 或更高，SDK 启动初期还可能返回尚未加载完成的部分插件列表。

github · github-actions\[bot\] · 11月23日 09:22

**「SDK 插件加载的历史变化」** OpenCode v2.2.7 曾让模型、提供商、generate.\*、voice.\* 和 websearch.query 等 SDK 端点等待插件加载最多 5 秒，超时后返回 503。v2.4.0 取消这层等待并恢复后台异步加载，因此客户端在启动初期看到的插件或提供商列表可能为空或不完整，需要通过对应的 \*.updated 事件刷新或自行轮询。

**「升级与权限影响」** 现有用户升级后，依赖旧 \`experimental\_image\_generate\` 权限白名单的流程会再次请求授权，Copilot 集成必须改用 \`COPILOT\_GITHUB\_TOKEN\` 或 OAuth，TUI 插件则需将 \`@opentui/core\` 和 \`@opentui/solid\` 升级至 0.9.4 或更高，否则相关功能可能无法正常加载。启用内置浏览器和自动化的团队还应设置 \`browser\` 拒绝规则或用 \`&quot;automations&quot;: false\` 限制权限，因为代理能够复用持久登录状态，并在创建自动化时仅请求一次批准后按 cron 或 MCP 事件执行 shell 命令。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/anomalyco/opencode/releases/tag/v2.4.0">anomalyco/opencode released v2.4.0</a></li>
<li><a href="https://github.com/anomalyco/opencode/releases">Releases · anomalyco / opencode · GitHub</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#browser-automation`, `#MCP`, `#workflow-automation`

---

<a id="item-tech-news-2"></a>
### [GLM-5.4 引入首个循环 Transformer 编码模型](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

**级别**: 核心必看

Z.ai 宣布推出面向通用编码任务的 GLM-5.4，并称其采用公司首个“loop transformer”（循环 Transformer）架构。开发者可通过 Z.ai Coding Plan 获取该模型；据 Simon Willison 的使用说明，他当时无法在常规 Z.ai API 套餐或 OpenRouter 上使用 GLM-5.4，切换到 Coding Plan 后取得的 API 密钥才可访问该模型。当前材料没有提供基准成绩、上下文长度、定价、吞吐量或延迟数据，因此尚无法据此判断其编码表现及循环计算带来的实际开销。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「循环 Transformer 的基本思路」** 普通 Transformer 在一次前向传播中通常让每层只计算一次；循环 Transformer 则让一组共享权重的层连续迭代多轮，以反复精炼隐藏状态并增加有效计算深度。Z.ai 的官方文档称，GLM-5.4 将 GLM-5 基座模型的 28 层复用于两轮迭代，并称可在不增加参数量的前提下深化推理；这一架构收益属于厂商说明，仍需独立评测验证。

**「编码代理的接入路径」** 开发者当前需通过 Z.ai Coding Plan 使用 GLM-5.4：在 ZCode 中选择 Coding Plan 模板，将 Base URL 配置为 \`api.z.ai/api/anthropic\` 并填入 API key，即可使用 GLM-5.4 和 GLM-5.3-Flash。常规 Model API 仍需等待安全评估完成，因此计划直接接入 Model API 的工作流暂不应假设 GLM-5.4 已全面开放。

**「架构透明度与推理耗时之争」** HarHarVeryFunny 赞赏 Z.ai 公开较多技术细节，认为循环 Transformer 是值得探索的方向；aurareturn 则将其动机解释为缓解推理时权重从 HBM 搬运至芯片所造成的内存带宽瓶颈。lnenad 报告“马拉松式思考”会显著拉长简单任务的完成时间，并质疑这是否足以抵消其接近前沿模型的收益；这是个人体验，而非已测性能结论。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward generalized coding with our first loop transformer</a></li>
<li><a href="https://simonwillison.net/2026/Nov/23/glm-54/">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM-5.4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://zcode.z.ai/en/docs/configuration">Connect GLM models and Coding Plans to use ZCode. | ZCode Docs</a></li>

</ul>
</details>

**标签**: `#AI coding models`, `#coding agents`, `#loop transformers`, `#GLM-5.4`, `#developer APIs`

---

<a id="item-tech-news-3"></a>
### [Codex rust-v0.172.0 更新终端、MCP 与审批体验](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐️ 7.0/10

**级别**: 核心必看

Codex rust-v0.172.0 为终端编码代理工作流新增斜杠命令参数补全，例如可用 \`Tab\` 将 \`/mcp lo\` 补全为 \`/mcp login\`，并支持从搜索结果和对话记录打开已保存会话及嵌套代理。带有缓存工具列表的可选 stdio MCP 服务器现在默认延迟到首次工具调用时启动，开发者还可在 \`config.toml\` 中为各个已连接应用工具指定审批审核者，并在配置或登录时为 app-server 客户端选择 Amazon Bedrock Runtime。\`codex exec resume\` 默认恢复已保存的沙箱权限、工作目录和工作区根目录，除非显式覆盖；远程会话也可在客户端与服务器操作系统不同时保留这些路径。该版本还会即时报告响应流中的提供商错误并指出所触及的 API 消费限额，同时修复父代理轮次被中断后子代理排队回复丢失的问题。

github · github-actions\[bot\] · 11月24日 00:03

**「Codex 版本迁移背景」** rust-v0.172.0 直接承接 rust-v0.171.0，发布说明通过两个版本标签的直接比较界定增量范围。该版本还完成了一项连接层迁移：Code Mode 的所有主机连接统一改用 gRPC，此前作为独立配置项的 \`code\_mode\_host\_grpc\` 设置已被弃用。

**「升级后的配置与兼容性影响」** 对使用 Codex app 和连接工具的团队，升级到 rust-v0.172.0 后可在 \`config.toml\` 中为每个连接工具单独指定审批审核者，将审批责任细化到工具级别。对于带缓存工具列表的可选 stdio MCP 服务器，进程现在默认在首次工具调用时才启动，因此依赖其“启动即运行”的脚本、监控或排障步骤需要围绕首次调用重新验证；此外，\`code\_mode\_host\_grpc\` 已被弃用，配置方不应再把该开关视为可继续依赖的接口。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/openai/codex/releases/tag/rust-v0.172.0">openai/codex released rust-v0.172.0</a></li>
<li><a href="https://whatsnew.fyi/product/codex/releases/rust-v0.172.0">Codex rust-v0.172.0 release notes · What&#x27;s New</a></li>

</ul>
</details>

**标签**: `#OpenAI Codex`, `#coding agents`, `#MCP`, `#developer tools`, `#release`

---

<a id="item-tech-news-4"></a>
### [Gemini 4 智能体结合 Lean 改进量子算法](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/) ⭐️ 7.0/10

**级别**: 核心必看

Google DeepMind 发布论文，提出由多个 Gemini 4 智能体组成的团队与 Lean 形式化定理证明结合，用于改进量子算法，并生成经数学验证的量子电路。团队同时在 GitHub 开源 Lean 库、问题规格和经验证的解法；现有材料未给出智能体协作机制、验证规模或电路性能提升幅度，因此尚无法据此量化成果。

rss · AI 热榜 · 11月23日 16:59

**「形式化证明的含义」** Lean 在这项工作中承担正确性证明层：候选量子算法的性质被写成可由定理证明器检查的定理，只有通过这些证明的解法才属于“形式化验证”后的结果。该流程面向聚变能、化学和酶建模的量子算法，因此证明所保证的是算法与电路规格的数学正确性，并不等同于已经在现实量子硬件上测得运行速度。

**「开源可验证工作流」** 开源的问题规格、Lean 库和验证解法可供研究与开发人员检查、复用这套多智能体量子算法工作流，并据证明结果审查生成电路的正确性。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/">Google DeepMind 用 Gemini 4 智能体团队与 Lean 形式化验证改进量子算法</a></li>

</ul>
</details>

**标签**: `#多智能体`, `#形式化验证`, `#Lean`, `#量子算法`

---

### 更多动态

<a id="item-tech-news-5"></a>
#### [Claude 将连接器与技能统一为插件](https://x.com/claudeai/status/2124970294523945328) ⭐️ 6.0/10

Claude 官方宣布将连接器与技能整合为插件，为 Claude 接入外部工具或教授新技能提供统一入口。该功能现已覆盖 Free、Pro、Max 和 Ultra 套餐，用户可在 claude.ai/plugins 浏览超过 10,000 个插件；Team 和 Enterprise 支持仍处于“即将支持”阶段。

rss · AI 热榜 · 11月23日 20:56

<a id="item-tech-news-6"></a>
#### [a16z 实测 11,307 次购物智能体运行](https://www.a16z.news/p/welcome-to-the-b2a-economy-how-agents) ⭐️ 4.0/10

a16z 与 The Prompting Company 报告了对 Grok Bot、Muse、Instinct、Dots 等购物智能体的行为测试：使用 1,270 条提示词完成 11,307 次完整运行，并将购物表现与 YipitData 消费数据进行比对。当前提供的材料仅概述测试规模，未给出各智能体的具体成绩、评测实现细节，也未列出标题所称的“五条方法”，因此不能据此判断性能优劣或方法能否复现。

rss · AI 热榜 · 11月23日 15:04