# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch104.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="embodied-epistemology-summary">第十一部分论文研读篇终章献辞：从象牙塔真理到重塑物理现实的磅礴伟力</h2>
    <p>回顾我们刚刚完整走过的第十一部分（必读论文研读篇，第 99 章至第 104 章）这波澜壮阔的六大篇章：从《Attention Is All You Need》与《ReAct》拉开自注意力与工具闭环的开天辟地大幕（第 99 章）；到《Tree of Thoughts》与《MemGPT》解开高维规划与分层虚拟内存的思维锁钥（第 100 章）；从《Toolformer》与《SWE-bench》攻克代码自举与真实软件工程重构的工业铁律（第 101 章）；到《CAMEL》、《MetaGPT》与《ChatDev》见证多智能体自发社会性分工涌现的文明奇迹（第 102 章）；从《Constitutional AI》与《DPO》铸造人类崇高价值的永恒伦理之锚（第 103 章）；直至本章《PaLM-E》、《RT-2》与《Sora》宣告硅基智能真正长出观察时空的眼睛与改造物质世界的手足（第 104 章）——整整二十余篇改变人类科技历史航向的殿堂级原著，在此完成了壮丽的学术大合流！</p>
    
    <p>正如近代科学哲学大师培根（Francis Bacon）所断言：“知识的力量不仅在于解释世界，更在于重塑世界。”这六大专题论文的全部精髓，绝非陈列在图书馆供人膜拜的静止符号，而是正在以前所未有的加速度，转化为全球数千万行正在运行的生产级代码、操纵着数以万计的工业机械臂、重塑着人类社会的生产力组织形态。掌握了这些经过历史大浪淘沙检验的第一性原理，我们便拥有了穿透一切虚妄工业营销迷雾、在波澜壮阔的通用人工智能新纪元中永远从容远航的定海神针！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch104.html")
else:
    print("Target not found")
