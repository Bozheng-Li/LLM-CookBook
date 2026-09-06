# 全书 55 章内容大纲（撰稿内容基准）

说明：每章按大纲展开，覆盖所有列出的知识点。论文均给出 arXiv 号。写作规范见 STYLE-GUIDE.md。

## 第 0 章 ch00-guide.html 序言、学习路径与全书地图
- 本书定位与读者画像；与《大模型大全》类参考书的差异（多模态专精+HTML交互）
- 全书十部分结构说明；四阶段学习路径：入门（0-8章）→核心理论（9-16）→架构与生成（17-33）→实战前沿（34-54）
- 三种阅读路线：研究者路线/工程师路线/速查路线（各配 SVG 路线图，共≥2 张 SVG）
- 环境准备：Python/PyTorch/CUDA/transformers/trl/diffusers 安装命令；硬件建议表
- 如何读论文、如何用本书的论文清单；符号约定表（张量记号等）
- 全书知识依赖图（大 SVG）

## 第 1 章 ch01-math-optimization.html 数学基础与优化理论
- 线性代数速览：矩阵分解、特征值、SVD 与多模态子空间
- 概率与信息论：KL 散度、交叉熵、互信息（为对比学习铺垫）
- 优化器演进：SGD→动量→Adam→AdamW（更新公式逐一推导）
- 学习率：warmup 原理、cosine/linear schedule、梯度裁剪
- 混合精度训练：FP16/BF16/FP8、loss scaling
- Muon 优化器（2024）简述
- 论文：Adam (1412.6980)、AdamW (1711.05101)、Kingma & Ba
- 表：优化器对比；不同阶段超参建议表；SVG：优化器损失面轨迹图

## 第 2 章 ch02-tokenization.html Tokenization：文本 BPE 与视觉 Token 化
- 为什么不按字符/词切分；BPE 完整算法+手工演算例子
- WordPiece/SentencePiece/Unigram；HuggingFace tokenizers 代码
- 特殊 token 与聊天模板；多模态中的特殊 token（<image>、<|image_pad|>）
- 视觉 Token 化路线 A：patch embedding（ViT 式）
- 路线 B：离散视觉词表：VQ-VAE (1711.00937)、VQGAN (2012.09841)、codebook
- 图像 token 数量估算与上下文预算；不同模型 token 策略对比表
- 论文：ViT (2010.11929)、VQ-VAE、VQGAN、Chameleon (2405.09818)
- SVG：BPE 合并过程、patch 切分示意、连续vs离散视觉token对比

## 第 3 章 ch03-transformer.html Transformer 架构详解
- 编码器-解码器→decoder-only 演进；GPT 与 BERT 分野
- 嵌入层；自注意力完整数学（QKV、缩放因子 1/√d 推导）
- 多头注意力；位置编码：正弦、可学习、RoPE 推导（2024-2026 主流）
- FFN 与 SwiGLU；LayerNorm/PreNorm/RMSNorm
- 注意力病理：attention sink、长度外推（NTK-aware、YaRN）
- KV Cache 原理与显存计算公式
- 多模态视角：文本流与视觉流如何共享/分离注意力（为 ch13 铺垫）
- 论文：Transformer (1706.03762)、RoPE (2104.09864)、GPT-3 (2005.14165)
- 图：ar5iv 原图 + 自绘张量形状流动 SVG；表：架构变体对比

## 第 4 章 ch04-flash-attention.html Flash Attention 与高效注意力
- 标准注意力的 HBM 瓶颈：内存 vs 计算分析（roofline）
- tiling + online softmax 完整推导（含数值例）
- 反向传播重计算；FA2 并行度改进；FA3 (2407.08608) Hopper 特性、FP8
- varlen 注意力与多模态打包（图文序列、多图）；滑动窗口/MQA/GQA
- 对多模态的意义：高分辨率→万级视觉 token→显存爆炸
- 论文：FA (2205.14135)、FA2 (2307.08691)、FA3 (2407.08608)、MQA/GQA (2305.13245v2? 用 2305.13246? → 写 GQA 论文名 "GQA: Training Generalized Multi-Query Transformer" arXiv:2305.13245)
- 代码：PyTorch scale_dot_product_attention 与 flash-attn-2 调用；SVG：tile 分块计算示意

## 第 5 章 ch05-cv-basics.html 计算机视觉基础
- 卷积网络简史：LeNet→AlexNet (1409.0575 ImageNet 论文)→VGG→ResNet (1512.03385)（残差推导）
- 检测（Faster R-CNN、YOLO）与分割（Mask R-CNN）一页通
- BatchNorm/数据增强/训练技巧
- ViT 前史：iGPT、DEiT 知识蒸馏；CNN vs ViT 归纳偏置讨论
- 下游任务表示学习：监督→自监督（对比/掩码）
- 论文：ResNet、ViT (2010.11929)、DEiT (2012.12877)
- 图：ResNet 原图、检测/分割任务示意 SVG；表：经典 CNN 对比

