# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="world-model-epistemology-summary">世界模型的认识论跃迁：从机械反射到因果心智的彼岸</h2>
    <p>回顾从行为主义（Behaviorism）到认知主义（Cognitivism）的百年科学演进，我们清晰地看到了一条从「刺激-反应（Stimulus-Response）」到「内部心智表征（Mental Representation）」的伟大飞跃。传统的无模型强化学习与简单的自回归单前向预测，在物理本质上依然停留在行为主义的反射阶段；而世界模型的诞生，真正宣告了人工智能迈入了认知心智的成熟期。</p>
    
    <p>通过在本章将递归状态空间模型（RSSM）的确定性-随机性双轨状态方程、变分证据下界（ELBO）的数学推导、Dreamer 系列从连续高斯到离散分类的代际演化、以及 Symlog 仿射缩放与双热编码的数值稳定性突破熔为一炉，我们实际上为智能体构筑了一座<strong>永恒运转于潜空间深处的因果推演沙盒</strong>。智能体无需肉身涉险，便能在纯粹的心灵潜空间中穷尽万千可能，在瞬息之间完成跨越物理时空的战略决断。这一理论基石，不仅为自动驾驶、具身机器人与通用电脑控制扫清了样本效率的终极障碍，更点亮了通用人工智能迈向因果推理圣殿的璀璨火炬。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology summary to ch095.html")
else:
    print("Target not found")
