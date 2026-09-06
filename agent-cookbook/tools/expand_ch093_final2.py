import os

path = r"D:/agent-cookbook/chapters/ch093.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个演进过程中，多模态认知记忆外挂系统更将传统离散的文字问答，全面升级为包含物理时空连续轨迹的宏观全息图谱。无论是跨越数年的软件工程架构重构历史，还是跨越数十万公里的具身机器人导航探索轨迹，都将在统一的神经认知记忆坐标系中获得永恒的秩序与生命力。</p>
"""

insert_target = '<h2 id="memory-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
