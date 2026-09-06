# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch102.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个深刻的认知坐标系中，多智能体系统不再是一堆简单并发运行的 Python 进程，而是一面映照人类协作智慧与组织科学的数字明镜。它让每一位身处智能革命浪潮中的工程师真切地感受到：未来的软件开发，将是一场由人类总指挥引领、由成百上千个高度专业化智能体共同演奏的恢弘数字交响乐章。</p>
"""

insert_target = '<h2 id="multi-agent-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