## 第 6 章 ch06-nlp-basics.html 自然语言处理：从 Word2Vec 到 BERT
- 分布式语义与 word2vec (1301.3781)：CBOW/Skip-gram、负采样推导
- seq2seq 与注意力机制 (1409.0473 Bahdanau；1508.04025 Luong)
- ELMo 上下文词向量；BERT (1810.04805)：MLM/NSP、fine-tune 范式
- GPT 谱系 1→2→3；zero/few-shot 涌现
- 交叉模态启示：BERT 式融合 → ViLBERT（引出第二部分）
- 论文：word2vec、Attention (1706.03762 复引)、BERT、GPT-2 (1904.??) → 写 GPT-2 无 arXiv 则提 OpenAI 博客
- SVG：word2vec 窗口、BERT 预训练示意；代码：HF pipeline

## 第 7 章 ch07-llm-basics.html 大语言模型基础
- 预训练：Scaling Laws (2001.08361) 与 Chinchilla (2203.15556) 计算/参数配比
- 数据管道：去重、过滤、课程
- SFT：LIMA 原则、指令数据；解码策略全家桶（greedy/beam/top-k/top-p/min-p/温度）数学+代码
- RLHF 三阶段（InstructGPT 2203.02155）；RLHF 数学（为 ch37 铺垫）
- 压缩：量化（INT8/INT4/GPTQ/AWQ）、蒸馏、剪枝
- 推测解码 (2211.15078)、Medusa、Eagle
- 幻觉定义与检测综述；LLM 安全基础
- 代码：TRL SFTTrainer 最小例；表：解码策略对比、量化方案对比

## 第 8 章 ch08-gpu-systems.html GPU 架构与训练系统
- GPU 为什么快：SM 结构、内存层级（寄存器/共享内存/L2/HBM）、tensor core
- 世代演进：V100→A100→H100→B200 关键规格表
- Roofline 模型；算子强度；注意力是访存受限、FFN 是算力受限
- 通信：NVLink/IB/PCIe；集合通信（all-reduce 等）
- 数据并行 DDP 原理与代码；ZeRO 1-3 思想（详留给 ch38）
- vLLM PagedAttention (2309.06180)：KV 显存碎片问题、虚拟内存式分页、continuous batching
- 图：GPU 内部结构 SVG、PagedAttention 原图；表：GPU 规格对比

## 第 9 章 ch09-mm-intro.html 多模态学习导论
- 定义与动机；多模态的heterogeneity（信息不对称、结构差异、语义差距）
- 五大核心技术挑战框架：表示/对齐/融合/转换/协同（Baltrušaitis 综述 1905.12660? → 综述 IEEE TPAMI 无 arXiv 写会议信息）
- 多模态简史：AVSR (1990s)→多核学习→深度学习时代（2015 Show and Tell 1502.03044、VQA 1504.00325 → VQA v1 论文 arXiv:1504.00325）→Transformer 融合→CLIP→LLM 时代
- 多模态任务地图：理解/检索/生成/编辑/定位/Agent；应用场景
- 为什么多模态 LLM ≠ LLM+编码器：粒度、空间、时序、幻觉新形态
- 2024-2026 趋势概览（原生多模态、统一模型、视频、具身）
- 图：任务地图大 SVG；历史时间线 SVG；表：五大挑战×代表方法

## 第 10 章 ch10-mm-representation.html 多模态表示学习
- 联合表示 vs 协调表示；共享子空间
- 经典：CCA、多核学习、深度 CCA
- 视觉语义嵌入：DeViSE (1305.15370?→1311.?). DeViSE arXiv:1311.5525? 实际 Frome et al. DeViSE arXiv:1311.3138? 不确定则只写论文名和年份。VSE (1504.06060)、VSE++ (1707.05612) hard negative 推导
- 双编码器 vs 单编码器融合谱系；冻结 vs 联合训练
- 表示性质评估：检索 R@K、对齐探针、跨模态泛化
- 模态差距（modality gap）现象 2023 研究
- 代码：CLIP 双塔最小实现；SVG：联合/协调空间对比；表：检索模型演进

## 第 11 章 ch11-vlp-classics.html 视觉语言预训练经典模型（2019–2021）
- VLP 时代背景：检测特征 (bottom-up 1707.07998)→grid 特征
- 单流 vs 双流：ViLBERT (1908.02265)、LXMERT (1908.07490)
- 预训练目标全景：MLM/ITM/ITC/MRR/MASK；UNITER (1909.11790) 统一
- OSCAR (2004.06165) tag 引入；VinVL (2101.00520)
- 端到端路线：Pixel-BERT；统一框架 UNICORN/OFA (2202.03052)
- 为什么被 CLIP+LLM 范式取代：任务特化、数据规模、架构耦合——历史的教训
- 表：VLP 模型×预训练目标大矩阵；图：ViLBERT/LXMERT 原图、目标函数 SVG

## 第 12 章 ch12-clip.html 对比学习与 CLIP 深度剖析（核心大章）
- 对比学习基础：InfoNCE 推导（互信息下界完整证明）
- 温度参数作用；批内负样本与假阴性
- CLIP (2103.00020)：4 亿图文对、架构、训练细节（论文 Appendix 级细节）
- Prompt engineering 与 ensemble；zero-shot 分类数学（softmax 温度）
- 局限：计数、细粒度、组合性（ARO benchmark）、脆弱性
- 家族演进：OpenCLIP/LAION-400M/2B (2210.08402)、EVA-CLIP (2303.15389)、SigLIP (2303.15343) sigmoid loss 推导、SigLIP-2 (2502.14786)、MetaCLIP (2309.16671)、DFN (2309.17425)、DataComp (2304.14108)
- 蒸馏到多模态 LLM：CLIP 作为视觉塔的得与失（hallucination、分辨率）
- 代码：OpenCLIP 训练脚本精讲、CLIP 检索/分类实战；SVG：双塔+温度、SigLIP vs CE 对比
- 表：CLIP 家族数据/性能对比

