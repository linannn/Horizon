---
layout: default
title: "Horizon 每日速递：2026-10-22"
description: "AI 精选的技术与研究日报"
date: 2026-10-22
lang: zh
locale: zh-CN
---

> 从 63 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [DeepSeek 开源 DeepInfer：每集群日吞吐 155T tokens](#item-tech-news-1) ⭐️ 8.0/10
2. [Mastra 1.79.0 推出实验性 MCP 事件流与可观测性升级](#item-tech-news-2) ⭐️ 7.0/10
3. [LiteLLM 1.107.0 供应链投毒事件](#item-tech-news-3) ⭐️ 7.0/10
4. [OpenAI 模型与 Codex 将进入 Google Cloud](#item-tech-news-4) ⭐️ 7.0/10
5. [Commerce.com 启用近 10 万域名 WebMCP 购物工具](#item-tech-news-5) ⭐️ 7.0/10
6. [OpenAI 发布 Codex PHP 漏洞自查技能](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenAI API 新增 12 小时提示缓存](#item-tech-news-7) ⭐️ 7.0/10
8. [Copilot CLI v1.0.102 更新代理、沙箱与模型选择](#item-tech-news-8) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DeepSeek 开源 DeepInfer：每集群日吞吐 155T tokens](https://www.latent.space/p/ainews-deepseek-deepinfer-open-source) ⭐️ 8.0/10

**级别**: 核心必看

Latent Space 报道称，DeepSeek 已开源推理系统 DeepInfer，并宣称其达到开源 SOTA（当前领先）水平。标题给出的指标为每个集群每天处理 155T tokens、每天产生 2200 万美元收益、毛利率约 80%，回本期为 81 天；但现有正文仅称“来自中国的开源炸弹”，未提供版本、代码地址、硬件配置或测量方法，因此这些数字不能视为经过独立验证的性能或财务结果。

rss · Latent Space · 10月21日 06:54

**「DeepInfer 的定位与开源范围」** DeepInfer 是 DeepSeek V4.1 Flash 模型的生产推理引擎，本次开源同时配套发布了 token 编解码库 deepseek-recipe；据现有报道，核心的 KVCache 管理等模块因内部耦合仍保持闭源，因此开放范围有限，且该框架已适配 NVIDIA 与华为升腾两种硬件平台。

**「部署决策仍需验证成本口径」** 推理服务运营者在据此调整部署或成本模型前，应核验代码与许可证、集群配置、模型负载，以及每日 2200 万美元收益、约 80% 毛利和 81 天回本期所采用的利用率、定价与资本开支假设；现有材料不足以证明其优于现有方案。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-deepseek-deepinfer-open-source">[AINews] DeepSeek DeepInfer: Open Source SOTA Inference running 155T toks/day/cluster making $22m/day at ~80% margin for a 81 day payback</a></li>
<li><a href="https://daily.steinslab.io/en/events/2026-10-20-deepseek-deepinfer/">DeepInfer Open-Sourced: 155T Daily Tokens Reveal Real-World ...</a></li>
<li><a href="https://todayforai.com/en/items/art-9832467f-c87">DeepSeek Open-Sources DeepInfer: 155T Daily Tokens on Single ...</a></li>

</ul>
</details>

**标签**: `#inference`, `#open-source`, `#deepseek`, `#AI-infrastructure`, `#cost-optimization`

---

<a id="item-tech-news-2"></a>
### [Mastra 1.79.0 推出实验性 MCP 事件流与可观测性升级](https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.79.0) ⭐️ 7.0/10

**级别**: 核心必看

Mastra 发布 @mastra/core 1.79.0，主要变化包括：基于 SEP-3415 草案的实验性 MCP Events（poll/stream/签名 webhook），可观测性新增 \`aggregateSpans\(\)\` 存储合约、\`timeToFirstChunkMs\` 指标以及支持 entityId/parent 等过滤的 \`querySpans\(\)\`，并将 Agent Controller 会话从 \`resourceId + scope\` 重构为按 \`sessionId\` 寻址，从而支持单一 resourceId 下的多会话。配套还带来 WorkspaceSandbox 的原生 filesystem API、Connect 的按端用户连接隔离以及 Microsoft Teams 渠道。版本包含若干破坏性变更：\`querySpans\(\)\` 移除 \`model\`/\`provider\` 过滤并从响应剔除 \`cost\`、\`inputTruncated\`、\`outputTruncated\` 字段，线程行查询路径改用 \`timeRange.traces\`/\`timeRange.threads\`，跨进程 \`DurableAgent.observe\(runId\)\` 在 agent ID 不匹配时将抛出 \`DURABLE\_AGENT\_OBSERVE\_AGENT\_MISMATCH\`。

github · Patrycja-J · 10月21日 12:28

**「会话寻址模型」** 此前，Mastra Agent Controller 以 \`resourceId\` 与 \`scope\` 的组合标识会话，并通过 \`getSessionByResource\(resourceId, scope\)\` 查找；其中 \`resourceId\` 同时承担会话定位和线程、记忆所有者两种职责。1.79.0 将两者拆分，由 \`sessionId\` 负责会话寻址，\`resourceId\` 仅标识线程与记忆的归属，为同一 resource 下管理多个独立会话提供了模型基础。

**「影响」** 依赖 \`querySpans\(\)\` 返回 \`cost\` 等字段进行 token 计费的下游流程将因响应字段被移除而需要等待存储适配器升级；与此同时，仍使用 \`resourceId + scope\` 组合调用会话 API 的代码必须迁移到 \`controller.getSession\(sessionId\)\` 等基于 \`sessionId\` 的新签名，否则会因破坏性变更而报错。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.79.0">mastra-ai/mastra released @mastra/core@1.79.0</a></li>

</ul>
</details>

**标签**: `#mcp`, `#agent-frameworks`, `#observability`, `#developer-tools`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [LiteLLM 1.107.0 供应链投毒事件](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/) ⭐️ 7.0/10

**级别**: 核心必看

Wiz 报告称，LiteLLM 1.107.0 于 2026 年 10 月 21 日 11:39 UTC 被上传至 PyPI，并被植入凭据窃取器和后门；PyPI 于同日 13:20 UTC 隔离了该版本。此次入侵涉及 3 个被盗的开发者 GitHub 凭据，GHCR 和 Docker Hub 的相关镜像标签也曾被植入，受影响标签约在 13:53 UTC 被移除。报告列出的最近安全版本为 v1.106.2。

hackernews · abhisek · 10月21日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=50181114)

**「LiteLLM 的代理角色」** LiteLLM 是面向开发者的 LLM 代理软件，而不是模型本身；依赖它的服务通过代理访问模型提供商，因而可能在运行时接触 API 凭据。评估这类组件的供应链风险时，Python 包版本与 GHCR、Docker Hub 等容器镜像标签需要一起核对，因为它们是同一软件的不同分发入口。

**「依赖方需回退并核查镜像」** 使用 LiteLLM 的开发和运维团队应暂时固定到 v1.106.2 或其他确认未受影响的版本，移除或隔离 1.107.0，并核查是否拉取过 GHRC 或 Docker Hub 上同期受影响的镜像标签。现有材料未说明凭据窃取器具体读取哪些秘密，因此不能据此断言所有环境都已发生凭据泄露。

**「评论者担忧多账户失陷与权限疲劳」** 评论者对 3 个开发者 GitHub 凭据同时被盗感到不安，认为这可能反映更系统性的账户安全问题；一名评论者建议在进一步通知前将 LiteLLM 固定在恶意版本发布之前。另有评论指出，沙箱和权限规则未必能阻止安装时发生的供应链攻击，因为开发者可能因反复授权而形成权限疲劳。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/">Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor</a></li>

</ul>
</details>

**标签**: `#ai-security`, `#supply-chain`, `#litellm`, `#python`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [OpenAI 模型与 Codex 将进入 Google Cloud](https://openai.com/index/openai-models-google-cloud/) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 宣布，其前沿模型和 Codex 智能体工作流将进入 Google Cloud 的 Model Garden，企业客户可通过 Google Cloud Marketplace 购买。现有 Google Cloud 消费承诺可用于抵扣这些采购。这是云分发和采购安排，并非新模型发布；现有材料未列出具体模型版本或正式上线日期。

hackernews · AI 热榜 · 10月21日 12:53 · [社区讨论](https://news.ycombinator.com/item?id=50180079)

**「云分发背景：OpenAI 与 Microsoft 的关系及跨云模型市场」** OpenAI 模型此前主要通过 Microsoft Azure 提供推理服务，与 Microsoft 形成了深度绑定的云合作关系，因此向 Google Cloud 分发属于对其既有云分发格局的明显扩展。与此同时，Anthropic 等其他前沿模型供应商已在 Google Cloud、AWS 和 Azure 等多个超大规模云平台上分发模型，Google Cloud 的 Model Garden 正是汇聚 Gemini、第三方及开源模型的统一企业 AI 平台，这为 OpenAI 模型进入同一采购框架提供了现成渠道。

**「GCP 客户可整合云消费承诺」** 已签订 Google Cloud 消费承诺的企业将多一条 OpenAI 模型采购渠道，并可按公告所述抵扣相关购买；具体适用范围仍取决于后续 Marketplace 条款。当前信息未说明正式上线时间、可用区域、模型版本、SLA 或数据处理条件，因此不能认定所有模型及 GCP 客户均已可用。

**「评论者关注收入竞争与微软关系」** 有评论者认为，允许用 GCP 承诺抵扣 OpenAI 采购，可能促使 Google 用既有云消费承诺争取模型推理收入；这是评论者的财务推测，实际影响取决于抵扣条款。另一位评论者指出，公告免责声明仍称 Microsoft 是 OpenAI 的主要云合作伙伴，也有人将此举解读为应对 Anthropic 的云端推理竞争，但现有材料未验证这些动机。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://openai.com/index/openai-models-google-cloud/">OpenAI models are coming to Google Cloud</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers">Google Cloud brings OpenAI models to customers | Google Cloud ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Google Cloud`, `#AI deployment`, `#enterprise infrastructure`

---

<a id="item-tech-news-5"></a>
### [Commerce.com 启用近 10 万域名 WebMCP 购物工具](https://blog.cloudflare.com/webmcp-commerce/) ⭐️ 7.0/10

**级别**: 核心必看

Cloudflare 表示，Commerce.com 旗下近 10 万个域名现已通过 WebMCP 向 AI 代理提供实际购物工具。该部署覆盖 Commerce.com 的每个商店，同时保留各个商户的控制权，但现有来源未说明商户可控制的具体功能或配置范围。

rss · Cloudflare AI · 10月21日 13:00

**「WebMCP 的作用」** Cloudflare 将代理式商务描述为让 AI 购物代理能够发现、浏览网站并执行交易，同时保留治理和控制；此次部署使用 WebMCP 向代理提供商店的实际购物工具。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://blog.cloudflare.com/webmcp-commerce/">How Commerce.com and Cloudflare are getting storefronts ready for AI agents</a></li>
<li><a href="https://www.cloudflare.com/solutions/agentic-commerce/">Agentic Commerce - Cloudflare</a></li>

</ul>
</details>

**标签**: `#WebMCP`, `#MCP`, `#AI agents`, `#agentic commerce`, `#Cloudflare`

---

<a id="item-tech-news-6"></a>
### [OpenAI 发布 Codex PHP 漏洞自查技能](https://x.com/OpenAI/status/2112945805686604033) ⭐️ 7.0/10

**级别**: 核心必看

OpenAI 宣布提供一项 Codex 技能，引导网站运营者和开发者运行 github.com/openai/php2shell-checker，检查 PHP 站点是否受相关关键漏洞影响。OpenAI 称，此项工作来自 Patch the Planet 计划，修复涉及对 PHP 引擎的大幅改动，并在约两个月协调后披露；建议的处置方式是升级 PHP 版本并应用安全厂商提供的缓解措施。当前公告未列出受影响版本、安装步骤或漏洞技术细节，因此无法据此确认工具的具体覆盖范围和部署条件。

rss · AI 热榜 · 10月21日 16:35

**「特定 PHP 漏洞的排查背景」** OpenAI 称，相关 PHP 引擎缺陷是在 Patch the Planet 计划中由模型协助研究员发现的，修复涉及引擎本身的大幅改动，并在约两个月协调后才披露。因此，这项 Codex 技能面向该特定漏洞的影响排查，并非覆盖所有 PHP 风险的通用扫描器。

**「站点需先排查运行时暴露」** 这使 PHP 站点运营者可以把响应重点放在运行时暴露：相关 PHP 2 Shell 缺陷位于 PHP 运行时而非应用代码，网站即使自身代码没有明显问题，也不能仅靠代码审查排除风险。运营者可先运行 \`github.com/openai/php2shell-checker\` 做影响排查，再依据结果升级 PHP 或采用安全厂商的缓解措施。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/OpenAI/status/2112945805686604033">OpenAI 发布 Codex 技能帮助网站自查 PHP 关键漏洞影响</a></li>
<li><a href="https://lean.shengsuanyun.com/apidocs/hot/b31hjqo2l088vfydp5gcdyv8p-openai-codex-php">OpenAI 发布 Codex 技能帮助网站自查 PHP 关键漏洞影响 - 胜算云 API 文档</a></li>
<li><a href="https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html">PHP Issues Emergency Patches for Two Critical PHP 2 Shell RCE...</a></li>

</ul>
</details>

**标签**: `#OpenAI Codex`, `#PHP 安全`, `#漏洞检测`, `#开发者工具`

---

<a id="item-tech-news-7"></a>
### [OpenAI API 新增 12 小时提示缓存](https://x.com/thsottiaux/status/2112712984644784534) ⭐️ 7.0/10

**级别**: 核心必看

据帖文转述的 OpenAI 开发者账号公告，OpenAI API 现已提供可选的 12 小时 prompt 缓存，持续运行的智能体即使间隔数小时再次发起请求，也可按更低的缓存输入费率复用指令、工具和上下文。Tibo 补充称，Codex 与 Work 中的已登录用户可永久保留缓存，重新打开旧对话或数小时后恢复会话时据称会命中缓存，且没有额外惩罚；这些条件并非面向所有 API 客户。

rss · AI 热榜 · 10月21日 01:10

**「理解缓存期限」** Prompt 缓存针对重复出现的指令、工具定义和上下文前缀，使后续请求可复用此前处理过的内容；此次增加的是可选的缓存保留时长。它不等于模型本身形成永久记忆：API 的 12 小时选项与 Codex、Work 登录用户会话恢复时的永久缓存保证属于不同层级的可用性承诺。

**「调用条件需按账户确认」** 长时间运行的智能体调用方需要确认并选择相应的 12 小时缓存选项；源码仅将永久保留和恢复会话时的缓存命中保证限定为 Codex 与 Work 已登录用户，其他账户不应默认适用这些条件。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://x.com/thsottiaux/status/2112712984644784534">OpenAI API 支持 12 小时 prompt 缓存，Codex 与 Work 用户缓存永久保留</a></li>

</ul>
</details>

**标签**: `#prompt-caching`, `#openai-api`, `#codex`, `#ai-coding-tools`, `#developer-workflow`

---

### 更多动态

<a id="item-tech-news-8"></a>
#### [Copilot CLI v1.0.102 更新代理、沙箱与模型选择](https://github.com/github/copilot-cli/releases/tag/v1.0.102) ⭐️ 6.0/10

GitHub 发布 Copilot CLI v1.0.102，为脚本化与代理式工作流改进了模型选择、权限继承和运行环境。提示模式现在可在 -p 命令及管道标准输入运行中使用托管的 Auto 模型；子代理可继承自定义工具和 MCP 工具审批，插件市场新增对 git-subdir 来源及长描述的支持。该版本还修复了包含 --effort 等选项别名的 Fish 命令补全，以及组织插件准备阻塞聊天消息发送的问题。沙箱中的长时间命令可持续运行超过 10 秒；被提供商过载错误截断的回复会退避重试并显示提供商消息和请求 ID，沙箱继承主机代理设置时也会遵循 NO\_PROXY 和 ALL\_PROXY。

github · copilot-cli-release-app\[bot\] · 10月21日 18:05