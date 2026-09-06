# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch107.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

rich_content = """
    <p>为了进一步消除 LLM-as-a-Judge 的评测偏差（如位置偏见 Position Bias、冗长偏见 Verbosity Bias 和自相偏袒 Self-enhancement Bias），在顶层设计中引入<strong>交叉双盲检验与裁判校准矩阵（Cross-blind Jury Matrix）</strong>：</p>
    <ul>
        <li><strong>打乱候选顺序与对偶评估（Permutation & Dual Evaluation）：</strong>针对任何依赖大模型裁判打分的生成型或分析型动作，必须将输出顺序在 $(A, B)$ 与 $(B, A)$ 间进行对偶置换评测。若评判结论发生反转，则该题目直接判定为<strong>不确定态（Indeterminate）</strong>并降级转交人工仲裁。</li>
        <li><strong>元评测校准数据集（Meta-evaluation Calibration Set）：</strong>定期抽取包含真实黄金答案、典型幻觉伪造样本及边缘边界案例的基准集合，评测大模型裁判在校准集上的宏查准率（Macro-Precision）与校准误差（ECE, Expected Calibration Error）。当裁判模型的打分置信度偏差超出阈值时，自动触发重试采样或切换为多模型投票仲裁机制。</li>
        <li><strong>动态状态转移博弈环境（Dynamic State-Space Game Harness）：</strong>对于涉及多回合博弈、谈判或对抗类任务的评估，采用动态响应仿真器模拟环境反馈。环境不仅提供静态断言判定，更维护包含资源消耗率、响应延迟波动与对抗干扰项的动态状态空间，从全局轨迹层面量化智能体的鲁棒决策熵与自适应衰减率。</li>
    </ul>
"""

target = '<h2 id="eval-engineering-epistemology">'
if target in text:
    new_text = text.replace(target, rich_content + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added rich content")