## 第 13 章 ch13-fusion.html 模态融合机制深度解析
- 融合分类：早期/晚期/混合；融合位置消融研究
- Cross-Attention 数学详解（Flamingo 式）：视觉为 K/V 文本为 Q；门控 tanh(α) 初始化→零初始化意义
- FiLM 特征级调制；Bottleneck 融合；Fusion-in-Decoder vs Fusion-in-Encoder
- token 级融合：插入 <img> token 的机制；注意力掩码设计（causal 跨模态）
- 双向 vs 单向注意力在多模态的选择（编码器双向/解码器因果）
- 融合的失败模式：模态坍塌、文本主导、视觉信息稀释
- 代码：从零实现 cross-attention 层；SVG：三种融合拓扑图；表：融合策略×代表模型×优缺点

## 第 14 章 ch14-vision-encoders.html 视觉编码器家族
- 选择维度：分辨率、patch 数、监督信号、感受野
- 分类监督：ViT/Swin (2103.14030)；自监督：MAE (2111.06377) 推导、DINOv2 (2304.07193)
- CLIP 监督：EVA-CLIP、SigLIP 塔对比（same-pretrain 匹配问题）
- 分辨率与动态分辨率；NaViT (2307.06304) patch n' pack
- SAM (2304.02643) 与分割先验；InternViT (2312.14238) 大塔
- 编码器组合研究：Cambrian-1 (2406.16860) SP 空间、Eagle (2401.14809) MoE 编码器、BRAVE
- 编码器对下游 VQA/OCR/grounding 影响的实证（Prismatic 2402.07865 结论）
- 表：编码器全景（参数/分辨率/预训练/许可）；SVG：编码器决策树

## 第 15 章 ch15-connectors.html 视觉—语言连接器设计（核心大章）
- 问题形式化：N_patch→M token；信息保留 vs 上下文预算
- 线性投影（LLaVA 1）与两层 MLP（LLaVA-1.5）为什么这么强
- Q-Former (BLIP-2 2301.12597)：可学习 query、stage1/stage2 目标详解+失败分析
- Perceiver Resampler (Flamingo 2204.14198)；C-Abstractor (Honeybee 2312.06742)
- Pixel Shuffle/Unshuffle（InternVL）；token 压缩：TokenPacker、LLaVA-PruMerge
- 视觉专家：CogVLM (2311.10782) visual expert 模块；Cross-attention（mPLUG-Owl）
- 连接器对比研究：Prismatic (2402.07865)、MM1 (2403.09611) 消融结论
- 表：连接器×token数×信息损失×训练成本；SVG：Q-Former 数据流详解（重点 SVG）

## 第 16 章 ch16-visual-instruction-tuning.html 视觉指令微调
- LLaVA (2304.08485)：GPT-4 生成指令数据全流程（conversation/detail/reasoning 三类）
- LLaVA-1.5 (2310.03744)：学术任务 VQA 数据混合的魔力；LLaVA-NeXT/OneVision (2408.03326)
- InstructBLIP (2305.06500)：指令感知的 Q-Former；MiniGPT-4 (2304.10592)
- mPLUG-Owl 系列；数据质量法则：ShareGPT4V、ALLaVA 合成数据
- 指令数据工程：多样性/复杂性/平衡；数据配方消融（Qwen-VL 论文数据表）
- SFT 细节：loss masking（只对回答算 loss）、打包、视觉 token 不算 loss
- 代码：LLaVA 风格 SFT 完整脚本（HF+多卡）；表：指令数据集全景；SVG：LLaVA 训练流水线

## 第 17 章 ch17-open-models.html 开源多模态大模型谱系（核心大章）
- LLaVA 系：1.5→1.6→NeXT→OneVision 技术演进
- Qwen-VL (2308.12966)→Qwen2-VL (2409.12191) NaViT 动态分辨率+M-RoPE→Qwen2.5-VL (2502.13923)→Qwen3-VL (2025)
- InternVL 1.0→1.5→2.0→2.5 (2412.05271)→3/3.5：动态分辨率+像素重排+渐进对齐
- MiniCPM-V (2408.01800) 端侧路线；DeepSeek-VL (2403.05525) 混合签名；Phi-3.5-Vision
- CogVLM/CogAgent；MoE-LLaVA (2401.15947)；GLM-4V
- 架构对比大表：视觉塔/连接器/分辨率/数据/许可/SOTA 分数
- 选型指南：什么场景用什么模型；本地部署起步代码
- 图：各代模型原图精选 ≥4 张；SVG：谱系演化树

