# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch103.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="alignment-epistemology-summary">安全对齐的哲学认识论：为人机共生文明铸造永恒的伦理之锚</h2>
    <p>回顾普罗米修斯盗取天火的神话，科技的力量从来都是一把锋利无比的双刃剑。人工智能的迅猛崛起，赋予了人类历史上最接近神明造物主般的算力与创造力；然而，如果这种力量缺乏敬畏与约束，它所释放出的破坏力也将是灭顶之灾。正如著名计算机科学家维纳在《人有人的用处》中所告诫的：“我们将最好把控制机器的决定权保留在人类自己手中，否则我们将面临机器按照自己荒谬逻辑运转的无情反噬。”</p>
    
    <p>安全、对齐与治理，绝不是阻碍技术创新的沉重枷锁，而是确保人工智能这艘满载人类希望的宏伟巨轮，在狂暴的深海大洋中不致触礁沉没的<strong>永恒压舱之石</strong>。从 Anthropic 宪法原则对人类最高法典的致敬，到斯坦福 DPO 对数学极简与确定性的追求，再到微软零信任防御对现实世界恶意敌对的清醒审视，这一代科学大师们用无懈可击的代码与严谨的微积分定理，共同为人机共生的未来文明铸造了一座不可动摇的伦理之锚。它让每一位开发者铭记：我们所守护的，不仅是系统的一行行代码逻辑，更是整个人类文明在硅基时代得以从容安息、繁衍演进的终极尊严！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch103.html")
else:
    print("Target not found")
