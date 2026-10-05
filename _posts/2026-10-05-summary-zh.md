---
layout: default
title: "Horizon 每日速递：2026-10-05"
description: "AI 精选的技术与研究日报"
date: 2026-10-05
lang: zh
locale: zh-CN
---

> 从 14 条内容中筛选出 5 条重要资讯。

---

1. [Strata 声称在单块 RTX 4090 上以约 100 tok/s 运行 125B Qwen 模型](#item-1) ⭐️ 6.0/10
2. [AWS 开发者开源 Pizza Bot：面向后台 AI 代理的收件箱](#item-2) ⭐️ 6.0/10
3. [PromptArmor：Databricks Genie 恶意 Skill 绕过四类控制外泄数据](#item-3) ⭐️ 6.0/10
4. [谷歌 RRSI 方法阻止自我改进 AI 智能体背题](#item-4) ⭐️ 5.0/10
5. [GitHub Copilot CLI v1.0.92-4 新增 config 子命令并修复 MCP 问题](#item-5) ⭐️ 4.0/10

---

## 更多动态

<a id="item-1"></a>
### [Strata 声称在单块 RTX 4090 上以约 100 tok/s 运行 125B Qwen 模型](https://github.com/Niko1221/Strata) ⭐️ 6.0/10

一个名为 Strata 的 GitHub 项目声称能在消费级 RTX 4090 上以约 100+ tokens/s 的速度推理 125B 参数的混合专家模型 Qwen3.8-Flash-Next，一位 Hacker News 评论者称自己在配备 128GB DDR5 和 Ryzen 7950X3D 的 4090 上实测达到 124 tokens/s。该说法目前存在争议：另一位评论者用 50 张图片做视觉基准测试，在完全相同的 GGUF 与视觉适配器权重下，Strata 的中位坐标误差为 154.8 像素，而 llama.cpp 为 46.5 像素。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

<a id="item-2"></a>
### [AWS 开发者开源 Pizza Bot：面向后台 AI 代理的收件箱](https://www.infoq.com/news/2026/10/pizza-bot-ai-agents/?utm_campaign=infoq_content&amp;utm_source=infoq&amp;utm_medium=feed&amp;utm_term=AI+Coding-news) ⭐️ 6.0/10

一批在 AWS 工作的开发者开源了 Pizza Bot，这是一个自托管应用，让 AI 代理在后台执行定时或由 webhook 触发的任务，并通过类似电子邮件的收件箱界面返回结果。代理还可以把工作委派给专用 worker，并在需要时暂停以等待人工批准。

rss · InfoQ AI Coding · 10月4日 06:34

<a id="item-3"></a>
### [PromptArmor：Databricks Genie 恶意 Skill 绕过四类控制外泄数据](https://www.promptarmor.com/resources/four-databricks-genie-controls-that-dont-stop-malicious-skills) ⭐️ 6.0/10

PromptArmor 披露，Databricks Genie Code 中的恶意 Skill 可以绕过该平台的四类控制措施：Skill 会把数据嵌入到聊天中渲染的 HTML 里，渲染过程借助用户浏览器发起网络请求将数据外泄，同时弹出钓鱼界面索取用户凭据。

rss · AI 热榜 · 10月5日 00:24

<a id="item-4"></a>
### [谷歌 RRSI 方法阻止自我改进 AI 智能体背题](https://the-decoder.com/google-researchers-find-a-way-to-keep-self-improving-ai-agents-from-memorizing-their-tests/) ⭐️ 5.0/10

谷歌研究人员提出 RRSI（Regularized Recursive Self-Improvement，正则化递归自我改进）方法，用于抑制自我改进型 AI 智能体记忆评测任务的倾向。据报道，RRSI 在未见过的基准测试上把分数最多提升 4.7 分，同时比未做正则化的版本少用约 30% 的 token。

rss · The Decoder · 10月4日 12:40

<a id="item-5"></a>
### [GitHub Copilot CLI v1.0.92-4 新增 config 子命令并修复 MCP 问题](https://github.com/github/copilot-cli/releases/tag/v1.0.92-4) ⭐️ 4.0/10

GitHub Copilot CLI 发布了 v1.0.92-4 补丁版本，新增用于列出、读取、设置和删除配置的 \`copilot config\` 子命令，同时改进了首次启动速度，并提升了同时连接多个 MCP 服务器时的响应能力。

github · copilot-cli-release-app\[bot\] · 10月4日 19:32