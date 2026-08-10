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

  function esc(s) { return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function render() {
    var body = document.body, partId = body.getAttribute('data-part'), topicId = body.getAttribute('data-topic');
    if (!partId || !topicId || document.querySelector('.technical-deepening')) return;
    var t = THREADS[partId]; if (!t) return;
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
  window.CB_RENDER_DEPTH = render;
})();
