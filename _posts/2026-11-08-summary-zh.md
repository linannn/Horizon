---
layout: default
title: "Horizon 每日速递：2026-11-08"
description: "AI 精选的技术与研究日报"
date: 2026-11-08
lang: zh
locale: zh-CN
---

> 从 32 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [Claude Code 本地设置误提交，1,122 个公开文件泄露凭据](#item-tech-news-1) ⭐️ 8.0/10
2. [MaxxBench 质疑 DeepSWE 评分可靠性](#item-tech-news-2) ⭐️ 8.0/10
3. [VISTA 以代码自修改提升具身智能体成功率](#item-tech-news-3) ⭐️ 6.0/10
4. [Copilot CLI v1.0.108-1 修复 Grok PDF 附件与 MCP 沙箱路径](#item-tech-news-4) ⭐️ 5.0/10
5. [下一代 Agent Harness 的持续学习记忆系统](#item-tech-news-5) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude Code 本地设置误提交，1,122 个公开文件泄露凭据](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 8.0/10

**级别**: 核心必看

APIiro 报告称，其检查公开 GitHub 仓库时识别出 1,122 个文件，其中 Claude Code 持久化的“Don’t Ask Again”命令含有暴露的密码或密钥。问题并非点击该按钮本身造成，而是开发者手动创建并提交了本应仅保留在本地的 .claude/settings.local.json，且获批命令中直接包含秘密。Claude Code 团队成员 Boris 承认该工具过去不执行秘密清洗，并表示正在研究如何防止此类问题。

hackernews · shmulc · 11月7日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=50407882)

**「持久化授权机制」** Claude Code 的“Don’t Ask Again”会把开发者批准的命令写入持久化允许列表；相关配置记录的是命令原文，因此若命令本身含有明文凭据，秘密也会被保存在配置中。风险由此从一次终端调用扩展为后续源码管理中的静态文件暴露。

**「立即检查并轮换凭据」** 使用该授权功能的开发者应检查提交历史及当前仓库中的 .claude/settings.local.json 等本地设置，移除误提交内容并轮换其中已经暴露的密码或 API 密钥。团队称 Claude Code 创建该文件时会自动将其加入 .gitignore，因此版本控制检查仍是阻止今后误提交的重要防线。

**「社区提出的隔离措施」** 为减少人工确认并限制代理权限，tsergiu 建议每个任务使用隔离网络的临时虚拟机，并配合限制外部服务访问权限的 API 代理。binarymax 则让 Claude 通过调用 1Password 的 op CLI 按需获取凭据，使代理无法直接读取秘密。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again">Claude Code&#x27;s &quot;Don&#x27;t Ask Again&quot; exposes passwords in 1,122 public GitHub files</a></li>
<li><a href="https://dzen.ru/a/au7m4aCL2QDFv4Wh">Утечка “ Don ’ t Ask Again ” от Claude Code : пароли и ключи... | Дзен</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding-agent security`, `#secret leakage`, `#GitHub`, `#AI coding workflows`

---

<a id="item-tech-news-2"></a>
### [MaxxBench 质疑 DeepSWE 评分可靠性](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 8.0/10

**级别**: 核心必看

MaxxBench 对 DeepSWE 基准的可靠性提出技术质疑，面向依赖该基准评估编码代理的开发与评测团队。现有页面摘要称，小模型在该基准上的成绩下滑更明显，并提出强化学习环境可能过拟合、基准实现可能有缺陷两类风险；但所给材料没有提供具体分数、模型范围或复现实验数据。其核心提醒是，DeepSWE 高分不能单独证明代理具备可迁移的真实软件工程能力，必须结合环境多样性和实现核验来解读。

hackernews · antiuniverse · 11月7日 17:19 · [社区讨论](https://news.ycombinator.com/item?id=50406222)

**「MaxxBench 的构造方式」** 理解这项批评的关键，是 MaxxBench 并非另建一套通用编码能力榜单，而是对 DeepSWE 现有任务做受控扰动：它修改了 89 个任务的指令或初始代码，例如要求小写文件名或使用 UTC 时间戳，并将补丁增量中位数控制在 17 行（3.5%）。这种设计用于检验模型在任务表述或起点发生变化时是否仍能完成同类软件工程工作，从而将原始榜单分数与跨条件鲁棒性区分开来。

**「选型时需交叉验证」** 采用 DeepSWE 分数选型时，团队应核查基准缺陷、比较训练环境与评测任务的分布，并增加不同复杂度环境下的复测；否则，小模型的基准落差可能被误读为真实能力差距，头部模型的高分也可能掩盖环境过拟合。

**「评论者讨论过拟合机制」** 多位评论者把较小的模型作为重点：有人认为图中小模型跌幅最大，并猜测它们更容易过拟合较简单的强化学习环境，也有人建议用更多样、刻意包含过难或过易任务的训练环境检验泛化。另有评论者提醒，基准差距未必对应真实场景差距，因为基于训练形成的假设在实践中未必同样不利。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://maxxbench.unlap.ai/research/why-maxxbench/">MaxxBench – &quot;Nice DeepSWE score. But is it true?&quot;</a></li>
<li><a href="https://daily.dev/posts/maxxbench-nice-deepswe-score-but-is-it-true--ue9ulip60">MaxxBench – &quot;Nice DeepSWE score. But is it true?&quot;</a></li>

</ul>
</details>

**标签**: `#coding-agent benchmarks`, `#LLM evaluation`, `#DeepSWE`, `#reinforcement learning`, `#benchmark validity`

---

### 更多动态

<a id="item-tech-news-3"></a>
#### [VISTA 以代码自修改提升具身智能体成功率](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247940414&amp;idx=3&amp;sn=6a208ab7dffbe83bfda1e6dd1c91550d) ⭐️ 6.0/10

VISTA 声称，具身智能体可通过主动探索和代码级自修改，在不更新模型权重的情况下迭代能力，并将所测任务的成功率从 17.5% 提高到 95%。这一方案把智能体的自我改进放在代码修改而非权重更新上，为机器人能力迭代提供了一条不同路径。当前信息未给出任务定义、样本量、对照实验、失败案例、复现方法或开源可用性，且结果来自二手报道，因此 95% 的适用范围与可靠性尚无法确认。

rss · 量子位 · 11月7日 04:30

<a id="item-tech-news-4"></a>
#### [Copilot CLI v1.0.108-1 修复 Grok PDF 附件与 MCP 沙箱路径](https://github.com/github/copilot-cli/releases/tag/v1.0.108-1) ⭐️ 5.0/10

GitHub 已发布 Copilot CLI v1.0.108-1，包含两项面向开发者工作流的修复：使用 Grok 4.7 或 Grok 4.6 时，PDF 附件不再导致该轮交互失败，而是回退为文件引用。启用沙箱后，执行 \`/cd\` 会重启正在运行的本地 MCP 服务，使其采用新目录的拒绝路径规则，而不再沿用离开目录时的配置。

github · copilot-cli-release-app\[bot\] · 11月7日 02:32

<a id="item-tech-news-5"></a>
#### [下一代 Agent Harness 的持续学习记忆系统](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247940414&amp;idx=1&amp;sn=07f6bd438992c5d7dc15b3e9f31cd6be) ⭐️ 4.0/10

报道介绍了一套面向下一代 Agent Harness 的记忆系统，其定位是“持续学习、永远在线”，旨在让智能体拥有持久且持续更新的记忆。文章没有披露项目名称、架构与实现、模型、部署方式、发布状态、基准测试或已知限制，因此目前能够确认的仅是产品方向，而非已经公开可用或经独立验证的能力。标题中的“抢跑 DeepSeek”和“硅谷华人造出来了”属于报道的营销性表述。

rss · 量子位 · 11月7日 04:30