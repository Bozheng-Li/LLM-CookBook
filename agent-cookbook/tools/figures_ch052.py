# -*- coding: utf-8 -*-
"""figures_ch052.py — ch052 Web/Computer-Use 基准插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 52-1: WebArena 架构 ----
f = F(940, 420)
f.text(470, 32, "WebArena 的自包含环境:真实站点的镜像宇宙", 18, C.ink, 800)
sites = [
    (60, 90,  C.indigo, "GitLab 镜像", "代码托管 · issue"),
    (260, 90, C.teal,   "OneStopMarket", "电商 · 购物车"),
    (460, 90, C.blue,   "内容管理 CMS", "Wiki · 论坛"),
    (660, 90, C.amber,  "地图应用", "导航 · POI 检索"),
]
for x, y, colr, t, d in sites:
    f.box(x, y, 180, 80, t, None, fill=C.white, stroke=colr)
    f.text(x + 90, y + 58, d, 10.5, C.faint)
f.note(70, 205, "全部容器化自托管 — 无外网依赖, 任务可复现 (第50章「环境参与评测」问题的最完整解答)")
b1 = f.box(120, 240, 200, 80, "Agent", "观察 DOM/截图 → 动作", fill=C.teal_s, stroke=C.teal)
b2 = f.box(400, 240, 200, 80, "动作接口", "点击 / 输入 / 导航", fill=C.amber_s, stroke=C.amber)
b3 = f.box(680, 240, 210, 80, "终态断言", "URL · DOM 状态 · 数据库", fill=C.purple_s, stroke=C.purple)
f.arrow(320, 280, 400, 280, "", C.soft)
f.arrow(600, 280, 680, 280, "", C.soft)
f.note(120, 350, "跨站任务的精髓: 「在 GitLab 找到同事给的 SKU, 去商城下单, 把订单号回帖到 CMS」")
f.note(120, 372, "— 单一站点做不出这类「信息搬运」任务, 跨站依赖是 WebArena 难度的真正来源", 11.5, C.indigo_d)
f.save("fig-webarena-arch")

# ---- fig 52-2: 表征方式对比 (DOM vs 截图 vs SoM) ----
f = F(940, 400)
f.text(470, 32, "GUI 的三种表征:模型「看到」什么", 18, C.ink, 800)
# DOM
f.box(50, 80, 260, 240, "DOM 树 / aXTree", None, fill=C.white, stroke=C.indigo)
f.text(180, 108, "DOM 树 / aXTree", 13.5, C.indigo, 800)
for i, ln in enumerate(["[button] Add to cart", "[textbox] search…", "[link] Order #1234", "", "+ 语义精确, token 密集", "- 长页面爆炸, 截断即失明"]):
    f.text(180, 138 + i * 20, ln, 11, C.ink if ln and not ln.startswith(("+", "-")) else C.faint)
# 截图
f.box(340, 80, 260, 240, "截图", None, fill=C.white, stroke=C.amber)
f.text(470, 108, "截图", 13.5, C.amber, 800)
f.raw('<rect x="370" y="125" width="120" height="70" rx="4" fill="%s" stroke="%s"/>' % (C.gray_s, C.line))
f.raw('<rect x="500" y="125" width="70" height="24" rx="4" fill="%s" stroke="%s"/>' % (C.teal_s, C.teal))
for i, ln in enumerate(["", "+ 与人看到的界面一致", "+ 布局/视觉信息全", "- 小目标定位难", "- 高分辨率 token 贵"]):
    f.text(470, 215 + i * 20, ln, 11, C.ink if ln and not ln.startswith(("+", "-")) else C.faint)
# SoM
f.box(630, 80, 260, 240, "Set-of-Marks 标注", None, fill=C.white, stroke=C.purple)
f.raw('<rect x="660" y="125" width="120" height="70" rx="4" fill="%s" stroke="%s"/>' % (C.gray_s, C.line))
for cx, cy, n in [(680, 140, "1"), (710, 155, "2"), (745, 140, "3"), (695, 175, "4"), (760, 170, "5")]:
    f.badge(cx, cy, n, fill=C.purple, r=8, fs=10)
for i, ln in enumerate(["元素编号叠加在截图上", "+ 定位精准(报编号即可)", "+ VLM 与 DOM 各取所长", "- 标注管线要自维护"]):
    f.text(760, 215 + i * 20, ln, 11, C.ink if not ln.startswith("-") else C.faint)
f.note(470, 355, "演化主线: DOM(文本派) → 截图(视觉派) → SoM(混合) — 训练语料更偏 DOM, 视觉前端更偏截图, 生产 SoM 渐成默认", 11.5, C.faint, anchor="middle")
f.save("fig-gui-representation")

# ---- fig 52-3: OSWorld 层级 ----
f = F(940, 340)
f.text(470, 32, "OSWorld:从「一个网站」到「整个操作系统」", 18, C.ink, 800)
layers = [
    (110, 90, C.teal,   "单应用任务", "在 LibreOffice 里做表格 · Chrome 设置"),
    (330, 90, C.blue,   "跨应用任务", "邮件附件 → 存盘 → 在文档里引用"),
    (550, 90, C.indigo, "系统级任务", "改系统设置 · 装软件 · 管理文件"),
    (740, 90, C.purple, "真实用户环境", "个人配置与习惯 — 最难最真实"),
]
for x, y, colr, t, d in layers:
    f.box(x, y, 160, 90, t, None, fill=C.white, stroke=colr, fs=12)
    for i, ln in enumerate(d.split(" · ")):
        f.text(x + 80, y + 56 + i * 15, ln, 9.5, C.faint)
for i in range(3):
    f.arrow(270 + i * 220, 135, 330 + i * 220, 135, "", C.soft)
f.note(470, 240, "VM 快照做环境 (VirtualBox/VMware) — 判定用「设置检查器」: 截图、文件、系统状态的终态断言", 11.5, C.ink, anchor="middle")
f.note(470, 270, "OSWorld 的任务平均需要数十步交互 — 长程失败率是主要得分瓶颈, 也是它比 WebArena 更难的原因", 11.5, C.faint, anchor="middle")
f.note(470, 305, "对照: WebArena 考「站点内的信息工作」, OSWorld 考「作为电脑用户生存」— 两级真实度阶梯", 11.5, C.indigo_d, anchor="middle")
f.save("fig-osworld-layers")