## 第 18 章 ch18-closed-models.html 闭源多模态模型剖析
- Flamingo (2204.14198) 详解：Perceiver Resampler+GATED XATTN-DENSE、80B、few-shot
- GPT-4V/4o：系统能力分析（System Card 信息）、流式语音视觉实时
- Gemini 1.5/2.x：MoE、长上下文视频；Claude vision；o 系列视觉推理
- 闭源 API 使用模式：图像输入规范、cost、rate limit；结构化输出
- 闭源 vs 开源差距量化（MMMU/LMArena 2024-2026 轨迹）；何时选闭源
- 评测 API 模型的实践脚本；SVG：闭源模型能力雷达图（手绘示意）

## 第 19 章 ch19-native-mm.html 原生多模态与早期融合
- 适配器路线的天花板；原生多模态定义
- Chameleon (2405.09818)：VQ tokenizer 早期融合、QK-norm 稳定性、训练 recipe
- Fuyu-8B：patch 直接进 decoder、无独立视觉塔
- Transfusion (2408.11039)：单 Transformer 内 LM+Diffusion 双目标推导
- 理论分析：早期 vs 晚期融合的表示效率（多模态 scaling law 研究）
- 风险与工程：训练不稳定、 tokenizer 信息损失、数据配比
- 表：原生 vs 适配器对比；图：Chameleon/Transfusion 原图；SVG：两种路线架构对比

## 第 20 章 ch20-unified-models.html 统一理解与生成模型
- 统一动机：理解⇄生成闭环
- Unified-IO (2206.08916)/UIO-2 (2310.16013)：离散化一切
- SEED (2307.08052)/SEED-X：语义视觉 token；Emu/Emu2/Emu3 (2409.18869) 自回归生成
- Janus (2410.13848)/Janus-Pro (2501.17811)：理解/生成解耦视觉编码器
- Show-o (2408.12528)：AR+离散扩散混合；omni 系列（实时全双工语音视觉）
- 统一模型的评测：理解不掉点吗？生成质量对比
- 表：统一模型大对比；图：Janus/Emu3 原图；SVG：统一架构谱系

## 第 21 章 ch21-grounding.html 细粒度感知与视觉定位
- Grounding 任务谱系：REC、REG、短语定位、分割对话
- Kosmos-2 (2306.14824)：定位数据 GRIT、文本内嵌 box token
- Shikra (2306.15195) 坐标数字文本化；Ferret (2310.07704) 混合区域表示+space-filling curve
- GLaMM (2311.03356) 像素级输出；Kosmos-2.5 文档
- Grounding 数据构造（SAM+检测器自动标注）；grounding 能力提升整体感知实证
- 表：grounding 模型对比；图：Ferret/GLaMM 原图；SVG：box 表示法对比

## 第 22 章 ch22-highres-docs.html 高分辨率与文档图表理解
- 低分辨率的代价：文字模糊、小物体；分辨率策略分类
- AnyRes（LLaVA-NeXT 切块策略）；InternVL 动态分辨率 tile 策略；Qwen2-VL NaViT 原生任意分辨率
- OCR-free 文档理解：Donut (2111.15664)、Pix2Struct (2210.03347)、UReader、mPLUG-DocOwl、GOT-OCR2.0 (2409.01704)
- 表格解析与 ChartQA/ChartLlama；数学几何图形（MathVista 类型）
- 文档智能生产管道：版面分析+VLM 混合方案；评估指标（CDM、TEDS）
- 表：文档模型×指标（DocVQA/ChartQA/OCRBench）；SVG：AnyRes 切块+拼接示意

## 第 23 章 ch23-generative-basics.html 生成模型基础：VAE 与 GAN
- 生成模型地图：likelihood-free vs likelihood-based
- VAE：ELBO 完整推导、重参数化、后验坍塌；VQ-VAE 离散化（承接 ch2）
- GAN (1406.2661)：minimax 推导、JS 散度、模式崩溃；StyleGAN 简述
- 两者为何被扩散取代；但在多模态 LLM 中 VAE 以 latent 形式复活（SD）+ tokenizer 复活（Chameleon）
- 代码：极简 VAE 训练 MNIST；SVG：VAE/GAN 结构图；表：生成模型族谱

## 第 24 章 ch24-diffusion.html 扩散模型：从 DDPM 到 Score SDE（核心大章）
- DDPM (2006.11239) 前向加噪推导；训练目标推导（噪声预测等价 ELBO）
- 采样：ancestral sampling；DDIM (2010.02502) 非马尔可夫、加速采样推导
- score matching 与 SDE 视角（概率流 ODE）；EDM (2206.00364) 设计空间
- 条件生成：CFG (2206.00364? → CFG 出自 Ho & Salimans 2207.12598) 完整推导与 guidance scale
- 评测：FID/IS/CLIP-score；sampler 对比表（DPM-Solver 等）
- 代码：从零实现 DDPM（MNIST/CIFAR 完整训练代码）；SVG：加噪/去噪链路图

## 第 25 章 ch25-latent-diffusion.html 潜在扩散与 Stable Diffusion（核心大章）
- 像素空间→潜在空间的动机与 8× 降采样
- LDM (2112.10752) 架构：VAE、UNet（ResBlock/Attention/时间嵌入详解）、CLIP 文本编码器
- Stable Diffusion 1.x/2.x 差异；CFG 实践；负提示词原理
- 采样器实战（Euler a/DPM++/UniPC）；SDXL (2307.01952)：双文本编码器、refiner、分辨率条件
- 训练微调：全参 vs LoRA vs textual inversion（详留 ch28）；显存分析
- 代码：diffusers 全流程（生成/img2img/inpaint）+ UNet 结构打印；SVG：LDM 全架构图（重点 SVG）

