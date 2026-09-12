---
type: concept
domain: AI 应用
tags:
  - AI 应用
  - agent
  - architecture
status: seed
created: 2026-09-12
source: "https://x.com/robotbird01/status/2098044628058689738"
---
# 企业级 Harness 平台

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：个人 Harness 拼的是轻和快，企业 Harness 拼的是权限分层和可审计——身份上下文必须咬住整条执行链，一碰审计就现原形的是套壳。】

## 它解决什么问题
个人向 Harness（Claude Code、Pi 等）直接搬进企业会失灵：多用户多租户的权限、Skill 沉淀复用、安全审计，这些是组织级需求而非个体需求。

## 工作原理（基于 Pi Agent 的企业化架构）
- **底层**：Pi Agent 作为运行时，Less is More 的轻内核
- **三大企业化重点**：权限体系、Skill 复用、安全可控
- **权限分层链**：身份与权限上下文从 User → Workspace → Skill → Tool → Data → Credential → Sandbox 每一跳都要咬住，不能在中间环节丢失
- **相关生态**：字节 deerflow 覆盖类似功能；CubePlex（开源的团队级 Managed Agent Platform）
- **验收标准**：跑过真实业务、过得了审计——「光有框架没用」

## 关系
- **相关**：[[编码代理自主性设计]]（单代理的权限模型 vs 组织级的权限分层）、[[上下文工程]]（Harness 即上下文的组织化）、[[Agent Skill]]（Skill 复用是企业化的核心诉求）
- **对比**：个人 Harness 重轻量与速度；企业 Harness 重多租户、审计与可控

## 常见误解
- 【改成你的话】

## 出处
- [企业级 harness 平台架构图（@robotbird01）](https://x.com/robotbird01/status/2098044628058689738)，含评论区关于权限分层链与 deerflow/CubePlex 的讨论
