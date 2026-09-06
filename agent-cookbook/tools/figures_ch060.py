# -*- coding: utf-8 -*-
"""figures_ch060.py — ch060 权限与沙箱插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 60-1: L0-L3 操作分级 ----
f = F(940, 420)
f.text(470, 32, "操作分级 L0~L3:按爆炸半径决定审批链", 18, C.ink, 800)
tiers = [
    (60,  100, 200, 220, "L0 只读", C.teal,  ["查询/检索/计算", "——", "自动执行", "示例: 查库存", "读文档"],
     "无副作用 = 无风险"),
    (290, 100, 200, 220, "L1 可逆写", C.amber, ["写入可撤销的数据", "——", "自动执行 + 事后审计", "示例: 加购物车", "写草稿"],
     "有撤销路径 = 低风险"),
    (520, 100, 200, 220, "L2 受控写", C.blue,  ["真实副作用·不可逆", "——", "预演 + 抽样人工审", "示例: 提交订单", "创建工单"],
     "损失可控 = 中风险"),
    (750, 100, 140, 220, "L3 高危", C.red,  ["资金/删除/外发", "——", "预演 + 逐条人工确认", "示例: 付款", "删除数据"],
     "不可逆且重大 = 闸门"),
]
for x, y, w, h, t, colr, lines_, note_ in tiers:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=14)
    for i, ln in enumerate(lines_):
        f.text(x + w/2, y + 50 + i * 22, ln, 10.5, C.red if ln == "——" else (colr if i == 3 or i == 0 else C.ink), 800 if i == 0 else 400)
    f.text(x + w/2, y + h - 14, note_, 9.5, C.faint)
f.note(470, 355, "分级的关键问题只有一个: 「这个动作做错了, 损失多大? 能撤销吗?」——答不出就按上一级处理", 11.5, C.ink, anchor="middle")
f.note(470, 385, "权限随任务动态收缩: 任务开始时只加载该任务所需级别的工具 — L0 任务里 L3 工具根本不在上下文中", 11.5, C.faint, anchor="middle")
f.save("fig-op-tiers")

# ---- fig 60-2: 沙箱技术谱系 ----
f = F(940, 380)
f.text(470, 32, "沙箱技术谱系:隔离强度 × 工程代价", 18, C.ink, 800)
rows = [
    (90,  C.teal,   "进程内限制", "纯软件约束 (超时/配额/系统提示)", "隔离★", "成本☆"),
    (160, C.blue,   "容器 (Docker)", "命名空间 + cgroups · 标准选择", "隔离★★★", "成本★"),
    (230, C.indigo, "微VM (gVisor/Firecracker)", "轻量内核隔离 · 强对抗环境", "隔离★★★★", "成本★★"),
    (300, C.purple, "整机VM", "OS 级隔离 · Computer-Use 场景", "隔离★★★★★", "成本★★★"),
]
for y, colr, t, d, iso, cost in rows:
    f.box(60, y, 520, 54, t, None, fill=C.white, stroke=colr, fs=12.5)
    f.text(330, y + 38, d, 10.5, C.faint)
    f.text(660, y + 27, iso, 11.5, colr, 800)
    f.text(810, y + 27, cost, 11.5, C.faint, 800)
f.note(470, 360, "选型公式: 隔离强度要匹配「被隔离代码的威胁等级」— 代码执行用微VM, 工具调用用容器, 纯查询进程内即可", 11.5, C.ink, anchor="middle")
f.save("fig-sandbox-spectrum")
