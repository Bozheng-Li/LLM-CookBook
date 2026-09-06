# -*- coding: utf-8 -*-
"""figures_ch089.py — ch089 多模态具身操作系统 Agent (Computer Use) 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 89-1: 多模态 Computer Use 闭环执行流水线
f = F(940, 420)
f.box(40, 60, 170, 110, "1. 多模态屏幕捕获\nScreen Observation\n无头 Xvfb / 物理截屏\nROI 动态裁剪与下采样", fill=C.blue_s, stroke=C.blue)
f.box(250, 60, 170, 110, "2. 视觉空间坐标定位\nVLM Grounding\n归一化坐标预测 (x,y)\n语义与图标多维解析", fill=C.indigo_s, stroke=C.indigo)
f.box(460, 60, 170, 110, "3. OS 硬件外设注入\nVirtual HID Injector\nPyAutoGUI / uinput 驱动\n鼠标点击/拖拽/键盘输入", fill=C.amber_s, stroke=C.amber)
f.box(670, 60, 220, 110, "4. 动作后置视觉校验\nPost-Action Verification\n前后两帧差分比对 (Diff)\n未产生状态变动自愈重试", fill=C.teal_s, stroke=C.teal)

f.arrow(210, 115, 250, 115, "高保真位图")
f.arrow(420, 115, 460, 115, "目标物理像素")
f.arrow(630, 115, 670, 115, "模拟外设信号")

# 底部视觉差分未生效自愈环路
f.elbow([(780, 170), (780, 240), (545, 240), (545, 170)], label="动作未产生预期视觉响应 (如点击未弹窗): 重新自适应变异点击坐标 (Max 3次)", color=C.red, label_pos=1)

# 底部基础设施与安全防护
f.box(100, 290, 740, 100, "隔离沙箱与人机物理控制权守卫 (Sandbox & Safety Guardrails)\n• 虚拟化桌面沙箱: Docker + XFCE + noVNC 隔离环境 (严格物理阻断宿主机污染)\n• 物理安全熔断开关 (Panic Button): 检测到光标疯狂移动或高敏弹窗，按 ESC 瞬间强杀进程\n• 敏感资产物理黑名单: 绝不接管个人银行密码、数字证书与系统底层终端", fill=C.purple_s, stroke=C.purple)

f.save("fig-computer-use-arch")

# fig 89-2: 视觉语义锚点坐标预测与状态变动验证
f = F(940, 360)
f.box(60, 100, 200, 160, "当前屏幕截图 (Frame T)\n分辨率: 1920x1080\n[文件编辑区] [另存为按钮]\n(模型视觉输入)", fill=C.blue_s, stroke=C.blue)

f.box(320, 100, 200, 160, "VLM 空间推理定位\n识别目标: '另存为按钮'\n预测归一化坐标:\n(0.84, 0.12)\n映射物理像素: (1612, 130)", fill=C.indigo_s, stroke=C.indigo)

f.box(580, 100, 180, 160, "执行物理点击\nMouse Left Click\n(1612, 130)\n等待 300ms 界面重绘", fill=C.amber_s, stroke=C.amber)

f.box(810, 100, 110, 160, "Frame T+1\n弹出保存框\n验证通过\n(Verified)", fill=C.green_s, stroke=C.green)

f.arrow(260, 180, 320, 180, "输入图像")
f.arrow(520, 180, 580, 180, "下发动作")
f.arrow(760, 180, 810, 180, "差分比对")

f.save("fig-vlm-grounding-diff")
print("ch089 figures generated successfully")
