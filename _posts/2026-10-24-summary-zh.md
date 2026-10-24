---
layout: default
title: "Horizon 每日速递：2026-10-24"
description: "AI 精选的技术与研究日报"
date: 2026-10-24
lang: zh
locale: zh-CN
---

> 从 58 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [Codex rust-v0.164.0 新增预设提示与企业 MCP 认证](#item-tech-news-1) ⭐️ 8.0/10
2. [Goose v1.56.0 更新子智能体编排与成本处理](#item-tech-news-2) ⭐️ 7.0/10
3. [月之暗面发布 Kimi K3.1 Pro 与 Highspeed API](#item-tech-news-3) ⭐️ 7.0/10
4. [80B 支招反让 9B 准确率下降 23.6 个百分点](#item-tech-news-4) ⭐️ 7.0/10
5. [Claude 为 123 个开源库生成形式化正确性证明](#item-tech-news-5) ⭐️ 7.0/10
6. [Quick Study：Claude Opus 5.5 生成照片绘画工具](#item-tech-news-6) ⭐️ 5.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Codex rust-v0.164.0 新增预设提示与企业 MCP 认证](https://github.com/openai/codex/releases/tag/rust-v0.164.0) ⭐️ 8.0/10

**级别**: 核心必看

OpenAI 已发布 Codex CLI 的 rust-v0.164.0 版本，面向编码代理用户加入 10 个编号的 \`/presets\` 槽位，并可通过 \`/model\` 和 \`/permissions\` 的内联参数直接设置模型、推理强度、速度和权限配置。该版本支持使用符合条件的 Codex 账户授权或专用登录方式认证企业 MCP，包括需要密钥的 OAuth 客户端，并在受支持的远程 Bash 命令和 Zsh 快照会话中遮蔽凭据。Amazon Bedrock 配置向导现已默认启用，并将 API 密钥与其他 AWS 登录方式归组；新版还支持在兼容 Kitty 或 Sixel 的终端中全屏预览图片，并修复压缩失败残留摘要、恢复会话时覆盖已保存设置及 Windows 代理认证等问题。

github · github-actions\[bot\] · 10月23日 04:48

**「既有 Codex CLI 工作流」** Codex CLI 已有终端斜杠命令、模型与权限配置，以及可压缩并恢复的会话历史；rust-v0.164.0 是相对 rust-v0.163.0 的增量版本，主要扩展这些交互面并修正会话状态处理。企业侧也沿用既有的 MCP、AWS 身份和代理连接流程，本版是在其上补充授权、凭据遮蔽和连接故障处理，而非另设一套代理架构。

**「用户影响」** 使用企业 MCP、远程 Bash、Zsh 快照会话或 Amazon Bedrock 的团队，可以减少重复配置提示词和身份接入步骤，并降低凭据在受支持环境中意外暴露的风险。凭据遮蔽仅覆盖发布说明列出的命令和会话类型，并非所有执行路径的通用保证；需要图片预览的开发者也应确认终端支持 Kitty 或 Sixel 图形协议。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/openai/codex/releases/tag/rust-v0.164.0">openai/codex released rust-v0.164.0</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Codex CLI`, `#MCP`, `#developer workflows`, `#credential security`

---

<a id="item-tech-news-2"></a>
### [Goose v1.56.0 更新子智能体编排与成本处理](https://github.com/aaif-goose/goose/releases/tag/v1.56.0) ⭐️ 7.0/10

**级别**: 核心必看

Goose v1.56.0 已发布，主要面向使用 AI 编码助手的开发者改进子智能体编排：可恢复失败或取消的 delegate 子智能体，通过 \`GOOSE\_MAX\_CONCURRENT\_SUBAGENTS\` 限制并发，并在界面中打开子智能体会话的只读链接。该版本还新增自动化思考级别控制、由提供商定义的缓存价格支持和 IO Intelligence 提供商，并以 Boa JavaScript 运行时取代 PCTX code mode；发布说明未提供这些改动的实现细节或性能数据。修复内容涉及 Windows 构建与 NSIS 安装程序、模型目录、上下文长度、OpenAI Responses、ACP、桌面端会话渲染及多种提供商兼容问题。

github · github-actions\[bot\] · 10月23日 15:49

**「既有委派机制」** Goose 现有的委派体系允许主会话启动子智能体，相关实现包括在 GDK 中运行前台子智能体、以全局轮次上限作为子智能体的回退限制，以及为斜杠命令和委派流程加载 recipe 扩展。v1.56.0 在这套架构上补充了生命周期管理和会话观察能力，同时将原有的 PCTX code mode 底层实现替换为 Boa JavaScript runtime。

**「实际影响」** 多智能体开发流程的操作者现在可以恢复中断的委派任务、限制同时运行的子智能体数量，并从界面检查委派会话，从而更直接地控制资源使用和排查执行过程。由于代码模式已从 PCTX 切换到 Boa JavaScript 运行时，依赖 PCTX 集成的团队应检查兼容性；发布说明没有交代迁移方案或兼容性范围。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/aaif-goose/goose/releases/tag/v1.56.0">aaif-goose/goose released v1.56.0</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#subagent orchestration`, `#developer tooling`, `#model reasoning`, `#release notes`

---

<a id="item-tech-news-3"></a>
### [月之暗面发布 Kimi K3.1 Pro 与 Highspeed API](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) ⭐️ 7.0/10

**级别**: 核心必看

截至 2026 年 10 月 23 日，月之暗面已通过 Moonshot API 上线 Kimi K3.1 Pro：标准档每百万输入 token 2 美元、每百万输出 token 10 美元，另有速度为标准档 2–3 倍的 Highspeed 版；Highspeed 收费为标准档两倍，但输入 token 缓存命中价格不变。模型当时尚未开放权重，月之暗面承诺最迟在 2026 年 11 月 4 日发布完整权重；附带 RSS 摘要称其为 3T 级、上下文窗口 100 万 token，但文章正文没有提供编码、工具调用或许可证细节。Moonshot 自测称 Kimi K3.1 Pro 约与 Claude Opus 5.5 和 GPT-6 Astra 相当；Artificial Analysis 给它 55 分，低于 Claude Opus 5.5 的 58 分，但高于 Claude Fable 5.1、GPT-6 Astra 和 Gemini 4 Argon 的 53 分。

rss · Simon Willison · 10月23日 19:40

**「前作 Kimi K3 的技术基础」** Kimi K3.1 Pro 的直接前作是 Kimi K3；MoonshotAI 官方仓库将 K3 描述为已开放权重的原生多模态智能体模型，采用 Kimi Delta Attention（KDA）和 Attention Residuals（AttnRes），总参数量为 2.8T，上下文窗口为 100 万 token。与已经开放权重的 K3 不同，K3.1 Pro 先以 API 形式提供、之后再承诺发布完整权重，因此此次变化涉及同一产品线中新版本的权重发布状态。

**「开发者影响」** 开发者现在可通过 OpenAI 兼容端点使用 \`kimi-k3.1-pro\`；Simon Willison 已用 LLM 0.32 的 \`llm openai endpoint\` 实际调用，并测试了 low、medium、max 三档 reasoning effort。需要自行托管或核验权重的团队则要等待承诺的 11 月 4 日发布，目前也缺少可据以判断使用条件的许可证说明。

**「社区实测与争议」** Plotly 博客作者 chriddyp 称，K3.1 Pro 在其数据分析基准上从 7 月 Kimi K3 的 81% 升至 98%，但因工具调用过多而运行较慢；在一次数据问题排查题中，它执行了 73 次查询，而 GPT-6.1 Sol 为 18 次。另一位评论者援引官方关于开放权重网络攻击能力低于前沿专有模型的说明，质疑 Moonshot 以安全为由限制开放权重；另有订阅者称，99 美元月费方案在一次会话进行 47 分钟后即触及 5 小时配额。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/23/kimi-k31-pro/">Introducing Kimi K3.1 Pro</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-K3">GitHub - MoonshotAI/ Kimi -K3: Open Frontier Intelligence · GitHub</a></li>

</ul>
</details>

**标签**: `#Kimi K3.1 Pro`, `#Moonshot AI`, `#developer APIs`, `#open-weight models`, `#model benchmarks`

---

<a id="item-tech-news-4"></a>
### [80B 支招反让 9B 准确率下降 23.6 个百分点](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247935810&amp;idx=3&amp;sn=4413b0b27aa8331deff0e7f935b3ee46) ⭐️ 7.0/10

**级别**: 核心必看

量子位援引 NeurIPS 2026 一项研究报告称，在该研究的受测设置中，80B 模型向 9B 模型提供建议后，9B 模型的准确率反而下降了 23.6 个百分点。结果说明，多模型协作不能默认“模型越强、建议越有用”，提供的信息是否适配当前任务同样重要。现有材料未交代任务范围、实验方法或缓解方案，因此这一降幅不能直接外推到所有多 Agent 系统。

rss · 量子位 · 10月23日 05:26

**「建议不等于能力增益」** 在多 Agent 的“建议者—执行者”协作中，顾问模型只提供辅助判断，执行者仍负责生成最终答案，因此评估重点应是接入建议后接收模型的端到端任务准确率。参数规模更大或输出信息更多，只能说明供给侧能力或信息量，不能证明这些建议适合接收模型当前的任务与推理条件。

**「协作流程需要验证净收益」** 采用“大模型给小模型支招”的开发者应在接入建议后单独测量最终准确率，不能仅凭模型规模或建议来源判断协作是否有效；具体在哪些条件下会降准以及如何规避，仍需论文方法细节确认。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247935810&amp;idx=3&amp;sn=4413b0b27aa8331deff0e7f935b3ee46">多Agent也会帮倒忙！80B给9B支招，准确率反降23.6个百分点 | NeurIPS&#x27;26</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#cross-model collaboration`, `#AI reliability`, `#LLM evaluation`, `#NeurIPS 2026`

---

<a id="item-tech-news-5"></a>
### [Claude 为 123 个开源库生成形式化正确性证明](https://the-decoder.com/anthropics-claude-now-writes-code-and-proves-it-safe-automatically/) ⭐️ 7.0/10

**级别**: 核心必看

Anthropic 已让 Claude 为 123 个开源库生成形式化正确性证明，产出约 1.8 亿行证明代码；Anthropic 称，Claude 还发现了多年常规测试未能发现的错误。该项目旨在让 AI 辅助的形式化验证像标准测试一样常规，但现有报道没有披露证明方法、覆盖范围或验证结果等关键细节。报道也未说明该能力是否已作为 Claude 产品功能向用户开放，因此目前更适合被视为 Anthropic 报告的研究成果，而非普遍可用的自动代码安全证明功能。

rss · The Decoder · 10月23日 11:32

**「形式化验证与测试的区别」** 形式化验证要求开发者先写出程序应满足的性质，再生成可由证明检查器核验的数学证明；它不同于只覆盖给定输入的常规测试，因此生成证明并不等于代码在所有行为上、尤其是安全性上得到无条件保证。相关报道更具体地将 Claude 的工作描述为验证开源库的安全性质，并称部分缺陷在此前运行“数万亿次”自动化测试后仍未被发现。

**「对代码质量 assurance 的实际影响」** Anthropic 报告的案例表明，Claude 形式化验证可为开源项目补充发现多年常规测试遗漏的缺陷，为维护者增加一条不同于测试的缺陷排查路径。由于报道未说明证明方法、覆盖范围及工具可用性，相关团队应将证明和缺陷报告作为需人工复核的工程输入，而不能据此认定代码已获得全面安全保证。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/anthropics-claude-now-writes-code-and-proves-it-safe-automatically/">Anthropic&#x27;s Claude now writes code and proves it safe automatically</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/claude-formal-verification-software-security">Claude finds bugs that survived trillions of software test runs</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#formal verification`, `#Claude`, `#open-source software`

---

### 更多动态

<a id="item-tech-news-6"></a>
#### [Quick Study：Claude Opus 5.5 生成照片绘画工具](https://simonwillison.net/2026/Oct/23/quick-study-painter/) ⭐️ 5.0/10

Simon Willison 发布了 Quick Study 网页工具：用户打开一张照片后，工具用 canvas 元素和模拟画笔生成绘画版本，提示词要求在几秒内完成。该实现由 Claude Opus 5.5 High 根据一段提示词生成，使用 Sobel 边缘检测，除 Google Fonts 外没有外部库。页面展示了苍鹭照片的模拟油画效果，但没有提供独立基准测试或更广泛效果数据。

rss · Simon Willison · 10月23日 21:35