# -*- coding: utf-8 -*-
"""figures_ch006.py — 第 6 章插图: 模糊提示 vs 可执行提示的改造对照"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(920, 500)
f.text(460, 32, "同一个需求:模糊提示 vs 可执行提示", 17, C.ink, 800)

# 左: 模糊提示
f.group(50, 64, 360, 232, "改造前", fill="#ffffff", label_fill=C.red_d)
f.box(80, 104, 300, 52, "帮我写个周报", fill=C.red_s, stroke=C.red, tc=C.red_d, fs=15)
f.mtext(230, 200, ["模型只能猜:给谁看?", "写什么?什么格式?多长?", "→ 输出四平八稳的模板文,", "写完还得自己重写一遍。"], 12, C.soft, 400, 1.7)

# 右: 可执行提示
f.group(470, 64, 410, 268, "改造后", fill="#ffffff", label_fill=C.green)
f.box(492, 100, 366, 150, "", fill=C.green_s, stroke=C.green, rx=9)
f.mtext(508, 124, [
    "你是我的写作助理。根据 <notes> 里的",
    "工作记录,给我写一份周报:",
    "① 面向不熟悉技术的老板;",
    "② 按『进展 / 风险 / 下周计划』三节;",
    "③ 每节 2~3 条,动词开头;",
    "④ 300 字以内,Markdown 输出。",
], 12, C.ink, 400, 1.62, anchor="start")

f.arrow(414, 180, 466, 180, color=C.faint, sw=2)

# 五个改造点
points = [("① 角色", "让模型代入职责"), ("② 素材边界", "只依据给定材料"), ("③ 受众", "决定深度与术语"),
          ("④ 结构", "交付的骨架"), ("⑤ 长度与格式", "可验收的标准")]
px = 480
for t, d in points:
    w = tw(t, 12) + 22
    f.pill(px + w / 2, 372, t, fill=C.indigo_s, tc=C.indigo_d, fs=12)
    f.text(px + w / 2, 396, d, 10.5, C.faint, 400)
    px += w + 12

f.text(60, 340, "改造的动作只有一个:", 12, C.ink, 700, anchor="start")
f.text(60, 360, "把脑子里的隐含期望,", 12, C.ink, 700, anchor="start")
f.text(60, 380, "全部搬到纸面上。", 12, C.ink, 700, anchor="start")
f.note(460, 448, "自检三问:模型知道背景吗?知道边界(用什么素材、不做什么)吗?知道交付长什么样吗?", 12, C.faint, anchor="middle")
f.note(460, 476, "仍不确定时,先让模型反问你 —— 它会告诉你它缺什么信息", 12, C.faint, anchor="middle")
f.save("fig-prompt-rewrite")

print("figures_ch006 done")
