/* Cookbook technical deepening layer. Topic text stays data-driven so pages remain small and maintainable. */
(function () {
  'use strict';

  var THREADS = {
    '00-overview': {
      arc: '从统计语言模型、词向量和 Seq2Seq，到 Transformer、规模化预训练、指令对齐与工具增强，核心变化始终是把可学习的表示、可扩展的计算和可验证的反馈连接起来。',
      mechanics: '先区分训练目标、模型参数、外部上下文和解码策略，再沿着“数据 -> 表示 -> 前向计算 -> 损失 -> 更新 -> 评测”闭环阅读后续章节。',
      tradeoff: '能力提升不能只看参数量：数据质量、训练配比、上下文长度、推理预算和服务成本共同决定实际效果。',
      frontier: '当前系统逐渐从单次文本生成转向多模态输入、可控推理、检索和工具执行；对新方法应同时检查公开实验、基准污染和可复现实作。',
      check: '能够画出一个 LLM/Agent 系统的数据流，并说明每一层的输入、输出、可观测指标和主要失败模式。',
      refs: [['Attention Is All You Need', 'https://arxiv.org/abs/1706.03762'], ['Chinchilla: Training Compute-Optimal Large Language Models', 'https://arxiv.org/abs/2203.15556'], ['Stanford CS336', 'https://cs336.stanford.edu/']]
    },
    '01-foundations': {
      arc: '从 n-gram 的局部统计到反向传播和梯度优化，再到策略梯度与偏好优化，现代大模型仍建立在概率建模、微积分和数值稳定性之上。',
      mechanics: '阅读公式时固定追踪张量形状、随机变量、目标函数和梯度估计的来源；任何优化器都应回到“估计什么、更新什么、误差如何传播”。',
      tradeoff: '更大的 batch、学习率或模型并不自动带来更好结果；梯度噪声、条件数、正则化和数据分布会改变稳定区间。',
      frontier: 'Muon、分层学习率、混合精度和 RLVR 等新方法都在重新讨论优化信号的质量与成本，结论必须结合任务和规模验证。',
      check: '能手算一次交叉熵、KL、反向传播和优势估计，并解释数值溢出、梯度爆炸与奖励稀疏的处理方式。',
      refs: [['Deep Learning textbook', 'https://www.deeplearningbook.org/'], ['Adam', 'https://arxiv.org/abs/1412.6980'], ['Reinforcement Learning: An Introduction', 'http://incompleteideas.net/book/the-book-2nd.html']]
    },
    '02-representation': {
      arc: '文本表示从 one-hot、Word2Vec/GloVe 的静态词向量，发展到上下文表示和可学习 tokenizer；序列边界与几何空间共同决定模型看到什么。',
      mechanics: '先由 tokenizer 把字符流映射为 token id，再用 embedding 查表得到向量；位置、上下文和训练目标随后逐层改写表示。',
      tradeoff: '大词表缩短序列却扩大 embedding 与长尾稀疏，小词表更通用却增加序列长度；检索 embedding 还需平衡维度、吞吐和领域偏差。',
      frontier: '多语统一词表、字节级模型、可学习分词和多向量检索仍在演进，评价应覆盖压缩率、未知输入、语义检索和推理成本。',
      check: '对同一段中英代码文本比较两种 tokenizer 的 token 数和边界，再测两种 embedding 的 recall@k 与存储成本。',
      refs: [['SentencePiece', 'https://arxiv.org/abs/1808.06226'], ['Word2Vec', 'https://arxiv.org/abs/1301.3781'], ['Sentence-BERT', 'https://arxiv.org/abs/1908.10084']]
    },
    '03-transformer': {
      arc: 'Transformer 用全局注意力替代循环状态，把序列建模拆成可并行的注意力、位置、归一化、前馈和残差组件，随后形成 decoder-only 主流。',
      mechanics: '重点追踪 Q/K/V 的形状、因果 mask、softmax 缩放、残差流和归一化位置；这些局部选择会直接影响训练稳定性、上下文外推和推理显存。',
      tradeoff: '表达能力、并行度、二次复杂度、KV Cache 规模和 kernel 友好性之间不存在单一最优解。',
      frontier: 'GQA/MLA、稀疏注意力、RMSNorm、SwiGLU 与更长上下文训练正在改变默认架构，但需要用端到端吞吐和质量共同评价。',
      check: '能够从公式推导一次 attention，并定位 mask、位置编码、norm 或 residual 实现中的常见 bug。',
      refs: [['Attention Is All You Need', 'https://arxiv.org/abs/1706.03762'], ['RoFormer / RoPE', 'https://arxiv.org/abs/2104.09864'], ['FlashAttention', 'https://arxiv.org/abs/2205.14135']]
    },
    '04-modern-arch': {
      arc: '现代架构围绕三个瓶颈演进：注意力的长度复杂度、稀疏专家的计算/通信、以及多模态和状态空间的统一表示。',
      mechanics: '比较架构时固定记录参数量、激活参数量、路由粒度、通信模式、缓存语义和训练目标，避免只按模型名称或榜单排序。',
      tradeoff: '稀疏化通常以路由不均衡和通信换取 FLOP 节省；长上下文和多模态则会把瓶颈转移到数据、显存或对齐层。',
      frontier: 'MoE、线性/混合注意力、视觉语言模型和扩散语言模型仍处于快速演进期，应明确哪些结论已稳定、哪些只在特定规模成立。',
      check: '能为给定上下文长度、GPU 预算和延迟目标选择架构，并说清质量、通信与运维代价。',
      refs: [['Switch Transformers', 'https://arxiv.org/abs/2101.03961'], ['Mamba', 'https://arxiv.org/abs/2312.00752'], ['LLaDA', 'https://arxiv.org/abs/2502.09992']]
    },
    '05-systems': {
      arc: '系统优化从 GPU 层次结构、Roofline 和通信原语出发，逐步发展到 FlashAttention、算子融合、编译器和端到端 profiling。',
      mechanics: '先判断瓶颈属于计算、HBM/SRAM 访问、kernel 启动还是跨卡通信，再选择 tile、融合、重计算、并行或布局优化。',
      tradeoff: '理论 FLOP、峰值带宽和实际吞吐常常不同；任何优化都必须同时报告精度、形状覆盖、显存和回退路径。',
      frontier: 'FP8、异步执行、编译期融合、推理/训练解耦和新一代互联正在改变系统边界，基准应固定硬件、batch、长度和版本。',
      check: '能够用 profiler 找到一个端到端热点，并解释优化前后算术强度、显存流量和延迟变化。',
      refs: [['FlashAttention-2', 'https://arxiv.org/abs/2307.08691'], ['Triton tutorials', 'https://triton-lang.org/main/getting-started/tutorials/'], ['Roofline model', 'https://crd.lbl.gov/divisions/computer-science/par/research/roofline/']]
    },
    '06-pretraining': {
      arc: '预训练从 CLM/MLM 目标扩展到多 token 预测、课程数据和合成数据，训练规模则由 Kaplan 经验律推进到 Chinchilla 的计算最优配比。',
      mechanics: '把数据去重、混合比例、token 预算、并行策略、checkpoint 和验证集视为同一个实验设计，而不是互相独立的脚本参数。',
      tradeoff: '更多数据、更多参数和更长训练之间需要按计算预算平衡；数据污染、重复和合成数据坍缩会让离线 loss 失真。',
      frontier: '持续预训练、数据飞轮、MTP、FP8 和新优化器仍在发展，必须报告数据谱系和消融实验。',
      check: '能从 token 预算估算训练 FLOP、显存和并行策略，并设计 loss spike、数据泄漏和 checkpoint 恢复的排查流程。',
      refs: [['Scaling Laws', 'https://arxiv.org/abs/2001.08361'], ['Chinchilla', 'https://arxiv.org/abs/2203.15556'], ['Megatron-LM', 'https://arxiv.org/abs/1909.08053']]
    },
    '07-posttraining': {
      arc: '后训练经历了 SFT、RLHF、DPO，再到可验证奖励和推理时扩展；关键转变是从模仿答案转向优化可检查的行为和过程。',
      mechanics: '对比 SFT、偏好损失、PPO/GRPO 和 verifier 时，明确参考策略、KL 约束、奖励粒度、采样分组和拒绝样本处理。',
      tradeoff: '更强的奖励信号可能带来 reward hacking、过度拒答、长度偏置或能力遗忘；必须联合看任务质量、安全和分布外表现。',
      frontier: 'RLVR、过程奖励、蒸馏和长轨迹训练正在融合，论文中的提升应通过独立 verifier 和可复现实验验证。',
      check: '能手算 DPO/GRPO 的一个 batch，解释 loss mask、KL、优势归一化和奖励作弊的诊断指标。',
      refs: [['InstructGPT', 'https://arxiv.org/abs/2203.02155'], ['DPO', 'https://arxiv.org/abs/2305.18290'], ['DeepSeek-R1', 'https://arxiv.org/abs/2501.12948']]
    },
    '08-inference': {
      arc: '推理由一次前向生成发展为带搜索、验证器和自适应预算的测试时计算，推理质量与计算量开始显式交换。',
      mechanics: '区分采样、束搜索、树搜索、验证器和思维长度；记录 token、并行分支、停止条件和最终选择规则。',
      tradeoff: '更长的推理链不必然更准确，延迟、显存、重复率和错误传播都需要纳入预算。',
      frontier: '混合推理、过程奖励、草稿-验证解码和自适应思考预算是当前主线，仍需任务级而非单一榜单评估。',
      check: '能设计一个带预算上限和失败回退的推理服务，并解释 verifier 错误如何影响最终答案。',
      refs: [['Chain-of-Thought', 'https://arxiv.org/abs/2201.11903'], ['Let’s Verify Step by Step', 'https://arxiv.org/abs/2305.20050'], ['Speculative Sampling', 'https://arxiv.org/abs/2211.17192']]
    },
    '09-efficiency': {
      arc: '效率优化从权重量化和 KV Cache，发展到 paged serving、推测解码、Prefill/Decode 分离和端到端成本工程。',
      mechanics: '把 TTFT、TPOT、吞吐、显存占用、并发和质量损失分开测量，避免用单一 tokens/s 掩盖服务瓶颈。',
      tradeoff: '压缩、批处理和 offload 会在精度、尾延迟、带宽和实现复杂度之间重新分配成本。',
      frontier: 'FP8/FP4、异构缓存、连续批处理和 disaggregated serving 正在成为规模化部署的基础设施。',
      check: '能根据 SLA 和 GPU 预算选择量化、并行和缓存方案，并给出可回归的基准表。',
      refs: [['vLLM / PagedAttention', 'https://arxiv.org/abs/2309.06180'], ['SmoothQuant', 'https://arxiv.org/abs/2211.10438'], ['AWQ', 'https://arxiv.org/abs/2306.00978']]
    },
    '10-applications': {
      arc: '应用系统从 prompt 模板走向上下文工程、RAG、结构化输出和可观测工作流，模型只是系统中的一个可替换组件。',
      mechanics: '把输入拆成检索、重排、上下文编排、生成、校验和反馈，每一步都保留证据、版本和失败原因。',
      tradeoff: '更多上下文可能增加噪声和成本；更严格的 schema、引用和 guardrail 会牺牲部分召回或表达自由度。',
      frontier: 'Agentic RAG、图检索、多模态检索和结构化推理正在融合，效果必须通过真实任务集而非 demo 判断。',
      check: '能从零设计一个带引用、结构校验、回归集和降级策略的知识应用。',
      refs: [['RAG', 'https://arxiv.org/abs/2005.11401'], ['RAG survey', 'https://arxiv.org/abs/2312.10997'], ['Structured Outputs', 'https://cookbook.openai.com/examples/structured_outputs_intro']]
    },
    '11-agents': {
      arc: 'Agent 从 ReAct 的思考-行动循环，发展到规划、记忆、代码执行、Computer Use、协议化工具和多 Agent 协作。',
      mechanics: '将 Agent 明确定义为“状态 -> 决策 -> 工具动作 -> 观测 -> 更新”的可恢复闭环，工具 schema、权限和停止条件与提示词同等重要。',
      tradeoff: '更多自主性会增加成本、延迟、越权和不可复现性；可靠 Agent 往往依赖确定性工作流、沙箱和人工接管。',
      frontier: 'MCP、A2A、Computer Use、SWE Agent 和 Agentic RL 快速演进，应区分协议事实、研究原型和生产经验。',
      check: '能记录完整轨迹，定义成功/失败/越权指标，并为工具超时、重复调用和外部副作用设计幂等回退。',
      refs: [['ReAct', 'https://arxiv.org/abs/2210.03629'], ['Toolformer', 'https://arxiv.org/abs/2302.04761'], ['OSWorld', 'https://arxiv.org/abs/2404.07972']]
    },
    '12-llmops': {
      arc: 'LLMOps 把离线实验、在线流量、数据回流、评测 CI、成本和安全护栏串成持续交付闭环。',
      mechanics: '每次请求应能关联 prompt/model/retrieval/tool/trace 版本，并将质量、延迟、token 和人工反馈写入可回放记录。',
      tradeoff: '更完整的 tracing 和评测会增加存储与延迟，但缺少证据就无法定位模型、数据还是工具导致的回归。',
      frontier: 'OpenTelemetry、自动评测、在线实验、模型路由和质量门禁正在成为默认基础设施。',
      check: '能定义一组线上 SLO、离线回归集和事故 runbook，并说明数据脱敏和采样策略。',
      refs: [['OpenTelemetry', 'https://opentelemetry.io/docs/'], ['Google SRE SLO', 'https://sre.google/sre-book/service-level-objectives/'], ['NIST AI RMF', 'https://www.nist.gov/itl/ai-risk-management-framework']]
    },
    '13-evaluation': {
      arc: '评测从单一准确率发展到 HELM、多维安全/鲁棒性、动态基准、污染检测、LLM Judge 和机制可解释性。',
      mechanics: '先定义任务和标签，再固定数据版本、提示模板、评分器、置信区间和人工抽检；分数必须能回溯到样本和轨迹。',
      tradeoff: '更大的 benchmark 不一定更可信；覆盖面、污染风险、评测成本、评分偏差和真实业务相关性需要共同权衡。',
      frontier: 'Agent 轨迹评测、机制可解释性、自动红队和持续评测仍在快速形成共识。',
      check: '能设计一个包含基准、对照、污染检查、统计不确定性和人工复核的完整评测实验。',
      refs: [['HELM', 'https://arxiv.org/abs/2211.09110'], ['BIG-bench', 'https://arxiv.org/abs/2206.04615'], ['Inspect AI', 'https://inspect.aisi.org.uk/']]
    },
    '14-governance': {
      arc: '治理从模型卡和偏见分析，发展到红队、隐私、版权、内容溯源、风险管理和部署后监测。',
      mechanics: '把风险映射到数据、训练、输入、工具、输出和运营环节，并为每项风险指定控制措施、证据和责任边界。',
      tradeoff: '过滤、审计和最小权限会增加开发成本，但缺少可追责证据时系统无法安全扩展。',
      frontier: '模型行为评测、来源证明、Agent 权限治理和法规落地仍随地区与版本变化，必须标注时效性。',
      check: '能为一个生成式应用写出风险登记表、红队方案、日志留存规则和上线门禁。',
      refs: [['Model Cards', 'https://arxiv.org/abs/1810.03993'], ['NIST AI RMF', 'https://www.nist.gov/itl/ai-risk-management-framework'], ['UNESCO AI Ethics', 'https://unesdoc.unesco.org/ark:/48223/pf0000381137']]
    },
    '15-practice': {
      arc: '实践章节把前面的抽象概念压缩成可运行闭环：数据、模型、训练/推理、指标、测试和故障诊断缺一不可。',
      mechanics: '每个实验都先建立最小基线，再逐项替换算法或系统组件，保留配置、随机种子、日志和对照结果。',
      tradeoff: '教学实现追求可读性，生产实现追求吞吐、鲁棒性和可维护性；两者差异应在实验结论中明确写出。',
      frontier: '实践优先选择已有开源实现和稳定协议，再用小规模实验验证原理，避免把不可复现的 demo 当作结论。',
      check: '能独立复现实验、解释指标变化，并把失败现象定位到数据、算法、系统或评测环节。',
      refs: [['nanoGPT', 'https://github.com/karpathy/nanoGPT'], ['Stanford CS336', 'https://cs336.stanford.edu/'], ['MCP Specification', 'https://modelcontextprotocol.io/specification/2025-06-18']]
    }
  };

  var TOPICS = {
    'attention': { arc: 'Bahdanau 注意力解决固定长度向量瓶颈，Transformer 改成全并行 scaled dot-product attention；FlashAttention 又把瓶颈从 FLOP 转向 HBM IO。', mechanics: '对 X 做 Q=XWq、K=XWk、V=XWv，计算 softmax(QK^T/sqrt(d))V；因果 mask 后第 i 行只能读 j<=i，朴素实现保存 O(n^2) 分数矩阵。', tradeoff: 'head_dim、GQA/MQA、mask 形状和 dtype 会决定 kernel 是否融合；长上下文中减少 KV 头数常比盲目降精度更直接。', frontier: 'FlashAttention-2/3、滑窗和稀疏注意力分别从调度、Tensor Core 与稀疏模式降低 IO，必须按长度和硬件复测。', check: '手算 4-token、2-head 的 QK^T、mask、softmax 和输出，并用 profiler 区分算力与显存瓶颈。' },
    'scaling-laws': { arc: 'Kaplan 用幂律拟合 loss 与参数、数据和计算量；Chinchilla 说明固定预算下旧路线往往模型过大、训练 token 不足。', mechanics: '典型形式为 L=Linf+A/N^a+B/D^b；实验必须把训练 FLOP、token、序列长度、重算和通信纳入同一预算表。', tradeoff: '小模型外推到大模型会受数据、架构和优化器影响，验证 loss 下降也可能与下游能力、污染和重复脱钩。', frontier: '多 token 预测、数据质量分层、合成数据和测试时计算正在扩展 scaling law 的变量，尚未形成单一公式。', check: '给定 10^23 FLOP 比较两组 N/D 配置，解释 token 不足导致的过拟合并设计跨规模消融。' },
    'grpo-rlvr': { arc: 'PPO 依赖 value model，DPO 绕过在线采样，GRPO 用同题多样本的组内相对奖励去掉 value model，RLVR 再把 verifier 作为奖励来源。', mechanics: '组内优势 A_i=(r_i-mean(r))/(std(r)+eps)，再用 ratio 的裁剪目标和 reference KL 更新；全对或全错组优势为零。', tradeoff: '组大小、奖励稀疏、长度偏置和 verifier 错误会直接改变梯度，不能只看 pass@1。', frontier: 'DeepSeekMath/R1 展示了可验证数学推理的规模化路径，迁移到开放域 Agent 仍需要过程奖励和副作用约束。', check: '手算奖励 [1,1,0,1] 的组内优势，解释零方差处理，并设计能抓住格式正确但答案错误的 verifier。' },
    'agent-algorithms': { arc: 'ReAct 交错推理与行动，Plan-and-Execute 拆分规划与执行，Reflexion、SWE-agent、OSWorld 把失败反馈、代码仓库和桌面环境纳入闭环。', mechanics: '轨迹可写成 tau=(s0,a0,o1,...,aT)；工具必须声明 schema、权限、超时、幂等性和结果校验，终止由成功判定或预算触发。', tradeoff: '自由循环提升覆盖面却增加 token、重复调用和越权风险；确定性工作流更稳，但需要明确编排边界。', frontier: 'MCP 解决工具协议，Agentic RL 研究轨迹信用分配，Computer Use 把视觉状态与鼠标键盘动作带入环境，成熟度不同。', check: '实现最大步数、工具超时、幂等写操作、轨迹回放和人工接管，并统计成功率、工具准确率和副作用率。' },
    'rag': { arc: 'RAG 从 DPR 稠密召回发展到 hybrid search、cross-encoder rerank、图检索和带引用的 Agentic RAG。', mechanics: '在线链路依次执行 query rewrite、召回、重排、上下文压缩和生成；faithfulness 要验证答案是否由证据支持。', tradeoff: 'chunk 越大语义越完整但噪声更高；top-k、重排深度和上下文长度共同决定延迟与成本，检索失败应允许 abstain。', frontier: 'GraphRAG、late interaction、多向量索引和检索训练正在改善复杂问题，但更新、引用粒度和污染仍是难点。', check: '用带 gold evidence 的问题集测 recall@k、MRR、context precision、faithfulness 和无答案拒答率。' },
    'kv-cache': { arc: 'KV Cache 消除 decode 阶段重复 K/V 计算；PagedAttention 切块管理，prefix caching 与 disaggregation 将缓存变成可调度资源。', mechanics: '缓存显存约为 2*layers*tokens*kv_heads*head_dim*bytes；GQA/MQA 通过减少 kv_heads 降低占用。', tradeoff: '共享缓存提高吞吐却引入匹配、租户隔离和失效策略；offload 节省显存但把瓶颈移到 PCIe/NVLink。', frontier: 'RadixAttention、KV 量化、选择性缓存和 Prefill/Decode 分离正在优化长上下文服务，需同时报告 TTFT、TPOT 和尾延迟。', check: '为 32 层、8 KV heads、128K context、BF16 模型估算缓存显存，并设计超限时的驱逐策略。' }
  };

  Object.assign(TOPICS, {
    'moe': { arc: '稀疏 MoE 从 conditional computation 走向 Switch、Mixtral 和细粒度专家；研究重点从“少算 FLOP”转向路由、通信和负载均衡。', mechanics: 'router 为每个 token 计算 gate，选择 top-k experts；辅助负载损失、capacity factor 和 token dropping 共同决定有效容量与训练稳定性。', tradeoff: '总参数量不等于激活参数量；专家并行的 all-to-all 通信、热点专家和 checkpoint 体积可能抵消计算收益。', frontier: 'shared expert、无辅助损失路由和细粒度专家正在减少路由冲突，但需报告 token-level 负载分布而非只报平均 FLOP。', check: '给出 8 experts、top-2、capacity factor=1.25 的 token 分配，计算溢出 token 数并解释路由退化。' },
    'long-context': { arc: '长上下文经历位置外推、RoPE scaling、长文档继续预训练和检索增强，窗口长度增加并不等价于有效利用率增加。', mechanics: '分别测长度外推、needle retrieval、跨段推理和位置偏置；记录有效 token、注意力衰减、KV 显存和训练数据长度分布。', tradeoff: '更长窗口带来 quadratic attention、缓存和噪声成本；上下文压缩、分块检索和摘要常比单纯扩窗更稳定。', frontier: 'YaRN、位置插值、Ring/Block attention 和长序列训练仍在演进，必须区分支持长度、训练长度和可靠工作长度。', check: '设计 4K/32K/128K 的同题对照，分别报告召回、推理、延迟和显存，而不是只写最大窗口。' },
    'multimodal': { arc: 'ViT/CLIP 将视觉表示接入语言模型，BLIP-2、Flamingo 和统一多模态模型逐步把图像、视频、音频纳入同一上下文。', mechanics: '视觉编码器输出 patch/token，connector 做投影或查询抽取，LLM 再以交叉注意力或前缀 token 消费；对齐数据与分辨率决定瓶颈。', tradeoff: '更高分辨率提升细节却增加视觉 token 和 KV 成本；冻结视觉塔稳定训练，但会限制领域适配。', frontier: '视频长时序、OCR/grounding、视觉工具调用和统一生成仍是活跃方向，评测需拆分感知、定位和推理。', check: '画出 image -> encoder -> connector -> LLM 的张量形状，并设计一个区分看错、读错和推理错的评测集。' },
    'dpo': { arc: 'DPO 将 RLHF 的偏好优化改写为 reference policy 上的分类式目标，随后出现 IPO、KTO、ORPO 等降低 reference 或偏好数据要求的方法。', mechanics: '核心 logit=beta*((log pi(y+)-log ref(y+))-(log pi(y-)-log ref(y-)))；只对 response token 求和，prompt token 不应进入偏好差。', tradeoff: 'beta、长度归一化、偏好噪声和 reference 漂移会改变梯度；margin 过大时 sigmoid 饱和，过拟合数据偏好。', frontier: '在线偏好、拒绝采样和 verifier preference 正在与 SFT/RLVR 合流，离线 DPO 仍需检查分布外行为。', check: '用两个 response 的 token log-prob 手算一次 DPO loss，比较 sum 与 mean reduction 的长度偏置。' },
    'quantization': { arc: '量化从 GPTQ/AWQ 的权重后训练量化，发展到 SmoothQuant、KV quant、FP8/FP4 和量化感知训练。', mechanics: '分别量化权重、激活和 KV；校准集决定 scale，异常通道会导致误差集中，per-channel/group-wise 颗粒度影响 kernel 效率。', tradeoff: '更低 bit 减少显存和带宽，却可能损害长上下文、稀有 token 和推理模型的细粒度概率；端到端吞吐不只由 bit 数决定。', frontier: 'W4A8、FP4 tensor core、动态激活量化和 KV 压缩快速发展，应同时报告 perplexity、任务准确率和实际 tokens/s。', check: '对同一模型比较 FP16、W8A8、W4A16 的误差、显存、首 token 延迟和长上下文退化。' },
    'agent-memory': { arc: 'Agent 记忆从简单对话历史发展到摘要、向量检索、事件记忆和可写长期状态；核心问题是何时写、何时读、何时遗忘。', mechanics: '把记忆分为 working/context、episodic、semantic 和 procedural，写入前做去重与权限过滤，读取后记录来源和新鲜度。', tradeoff: '记忆越多越容易污染当前任务；摘要压缩会丢失条件，向量相似度也不能替代时间、权限和冲突判断。', frontier: '记忆反思、用户模型和跨任务策略学习正在发展，长期一致性与可删除性仍缺少统一基准。', check: '设计写入/读取/更新/删除协议，并构造过期事实、冲突事实和越权记忆的回归用例。' },
    'agent-eval': { arc: 'Agent 评测从最终答案准确率扩展到 WebArena、SWE-bench、OSWorld 等环境中的轨迹、工具、成本和安全评测。', mechanics: '同时记录任务成功、步骤成功、工具参数、重试、token、延迟、人工接管和副作用；环境状态必须可重置、可回放。', tradeoff: '开放环境更真实但方差高、复现难；脚本化基准稳定却可能被提示模板过拟合。', frontier: '轨迹级 judge、过程验证和在线回归正在形成工具链，不能把 LLM-as-Judge 单独当作事实标准。', check: '对同一任务报告成功率置信区间、平均步数、p95 延迟、成本和越权率，并发布失败轨迹样例。' },
    'tool-use-mcp': { arc: '工具调用从手写 function schema 发展到 Toolformer 数据构造、模型原生调用和 MCP 协议化发现，协议统一不等于安全自动成立。', mechanics: '工具契约至少包含名称、参数 schema、权限、超时、幂等性、错误码和结果大小；调用前后都要检查提示注入和副作用。', tradeoff: '自动发现降低接入成本却扩大攻击面；强 schema 提高可验证性，却可能限制复杂工具的表达。', frontier: 'MCP 资源/提示/工具边界、代理间通信和沙箱执行正在快速演进，版本与权限必须显式记录。', check: '为一个有写操作的工具设计 allowlist、审批点、重试规则和审计事件，并验证重复提交不会产生二次副作用。' },
    'tokenization': { arc: '分词从词级和字符级方案发展到 BPE、WordPiece、Unigram 与 byte-level 编码，核心是在词表容量和序列长度之间做数据驱动折中。', mechanics: '训练阶段统计或优化子词单元，编码阶段按固定规则映射字符流；normalization、空格标记、特殊 token 和 offset mapping 都是接口契约。', tradeoff: '大词表降低平均 token 数，却增大 embedding、加剧长尾并可能损害多语公平；byte-level 无 OOV，但常产生更长序列。', frontier: '可学习 tokenizer、无 tokenizer 模型和领域自适应仍在研究，换词表通常意味着 embedding 与模型共同重训或迁移。', check: '手工执行数轮 BPE 合并，比较中英代码样本的压缩率，并验证 encode-decode、offset 和特殊 token 边界。' },
    'embeddings': { arc: '表示学习从稀疏 one-hot、Word2Vec/GloVe 静态向量，发展到上下文 token 表示与专门训练的句向量、检索向量。', mechanics: '输入 embedding 是参数查表；检索 embedding 通过对比学习让正样本靠近、负样本远离，使用前通常做 L2 归一化和内积搜索。', tradeoff: '更高维提升容量却放大存储与检索成本；通用模型覆盖广，领域模型更准但需要持续评测漂移。', frontier: '多向量、late interaction、指令化 embedding 与跨模态空间正在提升细粒度召回，索引成本同步上升。', check: '用一组带相关文档的问题比较两种 embedding 的 recall@5、MRR、向量存储与查询 p95。' },
    'language-model': { arc: '语言建模从 n-gram、RNN/Seq2Seq 发展到并行自回归 Transformer，并扩展出 masked、span corruption 和扩散式目标。', mechanics: '自回归模型分解 p(x)=∏p(x_t|x_<t)，训练使用 teacher forcing，推理逐 token 采样；loss mask 与 shifted labels 必须对齐。', tradeoff: '自回归目标统一且适合生成，却有串行 decode 成本和暴露偏差；双向目标理解强但不能直接按同一方式生成。', frontier: '多 token 预测、扩散语言模型和混合目标尝试提高训练信号或并行解码，尚未替代主流自回归接口。', check: '为 5-token 序列写出输入、标签和 causal mask，手算交叉熵并解释训练与推理计算图差异。' },
    'pre-transformer': { arc: 'RNN、LSTM、GRU 与 Seq2Seq attention 逐步解决序列状态、梯度和固定向量瓶颈，最终暴露串行计算限制，为 Transformer 铺路。', mechanics: '循环网络用 h_t=f(x_t,h_{t-1}) 压缩历史；门控控制写入、保留和输出，encoder-decoder attention 再允许解码器读取全部源状态。', tradeoff: '循环归纳偏置适合流式和短状态，却限制训练并行与长程梯度；注意力提高访问能力但引入序列平方关系。', frontier: '状态空间模型和混合循环/注意力架构重新利用线性递推优势，实际收益取决于硬件 kernel 与任务长度。', check: '比较同一长度下 RNN 与 self-attention 的关键路径、可并行度和状态内存，并手算一个 LSTM 门更新。' },
    'what-is-llm': { arc: '语言模型从统计计数、神经概率模型演进到自回归 Transformer；指令微调、偏好对齐和工具层改变的是交互行为，不应与基座训练混为一谈。', mechanics: '一次生成依次经过分词、embedding、逐层前向、logits、采样和 KV Cache 更新；模型权重、输入上下文与外部工具是三种不同的信息来源。', tradeoff: '更大模型提高模式覆盖，却不会自动获得实时事实、精确计算和持久记忆；这些能力通常需要检索、代码执行与状态系统。', frontier: '推理模型、多模态模型与 Agent 把测试时计算和环境反馈纳入系统，但“会生成解释”仍不等价于解释忠实。', check: '选一个回答错误，分别从训练知识、上下文、解码、工具和验证五层定位根因，并提出可测的系统修复。' },
    'model-families': { arc: 'Encoder-only、encoder-decoder、decoder-only 与扩散/状态空间路线分别优化理解、条件生成、统一续写和非自回归建模，没有按名称即可排序的单一谱系。', mechanics: '比较模型时同时记录训练目标、注意力方向、参数激活方式、上下文接口和解码过程；这些要素决定它适合分类、生成还是长序列。', tradeoff: '同规模模型会因 tokenizer、数据配比、后训练和推理预算产生巨大差异；参数量不能替代任务评测与部署基准。', frontier: 'MoE、混合注意力、扩散语言模型和原生多模态正在打破传统家族边界，选型应基于可复现能力矩阵。', check: '为检索编码、聊天生成、端侧部署和长文档推理各选一种架构，并写出不选其余方案的证据。' },
    'tech-map': { arc: '大模型工程已从单一模型训练扩展为数据、训练、推理、应用、评测和治理的完整技术栈，每层都有独立版本与责任边界。', mechanics: '用数据契约连接训练，用 API/事件契约连接服务，用评测集连接质量，用 trace 连接线上反馈；任何层都应可替换且可回放。', tradeoff: '自研越深控制力越强但验证和运维成本越高；托管能力降低启动成本，却带来供应商、隐私和可观测性边界。', frontier: '模型网关、统一评测、Agent 协议和推理资源编排正在成为跨层基础设施，不能由单个 prompt 代替。', check: '画出目标产品的技术栈，给每层标注输入、输出、所有者、版本、SLO 和失败降级。' },
    'timeline': { arc: '关键变化不是模型名称堆叠，而是注意力、规模律、指令对齐、推理时扩展和工具执行依次改变了可扩展能力的来源。', mechanics: '阅读时间线时区分论文首次提出、开源实现可复现、硬件支持成熟和产品大规模采用四个日期，避免把发布新闻当成技术成熟。', tradeoff: '前沿方法通常只在特定模型、数据或硬件上成立；越新的结果越需要检查消融、训练预算、污染和独立复现。', frontier: '多模态行动、RLVR、混合架构与低比特推理仍快速变化，稳定结论应按证据等级而非热度排序。', check: '任选一个前沿结论，列出原论文、独立复现、适用规模、失败场景和截至复核日期仍未知的部分。' },
    'learning-paths': { arc: '学习路线应从目标岗位反推交付物：算法路线重推导与实验，系统路线重 profiling 与容量，全栈路线重接口、评测和运行闭环。', mechanics: '每个阶段使用“先修 -> 核心概念 -> 可运行实验 -> 验收证据 -> 复盘”推进，章节阅读量不是完成度。', tradeoff: '广度能建立地图，深度才能定位问题；同时铺开所有方向会牺牲反馈速度，应以一个贯穿项目承载跨层知识。', frontier: '随着模型能力快速变化，稳定的学习资产是数学、系统测量、评测设计和故障归因，而不是供应商 API 记忆。', check: '选择一条路线，为四周学习周期定义每周产物、验收命令和一个可观察的失败注入。' },
    'architecture': { arc: 'Transformer 从 encoder-decoder 演进为 decoder-only 主流，随后引入 Pre-Norm、RMSNorm、SwiGLU、GQA/MQA 与 MoE 以改善稳定性和推理成本。', mechanics: '对形状 B×T×D 的残差流，单层依次执行 norm、causal attention、残差、norm、FFN、残差；每一步都必须保持 token 轴和隐藏维契约。', tradeoff: '增深提高组合层级却拉长串行路径，增宽提高容量但放大矩阵与缓存；头数、FFN 比例和 KV 头数共同决定参数与服务成本。', frontier: 'MLA、混合线性注意力、QK-Norm 与稀疏专家正在改变默认块结构，但端到端收益依赖训练和 kernel 配套。', check: '给定 B=2、T=8、D=16、4 heads，逐步写出 Q/K/V、attention、FFN 和残差张量形状并核算主要参数量。' },
    'multi-head': { arc: '多头注意力从等量 Q/K/V 头发展到 MQA、GQA 和 MLA，演进重点从表达子空间转向减少 decode 阶段 KV 读取。', mechanics: 'Q 头按 head_dim 切分；GQA 让多个 Q 头共享一组 K/V 头，输出拼接后再经 Wo 投影回 D，广播关系必须显式验证。', tradeoff: '更多 Q 头增加可分工子空间，但 KV 头越多缓存和带宽越高；过度共享又可能损害质量与长上下文召回。', frontier: 'head pruning、latent KV 与跨层缓存共享仍在探索，必须联合报告质量、KV 字节/token 和 TPOT。', check: '对 32 Q heads、8 KV heads、head_dim=128 计算每 token 每层 KV 大小，并与 MHA/MQA 比较。' },
    'normalization': { arc: 'BatchNorm 适合批统计，LayerNorm 适合序列模型；RMSNorm、省偏置变体和 Pre-Norm 逐渐成为大模型默认，QK-Norm 又把稳定器推进注意力打分。', mechanics: 'LayerNorm 对单 token 隐藏维计算均值和方差，RMSNorm 只计算均方根；统计量通常以 FP32 累积，再缩放回计算 dtype。', tradeoff: 'Pre-Norm 更易训练深层网络但可能稀释深层更新，Post-Norm 表达路径直接却更敏感；epsilon 和低精度实现会影响稳定区间。', frontier: 'QK-Norm、DeepNorm 与残差缩放尝试控制超深或长上下文模型的激活增长，结论依赖层数与初始化。', check: '手算一个 4 维向量的 LayerNorm/RMSNorm，比较输出，并构造 FP16 下 epsilon 过小导致异常的测试。' },
    'positional-encoding': { arc: '位置表示从绝对正弦与可学习 embedding，发展到相对位置、RoPE、ALiBi 及其长上下文缩放，目标从“知道位置”转向“可外推关系”。', mechanics: 'RoPE 按二维对子旋转 Q/K，使内积显式依赖相对位移；频率基底、position id 和 cache offset 必须在训练与增量推理间一致。', tradeoff: '更强外推往往牺牲短程分辨率或需要继续训练；支持窗口、训练窗口和可靠窗口不能写成同一个数字。', frontier: '位置插值、NTK/YaRN 缩放和分段频率方案持续演进，评价应覆盖不同深度位置与跨段推理。', check: '对一组二维 Q/K 手算两个位置的 RoPE 旋转和点积，并验证增量 decode 的 position offset。' },
    'ffn-activation': { arc: 'FFN 从 ReLU/GELU 两层 MLP 演进到 GLU、SwiGLU 和稀疏 MoE，逐渐承担大部分参数容量与条件计算。', mechanics: 'SwiGLU 计算 silu(XWg)⊙(XWu) 后经 Wd 投影；为保持参数量，门控中间维通常小于传统 4D FFN。', tradeoff: '更大中间维提高容量却增加参数、激活和通信；门控激活质量更好，但需要额外投影和融合 kernel。', frontier: 'MoE、低秩 FFN、结构化稀疏和动态深度都在重分配 token 级计算，路由稳定性比名义 FLOP 更重要。', check: '比较 D=4096 时传统 4D FFN 与 SwiGLU 的参数量和每 token GEMM 规模，并说明如何保持预算等价。' },
    'residual': { arc: '残差连接让深层网络保留恒等路径；与 Pre-Norm、残差缩放和并行分支结合后，成为控制梯度与激活传播的主干。', mechanics: '主路径保持 x，子层只学习增量 f(norm(x))；反向传播包含恒等项，使梯度不必完全穿过每个非线性子层。', tradeoff: '残差过强会让深层块贡献变小，增量过大又会造成激活漂移；dropout、缩放和 dtype 会改变平衡。', frontier: 'DeepNorm、ReZero、并行 attention/FFN 和层级缩放继续探索超深模型稳定性，但需与初始化和 norm 联合分析。', check: '用两层标量网络写出有无残差时的梯度链，构造监控每层 residual/branch norm 比例的诊断。' },
    'prompt-engineering': { arc: '提示设计从措辞技巧发展为任务契约、示例选择、结构约束和版本化评测；稳定系统依赖上下文与工具，而非“魔法句式”。', mechanics: '把提示拆成角色边界、任务、输入、约束、示例和输出 schema；动态数据必须与指令隔离并记录模板版本。', tradeoff: '更多示例可减少歧义却占用上下文并引入顺序偏差；强约束提高可解析性，但可能降低开放任务覆盖。', frontier: '自动提示搜索、DSPy 类编译和模型原生结构化输出正在替代手工微调措辞，核心仍是可执行评测。', check: '为一个抽取任务写最小 schema、三类边界样本和回归门禁，比较零样本与少样本的合法率和字段 F1。' },
    'context-engineering': { arc: '上下文工程把 prompt 扩展为检索证据、会话状态、工具结果和压缩策略的动态装配问题。', mechanics: '每段上下文应带来源、权限、新鲜度和 token 预算；装配顺序需处理指令优先级、去重、冲突与位置偏差。', tradeoff: '塞入更多 token 会增加成本和噪声，摘要会丢条件，截断会破坏因果链；预算应按任务价值分配而非平均切片。', frontier: '长上下文、上下文缓存、记忆和 Agentic retrieval 正在融合，但有效信息密度仍比最大窗口更关键。', check: '构造一组冲突、过期和越权上下文，验证装配器的排序、过滤、引用和拒答行为。' },
    'advanced-rag': { arc: '高级 RAG 从单次向量召回发展为查询改写、混合检索、cross-encoder 重排、上下文压缩和多跳检索。', mechanics: '召回阶段最大化 evidence recall，重排提高前列精度，生成阶段只消费稳定 chunk id；每层指标必须分开记录。', tradeoff: '重排深度和迭代轮数提升覆盖却增加尾延迟；查询改写可能扩大召回，也可能偏离用户原意。', frontier: 'late interaction、多向量文档表示、GraphRAG 与 Agentic RAG 在复杂问题上活跃，但索引更新和证据闭环仍是工程瓶颈。', check: '固定生成模型，扫描 hybrid 权重与 rerank top-k，报告 recall@k、MRR、faithfulness、p95 和单问成本。' },
    'structured-output': { arc: '结构化输出从提示 JSON、后处理修复发展到 function calling、JSON Schema 和约束解码，可靠性逐渐前移到生成过程。', mechanics: 'schema 同时约束类型、枚举、必填和嵌套；服务端仍需做语义校验、版本迁移与错误分类，语法合法不代表业务正确。', tradeoff: '约束越强重试越少，但复杂 schema 会提高解码开销并限制表达；宽松兼容又会把错误推给下游。', frontier: 'grammar-guided decoding、类型化 Agent 工具和可验证中间表示正在融合，跨供应商 schema 子集仍不一致。', check: '为版本化订单对象设计 schema，注入缺字段、非法枚举和语义冲突，验证错误码与迁移路径。' },
    'rag-agentic-lab': { arc: 'RAG 实验应从“能返回答案”升级为检索、重排、引用、验证和拒答的分层可复现实验。', mechanics: 'gold evidence 将问题与证据绑定；索引版本、chunk id、query、候选分数和最终引用共同组成可追溯链。', tradeoff: '多轮检索覆盖复杂问题，却会放大查询漂移、成本和不可复现性；每轮必须有触发条件和最大预算。', frontier: 'Agentic RAG、图检索与多模态证据正在融合，效果必须通过任务级证据覆盖和答案忠实度判断。', check: '完成至少 50 个带 gold evidence 的问题集，分层报告召回失败、重排失败、上下文截断和生成幻觉。' },
    'agent': { arc: 'Agent 从 ReAct 循环扩展到规划执行、反思、工作流编排和环境反馈；可靠性来自状态机与工具契约，不来自更长思维链。', mechanics: '每步读取状态，选择动作，校验工具参数，执行并记录 observation；成功条件、预算和停止原因必须机器可判定。', tradeoff: '开放循环提高任务覆盖却增加方差、成本和副作用；确定性节点更易测试，但需要显式设计转移与恢复。', frontier: 'Computer Use、代码 Agent 和 Agentic RL 正在扩大行动空间，沙箱、权限与轨迹评测仍是部署前提。', check: '实现一个最多 6 步的 Agent 状态机，注入工具超时和错误结果，验证重试、回退、接管和审计事件。' },
    'agent-safety': { arc: 'Agent 安全从文本过滤扩展到工具权限、提示注入、数据外泄、资源耗尽和不可逆副作用控制。', mechanics: '输入与工具结果均视为不可信；动作前执行 allowlist、参数校验、最小权限和审批，动作后核验环境状态。', tradeoff: '更严格审批降低自主性与速度，但高影响写操作不能仅靠模型自评；隔离强度应按资产风险分级。', frontier: '间接提示注入、跨工具数据流和长轨迹越权仍缺少统一防线，需结合 capability sandbox 与持续红队。', check: '对邮件读取后调用外部写工具的场景做威胁建模，验证恶意文档不能改变系统指令或外传秘密。' },
    'multi-agent': { arc: '多 Agent 从角色对话演进为任务分解、并行执行、辩论与层级调度；多个模型并不会自动带来正确性。', mechanics: '共享任务需定义消息 schema、所有权、终止、冲突合并和公共状态版本；独立子任务才适合并行。', tradeoff: '并行可降低墙钟时间，却增加通信 token、重复劳动与一致性成本；集中调度稳定但形成单点瓶颈。', frontier: 'Agent-to-Agent 协议、群体搜索和专业模型路由快速演进，收益必须扣除协调成本与错误相关性。', check: '把一个任务分成可并行与强依赖两部分，记录单 Agent/多 Agent 的成功率、token、时延和冲突次数。' },
    'computer-use': { arc: 'Computer Use 将 Agent 动作从结构化 API 扩展到截图、鼠标和键盘，覆盖旧系统的同时失去稳定 schema。', mechanics: '循环包含截图感知、元素定位、动作生成、执行和状态核验；坐标、缩放、窗口焦点和敏感区域都必须校验。', tradeoff: '视觉操作通用但脆弱、慢且难复现；有 API 时应优先 API，GUI 作为兼容层并限制高风险动作。', frontier: '视觉 grounding、DOM/无障碍树融合和桌面基准持续进步，真实环境漂移仍使离线分数偏乐观。', check: '设计一个可重置网页任务，分别用 DOM 工具和截图坐标完成，比较成功率、步骤数与误点击风险。' },
    'eval-methods': { arc: '模型评测从单一准确率演进为任务契约、分层指标、统计不确定性、人工复核和持续回归。', mechanics: '样本、模型、提示、工具、评分器与随机种子都要版本化；比较版本优先使用配对数据和置信区间。', tradeoff: '自动指标便宜稳定但可能偏离真实质量，人工评审更贴近任务却成本高、方差大；两者需要校准组合。', frontier: 'LLM Judge、轨迹评测和线上持续评测正在普及，Judge 偏差与数据污染仍必须独立审计。', check: '为 100 个配对样本计算差异、Wilson/Bootstrap 区间，列出按难度和失败类型的切片结论。' },
    'evaluation-lab': { arc: '可信评测实验将题目、任务契约、评分、统计检验、污染检查和发布门禁连成可回放闭环。', mechanics: '每行结果绑定 sample id、输入 hash、模型/提示版本、输出、判定、token、延迟、成本和失败归因。', tradeoff: '扩大样本降低统计噪声，却不修复任务定义偏差；更多 Judge 调用也不能替代关键样本的人审校准。', frontier: '动态基准、环境型 Agent 评测和过程验证逐渐替代静态题库，但复现成本与环境漂移更高。', check: '建立一个同时约束质量下限、p95、单问成本和安全红线的门禁，并验证任一红线失败都会阻断。' },
    'benchmarks': { arc: '基准从 MMLU、BIG-bench 等静态题库扩展到 HELM 多维评测、代码执行、网页和桌面环境任务。', mechanics: '解读分数时核对任务构成、shot 设置、工具权限、采样参数、评分脚本和置信区间，不能只抄榜单。', tradeoff: '覆盖广的基准便于比较，却可能与业务脱节并被训练污染；私有集更相关但缺少公开可比性。', frontier: '动态生成、抗污染和交互环境基准增长迅速，排行榜结论需要版本与时间戳。', check: '选择两个模型，复核一项公开榜单的配置并用 30 个私有样本验证排名是否仍成立。' },
    'contamination': { arc: '污染检测从精确字符串匹配发展到 n-gram、语义近邻、时间切分和 canary，但没有单一方法能证明模型从未见过样本。', mechanics: '分别检查训练-测试重叠、提示泄漏和评测调参过拟合；保存数据快照 hash 与可疑匹配证据。', tradeoff: '严格去重会误删合法相似样本，宽松检测又漏掉改写和翻译；污染风险应作为不确定性报告。', frontier: '动态私有集、可验证数据谱系和训练数据审计仍在发展，闭源训练数据下结论尤其受限。', check: '对一组题目实现精确与 13-gram 匹配，人工审查边界案例，并比较清洗前后的置信区间。' },
    'hallucination': { arc: '幻觉治理从事实核对扩展为检索失败、证据冲突、生成不忠实和过度回答的分层诊断。', mechanics: '先判断答案是否可由上下文蕴含，再检查引用存在性、冲突和时效；无证据时允许 abstain，而非强迫生成。', tradeoff: '更严格拒答提高精确性却降低覆盖，更多检索可能引入噪声；阈值应按业务损失而不是统一设定。', frontier: '可归因生成、self-verification 和事实性 Judge 快速发展，但模型自检与生成错误往往相关。', check: '构造有证据、无证据、冲突证据和过期证据四类样本，分别统计忠实度与拒答准确率。' },
    'interpretability': { arc: '可解释性从 attention 可视化、探针发展到因果干预、激活 patching、稀疏自编码器和电路分析。', mechanics: '相关性观察不能证明机制；需要通过 ablation、patching 或受控激活验证特征对输出的因果贡献。', tradeoff: '细粒度分析成本高且结论常依赖模型与提示；易读可视化可能掩盖多义特征和分布外失效。', frontier: '大规模 SAE、自动电路发现和行为-机制对齐仍在快速发展，稳定性与可复现性是关键。', check: '为一个已知行为设计基线、干预和对照，区分“相关激活”与“删除后确实改变输出”的因果证据。' },
    'sae-circuits': { arc: '稀疏自编码器尝试把稠密激活分解为可命名特征，再通过 feature attribution 与 circuit tracing 连接到行为。', mechanics: '编码器产生稀疏特征，解码器重构激活；需同时报告重构误差、稀疏度、dead features 与干预效果。', tradeoff: '更多特征降低重构误差却提高解释负担；自动命名可扩展，但标签可能只是相关描述而非机制。', frontier: '跨层特征、跨模型对齐和自动电路追踪正在扩展规模，尚缺统一的解释质量基准。', check: '训练或分析一个小型 SAE，选三项特征做最大激活样本、消融和定向激活对照。' },
    'fullstack-llm-app': { arc: '大模型应用从浏览器直连模型的 demo，演进为前端、业务 API、检索、模型网关、评测和观测分层的可交付系统。', mechanics: '浏览器只依赖业务 SSE 契约；后端负责输入校验、检索引用、模型路由和错误收敛，citation/token/done/error 事件相互独立。', tradeoff: 'demo 内存检索便于理解链路，却不提供持久化、权限和语义召回；生产替换必须保持 API 契约并补齐限流、超时和审计。', frontier: '模型路由、Agent 工作流、在线评测和 OpenTelemetry 正在进入统一应用平台，核心仍是每个边界可替换、可回放、可降级。', check: '从干净环境启动项目，写入文档并获得带引用流式回答；再注入空召回、上游超时和用户取消，验证事件与 UI 状态。' }
  });

  function esc(s) { return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function render() {
    var body = document.body, partId = body.getAttribute('data-part'), topicId = body.getAttribute('data-topic');
    if (!partId || !topicId || document.querySelector('.technical-deepening')) return;
    var t = THREADS[partId]; if (!t) return;
    if (TOPICS[topicId]) t = Object.assign({}, t, TOPICS[topicId]);
    var topic = (window.TOC && window.TOC.parts || []).reduce(function (found, p) { return found || (p.id === partId ? (p.topics || []).find(function (x) { return x.id === topicId; }) : null); }, null);
    var title = topic ? topic.title : topicId;
    var section = document.createElement('section'); section.className = 'technical-deepening';
    section.innerHTML = '<div class="td-kicker">本页新增 · 技术深化</div><h2>围绕“' + esc(title) + '”继续深入</h2>' +
      '<div class="td-grid"><article><h3>发展脉络</h3><p>' + esc(t.arc) + '</p></article>' +
      '<article><h3>机制抓手</h3><p>' + esc(t.mechanics) + '</p></article>' +
      '<article><h3>工程权衡</h3><p>' + esc(t.tradeoff) + '</p></article>' +
      '<article><h3>前沿观察</h3><p>' + esc(t.frontier) + '</p></article></div>' +
      '<div class="td-check"><strong>实践检查</strong><span>' + esc(t.check) + '</span></div>' +
      '<div class="td-refs"><strong>经典与延伸</strong>' + t.refs.map(function (r) { return '<a href="' + r[1] + '" target="_blank" rel="noopener noreferrer">' + esc(r[0]) + ' ↗</a>'; }).join('') + '</div>';
    var container = document.querySelector('.container'), ref = Array.from(container.querySelectorAll('h2')).find(function (h) { return /论文|参考|资料/.test(h.textContent); });
    if (ref) ref.parentNode.insertBefore(section, ref); else container.appendChild(section);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render); else render();
  window.CB_DEPTH_DATA = THREADS;
  window.CB_DEPTH_TOPICS = TOPICS;
  window.CB_RENDER_DEPTH = render;
})();
