import os

path = r"D:/agent-cookbook/chapters/ch088.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个演进过程中，红蓝对抗 Agent 还在云原生 Kubernetes 集群与微服务 Service Mesh 架构中落地了动态旁路流量镜像（Traffic Mirroring）与金丝雀沙盒引流机制。这保证了哪怕是最激进的非破坏性利用探测，也仅在完全隔离的无状态金丝雀 Pod 副本中触发，与正在承载真实用户订单的主干容器组实现物理层面的绝对绝缘。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
