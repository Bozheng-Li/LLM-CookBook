# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch110.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

deep_additions = """
    <h3>Q48: 生产环境下大模型经常出现输出截断（Max Tokens Exceeded），如何设计智能体的优雅断点续生机制？</h3>
    <p><strong>【核心考点】</strong>Finish Reason 状态捕获、滑动上下文拼接、AST 语法树自动修复与闭合补全。</p>
    <p><strong>【参考回答】</strong>当 API 返回的 <code>finish_reason</code> 为 <code>length</code> 时，表明当前输出因超出预设的 Token 阈值被系统强行截断。若直接将残缺内容丢弃并重新请求，将造成昂贵的 Token 浪费并剧烈增加端到端等待延迟。工业级自愈设计方案分为三步：① <strong>首尾状态捕获</strong>：捕获已被截断的局部生成文本，判定其最后截断点的语法状态（如是否处于 JSON 字符串引号内、数组中括号未闭合或代码函数体内部）；② <strong>递归单步续生提示（Continuation Prompting）</strong>：将已生成的残缺片段作为 Assistant 消息的历史前缀压回上下文，构造极其精简的引导词（如“系统检测到输出被截断，请紧接上述内容最后一句继续生成，严禁重复输出已完成部分”），驱动大模型以自回归贪婪方式仅补齐后续未尽部分；③ <strong>确定性拼接与 AST 校验</strong>：在内存缓冲区中执行无缝拼接，并通过静态分析解析器校验完整性。若仅缺失尾部闭合中括号或大括号，则直接在网关层通过确定性算法补全，避免触发不必要的额外推理调用。</p>

    <h3>Q49: 如何度量智能体在离线与线上生产环境中的“任务达成率（Task Success Rate）”？</h3>
    <p><strong>【核心考点】</strong>端到端任务成功率、轨迹有效性比率（Trajectory Efficiency）、单步决策确定性矩阵。</p>
    <p><strong>【参考回答】</strong>评估一个工业级 Agent 绝不能仅靠大模型裁判（LLM-as-a-Judge）打出一个主观分数，必须建立一套融合了客观状态断言与执行开销的多维量化度量坐标系：① <strong>环境状态硬断言（State Change Assertion）</strong>：判定智能体执行完毕后，外部真实系统的状态是否发生预期变更（如数据库中订单状态是否更新为已支付、Git 仓库中测试套件是否 100% 通过、文件系统中目标报告是否生成且格式合法），这是衡量任务成功的最高黄金法则；② <strong>轨迹效率比（Trajectory Efficiency Ratio, TER）</strong>：计算最优专家路径步数与智能体实际执行步数之比 $TER = \frac{N_{optimal}}{N_{actual}}$，用于量化智能体在探索过程中存在的无效试错与循环冗余；③ <strong>单步工具调用精准度（Step-level Precision & Recall）</strong>：统计智能体在每一步选择工具的准确率、参数提取的完备率与解析错误率，为系统的针对性调优提供细粒度的可解释归因依据。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, deep_additions + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added deep additions to ch110")
else:
    print("Target not found")
