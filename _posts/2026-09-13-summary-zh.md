---
layout: default
title: "Horizon 每日速递：2026-09-13"
description: "AI 精选的技术与研究日报"
date: 2026-09-13
lang: zh
locale: zh-CN
---

> 从 32 条内容中筛选出 4 条重要资讯。

---

1. [Gemini CLI 每夜版修复间接提示注入并加固沙箱隔离](#item-1) ⭐️ 5.0/10
2. [浙大开源可插拔 Agent 评测底座，配套 CLI 与 Skills](#item-2) ⭐️ 4.0/10
3. [OpenAI 建议为 GPT-6 Astra 精简提示词、减少刚性护栏](#item-3) ⭐️ 4.0/10
4. [OpenAI 将 GPT-Live-1 语音模型开放至 API](#item-4) ⭐️ 4.0/10

---

## 更多动态

<a id="item-1"></a>
### [Gemini CLI 每夜版修复间接提示注入并加固沙箱隔离](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0-nightly.20260912.g9c1b0a610) ⭐️ 5.0/10

谷歌开源项目 gemini-cli 发布了每夜版构建 v0.61.0-nightly.20260912.g9c1b0a610，其中包含两项与安全相关的改动：核心模块修复了通过构建文件修改和不可信标志触发的间接提示注入（PR \#29250），沙箱模块则加固了文件系统边界并隔离运行时状态（PR \#29214）。PR \#29250 同时是 @villahernandez-coder 的首次贡献，PR \#29214 则由 @diegogodinezr 提交。

github · gemini-cli-robot · 9月12日 01:25

<a id="item-2"></a>
### [浙大开源可插拔 Agent 评测底座，配套 CLI 与 Skills](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247922331&amp;idx=2&amp;sn=31d53cffe48bc2b01fe20512a63dc043) ⭐️ 4.0/10

浙江大学开源了一套可插拔的 Agent 评测底座，并配套提供命令行工具（CLI）与 Skills；该发布信息正文仅有“告别海量脚手架”一句口号。就目前给出的内容而言，公告没有提供仓库链接、更新日志、架构说明或基准测试数据。

rss · 量子位 · 9月12日 08:30

<a id="item-3"></a>
### [OpenAI 建议为 GPT-6 Astra 精简提示词、减少刚性护栏](https://the-decoder.com/gpt-6-astra-needs-leaner-prompts-and-fewer-guardrails-openai-recommends/) ⭐️ 4.0/10

OpenAI 的 Eric Provencher 警告称，过长的技能描述、无差别的读取要求以及僵化的审批规则会阻碍 GPT-6 Astra 的表现，公司建议开发者把指令与具体任务更紧密地绑定，并明确说明任务何时算完成。

rss · The Decoder · 9月12日 13:10

<a id="item-4"></a>
### [OpenAI 将 GPT-Live-1 语音模型开放至 API](https://x.com/OpenAIDevs/status/2098913661993603215) ⭐️ 4.0/10

OpenAI 宣布 GPT-Live-1 正式登陆 API，这就是 1-800-ChatGPT 背后那套语音能力，开发者可借此构建边说边听的自然对话语音智能体，并自行搭配后端模型与 harness。该模型此前先面向 ChatGPT 用户推出，如今才开放 API 接入。

rss · AI 热榜 · 9月12日 23:16