import os

path = r"D:/agent-cookbook/chapters/ch089.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个演进过程中，具身桌面智能体与企业内部身份治理系统（IAM）的结合，更让组织能够像管理真实人类员工一样，为每一个 Agent 分配专属的单点登录凭据、权限作用域与离散操作行为审计看板。具身操作系统 Agent 正在成为未来数字化企业组织架构中最具弹性的弹性劳动力底座。</p>
"""

insert_target = '<h2 id="production-readiness">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added IAM integration paragraph")
else:
    print("Target not found")
