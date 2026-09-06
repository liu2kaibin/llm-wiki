---
type: concept
domain: llm
tags:
  - llm
  - speech
status: seed
created: 2026-09-06
source: "https://x.com/wquguru/status/2096013016429211791"
---
# 开源 ASR 与 TTS（本地语音模型）

> [!abstract] TL;DR 一句话直觉
> 【改成你的话：开源语音模型已经能在 16GB 内存的 MacBook 上本地跑，多语种 ASR 的准确率甚至超过 Azure、ElevenLabs 这类闭源 API——语音这件事不再必须上云。】

## 它解决什么问题
语音转文字（ASR）和文字转语音（TTS）此前依赖闭源 API：按量付费、数据出域、离线不可用。开源模型补上了本地化这条线。

## 工作原理（代表模型）
- **Hojo-ASR-Multi-V1**（负责听）：Open ASR Leaderboard 多语种榜 WER 超过 Azure/ElevenLabs 闭源 API；支持德法西意葡 + 普通话、粤语
- **Hojo-TTS-Light-40M**（负责说）：4000 万参数的 ONNX 小模型，CPU 可跑——小模型 + ONNX 化是本地部署的关键组合（参见 [[量化]]）
- 运行门槛：16GB 内存以上的 MacBook 即可
- 背景：HuggingFace 被英伟达以 130 亿美元收购，开源模型仓库价值重估

## 关系
- **相关**：[[量化]]（本地可跑的前提）、[[预训练]]（基座+微调的开源生态）
- **应用**：会议纪要（配合 Whisper 类工具）、离线语音助手、隐私敏感场景

## 常见误解
- 【改成你的话】

## 出处
- [图解 ASR 和 TTS：HuggingFace 开源模型测评（@wquguru）](https://x.com/wquguru/status/2096013016429211791)
