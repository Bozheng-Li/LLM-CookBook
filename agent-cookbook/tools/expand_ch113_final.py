# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch113.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_113 = """
    <h2 id="taxonomy-epistemology-philosophy">认知图谱认识论：从术语网络到高阶认知飞跃</h2>
    <p>人类学习任何一门复杂前沿科学的终极跃迁，本质上都是在脑海中建立一套<strong>抗干扰、自洽且高密度的概念拓扑图谱（Conceptual Topology）</strong>。孤立地记住 300 个名词没有任何工程生产力，唯有洞悉它们在底层数学约束、控制论边界与物理系统实现上的内在因果张力，才能在面对未知故障时展现出大师级的从容定力：</p>

    <ul>
      <li><strong>从离散概念到动力学状态转移：</strong>当你审视 MDP、POMDP 与 RSSM 时，不要将它们视为教科书上的抽象数学公式，而应清晰看到智能体在每个毫秒的隐状态空间中，是如何在环境观测的引导下利用贝叶斯滤波动态修正对外部客观世界的置信状态分布（Belief State）。</li>
      <li><strong>从单向提示到控制论负反馈闭环：</strong>当你编写 ReAct、Reflexion 与 Saga 补偿代码时，必须时刻牢记维纳（Wiener）在半个多世纪前为现代控制论奠定的第一公理——任何开环系统在复杂外部环境扰动下都必然走向失控与崩溃。正是代码中断言校验、环境 Observation 与逆向补偿构成的负反馈回路，才真正赋予了大模型抵抗混沌与熵增的永恒生命力。</li>
      <li><strong>从局部调优到全局安全微隔离：</strong>当你配置 gVisor 沙箱、Docker 容器隔离与 CaMeL 双模型架构时，永远不要心存侥幸依赖大模型的“听话与自觉”。在概率与非确定性的智能洪流之上，必须始终依托经典操作系统内核、硬件虚拟化与强类型编译契约，为人类数字资产筑起最森严坚固的绝对物理防线。</li>
    </ul>

    <p>至此，全书从第 1 章到第 113 章的宏伟认知画卷已彻底收拢为一幅浑然一体的智慧全景图。带着这 300 条权威路标所凝聚的真理火种，每一位工程师都将具备穿透技术营销迷雾、直抵系统本质的最强认知武装，在通用人工智能的壮阔时代浪潮中书写属于自己的传奇华章！</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, final_push_113 + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Final push applied to ch113")
else:
    print("Target not found")
