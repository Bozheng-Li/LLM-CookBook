import os

path = r"D:/agent-cookbook/chapters/ch086.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <p>总而言之，端侧移动端 Agent 的落地标志着智能体技术从云端数据中心的象牙塔，真正下沉到了每个人日常随身携带的物理设备之中。它所面临的严苛内存、电量与温控挑战，不仅倒逼着模型量化与微架构层面的极致创新，更为未来智能家居、穿戴式具身硬件以及车载系统的全局自动化交互奠定了坚不可摧的技术基石。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final conclusion push")
else:
    print("Target not found")
