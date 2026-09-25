---
layout: default
title: "Horizon 每日速递：2026-09-25"
description: "AI 精选的技术与研究日报"
date: 2026-09-25
lang: zh
locale: zh-CN
---

> 从 45 条内容中筛选出 4 条重要资讯。

---

1. [Mastra 1.69.0 发布：一等公民分类器、默认失败关闭策略门控与后台工具](#item-1) ⭐️ 7.0/10
2. [Whiteboard：人类与 AI 智能体共同设计软件的开源 IDE](#item-2) ⭐️ 7.0/10
3. [Cline SDK v0.0.86 为本地服务器新增 max-tokens 压缩重试恢复机制](#item-3) ⭐️ 6.0/10
4. [GitHub Security Lab 基于 Taskflow Agent 发布 AI 模糊测试任务流](#item-4) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [Mastra 1.69.0 发布：一等公民分类器、默认失败关闭策略门控与后台工具](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0) ⭐️ 7.0/10

**级别**: 核心必看

Mastra 发布了 @mastra/core@1.69.0，开发者可通过 new Mastra\(\{ classifiers \}\) 将分类器注册为一等公民实体，并配有完整的管理 API（getClassifier、listClassifiers、addClassifier、removeClassifier 等）；同时新增 ClassifierProcessor，对智能体的输入、输出与流式内容套用类型化分类器策略，并引入 context.background.adopt\(\{ completion, cancel \}\) 这一原生后台工具执行机制。配套的 @mastra/connect@0.3.0 新增十个自动生成的 SaaS 工具提供方，覆盖 Slack、GitHub、Google Mail/Calendar、Fireflies、PostHog、Stripe、Discord、Twitter/X 与 HubSpot。 这些新增能力把安全门控与长时工具执行从应用层的临时拼接下沉到智能体框架内部，为 TypeScript 开发者提供了策略执行与异步任务的原生原语。 有两点需要注意：默认失败关闭属于行为变更，必须显式配置 errorStrategy: &\#x27;warn&\#x27; 才能恢复此前的失败开放行为；而被 adopt 的后台句柄仅保存在内存中，进程重启后正在进行的后台操作不会恢复。

github · PaulieScanlon · 9月24日 06:58

**背景**: Mastra 是一个用于构建 AI 智能体与工作流的开源 TypeScript 框架，定位为 TypeScript 原生方案，主要面向已经在 JavaScript 生态中开发的团队，而非 Python 优先的工具链。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.69.0">mastra-ai/mastra released @mastra/core@1.69.0</a></li>
<li><a href="https://mastra.ai/docs/agents/processors">Mastra Docs</a></li>
<li><a href="https://github.com/mastra-ai/mastra/releases">Releases · mastra-ai/mastra</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#agent framework`, `#Mastra`, `#developer tools`, `#policy enforcement`

---

<a id="item-2"></a>
## [Whiteboard：人类与 AI 智能体共同设计软件的开源 IDE](https://github.com/devdotfast/whiteboard) ⭐️ 7.0/10

**级别**: 核心必看

由 Sid、Alex、Ketan 和 Milan 四人组成的团队发布了 Whiteboard：一款基于 CodeOSS 构建、以 MIT 许可证开源的桌面应用，可接入 Claude Code、Codex 等智能体，并通过 SDK 让智能体在应用内画布上绘图。该版本包含用 Rust 编写的、基于 AST 的语义化 diff 查看器（配有 WASM 插件系统），支持点击时序图、ER 图或智能体轨迹片段直接跳转到对应代码，还提供 Decision Log，让智能体查询并关联自身轨迹，方便用户了解其自主做出的决策。 随着智能体编程工具让团队合并的代码量远超其实际阅读能力，Whiteboard 瞄准由此产生的“认知债务”，把架构与规格层面的评审变成共享的可视化工作区，而不是只能被动接受或拒绝的纯文本计划。团队表示，包括 Salesforce 和 Modal 在内的公司已在使用它评审架构或规格层面的变更。 根据团队在讨论中的回复，Whiteboard 目前无法在应用内直接编辑文件，因此它更像是与现有编辑器并存的架构与评审层，而非完整的替代型 IDE；而且目前可下载的桌面版本仅支持 macOS。

hackernews · sidharthkmenon · 9月24日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=49833867)

**背景**: Claude Code、OpenAI 的 Codex CLI 等现代 AI 编程智能体主要在终端中运行，自行编辑文件并执行命令。Whiteboard 团队表示，他们从技术主管岗位离职后，发现一边追求智能体编程的速度、一边维持可理解的代码库越来越困难，于是先为自己开发了这款工具。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/devdotfast/whiteboard">Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design</a></li>
<li><a href="https://news.ycombinator.com/item?id=49833867">Show HN: Whiteboard (YC W26) – An open-source IDE for ...</a></li>

</ul>
</details>

**社区讨论**: 评论区总体反应积极：有人预言这种流式图表演示动画会在 12 个月内成为普遍做法，也有人认为它确实解决了真实痛点——相比当前编程智能体的 Plan Mode，它提供了更可视化、可逐步来回协作的替代方案。有用户建议支持关联并评论 GitHub PR，以便用作评审工具；也有评论者质疑，既然不能在应用内编辑文件，它是否还能算作 IDE。另有一条关于仅支持 macOS 的抱怨被评论者本人更正为误会。

**标签**: `#AI coding tools`, `#coding agents`, `#open-source`, `#developer tools`, `#software design`

---

## 更多动态

<a id="item-3"></a>
### [Cline SDK v0.0.86 为本地服务器新增 max-tokens 压缩重试恢复机制](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.0.86) ⭐️ 6.0/10

Cline 发布 SDK v0.0.86：对于在输出 token 上限处被截断的纯文本回合，现在会在既有的 nudge-and-retry 恢复之前，每次运行先执行一次 compact-and-retry 尝试，并新增了 \`task.max\_tokens\_recovery\` 生命周期事件，包含 \`started\`、\`retried\`、\`failed\` 三种状态。该版本还改进了 hub 启动错误报告、让通过 hub 进行的会话重命名得以持久化、把终态会话错误持久化以便恢复时展示、将插件斜杠命令抽到 \`@cline/core\` 的共享服务 \`createPluginCommandService\`、让端点自有 provider 的模型列表失败得以向上传递，并使中止操作在空响应退避期间立即生效。

github · github-actions\[bot\] · 9月24日 05:43

<a id="item-4"></a>
### [GitHub Security Lab 基于 Taskflow Agent 发布 AI 模糊测试任务流](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/) ⭐️ 4.0/10

GitHub 发布博文，介绍基于 GitHub Security Lab Taskflow Agent 构建的全新 Fuzzing Taskflow，该 Agent 是一个以声明式 YAML 任务流来编写 LLM 驱动安全自动化的框架。这条模糊测试流水线面向 C/C++ 项目，已发布在 GitHubSecurityLab/seclab-taskflows-fuzzing 仓库中，据称可由 Agent 端到端执行。

rss · GitHub AI &amp; ML · 9月24日 18:26