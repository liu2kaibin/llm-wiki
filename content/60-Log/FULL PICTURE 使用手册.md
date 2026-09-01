---
type: log
title: FULL PICTURE 使用手册
tags:
  - manual
---
# FULL PICTURE：这个系统如何运作

## 0. 一句话

你在 Obsidian 里按纪律写卡片，其余一切（版本管理、备份、网站发布、隐私过滤）全自动。

## 1. 数据流全景

```
┌─ 捕获层（5 个入口）──────────────────────────────┐
│ ① Obsidian 手写   ② Web Clipper 剪藏             │
│ ③ arxiv_note.py   ④ Excalidraw 画图              │
│ ⑤ 对话 ZCode 代写                                  │
└───────────────┬─────────────────────────────────┘
                ▼
     content/00-Inbox/        原始素材（72h 内必须消化）
                ▼  复述 → 原子化 → 双链
     10-Concepts / 20-Papers / 30-Models   成熟卡片
                ▼  每周串联 2~3 张相关卡
     50-Essays                Karpathy 式长文
                │
                ▼ Obsidian Git（每 10 分钟 commit+pull+push）
     GitHub 仓库               私有内容源 + 全量版本历史
                ▼ push 触发 GitHub Actions（约 2 分钟）
     Quartz 构建               00-Inbox / 60-Log / 90-Templates 被排除
                ▼
     liu2kaibin.github.io/llm-wiki   公开网站（搜索/图谱/反链）
```

## 2. 所有写笔记的方式

| # | 方式 | 操作 | 落点 | 是否上网 |
|---|------|------|------|---------|
| 1 | 手写概念卡 | 在 `10-Concepts` 新建笔记，模板自动套 | 10-Concepts | ✅ |
| 2 | 网页剪藏 | 浏览器点 Obsidian 图标 → Save | 00-Inbox | ❌ |
| 3 | 论文卡片 | `python scripts/arxiv_note.py <arxiv_id>` | 20-Papers | ✅（骨架） |
| 4 | 模型档案 | 在 `30-Models` 新建笔记 | 30-Models | ✅ |
| 5 | 学习日志 | 在 `60-Log` 写每日流水 | 60-Log | ❌ |
| 6 | 长文写作 | 在 `50-Essays` 新建笔记 | 50-Essays | ✅ |
| 7 | 画直觉图 | 新建 Excalidraw，导出嵌入卡片 | Assets | ✅（随卡片） |
| 8 | 让 ZCode 代写 | 对话让我抓取/总结/生成卡片 | 任意 | 同落点 |
| 9 | PDF 精读 | PDF 拖进 `Assets`，Obsidian 内直接标注 | Assets | ❌ |

## 3. 端到端实例：一条 KV-Cache 知识的一生

**Day 1 · 捕获（30 秒）**
刷到一篇讲 KV-Cache 优化的博客 → 点浏览器 Obsidian 图标 → Save。
文件出现：`content/00-Inbox/Decode 优化新思路.md`（正文+原文链接）。
什么都不用管，10 分钟内它已被自动推送到 GitHub。

**Day 1 · 消化（15 分钟）**
晚上打开 Obsidian：
1. 读 Inbox 里这篇剪藏；
2. 在 `10-Concepts` 新建「PagedAttention」→ 模板自动展开；
3. 用自己的话填 TL;DR、原理；原文链接写进「出处」；
4. 正文里打到相关概念就打双链：`[[KV-Cache]]`、`[[量化]]`、`[[长上下文]]`；
5. frontmatter 里 `status: seed` 改 `growing`；
6. Inbox 原文删除（内容已吸收进卡片和出处链接）。

**Day 1 · 发布（0 操作）**
下次自动备份后，网站约 2 分钟内多出一个页面，图谱里 PagedAttention
与 KV-Cache 之间连出一条边，站内搜索可命中。

**Weekend · 串联（1 小时）**
发现 KV-Cache、量化、PagedAttention 三张卡能讲一个完整故事 →
在 `50-Essays` 新建《LLM 推理显存都花在哪了》，长文模板骨架已备好，
引用三张卡（`[[KV-Cache]]` 等），补一段动手验证代码 → 发布后这就是
你网站上第一篇真正的"Karpathy 式文章"。

## 4. 各目录职责

```
content/
├── index.md         网站首页 + Obsidian 总索引（Dataview 自动表）
├── WORKFLOW.md      工作流规则（主循环/纪律）
├── 00-Inbox/        剪藏与速记；72h 清空；不上网
├── 10-Concepts/     概念卡（一张卡一个概念）
├── 20-Papers/       论文卡（脚本生成骨架）
├── 30-Models/       模型档案
├── 50-Essays/       原创长文（网站的核心价值）
├── 60-Log/          学习日志，不上网（本手册也在这）
├── 90-Templates/    五个模板，改模板格式在这
└── Assets/          图片 / PDF / 附件
仓库根目录（不用 Obsidian 打开）：
├── quartz.config.yaml     站点标题/主题/发布范围(ignorePatterns)
├── .github/workflows/     push 自动部署
└── scripts/arxiv_note.py  论文工具
```

## 5. 核心纪律（比工具重要）

1. Inbox 不是家：72 小时内消化或删除；
2. 复述门槛：卡片必须是自己的话，剪藏原文只留在出处；
3. 原子性：一张卡只讲一件事，岔开了就开新卡并双链回来；
4. 直觉优先：先写"一句话直觉"，公式放后面；
5. 状态流转 seed → growing → evergreen，evergreen 标准＝能给人讲 10 分钟不卡壳。

## 6. 节奏建议

- 每天 15 分钟：1 张卡；
- 每周末 1 小时：清 Inbox + 1 篇长文草稿；
- 每月：打开图谱视图，把"孤岛节点"连进主图。
