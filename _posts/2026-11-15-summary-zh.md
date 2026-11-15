---
layout: default
title: "Horizon 每日速递：2026-11-15"
description: "AI 精选的技术与研究日报"
date: 2026-11-15
lang: zh
locale: zh-CN
---

> 从 36 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [browser-use 1.0.5 加入逐次 LLM 评判](#item-tech-news-1) ⭐️ 7.0/10
2. [Lovable 应用暴露护照资料与逾 20 万条私信](#item-tech-news-2) ⭐️ 7.0/10
3. [Claude Opus 5.5 成为付费方案默认模型](#item-tech-news-3) ⭐️ 6.0/10
4. [checkpointpostgres 3.2.1 优化异步检查点路径](#item-tech-news-4) ⭐️ 5.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [browser-use 1.0.5 加入逐次 LLM 评判](https://github.com/browser-use/browser-use/releases/tag/1.0.5) ⭐️ 7.0/10

**级别**: 核心必看

browser-use 1.0.5 为每次浏览器自动化运行加入由开发者自带模型执行的 LLM 评判，输出 success、failure\_reason、description、prompt\_injection\_detected、bot\_block\_or\_captcha\_detected 和 gotchas。评判器可读取运行轨迹、最后几张截图及最终页面（use\_vision=False 时除外），并通过 judge\_context 接收自定义标准；judge=False 可关闭评判，0.x 的 use\_judge 与 ground\_truth 参数也恢复可用。发布方的测试涵盖 13 次真实运行、每次评判 3 次：站点出现阻力时，15/15 次判定均发现 gotchas，而此前为 6/15；干净运行中仅 2/24 次出现 gotchas，成功判定数量未变。

github · sarath-menon · 11月14日 08:24

**「从代理执行到后置评判」** browser-use 是面向 AI 浏览器代理的开源 Python 库，既可控制本地浏览器、Browser Use Cloud，也可接入现有远程浏览器；因此，1.0.5 的 \`judge\` 是对既有代理运行结果的后置评估层，而不是一种新的浏览器操作方式（tool-1-2）。这一改动也承接了 0.x 的接口背景：\`use\_judge\` 和 \`ground\_truth\` 在 1.0.5 中重新可用，开发者可继续使用原有配置，或通过 \`judge\_context\` 为每次运行提供任务特定标准（tool-1-1）。

**「运行诊断更具体，但需考虑额外开销」** 自动化团队现在可以在一次运行诊断中同时确认任务是否成功，以及网站是否因输入被拒、报错、封锁、限流或表单格式要求而阻碍执行；但启用评判会给每次运行增加一次低开销模型请求，因此应评估新增的延迟和成本，不需要时可设置 judge=False。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/browser-use/browser-use/releases/tag/1.0.5">browser-use/browser-use released 1.0.5</a></li>
<li><a href="https://github.com/browser-use/browser-use/releases">Releases · browser-use/browser-use · GitHub</a></li>
<li><a href="https://github.com/browser-use/browser-use">GitHub - browser-use/browser-use: Open-source Python library ...</a></li>

</ul>
</details>

**标签**: `#browser-use`, `#AI agents`, `#browser automation`, `#agent evaluation`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [Lovable 应用暴露护照资料与逾 20 万条私信](https://www.crissyfield.de/research/lovable-en/) ⭐️ 7.0/10

**级别**: 核心必看

安全研究人员报告，一些由 Lovable 生成的应用因数据库行级安全（RLS）配置不足，暴露了护照资料以及超过 20 万条私人消息。自称 Lovable 安全负责人的评论者确认根因是 RLS 不足，并称平台会在发布前自动扫描每个应用、向所有用户免费提供更深入的静态应用安全测试（SAST）扫描；发现问题时，用户可选择由 Lovable 修复或启用后台自动修复。数据暴露范围来自研究报告，扫描与修复能力则属于平台方面的说明。

hackernews · armcat · 11月14日 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**「行级安全为何决定数据库可见性」** 数据库的行级安全（RLS）按用户与记录范围控制读取和写入；若生成的应用没有正确启用或配置策略，浏览器请求就可能绕过应用登录并取得本应隔离的数据。Crissy Field 对 Lovable 项目的扫描此前已由 11 月 3 日至 4 日的报道披露为覆盖 159,041 个项目，因此本次登上 Hacker News 的文章属于对同一批研究发现的后续传播，而不是另行宣布的一项新事件。

**「发布前需验证授权边界」** 在相关 RLS 漏洞中，未认证访问者可用公开 API 密钥直接查询敏感表并绕过服务器端检查，因此开发团队应把“未登录请求能否读取他人记录”列为发布前必测项。Lovable 的发布时后台扫描约需 10 至 15 秒，可检查数据库误配置、缺失的 RLS 策略和授权缺口，但自动修复仅处理不会影响应用行为的项目，其余告警仍需人工修复并复测。

**「讨论聚焦数据库默认值与平台责任」** 评论者在责任归属上存在分歧：部分观点认为 Supabase 为降低开发门槛而设置的数据库默认值应承担责任，同时也不应忽视 Lovable 对这些配置的依赖；关于既有项目是否仍受旧默认值影响的说法未获所给材料独立验证。另有评论者认为，AI 生成应用规模庞大且通过浏览器检查网络请求即可发现问题，因此平台应采用默认拒绝的数据库、最小权限 API 和自动化授权测试。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.crissyfield.de/research/lovable-en/">Lovable apps expose passport details and more than 200K private messages</a></li>
<li><a href="https://cybernews.com/security/lovable-ai-apps-expose-personal-information/">Lovable AI apps exposed sensitive data in open databases ...</a></li>
<li><a href="https://lovable.dev/blog/how-lovable-protects-your-apps-automatically">How Lovable protects your apps automatically</a></li>
<li><a href="https://www.superblocks.com/blog/lovable-vulnerabilities">Lovable Vulnerability Explained: How 170+ Apps Were Exposed</a></li>

</ul>
</details>

**标签**: `#AI coding security`, `#Lovable`, `#Supabase`, `#row-level security`, `#secure app generation`

---

### 更多动态

<a id="item-tech-news-3"></a>
#### [Claude Opus 5.5 成为付费方案默认模型](https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5/) ⭐️ 6.0/10

据 The Decoder 报道，Anthropic 已将 Claude Opus 5.5 设为所有付费方案的默认模型，影响 Claude 的全部付费用户。Anthropic 还发布提示词指南，建议删除“think hard”这类旧式指令，并从 Medium（中等）推理强度开始。现有材料未提供基准测试、方法或示例来量化旧提示习惯造成的减速，因此这应视为厂商推荐的提示词工作流，而非经独立测量证实的性能结论。

rss · The Decoder · 11月14日 16:42

<a id="item-tech-news-4"></a>
#### [checkpointpostgres 3.2.1 优化异步检查点路径](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.2.1) ⭐️ 5.0/10

LangGraph 的 checkpointpostgres 3.2.1 已发布，主要面向使用 PostgreSQL 持久化 LangGraph 检查点的开发者，更新了异步检查点路径：让单独的 store 读取在 pipeline 之外运行，在连接池场景跳过异步 saver 的锁，并在无待写入内容时避免线程跳转。相较 3.2.0，该版本还包含 checkpoint 4.3.2 和 4.3.1 的发布记录，并将 libs/checkpoint-postgres 中的 certifi 依赖从 2026.1.4 升至 2026.10.19。发布说明未提供基准测试或迁移指引，因此这些优化的实际收益幅度目前无法量化。

github · github-actions\[bot\] · 11月14日 01:39