# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch103.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="cross-paradigm-alignment-synthesis">安全对齐三大论著的工程升华：构筑企业级生产免疫防线</h2>
    <p>综合研读 Constitutional AI、DPO 与 Spotlighting 防御这三大开创性论著，我们清晰地看到了一条从“高层价值公理定义”到“底层数学模型优化”，再到“系统工程零信任防御”的<strong>立体三维纵深防御图谱</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>安全防御层级</th><th>核心学术论著支撑</th><th>技术实现与防御机制</th><th>防护的核心安全风险</th></tr></thead>
        <tbody>
          <tr><td><strong>L1: 伦理与价值公理层</strong></td><td>Constitutional AI (Bai 2022)</td><td>显式宪法原则、自我批判与 RLAIF 偏好学习</td><td>违法犯罪唆使、仇恨歧视言论、盛气凌人说教</td></tr>
          <tr><td><strong>L2: 算法优化与偏好对齐层</strong></td><td>DPO (Rafailov 2023)</td><td>Bradley-Terry 闭式对偶代换，直接在偏好数据上收敛</td><td>训练过程梯度坍塌、奖励模型欺骗 (Reward Hacking)</td></tr>
          <tr><td><strong>L3: 系统信道与沙箱隔离层</strong></td><td>Spotlighting (Hines 2024)</td><td>词元空间变换染色、双模型特权隔离与零信任架构</td><td>间接提示词注入 (Indirect Injection)、数据外泄与越权提权</td></tr>
        </tbody>
      </table>
      <caption>表 103-3 · 安全对齐三大论文在企业级智能体系统中的三层防御纵深映射表。为现代高危 Agent 筑牢免疫屏障。</caption>
    </div>

    <p>没有 Constitutional AI 的原则引导，模型就失去了判定是非善恶的伦理罗盘；没有 DPO 的数学对偶极简性，企业级偏好对齐就只能在昂贵且脆弱的 PPO 泥潭中苦苦挣扎；而没有 Spotlighting 的信道零信任绝缘，任何连接了互联网搜索与操作系统的智能体都将在第一封钓鱼邮件或恶意网页前彻底沦陷。唯有将这三大技术体系紧密融合，我们才能真正打造出既具备无与伦比生产力、又拥有无懈可击安全性的现代工业级可信超级智能体！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added cross-paradigm alignment synthesis to ch103.html")
else:
    print("Target not found")
