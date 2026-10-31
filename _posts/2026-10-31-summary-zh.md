---
layout: default
title: "Horizon 每日速递：2026-10-31"
description: "AI 精选的技术与研究日报"
date: 2026-10-31
lang: zh
locale: zh-CN
---

> 从 40 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [Cursor Marketplace 的 Claude Code 扩展植入 SSH 密钥](#item-tech-news-1) ⭐️ 8.0/10
2. [NESformer：用约 1GB Qwen 权重运行 NES](#item-tech-news-2) ⭐️ 7.0/10
3. [Claude Code v2.1.316 加强子代理与网关控制](#item-tech-news-3) ⭐️ 6.0/10
4. [OpenCode v2.2.5 发布：工作树快捷键与百分比上下文压缩](#item-tech-news-4) ⭐️ 6.0/10
5. [AI 代理加速 SRE 排障，也带来技能退化风险](#item-tech-news-5) ⭐️ 6.0/10
6. [Wiz 汇总至少九起 AI 开发者平台安全事件](#item-tech-news-6) ⭐️ 6.0/10
7. [Kimi K3.1 Pro 发布 3D 创作教程](#item-tech-news-7) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Cursor Marketplace 的 Claude Code 扩展植入 SSH 密钥](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 8.0/10

**级别**: 核心必看

Anthropic 表示，攻击者利用对 Cursor Marketplace 的访问权限发布了一个并非由 Anthropic 构建或发布的 Claude Code 篡改扩展；该扩展会把标为 \`svc-telemetry\` 的攻击者 SSH 公钥追加到开发者的 \`~/.ssh/authorized\_keys\`。Anthropic 官方渠道提供的版本不受影响，事件影响范围限于 Cursor 用户，并未涉及 Anthropic 系统或员工笔记本。开发者可以检查授权密钥文件中是否存在 \`svc-telemetry\` 标记，以确认系统是否受影响。

hackernews · \_chall · 10月30日 07:09 · [社区讨论](https://news.ycombinator.com/item?id=50300683)

**「恶意构建的发现与处置」** Phorion 最初披露，Cursor Marketplace 中一个被篡改的 Claude Code VS Code 扩展会在 macOS、Linux 和 Windows 上植入持久化 SSH 后门。Cursor 随后发布正式安全公告，将暴露时段界定为约太平洋时间凌晨 2:27 至下午 1:35；后续由版本 2.1.314 取代恶意构建，问题仍限于该市场中的篡改副本。

**「受影响用户应核查 SSH 授权」** Cursor Marketplace 的受影响用户应立即检查 \`~/.ssh/authorized\_keys\` 中是否存在标记为 \`svc-telemetry\` 的公钥；该条目会让持有对应私钥的一方获得 SSH 授权，若发现应移除该条目并另行审查登录记录。Cursor 公告称至多 5,000 名用户受影响并将直接联系他们；Anthropic 官方渠道的版本不受影响，因此核查重点是曾从 Cursor Marketplace 安装该扩展的机器，而不只是更新扩展。

**「讨论集中于责任归属与受影响范围」** Felix（Anthropic）称事件源于攻击者获得 Cursor Marketplace 的发布权限，并表示正与 Cursor 协作处理；评论者则追问篡改版本如何进入市场以及它与 Anthropic 原版的关系。有人认为 Open VSX 和 Cursor Marketplace 涉及其中，但对 Microsoft 官方扩展市场是否受影响表示不确定，因此不能据此认定该市场同样受影响。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/">Backdoor in Claude Code for VS Code extension on the Cursor Marketplace</a></li>
<li><a href="https://cursor.com/blog/claude-code-extension-security-notice">Security notice — malicious version of Anthropic. claude - code ...</a></li>
<li><a href="https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html">Official Claude Code Extension on Cursor Marketplace ...</a></li>

</ul>
</details>

**标签**: `#AI coding tools`, `#coding-agent security`, `#Claude Code`, `#Cursor Marketplace`, `#supply-chain compromise`

---

<a id="item-tech-news-2"></a>
### [NESformer：用约 1GB Qwen 权重运行 NES](https://github.com/dbreunig/nesformer) ⭐️ 7.0/10

**级别**: 核心必看

开源项目 NESformer 用约 1GB 的 Qwen 权重实现了一个可工作的 Nintendo Entertainment System（NES）。作者称，Opus 5.5 编码代理仅通过两次提示就生成了可运行权重和代码；该项目报告的运行速度比真实主机慢 150–290 倍，该性能数字尚不能视为独立基准。

hackernews · dbreunig · 10月30日 16:40 · [社区讨论](https://news.ycombinator.com/item?id=50306442)

**「从软件模拟到权重内执行」** 传统 NES 模拟器是在软件中确定性地执行 6502 CPU、2 KB 工作 RAM 和卡带 ROM；NESformer 则没有通过训练让 Qwen 学会模拟，而是由编译器将这些电路与状态编码进现成 Qwen3.5 检查点的权重，再让模型逐 token 预测 CPU 执行轨迹。其正确性依据是与常规模拟器日志对齐：官方仓库称参考 CPU 匹配 nestest 的 3,348 条指令，并与 py65 在 570 万条游戏指令上保持一致。

**「实际意义」** 该项目为研究神经网络如何承载确定性的硬件仿真，以及编码代理能否生成可运行权重，提供了一个开源实验样例。不过，按项目方报告的 150–290 倍速度差距，它目前更适合作为计算与代理能力研究对象，而非日常 NES 模拟器。

**「社区讨论」** 评论者提出，可以尝试把小型虚拟机编译进权重，让模型在内部执行 Python、shell 和 grep 等工具；这是尚待验证的研究设想。另一位评论者虽欣赏这类实验，但强调其效率极低，认为它反而凸显了确定性程序相较于 LLM 的效率优势。

<details><summary>来源依据</summary>
<ul>
<li><a href="https://github.com/dbreunig/nesformer">Show HN: A working Nintendo in ~1GB of Qwen weights</a></li>
<li><a href="https://daily.dev/posts/a-working-nintendo-in-1gb-of-qwen-weights-sbrwwn5e8">A Working Nintendo in ~1GB of Qwen Weights - daily.dev</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Qwen`, `#neural-network computation`, `#NES emulation`, `#open source`

---

### 更多动态

<a id="item-tech-news-3"></a>
#### [Claude Code v2.1.316 加强子代理与网关控制](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) ⭐️ 6.0/10

Claude Code v2.1.316 已发布：新增 \`CLAUDE\_CODE\_SUBAGENT\_EFFORT\`，可在未显式指定时为子代理设置 effort，而不再继承会话设置；同时可用 \`CLAUDE\_CODE\_DISABLE\_ULTRATHINK\` 关闭 \`ultrathink\` 关键字，并用 \`CLAUDE\_CODE\_DISABLE\_LOOPED\_CROSS\_CERT\_DROP\` 保留互相签发的系统交叉证书。Claude apps gateway 新增通过 spend limits admin API 的 \`pooled\_budget\` 设置组内成员共享的月度预算（叠加成员各自上限）、通过 \`managed.policy\_mode: layered\` 合并所有匹配开发者的策略，以及面向 Bedrock 上游的 \`guardrail.input\_tagging\`，后者以 Amazon Bedrock guardrail 的 prompt attacks filter 所需输入标签封装提示词，\`all\_messages\_and\_system\` 还会标记系统提示词。兼容性方面，Opus 4.8 的 fast mode 已于 2026 年 10 月 30 日弃用，并将于 11 月 30 日移除；移除后相关请求会直接报错且不会回退到标准 Opus 4.8，官方建议迁移到 Opus 5.5。发布说明还列出多项修复，包括 Vertex AI 和 Amazon Bedrock 在最新模型尚未向账户或区域开放时改用较旧模型、网关检查请求中提到的每个模型并对被阻止模型返回含字段名的 400，以及避免 Claude Code 自行退出后在 macOS 和 Linux 上遗留 shell 进程。

github · ashwin-ant · 10月31日 01:01

<a id="item-tech-news-4"></a>
#### [OpenCode v2.2.5 发布：工作树快捷键与百分比上下文压缩](https://github.com/anomalyco/opencode/releases/tag/v2.2.5) ⭐️ 6.0/10

OpenCode v2.2.5 已发布，新增 worktree、基线分支与 shell 模式快捷键：macOS 分别使用 ⌘⌥O、⌘⌥B 和 ⌘⇧X，Windows/Linux 使用 Ctrl+Alt+O、Ctrl+Alt+B 和 Ctrl+Shift+X。评论弹窗现在可按住 ⌘/Ctrl，或使用 ⌘Enter/Ctrl+Enter，仅发送当前引用及评论而不清空其余输入。\`opencode.json\` 中的 \`compaction.buffer\` 除 token 数外也接受百分比（例如 \`&quot;20%&quot;\`），可按模型上下文窗口比例预留空间；本版还修复了超过 10 MiB 的 MCP stdio 消息断连、LiteLLM 上下文错误终止会话，以及切换模型或恢复响应时 reasoning 被转为纯文本等问题。

github · github-actions\[bot\] · 10月30日 23:17

<a id="item-tech-news-5"></a>
#### [AI 代理加速 SRE 排障，也带来技能退化风险](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) ⭐️ 6.0/10

这篇面向 SRE 团队的分析主张，AI 代理虽然能加快常规故障调查，但不应导致工程师的手动排障和运维判断能力退化。文章建议，即使某些事件本可由 AI 处理，也刻意保留一部分供人工实践，以维持团队应对故障的能力。该建议目前主要停留在工作方式层面，没有配套实现、基准测试或量化结果，因此其效果仍属于作者主张，而非经过独立验证的结论。

hackernews · dorianniemiec · 10月30日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=50305693)

<a id="item-tech-news-6"></a>
#### [Wiz 汇总至少九起 AI 开发者平台安全事件](https://www.wiz.io/blog/black-october-for-ai-developer-platforms) ⭐️ 6.0/10

Wiz 研究团队汇总了 10 月内至少九个 AI 开发者平台披露的安全事件，涉及 Fireworks AI、Lightning AI、Railway、Warp、OpenCode 等。多起报告指向凭据窃取、agent swarm 攻击，以及以“蒸馏”为目的的窃取，显示出重复出现的风险模式。这是一份事件汇总；现有材料未提供受影响版本、完整攻击链、缓解措施或修复建议，因此无法确认各事件的具体影响范围和处置状态。

rss · AI 热榜 · 10月30日 22:51

<a id="item-tech-news-7"></a>
#### [Kimi K3.1 Pro 发布 3D 创作教程](https://mp.weixin.qq.com/s?__biz=MzkzMTY4NTIyNA%3D%3D&amp;mid=2247484364&amp;idx=1&amp;sn=42491c3f098deb797ee8f2a17d147b3a) ⭐️ 6.0/10

月之暗面发布 Kimi K3.1 Pro 官方 3D 创作教程，讲解参数化建模与网格化建模两条路径及相应工具选择。教程通过 4 个案例展示具体操作，包括在 Unreal Engine 中构建东方天宫、制作可 3D 打印的台灯、纯代码调用 Blender 生成建筑，以及结合 Tripo 与 Blender 搭建微缩城市，并给出“图胜于言”、先搭灰模再细化等 5 条使用技巧。此次发布的是 AI 辅助创作工作流教程，而非新的模型版本或量化效果评测。

rss · AI 热榜 · 10月30日 04:04