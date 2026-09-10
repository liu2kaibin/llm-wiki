---
type: concept
domain: AI 应用
tags:
  - AI 应用
  - agent
  - 资源
status: seed
created: 2026-09-09
source: "https://x.com/miles_mazy/status/2097154216267837847"
---
# Agent 架构学习三件套

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：学 Agent 架构的最短路径是三个开源项目按序通关——先亲手搭一个，再横向对比 35 种，最后补系统工程设计。】

## 它解决什么问题
想学 Agent 架构但资料零散：要么只有概念没有代码，要么只有代码没有工程视角。

## 工作原理（建议学习顺序）
1. **ai-agents-from-scratch**（先动手）：用 JavaScript + 本地模型从模型调用起步，逐步加入工具、记忆和 ReAct 循环，看清「选工具→读结果→定下一步」
2. **all-agentic-architectures**（再对比）：35 种 Agent 架构（工具调用、规划、记忆、RAG、多代理协作），同一任务换架构运行，观察拆任务与自检方式差异
3. **harness-books**（后补工程）：两本围绕 Claude Code 和 Codex 的第三方架构分析——任务持续执行、工具权限、长上下文处理、出错恢复

## 关系
- **相关**：[[Agent 与工具调用]]、[[Agent Skill]]、[[上下文工程]]（harness-books 正是这一主题的深化）、[[编码代理工作流]]
- **对照**：[[Agentic Design Patterns]]（模式理论）、[[AI 工程师必藏仓库]]（更大的仓库清单）

## 常见误解
- 【改成你的话】

## 出处
- [从零学 Agent 架构的三个 GitHub 项目（@miles_mazy）](https://x.com/miles_mazy/status/2097154216267837847)
