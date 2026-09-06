import os

path = r"D:/agent-cookbook/chapters/ch087.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <p>总而言之，全栈 Web 前端开发与 GUI 测试 Agent 的核心工程价值，不仅在于大幅解放了人类前端工程师在重复排版与繁琐样板代码上的精力消耗，更在于将「视觉感知、代码生成、即时编译与自动化像素级验收」彻底融为一体。它不仅是高产的代码生成器，更是一名不知疲倦、火眼金睛的自动化质量守门员，为现代敏捷软件工程注入了前所未有的高确定性与高交付水准。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final conclusion push")
else:
    print("Target not found")
