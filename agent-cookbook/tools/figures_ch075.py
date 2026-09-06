# -*- coding: utf-8 -*-
"""figures_ch075.py — ch075 Computer Use 与 Browser Use 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 75-1: 双轨交互架构 ----
f = F(940, 420)
f.text(470, 32, "Computer Use 与 Browser Use 的双轨交互体系", 18, C.ink, 800)
c1 = f.box(60, 100, 380, 220, "Browser Use (DOM/结构主导)", None, fill=C.white, stroke=C.teal)
f.text(250, 130, "Browser Use (DOM/结构主导)", 14, C.teal, 800)
for i, ln in enumerate([
    "· 底座: Playwright / CDP (Chrome DevTools)",
    "· 感知: 页面 Accessibility Tree + 局部截图",
    "· 操作: 结构化 CSS 选择器 / 语义点击",
    "· 特点: 执行极其精准、资源消耗相对低",
    "· 挑战: 动态反爬机制、反常态弹窗阻断"
]):
    f.text(250, 160 + i * 20, ln, 10.5, C.ink)

c2 = f.box(500, 100, 380, 220, "Computer Use (视觉/坐标主导)", None, fill=C.white, stroke=C.indigo)
f.text(690, 130, "Computer Use (视觉/坐标主导)", 14, C.indigo, 800)
for i, ln in enumerate([
    "· 底座: 原生操作系统 API (macOS/Win/X11)",
    "· 感知: 全屏/窗口级高清连续抓屏 (VLM)",
    "· 操作: 虚拟键鼠模拟 (鼠标移动/点击/热键)",
    "· 特点: 全局普适、无视软件技术栈与封锁",
    "· 挑战: 分辨率多重缩放、定位漂移、时钟延迟"
]):
    f.text(690, 160 + i * 20, ln, 10.5, C.ink)

f.note(470, 355, "前沿演进: 纯视觉与结构化正在合流 — 浏览器内走精确 DOM, 遇到 Canvas 或跨系统跳出走视觉坐标", 11.5, C.indigo_d, anchor="middle")
f.save("fig-computer-browser-dual")

# ---- fig 75-2: 验证码与对抗防御 ----
f = F(940, 380)
f.text(470, 32, "CAPTCHA、反自动化对抗与伦理红线", 18, C.ink, 800)
b1 = f.box(60, 110, 180, 110, "① 触发风控", "Cloudflare / 极验\n行为指纹与轨迹异常", fill=C.red_s, stroke=C.red)
b2 = f.box(300, 110, 180, 110, "② 判定意图", "正常数据获取?\n或黑产滥用?", fill=C.amber_s, stroke=C.amber)
b3 = f.box(540, 110, 180, 110, "③ 策略分流", "授权环境走 Bypass\n未授权则停手机制", fill=C.teal_s, stroke=C.teal)
b4 = f.box(770, 110, 120, 110, "④ 人工接管", "安全闸门\n人工完成校验", fill=C.purple_s, stroke=C.purple)
f.arrow(240, 165, 300, 165, "", C.soft)
f.arrow(480, 165, 540, 165, "", C.soft)
f.arrow(720, 165, 770, 165, "", C.soft)
f.note(470, 260, "伦理红线原则: 研发自动化智能体旨在提升人机交互效率，严禁用于绕过反爬机制实施黑客攻击或恶意刷量", 11.5, C.red, anchor="middle")
f.note(470, 290, "工程标准做法: 遇到验证码强制呼出人类接管 UI, 绝不擅自调用破解模型或打码平台(第65章合规基线)", 11.5, C.ink, anchor="middle")
f.save("fig-captcha-ethics")
