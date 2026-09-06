# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个深刻的认知视界之下，软件工程不仅是一套技术栈，更成为了一种测试与锤炼人工智能是否真正掌握因果逻辑与现实世界复杂性的终极竞技场。一个能够自主在多文件、多模块、动态运行态中穿梭自如的代码 Agent，其内在心智模型已经完成了对抽象符号世界与物理数字环境的完全对齐与深度贯通。</p>
"""

insert_target = '<h2 id="software-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
