# -*- coding: utf-8 -*-
"""figures_ch058b.py — ch058 混淆代理问题插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(940, 400)
f.text(470, 32, "Confused Deputy:有权限的代理人被无权限者指挥", 18, C.ink, 800)
atk = f.box(60, 120, 160, 100, "攻击者", "写入恶意网页", fill=C.red_s, stroke=C.red)
res = f.box(280, 120, 150, 100, "资源", "用户的数据\n(攻击者无权访问)", fill=C.amber_s, stroke=C.amber)
dep = f.box(510, 120, 160, 100, "Agent(代理)", "持有全部权限\n被注入指令操纵", fill=C.indigo_s, stroke=C.indigo)
vic = f.box(760, 120, 130, 100, "受害者", "数据被外泄", fill=C.purple_s, stroke=C.purple)
f.arrow(220, 160, 280, 160, "投毒", C.red)
f.arrow(430, 185, 510, 185, "Agent 读取", C.soft)
f.arrow(670, 160, 760, 160, "外泄", C.red)
f.note(70, 270, "关键缺陷: Agent 的权限 ≠ 用户的权限 — 代理合并了「读资源」与「听指挥」两个能力,")
f.note(70, 294, "而这两个能力的授权者不同(资源属于用户, 指挥可能来自任何数据源)。")
f.note(70, 326, "解法方向: ① 权限跟随数据来源(源自不可信域的指令降权) ② 高危动作需「用户来源」的指令 ③ 出站过滤", 11.5, C.indigo_d)
f.save("fig-confused-deputy")
