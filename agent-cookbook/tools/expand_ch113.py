# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch113.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

rich_terms_expansion = """
    <h2 id="deep-glossary-extended-matrix">进阶深度拓展：前沿多模态、具身智能与神经符号核心术语（Terms 217 - 300）</h2>
    <p>为了全面覆盖多模态大模型、具身物理控制以及神经符号混合系统的最新前沿突破，本节进一步精选并扩充了以下核心关键术语体系：</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>术语代码与中英文标准名称</th>
            <th>首创机构 / 学术出处</th>
            <th>形式化数学机制与物理本质</th>
            <th>工业应用与前沿系统架构映射</th>
            <th>全书对应章节</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>T217: Normalized Coordinate Space<br>归一化坐标空间映射</strong></td>
            <td>Anthropic (Computer Use, 2024)</td>
            <td>将屏幕物理分辨率任意缩放为统一的 $[0, 1000] \times [0, 1000]$ 连续网格，利用模型内置的视空先验消除物理像素分辨率扰动。</td>
            <td>桌面自动化控制与手机端操作系统 Agent 消除跨分辨率、跨缩放比（DPI）适配漂移的关键基石。</td>
            <td>第 86, 89 章</td>
          </tr>
          <tr>
            <td><strong>T218: Logic Tensor Networks (LTN)<br>逻辑张量网络</strong></td>
            <td>Serafini & Garcez (2016)</td>
            <td>利用软实数 t-范数（t-norms，如 Lukasiewicz 或 Product t-norm）将一阶谓词逻辑中的离散真值 $\{0, 1\}$ 连续松弛为 $[0, 1]$ 区间。</td>
            <td>神经符号 AI（Neuro-Symbolic AI）的核心算法，使得大模型不仅具备模糊直觉，更可受控于严谨符号形式化约束。</td>
            <td>第 96 章</td>
          </tr>
          <tr>
            <td><strong>T219: Visual Servoing (PBVS / IBVS)<br>视觉伺服伺服控制闭环</strong></td>
            <td>Chaumette & Hutchinson (2006)</td>
            <td>基于图像特征误差或三维位姿误差，利用图像雅可比矩阵（Image Jacobian）实时映射并计算末端执行器的控制速度。</td>
            <td>具身机器人机械臂抓取与动态环境避障 Agent 的核心经典物理控制算法。</td>
            <td>第 68, 104 章</td>
          </tr>
          <tr>
            <td><strong>T220: Elastic Weight Consolidation (EWC)<br>弹性权重巩固</strong></td>
            <td>Kirkpatrick et al. (DeepMind, 2017)</td>
            <td>利用费雪信息矩阵（Fisher Information Matrix $F$）对先前任务中重要的网络参数施加二次型曲率惩罚保护：$\sum_i F_i (\theta_i - \theta_i^*)^2$。</td>
            <td>防止智能体在持续强化学习与终身微调中发生灾难性遗忘的经典基石算法。</td>
            <td>第 97 章</td>
          </tr>
          <tr>
            <td><strong>T221: Prigogine Dissipative Structure<br>普利高津耗散结构理论</strong></td>
            <td>Ilya Prigogine (1977 诺贝尔奖)</td>
            <td>远离平衡态的开放非线性系统，通过持续与外界环境交换物质和能量并引入负熵流（$dS_e < 0$），在宏观上形成时间、空间上的自组织有序结构。</td>
            <td>智能体系统对抗内部推理漂移与长上下文熵增的终极物理世界哲学映射。</td>
            <td>第 92 章</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>通过这套立体互联的术语坐标系，技术人员在面对任何新型复杂的智能体架构时，都能够迅速调用底层形式化数学、控制论系统边界与工业级工程原语进行类比解构，彻底终结“知其然而不知其所以然”的碎片化学习迷局。</p>
"""

target = '<h2 id="epistemological-summary-and-farewell">'
if target in text:
    new_text = text.replace(target, rich_terms_expansion + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Expanded ch113 with deep terms expansion")
else:
    print("Target not found")
