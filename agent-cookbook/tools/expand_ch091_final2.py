import os

path = r"D:/agent-cookbook/chapters/ch091.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个理论视界之下，工程实践中遇到的所有疑难杂症——无论是强化学习微调中的奖励黑客攻击（Reward Hacking，第 43 章）、提示词注入导致的状态转移失控（第 59 章），还是多智能体死锁崩溃（第 85 章）——都不再是玄学玄奥的不可知之物，而是完全可以被精确定位为目标函数未对齐、马尔可夫状态被部分隐变量污染、或者策略偏离了纳什均衡边界的数学病态响应。</p>
"""

insert_target = '<h2 id="theory-summary-perspective">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
