# -*- coding: utf-8 -*-
"""figures_ch048.py — ch048 蒸馏与小型化插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 48-1: 白盒 vs 黑盒蒸馏 ----
f = F(940, 400)
f.text(470, 32, "蒸馏的两种通道:白盒(logits)与黑盒(轨迹)", 18, C.ink, 800)
# 左: 白盒
f.group(40, 60, 410, 290, "白盒蒸馏 · 需要教师权重")
tb = f.box(80, 110, 150, 70, "教师模型", "权重可及", fill=C.indigo_s, stroke=C.indigo)
sb = f.box(80, 230, 150, 70, "学生模型", None, fill=C.teal_s, stroke=C.teal)
f.arrow(155, 180, 155, 230, "logits / 软标签\n(KL 散度)", C.red)
f.pill(330, 145, "完整分布信息", C.blue_s, C.blue_d)
f.pill(330, 195, "≈ 1 块 GPU 即可", C.teal_s, C.teal_d)
f.pill(330, 245, "不能跨架构/闭源", C.amber_s, C.amber_d)
# 右: 黑盒
f.group(490, 60, 410, 290, "黑盒蒸馏 · 只要 API")
ab = f.box(530, 110, 150, 70, "教师模型", "仅 API 可用", fill=C.indigo_s, stroke=C.indigo)
tr = f.box(530, 230, 150, 70, "示范轨迹", "推理/工具调用", fill=C.amber_s, stroke=C.amber)
stu = f.box(710, 170, 150, 70, "学生模型", "SFT 学模仿", fill=C.teal_s, stroke=C.teal)
f.arrow(605, 180, 605, 230, "生成", C.red)
f.arrow(680, 265, 760, 240, "", C.soft)
f.arrow(785, 170, 785, 240, "", C.soft)
f.pill(790, 110, "跨架构 / 闭源可行", C.blue_s, C.blue_d)
f.pill(790, 160, "丢失分布细节", C.amber_s, C.amber_d)
f.save("fig-distill-paths")

# ---- fig 48-2: 端侧 Agent 算术 ----
f = F(940, 420)
f.text(470, 32, "端侧 Agent 的算术:参数量 × 精度 × 上下文 的三角约束", 17, C.ink, 800)
rows = [
    ("3B · Q4 · 8k 上下文", 110, C.teal,  "≈ 2GB 显存占用 · 手机可跑 · 能力≈GPT-3.5 的工具调用"),
    ("7B · Q4 · 16k 上下文", 190, C.blue, "≈ 5GB · 旗舰手机/小主机 · 经蒸馏后可过简单 Agent 任务"),
    ("7B · Q8 · 32k 上下文", 270, C.amber, "≈ 9GB · 需独显/NEC · 全格式可用,长轨迹可行"),
    ("14B · Q4 · 16k 上下文", 350, C.purple, "≈ 9GB · 端侧能力天花板档 · 推荐的「端侧 Agent 默认档」"),
]
for label, y, colr, note_ in rows:
    f.pill(230, y, label, colr + "_s", colr)
    f.text(700, y + 4, note_, 11.5, C.faint, 400, anchor="middle")
f.note(470, 395, "经验: KV 缓存占用量 = 2 × 层数 × KV头数 × 头维 × 上下文长度 × 精度字节 — 长上下文是端侧 Agent 的最大敌人", 11.5, C.faint, anchor="middle")
f.save("fig-edge-arithmetic")
