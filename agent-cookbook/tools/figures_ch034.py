# -*- coding: utf-8 -*-
"""figures_ch034.py — ch034 LlamaIndex 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 440)
f.text(480, 30, "LlamaIndex 的世界观:数据连接器 → 索引 → 查询引擎 → Agent", 16.5, C.ink, 800)

# 第一行: 数据源
sources = [("PDF/HTML", 60), ("数据库", 200), ("API", 340), ("Notion/Slack", 480), ("代码仓库", 640)]
for name, x in sources:
    f.box(x, 70, 110, 40, name, fill=C.gray_s, stroke=C.line, tc=C.soft, fs=11.5)
# 连接器
f.box(280, 140, 380, 44, "Data Connectors(LlamaHub: 数百种现成连接器)",
      fill=C.blue_s, stroke=C.blue, tc=C.blue_d, fs=12)
for name, x in sources:
    f.elbow([(x + 55, 110), (x + 55, 125), (400, 125), (400, 136)], color=C.faint, sw=1.1)

# 第二行: 索引
idx = [("向量索引", C.indigo), ("摘要索引", C.teal), ("知识图谱", C.purple), ("树索引", C.amber)]
ix = []
for i, (name, colr) in enumerate(idx):
    softmap = {C.indigo: C.indigo_s, C.teal: C.teal_s, C.purple: C.purple_s, C.amber: C.amber_s}
    b = f.box(70 + i * 215, 215, 180, 44, name + " Index", fill=softmap[colr], stroke=colr, tc=colr, fs=12)
    ix.append(b)
    f.elbow([(470, 184), (470, 200), (b["cx"], 200), (b["cx"], b["top"][1])], color=C.faint, sw=1.1)

# 第三行: 查询引擎 / Agent
qe = f.box(150, 300, 260, 50, "Query Engine 查询引擎", "检索 + 合成的一次性问答",
           fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12)
ag = f.box(540, 300, 260, 50, "Agent", "把 Query Engine 当工具的多步循环",
           fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12)
for b in ix:
    f.elbow([(b["cx"], b["bottom"][1]), (b["cx"], 285), (280, 285), (280, 296)],
            color=C.faint, sw=1.0)
f.elbow([(b["cx"] if False else 160, 285), (670, 285), (670, 296)], color=C.faint, sw=1.0)
f.note(480, 390, "分层选择: 简单问答用 Query Engine; 多步推理/跨源才升 Agent", 12, C.soft, 600)
f.note(480, 420, "一切检索形态(向量/摘要/图/树)都是统一 Index 抽象的实现 —— 换索引不改代码", 12, C.faint)
f.save("fig-llamaindex-world")
print("done")
