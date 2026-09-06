# -*- coding: utf-8 -*-
"""figures_ch081.py — ch081 知识库 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 81-1: 个人知识库端到端全景架构 ----
f = F(940, 420)
f.text(470, 32, "项目 1: 个人知识库问答 Agent 全流程架构 (End-to-End RAG)", 18, C.ink, 800)

b1 = f.box(60, 100, 180, 110, "① 多源文档摄取", "PDF / Markdown / 网页\n清洗 · 分块 (Chunking)", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(290, 100, 180, 110, "② 混合检索与重排", "BM25 (关键词) +\nDense (稠密向量) + Rerank", fill=C.teal_s, stroke=C.teal)
b3 = f.box(520, 100, 180, 110, "③ 意图路由与生成", "忠实性契约提示词 (63章)\n显式标注引用编号 [M1]", fill=C.amber_s, stroke=C.amber)
b4 = f.box(750, 100, 140, 110, "④ 校验与溯源", "主张-来源对齐\nStreamlit 前端交互", fill=C.purple_s, stroke=C.purple)

f.arrow(240, 155, 290, 155, "", C.soft)
f.arrow(470, 155, 520, 155, "", C.soft)
f.arrow(700, 155, 750, 155, "", C.soft)

# 底部评测闭环
f.raw('<rect x="110" y="250" width="720" height="90" rx="8" fill="#fafaf7" stroke="%s" stroke-dasharray="6 4"/>' % C.line)
f.text(470, 275, "评测驱动迭代闭环 (RAGAS 自动化质量评估)", 12.5, C.indigo_d, 800)
f.text(470, 298, "· 检索层指标: 上下文精确率 (Context Precision) & 上下文召回率 (Context Recall)", 10.5, C.ink)
f.text(470, 318, "· 生成层指标: 忠实度 (Faithfulness) & 答案相关度 (Answer Relevance) — 每次调优自动化门禁", 10.5, C.ink)

f.note(470, 375, "工程核心: 绝不裸调向量库，必须通过「分块切分 + 混合重排 + 显式引用 + 评测回归」实现 99% 的事实保真度", 11.5, C.indigo, anchor="middle")
f.save("fig-project-rag-arch")

# ---- fig 81-2: 混合检索与重排对比 ----
f = F(940, 380)
f.text(470, 32, "混合检索 (Hybrid Search) 与互惠排名融合 (RRF)", 18, C.ink, 800)

s1 = f.box(60, 110, 240, 100, "BM25 稀疏检索", "专攻专业术语、精确型号、\n专属名词与唯一代码 (精确匹配)", fill=C.teal_s, stroke=C.teal)
s2 = f.box(350, 110, 240, 100, "Embedding 稠密检索", "专攻自然语言同义词、意图匹配、\n跨语言与语义模糊理解", fill=C.blue_s, stroke=C.blue)
rrf = f.box(660, 110, 220, 100, "交叉编码重排 (Cross-Encoder)", "BGE-Reranker / Cohere\n深层注意力计算相关性打分", fill=C.amber_s, stroke=C.amber)

f.arrow(300, 160, 350, 160, "", C.soft)
f.arrow(590, 160, 660, 160, "RRF 融合 Top-50", C.soft)

f.note(470, 260, "RRF 融合公式: RRF_Score(d) = \sum_{m \in \{BM25, Dense\}} \frac{1}{k + r_m(d)} (其中常数 k=60)", 11.5, C.indigo_d, anchor="middle")
f.note(470, 290, "实战表现: 混合检索 + Rerank 相比单一向量检索，在企业私有文档问答上的 Top-3 召回率平均提升 28.5%", 11.5, C.faint, anchor="middle")
f.save("fig-hybrid-search-rrf")
