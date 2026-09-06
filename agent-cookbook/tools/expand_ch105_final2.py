# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch105.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个日新月异的技术浪潮中，框架的代码行数每天都在激增，各类封装库的 API 接口每年都在发生破坏性变更。但无论表层的代码语法如何翻新，底层的马尔可夫决策过程、控制论负反馈机制与分布式状态一致性原理却历久弥新、永恒不灭。</p>
"""

insert_target = '<h2 id="framework-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
