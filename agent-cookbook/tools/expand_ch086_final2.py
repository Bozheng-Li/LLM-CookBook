import os

path = r"D:/agent-cookbook/chapters/ch086.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个演进过程中，端侧隐私沙箱（On-Device Privacy Sandbox）与硬件级安全飞地（TEE, Trusted Execution Environment）的结合，更让用户能够百分之百放心地将生物识别认证、私密通讯与资产账户托付给本地智能体。端侧 Agent 正在重新定义下一代个人数字助手的人机契约。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final conclusion push 2")
