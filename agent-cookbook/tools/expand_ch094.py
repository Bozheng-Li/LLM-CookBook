import os

path = r"D:/agent-cookbook/chapters/ch094.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep theoretical sections:
# 1. Test-Time Compute Scaling Laws (Snell et al. 2024 & Brown et al. 2024 Math Formulation)
# 2. Complete Beam Search vs. Best-First Search vs. MCTS Trade-off Matrix & Implementation
# 3. Formal Deduction vs. Abduction vs. Induction in Agent Reasoning Loops (Peirce's Logic)

expansion_1 = """
    <h2 id="test-time-scaling-laws">测试时计算扩展定律（Test-Time Compute Scaling Laws）：数学建模与帕累托前沿</h2>
    <p>自 2020 年 Kaplan 与 Chinchilla 确立了预训练参数与数据量的幂律缩放法则（Pre-training Scaling Laws）以来，大模型界一直笼罩在「算力成本与数据墙枯竭」的阴影之下。然而，2024 年底至 2025 年初爆发的测试时计算革命（Test-time Scaling Laws，如 Snell et al., 2024 与 OpenAI o1 体系），正式宣告了第二缩放曲线的诞生：<strong>在模型参数量保持恒定的前提下，通过在推理阶段动态增加思考 Token、分支搜索与前向采样验证算力，可以在下游推理基准上实现超越数倍参数量大模型的惊人性能跃迁！</strong></p>
    
    <p>设输入问题为 $q$，基座模型参数量为 $\Theta$，推理阶段分配的测试时计算总预算为 $C_{\text{test}}$（以 FLOPs 或思考 Token 总数计量）。系统的期望任务准确率 $\mathcal{P}(\text{Success} \mid q, \Theta, C_{\text{test}})$ 遵循非饱和的对数-幂律综合曲线：</p>

    <p>$$\mathcal{P}(\text{Success}) = \frac{1}{1 + \left( \frac{\alpha(\Theta)}{C_{\text{test}}^{\beta_1}} + \frac{\gamma(q)}{N_{\text{samples}}^{\beta_2}} \right)}$$</p>

    <p>在测试时算力分配上，学术界严格确立了三种主要的算力消费分配流派：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>测试时算力流派</th><th>核心计算分配范式</th><th>理论复杂度</th><th>最优适用场景</th></tr></thead>
        <tbody>
          <tr><td><strong>采样并行自一致性 (Best-of-N / Self-Consistency)</strong></td><td>独立并行采样 $N$ 条完整解题路径，通过外置 Verifier 或多数投票选出胜者</td><td>时间复杂度 $O(N)$，空间并行度极高</td><td>答案空间离散且最终结果易于判别的场景（如数学选择题、代码单测）</td></tr>
          <tr><td><strong>序贯自回归长思维链 (Sequential Long CoT, o1/R1)</strong></td><td>单条推理链自主展开数千步隐式推演，在自回归中自主插入回溯与反思</td><td>时间延迟线性拉长，单流深水区推演</td><td>复杂逻辑定理证明、多步骤跨领域战略规划、长程代码重构</td></tr>
          <tr><td><strong>树搜索多路径剪枝 (MCTS / Beam Search)</strong></td><td>在步骤级别展开多候选分支，由 PRM 密集评分指导探索与剪枝</td><td>时间复杂度 $O(B \times D)$，显存占用较高</td><td>每一步都具有明确状态转移与可量化局部评分的确定性博弈场景</td></tr>
        </tbody>
      </table>
      <caption>表 94-4 · 测试时计算三大算力扩展流派对比矩阵。系统 2 慢思考在并行度、深度推演与分支剪枝间的帕累托权衡。</caption>
    </div>
"""

