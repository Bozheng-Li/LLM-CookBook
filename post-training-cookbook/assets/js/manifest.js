// 全书章节清单：nav.js 与搜索索引依赖此文件
window.COOKBOOK_MANIFEST = {
  title: "大模型后训练实战 Cookbook",
  subtitle: "从入门到精通：SFT · RLHF · 推理强化 · 安全对齐 · 工程实战",
  home: "index.html",
  parts: [
    { id: "p0", title: "第 0 部分 · 导读与学习路径", chapters: [
      { file: "chapters/00-introduction.html", title: "导读：为什么需要后训练" },
      { file: "chapters/01-roadmap.html", title: "后训练学习路径总览" },
      { file: "chapters/02-setup.html", title: "环境搭建与工具全景" }
    ]},
    { id: "p1", title: "第 1 部分 · 理论基础", chapters: [
      { file: "chapters/03-transformer-review.html", title: "Transformer 与语言模型基础回顾" },
      { file: "chapters/04-pretraining-review.html", title: "预训练、缩放定律与涌现" },
      { file: "chapters/05-rl-fundamentals.html", title: "强化学习基础" },
      { file: "chapters/06-rl-for-llm.html", title: "语言模型作为序贯决策问题" }
    ]},
    { id: "p2", title: "第 2 部分 · 后训练数据工程", chapters: [
      { file: "chapters/07-data-overview.html", title: "后训练数据全景图" },
      { file: "chapters/08-instruction-data.html", title: "指令数据构建" },
      { file: "chapters/09-preference-data.html", title: "偏好数据构建" },
      { file: "chapters/10-data-quality.html", title: "数据清洗、去重与质量过滤" },
      { file: "chapters/11-synthetic-data.html", title: "合成数据与 RLAIF 数据化" }
    ]},
    { id: "p3", title: "第 3 部分 · 监督微调（SFT）", chapters: [
      { file: "chapters/12-sft-fundamentals.html", title: "SFT 基本原理" },
      { file: "chapters/13-sft-implementation.html", title: "SFT 损失实现细节" },
      { file: "chapters/14-peft-lora.html", title: "参数高效微调：LoRA 家族" },
      { file: "chapters/15-chat-templates.html", title: "对话模板与特殊 Token" },
      { file: "chapters/16-sft-recipes.html", title: "SFT 实践法则与灾难性遗忘" },
      { file: "chapters/17-domain-adaptation.html", title: "领域继续预训练与适配" }
    ]},
    { id: "p4", title: "第 4 部分 · 偏好对齐与 RLHF", chapters: [
      { file: "chapters/18-alignment-overview.html", title: "对齐问题与 RLHF 全景" },
      { file: "chapters/19-reward-modeling.html", title: "奖励模型训练" },
      { file: "chapters/20-ppo.html", title: "PPO：从算法到实现" },
      { file: "chapters/21-rlhf-engineering.html", title: "RLHF 工程实践：KL、奖励黑客与稳定性" },
      { file: "chapters/22-dpo.html", title: "DPO：直接偏好优化" },
      { file: "chapters/23-dpo-variants.html", title: "DPO 变体全家桶" },
      { file: "chapters/24-online-alignment.html", title: "在线迭代对齐与免奖励模型方法" },
      { file: "chapters/25-grpo-family.html", title: "GRPO 与 Critic-free RLHF 家族" }
    ]},
    { id: "p5", title: "第 5 部分 · 推理增强后训练", chapters: [
      { file: "chapters/26-reasoning-paradigm.html", title: "推理后训练范式：从 CoT 到 o1/R1" },
      { file: "chapters/27-r1-replication.html", title: "R1 复现实战与配方" },
      { file: "chapters/28-process-reward.html", title: "过程奖励模型与搜索" },
      { file: "chapters/29-test-time-compute.html", title: "测试时计算扩展" },
      { file: "chapters/30-distillation.html", title: "知识蒸馏与推理小模型" },
      { file: "chapters/31-agentic-rl.html", title: "智能体后训练：工具、多轮与环境" }
    ]},
    { id: "p6", title: "第 6 部分 · 安全与价值对齐", chapters: [
      { file: "chapters/32-safety-training.html", title: "安全训练" },
      { file: "chapters/33-constitutional-ai.html", title: "RLAIF 与 Constitutional AI" },
      { file: "chapters/34-red-teaming.html", title: "红队测试与越狱防御" },
      { file: "chapters/35-honesty-hallucination.html", title: "诚实性、幻觉与校准" },
      { file: "chapters/36-scalable-oversight.html", title: "可扩展监督与弱到强" }
    ]},
    { id: "p7", title: "第 7 部分 · 评测", chapters: [
      { file: "chapters/37-evaluation-overview.html", title: "评测总览与方法论" },
      { file: "chapters/38-benchmarks.html", title: "基准测试大全" },
      { file: "chapters/39-llm-as-judge.html", title: "LLM-as-a-Judge" },
      { file: "chapters/40-human-eval-arena.html", title: "人类评估与竞技场" },
      { file: "chapters/41-eval-pitfalls.html", title: "评测陷阱与数据污染" }
    ]},
    { id: "p8", title: "第 8 部分 · 训练工程", chapters: [
      { file: "chapters/42-training-flops-memory.html", title: "算力与显存估算" },
      { file: "chapters/43-distributed-training.html", title: "分布式训练：ZeRO、FSDP 与并行策略" },
      { file: "chapters/44-attention-efficiency.html", title: "高效注意力与混合精度" },
      { file: "chapters/45-inference-engines.html", title: "推理引擎与 RL Rollout 基础设施" },
      { file: "chapters/46-debugging-cookbook.html", title: "训练调试急救手册" },
      { file: "chapters/47-open-recipes.html", title: "开源复现案例研究" }
    ]},
    { id: "p9", title: "第 9 部分 · 前沿专题", chapters: [
      { file: "chapters/48-model-merging.html", title: "模型融合" },
      { file: "chapters/49-self-improvement.html", title: "自我改进与 Self-Play" },
      { file: "chapters/50-multimodal-posttraining.html", title: "多模态后训练" },
      { file: "chapters/51-preference-theory.html", title: "偏好优化的统一理论视角" },
      { file: "chapters/52-continual-learning.html", title: "持续学习与机器遗忘" },
      { file: "chapters/53-future-directions.html", title: "未来方向与开放问题" }
    ]},
    { id: "p10", title: "第 10 部分 · 完整实战项目", chapters: [
      { file: "chapters/54-project-overview.html", title: "实战总览与算力方案" },
      { file: "chapters/55-project-sft.html", title: "项目一：从零 SFT 中文小模型" },
      { file: "chapters/56-project-dpo.html", title: "项目二：DPO 偏好对齐实战" },
      { file: "chapters/57-project-grpo-math.html", title: "项目三：GRPO 数学推理强化" },
      { file: "chapters/58-project-reward-model.html", title: "项目四：训练自己的奖励模型" },
      { file: "chapters/59-project-agent-rl.html", title: "项目五：工具调用智能体 RL" }
    ]},
    { id: "p11", title: "附录", chapters: [
      { file: "chapters/60-paper-library.html", title: "必读论文库（200+ 篇）" },
      { file: "chapters/61-tools-projects.html", title: "开源项目与工具大全" },
      { file: "chapters/62-glossary.html", title: "术语表" },
      { file: "chapters/63-faq.html", title: "FAQ 与常见错误" },
      { file: "chapters/64-resources.html", title: "课程、博客与社区资源" }
    ]}
  ]
};
