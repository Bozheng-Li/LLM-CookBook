# 🍳 多模态大模型 Cookbook（Multimodal LLM Cookbook）

> **从入门到精通 · 理论 · 实战 · 前沿** —— 一部面向中文读者的多模态大模型（Multimodal LLM）完整技术手册。
> 55 章 · 550+ 篇论文精读与推荐 · 300+ 代码示例 · 400+ 论文原图与图解 · 1000+ A4 页（打印） · 知识覆盖 2014 → 2026 顶会顶刊。

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](LICENSE)
[![Pages](https://img.shields.io/badge/HTML_book-55_chapters-blue)](index.html)
[![arXiv figures](https://img.shields.io/badge/paper_figures-437_images-orange)](assets/images/papers/)
[![中文](https://img.shields.io/badge/语言-中文_(术语双语)-red)](index.html)

## ✨ 本书特色

- **七层深度结构**：每一章都按「直觉 → 数学推导 → 架构图解 → 可运行代码 → 实验数据 → 实践配方 → 自测题」组织，深度对标专业参考书（关键算法给出不跳步的完整推导）。
- **图文并茂、离线可读**：437 张论文原图（ar5iv 官方渲染，含出处标注）+ 大量自绘 SVG 架构图，全部本地化，克隆即可离线阅读。
- **知识全覆盖**：视觉语言模型（CLIP/BLIP-2/LLaVA/Qwen-VL/InternVL…）、文生图与扩散模型（DDPM→SD3/Flux）、视频、音频、3D、具身智能（VLA）、多模态 Agent 与 RAG、评测与安全，直至 2026 年前沿（原生多模态、test-time compute、世界模型）。
- **完整学习路径**：四阶段路线图 + 三种阅读路线（研究者 / 工程师 / 速查）+ 全书知识依赖图。
- **即拿即用**：所有代码基于真实 API（transformers / OpenCLIP / diffusers / TRL / vLLM / lmms-eval），附超参数配方与踩坑指南。
- **互动 HTML**：内置全文搜索、暗色模式、数学公式（MathJax）、移动端适配；支持一键打印成 1000+ 页 PDF。

## 🗺 内容结构（十大部分 · 55 章）

| 部分 | 章节 | 主题 |
|---|---|---|
| 第〇部分 | 第 0 章 | 序言、学习路径与全书地图 |
| 一、单模态基石 | 第 1–8 章 | 数学与优化 · Tokenization · Transformer · Flash Attention · CV · NLP · LLM · GPU 系统 |
| 二、多模态核心理论 | 第 9–16 章 | 导论 · 表示学习 · VLP 经典 · **CLIP 精读** · 融合机制 · 视觉编码器 · 连接器 · 视觉指令微调 |
| 三、架构全景 | 第 17–22 章 | 开源/闭源 MLLM 谱系 · 原生多模态 · 统一模型 · Grounding · 高分辨率与文档理解 |
| 四、视觉生成 | 第 23–29 章 | VAE/GAN · 扩散模型 · Stable Diffusion · ControlNet · 文生图前沿 · 个性化 · 视频生成 |
| 五、更多模态 | 第 30–33 章 | 语音音频 · 视频理解 · 3D 感知 · 具身智能与 VLA |
| 六、训练实战 | 第 34–39 章 | 数据工程 · 预训练实战 · LoRA/QLoRA · 对齐与幻觉 · 分布式训练 · 推理部署 |
| 七、评测质量 | 第 40–41 章 | 基准全景 · 幻觉与安全评测 |
| 八、应用实战 | 第 42–46 章 | 多模态 RAG · GUI Agent · 多模态推理 · AIGC 工作流 · 端到端项目集 |
| 九、前沿视野 | 第 47–48 章 | 安全与伦理 · 2024–2026 前沿与开放问题 |
| 十、附录 | 第 49–54 章 | 论文阅读方法论 · 数据集清单 · 项目清单 · 术语表 · 自测题库 · 公式速查 |

## 🚀 如何阅读

1. **在线/本地阅读**：克隆仓库后直接用浏览器打开 [`index.html`](index.html)（无需任何构建步骤，全部静态文件）。

   ```bash
   git clone https://github.com/<your-username>/multimodal-cookbook.git
   cd multimodal-cookbook
   # 用浏览器打开 index.html 即可
   ```

2. **导出 PDF**：浏览器打开 `print.html`（全书合集页）→ 打印 → 保存为 PDF（建议启用背景图形）。或使用 Chrome 无头模式：

   ```bash
   chrome --headless --print-to-pdf=cookbook.pdf --no-pdf-header-footer print.html
   ```

3. **推荐起点**：零基础从 [第 0 章（学习路径）](chapters/ch00-guide.html) 开始；有 LLM 基础的读者可直接进入 [第 12 章（CLIP 精读）](chapters/ch12-clip.html) 与 [第 15 章（连接器设计）](chapters/ch15-connectors.html)。

## 🔧 环境准备（代码示例运行）

```bash
conda create -n mmcook python=3.11 -y && conda activate mmcook
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install transformers accelerate peft trl datasets open_clip_torch diffusers vllm
```

硬件建议与版本细节见 [第 0 章 · 环境准备](chapters/ch00-guide.html)。

## 📖 论文图片版权说明

全书论文插图通过 [ar5iv](https://ar5iv.labs.arxiv.org)（arXiv 官方 HTML 渲染服务）获取并标注出处，仅用于学术研究与教学用途；各图片版权归原论文作者所有，商用请遵循对应论文许可。

## 🤝 参与贡献

发现错误、过时结论或失效链接请提 Issue；贡献新章节前请阅读 [`STYLE-GUIDE.md`](STYLE-GUIDE.md)（写作规范）与 [`CHAPTER-OUTLINES.md`](CHAPTER-OUTLINES.md)（章节知识基准），保持结构与深度一致。所有章节均经过多维度独立评审（内容精确度 / 语言风格 / 图文样式 / 阅读体验 / 图示质量）后收录。

## 📄 许可

- 文字与插图编排：[CC BY-SA 4.0](LICENSE)
- 引用的论文图片与代码片段版权归各自作者，引用处均已标注来源。

---
*当前版本知识截止 2026-09 · 每季度滚动修订前沿章节 · Built with ❤️ for the multimodal community*
