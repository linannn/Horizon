---
layout: default
title: "Horizon 每日速递：2026-11-16"
description: "AI 精选的技术与研究日报"
date: 2026-11-16
lang: zh
locale: zh-CN
---

> 从 31 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [美团发布 LongCat-2.5 智能体模型权重](#item-tech-news-1) ⭐️ 7.0/10
2. [browser-use 1.0.6 默认切换至 BU 4.0](#item-tech-news-2) ⭐️ 6.0/10
3. [datasette-apps 0.4a0 增加应用间链接](#item-tech-news-3) ⭐️ 6.0/10
4. [datasette-agent 0.6a0 新增首页代理提问与哈希引用](#item-tech-news-4) ⭐️ 6.0/10
5. [1.4M 纯 HTML Three.js 游戏生成拆解](#item-tech-news-5) ⭐️ 6.0/10
6. [Anthropic 称并行 Claude 代理同仓库协作或更差](#item-tech-news-6) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [美团发布 LongCat-2.5 智能体模型权重](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 7.0/10

**级别**: 核心必看

美团已发布面向 AI 智能体的 LongCat-2.5 模型权重；该模型拥有 1.6 万亿参数，并称训练全程使用中国硬件。按美团公布的 Terminal Bench 成绩，LongCat-2.5 得分 88.4，略低于 Claude Opus 5；示例部署运行在 194 枚华为升腾芯片上。报道没有提供许可证、模型架构或具体实现细节，也未列出英伟达 GPU 的使用情况。

rss · The Decoder · 11月15日 10:06

**「背景」** LongCat-2.5 被定位为面向任务执行的 AI 智能体模型，Terminal Bench 则用于衡量智能体在终端环境中完成任务的表现。当前披露只给出了 88.4 分及其与 Claude Opus 5 的相对位置，没有说明测试设置或训练方法。

**「影响」** 对于需要在中国硬件上运行智能体的团队，公开权重及 194 枚升腾芯片的示例提供了一条可评估的非英伟达部署路径；开发者仍需先确认商用许可、硬件需求和测试结果能否复现。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/">Meituan releases a 1.6-trillion-parameter agent model that never touched an Nvidia GPU</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#released model weights`, `#Terminal Bench`, `#Huawei Ascend`, `#AI infrastructure`

---

### 更多动态

<a id="item-tech-news-2"></a>
#### [browser-use 1.0.6 默认切换至 BU 4.0](https://github.com/browser-use/browser-use/releases/tag/1.0.6) ⭐️ 6.0/10

browser-use 1.0.6 已发布；未显式指定 \`llm\` 时，\`Agent\(task\)\` 与 \`ChatBrowserUse\(\)\` 会从原先的 \`bu-fast\` 改为在 Browser Use 网关上运行 \`bu-4.0\`。默认模式下，\`bu-4.0\` 的输入与输出 token 价格分别为每 100 万 token 1.80 美元和 9.00 美元，均为 \`bu-fast\` 的 15 倍，后者对应价格为 0.12 美元和 0.60 美元，同时推理强度由中等调为高；发布说明中的简短测试任务费用从 0.0014 美元增至 0.022 美元。此次版本还支持首次无密钥运行在打开 Browser Use 登录页并获批后继续执行，云浏览器会打印实时查看链接；发布说明称，Judge 对 gotchas 的判断会依据本次运行实际观察到的内容。

github · sarath-menon · 11月16日 00:51

<a id="item-tech-news-3"></a>
#### [datasette-apps 0.4a0 增加应用间链接](https://simonwillison.net/2026/Nov/15/datasette-apps/) ⭐️ 6.0/10

datasette-apps 0.4a0 为运行在 Datasette 内的沙箱化 HTML 和 JavaScript 应用增加了链接支持，应用可以读取并使用 URL 中的 \`\#fragment\`。该版本还会向 Datasette Agent 报告支持的 URL scheme，帮助 Agent 编写能够相互链接的应用。开发者因此可以让独立应用协同导航，例如由搜索应用链接到详情应用中的具体记录表示。

rss · Simon Willison · 11月15日 04:02

<a id="item-tech-news-4"></a>
#### [datasette-agent 0.6a0 新增首页代理提问与哈希引用](https://simonwillison.net/2026/Nov/15/datasette-agent/) ⭐️ 6.0/10

datasette-agent 0.6a0 已发布，为 Datasette 的代理插件带来一组累积性小修复。其主要变化是在 Datasette 首页直接加入代理提问入口，用户可以用自然语言询问数据，并通过哈希提及引用表和查询；示例中输入“\#re”后，系统会显示 repos 和 releases 表的自动补全结果。该版本仍是 alpha，发布说明将其描述为一组小修复，而非重大版本更新。

rss · Simon Willison · 11月15日 03:49

<a id="item-tech-news-5"></a>
#### [1.4M 纯 HTML Three.js 游戏生成拆解](https://mp.weixin.qq.com/s/ZJddy1ssHBvw_1sm12jrkg) ⭐️ 6.0/10

数字生命卡兹克拆解了一款近期在群聊中流传的约 1.4M 单文件 HTML/Three.js 3D 游戏，重点介绍如何让 AI 通过代码完成程序化生成。据作者分析，约 700KB 是直接打包进文件的 Three.js，其余内容均由代码生成，游戏不含图片、模型或录音。文章还提供了一套面向类似项目的 AI 提示词模板，但现有原文摘要没有附上模板正文、代码或完整实现步骤，因此尚不足以复现整个流程。

rss · AI 热榜 · 11月15日 23:56

<a id="item-tech-news-6"></a>
#### [Anthropic 称并行 Claude 代理同仓库协作或更差](https://blog.qiaomu.ai/worse-together-multi-agent) ⭐️ 4.0/10

对于考虑在同一代码仓库中并行分配任务的开发者，文章转述 Anthropic 的最新研究称，两个 Claude 代理同时工作时，团队整体表现可能明显低于仅使用一个 Claude。现有内容未提供实验设计、量化指标、适用条件或缓解措施，因此这只能作为研究结论的二手转述，不能据此认定所有多代理编码工作流都会退化。

rss · 向阳乔木 · 11月15日 02:49