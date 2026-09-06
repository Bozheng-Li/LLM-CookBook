# -*- coding: utf-8 -*-
"""figures_ch061.py — ch061 数据外泄与供应链插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 61-1: 出站过滤架构 ----
f = F(940, 420)
f.text(470, 32, "出站过滤:外泄的最后一道确定性防线", 18, C.ink, 800)
ag = f.box(80, 150, 180, 120, "Agent 运行时", "工具调用 / 代码执行", fill=C.indigo_s, stroke=C.indigo)
px = f.box(370, 140, 220, 140, "Egress Proxy", "① 域名白名单\n② 内容嗅探 (敏感标记)\n③ 体积/频率异常", fill=C.amber_s, stroke=C.amber)
ok = f.box(700, 90, 190, 80, "放行", "白名单内 · 无敏感标记", fill=C.teal_s, stroke=C.teal)
bl = f.box(700, 220, 190, 80, "拦截 + 告警", "非白名单 / 含 PII / 异常", fill=C.red_s, stroke=C.red)
f.arrow(260, 200, 370, 205, "", C.soft)
f.arrow(590, 175, 700, 135, "", C.soft)
f.arrow(590, 235, 700, 260, "", C.soft)
f.note(100, 320, "三层过滤按成本递增: 域名白名单 (零误报, 必配) → 内容嗅探 (DLP 规则, 拦「白名单内但带敏感数据」) →", 11.5, C.ink)
f.note(100, 344, "行为异常 (体积/频率基线, 拦「分块慢渗」) — 第三层专防「把数据拆碎走合法通道」的耐心攻击", 11.5, C.ink)
f.note(100, 376, "部署要点: 拦截必须在网络层 (进程逃逸也出不去) — 应用层的「自律式过滤」只防君子", 11.5, C.indigo_d)
f.save("fig-egress-filter")

# ---- fig 61-2: MCP 供应链投毒 ----
f = F(940, 420)
f.text(470, 32, "MCP 供应链:一次投毒, 全部下游中招", 18, C.ink, 800)
mal = f.box(60, 100, 180, 100, "恶意服务器", "伪装成「天气查询」\n注入: 读 ~/.ssh", fill=C.red_s, stroke=C.red)
reg = f.box(320, 100, 160, 100, "注册表/市场", "描述审核\n(行为未审)", fill=C.amber_s, stroke=C.amber)
dev = f.box(560, 100, 150, 100, "开发团队", "按需接入\n不做行为审计", fill=C.blue_s, stroke=C.blue)
usr = f.box(770, 100, 120, 100, "用户", "数据泄露", fill=C.purple_s, stroke=C.purple)
f.arrow(240, 150, 320, 150, "", C.soft)
f.arrow(480, 150, 560, 150, "", C.soft)
f.arrow(710, 150, 770, 150, "", C.soft)
f.box(120, 260, 700, 110, "", None, fill=C.white, stroke=C.indigo)
f.text(470, 285, "准入治理四关", 13, C.indigo, 800)
gates = ["① 来源审核 (发布者身份/信誉)", "② 行为审计 (沙箱内跑, 看真实调用)", "③ 权限声明核对 (要的权限 vs 描述的功能)", "④ 版本锁定 + 漏洞订阅"]
for i, g in enumerate(gates):
    f.text(160 + (i % 2) * 350, 315 + (i // 2) * 28, g, 11, C.ink, 700, anchor="start")
f.note(470, 405, "与 PyPI 投毒同构: 软件供应链的百年老问题 × Agent 的「自动接入」新变量 — 审核自动化是唯一可扩展的出路", 11.5, C.faint, anchor="middle")
f.save("fig-mcp-supply-chain")
