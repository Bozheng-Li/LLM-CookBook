# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>与此同时，基于端到端可微潜空间的世界模型，使得传统强化学习中脆弱不堪的策略梯度估算，一跃升级为具备解析全导数支持的高确定性梯度链。无论是应对极端复杂物理约束的机器人控制，还是跨越数千步长时程的软件重构与战略决策，世界模型都展现出了无与伦比的数学优雅与工程威能。</p>
"""

insert_target = '<h2 id="world-model-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
