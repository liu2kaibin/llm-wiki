---
type: concept
domain: AI 应用
tags:
  - AI 应用
  - architecture
status: seed
created: 2026-09-04
source: "https://x.com/oops073111/status/2095341660385509463"
---
# Ontology 语义层（Palantir）

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：Palantir 的护城河不在单点技术，而在 Ontology——把企业的数据、逻辑、行动统一建模成对象/属性/链接/动作，让 AI 的输出能直接变成业务操作。】

## 它解决什么问题
企业的 AI 要落地，卡点从来不是模型而是「AI 输出如何对接真实业务」——数据分散、语义不一致、行动无法闭环。

## 工作原理
- 对象、属性、链接、动作四类建模原语构成语义层
- 产品线分工：Foundry（数据平台）+ AIP（AI 平台层）+ Apollo（交付/运维），Ontology 是贯穿的核心
- 配套：多模态数据平面（文档/图像）、互操作层（API/外部系统）、Rubix 混合部署基础（边缘到云）

## 关系
- **相关**：[[Agent 与工具调用]]（Ontology 的 Action 本质是「给企业的工具调用层」）、[[RAG]]（语义层是比向量检索更结构化的企业知识组织方式）

## 常见误解
- 把 Palantir 当大数据公司——它本质是语义建模公司；FDE（前沿部署工程师）模式的瓶颈也在领域建模能力而非算法

## 出处
- [Palantir 架构中心中文全解系列（7 篇，@oops073111）](https://x.com/oops073111/status/2095341660385509463)，编译自 palantir.com Architecture Center
