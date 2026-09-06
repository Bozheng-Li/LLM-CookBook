# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 图 112-1: 工业级 Deep Research 深度研报 Agent 架构设计全景
f = F(940, 420)
f.box(40, 50, 240, 150, "1. 意图分解与假设树规划\n• 目标语义解构与多轮澄清\n• 树状探索假说生成 (Depth<=3)\n• 广度与深度优先动态切换\n• 停机启发式准则与预算熔断", fill=C.blue_s, stroke=C.blue)
f.box(340, 50, 260, 150, "2. 多通道搜网与信度加权\n• Google / Bing / arXiv 并发抓取\n• 网页清洗与 DOM 节点语义过滤\n• 贝叶斯信度更新与交叉盲审\n• 冲突事实检测与真理发现算法", fill=C.indigo_s, stroke=C.indigo)
f.box(640, 50, 260, 150, "3. 事实黑板与动态增量聚合\n• 事实原子 (Fact Atoms) 向量外挂\n• 全局 Blackboard 协同记忆\n• 去重、实体对齐与知识图谱\n• 章节结构化大纲动态扩展", fill=C.teal_s, stroke=C.teal)

f.arrow(280, 125, 340, 125, color=C.blue)
f.arrow(600, 125, 640, 125, color=C.indigo)

f.box(80, 250, 780, 140, "4. 章节流式合成与可信引文溯源校验 (Hierarchical Synthesis & Grounding)\n• Section-by-Section 模块化长文本装配流水线 (Map-Reduce 范式)\n• 零幻觉引文锚定校验器 (Strict Grounding Assertion & URL Ping)\n• 格式渲染引擎 (PDF, Markdown, LaTeX 与交互式图表集成)\n• 自动化质检评判 (LLM-as-a-Judge 忠实度与覆盖度评分门禁)", fill=C.purple_s, stroke=C.purple)

f.arrow(160, 200, 160, 250, color=C.blue)
f.arrow(470, 200, 470, 250, color=C.indigo)
f.arrow(770, 200, 770, 250, color=C.teal)

f.save("fig-deep-research-sys-design")
print("Saved fig-deep-research-sys-design.svg")

# 图 112-2: 企业级 Repo Coding Agent 核心执行状态机拓扑
f2 = F(940, 360)
f2.box(40, 50, 190, 260, "代码仓库全景感知\n\n• AST 语法树解析 (Tree-sitter)\n• 符号拓扑调用图 (Call Graph)\n• PageRank 仓库核心骨架提取\n• 模糊检索与语义 Embedding 索引", fill=C.gray_s, stroke=C.line)
f2.box(260, 50, 200, 260, "故障定位与补丁合成\n\n• Ripgrep 精准行级正则匹配\n• 故障上下文切片 (Context Slice)\n• 严格 Search/Replace 补丁块\n• 静态类型分析 (mypy/ruff) 门禁", fill=C.blue_s, stroke=C.blue)
f2.box(490, 50, 200, 260, "物理沙箱隔离回归\n\n• Git Worktree 分支瞬时快照\n• Docker / gVisor 隔离沙箱环境\n• 自动化执行 pytest / ctest\n• 捕获 Traceback 失败自愈循环", fill=C.amber_s, stroke=C.amber)
f2.box(720, 50, 180, 260, "代码审查与交付归档\n\n• FAIL_TO_PASS 靶向断言验证\n• PASS_TO_PASS 防劣化基准\n• 生成 Conventional Commit\n• 自动化发起 Pull Request", fill=C.green_s, stroke=C.green)

f2.arrow(230, 180, 260, 180, color=C.indigo)
f2.arrow(460, 180, 490, 180, color=C.amber)
f2.arrow(690, 180, 720, 180, color=C.green)

f2.save("fig-coding-agent-sys-design")
print("Saved fig-coding-agent-sys-design.svg")
