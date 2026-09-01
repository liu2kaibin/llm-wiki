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
| 网页 | Obsidian Web Clipper（浏览器扩展） | 00-Inbox |
| 论文 | `python scripts/arxiv_note.py <arxiv_id>` | 20-Papers |
| 视频 | YouTube（Karpathy Zero to Hero 等），记时间戳笔记 | 00-Inbox |
| 订阅 | Karpathy 博客 / Lil'Log / Jay Alammar / Ahead of AI / HF Blog | 00-Inbox |

## 每周节奏

- 周中：随手剪藏 + 每天 1 张概念卡（15 分钟够）
- 周末：清空 Inbox + 串一篇长文草稿
