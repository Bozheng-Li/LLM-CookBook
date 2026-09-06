# -*- coding: utf-8 -*-
"""figures_ch003.py — 第 3 章插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 心智模型: 食谱 vs 厨师
f = F(920, 420)
f.text(460, 30, "心智模型:工作流是食谱,Agent 是厨师", 17, C.ink, 800)
left = f.box(60, 80, 380, 200, "", fill=C.blue_s, stroke=C.blue, rx=14)
f.text(250, 112, "📋 工作流 Workflow = 食谱", 15, C.blue_d, 800)
f.mtext(250, 146, ["步骤 1: 热锅 → 步骤 2: 炒蛋 → 步骤 3: 下饭", "每一步由『食谱作者』预先决定,", "换食材(新需求)就要改食谱(改代码)。", "可预测、可复现,但僵硬。"], 12, C.ink, 400, 1.8)
right = f.box(480, 80, 380, 200, "", fill=C.teal_s, stroke=C.teal, rx=14)
f.text(670, 112, "👨‍🍳 Agent = 厨师", 15, C.teal_d, 800)
f.mtext(670, 146, ["目标是『一桌好菜』,步骤由厨师现场判断:", "鸡蛋不新鲜 → 换西红柿;", "客人赶时间 → 先上凉菜。", "灵活、能应对意外,但需要信任与验收。"], 12, C.ink, 400, 1.8)
f.arrow(445, 180, 475, 180, color=C.faint, sw=1.6)
f.group(60, 300, 800, 90, "工程含义")
f.text(80, 336, "选食谱还是雇厨师,取决于任务的『意外密度』: 步骤固定且输入稳定 → 工作流;输入多变且需要判断 → Agent。", 12.5, C.ink, 400, anchor="start")
f.text(80, 364, "大多数真实系统是混合体:外层工作流编排,内层若干个『厨师』处理不可预测的子任务(见第 14、24 章)。", 12.5, C.ink, 400, anchor="start")
f.save("fig-mental-model")

print("ch003 figures done")
