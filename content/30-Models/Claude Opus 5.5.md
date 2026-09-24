---
type: model
domain: llm
tags:
  - model
status: seed
created: 2026-09-24
developer: "Anthropic"
released: 2026-09
params: ""
context_window: ""
open_weights: false
url: "https://x.com/ArtificialAnlys/status/2102932119995756613"
---
# Claude Opus 5.5

> [!abstract] 定位一句话
> AA Coding Agent Index 新科状元（66 分，历史最高）：能力上限往上推了一截，但每任务成本也更贵——帕累托前沿的高成本端被它顶开。

## 关键事实
- **Coding Agent Index 66 分**：超过 Fable 5.1（62）、Opus 5（60）；三项评估全面提升——Terminal-Bench 4.0 +8.6pp（54.5→63.1%）、DeepSWE v1.1（62.5→68.4%）、SWE-Atlas-QnA（62.1→66.4%）
- **AA 智能指数 58 分**：超过 Fable 5.1 和 GPT-6 Astra（均 53）
- **单价降、总价升**：输入/输出降至 $4/$20（-20%）、缓存读 $0.20（-60%）；但每任务 $13.04（+21%），因每任务消耗约 1560 万令牌（输出约为 Opus 5 的 2.4 倍）——典型的「更聪明但更能烧」
- **同期对手**：OpenAI 同周发布 GPT-6 Sol（48 分）/ Luna（37 分），价格均为前代一半，但未追上 Opus 5 的 51 分

## 技术要点
- 评估设置为 Claude Code「最大努力模式」；低价高耗说明推理规模扩大（可能是更长的思考与更多工具轮次）

## 相关笔记
- [[Muse Spark 1.3]]、[[MiMo 2.6]]、[[输出蒸馏与模型相似度]]、[[模型分工与赛马]]（贵模型适合放方案阶段）

## 出处
- [AA：Opus 5.5 登顶 Coding Agent Index](https://x.com/ArtificialAnlys/status/2102932119995756613)
- [Opus 5.5 vs GPT-6 Sol/Luna 对比（@ScarletKc）](https://x.com/ScarletKc/status/2102570634027102447)