## 第 26 章 ch26-control-editing.html 条件控制与图像编辑
- 控制需求谱系：结构/语义/身份/指令
- ControlNet (2302.05543)：zero-convolution 数学与动机、完整推导；T2I-Adapter 对比
- IP-Adapter：解耦交叉注意力（图像 prompt）；Reference-only
- 编辑：InstructPix2Pix (2210.09261?) → InstructPix2Pix arXiv:2210.09261 不确定 → 写论文名+2023 CVPR。SDEdit、P2P（prompt-to-prompt）
- 一致性控制（union controlnet）；视频版控制（引 ch29）
- 代码：ControlNet 推理+训练自定义条件；SVG：ControlNet 结构（zero-conv 图）

## 第 27 章 ch27-t2i-frontier.html 文生图前沿（2023–2026）
- 自回归路线：Parti (2206.10789)、LlamaGen (2406.06525)、VAR (2404.02905) 下一步预测范式
- DALL-E 3 (2310.16825)：重标注数据（synthetic caption）革命→影响 VLM 数据
- Imagen 2/3 (2405.03546?)：Imagen 3 技术报告无 arXiv 写报告名。SD3 (2403.03206)：rectified flow 推导、双/三文本编码器、QK-norm
- Flux.1：引导蒸馏、12B；2025-2026 新一代（GPT-4o 原生生图、Gemini 图像、中文系可灵/HunyuanImage）
- 评测：HPS/ImageReward/GenEval；文字渲染能力竞赛
- 表：2022→2026 文生图模型能力演进表；SVG：三大路线谱系图

## 第 28 章 ch28-personalization.html 个性化与一致性生成
- 目标：特定主体/风格/身份的可控生成
- Textual Inversion (2208.01618) 原理；DreamBooth (2208.12242) class prior loss 推导
- LoRA 训练实战（SD + Flux）；Custom Diffusion；InstantID/IP-Adapter FaceID 身份保持
- 主体一致 vs 风格一致 vs 角色一致性（故事绘本案例）
- 数据：少量样本怎么用；评测（DreamBench DINO 分数）
- 代码：diffusers 训练 DreamBooth-LoRA 完整脚本；表：个性化方法对比；SVG：textual inversion vs LoRA 对比

## 第 29 章 ch29-video-gen.html 视频生成与世界模型
- 视频生成挑战：时序一致性、3D 稀疏性、数据
- Video Diffusion (2212.00799?) → Video Diffusion Models arXiv:2204.03475。 faktorized 空时注意力；AnimateDiff 运动模块
- DiT (2212.09748)：transformer 替代 UNet、scaling；Sora 技术报告解读（ spacetime patch、视频原生）
- 开源视频模型：CogVideoX (2408.06072) 3D VAE、HunyuanVideo、Wan2.x、LTX-Video
- 世界模型视角：Genie (2402.15391)、GameNGen (2408.14837)、Genie-2；Sora 的世界模拟争议
- 评测（VBench）；算力经济学
- 表：视频模型对比；图：DiT/Sora 示意、CogVideoX 原图；SVG：3D VAE 压缩示意

## 第 30 章 ch30-audio.html 语音与音频多模态
- 音频表示：波形/频谱/log-mel；音频 token 化（ENCODEC/SoundStream RVQ）
- Whisper (2212.04356)：弱监督 68 万小时、架构、多任务 token；voice activity
- Speech-LLM：SALMONN (2310.13289)、Qwen-Audio/Qwen2-Audio (2407.10759)、Step-Audio；全双工对话（GPT-4o 模式）
- 音乐/音效生成：MusicGen (2306.05284)（LM over RVQ）、AudioLDM/Stable Audio
- TTS 演进：VALL-E (2301.02111)、CosyVoice；zero-shot 克隆伦理
- 表：音频模型全景；SVG：mel 频谱→encoder→LLM 流程

## 第 31 章 ch31-video-understanding.html 视频理解大模型（核心大章）
- 视频任务谱系：分类→时序定位→时刻检索→长视频 QA→流式
- 视觉骨干：TimeSformer (2102.05095) 分裂注意力、Video Swin (2106.13230)
- 视频 MLLM：Video-LLaMA、Video-LLaVA (2311.10122) 对齐前置、LLaMA-VID (2311.17043) 双 token 压缩、MovieChat
- 长视频：LongVA (2406.16852)、LongContext 扩展、帧采样策略（uniform/keyframe/查询引导）
- 流式与实时：StreamingVideo、时刻级理解；o3/GPT-4o 视频能力
- 数据：视频字幕合成（Panda-70M 等）；评测：Video-MME (2405.21075)、MVBench、TempCompass
- 表：视频 MLLM 对比（帧数/长度/分数）；SVG：帧采样策略对比、token 压缩管线

## 第 32 章 ch32-3d.html 3D 感知与生成
- 3D 表示：点云/体素/mesh/隐式；相机模型与 NeRF (2003.08934) 体渲染推导
- 3D Gaussian Splatting (2308.04079)：原理与训练
- 3D 生成：DreamFusion SDS 推导 (2209.14988)、LRM (2311.04400)、TRELLIS (2412.01506)、单图转 3D 现状
- 3D 与 LLM：3D-LLM、空间推理基准（SpatialVLM 2405.???→不写编号）
- 世界坐标与具身衔接（引 ch33）
- 图：NeRF/3DGS 原图；SVG：体渲染射线示意；表：3D 表示对比

