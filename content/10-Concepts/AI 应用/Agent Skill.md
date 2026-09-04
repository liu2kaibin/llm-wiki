---
type: concept
domain: AI 应用
tags:
  - AI 应用
  - agent
status: seed
created: 2026-09-04
source: "https://x.com/XiaohuiAI666/status/2095130302381494664"
---
# Agent Skill

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：Skill 就是给 AI 装的插件——一个文件夹加一份 SKILL.md 说明书，Agent 启动时把名字和描述预载进系统提示词，干活时自己判断调用哪个。】

## 它解决什么问题
裸模型像聪明但两手空空的实习生；Skill 把流程纪律、领域知识、工具操作固化成可复用的能力包，不用每次在对话里重新教。

## 工作原理
- 一个文件夹 = 一个 Skill：`SKILL.md`（名字、用途、执行流程）+ 可选脚本与参考文件
- 安装位置：`~/.codex/skills/` 全局生效；项目内 `.codex/skills/` 只对该项目生效
- Agent 启动时预加载全部技能名+描述，按任务自主选用
- 开放标准：agentskills.io；Codex 官方精选 39 个（openai/skills 仓库）

## 关系
- **相关**：[[Agent 与工具调用]]（Skill 是工具调用的「说明书化」）
- **对比**：WorkBuddy 类平台走社区大卖场（7 万+技能），Codex 走精品店路线（官方 39 个 + 开放标准自淘）

## 常见误解
- 装得越多越好——每个技能都消耗上下文窗口，装太多反而让模型选技能时判断失准

## 出处
- [Codex 最推荐的 15 个 skill（@XiaohuiAI666）](https://x.com/XiaohuiAI666/status/2095130302381494664)
- [/show-me：让 PR 描述极可读的技能（@mattpocockuk）](https://x.com/mattpocockuk/status/2095460192871698728)
- [book-to-skill：把一本书炼成 Skill 的开源项目](https://github.com/virgiliojr94/book-to-skill)
