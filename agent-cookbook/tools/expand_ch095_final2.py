# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个深刻的认知视界中，世界模型不仅为单智能体提供了强大的反事实推理能力，更为多智能体协作与对抗博弈构建了全真的数字孪生演练场。从虚拟经济系统的宏观调控模拟，到复杂物理环境中的多机协同作战，潜空间动力学正在重塑我们理解复杂系统与控制未来的根本方式。</p>
"""

insert_target = '<h2 id="world-model-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