expansion_2 = """
    <h2 id="peirce-logic-triad">皮尔士逻辑三元体：演绎、归纳与溯因推理在 Agent 循环中的交织</h2>
    <p>美国实用主义哲学与逻辑学宗师查尔斯·桑德斯·皮尔士（Charles Sanders Peirce）在 19 世纪末打破了传统形式逻辑的僵硬对立，确立了人类理性认知的三大底层逻辑形态：<strong>演绎推理（Deduction）</strong>、<strong>归纳推理（Induction）</strong>与<strong>溯因推理（Abduction）</strong>。一个真正拥有通用推理能力的自主智能体，必须在决策循环中将这三者无缝啮合：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>逻辑形态 (Peirce)</th><th>形式化逻辑推导结构</th><th>在 Agent 决策循环中的功能映射</th><th>典型落地工程案例</th></tr></thead>
        <tbody>
          <tr><td><strong>演绎推理 (Deduction)</strong></td><td>规则 (Rule) + 情况 (Case) $\implies$ 结果 (Result)<br><em>所有偶数都能被2整除；4是偶数；故4能被2整除。</em></td><td><strong>自顶向下确定性执行：</strong>根据已知代码规范与系统指令，严格推导工具调用的参数与返回结构</td><td>编译器语法检查、SQL 抽象语法树校验、安全沙箱权限阻断</td></tr>
          <tr><td><strong>归纳推理 (Induction)</strong></td><td>情况 (Case) + 结果 (Result) $\implies$ 规则 (Rule)<br><em>该样本A有效；该样本B有效；故此类样本均有效。</em></td><td><strong>自底向上规律提炼：</strong>通过多次少样本（Few-Shot）示例学习或历史工具成功经验，自学习抽象出通用解题套路</td><td>知识库多样本蒸馏、代码重构风格自适应、用户偏好动态建模</td></tr>
          <tr><td><strong>溯因推理 (Abduction)</strong></td><td>规则 (Rule) + 结果 (Result) $\implies$ 情况 (Case)<br><em>草地湿了必定是下雨；草地湿了；假设刚下了雨。</em></td><td><strong>反向诊断与故障归因：</strong>面对异常报错堆栈或未预期结果，逆向猜测最可能的根本诱因（Root Cause）并提出假说</td><td>自动化 Debugging、红蓝对抗漏洞根因分析、医疗辅助诊断</td></tr>
        </tbody>
      </table>
      <caption>表 94-5 · 皮尔士逻辑三元体与 AI Agent 认知推理循环映射矩阵。构筑起发现问题、分析问题与严密执行的完备理性逻辑闭环。</caption>
    </div>

    <p>传统的单步 Prompt 往往只能完成简单的演绎或浅层归纳；而当智能体面对一个复杂的线上生产事故（如「系统在每天凌晨 3 点偶发性报 502 错误」）时，它必须首先利用<strong>溯因推理</strong>逆向提出「定时任务打爆连接池」的候选假说，继而利用<strong>演绎推理</strong>前向推导该假说成立时应有的具体日志证据，最后通过<strong>归纳推理</strong>结合历史多天数据确认规律，形成坚不可摧的认知逻辑闭环。</p>
"""

expansion_3 = """
    <h2 id="beam-vs-mcts-tradeoff">图搜索算法谱系对比：Beam Search、Best-First 与 MCTS 的计算前沿</h2>
    <p>在推理状态空间中展开前向规划时，工程架构师必须在搜索质量、时间延迟与计算资源消耗之间做出严密的数学折演。以下给出三种核心搜索范式的对比与轻量化束搜索（Beam Search）实现：</p>

    <div class="codeblock">
      <div class="cb-head"><span>束搜索 (Beam Search) 推理分支规划器（beam_reasoning.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>from typing import List, Tuple

class BeamReasoningPlanner:
    def __init__(self, policy_llm, prm_scorer, beam_width: int = 3, max_depth: int = 5):
        self.policy = policy_llm
        self.prm = prm_scorer
        self.k = beam_width          # 束宽 (Beam Width): 始终保留最有希望的前 k 个活跃分支
        self.max_depth = max_depth

    def search_solution(self, initial_problem: str) -> str:
        \"\"\"基于固定束宽的 Beam Search 剪枝规划\"\"\"
        # 维护当前的活跃候选轨迹集: [(cumulative_score, trajectory_text)]
        current_beams = [(0.0, f"Problem: {initial_problem}")]

        for depth in range(self.max_depth):
            all_candidates = []

            for cum_score, trajectory in current_beams:
                if "Answer:" in trajectory or "最终结论" in trajectory:
                    all_candidates.append((cum_score, trajectory))
                    continue

                # 为当前路径采样 3 个不同的后续推导步骤
                next_steps = self.policy.sample_steps(trajectory, num_samples=3)
                for step_text in next_steps:
                    # 调用 PRM 评估该新增步骤的局部质量增量
                    step_score = self.prm.score_step(trajectory, step_text)
                    new_trajectory = trajectory + "\\n• " + step_text
                    all_candidates.append((cum_score + step_score, new_trajectory))

            # 按照累积分数降序严格裁剪，仅保留前 k 个最强分支
            all_candidates.sort(key=lambda x: x[0], reverse=True)
            current_beams = all_candidates[:self.k]

            print(f"[Beam Depth {depth+1}] 活跃保留最优得分: {current_beams[0][0]:.3f}")

        # 返回最终得分最高的最佳完整思考链
        return current_beams[0][1]</code></pre>
    </div>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch094.html with scaling laws, Peirce logic and Beam search")
else:
    print("Target not found")
