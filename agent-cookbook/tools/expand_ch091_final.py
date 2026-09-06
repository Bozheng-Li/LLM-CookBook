import os

path = r"D:/agent-cookbook/chapters/ch091.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="theory-summary-perspective">哲学与形式化启示：从概率补全到理性主体的数学跃迁</h2>
    <p>回顾整个智能体形式化演进历程，我们清晰地看到了一条从直觉工程向公理化数学跃迁的壮阔轨迹：大语言模型原本仅仅是在海量语料上训练的无监督自回归分布 $P(w_t \mid w_{<t})$，但在赋予了状态、动作、转移核与奖励标量后，它瞬间升华为了一个符合冯·诺伊曼-摩根斯坦期望效用理论（vNM Utility Theorem）的<strong>理性行动主体（Rational Agent）</strong>。</p>
    
    <p>从贝尔曼压缩算子保证的单智能体全局最优收敛，到 POMDP 信念空间中贝叶斯滤波对物理迷雾的理性推断，再到随机博弈中多智能体纳什均衡与无悔学习对复杂群体动态的自发调谐，形式化理论为我们提供了一套超越具体代码框架的“上帝视角”。无论未来的基座模型如何迭代、上下文窗口如何膨胀，任何具备自治特性的智能系统，其底层的行为逻辑终究无法摆脱这套数学公理体系的终极引力。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added philosophical perspective section")
else:
    print("Target not found")
