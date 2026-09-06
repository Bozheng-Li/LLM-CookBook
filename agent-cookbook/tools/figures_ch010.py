# -*- coding: utf-8 -*-
"""figures_ch010.py — 第 10 章插图: ANN 索引原理对比"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 10-2 三种 ANN 索引: 暴力 / 分桶 / 分层图 (新画) -------------------
f = F(960, 430)
f.text(480, 32, "ANN 三种索引：暴力、分桶与分层图", 18, C.ink, 800)
f.text(480, 56, "在百万级向量里找 q 的最近邻 —— 三种索引代表三种「剪枝」思路", 12.5, C.faint)

# ============ 面板一: Flat 暴力检索 ============
x0 = 50
f.group(x0, 80, 280, 236, "Flat 暴力检索", fill="#ffffff", stroke=C.line, label_fill=C.soft)
pts_flat = [(95, 142), (130, 115), (175, 150), (215, 120), (255, 145),
            (105, 188), (150, 202), (195, 236), (240, 206), (277, 186),
            (120, 256), (170, 266), (232, 254), (268, 240)]
q1 = (160, 176)
for p in pts_flat:
    f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" '
          'stroke-dasharray="3 3" opacity="0.5"/>' % (q1[0], q1[1], p[0], p[1], C.faint))
for p in pts_flat:
    f.raw('<circle cx="%d" cy="%d" r="4.5" fill="%s"/>' % (p[0], p[1], C.teal))
f.raw('<circle cx="%d" cy="%d" r="6.5" fill="%s" stroke="%s" stroke-width="2"/>'
      % (q1[0], q1[1], C.red, C.red_d))
f.text(q1[0] + 13, q1[1] - 8, "q", 12.5, C.red_d, 800)
f.note(x0 + 14, 302, "与全部 N 个向量逐一比较 · 精确但 O(N·d)", 10.5, C.faint)
f.text(x0 + 140, 344, "零预处理 · 小库直接用", 12, C.soft, 600)

# ============ 面板二: IVF 倒排分桶 ============
x0 = 350
f.group(x0, 80, 280, 236, "IVF 倒排分桶", fill="#ffffff", stroke=C.line, label_fill=C.soft)
clusters = [
    ((432, 138), [(407, 122), (447, 112), (457, 146), (417, 158)], True),
    ((545, 188), [(518, 172), (560, 162), (570, 204), (524, 214)], False),
    ((455, 258), [(428, 246), (470, 236), (486, 272), (432, 276)], False),
]
q2 = (382, 232)
# 被选中的桶 A 高亮
f.raw('<circle cx="432" cy="138" r="40" fill="%s" opacity="0.35"/>' % C.teal_s)
for (cx, cy), pts, picked in clusters:
    f.raw('<circle cx="%d" cy="%d" r="40" fill="none" stroke="%s" stroke-width="1.4" '
          'stroke-dasharray="5 4" opacity="0.75"/>' % (cx, cy, C.blue))
    for p in pts:
        f.raw('<circle cx="%d" cy="%d" r="4.5" fill="%s"/>' % (p[0], p[1], C.blue))
    f.raw('<rect x="%d" y="%d" width="9" height="9" fill="%s" transform="rotate(45 %d %d)"/>'
          % (cx - 4.5, cy - 4.5, C.blue_d, cx, cy))
for p in [(407, 122), (447, 112), (457, 146), (417, 158)]:
    f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.4" opacity="0.8"/>'
          % (q2[0], q2[1], p[0], p[1], C.teal))
f.raw('<circle cx="%d" cy="%d" r="6.5" fill="%s" stroke="%s" stroke-width="2"/>'
      % (q2[0], q2[1], C.red, C.red_d))
f.text(q2[0] - 14, q2[1] - 8, "q", 12.5, C.red_d, 800)
f.text(432, 92, "质心", 10.5, C.blue_d, 700)
f.note(x0 + 14, 302, "先聚类分桶 · 只搜最近的 nprobe 个桶", 10.5, C.faint)
f.text(x0 + 140, 344, "nprobe 调召回与速度", 12, C.soft, 600)

# ============ 面板三: HNSW 分层近邻图 ============
x0 = 650
f.group(x0, 80, 280, 236, "HNSW 分层近邻图", fill="#ffffff", stroke=C.line, label_fill=C.soft)
top = [(728, 132), (856, 128)]
mid = [(702, 186), (762, 178), (824, 190), (882, 180)]
bot = [(688, 258), (724, 250), (758, 262), (794, 246), (830, 258),
       (864, 250), (898, 262), (918, 252)]
def edges(seq):
    for a, b in zip(seq, seq[1:]):
        f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.1" opacity="0.55"/>'
              % (a[0], a[1], b[0], b[1], C.purple))
edges(top); edges(mid); edges(bot)
# 跨层连接(示意)
for a, b in [(top[0], mid[1]), (top[1], mid[3]), (mid[1], bot[2]), (mid[2], bot[4])]:
    f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.1" '
          'stroke-dasharray="3 3" opacity="0.4"/>' % (a[0], a[1], b[0], b[1], C.purple))
for p in top:
    f.raw('<circle cx="%d" cy="%d" r="5.5" fill="%s"/>' % (p[0], p[1], C.purple))
for p in mid:
    f.raw('<circle cx="%d" cy="%d" r="4.5" fill="%s"/>' % (p[0], p[1], C.purple))
for p in bot:
    f.raw('<circle cx="%d" cy="%d" r="3.8" fill="%s"/>' % (p[0], p[1], C.teal))
f.arrow(top[0][0] - 26, top[0][1], top[0][0] - 8, top[0][1], color=C.indigo, sw=1.8)
f.text(top[0][0] - 40, top[0][1] + 4, "入口", 11, C.indigo_d, 700)
f.arrow(top[0][0] + 8, top[0][1] + 7, mid[1][0] - 4, mid[1][1] - 6, color=C.indigo, sw=1.8)
f.arrow(mid[1][0] + 5, mid[1][1] + 6, bot[2][0] - 2, bot[2][1] - 8, color=C.indigo, sw=1.8)
f.text(918, 138, "L2", 10.5, C.faint, 700, anchor="start")
f.text(918, 192, "L1", 10.5, C.faint, 700, anchor="start")
f.text(918, 262, "L0", 10.5, C.faint, 700, anchor="start")
f.note(x0 + 14, 302, "顶层稀疏底层稠密 · 贪心下降, O(log N) 量级", 10.5, C.faint)
f.text(x0 + 140, 344, "M 与 efSearch 调准调快", 12, C.soft, 600)

f.note(480, 396, "召回率、延迟、内存构成三角权衡：没有万能参数，按数据规模与延迟预算实测调优",
       12.5, C.soft, anchor="middle")
f.save("fig-ann-index")
