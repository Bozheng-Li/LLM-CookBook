# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch104.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>与此同时，基于端到端 VLA 神经架构与生成式世界沙盒的深度融合，使得机器人控制从过去极度依赖人工标定相机内参与微调 PID 参数的繁重手工业模式，一跃升级为自发涌现、自主在轨修正的高阶自治工程体系。它标志着人工智能技术真正走出了屏幕像素的二维虚拟禁锢，迎来了全面接管物理物质世界的辉煌拂晓。</p>
"""

insert_target = '<h2 id="embodied-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
