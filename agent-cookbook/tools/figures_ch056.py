# -*- coding: utf-8 -*-
"""figures_ch056.py — ch056 自建评测插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 56-1: 评测 harness 架构 ----
f = F(940, 430)
f.text(470, 32, "自建评测 Harness 的五层架构", 18, C.ink, 800)
layers = [
    (60,  80,  C.indigo, "题目层 Task Store", "任务定义 + 终态判据 + 元数据\n版本化 · 难度标签 · 陷阱标记"),
    (250, 80,  C.teal,   "环境层 Environment", "Docker 沙箱 · mock API · DB 副本\n快照重置 · 并行副本池"),
    (440, 80,  C.amber,  "执行层 Runner", "被测系统接入 · 轨迹记录 · 预算控制\n超时熔断 · 并发调度"),
    (630, 80,  C.purple, "判分层 Grader", "终态断言 → 轨迹约束 → Judge\n判定结果 + 依据落库"),
    (820, 80,  C.red,    "报告层 Reporter", "分层报告 · 趋势线 · 回归对比\n门禁判定 → CI 信号"),
]
for x, y, colr, t, d in layers:
    f.box(x, y, 30, 240, "", None, fill=colr, stroke=colr)
    f.text(x + 15, y - 12, str(layers.index((x, y, colr, t, d)) + 1), 12, colr, 800)
    f.text(x + 44, y + 10, t, 12.5, C.ink, 800, anchor="start")
    for i, ln in enumerate(d.split("\n")):
        f.text(x + 44, y + 34 + i * 17, ln, 10.5, C.faint, 400, anchor="start")
f.note(470, 350, "数据流: 任务 → 环境 → 执行 → 判定 → 报告, 全程带版本戳 (任务版/环境版/判分版/被测版) — 无版本的分数不存在", 11.5, C.ink, anchor="middle")
f.note(470, 380, "复用原则: 环境层与判分层与第 45/54 章的训练/工具评测共用 — 一套基建三处受益", 11.5, C.faint, anchor="middle")
f.save("fig-eval-harness")

# ---- fig 56-2: CI 门禁流水线 ----
f = F(940, 400)
f.text(470, 32, "评测进 CI:变更的质量门禁流水线", 18, C.ink, 800)
stages = [
    (60,  140, 150, 90, "提交/变更", "提示词 · 工具\n模型 · 框架配置", C.indigo),
    (250, 140, 150, 90, "快测门禁", "地基层 30 题\n分钟级 · 阻断式", C.teal),
    (440, 140, 150, 90, "夜间回归", "完整自建集\n小时级 · 报告制", C.amber),
    (630, 140, 140, 90, "安全门禁", "注入回归集\n失败必须阻断", C.red),
    (810, 140, 90, 90, "发布", "灰度 5%\n→ 全量", C.purple),
]
for x, y, w, h, t, d, colr in stages:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=13)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + w/2, y + 52 + i * 15, ln, 9.5, C.faint)
for i in range(4):
    x1 = stages[i][0] + stages[i][2]
    x2 = stages[i+1][0]
    f.arrow(x1 + 4, 185, x2 - 4, 185, "", C.soft)
# 失败回路
f.elbow([(325, 230), (325, 310), (135, 310), (135, 230)], "快测失败: 立即阻断+定位", C.red, label_pos=1)
f.elbow([(700, 230), (700, 345), (325, 345), (325, 310)], "安全失败: 无条件阻断", C.red, label_pos=1)
f.note(470, 60, "门禁哲学: 快测防「明显回退」(分钟), 夜测防「慢性漂移」(天), 安全门禁防「事故」(无条件)", 11.5, C.faint, anchor="middle")
f.save("fig-ci-gates")
