# -*- coding: utf-8 -*-
"""figures_ch101.py — ch101 代码生成、仓库演进与工具调用核心论文研读 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 101-1: 工具调用与代码工程三大里程碑演进全景
f = F(940, 420)
# 1. Toolformer
f.box(40, 60, 260, 150, "1. 自主工具自学习: Toolformer\nSchick et al. (Meta 2023)\n• 自监督自举合成 API 标记\n• 困惑度过滤 (Perplexity Filtering)\n• 首创将 API 视为普通文本 Token", fill=C.blue_s, stroke=C.blue)

# 2. Gorilla
f.box(340, 60, 260, 150, "2. 开放 API 检索调用: Gorilla\nPatil et al. (UC Berkeley 2023)\n• 检索感知微调 (Retriever-Aware SFT)\n• 彻底攻克 API 幻觉与参数错乱\n• 适配快速变化的云端生态", fill=C.indigo_s, stroke=C.indigo)

# 3. SWE-bench
f.box(640, 60, 260, 150, "3. 真实软件工程基准: SWE-bench\nJimenez et al. (Princeton 2024)\n• 2,294 个真实 GitHub 生产 Issue\n• 双向严格回归断言 (Fail-to-Pass)\n• 成为全球 Coding Agent 黄金试金石", fill=C.teal_s, stroke=C.teal)

# 底部演进核心线索
f.box(100, 260, 740, 130, "工具使用与软件工程的三重技术跃迁 (Technological Paradigm Shifts)\n• 从被动调用到自发自学 (Toolformer): 突破人为编写 Few-Shot 限制，模型自发学会何时、调用何种工具降低交叉熵损失\n• 从记忆孤立到动态检索适配 (Gorilla): 解决数千个快速迭代外部 API 的长尾参数匹配难题，消除 API 幻觉\n• 从玩具刷题到真实工业代码重构 (SWE-bench): 告别单函数补全，跨入包含多文件定位、Git Diff 补丁与测试自愈的真工程时代", fill=C.amber_s, stroke=C.amber)

f.save("fig-tool-code-papers-evolution")

# fig 101-2: Toolformer 自监督自举学习流水线
f = F(940, 360)
f.box(40, 90, 200, 160, "1. 启发式采样 API 候选\n输入原始普通文本\n采样生成嵌入式调用语法\n`[Calculator(24 * 7)]`\n(自举产生海量候选标记)", fill=C.blue_s, stroke=C.blue)

f.box(270, 90, 200, 160, "2. 物理执行并获取回显\n真实调用外部计算器/API\n将返回值填入文本尾部\n`[Calculator(24 * 7) -> 168]`\n(外部工具提供确定性结果)", fill=C.indigo_s, stroke=C.indigo)

f.box(500, 90, 210, 160, "3. 困惑度增益过滤 (PPL)\n计算包含 API 前后的损失差值:\nL(带API) < L(无API) - threshold\n仅当工具显著降低后续损失时\n保留该样本进入训练集", fill=C.amber_s, stroke=C.amber)

f.box(740, 90, 160, 160, "4. 最终标准 SFT\n在优质微调集上\n微调基座大模型\n自主涌现工具调用", fill=C.green_s, stroke=C.green)

f.arrow(240, 170, 270, 170)
f.arrow(470, 170, 500, 170)
f.arrow(710, 170, 740, 170)

f.save("fig-toolformer-bootstrap-pipeline")
print("ch101 figures generated successfully")
