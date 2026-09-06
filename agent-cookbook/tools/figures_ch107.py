# -*- coding: utf-8 -*-
"""figures_ch107.py — ch107 智能体基准评测与验证平台工具链 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 107-1: 全球四大主流 Agent 评测基准多维能力空间
f = F(940, 420)
# 1. SWE-bench
f.box(40, 60, 200, 150, "1. SWE-bench (代码)\n• 真实 GitHub 缺陷工单\n• 跨多文件代码定位\n• 双向严格单测断言\n(软件工程唯一硬标尺)", fill=C.blue_s, stroke=C.blue)

# 2. WebArena
f.box(260, 60, 200, 150, "2. WebArena (网页)\n• 真实独立网站沙箱\n• 动态 DOM 逆向与交互\n• 复杂表单、点击、拖拽\n(网页浏览智能体金标)", fill=C.indigo_s, stroke=C.indigo)

# 3. GAIA
f.box(480, 60, 200, 150, "3. GAIA (通用助理)\n• 多模态混合复杂难题\n• 跨网页/PDF/音视频工具\n• 概念反思与逆向事实推演\n(通用全能 Agent 标杆)", fill=C.amber_s, stroke=C.amber)

# 4. AgentBench
f.box(700, 60, 200, 150, "4. AgentBench (全域)\n• 8 大跨异构环境沙箱\n• OS 终端、DB 数据库、博弈\n• 多轮对话与指令遵从\n(全景综合能力大考场)", fill=C.teal_s, stroke=C.teal)

# 底部评测流水线核心原则
f.box(80, 260, 780, 130, "工业级 Agent 持续评测三大铁律 (Evaluation Engineering Principles)\n• 沙箱完全物理隔离 (Containerized Isolation): 每一个测试任务必须在全新无污染的 Docker 容器内执行\n• 严格客观断言 (Deterministic Assertions): 坚决摒弃脆弱的主观 LLM-as-a-Judge 打分，100% 依据状态转移与单测返回值\n• CI/CD 自动化回归 (Automated Regression): 每次提示词修改或模型微调，自动触发黄金子集回归跑分防退化", fill=C.purple_s, stroke=C.purple)

f.save("fig-agent-benchmarks-quadrant")

# fig 107-2: 自动化评测判题驱动执行流水线
f = F(940, 350)
f.pill(120, 70, "测试集工单元数据", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 150, 180, 80, "1. 瞬时沙箱热拉起\nDocker run 隔离容器\n挂载目标历史仓库/网站", fill=C.indigo_s, stroke=C.indigo)
f.box(280, 150, 180, 80, "2. 智能体闭环交互\n下发自然语言任务\nAgent 执行工具与代码", fill=C.amber_s, stroke=C.amber)
f.box(500, 150, 180, 80, "3. 提取运行态补丁/状态\n获取 Git Diff 补丁\n或捕获网页数据库状态", fill=C.teal_s, stroke=C.teal)
f.box(720, 150, 180, 80, "4. 客观断言裁判\n执行单元测试脚本\nPASS / FAIL 判定", fill=C.green_s, stroke=C.green)

f.arrow(120, 95, 150, 150)
f.arrow(240, 190, 280, 190, "沙箱就绪")
f.arrow(460, 190, 500, 190, "交互完毕")
f.arrow(680, 190, 720, 190, "触发测试")

f.save("fig-eval-harness-pipeline")
print("ch107 figures generated successfully")
