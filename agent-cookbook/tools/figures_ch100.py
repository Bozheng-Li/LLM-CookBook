# -*- coding: utf-8 -*-
"""figures_ch100.py — ch100 规划、记忆与长上下文核心论文研读 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 100-1: 规划与长记忆三大标杆论文认知矩阵
f = F(940, 420)
# 1. Tree of Thoughts (ToT)
f.box(40, 60, 260, 150, "1. 思维树 Tree of Thoughts (ToT)\nYao et al. (2023)\n• 广度优先 (BFS) / 深度优先 (DFS)\n• 启发式局部剪枝与回溯\n• 突破单向自回归贪心思维瓶颈", fill=C.blue_s, stroke=C.blue)

# 2. MemGPT
f.box(340, 60, 260, 150, "2. 操作系统级记忆 MemGPT\nPacker et al. (2023)\n• 分层虚拟内存管理 (OS Paging)\n• 主上下文 (RAM) vs 外部归档 (Disk)\n• 自主产生 Function Call 换页", fill=C.purple_s, stroke=C.purple)

# 3. AgentBench
f.box(640, 60, 260, 150, "3. 通用智能体基准 AgentBench\nLiu et al. (2023)\n• 8 大跨域复杂交互环境\n• OS、DB、Web、KG、代码与对抗\n• 首次标准化度量 Agent 综合决策力", fill=C.teal_s, stroke=C.teal)

# 底部连接与演进线索
f.box(100, 260, 740, 130, "认知规划、分层记忆与评测度量三位一体 (Cognitive Triad)\n• 树状搜索攻克非平凡规划: ToT 将经典图论搜索与启发式剪枝植入思维链，解开 24 点等 NP 难题\n• 虚拟内存机制突破物理视界: MemGPT 借鉴现代 OS 换页中断协议，以有限 Context 实现无限生命周期运转\n• 标准化多维实境检验标尺: AgentBench 告别死板静态选择题，开创具身沙箱与真实交互综合评估新纪元", fill=C.amber_s, stroke=C.amber)

f.save("fig-planning-memory-papers")

# fig 100-2: MemGPT 操作系统分层内存调度流水线
f = F(940, 350)
f.box(60, 90, 240, 160, "主上下文 (Main Context / RAM)\n• 系统指令 System Instructions\n• 核心工作记忆 Working Memory\n• 活跃对话轮次 FIFO Buffer\n(处于 LLM 注意力直接观察区)", fill=C.indigo_s, stroke=C.indigo)

f.box(360, 90, 220, 160, "自发换页中断决策\nLLM Function Calling\n• core_memory_append\n• archival_memory_insert\n• conversation_search\n(智能体自主感知容量并换入/换出)", fill=C.amber_s, stroke=C.amber)

f.box(640, 90, 240, 160, "外部持久存储 (External / Disk)\n• 归档数据库 Archival Storage\n  (全量历史海量知识库向量)\n• 召回存储 Recall Storage\n  (过往所有会话日志明细)", fill=C.purple_s, stroke=C.purple)

f.arrow(300, 150, 360, 150, "容量将满换出")
f.arrow(360, 190, 300, 190, "按需线索换入")
f.arrow(580, 150, 640, 150, "写入归档")
f.arrow(640, 190, 580, 190, "向量召回")

f.save("fig-memgpt-os-paging")
print("ch100 figures generated successfully")
