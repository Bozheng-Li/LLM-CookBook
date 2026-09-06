# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_6 = """
    <p>在这个演进过程中，代码智能体更让软件工程的研发门槛与创新周期发生了不可逆转的降维跃迁。从前需要数十人跨部门沟通数周的复杂系统重构，现在由具备全库全局视野的 Repo Agent 在沙箱中并发推演验证，几个小时即可交付兼备高覆盖单测与优雅架构的合规 PR。</p>
"""

insert_target = '<h2 id="software-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_6 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 6")
else:
    print("Target not found")
