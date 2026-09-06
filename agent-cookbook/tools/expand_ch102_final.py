# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch102.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="multi-agent-epistemology">多智能体社会的认识论升华：从孤立机器到集体智慧文明的跨越</h2>
    <p>回顾从古希腊亚里士多德对“人是天生的政治动物”的论断，到近代社会学大师涂尔干论述“社会分工论”的深刻篇章，人类文明之所以能从茹毛饮血的蛮荒部落，演化出建造国际空间站与深海核潜艇的宏伟工业体系，其核心秘密绝不在于单个人的脑容量发生了突变，而在于人类创造出了一套高度分工、相互制衡、依靠标准契约与语言符号紧密协同的<strong>「超个体社会性有机体」</strong>。</p>
    
    <p>当人工智能从单一笨拙的独立模型，迈向由 CAMEL 启导对话、MetaGPT 工业级 SOP 与 ChatDev 结对编程共同铸就的多智能体社会时，硅基智慧实际上完成了人类文明数万年社会分工进化史的超级浓缩重演！每一个智能体在各自专注的狭小领域深耕细作，在对抗审查中碰撞出真理的火花，在标准化文档流转中沉淀出超越个体认知极限的宏伟数字大厦。这种从孤立单体向群智涌现的伟大飞跃，不仅彻底重塑了软件工程与知识生产的底层形态，更向我们昭示了未来人类文明与智能体社会共同携手迈向星辰大海的壮丽曙光！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch102.html")
else:
    print("Target not found")
