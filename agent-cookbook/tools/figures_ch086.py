# -*- coding: utf-8 -*-
"""figures_ch086.py — ch086 端侧与移动端轻量化 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 86-1: 端云协同与移动端轻量化 Agent 架构
f = F(940, 420)
f.box(40, 60, 170, 110, "1. 手机端感知与无障碍\nAndroid aXTree / iOS\n轻量截屏与 OCR 预处理\n敏感隐私本地脱敏", fill=C.blue_s, stroke=C.blue)
f.box(250, 60, 170, 110, "2. 端侧轻量 SLM\n(0.5B ~ 3B Q4_K_M)\n端侧 Fast 意图分类\n简易单步 Tool Call", fill=C.indigo_s, stroke=C.indigo)
f.box(460, 60, 170, 110, "3. 端云自适应路由\nOn-Device vs Cloud\n高复杂度 / 深度推理\n自动上浮至云端大模型", fill=C.amber_s, stroke=C.amber)
f.box(670, 60, 220, 110, "4. 物理按键与手势注入\nOS Action Injector\nTap / Swipe / InputText\n执行前后视觉校验 (Verify)", fill=C.teal_s, stroke=C.teal)

f.arrow(210, 115, 250, 115, "结构化树")
f.arrow(420, 115, 460, 115, "意图与置信度")
f.arrow(630, 115, 670, 115, "执行动作")

# 云端回退虚线
f.elbow([(545, 60), (545, 20), (780, 20), (780, 60)], label="复杂长程规划 (Cloud 70B+ / o1)", color=C.red, label_pos=1)

# 底部系统限制与低功耗保护
f.box(100, 290, 740, 100, "移动端苛刻资源约束治理 (Resource & Battery Protection)\n• 内存硬预算: 常驻运行内存 <= 1.5GB (防 Android LMK 强杀)\n• NPU / GPU 异构加速: llama.cpp / MLC-LLM / CoreML 低功耗推理\n• 温度与电池守卫: 高频感知降频，避免设备过热降频卡死", fill=C.purple_s, stroke=C.purple)

f.save("fig-mobile-agent-arch")

# fig 86-2: 移动端无障碍 UI 树剪枝与精简
f = F(940, 350)
f.box(60, 100, 200, 160, "原始 Android UI 树\n(上千个嵌套 View 节点)\n• LinearLayout\n• FrameLayout\n• ScrollView\n• 隐藏/不可视组件\n(体积 > 50KB / 15k Token)", fill=C.red_s, stroke=C.red)

f.box(360, 100, 220, 160, "三级过滤剪枝流水线\n1. 可视边界过滤 (is_visible)\n2. 可交互属性过滤\n   (clickable / focusable)\n3. 文本与语义属性压缩\n   (仅保留 text / desc / id)", fill=C.amber_s, stroke=C.amber)

f.box(680, 100, 200, 160, "精简极小 UI 树\n(15~30 个关键控件)\n[1] 搜索框 (Editable)\n[2] 扫一扫 (Clickable)\n[3] 付款码 (Clickable)\n(体积 < 1.2KB / 400 Token)", fill=C.green_s, stroke=C.green)

f.arrow(260, 180, 360, 180, "原始 Dump")
f.arrow(580, 180, 680, 180, "极速压缩")

f.save("fig-mobile-axtree-prune")
print("ch086 figures generated successfully")
