---
layout: default
title: "Horizon 每日速递：2026-11-21"
description: "AI 精选的技术与研究日报"
date: 2026-11-21
lang: zh
locale: zh-CN
---

> 从 56 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [Inkling 2 Mini：面向本地推理的循环 Transformer](#item-tech-news-1) ⭐️ 7.0/10
2. [Figma 演示 Specs 到 Codex 的开发工作流](#item-tech-news-2) ⭐️ 7.0/10
3. [腾讯混元发布 Hy4 开放权重模型](#item-tech-news-3) ⭐️ 7.0/10
4. [Claude Code v2.1.330 更新企业登录与自托管运行器](#item-tech-news-4) ⭐️ 6.0/10
5. [GitHub Copilot CLI v1.0.115-2 扩展沙箱与模型配置](#item-tech-news-5) ⭐️ 6.0/10
6. [“Agent 版 arXiv”声称 12 周产出近千篇论文](#item-tech-news-6) ⭐️ 4.0/10
7. [Hermes Agent 拟将个人 AI 技巧共享给团队](#item-tech-news-7) ⭐️ 4.0/10
8. [DeepSeek Harness 13 个插件玩法分享](#item-tech-news-8) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Inkling 2 Mini：面向本地推理的循环 Transformer](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

**级别**: 核心必看

Thinking Machines Lab 发布开放权重模型 Inkling 2 Mini，面向需要本地推理的开发者：它采用循环 Transformer，中间 12 层对每个 token 运行 3 次，总参数量为 26.4B、激活参数量为 3.4B，内存占用约 20GB，可在内存至少 32GB 的 Mac 上运行。官方称训练全程使用 NVFP4，Unsloth 已提供可配合 Ollama 和 llama.cpp 使用的 GGUF 版本。发布方同时指出，循环机制改善的是推理行为，并不会增加权重能够存储的事实总量；其 AA-Omniscience 成绩与同规模模型相当，知识密集型基准也不会因更多推理计算而改善。相关性能数字目前主要来自厂商公告，实际场景表现仍待独立复现。

hackernews · AI 热榜 · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「循环层与稀疏激活的区别」** 理解该模型需要区分两种机制：循环 Transformer 会在同一前向传播中重复执行指定中间层，以增加每个 token 的计算深度；混合专家模型（MoE）则通过稀疏激活控制每个 token 实际使用的参数量，两种机制分别关系到计算量与权重容量。本地部署 Inkling 2 Mini 因而需要推理框架支持循环层，并正确处理逐专家 NVFP4 缩放；仅能加载普通 GGUF 文件并不足以保证兼容运行。

**「本地部署与评测成本」** 希望离线运行的开发者可优先测试 Inkling 2 Mini 的 GGUF 路径，并通过 Unsloth Desktop 或 llama.cpp 覆盖 Mac、NVIDIA 和 AMD 设备；部署时应确认所用推理栈支持该模型的循环架构，而不是只验证权重文件能否加载。评测还需计入输出冗余：Artificial Analysis 的 Intelligence Index 测试中，该模型共生成 161M tokens，而同级模型中位数为 85.7M，因此本地运行的计算量和耗时可能明显更高。

**「社区对性能与风险的讨论」** 社区对真实表现持保留态度：montroser 认为，如果基准结果能在现实场景中复现，达到 Qwen3.8-27B 水平将很亮眼，但这属于附带条件的评价；lilytweed 则推测开放模型可能更多采用循环架构，并提出这种架构在高普及度下的安全性和可解释性问题。dofm 称其在 Unsloth“extra high”思考模式下的测试凸显了事实知识未随推理能力同步提升这一限制。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Inkling 2 Mini</a></li>
<li><a href="https://unsloth.ai/docs/models/inkling-2-mini">Inkling 2 Mini - Run Locally Guide | Unsloth Documentation</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling-2-mini">Inkling 2 Mini - Intelligence, Performance &amp; Price... | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#looped transformers`, `#local inference`, `#GGUF`, `#model release`

---

<a id="item-tech-news-2"></a>
### [Figma 演示 Specs 到 Codex 的开发工作流](https://www.figma.com/blog/workflow-lab-specs-and-the-figma-agent/) ⭐️ 7.0/10

**级别**: 核心必看

Figma 在 Workflow lab 中演示了一套端到端工作流：工程师可在 Specs 中汇集 PRD、Hex 数据、FigJam 图、标注后的设计和组件说明，再由 Figma agent 生成供编码智能体使用的实现计划。演示最后通过 Figma MCP 共享计划链接，让 Codex 读取上下文并实现功能；Specs 与 code layers 已面向所有套餐开放 beta。该内容属于厂商工作流演示，未提供实现细节、效果评测或成效数据。

rss · AI 热榜 · 11月20日 22:17

**「从协作画布到智能体工作流」** Figma 最初以支持多人实时编辑同一设计的协作画布为核心，而其官方定位现已扩展为在同一工作空间连接设计、代码与 AI。理解此次演示的关键，是 Specs、Figma agent 与 Figma MCP 分别承接设计资料汇集、任务规划和上下文传递，使编码智能体能直接利用画布中的需求与设计信息。

**「验证 MCP 上下文完整性」** 该工作流的落地门槛是编码智能体能访问 Figma MCP 并打开计划链接；本次演示展示了 Codex，而一篇 Figma–Cursor 实践帖称 Claude 也可经 MCP 读取 token、间距、颜色和组件规范。团队试用其他编码智能体时，应把“是否完整取得 Specs 上下文并保留需求、数据与组件约束”作为验收项；官方未给出准确率、耗时或代码质量评测，因此 beta 结果不宜直接当作生产效果承诺。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.figma.com/blog/workflow-lab-specs-and-the-figma-agent/">Figma 演示用 Specs 与 Figma agent 把上下文变成可实现的开发计划</a></li>
<li><a href="https://en.wikipedia.org/wiki/Figma">Figma - Wikipedia</a></li>
<li><a href="https://www.figma.com/">Figma : The collaborative canvas for design, code, and AI</a></li>
<li><a href="https://www.linkedin.com/posts/davidmaxinran_how-to-set-up-the-figma-cursor-workflow-activity-7439286871265906688-2Ewj">Setting up Figma Cursor workflow with AI | Xinran Ma... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#Figma`, `#AI 编码智能体`, `#MCP`, `#设计转代码`, `#AI 工作流`

---

<a id="item-tech-news-3"></a>
### [腾讯混元发布 Hy4 开放权重模型](https://x.com/TencentHunyuan/status/2123625549147070538) ⭐️ 7.0/10

**级别**: 核心必看

腾讯混元已发布 Hy4 开放权重，定位为原生多模态 MoE 模型，总参数为 770B、激活参数为 49B，并支持 1M 上下文。官方同步发布了包含安全评估报告的 Hy4 System Card，并提供 GitHub、Hugging Face 权重及 GGUF 下载链接；团队计划于本周五美太平洋时间上午 8 点至 10 点在 r/LocalLLaMA 举行 AMA。现有公告未提供性能基准、硬件要求、代码代理集成或实际部署工作流，这些方面仍待验证。

rss · AI 热榜 · 11月20日 03:52

**「MoE 参数口径与预览状态」** MoE（混合专家）模型的“总参数”与“激活参数”是两个不同口径：770B 指模型全部权重规模，49B 指每个 token 实际激活的参数量，后者更接近单次推理的计算负担。腾讯的官方 Hugging Face 条目使用 \`tencent/Hy4-preview\` 标识，并提供在推理库、推理服务商、Notebook 和本地应用中使用该模型的说明，显示当前开放权重仍采用预览版命名。

**「对本地部署的实际影响」** 开发者与组织现在可以下载 Hy4 权重（包括 GGUF）并在自有环境开展部署验证，而不必等待或仅限于托管接口。鉴于官方 Hugging Face 条目仍使用 \`tencent/Hy4-preview\` 标识，且发布公告没有给出硬件需求、基准或实测工作流，团队应先在目标硬件上测量内存/显存占用、延迟和任务质量，再决定是否用于生产环境。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/TencentHunyuan/status/2123625549147070538">腾讯混元开放 Hy4 权重</a></li>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/ Hy 4 -preview · Hugging Face</a></li>
<li><a href="https://kie.ai/blog/what-is-tencent-hy4">What Is Tencent Hy 4 ? 770 B MoE , 1 M Context</a></li>

</ul>
</details>

**标签**: `#Tencent Hunyuan`, `#Hy4`, `#open-weight models`, `#multimodal MoE`, `#1M context`

---

### 更多动态

<a id="item-tech-news-4"></a>
#### [Claude Code v2.1.330 更新企业登录与自托管运行器](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) ⭐️ 6.0/10

Claude Code v2.1.330 已发布：执行 \`claude auth login\` 后，Claude Code 现在会应用 Anthropic Enterprise Admin Console 中所管理组织的设置，并使用该组织的云提供商或网关。新增的内置 mod“easel”可按要求绘制图表，并在 MCP 指标结果下绘图；它支持 Pro、Max，以及可用时的 Team、Enterprise 版本，但仅限 macOS 和 Linux，用户可在 \`/config\` 中关闭自动绘图。该版本还加入完整登录链接开关 \`CLAUDE\_CODE\_FULL\_SIGNIN\_LINK=1\`、自托管运行器的 \`--start-dir\` 与 \`SELF\_HOSTED\_RUNNER\_START\_DIR\`，并改进插件市场错误提示、插件安装 JSON 状态及运行器延迟指标。修复项涵盖长对话压缩和 WebFetch 导致的卡顿、误删其他会话正在使用的 worktree、并发写入导致设置或插件数据丢失，以及多项 MCP、Code Mode 和平台兼容问题。

github · claude-code-publisher\[bot\] · 11月20日 22:32

<a id="item-tech-news-5"></a>
#### [GitHub Copilot CLI v1.0.115-2 扩展沙箱与模型配置](https://github.com/github/copilot-cli/releases/tag/v1.0.115-2) ⭐️ 6.0/10

GitHub 已发布 Copilot CLI v1.0.115-2，集中更新编码代理的沙箱、模型配置、原生扩展和 Browser Use 功能。Windows 沙箱默认允许包查询，可将 sandbox.userPolicy.capabilities 设为 \[\] 关闭；macOS 可通过 sandbox.userPolicy.seatbelt.extraMachLookups 放行特定 Mach 服务，而无需启用 Keychain 访问。/model 现可新增并切换本地会话的自定义提供商模型、管理已配置模型，并加入 Gemini 4 Hydrogen（账户可用时支持 Extra High 推理）、GPT-6.2 Astra 和 MAI-Code-2-Flash；原生扩展也可在调用其声明的斜杠命令时延迟激活。Browser Use 升至 0.2.1，新增会话级标签页、预览显示命名及配套浏览器扩展支持；该版本还修复了 --resume 或 --continue 未应用 --max-ai-credits、空 --available-tools 反而提供全部工具等行为问题。

github · copilot-cli-release-app\[bot\] · 11月20日 14:33

<a id="item-tech-news-6"></a>
#### [“Agent 版 arXiv”声称 12 周产出近千篇论文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247947397&amp;idx=2&amp;sn=4a13a27482d1647338c4b0eec8a1d573) ⭐️ 4.0/10

量子位的一篇标题式预告称，“Agent 版 arXiv”使用 936 个智能体，在 12 周内产出近千篇论文，并同时开展论文同行评议。现有原文只补充“甚至学会了同行打假”，未说明系统的正式名称、生成与评审流程、评测指标、开放获取方式或人工监督条件。由于缺少架构、结果明细和独立验证，文章标题中的数量与评审能力目前只能视为宣传性宣称，不能据此判断这些论文是否达到真实学术出版或同行评审的质量标准。

rss · 量子位 · 11月20日 06:26

<a id="item-tech-news-7"></a>
#### [Hermes Agent 拟将个人 AI 技巧共享给团队](https://the-decoder.com/hermes-agents-collective-wisdom-feature-turns-one-employees-ai-trick-into-the-whole-teams-skill/) ⭐️ 4.0/10

开源 AI 代理 Hermes Agent 计划新增 Microsoft Teams 集成，使企业用户可直接在 Teams 中运行它。其 Collective Wisdom 功能拟把某位员工使用 AI 的技巧转化为整个团队可共享的能力，但目前公告未说明具体实现、发布时间、版本、兼容性或实际效果，因此这仍是待交付功能，而非已证实上线的能力。

rss · The Decoder · 11月20日 09:59

<a id="item-tech-news-8"></a>
#### [DeepSeek Harness 13 个插件玩法分享](https://x.com/Khazix0918/status/2123627885730951241) ⭐️ 4.0/10

在 DeepSeek Harness 发布 100 天之际，卡兹克分享了 13 个围绕该工具的插件玩法，供关注其插件扩展方式的开发者参考。现有转述正文只给出数量和主题，没有列出插件名称、配置步骤、适用场景或效果测试，因此无法据此判断各项玩法的具体能力、兼容性或可复现性。

rss · AI 热榜 · 11月20日 04:01