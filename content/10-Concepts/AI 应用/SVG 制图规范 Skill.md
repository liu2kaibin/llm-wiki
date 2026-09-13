---
type: concept
domain: AI 应用
tags:
  - AI 应用
  - agent
status: seed
created: 2026-09-13
source: "https://x.com/Jolyne_AI/status/2098774641586377038"
---
# SVG 制图规范 Skill（svg-diagram）

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：AI 画架构图翻车的根因是「怎么画」没有规矩——这个 Skill 把规范写成硬约束再配 12 项成品校验，让 SVG 从看运气变成可交付。】

## 它解决什么问题
Claude Code/Codex 顺手生成的 SVG 架构图连线乱拐、字号不齐、间距靠猜；这类问题靠 prompt 修不好，要靠规范+校验闭环。

## 工作原理（bybit-exchange 开源）
- **规范前置**：框高跟字号走、拐弯只用曲线、箭头到目标框固定留白 11px、文字基线公式写死
- **零依赖检查器**：读最终 SVG 做 12 项硬核校验（转义、留白、字体、重叠、配色），报错点名到具体数值（如「边距 11，应为 20-25」）
- **中英双字符宽度表**：中文按「每字一个字号」算宽，落笔前判定是否溢出
- **视觉规范**：字体栈强制 Noto Sans CJK SC、五组语义配色、自带白底（暗色主题不脏）
- 覆盖架构图、流程图、时序图、数据流、状态机五类；一条命令接入 Claude Code、Codex、Cursor、Gemini CLI

## 关系
- **相关**：[[Agent Skill]]（「规范+校验」型 Skill 的范本）、[[AI 插画生成]]（同为「AI 出图」的工程化路线）
- **对本 wiki**：卡片里的架构图/流程图可以直接用它替代手画

## 常见误解
- 【改成你的话】

## 出处
- [svg-diagram Skill（@Jolyne_AI）](https://github.com/bybit-exchange/svg-diagram)
