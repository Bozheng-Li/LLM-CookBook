/* 多模态大模型 Cookbook · 全书目录清单
 * 本文件由所有章节共享，book.js 依据它生成侧边栏与上下章导航。 */
const BOOK = {
  title: "多模态大模型 Cookbook",
  subtitle: "从入门到精通 · 理论 · 实战 · 前沿",
  parts: [
    { name: "第〇部分 · 阅读指南", chapters: [
      { no: "0",  path: "ch00-guide.html", title: "序言、学习路径与全书地图" },
    ]},
    { name: "第一部分 · 基础篇：单模态基石", chapters: [
      { no: "1",  path: "ch01-math-optimization.html", title: "数学基础与优化理论" },
      { no: "2",  path: "ch02-tokenization.html", title: "Tokenization：文本 BPE 与视觉 Token 化" },
      { no: "3",  path: "ch03-transformer.html", title: "Transformer 架构详解" },
      { no: "4",  path: "ch04-flash-attention.html", title: "Flash Attention 与高效注意力" },
      { no: "5",  path: "ch05-cv-basics.html", title: "计算机视觉基础" },
      { no: "6",  path: "ch06-nlp-basics.html", title: "自然语言处理：从 Word2Vec 到 BERT" },
      { no: "7",  path: "ch07-llm-basics.html", title: "大语言模型基础" },
      { no: "8",  path: "ch08-gpu-systems.html", title: "GPU 架构与训练系统" },
    ]},
    { name: "第二部分 · 多模态核心理论", chapters: [
      { no: "9",  path: "ch09-mm-intro.html", title: "多模态学习导论" },
      { no: "10", path: "ch10-mm-representation.html", title: "多模态表示学习" },
      { no: "11", path: "ch11-vlp-classics.html", title: "视觉语言预训练经典模型（2019–2021）" },
      { no: "12", path: "ch12-clip.html", title: "对比学习与 CLIP 深度剖析" },
      { no: "13", path: "ch13-fusion.html", title: "模态融合机制深度解析" },
      { no: "14", path: "ch14-vision-encoders.html", title: "视觉编码器家族" },
      { no: "15", path: "ch15-connectors.html", title: "视觉—语言连接器设计" },
      { no: "16", path: "ch16-visual-instruction-tuning.html", title: "视觉指令微调" },
    ]},
    { name: "第三部分 · 多模态大模型架构全景", chapters: [
      { no: "17", path: "ch17-open-models.html", title: "开源多模态大模型谱系" },
      { no: "18", path: "ch18-closed-models.html", title: "闭源多模态模型剖析" },
      { no: "19", path: "ch19-native-mm.html", title: "原生多模态与早期融合" },
      { no: "20", path: "ch20-unified-models.html", title: "统一理解与生成模型" },
      { no: "21", path: "ch21-grounding.html", title: "细粒度感知与视觉定位" },
      { no: "22", path: "ch22-highres-docs.html", title: "高分辨率与文档图表理解" },
    ]},
    { name: "第四部分 · 文生图与视觉生成", chapters: [
      { no: "23", path: "ch23-generative-basics.html", title: "生成模型基础：VAE 与 GAN" },
      { no: "24", path: "ch24-diffusion.html", title: "扩散模型：从 DDPM 到 Score SDE" },
      { no: "25", path: "ch25-latent-diffusion.html", title: "潜在扩散与 Stable Diffusion" },
      { no: "26", path: "ch26-control-editing.html", title: "条件控制与图像编辑" },
      { no: "27", path: "ch27-t2i-frontier.html", title: "文生图前沿（2023–2026）" },
      { no: "28", path: "ch28-personalization.html", title: "个性化与一致性生成" },
      { no: "29", path: "ch29-video-gen.html", title: "视频生成与世界模型" },
    ]},
    { name: "第五部分 · 音频、视频理解与具身智能", chapters: [
      { no: "30", path: "ch30-audio.html", title: "语音与音频多模态" },
      { no: "31", path: "ch31-video-understanding.html", title: "视频理解大模型" },
      { no: "32", path: "ch32-3d.html", title: "3D 感知与生成" },
      { no: "33", path: "ch33-embodied.html", title: "具身智能与 VLA" },
    ]},
    { name: "第六部分 · 训练与对齐实战", chapters: [
      { no: "34", path: "ch34-data-engineering.html", title: "多模态数据工程" },
      { no: "35", path: "ch35-mm-pretraining.html", title: "多模态预训练实战" },
      { no: "36", path: "ch36-peft.html", title: "参数高效微调（LoRA/QLoRA）" },
      { no: "37", path: "ch37-mm-alignment.html", title: "多模态对齐与幻觉缓解" },
      { no: "38", path: "ch38-distributed-training.html", title: "分布式训练基础设施" },
      { no: "39", path: "ch39-inference-deployment.html", title: "推理优化与部署" },
    ]},
    { name: "第七部分 · 评测与质量", chapters: [
      { no: "40", path: "ch40-benchmarks.html", title: "多模态评测基准全景" },
      { no: "41", path: "ch41-safety-eval.html", title: "幻觉、鲁棒性与安全评测" },
    ]},
    { name: "第八部分 · 多模态应用与 Agent", chapters: [
      { no: "42", path: "ch42-mm-rag.html", title: "多模态 RAG 与文档智能" },
      { no: "43", path: "ch43-mm-agents.html", title: "多模态 Agent 与 GUI 操作" },
      { no: "44", path: "ch44-mm-reasoning.html", title: "多模态推理与视觉思维链" },
      { no: "45", path: "ch45-aigc-workflow.html", title: "AIGC 生产工作流" },
      { no: "46", path: "ch46-projects.html", title: "端到端项目实战集" },
    ]},
    { name: "第九部分 · 安全、伦理与前沿", chapters: [
      { no: "47", path: "ch47-safety-ethics.html", title: "多模态安全与伦理" },
      { no: "48", path: "ch48-frontier-2026.html", title: "2024–2026 前沿与开放问题" },
    ]},
    { name: "第十部分 · 附录", chapters: [
      { no: "49", path: "ch49-paper-reading.html", title: "论文阅读方法论与文献地图" },
      { no: "50", path: "ch50-datasets.html", title: "数据集与基准清单" },
      { no: "51", path: "ch51-projects-list.html", title: "开源项目与模型清单" },
      { no: "52", path: "ch52-glossary.html", title: "术语表" },
      { no: "53", path: "ch53-quiz.html", title: "全书自测题库" },
      { no: "54", path: "ch54-cheatsheet.html", title: "公式与方法速查表" },
    ]},
  ]
};
const BOOK_ID_TO_PART = {};
BOOK.parts.forEach((p, pi) => p.chapters.forEach(c => { BOOK_ID_TO_PART[c.path] = pi; }));
if (typeof module !== "undefined") module.exports = BOOK;
