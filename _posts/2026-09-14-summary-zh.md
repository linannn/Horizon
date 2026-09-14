---
layout: default
title: "Horizon 每日速递：2026-09-14"
description: "AI 精选的技术与研究日报"
date: 2026-09-14
lang: zh
locale: zh-CN
---

> 从 26 条内容中筛选出 3 条重要资讯。

---

1. [Simon Willison 发布 commit-rewriter 0.1，用于批量修改 git 提交信息](#item-1) ⭐️ 6.0/10
2. [AllSpark 发布 Iris-mini 与 Iris-pro 开放权重搜索智能体](#item-2) ⭐️ 4.0/10
3. [Agent Harness 上下文工程：对抗上下文溢出与目标丢失的四类机制](#item-3) ⭐️ 4.0/10

---

## 更多动态

<a id="item-1"></a>
### [Simon Willison 发布 commit-rewriter 0.1，用于批量修改 git 提交信息](https://simonwillison.net/2026/Sep/14/commit-rewriter/) ⭐️ 6.0/10

Simon Willison 发布了 commit-rewriter 0.1，这是一个小型 Python 网页应用，通过 \`uvx commit-rewriter path/to/repo\` 启动本地浏览器界面（默认地址为 http://127.0.0.1:8000，可用 -p/--port 更改端口），用于批量编辑仓库中的 git 提交信息；若已在仓库目录内可省略路径。界面左侧栏按顺序列出提交，支持按提交信息、作者或哈希搜索，可勾选“仅显示已编辑项”，还能暂存或丢弃草稿，并查看每条提交的完整格式化 diff。

rss · Simon Willison · 9月14日 00:28

<a id="item-2"></a>
### [AllSpark 发布 Iris-mini 与 Iris-pro 开放权重搜索智能体](https://the-decoder.com/iris-mini-and-iris-pro-are-the-strongest-open-weight-search-agents-in-their-class/) ⭐️ 4.0/10

AllSpark 团队发布了 Iris-mini（35B-A3B）和 Iris-pro（397B-A17B）两款开源搜索智能体，分别基于 Qwen3.6-35B-A3B 与 Qwen3.5-397B-A17B 构建，均支持 256,000 token 的上下文窗口，并声称在各自参数规模档位的开放权重搜索智能体中基准成绩领先。配套论文（arXiv 2609.04304）同时公开了数据流水线与训练配方，并称其训练数据和模型还提升了从未被专门训练过的任务表现，例如通用工具调用和办公工作。

rss · The Decoder · 9月13日 12:58

<a id="item-3"></a>
### [Agent Harness 上下文工程：对抗上下文溢出与目标丢失的四类机制](https://www.marktechpost.com/2026/09/12/context-engineering-inside-the-harness-4-mechanisms-that-beat-context-overflow-and-goal-loss-on-long-horizon-tasks) ⭐️ 4.0/10

MarkTechPost 于 2026 年 9 月 12 日发表文章，拆解了 Agent harness 在长任务中赖以维系运行的四类机制：上下文预算与卸载、压缩、todo-state 复述，以及跨会话记忆。

rss · AI 热榜 · 9月13日 05:56