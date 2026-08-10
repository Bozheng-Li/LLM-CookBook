# LLM Cookbook 核心章节深化总览

日期：2026-08-09

## 已完成

围绕“大厂大模型算法工程师面试高频内容”，深化了 6 个核心页面：

- `pages/03-transformer/attention.html`：补充 Attention shape、复杂度与显存账本，Prefill/Decode，causal mask 与数值稳定性，MHA/MQA/GQA/MLA，RoPE 长上下文，FlashAttention 边界，面试模板与排障清单。
- `pages/06-pretraining/distributed-training.html`：补充 ZeRO-1/2/3、FSDP、TP/PP/EP 选型，pipeline bubble 与 micro-batch，MoE capacity factor/负载均衡，70B+128K 训练系统设计，OOM/吞吐排查。
- `pages/07-posttraining/dpo.html`：补充 DPO/IPO/KTO/ORPO/SimPO/GRPO 对比，偏好数据质量与长度偏差，beta/学习率/reference logprob 缓存，训练指标诊断和选型问答。
- `pages/08-inference/inference-scaling.html`：补充 test-time compute budget，verifier/PRM/ORM，pass@k 成本算例，p50/p95/p99、超时、取消与预算闸门。
- `pages/10-applications/advanced-rag.html`：补充 RAG 误差分解，Recall@k/MRR/nDCG/context precision/recall/faithfulness/citation correctness，hybrid retrieval/rerank/chunking，企业知识库生产架构与面试题。
- `pages/11-agents/agent-eval.html`：补充 pass^k、置信区间与 all-pass，结果/过程/安全评估分层，轨迹指标、沙箱与状态断言、成本-成功率 frontier、LLM judge 偏差和系统设计题。
- `pages/06-pretraining/data-engineering.html`：补充 Exact Hash/MinHash/SimHash 边界、近重复处理、temperature sampling、领域配比与课程设计、benchmark contamination、15T token 数据管线的可追溯/可回滚/可重放设计，以及面试问答和排障清单。
- `pages/06-pretraining/stability-optimizer.html`：补充 AdamW/Muon/Adafactor 选型、global batch 与梯度累积、warmup/cosine、Grad Norm/Update Norm/Loss Scale/NaN 诊断、checkpoint rollback、7B/70B 稳定性系统设计和面试排障清单。
- `pages/09-efficiency/inference-engines.html`：补充 static/continuous batching、PagedAttention、block-based KV cache、prefix caching、TTFT/TPOT/ITL、chunked prefill、长短请求混部、抢占取消、引擎选型和多租户 70B 服务设计。
- `pages/12-llmops/prompt-eval-ci.html`：补充 Prompt/Model/参数/工具 Schema/检索快照版本化、Golden Set 与分层抽样、Pointwise/Pairwise、LLM Judge 校准、质量/成本/延迟/安全门禁、Bootstrap 置信区间、Shadow/Canary/自动回滚和发布流水线设计。

## 验收

- `tools/check.py`：全站 98 / 98 页面达标；第二轮新增的 4 个页面，以及本次收尾补充的 2 个 LLMOps 页面，均满足正文、图表、表格、代码、深入块和外链门槛。
- 第一轮 6 个重点页面、第二轮 4 个重点页面 HTML 标签平衡检查：全部通过。
- 原有页面结构、交叉链接和参考文献区均保留。
- 第二轮未形成新的外部 Phase 1 研究摘要：研究成员遭遇认证不可用和上游/代理连接故障，本轮按兜底策略使用本地材料、既有来源和结构审计完成，不将其描述为新增外部调研。

## 失败与重试

分布式训练深化曾出现一次 max turns 超限、一次代理 502；Advanced RAG 曾出现代理 502。后续已通过缩小任务范围、避免外网检索的重试完成对应页面，失败尝试未被当作成果。

## 后续候选

## 第二轮收尾状态

- 已完成：训练数据工程、训练稳定性与优化器、推理引擎、Prompt 评测与 CI/CD 门禁 4 个页面的面试向深化。
- 已完成：`pages/12-llmops/observability.html` 与 `pages/12-llmops/cost-engineering.html` 面试区块补齐，分别加入可观测性 Trace Schema/质量排障/SLO 设计，以及成本估算/缓存/多租户治理/单位经济/成本优化系统题。
- 已有面试内容、暂不重复修改：`pages/06-pretraining/objectives.html` 与 `pages/09-efficiency/quantization.html`，两页均已有独立的标准回答、追问和常见误区区块。
- 已补验：本机 Edge headless 可用，已对 `observability.html`、`cost-engineering.html`、`data-engineering.html`、`inference-engines.html`、`prompt-eval-ci.html` 进行真实浏览器截图渲染；5 张截图均成功生成，尺寸为 1440×1200。截图文件位于工作区根目录，作为本轮验收产物保留。