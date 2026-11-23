---
layout: default
title: "Horizon 每日速递：2026-11-23"
description: "AI 精选的技术与研究日报"
date: 2026-11-23
lang: zh
locale: zh-CN
---

> 从 27 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [梅纳德称 Claude 合作黎曼猜想证明正确](#item-tech-news-1) ⭐️ 8.0/10
2. [AI 编程智能体模拟职场任务完成率不足一成](#item-tech-news-2) ⭐️ 7.0/10
3. [Perplexity 推出 Monitor API 持续监控网页变化](#item-tech-news-3) ⭐️ 7.0/10
4. [Browser Use 1.0.8 优化代理计费与审批](#item-tech-news-4) ⭐️ 6.0/10
5. [Inkling、Qwen 与 Unsloth 本地 AI 入门指南](#item-tech-news-5) ⭐️ 6.0/10
6. [MiniCPM5-2B 在 Mac 本地分析体检报告实测](#item-tech-news-6) ⭐️ 6.0/10
7. [Copilot CLI v1.0.115-7 修复会话附加与后台进程残留](#item-tech-news-7) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [梅纳德称 Claude 合作黎曼猜想证明正确](https://www.ithome.com/1/030/677.htm) ⭐️ 8.0/10

**级别**: 核心必看

2022 年菲尔兹奖得主、牛津大学数学教授詹姆斯·梅纳德在采访中表示，他相信 Anthropic 数学家莱文特·阿尔珀格与 Claude 合作完成的黎曼猜想证明是正确的。梅纳德给出的依据是，该证明已通过 Lean 库的形式化验证并经独立核实，同时阿尔珀格过往研究记录可靠。不过，当前报道只转述这一评价，未提供证明内容或 Lean 验证工程细节，因此这不等同于数学界已经正式认可该证明。

rss · AI 热榜 · 11月22日 09:35

**「形式化验证不等于学界认可」** Lean 形式化验证是把证明表示为可由 Lean 系统检查的严格形式对象；“验证通过”说明该形式表达通过了检查，但不自动代表数学界已经接受其思路与意义。对此类重大 conjectures 的认可，通常仍需同行审查证明本身及相关验证工程。

**「引用时区分机器验证与学界认可」** 数学家、编辑及出版机构不应仅凭当前报道就把这项成果表述为“黎曼猜想已被解决”，而应分别标注 Lean 形式化验证与学界正式认可的状态；在核对证明内容、验证工程并完成学界审查前，也不宜将其作为已确立的结论引用。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.ithome.com/1/030/677.htm">菲尔兹奖得主梅纳德谈 Claude 合作证明黎曼猜想：相信证明正确，但需被理解才可能获认可</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI数学研究`, `#形式化验证`, `#Lean`, `#黎曼猜想`

---

<a id="item-tech-news-2"></a>
### [AI 编程智能体模拟职场任务完成率不足一成](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/) ⭐️ 7.0/10

**级别**: 核心必看

一项将 AI 编程智能体置于模拟开发者工作环境的基准测试显示，Opus 5.5 和 Astra 在包含同事、项目看板及未完成交接的日常流程中，完整解决的任务仍不足十分之一。它们能迅速完成边界清晰的独立编程任务，但在需要持续开发并可靠关闭工单的自主工作流中容易失去跟踪，表明隔离式编码测试的高分不能直接代表真实任务完成能力。由于摘要未提供样本量、任务构成和评测方法，该结果的稳健性尚难判断。

rss · The Decoder · 11月22日 15:15

**「从单点编码到完整工作流」** 隔离式编码评测主要考察代理能否完成边界清晰的一次性任务，而模拟职场的评测要求它从项目看板、同事沟通和未完成交接中恢复上下文，并持续推进到工单真正关闭。相关上下文工程文档也指出，代理在大型既有代码库中未必能提高开发效率，甚至可能因额外改动而制造返工；因此，本次测试区分的是单点编码表现与端到端自主交付能力。

**「落地评估需转向完整交付」** 对计划让 AI 编程代理处理真实工单或工单队列的团队，隔离式编码成绩不能直接作为自主交付产能或吞吐量的采购依据；验收应关注完整关闭工单率，并测试上下文恢复、持续推进和未完成交接等能力。上线评估还应记录成本、token 消耗与执行时间，并保留人工复核；由于摘要未披露样本量和评测方法，不能据此直接推算生产环境中的节省工时。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/">AI coding agents ace isolated tests but complete fewer than one in ten tasks in a simulated workplace</a></li>
<li><a href="https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md">advanced-context-engineering-for- coding - agents / ace -fca.md at main...</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks &amp; Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#agent benchmarks`, `#autonomous software development`, `#engineering workflow evaluation`

---

<a id="item-tech-news-3"></a>
### [Perplexity 推出 Monitor API 持续监控网页变化](https://the-decoder.com/perplexitys-new-monitor-api-turns-web-search-from-a-one-off-query-into-a-nonstop-watchdog/) ⭐️ 7.0/10

**级别**: 核心必看

Perplexity 宣布推出面向智能体开发者的 Monitor API，可按计划搜索网页，并在发现相关变化时通过 webhook 发出提醒。该 API 使用 Perplexity 自有的决策模型过滤不重要的结果，将网页搜索从单次查询扩展为持续监控。现有说明尚未提供定价、调用限额、实现示例或具体可用范围。

rss · The Decoder · 11月22日 14:20

**「此前的网页监控瓶颈」** Perplexity 称，在 Monitor API 之前，团队若要让智能体持续跟踪网页，必须自行按计划触发重复搜索，并维护用于去重和变更检测的定制代码；当范围扩大到数百个主题或页面时，这套流程几乎无法维护。11 月 16 日发布的 Monitor API 将定时搜索、持久监控状态、去重和变更检测整合进一个接口，把原本由应用方承担的后台工作交给平台。

**「对开发者的影响」** 开发者可以将 Monitor API 接入智能体，让后续流程由变更触发的 webhook 驱动，而不必逐一检查所有定时搜索结果；在定价、限额和接入细节公布前，团队仍需评估运行成本与可用范围。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://the-decoder.com/perplexitys-new-monitor-api-turns-web-search-from-a-one-off-query-into-a-nonstop-watchdog/">Perplexity&#x27;s new Monitor API turns web search from a one-off query into a nonstop watchdog</a></li>
<li><a href="https://www.perplexity.ai/hub/blog/introducing-perplexitys-monitor-api">Introducing Perplexity’s Monitor API</a></li>
<li><a href="https://www.konsulteer.com/article/perplexity-launches-monitor-api-to-bring-continuous-web-intelligence-to-ai-agents">Perplexity Launches Monitor API to Bring Continuous Web ...</a></li>
<li><a href="https://www.europesays.com/ai/250358/">Perplexity&#x27;s new Monitor API turns web search from a one-off ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#web monitoring`, `#developer APIs`, `#webhooks`, `#Perplexity`

---

### 更多动态

<a id="item-tech-news-4"></a>
#### [Browser Use 1.0.8 优化代理计费与审批](https://github.com/browser-use/browser-use/releases/tag/1.0.8) ⭐️ 6.0/10

Browser Use 1.0.8 已发布，开发者可通过 \`pip install &\#x27;browser-use==1.0.8&\#x27;\` 安装。发布说明称，Judge 作为运行中的额外一轮执行，使模型提供商从缓存读取该次运行，避免重复为运行轨迹计费，同时返回相同的 verdict 字段，包括 gotchas；无头机器或通过 SSH 运行时，系统会输出链接和代码，用户可在其他设备完成审批后继续执行。该版本还修复了 DeepSeek 和 Qwen 在 thinking 模式下达到步数上限后拒绝强制最终调用的问题，改为再次发起非强制请求以返回答案，并确保 \`bu.type\` 不输出密码字段的值、\`Browser\(cdp\_url=...\)\` 接入已打开的唯一页面而非新建空白标签页；网关调用预留的输出 token 从 32,768 降至 16,384，以减少余额不足导致运行中途被拒绝的情况。

github · gregpr07 · 11月22日 03:30

<a id="item-tech-news-5"></a>
#### [Inkling、Qwen 与 Unsloth 本地 AI 入门指南](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) ⭐️ 6.0/10

GPU Partner 博客发布了一篇面向初学者的指南，讲解如何组装并运行由 Inkling、Qwen 和 Unsloth 构成的本地 AI 技术栈。现有材料只确认了“Qwen 本地部署入门工作流”这一主题；由于文章正文缺失，无法核实具体模型版本、量化配置、硬件门槛、命令步骤或各组件的兼容性。

hackernews · Retell15 · 11月22日 21:01 · [社区讨论](https://news.ycombinator.com/item?id=50603845)

<a id="item-tech-news-6"></a>
#### [MiniCPM5-2B 在 Mac 本地分析体检报告实测](https://x.com/OpenBMB/status/2124461770043785636) ⭐️ 6.0/10

面壁智能转述了用户 @cxjwin 在搭载 M4 Pro、48GB 内存的 Mac 上本地运行 MiniCPM5-2B 的实测：通过 Homebrew 安装 llama.cpp，并用 Colima 启动 Docker 部署由 Theta Health 以 Apache-2.0 开源的 Mirobody，处理一份 14 页体检报告 PDF。首次处理漏掉 3 页扫描版化验单；将截图单独上传后，58 行化验数值均与原件逐项一致，其中 20 行成功映射到 LOINC 编码，肌酐因名称歧义被留空而未猜测。模型经过 11 步处理找到全部 5 项带箭头的指标，但把一项处于参考范围内的血糖误判为超标；这是用户实测结果，并非官方性能验证。接入 Claude Code 时，用户改用演示账号以避免数据上传。

rss · AI 热榜 · 11月22日 11:15

<a id="item-tech-news-7"></a>
#### [Copilot CLI v1.0.115-7 修复会话附加与后台进程残留](https://github.com/github/copilot-cli/releases/tag/v1.0.115-7) ⭐️ 4.0/10

GitHub 发布 Copilot CLI v1.0.115-7，修复使用 \`--ui-server\` 的客户端无法在服务器开始监听后立即附加到已恢复 CLI 会话的问题。该版本还确保通过 npm 安装的 Copilot CLI 在启动期间被停止时，不会继续作为后台进程运行。

github · copilot-cli-release-app\[bot\] · 11月22日 11:40