## 第 33 章 ch33-embodied.html 具身智能与 VLA
- 具身定义与挑战；Sim2Real
- RT-1 (2212.06817) 大规模机器人数据；RT-2 (2307.15818) VLM→动作 token（co-fine-tune）
- PaLM-E (2303.03378) 多模态具身 LLM；RT-X/Open X-Embodiment
- OpenVLA (2406.09246)：开源 7B VLA、action tokenization；π0 (2410.24164) flow matching 动作头
- 2025-2026 具身前沿：world model+planning、人形机器人数据、sim 数据（Isaac）
- 评测基准：SIMPLER、CALVIN、LIBERO
- 表：VLA 模型对比；图：RT-2/OpenVLA/π0 原图；SVG：VLA 输入输出流

## 第 34 章 ch34-data-engineering.html 多模态数据工程（核心大章）
- 数据分层：预训练图文（亿级）→SFT 指令（百万）→偏好（十万）
- 大型图文数据集：CC3M/CC12M/SBU、LAION-400M/5B (2210.08402)、DataComp (2304.14108)、COYO
- 清洗管道：NSFW/去重（MinHash）、CLIP-score 过滤、水印检测；DataComp 实验方法论
- 重新标注革命：BLIP captioner、LLaVA 合成、ShareGPT4V、CapsFusion；DALL-E 3 重标注 (2310.16825)
- SFT 数据：LLaVA-Instruct 构造细节、视觉问答自动生成管道、多样性-复杂性策略
- 数据配比与课程：Qwen-VL/InternVL 数据配方；数据飞轮与自举
- 法律与许可：LAION 诉讼、数据合规
- 表：数据集全景（规模/许可/用途）；SVG：数据管道流程图

## 第 35 章 ch35-mm-pretraining.html 多模态预训练实战（核心大章）
- 三阶段范式：模态对齐预训练（投影+冻结 LLM）→端到端 SFT→（可选）偏好对齐
- 阶段 1 深度：数据（LAION 子集+CC）、目标（ITC/ITM/生成混合）、冻结策略消融（LLaVA 论文：只训投影 vs 全解冻）
- 阶段 2：指令数据混合、学习率、epoch；视觉塔微调与否
- 完整代码：从 0 构建迷你 LLaVA（CLIP+TinyLlama+LoRA，含数据加载/训练/推理 ~150 行核心）
- 超参数配方表（batch/lr/warmup/epoch per stage）；显存计算实例
- 训练监控：loss 曲线形态、对齐诊断（检索分数、注意力图）
- 失败模式诊断手册：不学视觉（过拟合文本先验）、幻觉爆炸、分辨率失配
- SVG：三阶段流程图+数据流；box-recipe：可复现配方

## 第 36 章 ch36-peft.html 参数高效微调（LoRA/QLoRA）
- 全参微调的显存数学（权重/梯度/优化器/激活）
- LoRA (2106.09685)：低秩假设、数学推导、梯度公式、初始化 A/B
- 超参数：rank/alpha/dropout/目标模块选择（attention only vs all-linear）
- QLoRA (2305.14314)：4-bit NF4、双重量化、paged optimizer；DoRA (2402.09353)
- 多模态特化：微调视觉塔 vs 投影 vs LLM 的组合策略；视觉 token 压缩辅助
- PEFT 库实战代码（VLM + LoRA 完整例）；保存/合并/多 adapter 服务
- 表：PEFT 方法对比（参数量/显存/性能）；SVG：LoRA 注入示意

## 第 37 章 ch37-mm-alignment.html 多模态对齐与幻觉缓解
- 多模态幻觉定义与分类：对象存在性/属性/关系/计数；语言先验导致的幻觉
- LLaVA-RLHF (2309.14525)：幻觉惩罚 RLHF；RLHF-V (2405.16120)：细粒度人类反馈；RLAIF-V (2405.17220) 自动化
- 多模态 DPO：偏好数据构造（POVID、HA-DPO、CSR）；直接偏好优化在视觉场景的适配
- 解码层缓解：VCD（对比解码）、OPERATE；推理时自我校正
- 评测：POPE (2305.10355)、AMBER、HallusionBench (2310.14566)
- 实战：构造 DPO 偏好数据+训练脚本（TRL DPOTrainer + VLM）
- 表：幻觉缓解方法矩阵；SVG：幻觉成因分解图

## 第 38 章 ch38-distributed-training.html 分布式训练基础设施
- 并行策略：DP→DDP→ZeRO 1/2/3 数学（通信量分析）→FSDP
- 张量并行（Megatron 列/行并行推导）、序列并行、流水线并行（1F1B）
- 多模态特有：视觉塔/LLM 异构并行、图像数据打包、varlen batch
- DeepSpeed 配置精讲（ZeRO-3 + offload）；accelerate 实战
- 显存计算公式大全（参数+优化器+梯度+激活，含公式）；H100 集群训练 7B VLM 实例估算
- 故障排查：loss spike、通信瓶颈（NCCL）、断点续训
- 表：并行策略选型；SVG：ZeRO 分片示意、流水线 1F1B 时序

