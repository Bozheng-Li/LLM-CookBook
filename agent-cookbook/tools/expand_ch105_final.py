# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch105.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="framework-epistemology-summary">开源生态与框架选型的工程哲学：没有银弹，唯有适者生存</h2>
    <p>回顾计算机软件工程发展这几十年的漫长历史，从当年的 C/C++ 时代到后来的 Java Spring 生态，再到前端 Angular、React、Vue 的百团大战，技术框架的繁荣与更迭从来都遵循着一条残酷而冷酷的规律：<strong>世界上从来不存在一个能够解决所有问题的“银弹框架”；任何脱离具体业务场景与团队工程素养的盲目选型，最终都难逃重构重写的历史宿命。</strong></p>
    
    <p>开源 Agent 框架的爆发式涌现，不是简单的工具轮子重复制造，而是人类软件工程范式在拥抱非确定性大模型时所展现出的<strong>惊人自组织与适应性演化</strong>：LangGraph 代表了对控制确定性与系统状态严密性的极致追求；Dify 代表了将 AI 技术平民化、让业务人员成为超级创造者的中台普惠哲学；MetaGPT 代表了将人类百年工业管理智慧注入硅基代码的工程严谨精神；而 AutoGen 与 CrewAI 则代表了敏捷轻量、敢于在混沌中快速试错的黑客极客精神。</p>
    
    <p>作为一名身处大模型时代洪流中央的合格架构师，我们绝不应当沦为某一个特定框架的狂热信徒或精神门徒。真正的系统智慧，在于<strong>洞察每一个框架底层代码所封装的核心权衡与设计代价</strong>：在探索期用好 CrewAI 的轻灵，在生产期用稳 LangGraph 的坚韧，在中台期用活 Dify 的宽广，在工程研发期用透 MetaGPT 的规整。不困于工具，不泥于表象，深深扎根于系统状态机、数据流图谱与业务本质的第一性原理之上，方能在这场波澜壮阔的智能体大革命中，构建起经得起时间与并发冲刷的传世工业系统！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch105.html")
else:
    print("Target not found")
