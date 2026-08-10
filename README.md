# 大模型技术 Cookbook

> 从数学基础到 Transformer、训练、推理、Agent 与 LLMOps 的系统化中文知识手册。

[![Online Reading](https://img.shields.io/badge/在线阅读-GitHub%20Pages-185FA5?style=for-the-badge)](https://bozheng-li.github.io/LLM-CookBook/)
[![Static Site](https://img.shields.io/badge/站点-纯静态%20HTML%2FCSS%2FJS-2E7D32?style=for-the-badge)](https://github.com/Bozheng-Li/LLM-CookBook)
[![License](https://img.shields.io/badge/license-MIT-6B4FBB?style=for-the-badge)](LICENSE)

一个面向学习、面试和工程实践的 LLM 知识库。它不把大模型技术写成名词清单，而是沿着“直觉 → 公式 → 代码 → 系统设计 → 评测与排障”的路径，把每个关键概念拆成可以继续追问、验证和落地的知识单元。

## 你会在这里学到什么

- **基础与架构**：线性代数、概率信息论、Tokenization、Embedding、Transformer、Attention、位置编码、MoE 与多模态。
- **训练与对齐**：预训练目标、数据工程、Scaling Laws、分布式训练、混合精度、SFT、LoRA、RLHF、DPO、GRPO 与安全对齐。
- **推理与效率**：解码策略、推理时扩展、KV Cache、量化、蒸馏、投机解码、推理引擎、Batching 与服务成本。
- **应用与智能体**：Prompt、Context Engineering、RAG、Agent、工具调用、MCP、结构化输出、记忆和多智能体。
- **工程化与治理**：LLMOps、可观测性、Prompt 评测 CI、成本工程、基准评测、幻觉、安全红队、治理与合规。
- **面试与实战**：显存账本、通信账本、复杂度分析、系统设计题、标准回答、追问、常见误区和故障排查清单。

## 项目规模

| 指标 | 当前规模 |
| --- | ---: |
| 知识篇章 | 16 |
| 知识点页面 | 98 |
| 学习阶段 | 7 |
| 难度分级 | 入门 / 进阶 / 高级 |
| 站点形式 | 纯静态 HTML / CSS / JavaScript |
| 公式与图表 | KaTeX、Mermaid、Highlight.js、Chart.js |
| 内容验收 | `tools/check.py` 全站 98 / 98 达标 |
| 渲染风险扫描 | `tools/check_rendering.py` 全站 98 / 98 无风险 |

## 在线阅读

- **主站**：<https://bozheng-li.github.io/LLM-CookBook/>
- **仓库**：<https://github.com/Bozheng-Li/LLM-CookBook>
- **首页入口**：[`index.html`](index.html)
- **术语表**：[`glossary.html`](glossary.html)
- **知识依赖图**：[`dependency.html`](dependency.html)

如果 Pages 尚未完成首次构建，也可以直接打开仓库中的 `index.html`，或按下面的方式在本地启动静态服务器。

## 七阶段知识地图

1. **导论全景**：认识大模型、发展时间线、模型家族和学习路线。
2. **数学与神经网络基础**：补齐读论文、读代码所需的最小数学工具。
3. **序列建模与表示**：理解语言模型、词元化、嵌入和 Transformer 前史。
4. **Transformer 与现代架构**：从 Attention、位置编码到 MoE、长上下文和多模态。
5. **训练、后训练与对齐**：覆盖数据、优化、分布式训练、SFT、偏好优化和 RLVR。
6. **推理、应用与工程治理**：把模型变成可用、可评测、可观测、可控成本的产品。
7. **实战菜谱**：通过完整案例把知识串成工程流程。

## 推荐学习路径

### 应用开发者

`00 导论全景` → `02 序列与表示` → `10 应用范式` → `11 Agent 智能体` → `12 LLMOps`

重点关注 Prompt、RAG、结构化输出、工具调用、评测、可观测性和成本治理。

### 大模型算法工程师

`01 数学基础` → `03 Transformer` → `04 现代架构` → `05 GPU 与算子` → `06 预训练` → `07 后训练` → `08 推理扩展` → `09 效率部署`

重点关注 Attention 复杂度与显存、分布式并行、优化器、训练稳定性、DPO/GRPO、KV Cache、量化和推理服务。

### 提示与上下文工程

`00 学习路径` → `10 Prompt / Context / RAG` → `11 Agent` → `13 评估` → `12 LLMOps`

重点关注任务分解、检索误差分解、轨迹评估、Prompt 版本化和发布门禁。

### 研究者

按全站顺序阅读，并优先打开带“前沿”标记的篇章，再回看对应的基础页面和参考文献。

## 快速开始

### 直接在线阅读

打开 <https://bozheng-li.github.io/LLM-CookBook/> 即可。页面支持：

- 全站关键词搜索，快捷键 `/` 聚焦搜索框；
- 入门、进阶、高级难度筛选；
- 浅色 / 暗色主题切换；
- 阅读进度记录；
- 页面目录、前后页导航和术语反链；
- Mermaid 图、KaTeX 公式、代码高亮和 Chart.js 图表。

### 本地启动

本项目没有后端依赖，推荐使用静态服务器，避免浏览器对本地文件路径和脚本的限制：

```bash
python -m http.server 8765 --directory .
```

然后访问 <http://127.0.0.1:8765/>。

Windows 下也可以使用项目提供的 Python 运行时，或使用任意静态文件服务器：

```bash
npx serve .
```

### 内容质量检查

```bash
python tools/check.py all
python tools/check_rendering.py all
```

`check.py` 检查正文、Mermaid 图、表格、代码块、深入阅读块和外链；`check_rendering.py` 检查公式分隔符、Mermaid 首行、图片路径、Canvas 和渲染脚本结构。

## 目录结构

```text
.
├── index.html                  # Cookbook 首页
├── glossary.html               # 全站术语表
├── dependency.html             # 知识依赖图
├── pages/                      # 16 篇、98 个知识点页面
├── assets/
│   ├── css/theme.css           # 统一主题与响应式排版
│   ├── js/                     # 导航、搜索、目录和渲染逻辑
│   ├── img/                    # 公共图片
│   └── figures/                # 论文图与章节插图
├── tools/
│   ├── toc.json                # 目录单一数据源
│   ├── generate.py             # 站点辅助生成器
│   ├── check.py                # 内容质量验收
│   ├── check_rendering.py      # 静态渲染风险扫描
│   └── WRITING-GUIDE.md        # 页面写作规范
├── .github/workflows/          # GitHub Pages 自动发布
├── CONTRIBUTING.md             # 贡献指南
├── CHANGELOG.md                # 版本记录
└── LICENSE                    # MIT 许可证
```

备份目录、缓存、工作区记忆、临时 HTML 和本地截图验收产物不会进入 Git 提交，详见 [`.gitignore`](.gitignore)。

## 内容原则

- **先讲问题，再讲机制**：每节尽量回答“为什么需要它、怎么工作、什么时候会失败”。
- **公式和代码相互验证**：重要结论同时给出公式、形状、复杂度或伪代码。
- **工程账本优先**：显存、通信、延迟、吞吐、成本和可靠性尽量给出可计算的账本。
- **区分事实与判断**：快速演进的前沿内容会标注不确定性，外部来源建议在重要场景二次核验。
- **不编造引用**：论文、官方文档、数字和 URL 以页面中的真实来源为准。

## 贡献方式

欢迎提交：

- 事实纠错、死链修复和引用更新；
- 公式、代码、图表或系统设计的改进；
- 新的面试追问、排障清单和实战案例；
- 排版、无障碍、响应式和浏览体验改进。

提交前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，并确保新增或修改页面保留 `<!-- cookbook:handcrafted -->` 标记、使用相对链接、通过质量检查。

## 许可证与引用

本项目代码、排版和原创文字以 [MIT License](LICENSE) 发布。页面中的论文图、公共素材和第三方引用仍以各自来源声明为准，使用前请遵守原始许可证。

如果本 Cookbook 对你的学习或项目有帮助，欢迎 Star、提出 Issue，或提交一个小而清晰的 Pull Request。

---

> 本项目由 AI 辅助整理与持续维护。大模型技术变化很快，重要技术选型、生产配置和安全决策请结合官方文档与实际实验二次核验。
