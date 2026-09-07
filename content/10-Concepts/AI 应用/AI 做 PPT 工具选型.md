---
type: concept
domain: AI 应用
tags:
  - AI 应用
status: seed
created: 2026-09-07
source: "https://x.com/miles_mazy/status/2096410003590774997"
---
# AI 做 PPT 工具选型

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：AI 做 PPT 的选型第一问不是「哪个工具强」，而是「交付格式要不要可编辑」——决定了走 Markdown 演示还是原生 PPTX 路线。】

## 它解决什么问题
AI 生成演示的工具井喷，但输出格式、可编辑性、风格一致性差异巨大，不按场景选型会返工。

## 工作原理（场景 → 工具映射）
- **自己演讲/课件**：Slidev（代码高亮、公式、交互，适合技术分享）、Marp（文字图片为主的常规课件）——Markdown 驱动，改稿容易；局限：导出的 PPTX 是图片式，对方没法改字
- **正式交付/汇报答辩**：ppt-master（保留可编辑文字和图表）、slide-skill（主题版式明确）、deck-dna（沿用公司已有风格）
- **科普/论文转演示**：baoyu-slide-deck（宝玉）、PPTAgent（从论文报告整理成演示）
- **已有图片稿改字换图**：Image2PPTX、LRriver/AIPPT
- **生成-修改-导出一体**：codex-slides（先改大纲再改页面）、Presenton（模板+编辑+模型接入）
- **作者最终搭配**：自己讲课用 Marp 为主；正式交付用模板 + ppt-master + 生图

## 关系
- **相关**：[[Agent Skill]]（这些都是 Skill 形态）、[[AI 插画生成]]（配图环节的配套）

## 常见误解
- 把 Slidev/Marp 当原生 PPTX 替代品——对方要继续改文字和数据时不能用它交付

## 出处
- [史上最全 PPT 技能合集（@miles_mazy）](https://x.com/miles_mazy/status/2096410003590774997)
