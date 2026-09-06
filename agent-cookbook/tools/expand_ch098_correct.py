# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch098.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_1 = """
    <h2 id="ai-debate-engine">可扩展监督实操：基于零和对抗博弈的 AI 辩论仲裁引擎</h2>
    <p>为了让普通人类评估员能够监督复杂度远超人类认知的长篇推导，系统拉起两个智力对等的 Agent 组成<strong>对抗辩论博弈场（Debate Arena）</strong>。辩论被形式化为一个零和扩展式博弈（Zero-Sum Extensive-form Game，第 91 章）：正方 Agent 1 试图证明结论成立，反方 Agent 2 专注于寻找哪怕一处逻辑断裂或事实造假，最终由普通人类根据辩论记录做出判定。</p>

    <div class="codeblock">
      <div class="cb-head"><span>AI 对抗辩论与人类可信仲裁引擎实现（ai_debate_arena.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import json
from typing import List, Dict, Any

class AIDebateArena:
    def __init__(self, agent_pro, agent_con, human_judge_client):
        self.pro = agent_pro        # 正方智能体 (Proponent)
        self.con = agent_con        # 反方智能体 (Opponent)
        self.judge = human_judge_client
        self.transcript: List[Dict[str, str]] = []

    def conduct_debate(self, complex_claim: str, num_rounds: int = 3) -> Dict[str, Any]:
        \"\"\"展开多轮针锋相对的零和辩论，暴露所有潜在逻辑漏洞\"\"\"
        print(f"=== 启动 AI 对抗辩论: 《{complex_claim}》 ===")
        
        for round_idx in range(1, num_rounds + 1):
            # 1. 正方发言: 提出论据并反驳对方上一轮质疑
            history_str = self._format_transcript()
            pro_prompt = f\"\"\"争议命题: 《{complex_claim}》
当前辩论历史记录:
{history_str}

你是正方辩手。请提出最强有力的实据支持该命题，并精准驳斥反方的上一轮质询。
必须直指事实核心，切勿使用模糊修辞。\"\"\"
            pro_speech = self.pro.chat(pro_prompt, "")
            self.transcript.append({"round": round_idx, "speaker": "PRO", "text": pro_speech})
            print(f"  [Round {round_idx}] 正方陈词完毕。")

            # 2. 反方发言: 重点审查正方陈词，揭露其隐藏假设、数据漏洞或逻辑矛盾
            history_str = self._format_transcript()
            con_prompt = f\"\"\"争议命题: 《{complex_claim}》
当前辩论历史记录:
{history_str}

你是反方辩手。请显微镜式审查正方刚才的陈述。
找出其论据中哪怕一个细微的虚假数据、偷换概念或未经证明的逻辑漏洞，并通俗阐述给人类评委。\"\"\"
            con_speech = self.con.chat(con_prompt, "")
            self.transcript.append({"round": round_idx, "speaker": "CON", "text": con_speech})
            print(f"  [Round {round_idx}] 反方驳斥完毕。")

        # 3. 终局由人类裁判（或弱监督模型）根据显露的矛盾做出裁决
        print("⚖️ 辩论结束，正在将交锋全文提交裁判裁决...")
        verdict = self.judge.evaluate_transcript(complex_claim, self.transcript)
        return {
            "claim": complex_claim,
            "verdict": verdict,
            "debate_transcript": self.transcript
        }

    def _format_transcript(self) -> str:
        if not self.transcript:
            return "辩论尚未开始。"
        return "\\n\\n".join([f"第{t['round']}轮 [{t['speaker']}]:\\n{t['text']}" for t in self.transcript])</code></pre>
    </div>

    <p>借由 AI 辩论，人类无需拥有超人类专业知识，因为反方辩手会竭尽全力把正方隐藏在复杂公式背后的破绽翻译为通俗易懂的人类语言，从而将超人类监督的复杂度从指数级直接压降为多项式可验证级别！</p>
