# -*- coding: utf-8 -*-
"""figures_ch068.py — ch068 移动/OS Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 68-1: 移动 Agent 的感知-动作栈 ----
f = F(940, 420)
f.text(470, 32, "移动 Agent 的感知与动作栈", 18, C.ink, 800)
l1 = f.box(60, 90, 250, 110, "感知层", "aXTree (无障碍树)\n+ 截图 + 控件 ID", fill=C.teal_s, stroke=C.teal)
l2 = f.box(345, 90, 250, 110, "决策层", "LLM/多模态模型\n规划 + 动作选择", fill=C.indigo_s, stroke=C.indigo)
l3 = f.box(630, 90, 250, 110, "动作层", "a11y 指令 / 注入事件\n坐标点击 / 手势", fill=C.amber_s, stroke=C.amber)
f.arrow(310, 145, 345, 145, "", C.soft)
f.arrow(595, 145, 630, 145, "", C.soft)
f.raw('<rect x="60" y="240" width="820" height="110" rx="10" fill="#fafaf7" stroke="%s" stroke-dasharray="6 4"/>' % C.line)
f.text(470, 268, "移动 vs 桌面的三个工程差异", 12.5, C.indigo_d, 800)
f.text(470, 292, "① 系统弹层是不可控变量 (权限框/通知) — 必须进考纲(第52章)", 11, C.ink)
f.text(470, 312, "② 交互粒度更粗: 无悬停/右键, 每次点击的语义权重更大", 11, C.ink)
f.text(470, 332, "③ 生命周期与后台化: App 切换/杀进程 — 任务状态要可持久化", 11, C.ink)
f.save("fig-mobile-stack")

# ---- fig 68-2: OS-Copilot 的技能框架 ----
f = F(940, 400)
f.text(470, 32, "OS-Copilot 式技能框架:Agent 的「可成长器官」", 18, C.ink, 800)
core = f.box(380, 150, 180, 100, "规划核心", "任务分解\n技能调度", fill=C.indigo_s, stroke=C.indigo)
sk1 = f.box(80, 80, 180, 70, "内置技能", "文件/剪贴板/截图", fill=C.teal_s, stroke=C.teal, fs=12)
sk2 = f.box(80, 250, 180, 70, "自学习技能", "FRIDAY: 从演示学新技能", fill=C.amber_s, stroke=C.amber, fs=12)
sk3 = f.box(680, 80, 180, 70, "外部工具", "MCP / 插件市场", fill=C.blue_s, stroke=C.blue, fs=12)
sk4 = f.box(680, 250, 180, 70, "技能库(成长)", "自建技能沉淀复用", fill=C.purple_s, stroke=C.purple, fs=12)
for sk in (sk1, sk2, sk3, sk4):
    f.arrow(sk["cx"], sk["cy"] + (0 if sk["cy"] < 200 else 0), 470, 200, "", C.soft, sw=1.4)
f.note(470, 360, "与固定流程自动化的本质区别: 技能库随使用成长 — 「用得越久越能干」是 OS Agent 的产品价值核心", 11.5, C.indigo_d, anchor="middle")
f.save("fig-os-copilot")
