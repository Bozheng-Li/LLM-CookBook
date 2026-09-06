# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_5 = """
    <p>它让每一位身处数字化时代前沿的开发者和架构师坚信：真正卓越的智能体系统，不仅能够在虚拟的对话框中侃侃而谈，更能在大规模工业级生产现实中乘风破浪、无畏前行！</p>
"""

insert_target = '<h2 id="software-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_5 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 5")
else:
    print("Target not found")
