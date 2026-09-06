import os

path = r"D:/agent-cookbook/chapters/ch088.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <p>总而言之，AI 驱动的渗透测试与红蓝对抗 Agent 的本质绝不是制造新的攻击武器，而是通过前沿智能体技术的自动化与深度推理能力，将原本极其依赖极少数顶级安全白帽黑客的稀缺攻防能力，全面普惠并平民化为所有企业均可低成本常态化运行的数字安全疫苗系统。通过不知疲倦地探索脆弱性、即时验证与自动加固闭环，构建真正具备免疫自愈能力的次世代可信软件基础设施。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final conclusion push")
else:
    print("Target not found")
