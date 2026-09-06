# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="swe-bench-advanced-mechanisms">工程实操进阶：破解 SWE-bench 核心难关的五大前沿架构战法</h2>
    <p>在普林斯顿大学发表 SWE-bench 之后，全球顶尖实验室与大厂纷纷派出自研的代码智能体参与打榜角逐。在漫长而残酷的真机评测中，能够在真实开源代码仓库中斩获 40% 以上解决率的高阶系统（如 SWE-agent、Aider、AutoCodeRover），无一例外在底层实现了以下五项革命性的工程战法：</p>
    
    <p><strong>① 专门针对代码浏览的交互式命令行接口（Agent-Computer Interface, ACI）：</strong>传统的 Bash 终端交互对于大模型而言充斥着大量无用冗余输出（如一个 <code>ls</code> 或 <code>cat</code> 几千行的大文件会瞬间撑爆上下文）。前沿架构为 Agent 专门定制了一组精炼指令集：包含带行号的窗口化查看指令 <code>view_file(path, start_line, end_line)</code>、以及超高速正则定位命令 <code>search_dir(pattern)</code>，使大模型的注意力始终聚焦在最关键的代码窗口之内；</p>
    
    <p><strong>② 基于 AST 语法的最小侵入性精准编辑协议：</strong>如我们在第 84 章中所深入推导的，彻底摒弃全文件重写，严格推行 <code>SEARCH/REPLACE</code> 块替换协议。这使得单次编辑的 Token 消耗从上万个骤降至数百个，且大幅降低了因为语法缩进错位导致的编译失败率；</p>
    
    <p><strong>③ 动态单测生成与假阳性抑制：</strong>在修复复杂 Bug 前，高阶 Agent 会首先自主分析工单描述，编写一个能够稳定复现当前缺陷的最小复现测试脚本（Reproduction Script）。在执行补丁后，只有当复现脚本从红灯变为绿灯、且全库既有测试无一报错时，才允许打包提交 Git 补丁；</p>
    
    <p><strong>④ 跨多模块调用链图谱追踪：</strong>利用第 84 章的 Tree-sitter Repo Map 与 LSP 语言服务协议，在修改某个核心基类函数前，自动扫描全工程所有直接或间接调用该函数的下游代码段，实现联动无损重构，彻底解决“改好了一个地方，炸塌了另外八个模块”的经典悲剧；</p>
    
    <p><strong>⑤ 自动化 Git Worktree 隔离与多候选分支并行推演：</strong>面对极其棘手的深水区 Issue，单线推演极易陷入死胡同。顶尖系统同时检出 3 个相互物理隔离的 Git Worktree 沙箱，并发尝试不同的重构思路（例如思路 A 尝试修改底层数据库适配层，思路 B 尝试在上层业务做入参防御过滤）；经过沙箱回归测试后，挑选测试覆盖率最高、代码变动最少的方案作为最终 PR，实现了群智协同级的超凡稳定性。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added advanced SWE-bench mechanisms to ch101.html")
else:
    print("Target not found")