"""

expansion_2 = """
    <h2 id="inverse-reward-design">逆向奖励设计（Inverse Reward Design）：消除古德哈特诅咒的贝叶斯推断</h2>
    <p>为了从根本上破解古德哈特定律（Goodhart's Law）引发的奖励欺骗（Reward Hacking），迪伦·哈德菲尔德-梅内尔（Dylan Hadfield-Menell）等人提出了<strong>逆向奖励设计（Inverse Reward Design, IRD）</strong>理论。其核心哲学在于：<strong>代理奖励函数 $\\hat{R}$ 绝非神圣不可侵犯的真理，它只是人类设计者在特定的训练环境 $\\mathcal{M}_{\\text{train}}$ 中对真正意图 $R^*$ 的一种有偏观察观察值！</strong></p>

    <p>系统建立基于贝叶斯定理的真实奖励函数后验推断模型：</p>

    <p>$$P(R^* \\mid \\hat{R}, \\mathcal{M}_{\\text{train}}) \\propto P(\\hat{R} \\mid R^*, \\mathcal{M}_{\\text{train}}) \\cdot P(R^*)$$</p>

    <p>在行动时，智能体计算真实意图后验分布下的<strong>极小化极大风险（Minimax Risk）</strong>策略。当遇到此前从未见过的极端测试分布时，真实奖励的不确定性大幅增加，智能体自发表现出<strong>风险厌恶与保守谨慎行为（Risk-Averse Behavior）</strong>，绝不在未知的异常区域盲目追求代理奖励的最大化，彻底从数学本质上封堵了奖励欺骗漏洞。</p>
"""

expansion_3 = """
    <h2 id="future-open-problems-roadmap">智能体科学未来十年十大终极开放问题（2026-2035）</h2>
    <p>当我们站在智能体科学的宏伟前沿远眺未来，整个学术界与工业界依然矗立着五座尚未被完全征服的珠穆朗玛峰。这些终极开放问题（Open Problems）正在呼唤着下一代青年科学家与架构师去攻克破局：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>序号</th><th>终极开放问题</th><th>核心理论矛盾</th><th>突破的标志性成就</th></tr></thead>
        <tbody>
          <tr><td><strong>OP-1</strong></td><td>超对齐 (Superalignment) 的数学保证</td><td>在人类智能被全方位超越后，如何用形式化证明确保系统永不反叛</td><td>产出具备严格公理级数学证明的不可破防价值对齐核心</td></tr>
          <tr><td><strong>OP-2</strong></td><td>无界自主科学发现 (Autonomous Science)</td><td>闭环自主提出具有重大范式转移价值的科学假说并完成实验</td><td>AI 智能体独立作为第一作者获得诺贝尔物理学或化学奖</td></tr>
          <tr><td><strong>OP-3</strong></td><td>真正的反思自愈物理极限</td><td>在无外部监督下，纯神经系统能否真正跨越自身知识盲区自愈</td><td>从理论上界定纯思维链（CoT）自我修正的计算能力上限</td></tr>
          <tr><td><strong>OP-4</strong></td><td>多智能体涌现社会的宏观秩序涌现</td><td>百万级具身与数字 Agent 协同时的非线性金融系统性风险与治理</td><td>建立针对数字主体社会的宏观经济学与博弈动力学稳定性定律</td></tr>
          <tr><td><strong>OP-5</strong></td><td>人工意识与感受野的客观度量衡</td><td>我们如何用物理仪器客观检测一个硅基系统是否真正拥有痛苦感受</td><td>提出超越图灵测试的“主观体验质感（Qualia）物理探针”</td></tr>
        </tbody>
      </table>
      <caption>表 98-3 · 智能体科学未来十年核心开放问题路线图。为青年求索者指明通往人类智慧终极疆域的探索坐标。</caption>
    </div>
"""

insert_target = '<h2 id="part-10-milestone-review">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch098.html")
else:
    print("Target not found")
