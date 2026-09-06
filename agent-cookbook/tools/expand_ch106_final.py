# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch106.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="model-selection-epistemology">基础大模型选型的工程认识论：驾驭算力巨浪的理性之锚</h2>
    <p>回顾从蒸汽机、电力到内燃机的历次工业革命史，任何一项通用目的技术（GPT）要想真正从实验室的轰动演示，转化为推动整个人类社会生产力飞跃的坚固巨轮，其核心转折点永远不在于制造出世界上最庞大昂贵的那台巨兽，而在于如何通过精益的工业标准化、流水线解耦与成本优化，让这项技术以普惠、廉价、可靠的方式流淌进千家万户、润物细无声。</p>
    
    <p>基座大模型作为数字文明时代的“全新工业母机”，其选型过程绝不仅仅是一个简单的技术参数对比，更是一场融合了商业财务预算、数据主权安全、全球地缘合规与系统架构健壮性的宏大系统工程博弈。从 DeepSeek 凭借 MLA 架构对显存带宽物理极限的精妙突破，到阿里 Qwen 以全尺寸 Apache 开源生态对工业落地门槛的全面平民化；从 Meta LLaMA 汇聚全球开发者智慧的开放社区洪流，到 Anthropic Claude 与 OpenAI 在高维推理与多模态世界模拟上的巅峰探索——全球各大模型家族的竞相迸发，共同为人类智能体构筑起了前所未有的繁荣智慧森林。</p>
    
    <p>作为新时代的软件工程师与技术领袖，我们既要怀抱拥抱一切前沿 SOTA 的开放激情，更要坚守立足于业务现实与工程第一性原理的清醒理性。不随波逐流，不盲目崇拜，用分层路由驾驭算力洪峰，以红黄绿防线捍卫数据尊严。唯有如此，我们方能真正驭风破浪，在这场重塑人类文明组织形态的历史大浪潮中，打造出兼备巅峰智力与永恒商业生命力的伟大智能体系统！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch106.html")
else:
    print("Target not found")
