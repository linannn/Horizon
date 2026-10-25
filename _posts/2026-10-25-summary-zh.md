---
layout: default
title: "Horizon 每日速递：2026-10-25"
description: "AI 精选的技术与研究日报"
date: 2026-10-25
lang: zh
locale: zh-CN
---

> 从 30 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [Pydantic AI v2.61.0 更新思考配置、引用与工作区隔离](#item-tech-news-1) ⭐️ 7.0/10
2. [MCP Servers v2.1.0 修复三款服务器八项漏洞](#item-tech-news-2) ⭐️ 7.0/10
3. [gpu-unlock 解锁 NVIDIA 3000 系列 FP/BF16 发射率](#item-tech-news-3) ⭐️ 7.0/10
4. [编码代理复杂框架成本最高增至三倍，效果提升有限](#item-tech-news-4) ⭐️ 7.0/10
5. [Kimi K3.1 Pro 发布：2.8T 参数与百万 Token 上下文](#item-tech-news-5) ⭐️ 7.0/10
6. [Battledrones v14 新增四人地图与 WebSocket 联机](#item-tech-news-6) ⭐️ 6.0/10
7. [OpenAI 红队测试称智能体可跨虚拟机传递秘密](#item-tech-news-7) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Pydantic AI v2.61.0 更新思考配置、引用与工作区隔离](https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0) ⭐️ 7.0/10

**级别**: 核心必看

Pydantic AI 已发布 v2.61.0，为 AI 代理开发者加入结构化引用和新模型名称：TextPart 可携带结构化引用，Bedrock、OpenRouter 与 xAI 的引用会被统一规范化并在消息历史中保留，同时新增 kimi-k3.1-pro 和 kimi-k3.1-pro-highspeed。兼容性方面，thinking=False 遇到无法关闭思考的模型时会发送模型可接受的最低思考量，并会在更宽作用域的提供商专用设置覆盖 thinking 时发出警告；CohereModel 工具返回中的文件也不再被静默丢弃，而是抛出 NotImplementedError。该版本还将并发工作区运行固定到各自的 Prefect 环境，修正 pydantic\_graph 中 bool 与 int 输入落入同一 Literal 决策分支的问题，并弃用没有任何 Gemini Live 模型支持的 google\_multi\_speaker。此外，托管 MCP 能力现可使用异步 auth 函数，持久化引擎扩展的操作类型、ParameterTransports、DurableRunContext 和运行身份钩子也已转为公开接口。

github · dsfaccini · 10月24日 03:13

**「相关配置机制」** Pydantic AI 的模型思考配置同时涉及通用 \`thinking\` 参数和提供商专用设置，作用域差异会影响最终采用的配置；托管 MCP 则通过 \`auth\` 函数接入授权流程。\`pydantic\_graph\` 使用 \`Literal\` 区分决策分支，因此保持 \`bool\` 与 \`int\` 输入的类型差异，是图执行逻辑正确分派分支的前提。

**「升级前需验证类型分派与工具返回」** 升级到 v2.61.0 后，使用 \`pydantic\_graph\` 并以 \`Literal\` 区分 \`bool\` 与 \`int\` 输入的应用应重新执行分支回归测试，因为两类输入现在不会再落入同一决策分支。另一个兼容点是 \`CohereModel\` 工具返回包含文件时，调用会抛出 \`NotImplementedError\` 而非静默丢弃文件；相关代码需在上线前显式处理文件载荷，避免升级后出现运行失败。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0">pydantic/pydantic-ai released v2.61.0</a></li>

</ul>
</details>

**标签**: `#pydantic-ai`, `#coding-agents`, `#model-thinking`, `#tool-calls`, `#developer-tools`

---

<a id="item-tech-news-2"></a>
### [MCP Servers v2.1.0 修复三款服务器八项漏洞](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0) ⭐️ 7.0/10

**级别**: 核心必看

MCP Servers v2.1.0 已发布三款安全修复包：\`@modelcontextprotocol/server-filesystem\` 2.0.1、\`@modelcontextprotocol/server-everything\` 2.0.1 和 \`mcp-server-fetch\` 2026.10.24，共修复八项漏洞。filesystem 2.0.1 阻止目录检查与写入之间替换符号链接造成的越界写入，并收紧路径、符号链接及目录列表检查；everything 2.0.1 为 HTTP 和 SSE 传输加入 \`Origin\` 校验并移除通配 CORS；fetch 2026.10.24 统一 IDNA 地址检查与连接所用主机名、拦截封装私网 IPv4 的 NAT64 地址，并在每次重定向后重新检查 robots.txt。受影响版本分别为 filesystem 的 1.0.0 至 2.0.0 及截至 2026.8.31 的日期版本、everything 的 1.0.0 至 2.0.0 及 2025.9.24 至 2026.8.31 的日期版本，以及 fetch 的截至 2026.10.19 版本。filesystem 的符号链接竞态修复在 Linux 和 macOS 上已解决该写入问题，但 Windows 仅部分修复；使用日期版本的 TypeScript 用户还须显式安装 2.0.1，例如运行 \`npm install @modelcontextprotocol/server-filesystem@2.0.1\`，因为包管理器会将语义版本 2.0.1 排在所有 2025.x 和 2026.x 日期版本之后。

github · cliffhall · 10月25日 00:03

**「版本体系背景」** MCP Servers 仓库中的 TypeScript 服务器此前采用 2025.x、2026.x 等日期版本，后来从 1.0.0 起改用语义版本；本次 filesystem 与 everything 的修复版因而标为 2.0.1。npm 的版本排序会把 2025.x 和 2026.x 视为高于 2.0.1，因此依赖普通“升级到最新版”的包管理器不会自动采用这一修复版；Python 的 fetch 服务器仍采用日期版本，本次版本为 2026.10.24。

**「升级要求与 Windows 残余风险」** 部署这三款服务器的组织应将 \`@modelcontextprotocol/server-filesystem\` 和 \`@modelcontextprotocol/server-everything\` 显式升级到 2.0.1，并将 \`mcp-server-fetch\` 升级到 2026.10.24；使用日期版本的 TypeScript 用户必须指定目标版本（例如运行 \`npm install @modelcontextprotocol/server-filesystem@2.0.1\`），否则普通依赖升级不会拉取修复包。filesystem 的目录替换符号链接竞态在 Windows 上仅部分修复，因此升级 2.0.1 仍不能消除该平台的全部风险，需按 GHSA-53mr-w429-c597 的说明配置缓解措施。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0">modelcontextprotocol/servers released v2.1.0</a></li>

</ul>
</details>

**标签**: `#MCP`, `#security fixes`, `#filesystem server`, `#symlink race`, `#developer tools`

---

<a id="item-tech-news-3"></a>
### [gpu-unlock 解锁 NVIDIA 3000 系列 FP/BF16 发射率](https://github.com/Zagitta/gpu-unlock) ⭐️ 7.0/10

**级别**: 核心必看

开源项目 gpu-unlock 利用 NVIDIA 3000 系列显卡启动固件中的漏洞，绕过默认限制并提高 FP/BF16 指令发射率；社区提到的支持型号包括 RTX 4090 和 RTX 4070 Ti Super。这一方法可能改善 LLM 推理等 FP/BF16 密集型任务的性能，但现有材料仅给出定性实测反馈，未提供统一、可复核的吞吐提升数字。部分显卡需要把功耗上限提高到 450W，并会因此产生更高热量和冷却需求，固件利用本身也带来安全风险。

hackernews · fragebogen · 10月24日 09:58 · [社区讨论](https://news.ycombinator.com/item?id=50219700)

**「加载时序决定解锁是否生效」** 该方案必须在 NVIDIA 驱动绑定显卡之前加载 gpu-unlock；否则 nvidia.ko 先绑定设备时，解锁会因 -EBUSY 失败。项目为此将 gpu-unlock 和固件放入 initramfs，并在 mkinitcpio 配置中把它排在 nvidia 之前，以尽量缩短显示设备暂时无输出的时间。

**「部署前需核算 450W 功耗与散热余量」** 对采用 gpu-unlock 的 RTX 4090 或 RTX 4070 Ti Super 用户，固件解锁能提升 FP/BF16 发射率，因而可缓解计算受限型 BF16 负载的指令吞吐瓶颈；但评论者称部分型号要获得完整收益需把功耗上限提高到 450W，这明显高于原厂散热设计余量。部署前应核对电源容量、机箱风道和散热能力，并把固件漏洞利用带来的稳定性风险纳入评估；现有社区反馈没有给出跨型号可复核的统一吞吐增幅。

**「社区认可性能，但强调固件与散热风险」** 项目作者 Zagitta 表示，该项目主要把已有的固件利用封装成无需修改 NVIDIA 驱动的独立启动模块；一名测试者称结果真实，但认为固件利用具有风险。另一名使用消费级硬件从事神经网络研究的用户认为，该解锁对 LLM 等计算受限任务很有价值，不过实际采用仍需权衡功耗、温度和散热条件。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/Zagitta/gpu-unlock">GPU-unlock: FP/BF16 instruction issue rate on Nvidia 3000&#x27;s cards</a></li>
<li><a href="https://github.com/Zagitta/gpu-unlock/issues">Issues · Zagitta/ gpu - unlock · GitHub</a></li>

</ul>
</details>

**标签**: `#NVIDIA 3000-series`, `#FP/BF16`, `#GPU firmware`, `#AI inference`, `#open-source hardware`

---

<a id="item-tech-news-4"></a>
### [编码代理复杂框架成本最高增至三倍，效果提升有限](https://the-decoder.com/fancy-harnesses-make-coding-agents-more-expensive-but-not-better-study-finds/) ⭐️ 7.0/10

**级别**: 核心必看

一项受控研究发现，在 Claude Code、OpenCode 和 mini-SWE-agent 等编码代理框架之间切换，任务通过率相较于使用同一配置重复运行几乎没有明显提升，但单任务成本最高可达到三倍。研究认为，主要成本增量来自每一步都重新发送系统提示词。当前报道未给出研究方法、样本范围和效应量，因此这些结果不应直接外推到所有代理框架或工作负载。

rss · The Decoder · 10月24日 09:21

**「编码代理框架与模型能力的区分」** 这里的“框架”（harness）指承载模型运行并组织代理交互的外围机制，而不是底层模型本身。此前的技术讨论认为框架设计可能显著影响结果：Prismor 提出跨 Claude Code、Codex、Cursor 等代理的框架对齐可能比模型对齐更关键，另一篇围绕 Terminal-Bench 的文章则将模型比作发动机、将框架比作传动和操控系统。这些属于先前的技术观点，而非受控实验结论，构成了本项研究专门比较“切换框架”与“重复同一配置”的背景。

**「选型应同时衡量成本与通过率」** 开发团队选择编码代理框架时，应在自己的工作负载上同时测量任务通过率和单任务 token 成本，而不是默认更复杂的框架能带来更好的结果；若通过率增益不显著，保留更省 token 的现有配置可避免无明确收益的成本放大。由于报道未披露样本范围和效应量，这一结论不应直接外推到所有代理框架。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/fancy-harnesses-make-coding-agents-more-expensive-but-not-better-study-finds/">Fancy harnesses make coding agents more expensive but not better, study finds</a></li>
<li><a href="https://www.prismor.dev/blog/harness-alignment-over-model-alignment">For Coding Agents , Harness Alignment Matters More Than Model...</a></li>
<li><a href="https://kimchi.dev/blog/same-model-different-harness-terminal-bench">Same Model, Different Results: What Actually Separates AI Coding ...</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#agent-harnesses`, `#evaluation`, `#token-cost`, `#system-prompts`

---

<a id="item-tech-news-5"></a>
### [Kimi K3.1 Pro 发布：2.8T 参数与百万 Token 上下文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&amp;mid=2647687627&amp;idx=1&amp;sn=4816c8130f378587885913b465fd686f) ⭐️ 7.0/10

**级别**: 核心必看

月之暗面已发布旗舰模型 Kimi K3.1 Pro，参数规模为 2.8T，支持 100 万 Token 上下文；完整模型权重预计于 11 月 4 日前开放，因此目前仍属于待交付计划。标准版 API 定价为输入每百万 Token 13 元、输出 68 元，据报道较 K3 基本减半；同步推出的 Highspeed 版本输出速度约为 2 至 3 倍，但价格翻倍。现有来源尚未提供开放许可证、模型架构或基准测试细节。

rss · AI 热榜 · 10月24日 02:08

**「K3 与 K3.1 Pro 的技术关系」** 同系列的 Kimi K3 已在官方 Hugging Face 模型页公开，模型卡将其称为原生多模态、具备智能体能力的“开放权重”模型，并列出 2.8T 参数、Kimi Delta Attention（KDA）、Attention Residuals（AttnRes）和 100 万 Token 上下文。因此，K3.1 Pro 的核心规格延续了 K3 已公开的配置；但现有信息尚不能确认 K3.1 Pro 是否沿用相同架构，“完整权重开放”也不等于已经明确采用某项开源许可证。

**「开发者的选型与成本」** 需要百万 Token 上下文的开发者可按标准版每百万 Token 输入 13 元、输出 68 元估算 API 预算；若更看重输出速度，则需权衡 Highspeed 版本约 2 至 3 倍的速度与翻倍价格。计划本地部署的团队仍应等待权重实际开放，并确认许可证与部署要求。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&amp;mid=2647687627&amp;idx=1&amp;sn=4816c8130f378587885913b465fd686f">Kimi 发布开源旗舰模型 K3.1 Pro：2.8T 参数、100万 Token 上下文，实测 3D 与视频动效</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi - K 3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#Kimi K3.1 Pro`, `#开源大模型`, `#长上下文`, `#API定价`

---

### 更多动态

<a id="item-tech-news-6"></a>
#### [Battledrones v14 新增四人地图与 WebSocket 联机](https://simonwillison.net/2026/Oct/24/battledrones/) ⭐️ 6.0/10

Battledrones v14 发布了采用冷色冰原主题的四人地图“Compass Rose”，并让该地图的 WebSocket 非音频多人模式支持最多四名真人玩家；此前地图仅限两人参赛。据作者 Simon Willison 描述，Claude Opus 5.5 根据一段自然语言提示实现了新地图及联机改动，包括新增紫色和绿色机器人队伍、空余玩家槽位由 AI 填充，以及通过分享链接或二维码加入。作者同时提供了启用“Goliath Armada”变种器的四人 AI 战斗回放，其中每队初始拥有四台巨型 Goliath 机体，但未给出代码级验证结果。

rss · Simon Willison · 10月24日 03:59

<a id="item-tech-news-7"></a>
#### [OpenAI 红队测试称智能体可跨虚拟机传递秘密](https://x.com/emollick/status/2114001653879672877) ⭐️ 6.0/10

Ethan Mollick 转述称，OpenAI 红队测试让使用前沿模型的智能体攻击其加固的隔离基础设施，结果智能体几乎在每个受限联网服务中都找到漏洞。测试还显示，智能体能借助类似 Spectre 和 Meltdown 的 CPU 缓存时序侧信道，在不联网、无共享文件的虚拟机之间传递秘密。该信息目前是转述，未披露受影响产品、复现条件或缓解措施，也没有提供独立验证。

rss · AI 热榜 · 10月24日 14:30