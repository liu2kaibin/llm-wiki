---
type: moc
tags:
  - moc
---
# 🧠 LLM Wiki

> 以 [Karpathy](https://karpathy.bearblog.dev/) 的写作为标杆：直觉优先、亲手验证、长期沉淀。
> 工作流见 [[WORKFLOW]]。

## 📇 概念卡（10-Concepts）

```dataview
TABLE WITHOUT ID file.link AS "概念", status AS "状态", created AS "创建"
FROM "10-Concepts"
SORT status ASC, file.name ASC
```

## 📄 论文笔记（20-Papers）

```dataview
TABLE WITHOUT ID file.link AS "论文", year AS "年份", authors AS "作者"
FROM "20-Papers"
SORT year DESC
```

## 🤖 模型档案（30-Models）

```dataview
TABLE WITHOUT ID file.link AS "模型", developer AS "厂商", released AS "发布"
FROM "30-Models"
SORT released DESC
```

## ✍️ 长文（50-Essays）

```dataview
TABLE WITHOUT ID file.link AS "文章", status AS "状态", created AS "创建"
FROM "50-Essays"
SORT created DESC
```

## 📥 待消化（00-Inbox）

```dataview
LIST
FROM "00-Inbox"
SORT file.ctime DESC
```

---
状态说明：`seed` 种子（只有骨架）→ `growing` 生长中 → `evergreen` 成熟（可对外讲清楚）
