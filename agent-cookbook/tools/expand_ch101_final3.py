# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>与此同时，基于契约驱动与静态类型系统的形式化辅助编译，更为代码生成大模型筑牢了防止语法越界与逻辑坍塌的刚性外骨骼。无论是面对分布式系统的并发竞态漏洞，还是现代 Web 微服务的复杂异步回调，代码智能体都展现出了前所未有的工业级稳健性与自愈威能。</p>
"""

insert_target = '<h2 id="software-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
