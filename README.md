# 大模型技术 Cookbook

> 一份从数学基础、Transformer、预训练、后训练，到推理、Agent、LLMOps、评测与治理的系统化中文学习手册。

[![在线阅读](https://img.shields.io/badge/在线阅读-GitHub%20Pages-2ea44f?style=flat-square)](https://bozheng-li.github.io/LLM-CookBook/)
[![GitHub stars](https://img.shields.io/github/stars/Bozheng-Li/LLM-CookBook?style=flat-square)](https://github.com/Bozheng-Li/LLM-CookBook/stargazers)
[![License](https://img.shields.io/badge/site-static-1f6feb?style=flat-square)](https://github.com/Bozheng-Li/LLM-CookBook)

## 先打开阅读端

### 在线阅读

**[打开大模型技术 Cookbook](https://bozheng-li.github.io/LLM-CookBook/)**

这是推荐入口。站点支持章节导航、站内搜索、难度筛选、阅读进度、深色模式、公式渲染、原生 HTML 思维图与流程图、Mermaid 专项图表和代码高亮。所有浏览器运行时和图片资源均随仓库提供，正文页面不依赖 CDN 或后端服务。

> 首次启用提示：仓库管理员需要在 GitHub 的 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。完成一次后，后续推送 `main` 会自动更新阅读端。

### 本地阅读

```bash
git clone https://github.com/Bozheng-Li/LLM-CookBook.git
cd LLM-CookBook
python -m http.server 8000
```

然后访问 <http://localhost:8000/>。如果 8000 端口被占用，可以换成任意本地端口。

## 这份手册适合谁

- 想建立大模型完整知识地图的开发者和技术管理者
- 想从公式、代码和系统约束理解 Transformer 的算法工程师
- 想实践微调、RAG、Agent、推理部署和评测的应用开发者
- 想快速定位论文、官方文档和课程资料的研究学习者

内容采用“直觉解释 → 关键公式 → 工程实现 → 失败模式 → 延伸资料”的组织方式。每个页面末尾都提供高亮的深化资料卡；篇章级主题另外给出学习目标、先修关系、最小实验、失败注入和量化验收标准，避免只停留在术语解释。

## 章节地图

| 阶段 | 章节 | 主要问题 |
| --- | --- | --- |
| 基础 | [00 导论全景](pages/00-overview/index.html)、[01 数学与神经网络基础](pages/01-foundations/index.html)、[02 序列建模与表示](pages/02-representation/index.html) | 模型在预测什么？文本如何变成向量？梯度如何更新？ |
| 架构 | [03 Transformer 核心](pages/03-transformer/index.html)、[04 现代架构演进](pages/04-modern-arch/index.html) | 注意力、位置编码、MoE、长上下文和多模态如何工作？ |
| 训练 | [05 GPU 与算子系统](pages/05-systems/index.html)、[06 预训练](pages/06-pretraining/index.html)、[07 后训练与对齐](pages/07-posttraining/index.html) | 如何把模型训练出来，并让它遵循指令？ |
| 推理与应用 | [08 推理与推理时扩展](pages/08-inference/index.html)、[09 效率与部署](pages/09-efficiency/index.html)、[10 应用系统](pages/10-applications/index.html) | 如何以可控成本生成、检索和服务化？ |
| 生产与治理 | [11 Agents](pages/11-agents/index.html)、[12 LLMOps](pages/12-llmops/index.html)、[13 评测](pages/13-evaluation/index.html)、[14 治理](pages/14-governance/index.html) | 如何让系统可用、可测、可追责？ |
| 动手实践 | [15 实战](pages/15-practice/index.html) | 从零实现 tokenizer、miniGPT、FlashAttention、RAG、Agent 与全栈大模型应用。 |

## 推荐阅读路线

### 快速建立全局认知

[什么是大模型](pages/00-overview/what-is-llm.html) → [Transformer 完整架构](pages/03-transformer/architecture.html) → [预训练目标](pages/06-pretraining/objectives.html) → [推理引擎](pages/09-efficiency/inference-engines.html)

### 算法工程路线

[线性代数](pages/01-foundations/linear-algebra.html) → [注意力机制](pages/03-transformer/attention.html) → [Scaling Laws](pages/06-pretraining/scaling-laws.html) → [分布式训练](pages/06-pretraining/distributed-training.html) → [量化与模型压缩](pages/09-efficiency/quantization.html)

### 应用开发路线

[Prompt 工程](pages/10-applications/prompt-engineering.html) → [RAG](pages/10-applications/rag.html) → [结构化输出](pages/10-applications/structured-output.html) → [全栈大模型应用](pages/15-practice/fullstack-llm-app.html) → [生产观测](pages/12-llmops/observability.html)

### 研究与前沿路线

[注意力变体](pages/04-modern-arch/attention-variants.html) → [MoE](pages/04-modern-arch/moe.html) → [推理模型](pages/08-inference/reasoning-models.html) → [验证器与过程奖励](pages/08-inference/verifier-prm.html) → [可解释性](pages/13-evaluation/interpretability.html)

## 内容特色

- **系统化**：从数学、表示、架构、训练到生产治理，按依赖关系组织，而不是按热点堆叠术语。
- **可验证**：关键结论尽量回到原始论文、官方文档、大学课程和公共机构材料。
- **工程化**：显存、带宽、延迟、评测、失败模式和成本约束都会落到具体决策上。
- **教材化**：页面级学习契约把知识点转成可复现实验、指标记录和通过/回退条件，适合自学、带教和代码评审。
- **图表可读**：概念思维图和流程图使用原生 HTML，适配移动端、暗色与打印；时序图、状态图等专项语义图保留离线 Mermaid 渲染。
- **可运行**：实战章节提供 Python、PyTorch、Triton、RAG、Agent，以及 FastAPI + React 全栈参考项目。
- **持续更新**：前沿内容会标注时效性，引用资料记录检索日期和来源类型。

## 项目结构

```text
.
├── index.html                 # 站点首页与学习入口
├── references.html            # 独立的论文、教程与规范资源中心
├── glossary.html              # 全站术语表
├── dependency.html            # 知识依赖图
├── pages/                     # 00–15 章节与主题页
├── assets/css/theme.css       # 主题、布局和资料卡样式
├── assets/js/nav.js           # 导航、搜索、进度和页面行为
├── assets/js/toc.js           # 章节目录数据
├── assets/js/resources.js     # 权威延伸资料与中文摘要
├── assets/figures/            # 本地论文插图与教学图
├── assets/vendor/             # 离线公式、流程图、图表和代码高亮运行时
├── examples/                  # 可运行的配套代码（见下表）
└── .github/workflows/pages.yml# GitHub Pages 自动部署
```

## 可运行示例

第 15 章的每个实战页面都配了一份可以直接跑的代码，都带自检测试，都能离线运行。

| 目录 | 依赖 | 自检 | 对应章节 |
| --- | --- | --- | --- |
| `examples/build-tokenizer/` | 无（仅标准库） | 9 项 | 手写 BPE Tokenizer |
| `examples/build-minigpt/` | PyTorch | 11 项 | 从零实现 miniGPT |
| `examples/build-flashattention/` | PyTorch | 10 项 | 手写 FlashAttention |
| `examples/rag-practice/` | 无（仅标准库） | 21 项 | 搭建一个 RAG 系统 |
| `examples/fullstack-llm/` | FastAPI + React | pytest | 全栈 LLM 应用 |

每个目录下的 `README.md` 记录了实测数据和可复现的结论，而不只是使用说明。
自带数据，首次运行不需要网络，也不需要 API 密钥。

## 资料与引用标准

资料优先级为：原始论文和 DOI/arXiv，其次是 PyTorch、Hugging Face、NVIDIA 等官方文档，再次是大学课程、公开讲座和 NIST、OECD、UNESCO 等公共机构材料。页面中的延伸资料不是广告推荐，而是用于解释正文、核对事实和继续学习的入口。

## 贡献方式

欢迎通过 Issue 或 Pull Request 提交内容修正、失效链接、公式错误和新的权威资料。新增资料请尽量附上：作者或机构、发布日期、稳定链接、中文摘要，以及它解决了当前页面中的哪个具体问题。

阅读站点是纯静态 HTML，不需要数据库、构建服务或 API 密钥。`examples/` 中的参考项目是独立教学资源，不参与 GitHub Pages 构建；修改正文 HTML、CSS 或 JavaScript 后，推送到 `main` 分支即可由 GitHub Actions 自动发布。

## 运行状态

在线站点：<https://bozheng-li.github.io/LLM-CookBook/>  
代码仓库：<https://github.com/Bozheng-Li/LLM-CookBook>
