---
type: concept
domain: AI 应用
tags:
  - AI 应用
  - infrastructure
status: seed
created: 2026-09-21
source: "https://x.com/fankaishuoai/status/2101625967882199247"
---
# 个人 AI 工作站（单机全栈工作流）

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：一台 Mac Studio 当「AI 后端」，人只用笔记本/手机远程接入——Agent 管知识库、浏览器、GitHub、Cloudflare、Stripe，本地量化模型管推理；稳定工具组合胜过追新。】

## 它解决什么问题
工具太多、追新太累；把工作流收敛到一套稳定基础设施上，让 Agent 常驻干活，人随时随处接入。

## 工作原理（分层架构）
- **接入层**：Tailscale 虚拟网（任意设备接入）、Syncthing 文件同步、Parsec 远程桌面、Paseo 远程控制与多 Agent 编排（手机/iPad 可用）
- **调度层**：Bot 任务在 Paseo 配定时；非 AI 任务写 Python 脚本交给系统 cron——「不需要模型的任务别浪费模型」
- **Agent 层**：收敛到三个开源工具——Pi Agent、Codex CLI、DeepSeek Harness
- **挂载的基础设施**：Obsidian（知识库交给 Agent 管理）、常驻 Chrome（邮件、YouTube 后台、网页端模型）、GitHub（远程 PR）、Cloudflare（域名/部署/D1/R2，Agent 直接下命令）、Stripe（付款分析）
- **媒体层**：yt-dlp、FFmpeg-full、OpenMontage + 剪映
- **模型层（oMLX 本地推理）**：DeepSeek V4 2.4-bit、Qwen3.8-27B/Qwen3.6-35B-A3B 量化版；ASR 用 Qwen3-ASR/Whisper；TTS 用 Qwen3-TTS；情绪识别 SenseVoice；RAG 用 BGE-M3 + BGE-Reranker

## 权限最小化（评论区精华）
Stripe 给**只读**权限、Cloudflare 部署只给 **preview 环境**——付款和部署权限交出去，出错代价和普通工具完全不是一个量级（参见 [[编码代理自主性设计]] 的授权分层原则）。

## 关系
- **相关**：[[企业级 Harness 平台]]（同一命题的个人版：组织级加多租户与审计）、[[开源 ASR 与 TTS]] 与 [[量化]]（本地模型矩阵的可行性）、[[向量数据库]]（BGE-M3 检索层）、[[Windows 必装十款软件]]（Tailscale 双榜常客）、[[模型分工与赛马]]（作者观点相反相成：别追新模型，用真实工作流测）
- **哲学**：工具组合稳定 > 持续折腾；测模型要拿真实工作流测

## 常见误解
- 【改成你的话】

## 出处
- [我的 Mac Studio AI 工作站（@fankaishuoai 范凯）](https://x.com/fankaishuoai/status/2101625967882199247)
