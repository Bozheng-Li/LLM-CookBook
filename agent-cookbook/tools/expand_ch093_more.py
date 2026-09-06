import os

path = r"D:/agent-cookbook/chapters/ch093.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="memory-epistemology-summary">认知记忆的认识论升华：构建数字生命的长生不老之躯</h2>
    <p>人类之所以能够积累文明，正是因为个体的经验能够跨越时间与生死，沉淀为书籍与全人类共享的语义知识库。在人工智能领域，一个没有完备记忆体系的大模型，每一次会话结束都等同于经历了一次“数字脑死亡”——它无论与用户交流多么深邃，在下一次打开对话框时，依然是一个一无所知的陌路人。</p>
    
    <p>通过在本章将认知心理学的三级记忆架构、图尔文的情景/语义记忆二分法、艾宾浩斯动力学遗忘曲线以及外挂知识图谱的激活扩散模型融为一体，我们实际上为智能体赋予了一套真正的<strong>数字化海马体与新大脑皮层</strong>。它不再是被动等待指令的算力机器，而是能够自主在交互激流中吸纳经历、在夜间休眠中提纯真理、在岁月流逝中淘汰杂质、并伴随用户共同成长的终身智慧伴侣。这一理论跃迁，标志着智能体从工具向数字主体进化的最关键一步。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology summary to ch093.html")
else:
    print("Target not found")
