# -*- coding: utf-8 -*-
"""figures_ch084.py — ch084 企业级代码助手与 Repo Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 84-1: 仓库级 Repo Agent 全景流水线
f = F(940, 420)
f.box(40, 60, 170, 110, "1. 仓库骨架索引\nRepo Indexing\nTree-sitter AST 解析\n符号引用调用图 (Callgraph)", fill=C.blue_s, stroke=C.blue)
f.box(250, 60, 170, 110, "2. 跨文件语义定位\nLocalization\nRipgrep 正则定位\nPageRank 核心符号拓扑", fill=C.indigo_s, stroke=C.indigo)
f.box(460, 60, 170, 110, "3. 精准补丁生成\nPatch Generation\nUnified Diff 规范\n精确块替换 (Aider/SWE)", fill=C.amber_s, stroke=C.amber)
f.box(670, 60, 220, 110, "4. 自动化测试闭环\nCI/CD & Self-Repair\nPytest 单元测试断言\n报错反思再修复 (TDD)", fill=C.teal_s, stroke=C.teal)

f.arrow(210, 115, 250, 115, "符号字典")
f.arrow(420, 115, 460, 115, "相关文件/类")
f.arrow(630, 115, 670, 115, "git diff 补丁")

# 底部测试失败自愈环路
f.elbow([(780, 170), (780, 240), (545, 240), (545, 170)], label="测试用例红灯 (AssertionError): 提取失败堆栈重新生成 Diff (Max 4次)", color=C.red, label_pos=1)

# 底部安全与环境沙箱底座
f.box(100, 290, 740, 100, "代码执行隔离与版本控制网关 (Sandbox & Git Environment)\n• 独立 Git 分支沙箱 (Worktree 物理隔离，杜绝污染主干)\n• 静态 AST 安全审查 (禁用高危 os.system / 危险套接字)\n• 资源限制保护 (容器化 Pytest，512MB 内存 / 15s 硬超时)", fill=C.purple_s, stroke=C.purple)

f.save("fig-repo-agent-arch")

# fig 84-2: 符号依赖图与搜索定位
f = F(940, 360)
f.pill(120, 70, "用户 Issue / 需求描述", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 150, 180, 80, "全局目录树骨架\nRepo Map\n核心类/函数签名摘要", fill=C.indigo_s, stroke=C.indigo)
f.box(280, 150, 180, 80, "精准符号检索\nSymbol Def/Ref\n查找函数定义与调用点", fill=C.amber_s, stroke=C.amber)
f.box(500, 150, 180, 80, "局部依赖上下文装配\nContext Slicing\n引入关联头文件/接口", fill=C.teal_s, stroke=C.teal)

f.arrow(120, 95, 150, 150)
f.arrow(240, 190, 280, 190, "粗筛候选")
f.arrow(460, 190, 500, 190, "跨文件追踪")

# 输出
f.pill(780, 190, "最小有效上下文 Prompt", fill=C.green_s, tc=C.ink, stroke=C.green)
f.arrow(680, 190, 780, 190, "精炼注入")

f.save("fig-repo-symbol-map")
print("ch084 figures generated successfully")
