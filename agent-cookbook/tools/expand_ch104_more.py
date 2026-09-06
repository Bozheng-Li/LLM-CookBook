# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch104.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="cross-paradigm-embodied-synthesis">具身三大论著的工程升华：构筑端到端物理世界自主实体</h2>
    <p>综合研读 PaLM-E、RT-2 与 Sora 这三大殿堂级文献，我们清晰地看到了一条从“高层跨模态通识理解”到“微观物理动作执行”，再到“全真时空环境因果模拟”的<strong>完整具身闭环宇宙图景</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>具身智能系统层级</th><th>核心学术论著支撑</th><th>技术实现与核心算法</th><th>在物理现实中实现的关键质跃</th></tr></thead>
        <tbody>
          <tr><td><strong>L1: 跨模态因果通识大脑</strong></td><td>PaLM-E (Driess 2023)</td><td>562B 超大规模多模态统一词元化注入</td><td>将互联网全人类百科常识无损迁移至具身场景，打破单模态孤岛</td></tr>
          <tr><td><strong>L2: 神经运动学物理执行末端</strong></td><td>RT-2 / OpenVLA (Brohan 2023)</td><td>视觉-语言-动作 (VLA) 动作离散分桶映射</td><td>将离散自然语言指令直接翻译为 256 桶离散物理电机控制增量，实现端到端闭环</td></tr>
          <tr><td><strong>L3: 全时空物理因果仿真沙盒</strong></td><td>Sora / DiT (OpenAI 2024)</td><td>时空潜补丁 (Spacetime Patches) 扩散 Transformer</td><td>在没有人类显式编写渲染与刚体方程下，自发涌现客体永存性与物理三维连续性</td></tr>
        </tbody>
      </table>
      <caption>表 104-5 · 具身智能与世界模型三大论文在未来自主机器人中的三层大一统融合图谱。为具身物理落地确立终极坐标。</caption>
    </div>

    <p>没有 PaLM-E 的统一跨模态表征，机器人就只能沦为一个缺乏常识的盲目控制器；没有 RT-2 的动作词元化创新，具身智能就无法复用万亿 Token 互联网预训练的惊人涌现泛化红利；而没有 Sora 类的全时空因果世界模拟器，机器人策略就必须在危险昂贵的物理现实中耗费数百万次物理碰撞试错。唯有将这三大理论成果深度熔铸，我们才能真正创造出能够自主在工厂车间、复杂家庭、深海太空自由穿梭，真正理解并改变物理世界的次世代超级具身智能体！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added cross-paradigm embodied synthesis to ch104.html")
else:
    print("Target not found")
