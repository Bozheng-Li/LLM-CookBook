/*
 * Cookbook 深化资料目录。
 * 资料按章节维护，页面通过 body[data-part] 自动选择对应资料包；
 * 这样既能覆盖章节首页，也能让主题页共享一套可审校、可更新的来源。
 */
(function () {
  "use strict";

  var PART_PACKS = {
    "00-overview": {
      summary: "这一章负责建立全局坐标：语言模型到底在优化什么、Transformer 为什么成为主干，以及从论文到工程实践应该怎样安排学习顺序。",
      takeaway: "先把“预测 token、扩展规模、解码生成”这条主线串起来，再进入后面的训练、推理和应用章节。",
      items: [
        { type: "论文", title: "Attention Is All You Need", source: "Vaswani et al. · 2017", note: "Transformer 的原始论文。重点看 Figure 1、Scaled Dot-Product Attention 和训练目标，后续几乎所有架构页都会回到这里。", url: "https://arxiv.org/abs/1706.03762" },
        { type: "课程", title: "Stanford CS336: Language Modeling from Scratch", source: "Stanford University · 2024–2026", note: "从数据清洗、分词、模型、训练到评测逐步搭建语言模型，适合作为本 Cookbook 的平行课程。", url: "https://cs336.stanford.edu/" },
        { type: "官方教程", title: "Hugging Face LLM Course", source: "Hugging Face", note: "把 Transformer、Tokenizer、数据集和微调放进一条可运行的工程路径，适合边读边做。", url: "https://huggingface.co/learn/llm-course/chapter1/1" },
        { type: "课程/视频", title: "Stanford CS25: Transformers United", source: "Stanford University", note: "以公开讲座和嘉宾报告补足前沿模型的背景，适合在掌握基础后选择感兴趣的专题观看。", url: "https://web.stanford.edu/class/cs25/" },
        { type: "教材", title: "Speech and Language Processing", source: "Jurafsky & Martin · Stanford", note: "从概率语言模型到神经语言模型的教材级脉络，适合查概念、公式和术语的标准定义。", url: "https://web.stanford.edu/~jurafsky/slp3/" }
      ]
    },
    "01-foundations": {
      summary: "本章把阅读大模型论文所需的数学和学习理论补齐：向量与矩阵、梯度和链式法则、优化器，以及强化学习的基本对象。",
      takeaway: "不要只记优化器名称；要能解释梯度从哪里来、参数为什么更新、以及奖励信号为何可能不稳定。",
      items: [
        { type: "教材", title: "Deep Learning", source: "Goodfellow, Bengio & Courville · MIT Press", note: "覆盖线性代数、概率、数值计算、神经网络和优化，是本章公式的长期参考书。", url: "https://www.deeplearningbook.org/" },
        { type: "课程讲义", title: "CS231n: Optimization · Backpropagation", source: "Stanford University", note: "用计算图和局部梯度解释反向传播，并把学习率、动量和二阶信息的作用讲清楚。", url: "https://cs231n.github.io/optimization-2/" },
        { type: "官方教程", title: "Automatic Differentiation with torch.autograd", source: "PyTorch", note: "将链式法则映射到真实张量代码，适合验证页面中的梯度推导和排查训练实现。", url: "https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html" },
        { type: "论文", title: "Adam: A Method for Stochastic Optimization", source: "Kingma & Ba · 2014", note: "Adam 和 AdamW 的共同起点。阅读时关注一阶、二阶矩估计和偏置修正，而不是只背默认超参数。", url: "https://arxiv.org/abs/1412.6980" },
        { type: "教材", title: "Reinforcement Learning: An Introduction", source: "Sutton & Barto · MIT Press", note: "MDP、价值函数、策略梯度和时序差分学习的经典教材，为 RLHF、GRPO 和 Agentic RL 铺垫。", url: "http://incompleteideas.net/book/the-book-2nd.html" }
      ]
    },
    "02-representation": {
      summary: "本章解释文本如何变成模型可计算的序列：子词分词控制序列长度，Embedding 把离散 id 映射到几何空间，RNN/Seq2Seq 则交代 Transformer 出现前的历史问题。",
      takeaway: "Tokenizer 不是输入层外的附属工具；词表、序列长度、Embedding 矩阵和训练数据分布是同一个设计问题。",
      items: [
        { type: "论文", title: "Neural Machine Translation of Rare Words with Subword Units", source: "Sennrich, Haddow & Birch · ACL 2016", note: "BPE 在神经机器翻译中的经典用法，解释为什么子词能在词表规模和未登录词之间取得折中。", url: "https://arxiv.org/abs/1508.07909" },
        { type: "论文", title: "SentencePiece: A Simple and Language Independent Subword Tokenizer", source: "Kudo & Richardson · EMNLP 2018", note: "把空格当作普通符号、直接从原始字符流训练，特别适合中文、日文和代码等非空格语言。", url: "https://arxiv.org/abs/1808.06226" },
        { type: "官方教程", title: "Byte-Pair Encoding Tokenization", source: "Hugging Face LLM Course", note: "逐轮实现 BPE 合并规则，并展示词表大小、边界标记和编码结果之间的关系。", url: "https://huggingface.co/learn/llm-course/chapter6/5" },
        { type: "论文", title: "Efficient Estimation of Word Representations in Vector Space", source: "Mikolov et al. · 2013", note: "Word2Vec 的原始论文，适合理解分布式表示如何从共现统计中学习语义几何。", url: "https://arxiv.org/abs/1301.3781" },
        { type: "项目/资料", title: "GloVe: Global Vectors for Word Representation", source: "Stanford NLP", note: "将全局词共现矩阵与局部上下文结合，是从静态 Embedding 过渡到上下文表示的清晰对照。", url: "https://nlp.stanford.edu/projects/glove/" }
      ]
    },
    "03-transformer": {
      summary: "本章逐件拆开 Transformer：注意力、因果掩码、位置编码、归一化、前馈网络和残差连接，并说明它们如何组成 decoder-only LLM。",
      takeaway: "读架构图时始终追踪三条信息流：token 表示、位置关系和残差主干；任何变体都可以放回这三条流里比较。",
      items: [
        { type: "论文", title: "Attention Is All You Need", source: "Vaswani et al. · NeurIPS 2017", note: "注意力和 Encoder–Decoder Transformer 的原始定义，适合作为公式与架构的基线。", url: "https://arxiv.org/abs/1706.03762" },
        { type: "实现讲解", title: "The Annotated Transformer", source: "Harvard NLP", note: "将原论文逐行翻译成 PyTorch 实现，适合把 Q/K/V、mask、残差和学习率调度对应到代码。", url: "https://nlp.seas.harvard.edu/annotated-transformer/" },
        { type: "官方文档", title: "Scaled Dot Product Attention", source: "PyTorch", note: "说明 SDPA 的数学定义、mask 语义与后端选择，是核对实际 API 行为的权威入口。", url: "https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html" },
        { type: "论文", title: "RoFormer: Enhanced Transformer with Rotary Position Embedding", source: "Su et al. · 2021", note: "RoPE 的原始论文，重点理解旋转后内积为何自然携带相对位置信息。", url: "https://arxiv.org/abs/2104.09864" },
        { type: "论文", title: "Root Mean Square Layer Normalization", source: "Zhang & Sennrich · 2019", note: "RMSNorm 的来源和计算简化，帮助比较 LayerNorm、RMSNorm 以及 Pre-Norm 结构。", url: "https://arxiv.org/abs/1910.07467" }
      ]
    },
    "04-modern-arch": {
      summary: "本章关注 Transformer 之后的架构选择：稀疏专家、线性/状态空间模型、长上下文、多模态和扩散语言模型。重点是理解每种方法改变了哪一层约束。",
      takeaway: "比较新架构时同时看训练目标、权重兼容性、推理状态和硬件实现；只看理论复杂度很容易得出错误结论。",
      items: [
        { type: "论文", title: "Switch Transformers: Scaling to Trillion Parameter Models", source: "Fedus, Zoph & Shazeer · 2021", note: "MoE 路由、容量因子和负载均衡的经典介绍，适合建立稀疏激活的共同语言。", url: "https://arxiv.org/abs/2101.03961" },
        { type: "论文", title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces", source: "Gu & Dao · 2023", note: "选择性状态空间模型的代表作，解释线性扫描、选择机制和长序列效率之间的关系。", url: "https://arxiv.org/abs/2312.00752" },
        { type: "论文", title: "GQA: Training Generalized Multi-Query Transformer Models", source: "Ainslie et al. · 2023", note: "用较少 KV 头降低推理带宽和缓存开销，是理解 MQA/GQA 工程取舍的直接来源。", url: "https://arxiv.org/abs/2305.13245" },
        { type: "论文", title: "An Image is Worth 16x16 Words", source: "Dosovitskiy et al. · 2020", note: "ViT 将图像 patch 化并交给 Transformer，帮助理解多模态视觉编码器的基本范式。", url: "https://arxiv.org/abs/2010.11929" },
        { type: "论文", title: "Large Language Diffusion Models", source: "Nie et al. · 2025", note: "以 LLaDA 为代表的扩散语言模型工作，适合和自回归模型对照并识别当前研究边界。", url: "https://arxiv.org/abs/2502.09992" }
      ]
    },
    "05-systems": {
      summary: "本章把模型公式连接到真实硬件：GPU 的执行和内存层级、FLOP 与带宽核算、FlashAttention 的 IO 优化，以及 Triton kernel 的工程方法。",
      takeaway: "性能问题先判断是算力受限还是访存受限，再用 profiler 和小规模 benchmark 验证；不要把峰值 FLOP 当成实际吞吐。",
      items: [
        { type: "论文", title: "FlashAttention: Fast and Memory-Efficient Exact Attention", source: "Dao et al. · NeurIPS 2022", note: "分块、online softmax 和重计算的原始论文，完整解释“IO 感知”为什么能在不近似的情况下加速。", url: "https://arxiv.org/abs/2205.14135" },
        { type: "官方文档", title: "CUDA C++ Programming Guide", source: "NVIDIA", note: "warp、线程块、共享内存、全局内存和同步语义的权威参考，核对 GPU 章节中的硬件事实。", url: "https://docs.nvidia.com/cuda/cuda-c-programming-guide/" },
        { type: "官方指南", title: "CUDA C++ Best Practices Guide", source: "NVIDIA", note: "合并访存、occupancy、bank conflict 和性能分析的工程清单，适合配合 profiler 使用。", url: "https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/" },
        { type: "官方教程", title: "Triton Tutorials", source: "OpenAI Triton", note: "从向量加法、矩阵乘法到融合 kernel 的渐进式教程，是实战页面的直接延伸。", url: "https://triton-lang.org/main/getting-started/tutorials/" },
        { type: "论文", title: "Roofline: An Insightful Visual Performance Model", source: "Williams et al. · CACM 2009", note: "用算术强度把计算瓶颈和带宽瓶颈放在同一张图上，是性能剖析的经典框架。", url: "https://doi.org/10.1145/1498765.1498785" }
      ]
    },
    "06-pretraining": {
      summary: "本章覆盖从数据到训练集群的完整预训练链路：目标函数、语料清洗与合成、Scaling Laws、并行策略、混合精度和稳定性。",
      takeaway: "预训练效果不是参数量单变量函数；数据质量、token 数、优化稳定性和通信效率共同决定最终结果。",
      items: [
        { type: "论文", title: "Scaling Laws for Neural Language Models", source: "Kaplan et al. · 2020", note: "最早系统刻画模型规模、数据量、计算量和损失之间幂律关系的工作。", url: "https://arxiv.org/abs/2001.08361" },
        { type: "论文", title: "Training Compute-Optimal Large Language Models", source: "Hoffmann et al. · 2022", note: "Chinchilla 结论：固定算力下模型参数和训练 token 应共同增长，纠正只堆参数的直觉。", url: "https://arxiv.org/abs/2203.15556" },
        { type: "论文", title: "The Pile: An 800GB Dataset of Diverse Text", source: "Gao et al. · 2020", note: "公开语料混合、来源比例和去重处理的代表性数据集论文。", url: "https://arxiv.org/abs/2101.00027" },
        { type: "论文", title: "Megatron-LM: Training Multi-Billion Parameter Language Models", source: "Shoeybi et al. · 2019", note: "张量并行、流水线并行和大规模 Transformer 训练工程的经典来源。", url: "https://arxiv.org/abs/1909.08053" },
        { type: "官方文档", title: "Fully Sharded Data Parallel", source: "PyTorch", note: "FSDP 的参数、梯度和优化器状态分片语义，适合将并行原理落到可运行配置。", url: "https://pytorch.org/docs/stable/fsdp.html" }
      ]
    },
    "07-posttraining": {
      summary: "本章讨论基础模型如何变成可用助手：监督微调、偏好数据、RLHF、DPO、GRPO、LoRA、蒸馏和安全对齐。",
      takeaway: "后训练首先是数据和目标的设计问题，其次才是算法名称；每种方法都在能力、稳定性、成本和可控性之间交换。",
      items: [
        { type: "论文", title: "Training Language Models to Follow Instructions with Human Feedback", source: "Ouyang et al. · 2022", note: "InstructGPT 的 SFT、奖励模型和 PPO 三阶段流程，是理解 RLHF 工业范式的主线。", url: "https://arxiv.org/abs/2203.02155" },
        { type: "论文", title: "Deep Reinforcement Learning from Human Preferences", source: "Christiano et al. · 2017", note: "人类偏好训练奖励模型并优化策略的早期奠基工作。", url: "https://arxiv.org/abs/1706.03741" },
        { type: "论文", title: "LoRA: Low-Rank Adaptation of Large Language Models", source: "Hu et al. · ICLR 2022", note: "冻结基座、训练低秩增量的参数高效微调方法，适合结合页面代码估算显存。", url: "https://arxiv.org/abs/2106.09685" },
        { type: "论文", title: "Direct Preference Optimization", source: "Rafailov et al. · NeurIPS 2023", note: "把奖励模型和 PPO 目标化简为偏好分类损失，帮助比较 DPO 与 RLHF 的隐含 KL 约束。", url: "https://arxiv.org/abs/2305.18290" },
        { type: "论文", title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning", source: "DeepSeek-AI · 2024", note: "GRPO 的代表性来源，展示可验证奖励、群组采样和推理强化的训练闭环。", url: "https://arxiv.org/abs/2402.03300" }
      ]
    },
    "08-inference": {
      summary: "本章聚焦生成阶段的决策：采样和解码、Self-Consistency、Best-of-N、树搜索、验证器，以及 test-time scaling 的成本边界。",
      takeaway: "推理时扩展不是无条件增加采样次数；先确认任务是否可验证，再把额外计算预算放到候选生成、验证或搜索中的瓶颈。",
      items: [
        { type: "论文", title: "The Curious Case of Neural Text Degeneration", source: "Holtzman et al. · 2020", note: "Nucleus sampling 的原始论文，解释贪心/beam search 为什么会导致重复和退化。", url: "https://arxiv.org/abs/1904.09751" },
        { type: "论文", title: "Self-Consistency Improves Chain of Thought Reasoning", source: "Wang et al. · 2022", note: "通过多条推理路径投票提高可验证任务准确率，是 test-time scaling 的基础范式。", url: "https://arxiv.org/abs/2203.11171" },
        { type: "论文", title: "Let's Verify Step by Step", source: "Lightman et al. · 2023", note: "过程奖励模型和逐步验证的代表作，说明“答案对不对”和“推理过程是否可靠”是不同信号。", url: "https://arxiv.org/abs/2305.20050" },
        { type: "论文", title: "Tree of Thoughts", source: "Yao et al. · NeurIPS 2023", note: "把语言模型生成组织成可回溯的搜索树，适合和页面中的 beam、Best-of-N 对照。", url: "https://arxiv.org/abs/2305.10601" },
        { type: "技术报告", title: "DeepSeek-R1", source: "DeepSeek-AI · 2025", note: "大规模推理强化的公开技术报告，适合观察奖励设计、冷启动和蒸馏的组合方式。", url: "https://arxiv.org/abs/2501.12948" }
      ]
    },
    "09-efficiency": {
      summary: "本章从模型压缩、KV Cache、推理引擎、投机解码和端侧部署几个角度回答同一个问题：怎样以更少显存和更低延迟提供可接受的能力。",
      takeaway: "先定义服务约束（质量、TTFT、吞吐、显存和成本），再选量化、批处理、缓存或硬件方案，避免只比较单一速度数字。",
      items: [
        { type: "论文", title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", source: "Frantar et al. · 2022", note: "基于近似二阶信息的后训练量化代表作，解释 4-bit 权重量化的误差补偿。", url: "https://arxiv.org/abs/2210.17323" },
        { type: "论文", title: "AWQ: Activation-aware Weight Quantization", source: "Lin et al. · MLSys 2024", note: "保护激活显著权重的量化方法，适合比较 GPTQ、AWQ 与不同推理后端。", url: "https://arxiv.org/abs/2306.00978" },
        { type: "论文", title: "SmoothQuant: Accurate and Efficient Post-Training Quantization", source: "Xiao et al. · 2022", note: "将量化难度从激活迁移到权重，为 W8A8 推理提供工程路径。", url: "https://arxiv.org/abs/2211.10438" },
        { type: "官方文档", title: "vLLM Documentation", source: "vLLM Project · UC Berkeley 起源", note: "连续批处理、PagedAttention、量化和 OpenAI-compatible server 的实践入口。", url: "https://docs.vllm.ai/en/latest/" },
        { type: "论文", title: "FlexGen: High-Throughput Generative Inference of Large Language Models", source: "Sheng et al. · 2023", note: "在 GPU、CPU 和磁盘之间进行 offload 的系统设计，适合理解端侧与低显存部署。", url: "https://arxiv.org/abs/2303.06865" }
      ]
    },
    "10-applications": {
      summary: "本章把模型能力落到应用：Prompt 和 Context Engineering、RAG、重排、结构化输出，以及带评测的 Agentic RAG。",
      takeaway: "应用质量取决于信息是否被正确组织和验证；提示词只是接口的一部分，检索、约束、评测和失败处理同样重要。",
      items: [
        { type: "论文", title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", source: "Lewis et al. · NeurIPS 2020", note: "RAG 的原始论文，明确区分参数化记忆与外部非参数化记忆。", url: "https://arxiv.org/abs/2005.11401" },
        { type: "论文", title: "ReAct: Synergizing Reasoning and Acting in Language Models", source: "Yao et al. · ICLR 2023", note: "交错推理与行动的 Agent 范式，也是工具调用和 Agentic RAG 的共同基础。", url: "https://arxiv.org/abs/2210.03629" },
        { type: "官方示例", title: "Structured Outputs Introduction", source: "OpenAI Cookbook", note: "展示如何用 JSON Schema 约束生成并验证结构化结果，适合与本页的约束解码对照。", url: "https://cookbook.openai.com/examples/structured_outputs_intro" },
        { type: "官方文档", title: "Prompting Guide", source: "Hugging Face Transformers", note: "从任务模板、少样本示例到生成参数，提供可迁移的提示设计基础。", url: "https://huggingface.co/docs/transformers/tasks/prompting" },
        { type: "综述论文", title: "Retrieval-Augmented Generation for Large Language Models: A Survey", source: "Gao et al. · 2023", note: "按检索、增强、生成和评测梳理 RAG 变体，适合作为进阶地图。", url: "https://arxiv.org/abs/2312.10997" }
      ]
    },
    "11-agents": {
      summary: "本章把 Agent 看成一个带工具的闭环系统：模型负责决策，工具改变环境，反馈驱动下一步；记忆、规划、协作和安全共同决定可靠性。",
      takeaway: "Agent 的核心不是“让模型多想几步”，而是设计可观察、可中止、可验证的行动循环。",
      items: [
        { type: "论文", title: "ReAct: Synergizing Reasoning and Acting", source: "Yao et al. · ICLR 2023", note: "最常用的思考–行动–观察循环之一，适合作为工具型 Agent 的最小抽象。", url: "https://arxiv.org/abs/2210.03629" },
        { type: "论文", title: "Toolformer: Language Models Can Teach Themselves to Use Tools", source: "Schick et al. · 2023", note: "展示模型如何学习何时调用 API 以及如何把工具结果纳入上下文。", url: "https://arxiv.org/abs/2302.04761" },
        { type: "协议规范", title: "Model Context Protocol Specification", source: "MCP Steering Group", note: "工具、资源和提示的开放协议规范，适合核对 MCP 客户端/服务端边界和安全责任。", url: "https://modelcontextprotocol.io/specification/2025-06-18" },
        { type: "论文", title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", source: "Yang et al. · 2024", note: "以代码仓库任务说明工具接口、上下文组织和执行反馈如何影响 Agent 成功率。", url: "https://arxiv.org/abs/2405.15793" },
        { type: "论文", title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks", source: "Xie et al. · 2024", note: "桌面环境中的长链任务评测，帮助理解 Computer Use 的状态、动作和可复现性问题。", url: "https://arxiv.org/abs/2404.07972" }
      ]
    },
    "12-llmops": {
      summary: "本章覆盖模型上线后的工程闭环：评测 CI、RAG 生产化、成本控制、观测、护栏和故障处理。",
      takeaway: "生产系统的最小闭环是可追踪输入、可解释输出、可回放轨迹和可执行的质量门禁，而不是简单接一个模型 API。",
      items: [
        { type: "官方文档", title: "OpenTelemetry Documentation", source: "Cloud Native Computing Foundation", note: "统一 traces、metrics 和 logs 的开放标准，适合为 LLM 调用、检索和工具链建立关联追踪。", url: "https://opentelemetry.io/docs/" },
        { type: "工程指南", title: "Service Level Objectives", source: "Google SRE", note: "从用户目标定义可测 SLO、错误预算和告警策略，为延迟和可用性指标提供中立框架。", url: "https://sre.google/sre-book/service-level-objectives/" },
        { type: "官方框架", title: "AI Risk Management Framework", source: "NIST", note: "将治理、测量、管理和映射组织成风险闭环，可作为护栏和上线审查的通用基线。", url: "https://www.nist.gov/itl/ai-risk-management-framework" },
        { type: "官方文档", title: "Ragas Documentation", source: "Ragas Project", note: "提供 RAG 的 context precision、faithfulness 等评测指标和数据集组织方式。", url: "https://docs.ragas.io/" },
        { type: "官方文档", title: "MLflow GenAI Evaluation and Monitoring", source: "MLflow", note: "展示生产轨迹、在线评估和反馈回流的实现方式，适合与页面中的评测 CI 对照。", url: "https://mlflow.org/docs/latest/genai/eval-monitor/" }
      ]
    },
    "13-evaluation": {
      summary: "本章讨论如何知道模型是否真的变好了：基准设计、任务级评测、污染检测、幻觉分析和可解释性工具。",
      takeaway: "分数不是结论；必须同时报告任务定义、数据来源、污染风险、统计不确定性和人工/自动评审的边界。",
      items: [
        { type: "论文", title: "Holistic Evaluation of Language Models (HELM)", source: "Liang et al. · Stanford CRFM", note: "将准确性、鲁棒性、偏见、毒性和效率放在统一评测框架中，适合作为基准设计总览。", url: "https://arxiv.org/abs/2211.09110" },
        { type: "论文", title: "Measuring Massive Multitask Language Understanding", source: "Hendrycks et al. · 2021", note: "MMLU 的任务构成和多学科知识评估方式，帮助理解基准覆盖范围与局限。", url: "https://arxiv.org/abs/2009.03300" },
        { type: "论文", title: "Beyond the Imitation Game: BIG-bench", source: "Srivastava et al. · 2022", note: "大规模多任务基准及其涌现曲线，适合讨论任务选择和能力分布。", url: "https://arxiv.org/abs/2206.04615" },
        { type: "论文", title: "TruthfulQA: Measuring How Models Mimic Human Falsehoods", source: "Lin, Hilton & Evans · 2022", note: "用对抗式问题测量模型复述常见错误信念的倾向，是幻觉与真实性章节的重要对照。", url: "https://arxiv.org/abs/2109.07958" },
        { type: "评测工具", title: "Inspect AI", source: "UK AI Security Institute", note: "开放的模型评测框架，支持任务、评分器、沙箱和轨迹记录，适合搭建可复现实验。", url: "https://inspect.aisi.org.uk/" }
      ]
    },
    "14-governance": {
      summary: "本章从风险、伦理、隐私、版权、安全测试和内容溯源几个角度讨论大模型治理，强调证据、责任和可审计性。",
      takeaway: "治理不是给模型贴一个“安全”标签，而是把风险识别、控制措施、评估证据和责任归属写进全生命周期。",
      items: [
        { type: "风险框架", title: "AI Risk Management Framework", source: "NIST · 2023", note: "提供 Govern、Map、Measure、Manage 四类活动，是组织 AI 风险管理的通用基线。", url: "https://www.nist.gov/itl/ai-risk-management-framework" },
        { type: "国际规范", title: "Recommendation on the Ethics of Artificial Intelligence", source: "UNESCO · 2021", note: "以人权、比例原则、透明度和环境责任为核心，适合伦理与公平章节的国际参照。", url: "https://unesdoc.unesco.org/ark:/48223/pf0000381137" },
        { type: "国际原则", title: "OECD AI Principles", source: "OECD", note: "强调包容增长、人本价值、透明可解释、稳健安全和问责，适合和企业治理要求对照。", url: "https://oecd.ai/en/ai-principles" },
        { type: "法规", title: "Regulation (EU) 2024/1689 (AI Act)", source: "European Union", note: "按风险等级规定透明度、通用 AI 和高风险系统义务，阅读时重点看定义与适用范围。", url: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj" },
        { type: "论文", title: "Model Cards for Model Reporting", source: "Mitchell et al. · FAT* 2019", note: "用标准化模型卡记录用途、限制、评测和偏差，是把研究结果转成可审计文档的经典方案。", url: "https://arxiv.org/abs/1810.03993" }
      ]
    },
    "15-practice": {
      summary: "本章把前面的概念串成可运行项目：手写 tokenizer、miniGPT、FlashAttention kernel、RAG、微调和工具型 Agent。",
      takeaway: "每个实战都应该保留一个可验证闭环：输入数据、模型计算、指标/测试和失败诊断缺一不可。",
      items: [
        { type: "代码仓库", title: "nanoGPT", source: "Andrej Karpathy", note: "约数百行的 GPT 训练代码，适合逐行追踪数据、前向、反向和采样。", url: "https://github.com/karpathy/nanoGPT" },
        { type: "课程", title: "Stanford CS336: Language Modeling from Scratch", source: "Stanford University", note: "将从零实现扩展到真实数据、分布式训练和评测，适合作为实战的上一级路线。", url: "https://cs336.stanford.edu/" },
        { type: "官方教程", title: "Hugging Face Tokenizers Course", source: "Hugging Face", note: "从 BPE 训练到编码器导出，能直接对照本章手写 tokenizer 的每一步。", url: "https://huggingface.co/learn/llm-course/chapter6/1" },
        { type: "官方教程", title: "Triton Tutorials", source: "OpenAI Triton", note: "通过小 kernel 逐步学习 tile、mask、程序实例和性能 benchmark，适合 FlashAttention 实战。", url: "https://triton-lang.org/main/getting-started/tutorials/" },
        { type: "官方规范", title: "Model Context Protocol Specification", source: "MCP Steering Group", note: "为工具型 Agent 实战提供协议层约束，重点查看工具 schema、资源和传输安全。", url: "https://modelcontextprotocol.io/specification/2025-06-18" }
      ]
    }
  };

  var TOPIC_HINTS = {
    "attention": "注意力的核心不是一个黑盒层，而是对上下文位置进行内容相关的加权读取；结合 FlashAttention 资料能同时看懂数学和 IO。",
    "kv-cache": "KV Cache 把已处理 token 的键和值保存下来，换取 decode 阶段少做重复计算；它的代价会转化为显存容量和调度复杂度。",
    "moe": "MoE 只激活少量专家，因此要同时关注路由质量、负载均衡、通信和总参数/激活参数的区别。",
    "scaling-laws": "Scaling Laws 是小规模实验外推的工具，不是能力必然增长的保证；数据质量和训练配比决定外推是否可信。",
    "rag": "RAG 的关键链路是切分、召回、重排、上下文编排和引用验证，生成模型只是最后一环。",
    "advanced-rag": "Advanced RAG 的增益通常来自检索策略和评测闭环，而不是单纯把 top-k 调大。",
    "agent": "Agent 的最小闭环是决策、行动、观察和停止条件；工具 schema 与失败反馈往往比提示词花样更重要。",
    "tool-use-mcp": "MCP 统一的是工具发现和调用语义，不会自动解决权限、数据泄露或工具结果可信度问题。",
    "hallucination": "幻觉既可能来自知识缺失，也可能来自检索、解码和评测设计；缓解策略必须与成因对应。",
    "benchmarks": "基准分数只有在任务定义、数据污染、提示模板和统计波动都公开时才具有可比较性。",
    "privacy-security": "隐私与安全控制应覆盖训练数据、上下文、工具调用、日志和模型输出，而不是只做输出过滤。",
    "safety-redteam": "红队测试的价值在于发现可复现的失败模式，并把它们转成护栏、评测集和上线门禁。"
  };

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/\"/g, "&quot;").replace(/'/g, "&#39;");
  }

  function currentContext() {
    var partId = document.body.getAttribute("data-part") || "";
    var topicId = document.body.getAttribute("data-topic") || "";
    var part = null;
    var topic = null;
    (window.TOC && window.TOC.parts || []).forEach(function (candidate) {
      if (candidate.id === partId) {
        part = candidate;
        (candidate.topics || []).forEach(function (item) {
          if (item.id === topicId) topic = item;
        });
      }
    });
    return { partId: partId, topicId: topicId, part: part, topic: topic };
  }

  function insertBeforeReferences(container, section) {
    var headings = container.querySelectorAll("h2");
    var referenceHeading = null;
    for (var i = 0; i < headings.length; i++) {
      var text = headings[i].textContent || "";
      if (/参考|延伸|论文|资料/.test(text)) {
        referenceHeading = headings[i];
        break;
      }
    }
    if (referenceHeading) {
      referenceHeading.parentNode.insertBefore(section, referenceHeading);
      return;
    }
    var pager = container.querySelector("#pager");
    if (pager) pager.parentNode.insertBefore(section, pager);
    else container.appendChild(section);
  }

  function render() {
    if (document.querySelector(".resource-deepening")) return;
    var ctx = currentContext();
    if (!ctx.partId || !PART_PACKS[ctx.partId]) return;
    var pack = PART_PACKS[ctx.partId];
    var container = document.querySelector(".container");
    if (!container || !pack.items || pack.items.length < 4) return;

    var title = ctx.topic ? ctx.topic.title : (ctx.part ? ctx.part.title : "本章");
    var topicHint = ctx.topicId && TOPIC_HINTS[ctx.topicId];
    var summary = topicHint || (ctx.topic && ctx.topic.desc) || pack.summary;
    var section = document.createElement("section");
    section.className = "resource-deepening";
    section.setAttribute("aria-labelledby", "resource-deepening-title");
    var items = pack.items.map(function (item) {
      return "<li class=\"rd-item\">" +
        "<div class=\"rd-meta\"><span class=\"rd-type\">" + escapeHtml(item.type) + "</span>" +
        "<span class=\"rd-source\">" + escapeHtml(item.source) + "</span></div>" +
        "<a href=\"" + escapeHtml(item.url) + "\" target=\"_blank\" rel=\"noopener noreferrer\">" + escapeHtml(item.title) + " ↗</a>" +
        "<p class=\"rd-note\">" + escapeHtml(item.note) + "</p></li>";
    }).join("");
    section.innerHTML =
      "<div class=\"rd-head\"><div><div class=\"rd-kicker\">本页新增 · 权威延伸资料</div>" +
      "<h2 id=\"resource-deepening-title\">围绕“" + escapeHtml(title) + "”继续深入</h2></div></div>" +
      "<p class=\"rd-summary\">" + escapeHtml(summary) + "</p>" +
      "<p class=\"rd-takeaway\"><strong>阅读提示：</strong>" + escapeHtml(pack.takeaway) + "</p>" +
      "<ul class=\"rd-list\">" + items + "</ul>" +
      "<p class=\"rd-foot\">资料优先选用原始论文、官方文档、大学课程和公共机构材料；链接按 2026-08-10 检索，具体版本以来源页面为准。</p>";
    insertBeforeReferences(container, section);
  }

  window.CB_RESOURCE_DATA = PART_PACKS;
  window.CB_RENDER_RESOURCES = render;
})();
