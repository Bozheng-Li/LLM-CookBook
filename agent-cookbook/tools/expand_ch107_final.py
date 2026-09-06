# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch107.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="eval-engineering-epistemology">评测科学的工程认识论：客观检验尺度的理性之光</h2>
    <p>回顾从伽利略在比萨斜塔建立落体物理实验，到现代粒子物理学通过大型强子对撞机（LHC）捕捉希格斯玻色子的数百年科学探索史，人类科学大厦的每一寸拓荒与演进，从来都建立在<strong>「可证伪性（Falsifiability）」与「客观可精确度量（Reproducible Measurement）」</strong>的坚固铁律之上。缺乏客观实验度量的假说，哪怕数学包装得多么繁复华丽，最终都只能沦为空洞的哲学玄学；而唯有经受住严酷、冷酷且可无情复现的物理实验反复淬火检验的理论，才能成为照亮文明前进的永恒科学真理。</p>
    
    <p>在人工智能智能体系统的研发高潮中，构建一套标准化的基准评测平台工具链，正是整个技术体系走向成熟工业化阶段的最关键分水岭。从 SWE-bench 以真实开源仓库代码与双向单元测试断言筑起的软件工程试金石，到 WebArena 以全真多网站沙箱和数据库底层状态检查设立的多模态网页操作标杆；从 GAIA 汇聚人类最高专家智慧构建的复杂长程推理大考场，到 AgentBench 横跨八大异构沙箱环境的全域综合度量图谱——这一整套评测工具链的诞生与演化，彻底粉碎了过去靠主观经验打分、靠精心包装几个成功 Case 欺世盗名的行业乱象，为每一位求真务实的工程师装上了一双洞察系统真实边界的火眼金睛。</p>
    
    <p>作为新时代的智能体架构师与研发领军者，我们必须在内心深处对评测科学怀有最高的敬畏与严谨。不逃避测试红灯，不美化跑分缺陷，把自动化评测流水线作为代码合入生产主干的不可逾越的第一守门神。唯有在真实世界的残酷客观检验中经受住千百次严酷拷问的智能体系统，方能真正走出实验室的温室象牙塔，在波澜壮阔的数字化生产现实世界中乘风破浪、履险如夷！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology section to ch107.html")
else:
    print("Target not found")
