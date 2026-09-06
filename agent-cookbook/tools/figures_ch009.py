# -*- coding: utf-8 -*-
"""figures_ch009.py — 第 9 章插图: 能力边界与为什么需要 Agent"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 9-2 四堵墙与四根支柱 (新画) --------------------------------------
f = F(960, 430)
f.text(480, 32, "为什么需要 Agent：四堵墙与四根支柱", 18, C.ink, 800)
f.text(480, 56, "裸 LLM 的每一条边界，恰好对应 Agent 架构要补上的一种机制", 12.5, C.faint)

walls = [
    ("知识截止", "训练数据之后的世界一无所知", C.red, C.red_s, C.red_d),
    ("幻觉与过度自信", "流畅优先于真实，置信度失真", C.red, C.red_s, C.red_d),
    ("无状态", "每次调用从零开始，没有记忆", C.amber, C.amber_s, C.amber_d),
    ("无行动能力", "只会生成文本，不能感知与执行", C.amber, C.amber_s, C.amber_d),
]
pillars = [
    ("检索接地（RAG / 搜索）", "把时效事实注入上下文再作答", C.teal, C.teal_s, C.teal_d),
    ("工具调用 + 结果校验", "计算器、代码执行、API 交叉核实", C.teal, C.teal_s, C.teal_d),
    ("记忆系统", "短期上下文 + 长期持久化存储", C.indigo, C.indigo_s, C.indigo_d),
    ("规划 - 执行 - 反思", "任务分解、中间结果验证、重试", C.indigo, C.indigo_s, C.indigo_d),
]
f.group(40, 78, 340, 282, "裸 LLM 的四堵墙", fill="#ffffff", stroke=C.line, label_fill=C.soft)
f.group(580, 78, 340, 282, "Agent 的四根支柱", fill="#ffffff", stroke=C.line, label_fill=C.soft)
for i, ((wt, ws, wc, wfs, wtd), (pt, ps, pc, pfs, ptd)) in enumerate(zip(walls, pillars)):
    y = 116 + i * 60
    f.box(62, y, 296, 50, wt, ws, fill=wfs, stroke=wc, tc=wtd, fs=13, sub_fs=10.5)
    f.box(602, y, 296, 50, pt, ps, fill=pfs, stroke=pc, tc=ptd, fs=13, sub_fs=10.5)
    f.arrow(362, y + 25, 596, y + 25, color=C.faint, sw=1.6, dash="5 4")
f.note(480, 392, "Agent 不是让概率大脑变得更聪明，而是给它接上外部世界与纠错回路 —— 能力边界决定系统架构",
       12.5, C.soft, anchor="middle")
f.save("fig-why-agent")
