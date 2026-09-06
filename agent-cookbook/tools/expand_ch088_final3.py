import os

path = r"D:/agent-cookbook/chapters/ch088.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>与此同时，基于密码学签名的全生命周期审计不可篡改存证，更为企业在面对外部监管与合规审计时提供了强有力的法律级合规支撑，使 AI 渗透与防御智能体真正成为数字化时代安全攻防的坚固守护者。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
