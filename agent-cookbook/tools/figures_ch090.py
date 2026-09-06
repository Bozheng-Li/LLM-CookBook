# -*- coding: utf-8 -*-
"""figures_ch090.py — ch090 全知科研助理与文献挖掘 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 90-1: 学术文献全生命周期挖掘与综述 Agent 全景流水线
f = F(940, 420)
f.box(40, 60, 160, 110, "1. 多源文献检索\narXiv / Semantic\nOpenAlex / Google\n双向引用滚雪球 (Snowball)", fill=C.blue_s, stroke=C.blue)
f.box(240, 60, 170, 110, "2. 跨模态深层解析\nNougat / MinerU\n复杂公式 LaTeX 提取\n表格数据结构化转录", fill=C.indigo_s, stroke=C.indigo)
f.box(450, 60, 180, 110, "3. 学术引文图谱\nCitation Graph\nPageRank 奠基之作识别\n演进脉络聚类 (Clustering)", fill=C.amber_s, stroke=C.amber)
f.box(670, 60, 230, 110, "4. 综述与前沿假设生成\nLiterature Review & Hypothesis\n万字文献综述 (Review)\n待攻克 Open Problem 挖掘", fill=C.teal_s, stroke=C.teal)

f.arrow(200, 115, 240, 115, "PDF / BibTeX")
f.arrow(410, 115, 450, 115, "结构化 Markdown")
f.arrow(630, 115, 670, 115, "引文拓扑图")

# 底部假设验证自愈环
f.elbow([(785, 170), (785, 240), (540, 240), (540, 170)], label="生成假设缺乏实证支持或存在既有反例: 触发定向论文反向溯源", color=C.red, label_pos=1)

# 底部学术基座基础设施
f.box(100, 290, 740, 100, "科研级基础设施与严谨性护栏 (Scientific Infrastructure & Rigor)\n• 权威引文解析: 严格校验 DOI、arXiv ID、发表年份与顶会级别 (CCF/CORE 评级)\n• 零幻觉引文阻断 (Zero Hallucinated Citations): 严禁凭空捏造不存在的论文与作者姓名\n• 跨学科概念对齐: 统一数学符号与公式定义，消解不同流派命名歧义", fill=C.purple_s, stroke=C.purple)

f.save("fig-scholar-agent-arch")

# fig 90-2: 双向引用滚雪球与知识演化树
f = F(940, 360)
f.box(60, 120, 170, 120, "经典开山之作\n(Seed Paper)\n例如: Vaswani 2017\n'Attention Is All You Need'\n奠定 Transformer 范式", fill=C.blue_s, stroke=C.blue)

f.box(300, 50, 180, 100, "前向引文追踪 (Forward)\n谁引用了它？\nBERT, GPT-1, T5\n架构分支分化", fill=C.indigo_s, stroke=C.indigo)

f.box(300, 210, 180, 100, "后向参考文献 (Backward)\n它参考了谁？\nSeq2Seq, Bahdanau Attention\n思想源头溯源", fill=C.amber_s, stroke=C.amber)

f.box(560, 120, 180, 120, "图拓扑社群聚类\nCommunity Detection\n识别出三大学派:\n1. 缩放定律 (Scaling Law)\n2. 稀疏注意力 (Sparse)\n3. 具身智能 (Embodied)", fill=C.purple_s, stroke=C.purple)

f.box(800, 120, 110, 120, "产出综述\nSurvey Report\n& 趋势研判", fill=C.green_s, stroke=C.green)

f.arrow(230, 160, 300, 100, "被引")
f.arrow(230, 200, 300, 260, "引证")
f.arrow(480, 100, 560, 160)
f.arrow(480, 260, 560, 200)
f.arrow(740, 180, 800, 180)

f.save("fig-citation-snowball-tree")
print("ch090 figures generated successfully")
