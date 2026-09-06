# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="software-engineering-epistemology">代码智能体的认识论跃迁：从自然语言符号到可执行计算实体的闭环</h2>
    <p>回顾从图灵机问世至今的计算机科学史，程序代码一直是人类为了在物理硅基芯片上精确表达数学逻辑而创造的最严谨、最冷酷的形式化符号体系。自然语言是模糊、多义且宽容的；而代码世界则是零容忍、非黑即白的——多一个分号、少一个缩进、错一个指针，整个系统就会毫不留情地轰然崩溃。</p>
    
    <p>长期以来，自然语言大模型一直被困在“只能产出概率文本、无法确认物理因果”的虚拟囚笼之中。而 Toolformer、Gorilla 与 SWE-bench 这三大开创性论著的最伟大贡献，正在于它们在<strong>「模糊的人类自然语言意图」</strong>与<strong>「绝对确定性的物理可执行代码世界」</strong>之间，架起了一座由自监督自举学习、检索感知类型约束与双向单元测试断言共同筑就的钢铁飞桥！</p>
    
    <p>当大语言模型不仅能“谈论”代码，更能在真实世界中自发“调用”工具、在动态云端中精准“匹配”接口、在百万行真实工程中自主“重构与修复”缺陷时，AI 实际上完成了从一个被动的“文本预测概率模型”，向一个真正拥有物理世界改造力、具备完整认知与行动闭环的<strong>「自主软件工程实体（Autonomous Software Engineering Entity）」</strong>的壮丽升华。这一跨越不仅彻底重塑了全球数十万亿美元软件产业的生产力格局，更指引着我们迈向能够自主开发下一代更强智能体的“智能自举演进（Recursive Self-Improvement）”历史转折点！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch101.html")
else:
    print("Target not found")