## 第 39 章 ch39-inference-deployment.html 推理优化与部署
- 推理瓶颈：prefill 算力 vs decode 访存；视觉 token 的 prefill 开销
- 视觉 token 剪枝：FastV (2403.06764)、PyramidDrop、SparseVLM；注意力稀疏
- 量化：GPTQ/AWQ/SmoothQuant 数学与效果表；多模态量化难点（视觉 token 激活离群）
- 引擎：vLLM (2309.06180) 多模态输入、SGLang、TensorRT-LLM；端侧 MLC/llama.cpp/ExecuTorch
- 服务化：批处理、prefix cache（系统提示+图像缓存）、多模态 API 设计
- 实战：OpenAI 兼容多模态服务搭建（vLLM 代码）；端侧 MiniCPM-V 部署
- 表：量化方案×吞吐×质量；SVG：推理服务架构图

## 第 40 章 ch40-benchmarks.html 多模态评测基准全景（核心大章）
- 评测方法论：选择题 vs 开放式；答案提取陷阱；LLM-as-judge 在多模态的偏差
- 通用：MME (2306.13394)、MMBench (2307.06281)、MMStar、SEAL；知识：MMMU (2311.16502)/MMMU-Pro (2409.02813)
- 推理：MathVista (2310.02215)、MathVerse (2403.14624)、MMVet；OCR/文档：OCRBench、DocVQA (2007.00387)、ChartQA (2203.10244)
- 视频：Video-MME (2405.21075)、MVBench、TempCompass；幻觉：POPE/AMBER/HallusionBench
- Agent：OSWorld (2404.07972)、WebVoyager、GUI-World；生成评测：VBench、GenEval、HPS
- Leaderboard 生态与污染问题；动态评测（LiveBench 思想）
- 表：基准全景大表（模态/规模/指标/SOTA）；SVG：评测维度地图

## 第 41 章 ch41-safety-eval.html 幻觉、鲁棒性与安全评测
- 鲁棒性维度：噪声/旋转/遮挡/对抗扰动下的性能退化研究
- 对抗攻击：视觉扰动、typographic attack（贴纸攻击）、图像内嵌恶意指令（indirect prompt injection）
- 越狱：多模态越狱（图像-文本协同）、编码绕过；防御（输入过滤、attention 调整）
- 深度伪造与检测：face swap、AIGC 检测基准；水印（SynthID、不可见水印）
- 隐私：人脸识别泄露、EXIF/GPS、训练数据记忆与抽取
- 红队实践：自动化红队管道代码框架
- 表：攻击×防御矩阵；SVG：多模态威胁模型图

## 第 42 章 ch42-mm-rag.html 多模态 RAG 与文档智能
- 为什么文本 RAG 不够：PDF 版面/图表/扫描件
- 视觉文档检索：ColPali (2407.01449) late-interaction、ColQwen；对比 OCR 管线
- 多模态 embedding：BGE-VL、VLM2Vec (2410.05160)、E5-V；图文检索统一
- 架构：图文混合切块、多向量索引、重排；M3DocRAG、VisRAG
- 长文档：页级/版面级索引；图表理解增强
- 生产实践：增量索引、缓存、成本；评测（ViDoRe）
- 代码：ColPali+Qwen2-VL 端到端文档问答；SVG：多模态 RAG 架构

## 第 43 章 ch43-mm-agents.html 多模态 Agent 与 GUI 操作（核心大章）
- 视觉工具调用：Visual ChatGPT (2303.04671)、HuggingGPT (2303.17580)、ViperGPT (2303.08128)/VisProg (2211.11559) 代码生成式
- GUI Agent：CogAgent (2312.08914) 高分辨率+双重编码、AppAgent、SeeClick、UI-TARS (2501.12326) 原生动作模型
- Computer use 范式：屏幕截图→规划→点击/输入；Set-of-Mark 提示
- 评测：OSWorld (2404.07972)、AndroidWorld、WebArena-Lite；成功率现状
- 多模态 Agent 系统：规划（视觉 CoT）+记忆+工具+反思；多 agent 协作
- 代码：最小 GUI Agent 循环（截图+pyautogui+VLM）；SVG：Agent 循环架构

## 第 44 章 ch44-mm-reasoning.html 多模态推理与视觉思维链
- 视觉推理的特殊性：感知瓶颈 vs 推理瓶颈；visual CoT 数据
- 数学推理：MathVista/MMVet 分析；几何/图表/函数图像推理
- 长思考范式迁移：o3 视觉思维（图像缩放/检索工具使用）、QVQ、视觉 PRM（VisualPRM 2412.?? →写论文名）
- test-time compute 在视觉任务 scaling（更多 token/分辨率/搜索）
- 工具增强推理：代码解释器绘图、SAM 辅助分割再推理、坐标工具
- 训练方法：思维链 SFT、RL（GRPO 视觉版）、过程奖励
- 表：推理基准 SOTA 演进；SVG：visual CoT 流程

