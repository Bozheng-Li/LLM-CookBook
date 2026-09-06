import os

path = r"D:/agent-cookbook/chapters/ch089.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>与此同时，基于多模态时空图谱的自我监督回放机制，更让具身智能体能够像熟练工一样，通过不断观摩人类专家的桌面操作录屏录像，自主提炼出高频复合操作快捷工作流，持续迈向更高层次的自动化与自主演进。</p>
"""

insert_target = '<h2 id="production-readiness">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added video imitation paragraph")
else:
    print("Target not found")
