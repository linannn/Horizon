---
layout: default
title: "Horizon 每日速递：2026-09-20"
description: "AI 精选的技术与研究日报"
date: 2026-09-20
lang: zh
locale: zh-CN
---

> 从 29 条内容中筛选出 3 条重要资讯。

---

1. [pydantic-ai v2.46.0 发布：TypeSafeModel 增强、实时播放与 Temporal 事件流](#item-1) ⭐️ 6.0/10
2. [Claude Code v2.1.278 将 auto 模式默认切换为服务端分类器](#item-2) ⭐️ 5.0/10
3. [Unity 为 Claude Code 和 Codex 发布官方插件，阻止 AI 代理使用过时教程](#item-3) ⭐️ 4.0/10

---

## 更多动态

<a id="item-1"></a>
### [pydantic-ai v2.46.0 发布：TypeSafeModel 增强、实时播放与 Temporal 事件流](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) ⭐️ 6.0/10

pydantic-ai 发布 v2.46.0，带来 8 项新功能与约 10 项缺陷修复：\`TypeSafeModel\` 现在可以填充工具参数、并可先选定联合输出类型再填充；新增 \`RealtimeSession.wait\_for\_playback\(\)\`，让示例在关闭前先播放完回复；\`ModelProfile\` 新增 \`supports\_text\_output\` 标志；\`TemporalDurability\` 新增 \`event\_stream\_topic\`，可通过 Temporal Workflow Streams 流式输出 agent 事件；此外还有 \`typesafe\_boolean\_threshold\` 阈值设置、运行时构建选项集的 \`Choices\` 辅助类，以及通过 \`UseEnumMemberDocstrings\` 用成员文档字符串描述 Enum 选项的能力。

github · DouweM · 9月19日 03:51

<a id="item-2"></a>
### [Claude Code v2.1.278 将 auto 模式默认切换为服务端分类器](https://github.com/anthropics/claude-code/releases/tag/v2.1.278) ⭐️ 5.0/10

Claude Code v2.1.278 将 auto 模式在 Claude API、Enterprise 用户以及 Bedrock、Vertex、Foundry 和各类网关上的默认行为改为使用服务端分类器，该分类器不计收分类器开销费用；在 Bedrock、Vertex、Foundry 和网关上可通过环境变量 CLAUDE\_CODE\_AUTO\_MODE\_SERVER=0 选择退出，回退到计费路径时会给出警告。该版本还在 /status 中新增了 “Auto mode server” 一行，用于显示当前会话的 auto 模式分类器是否运行在服务端。

github · ashwin-ant · 9月19日 03:10

<a id="item-3"></a>
### [Unity 为 Claude Code 和 Codex 发布官方插件，阻止 AI 代理使用过时教程](https://the-decoder.com/unity-launches-official-plugins-for-claude-code-and-openai-codex-to-stop-ai-agents-from-using-outdated-tutorials/) ⭐️ 4.0/10

Unity 已为 Anthropic 的 Claude Code 和 OpenAI 的 Codex 发布了官方插件。据 Unity 称，推出插件的原因是通用型 AI 代理往往从论坛帖子和旧版本引擎的教程中获取答案，结果生成的代码虽然可能通过编译，但常常无法按预期工作。

rss · The Decoder · 9月19日 13:31