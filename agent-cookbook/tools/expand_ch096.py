# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch096.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep theoretical sections:
# 1. Differentiable Inductive Logic Programming (ILP) & Neural Logic Machines (NLM)
# 2. Complete Lean 4 Formal Verification Pipeline for Agent Action Safety
# 3. Knowledge Graph Embedding (TransE, RotatE) vs. Neural-Symbolic Reasoning

expansion_1 = """
    <h2 id="neural-logic-machines">归纳逻辑编程与神经逻辑机（NLM）：可微符号规则学习</h2>
    <p>传统的符号系统最被诟病的一点在于：所有的逻辑规则必须由人类专家手工逐行编写，在面对复杂的工业生产时存在巨大的规则构建瓶颈。与此相对，经典机器学习擅长从数据中自动拟合参数，却难以输出干净通用的符号规则。<strong>归纳逻辑编程（Inductive Logic Programming, ILP）</strong>正是这一难题的圣杯：<strong>从正负样本事实中，自主诱导归纳出通用的抽象一阶谓词公理</strong>。</p>
    
    <p>近年来，随着深度学习与张量代数的深度融合，以<strong>神经逻辑机（Neural Logic Machines, NLM）</strong>与可微归纳逻辑编程（$\partial$ILP）为代表的架构取得了决定性突破。NLM 将一阶谓词逻辑公式严格形式化为高阶张量空间上的排列等变（Permutation-equivariant）运算网络：</p>

    <p>设实体集合为 $\mathcal{E}$（包含 $N$ 个实体），零阶谓词表示全局属性（标量或向量），一阶谓词 $P(x)$ 对应于向量矩阵 $\mathbf{T}^{(1)} \in [0, 1]^{N \times D_1}$，二阶二元关系谓词 $R(x, y)$ 对应于三阶张量 $\mathbf{T}^{(2)} \in [0, 1]^{N \times N \times D_2}$。</p>
    
    <p>NLM 在张量流空间内定义了三种可微逻辑原子操作：</p>
    <p><strong>1. 扩展操作（Expansion / Quantification）：</strong>将 $r$ 阶谓词通过张量广播扩展为 $r+1$ 阶谓词（引入新自由变量，对应于全称或存在量词的先验构造）；</p>
    <p><strong>2. 归约操作（Reduction / Marginalization）：</strong>利用可微最大值池化（Max-pooling）或求和对某一维度进行投影归约：$\mathbf{T}^{(r-1)}(x) = \max_y \mathbf{T}^{(r)}(x, y)$，严格对应于存在量词 $\exists y$ 的可微语义；</p>
    <p><strong>3. 关系映射（Relational Mapping）：</strong>在相同阶数的谓词张量之间应用多层感知机（MLP）进行特征非线性组合与规则蕴涵演算。</p>

    <div class="codeblock">
      <div class="cb-head"><span>神经逻辑机 (NLM) 一阶与二阶谓词可微张量推理层（nlm_layer.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import torch
import torch.nn as nn

class NeuralLogicLayer(nn.Module):
    def __init__(self, in_features_1: int, in_features_2: int, out_features_2: int):
        super().__init__()
        # 用于将两个一阶谓词特征通过笛卡尔积扩展并融合成二阶关系谓词的线性映射
        self.expand_mlp = nn.Sequential(
            nn.Linear(in_features_1 * 2 + in_features_2, out_features_2),
            nn.Sigmoid() # 输出真值概率归一化至 [0, 1]
        )

    def forward(self, unary_predicates: torch.Tensor, binary_predicates: torch.Tensor) -> torch.Tensor:
        \"\"\"
        unary_predicates: 一阶谓词张量, 形状 (Batch, N, in_features_1)
        binary_predicates: 二阶关系谓词张量, 形状 (Batch, N, N, in_features_2)
        \"\"\"
        B, N, D1 = unary_predicates.shape
        
        # 1. 扩展算子: 通过张量外积广播将两个实体 x 和 y 的属性并联
        u_expanded_x = unary_predicates.unsqueeze(2).expand(B, N, N, D1) # (B, N, N, D1)
        u_expanded_y = unary_predicates.unsqueeze(1).expand(B, N, N, D1) # (B, N, N, D1)

        # 2. 关系张量拼接
        combined_feat = torch.cat([u_expanded_x, u_expanded_y, binary_predicates], dim=-1)

        # 3. 执行可微规则变换，推断新的二阶关系概率
        new_binary_predicates = self.expand_mlp(combined_feat)
        return new_binary_predicates</code></pre>
    </div>

    <p>通过堆叠这种逻辑张量层，系统能够直接从积木搬运（Blocks World）、家庭亲属关系图谱等具体数据中，<strong>端到端学出「祖父必定是父亲的父亲（$\forall x, y, z: Father(x, y) \land Father(y, z) \to Grandfather(x, z)$）」等完美的通用符号公理</strong>。这种归纳规则不仅具备 100% 的可读性与可解释性，更能在实体数量从训练时的 10 个外推到测试时的 10,000 个时，保持惊人的零错误泛化！</p>
"""

