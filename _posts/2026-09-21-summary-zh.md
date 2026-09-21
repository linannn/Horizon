---
layout: default
title: "Horizon 每日速递：2026-09-21"
description: "AI 精选的技术与研究日报"
date: 2026-09-21
lang: zh
locale: zh-CN
---

> 从 32 条内容中筛选出 3 条重要资讯。

---

1. [阶跃星辰发布 Step 5 Preview：600B 稀疏 MoE，10 月 15 日开源权重](#item-1) ⭐️ 7.0/10
2. [Google 开源智能体编排器 AX 引发关注与质疑](#item-2) ⭐️ 6.0/10
3. [llm-keys-ui 0.1：为远程机器提供输入 API 密钥的本地网页界面](#item-3) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [阶跃星辰发布 Step 5 Preview：600B 稀疏 MoE，10 月 15 日开源权重](https://mp.weixin.qq.com/s?__biz=MzkyNTYxNzg5Mg%3D%3D&amp;mid=2247488120&amp;idx=1&amp;sn=8ba9ac7f0b36682d6262290677c665da) ⭐️ 7.0/10

**级别**: 核心必看

阶跃星辰发布旗舰基座模型 Step 5 Preview，采用稀疏 MoE 架构，总参数量 600B、每次激活 27B，支持 100 万 Token 上下文以及文本与视觉输入。该模型在 Artificial Analysis Intelligence Index 上取得 44 分，位居全球开源模型前三，官方表示将于 10 月 15 日正式开源权重。 如果权重如期开源，开发者将获得一个具备百万级上下文、且单任务成本约为 Claude Opus 5 八分之一的顶级开源模型选项，这会直接影响开源生态中的模型选型、部署成本核算以及长上下文应用的架构设计。 最需要留意的是，这一版本仍属“Preview”：权重只是承诺在 10 月 15 日开源，目前尚不可下载，且公开材料没有给出编程或 Agent 工作流等细分基准数据，因此 44 分的综合指数成绩和 1/8 的成本比例尚无按任务类型的独立验证。

rss · AI 热榜 · 9月20日 02:00

**背景**: 稀疏混合专家（MoE）模型保留极大规模的参数池，但每个 Token 只经过其中一小部分专家网络——这里是 600B 中的 27B——因此在同等总参数量下，能以更低的推理成本承载更多知识。Artificial Analysis Intelligence Index 是一个综合基准，把数学、科学、编程和推理等十项高难度评测聚合成一个分数，用于横向比较模型能力。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzkyNTYxNzg5Mg%3D%3D&amp;mid=2247488120&amp;idx=1&amp;sn=8ba9ac7f0b36682d6262290677c665da">阶跃星辰发布旗舰模型 Step 5 Preview，10 月 15 日开源权重</a></li>
<li><a href="https://www.ithome.com/1/004/705.htm">阶 跃 发 布 旗 舰 模 型 Step 5 Preview ：跻身 AA...</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index v4.3.2</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#MoE`, `#long-context`, `#model-release`

---

## 更多动态

<a id="item-2"></a>
### [Google 开源智能体编排器 AX 引发关注与质疑](https://agentexecutor.io/) ⭐️ 6.0/10

一个名为 AX、被冠以 Google 之名的开源智能体编排框架经由 agentexecutor.io 出现在 Hacker News 上，其 GitHub 仓库（google/ax）将其描述为面向自主智能体工作负载的高吞吐量声明式编排器。该提交本身只包含标题和链接，没有变更日志、架构说明或能力文档，却仍引发了 156 分、69 条评论的讨论。

hackernews · blazarquasar · 9月20日 22:32 · [社区讨论](https://news.ycombinator.com/item?id=49780797)

<a id="item-3"></a>
### [llm-keys-ui 0.1：为远程机器提供输入 API 密钥的本地网页界面](https://simonwillison.net/2026/Sep/20/llm-keys-ui/) ⭐️ 6.0/10

Simon Willison 发布了 llm-keys-ui 0.1，这是其 llm CLI 的一个插件：它在远程机器上启动一个本地网页界面，让人在那里手动填入 API 密钥，而不必把密钥粘贴进代理会话；之后代理可以用 \`llm keys get anthropic\` 这类命令取用密钥。启动方式是 \`uvx --with llm-keys-ui llm keys-ui --all\`，它会输出可访问的网址（包括局域网和 Tailscale 设备 IP）。

rss · Simon Willison · 9月20日 19:22