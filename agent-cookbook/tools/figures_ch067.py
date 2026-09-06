# -*- coding: utf-8 -*-
"""figures_ch067.py — ch067 GUI Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 67-1: GUI Agent 的感知-决策-执行循环 ----
f = F(940, 420)
f.text(470, 32, "GUI Agent 循环:感知 → 决策 → 执行 → 验证", 18, C.ink, 800)
p1 = f.box(60, 100, 190, 110, "① 感知", "截图 + DOM/aXTree\nSoM 标注(第52章)", fill=C.teal_s, stroke=C.teal)
p2 = f.box(300, 100, 190, 110, "② 决策", "下一步动作 + 目标元素\n(点击/输入/滚动)", fill=C.indigo_s, stroke=C.indigo)
p3 = f.box(540, 100, 180, 110, "③ 执行", "坐标点击 / 控件操作\n动作层(Playwright/OS)", fill=C.amber_s, stroke=C.amber)
p4 = f.box(770, 100, 130, 110, "④ 验证", "预期状态检查\n(第46章断言)", fill=C.purple_s, stroke=C.purple)
f.arrow(250, 155, 300, 155, "", C.soft)
f.arrow(490, 155, 540, 155, "", C.soft)
f.arrow(720, 155, 770, 155, "", C.soft)
f.elbow([(835, 210), (835, 300), (155, 300), (155, 210)], "未达预期 → 重感知 (错误恢复循环)", C.red, label_pos=1)
f.note(470, 350, "与文本 Agent 循环的唯一结构差异: 「执行验证」强制在环 — GUI 动作的不可逆性要求每步后核对(第58章传导链)", 11.5, C.ink, anchor="middle")
f.note(470, 385, "性能三支柱: 感知精度(第66章) × 动作可靠性(本章) × 错误恢复策略(本章 67.4)", 11.5, C.faint, anchor="middle")
f.save("fig-gui-loop")

# ---- fig 67-2: WebVoyager → Computer Use 的能力阶梯 ----
f = F(940, 380)
f.text(470, 32, "GUI Agent 的四级阶梯:从网页到桌面", 18, C.ink, 800)
steps = [
    (60,  240, 200, 90, "L1 网页浏览", C.teal,  "DOM/结构化优先\nWebVoyager 类", "浏览器内"),
    (290, 170, 200, 160, "L2 视觉网页", C.blue, "纯截图操作\nVisualWebArena", "无 DOM 依赖"),
    (520, 100, 200, 230, "L3 桌面应用", C.amber, "本地软件窗口\n剪贴板/文件系统", "OS 级 API"),
    (750, 30, 150, 300, "L4 整机操作", C.red, "系统设置/多应用\nComputer Use", "全 OS 权限"),
]
for x, y, w, h, t, colr, d, scope in steps:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=13)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + w/2, y + 52 + i * 17, ln, 10.5, C.ink)
    f.text(x + w/2, y + h - 12, scope, 9.5, colr, 800)
for i in range(3):
    x1 = steps[i][0] + steps[i][2]
    f.arrow(x1 + 3, steps[i][1] + 45, x1 + 27, steps[i+1][1] + 80, "", C.soft)
f.note(470, 360, "阶梯的爬升=工程复杂度的跃迁: L1→L2 加视觉, L2→L3 加 OS 集成与权限(第60章), L3→L4 加全系统沙箱与审计", 11.5, C.faint, anchor="middle")
f.save("fig-gui-ladder")