## 第 45 章 ch45-aigc-workflow.html AIGC 生产工作流
- ComfyUI 核心概念：节点图/latent 流/model 管理；SDXL/Flux 工作流搭建
- 生产管线：批量生成、 ControlNet 组合、放大（Tile/Upscaler）、修脸
- IP-Adapter/InstantID 工业级角色一致性；电商/设计场景案例
- API 化：ComfyUI API 调用代码、队列、GPU 池化；成本优化（批量化/LCM/蒸馏模型）
- 版权与合规：训练数据争议、商用许可表（SD/Flux/模型许可证对比）
- SVG：ComfyUI 工作流节点图（自绘）；表：模型许可对比

## 第 46 章 ch46-projects.html 端到端项目实战集（核心大章）
- 项目 1：从零训练迷你 LLaVA（数据→预训练→SFT→评测，完整代码+清单）
- 项目 2：企业文档问答（ColPali+Qwen2-VL+重排，含 PDF 处理与评测）
- 项目 3：多模态搜索（CLIP/OpenCLIP 向量库、图文互搜、重排）
- 项目 4：垂直领域 VLM 微调（医疗/工业质检案例：数据构造→LoRA→评测→部署）
- 项目 5：多模态 Agent（视觉工具箱+ReAct，图像编辑助手）
- 每个项目：目标/架构图（SVG）/数据/训练/评估/部署/避坑清单

## 第 47 章 ch47-safety-ethics.html 多模态安全与伦理
- 多模态特有风险：跨模态攻击面更大；名人脸、版权角色
- 内容安全：NSFW 多模态检测、儿童安全；AIGC 标识义务（中国《人工智能生成合成内容标识办法》2025、EU AI Act 透明度条款）
- 深度伪造治理：检测技术（语音/人脸/全图）、溯源标准（C2PA）
- 版权：训练数据合理使用争议（NYT v. OpenAI 类比）、图像风格版权、模型输出侵权
- 隐私技术：人脸模糊、PII 抹除、差分隐私训练
- 对齐与价值观：多模态偏见（性别/种族 in 数据）；红队案例库
- 表：法规×要求对比；SVG：多模态安全分层防御图

## 第 48 章 ch48-frontier-2026.html 2024–2026 前沿与开放问题
- 趋势 1：原生多模态与统一模型成为主流（4o/Chameleon/Gemini 系）
- 趋势 2：推理时计算 scaling 与多模态长思考（o 系列、视觉 RL）
- 趋势 3：视频与 4D、世界模型（Sora/Genie 系）、空间智能（李飞飞）
- 趋势 4：具身智能爆发（VLA、人形机器人）
- 趋势 5：Agent 化（GUI/computer use/多模态工具生态 MCP）
- 趋势 6：效率革命（端侧、token 压缩、小模型逼近大模型）
- 开放问题清单：无限视觉 token、真正跨模态推理、记忆与终身学习、评测失效
- 顶会趋势分析：CVPR/NeurIPS/ICLR/ICML 2024-2026 多模态论文主题统计与热点
- SVG：2026 技术版图

## 第 49 章 ch49-paper-reading.html 论文阅读方法论与文献地图
- 三遍读论文法；如何精读架构图与实验表；复现策略
- 文献管理：Zotero/arXiv API/Connected Papers 代码示例（arxiv api 脚本）
- 按主题的必读论文路线图（10 条主题线，每条 5-8 篇带 arXiv 号）
- 顶会 tracker：CVPR/ICCV/ECCV/NeurIPS/ICML/ICLR/ACL/EMNLP 与多模态相关 track
- 追踪渠道：arXiv sanity、Papers with Code、HuggingFace Daily、X 列表
- 如何写文献综述；SVG：文献地图（10 条主线时间轴）

## 第 50 章 ch50-datasets.html 数据集与基准清单
- 大表格分类：图文预训练（20+）、指令微调（20+）、VQA/推理（25+）、OCR/文档（15+）、视频（15+）、音频（10+）、具身（10+）、生成评测（10+）、幻觉/安全（10+）
- 每条：名称/年份/规模/许可/下载/HF 链接/适用任务
- 使用注意：测试集污染、许可合规
- 合计 ≥150 条目

## 第 51 章 ch51-projects-list.html 开源项目与模型清单
- 分类大表：训练框架（LLaMA-Factory/multipack/swift）、推理引擎、评测工具、数据工具、Agent 框架、AIGC 工具
- 模型库：HF 精选 per 类别（VLM/生成/音频/视频/3D）
- 每条：项目/星数量级/维护方/许可/一句话评价
- 合计 ≥150 条目

## 第 52 章 ch52-glossary.html 术语表
- 300+ 术语，中英对照+一句话定义+相关章节链接
- 按字母序；涵盖：架构/训练/数据/评测/生成/系统 六大类

## 第 53 章 ch53-quiz.html 全书自测题库
- 按十部分组织，每部分 8-12 题（选择/简答/推导/代码题）
- 每题给详细答案要点（含公式）；题目标注对应章节
- 共 ≥100 题

## 第 54 章 ch54-cheatsheet.html 公式与方法速查表
- 核心公式卡片：注意力/RoPE/InfoNCE/SigLIP/DDPM/DDIM/CFG/LDM/LoRA/DPO/GRPO/VQ/体渲染/ZeRO 通信量
- 方法选择决策树（SVG）：微调策略选择/模型选择/融合策略选择
- 超参数速查表；常用 shell/代码片段集
- 速查卡排版：卡片网格
