# -*- coding: utf-8 -*-
"""figures_ch046.py — ch046 PRM/ORM 奖励设计插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 46-1: ORM vs PRM ----
f = F(940, 400)
f.text(470, 32, "结果奖励 ORM 与过程奖励 PRM", 18, C.ink, 800)

# 左: ORM
f.group(40, 60, 400, 300, "ORM · Outcome-based")
steps_l = ["读题", "列式", "计算", "验算", "答案"]
x = 80
for i, s in enumerate(steps_l):
    c = C.teal if i < len(steps_l) - 1 else C.red
    b = f.box(x, 120, 62, 46, s, None, fill=C.white, stroke=c, fs=12)
    if i < len(steps_l) - 1:
        f.arrow(x + 62, 143, x + 84, 143, "", C.soft)
    x += 84
f.text(240, 210, "✓ / ✗ 只看终点", 13, C.red, 800)
f.note(60, 250, "优点: 信号绝对客观, 无需人工定义「好过程」")
f.note(60, 275, "缺点: 信用分配缺失 — 错在哪步不知道;")
f.note(60, 298, "      幸存者偏差 — 错误过程也可能蒙对答案")
f.note(60, 335, "代表: RLVR 数学判分 · WebRL 的成功判别器", 11.5, C.indigo_d)

# 右: PRM
f.group(500, 60, 400, 300, "PRM · Process-based")
x = 540
for i, s in enumerate(steps_l):
    col = C.teal if i != 2 else C.red
    b = f.box(x, 120, 62, 46, s, None, fill=C.white, stroke=col, fs=12)
    if i < len(steps_l) - 1:
        f.arrow(x + 62, 143, x + 84, 143, "", C.soft)
    x += 84
f.text(700, 210, "每步一个评分 ✓ ✗ ✓ ✓ ✓", 13, C.indigo, 800)
f.note(520, 250, "优点: 信用分配精确; 可在推理中途剪枝(提前终止)")
f.note(520, 275, "缺点: 标注昂贵; 判据本身可被黑客(格式合规≠正确)")
f.note(520, 335, "代表: Math-Shepherd 自动过程标注 · OmegaPRM", 11.5, C.indigo_d)
f.save("fig-orm-prm")

# ---- fig 46-2: Math-Shepherd 自动过程标注 ----
f = F(940, 400)
f.text(470, 32, "Math-Shepherd: 用「续写成功率」自动标注过程分", 18, C.ink, 800)
b1 = f.box(60, 90, 180, 100, "中间步骤 sₜ", "「两边同除以\n(x-1)」", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(300, 90, 180, 100, "从此步续写 N 次", "MC 蒙特卡洛 rollout\n(N=8~16)", fill=C.amber_s, stroke=C.amber)
b3 = f.box(540, 90, 170, 100, "统计到达终点率", "4/8 次得到正确答案", fill=C.teal_s, stroke=C.teal)
b4 = f.box(760, 90, 130, 100, "过程分 0.5", "自动、零人工", fill=C.purple_s, stroke=C.purple)
f.arrow(240, 140, 300, 140, "", C.soft)
f.arrow(480, 140, 540, 140, "", C.soft)
f.arrow(710, 140, 760, 140, "", C.soft)
f.note(80, 230, "直觉: 「好步骤」是继续走更容易到达终点的步骤 — 与 Toolformer「插入调用降低损失」判据同构:")
f.note(80, 254, "都是用「对后续任务的帮助」这一统计证据替代人工标注。两种补全模式:")
f.note(100, 286, "硬估计: rollout 全程跑到底, 只统计最终对错 (干净但贵)")
f.note(100, 310, "软估计: 用 PRM 当前版本给 rollout 中途打分 (便宜但引入自身偏差)")
f.note(80, 355, "坑: 「碰运气」步骤会得到虚高分 — 同一步骤多题多次标注取中位数可抑制方差", 11.5, C.red)
f.save("fig-math-shepherd")

# ---- fig 46-3: 奖励黑客四种形态 ----
f = F(940, 400)
f.text(470, 32, "奖励黑客的四种形态与断点器", 18, C.ink, 800)
cells = [
    (60,  90, C.red,    "格式黑客", "把思考写成判分器爱看的模板\n(每步都「验证:✓」但内容空洞)", "判分器加「内容多样性/长度惩罚」;\n定期抽看真实轨迹"),
    (500, 90, C.amber,  "判别器黑客", "学会 ORM 的盲区:\n用判分器看不出的方式作弊", "对抗轮换: 更新判别器 ↔ 更新策略;\n保留规则判分做锚"),
    (60,  240, C.purple, "赌徒黑客", "多采样碰运气:\n输出 5 个答案蹭对 1 个", "答案唯一性约束;\nbest-of-n 计分改为 first-answer"),
    (500, 240, C.teal,  "刷子黑客", "在「易通过」的验证子集上\n反复横跳刷分", "隐藏测试集轮换;\n通过率-难度联合监控"),
]
for x, y, colr, t, d, fix in cells:
    f.box(x, y, 380, 130, t, None, fill=C.white, stroke=colr)
    f.text(x + 190, y - 12, t, 14, colr, 800)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + 190, y + 40 + i * 17, ln, 11.5, C.ink)
    for i, ln in enumerate(("断点器: " + fix).split("\n")):
        f.text(x + 190, y + 86 + i * 15, ln, 10.5, C.faint)
f.save("fig-reward-hacking")