expansion_2 = """
    <h2 id="lean4-safety-pipeline">形式化定理证明实战：基于 Lean 4 的 Agent 动作安全证明链</h2>
    <p>在涉及智能合约执行、工业机器人避障或无人机空中交会的深水区，即便 SMT 求解器给出了 SAT 判定，我们仍需要一份具备数学公理严格背书的<strong>形式化数学证明对象（Formal Proof Object）</strong>。这就是现代交互式定理证明器 <strong>Lean 4</strong> 的绝对统治领域。</p>
    
    <p>在 Lean 4 中，依赖类型论（Calculus of Inductive Constructions）贯彻了著名的<strong>柯里-霍华德同构（Curry-Howard Isomorphism）</strong>：<strong>命题即类型，证明即程序（Propositions-as-Types, Proofs-as-Programs）</strong>。如果大模型能够为某个动作写出一个合法的 Lean 4 函数，该函数的返回类型恰好是「系统处于安全状态」，那么只要这段代码通过了 Lean 4 编译器的强类型检查，就<strong>在数学上绝对杜绝了系统进入灾难崩溃态的任何理论可能</strong>！</p>

    <div class="codeblock">
      <div class="cb-head"><span>基于 Lean 4 的无人机安全避障形式化公理证明规范（DroneSafety.lean）</span><button class="cb-copy">复制</button></div>
      <pre><code>-- 导入基础实数理论库
import Mathlib.Data.Real.Basic

-- 1. 定义无人机物理状态与安全公理
structure DroneState where
  distance_to_obstacle : ℝ
  current_speed : ℝ
  braking_power : ℝ
  h_power_pos : braking_power > 0

-- 2. 声明企业级物理安全定理: 在制动功率充沛的前提下，刹车距离严格小于最小安全裕度
theorem safe_braking_guarantee (s : DroneState) (h_speed_safe : s.current_speed ≤ 5.0) 
  (h_dist : s.distance_to_obstacle ≥ 10.0) (h_brake : s.braking_power ≥ 2.5) :
  (s.current_speed ^ 2) / (2 * s.braking_power) < s.distance_to_obstacle := by
  -- 利用 Lean 4 内置代数策略证明该不等式恒成立
  have h_num : s.current_speed ^ 2 ≤ 25.0 := by nlinarith
  have h_denom : 2 * s.braking_power ≥ 5.0 := by linarith
  have h_stopping_dist : (s.current_speed ^ 2) / (2 * s.braking_power) ≤ 5.0 := by
    -- 刹车距离至多为 5.0 米
    apply div_le_of_le_mul
    linarith
    nlinarith
  linarith</code></pre>
    </div>

    <p>在生产级高可用智能体流水线中，Agent 在向物理外设下发高危动作之前，首先调用微调代码模型合成上述 Lean 4 形式化证明代码；底层调用 Lean 编译器在 50 毫秒内执行 <code>lean --run DroneSafety.lean</code>。若编译器编译通过，打上加密数字指纹予以执行；若类型检查报错（证明不成立），执行管道直接物理硬件断电，彻底筑牢工业级数字安全的马奇诺防线。</p>
"""

expansion_3 = """
    <h2 id="kg-embedding-synergy">知识图谱嵌入与逻辑推演的双向赋能：TransE 到 RotatE</h2>
    <p>在知识图谱工程中，离散的符号三元组 $(h, r, t)$（头实体、关系、尾实体）在面对海量实体补全时，极易遭遇高昂的图搜索遍历代价。现代神经符号 AI 将离散图谱嵌入至高维连续几何流形中，形成了<strong>知识图谱嵌入（Knowledge Graph Embedding, KGE）</strong>经典理论谱系：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>KGE 模型</th><th>几何流形空间</th><th>打分函数 $f_r(h, t)$</th><th>可表达的逻辑模式 (Symmetry, Transitivity, Composition)</th></tr></thead>
        <tbody>
          <tr><td><strong>TransE (Bordes et al., 2013)</strong></td><td>实数欧氏空间 $\mathbb{R}^d$</td><td>$-\|\mathbf{h} + \mathbf{r} - \mathbf{t}\|$ (平移向量)</td><td>擅长传递性与反自反性，但<strong>完全无法处理对称关系</strong> (若 $h+r=t$ 且 $t+r=h$，迫使 $r=0$)</td></tr>
          <tr><td><strong>RotatE (Sun et al., 2019)</strong></td><td>复数复平面空间 $\mathbb{C}^d$</td><td>$-\|\mathbf{h} \circ \mathbf{r} - \mathbf{t}\|$ (复数旋转)</td><td>完美支持<strong>对称性、反对称性、反转性与关系复合</strong>（Euler 恒等式 $e^{i\theta}$）</td></tr>
          <tr><td><strong>BoxE (Abboud et al., 2020)</strong></td><td>高维超矩形边界空间 $\mathbb{R}^d$</td><td>实体点落入超矩形包围盒的归一化距离</td><td>原生支持<strong>一阶逻辑全称量词、多对多重叠拓扑与子类归属</strong>演绎</td></tr>
        </tbody>
      </table>
      <caption>表 96-4 · 主流知识图谱嵌入模型几何映射机理与逻辑代数表达能力对比矩阵。将离散拓扑化为连续流形几何运算。</caption>
    </div>

    <p>在先进智能体架构中，知识图谱嵌入不再是脱机的打分玩具，而是与大语言模型的自回归注意力机制紧密耦合成<strong>双向能量引导循环</strong>：KGE 的连续几何内积为语言模型的 Next-Token 采样提供深层拓扑先验能量偏置；而语言模型反过来利用海量无监督语料，持续校正与增量更新图谱嵌入空间的复数旋转流形，实现符号与神经的终极互惠共生。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch096.html with NLM, Lean4 and KGE")
else:
    print("Target not found")
