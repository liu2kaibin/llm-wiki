---
type: moc
tags:
  - workflow
---
# WORKFLOW 工作流

## 一条主循环：捕获 → 消化 → 连接 → 写作

```
剪藏/论文/视频 ──▶ 00-Inbox（原文+速记）
                     │
                     ▼  用自己的话复述，一张卡一个概念
              10-Concepts / 20-Papers / 30-Models（原子卡片）
                     │
                     ▼  [[链接]] 优先，让图谱自己生长
              每周把 2~3 张相关卡片串成一篇 50-Essays 长文
```

## 规则

1. **Inbox 不是家**：素材进 Inbox 后 72 小时内要么消化成卡片，要么删掉。
2. **复述门槛**：卡片内容必须是自己复述的话，剪藏原文放「出处」小节。
3. **原子性**：一张卡只讲一个概念；写的时候发现要岔开，就新建卡片并 `[[链接]]` 回来。
4. **直觉优先（Karpathy 纪律）**：每张卡先写"一句话直觉"，再写公式；每篇长文先画图再写字。
5. **状态流转**：`seed → growing → evergreen`。evergreen 的标准是：能给同事讲 10 分钟不卡壳。

## 素材通道

| 通道 | 工具 | 落点 |
| ---- | ---- | ---- |
| 网页 | Obsidian Web Clipper（浏览器扩展） | `Clippings/`（默认目录；仅本地，不入仓库不上网） |
| 论文 | `python scripts/arxiv_note.py <arxiv_id> [domain=xx]` | 20-Papers |
| 视频 | YouTube（Karpathy Zero to Hero 等），记时间戳笔记 | Clippings/ |
| 订阅 | Karpathy 博客 / Lil'Log / Jay Alammar / Ahead of AI / HF Blog | Clippings/ |

## 每周节奏

- 周中：随手剪藏 + 每天 1 张概念卡（15 分钟够）
- 周末：清空剪藏 + 串一篇长文草稿

## 内外有别（红线）

1. 公司内网页面（SharePoint 等）的剪藏**只存在本地 `Clippings/`**，已被 git 忽略、不会进入公开仓库和网站；
2. 内部资料只能提炼成**你自己的话**的卡片，且出处写「内部资料」，不带内网链接；
3. 拿不准是否涉密 → 先放 `60-Log/`（永不发布），确认后再挪进领域目录。
