# -*- coding: utf-8 -*-
"""figures_ch074.py — ch074 Coding Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 74-1: 三代 Coding Agent 演进 ----
f = F(940, 420)
f.text(470, 32, "Coding Agent 的三代跃迁: 从补全到全自主协作", 18, C.ink, 800)
gens = [
    (60, 100, 240, 240, "一代: Copilot 时代\n(2021-2023)", C.teal, [
        "模式: 行级/函数级单步续写",
        "上下文: 当前光标周围片区",
        "操作: 仅生成文本代码",
        "验证: 人工肉眼核对/编译",
        "",
        "定位: 智能打字机 / 效率插件",
        "局限: 无项目级感知，零执行权"
    ]),
    (350, 100, 240, 240, "二代: Devin 时代\n(2024 初)", C.amber, [
        "模式: Issue 到 PR 端到端处理",
        "上下文: 仓库代码检索 + 终端日志",
        "操作: 编辑文件 + 跑 Shell 编译",
        "验证: 自动化测试套件判分",
        "",
        "定位: 虚拟初级工程师 (PR 生成器)",
        "局限: 幻觉绕圈，成本不可控"
    ]),
    (640, 100, 240, 240, "三代: Claude Code / CLI 时代\n(2024 末-2025)", C.purple, [
        "模式: 终端原生、紧密人机双工",
        "上下文: 紧凑 AST/grep/编辑原语",
        "操作: 最小 diff 修改 + 编译反馈",
        "验证: 动态测试运行 + 本地回滚",
        "",
        "定位: 极速配对编程助手",
        "突破: 延迟极低、无缝融入既有工具链"
    ])
]
for x, y, w, h, t, colr, lines_ in gens:
    f.box(x, y, w, h, t.split("\n")[0] + " " + t.split("\n")[1], None, fill=C.white, stroke=colr, fs=13)
    for i, ln in enumerate(lines_):
        if ln == "": continue
        f.text(x + w/2, y + 54 + i * 17, ln, 10, C.indigo_d if "定位" in ln or "突破" in ln else C.ink)
f.note(470, 375, "演化本质: 从代码生成(文本输出)到闭环工程交互(读-搜-改-跑-修)的系统级跃进", 11.5, C.faint, anchor="middle")
f.save("fig-coding-agent-evolution")

# ---- fig 74-2: 测试驱动循环 (TDD loop) ----
f = F(940, 380)
f.text(470, 32, "Coding Agent 的测试驱动闭环 (Test-Driven Feedback Loop)", 18, C.ink, 800)
b1 = f.box(60, 120, 170, 110, "① 定位与复现", "检索故障代码\n编写最小失败测试", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(290, 120, 170, 110, "② 补丁修改", "最小 diff 精确替换\n保持既有架构风格", fill=C.teal_s, stroke=C.teal)
b3 = f.box(520, 120, 170, 110, "③ 本地运行验证", "执行 pytest / jest\n双闸检查 (51 章)", fill=C.amber_s, stroke=C.amber)
b4 = f.box(750, 120, 130, 110, "④ 提交 PR", "干净 git commit\n解释根因与方案", fill=C.purple_s, stroke=C.purple)
f.arrow(230, 175, 290, 175, "", C.soft)
f.arrow(460, 175, 520, 175, "", C.soft)
f.arrow(690, 175, 750, 175, "通过", C.teal)
f.elbow([(605, 230), (605, 300), (375, 300), (375, 230)], "测试失败: 解析堆栈报错与 diff, 重规划补丁 (限制 3-5 轮)", C.red, label_pos=1)
f.note(470, 350, "成功率的分水岭: 凡是具备「编写失败用例复现 Bug」能力的 Agent，最终代码修复正确率提高 2.8 倍", 11.5, C.red, anchor="middle")
f.save("fig-coding-agent-tdd")
