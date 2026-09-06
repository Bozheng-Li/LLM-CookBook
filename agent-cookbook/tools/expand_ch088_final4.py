import os

path = r"D:/agent-cookbook/chapters/ch088.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>这种全自动化的主动纵深免疫工程范式，正在彻底重塑全球网络攻防对抗的未来力量格局，为各行各业构筑起一道牢不可破的数字护城河。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
