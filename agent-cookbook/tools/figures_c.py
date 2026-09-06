# -*- coding: utf-8 -*-
"""figures_c.py — 多模态/理论/资源/首页插图 (fig 71-84)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *
SOFT = {C.teal: C.teal_s, C.blue: C.blue_s, C.purple: C.purple_s, C.amber: C.amber_s, C.indigo: C.indigo_s, C.red: C.red_s, C.faint: C.gray_s}

# ---- 71 hero overview (index) ---------------------------------------------
f = F(980, 400)
f.text(490, 36, "The Agent Anatomy", 20, C.ink, 800)
user = f.person(110, 200)
f.text(110, 250, "用户", 12.5, C.purple_d, 700)
orch = f.box(230, 140, 220, 110, "🧠 Orchestrator", "LLM 策略中枢\n规划 · 反思 · 决策", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=14)
mem = f.cylinder(240, 320, 130, 76, "记忆\n向量 + 情节", fs=11.5)
tools = [("🔍 检索", 560, 70, C.teal), ("🌐 浏览器", 560, 150, C.blue), ("💻 代码执行", 560, 230, C.purple), ("📞 MCP 工具", 560, 310, C.amber)]
softmap = {C.teal: C.teal_s, C.blue: C.blue_s, C.purple: C.purple_s, C.amber: C.amber_s}
tb = []
for t, x, y, colr in tools:
    b = f.box(x, y, 170, 56, t, fill=softmap[colr], stroke=colr, tc=colr, fs=13)
    tb.append(b)
    f.elbow([(450, 195), (505, 195), (505, y + 28), (556, y + 28)], color=C.faint, sw=1.3)
f.arrow(110, 200, 226, 200, label="任务", color=C.purple, sw=1.6)
f.elbow([(560 + 170 + 20, 200), (790, 200), (790, 380), (450, 380), (450, 254)], label="观察结果回填", color=C.teal, sw=1.4, dash="5 4")
f.elbow([(300, 254), (280, 300), (305, 300)], color=C.faint, sw=1.3, dash="4 4")
f.note(490, 388, "LLM + 工具 + 记忆 + 循环 = Agent", 13, C.faint)
f.save("fig-hero-overview")

# ---- 72 vlm agent (ch66) ----------------------------------------------------
f = F(920, 380)
f.text(460, 30, "多模态 Agent:把『看』变成一种工具调用", 17, C.ink, 800)
cam = f.box(70, 90, 190, 70, "视觉输入", "截图 / 摄像头帧", fill=C.blue_s, stroke=C.blue, tc=C.blue_d, fs=12.5)
enc = f.box(320, 90, 190, 70, "视觉编码器", "ViT → 视觉 Token", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12.5)
llm = f.box(570, 90, 150, 70, "LLM", "统一序列建模", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=13)
out = f.box(780, 90, 110, 70, "动作", "点击(345,220)\n/ 描述 / 代码", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=11)
for a, b in [(cam, enc), (enc, llm), (llm, out)]:
    f.arrow(a["right"][0], 125, b["x"], 125, color=C.faint)
f.group(70, 210, 820, 120, "三种视觉接地(Grounding)方式")
f.mtext(90, 248, ["① 坐标回归:直接输出像素坐标(需专门训练,如 CogAgent)  ② Set-of-Mark:给可交互元素编号,输出编号"], 12.5, C.ink, 400, 1.9, anchor="start")
f.mtext(90, 276, ["③ 结构化解析:HTML/无障碍树为主、视觉为辅 —— 当前工程上最稳的组合"], 12.5, C.ink, 400, 1.9, anchor="start")
f.note(460, 358, "视觉 Token 很贵:一张 1080p 截图 ≈ 1000~1600 Token;多模态 Agent 的成本预算大头在『看』", 12, C.faint, anchor="middle")
f.save("fig-vlm-agent")

# ---- 73 som (ch67) -----------------------------------------------------------
f = F(920, 430)
f.text(460, 30, "Set-of-Mark:让模型『点着编号』操作界面", 17, C.ink, 800)
scr = f.box(80, 70, 380, 280, "", fill="#ffffff", stroke=C.ink, rx=6)
f.text(270, 92, "Browser — 商城首页", 11.5, C.faint, 600)
f.raw('<rect x="110" y="110" width="150" height="26" rx="6" fill="%s" stroke="%s"/>' % (C.blue_s, C.blue))
f.text(185, 127, "搜索框 ①", 11, C.blue_d, 700)
f.raw('<rect x="110" y="150" width="90" height="22" rx="6" fill="%s" stroke="%s"/>' % (C.teal_s, C.teal))
f.text(155, 165, "首页 ②", 10.5, C.teal_d, 700)
f.raw('<rect x="210" y="150" width="90" height="22" rx="6" fill="%s" stroke="%s"/>' % (C.teal_s, C.teal))
f.text(255, 165, "购物车 ③", 10.5, C.teal_d, 700)
f.raw('<rect x="110" y="190" width="100" height="70" rx="6" fill="%s" stroke="%s"/>' % (C.purple_s, C.purple))
f.text(160, 230, "商品卡 ④", 11, C.purple_d, 700)
f.raw('<rect x="230" y="190" width="100" height="70" rx="6" fill="%s" stroke="%s"/>' % (C.purple_s, C.purple))
f.text(280, 230, "商品卡 ⑤", 11, C.purple_d, 700)
f.raw('<rect x="110" y="280" width="220" height="30" rx="6" fill="%s" stroke="%s"/>' % (C.amber_s, C.amber))
f.text(220, 299, "加入购物车 ⑥", 11, C.amber_d, 700)
f.box(520, 90, 360, 110, "原始截图 → 标注后图像", "检测可交互元素 → 框选 + 编号叠加\n模型输出: click(6) 而非 click(347,295)", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=11.5, weight=400)
f.box(520, 230, 360, 110, "为什么有效", "编号把『视觉定位』变成『选择填空』,\n准确率大幅提升且省视觉 Token;\nHTML 树可提供编号的语义(aria-label)。", fill=C.gray_s, stroke=C.line, fs=11.5, weight=400)
f.note(460, 408, "WebVoyager(2024) 验证 SoM + 历史摘要的浏览器 Agent 达到人类水平任务成功率(该基准下)", 12, C.faint, anchor="middle")
f.save("fig-som")

# ---- 74 vla (ch69) -----------------------------------------------------------
f = F(920, 380)
f.text(460, 30, "VLA:视觉-语言-动作,从数字世界到物理世界", 17, C.ink, 800)
f.box(60, 80, 220, 90, "摄像头 + 语言指令", "『把桌上的杯子\n放进水槽』", fill=C.blue_s, stroke=C.blue, tc=C.blue_d, fs=12)
f.box(340, 80, 240, 90, "VLA 模型", "视觉 Token + 语言 →\n动作 Token 序列", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12.5)
f.box(640, 80, 230, 90, "机器人执行", "机械臂关节角/\n末端位姿 50Hz 闭环", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12)
f.arrow(280, 125, 336, 125, color=C.faint)
f.arrow(580, 125, 636, 125, color=C.faint)
f.elbow([(755, 170), (755, 250), (170, 250), (170, 174)], label="新的观察(闭环)", color=C.faint, dash="5 4")
f.group(60, 280, 810, 80, "与数字 Agent 的三个不同")
f.mtext(80, 314, ["① 动作空间连续且高频  ② 失败不可撤销(杯子会碎)  ③ 数据昂贵(遥操采集)→ 模仿学习为主,RL 为辅"], 12.5, C.ink, 400, 1.9, anchor="start")
f.note(460, 372, "RT-2(2023) 首证『网络级视觉语义』可迁移到机器人;π0/GR00T(2024-25) 推向通用机器人基座", 12, C.faint, anchor="middle")
f.save("fig-vla")

# ---- 75 mdp (ch91) -----------------------------------------------------------
f = F(880, 340)
f.text(440, 30, "MDP:Agent 的最小数学模型", 17, C.ink, 800)
s0 = f.box(80, 120, 130, 50, "s₀ 状态", fill=C.blue_s, stroke=C.blue, tc=C.blue_d)
s1 = f.box(330, 120, 130, 50, "s₁ 状态", fill=C.blue_s, stroke=C.blue, tc=C.blue_d)
s2 = f.box(580, 120, 130, 50, "s₂ …", fill=C.blue_s, stroke=C.blue, tc=C.blue_d)
f.arrow(210, 132, 326, 132, label="动作 a₀", color=C.indigo, sw=1.6)
f.arrow(460, 132, 576, 132, label="动作 a₁", color=C.indigo, sw=1.6)
f.elbow([(645, 120), (645, 80), (145, 80), (145, 116)], color=C.faint, dash="5 4")
f.text(395, 72, "环境转移 P(s'|s,a) + 奖励 r(s,a)", 12, C.faint, 600)
f.text(395, 200, "目标:最大化期望累计回报 E[ Σ γᵗ·rₜ ]", 14, C.ink, 700)
f.group(60, 240, 760, 70, "映射到 LLM Agent")
f.text(80, 286, "状态=对话历史+观察 · 动作=生成文本(工具调用) · 奖励=任务成功信号 · 策略 π(a|s)=LLM 本身", 12, C.soft, 400, anchor="start")
f.note(440, 326, "POMDP:真实环境状态不可全见(Agent 只能通过观察推断)—— 这正是『记忆』存在的原因", 12, C.faint, anchor="middle")
f.save("fig-mdp")

# ---- 76 mcts (ch93) -----------------------------------------------------------
f = F(920, 440)
f.text(460, 30, "MCTS:用『模拟』代替『蛮力』搜索决策树", 17, C.ink, 800)
f.text(460, 58, "① 选择  ② 扩展  ③ 模拟(rollout)  ④ 反向传播 —— 循环千次", 12, C.faint, 600)
root = f.box(390, 84, 140, 44, "根:当前局面", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=11.5)
c1 = f.box(220, 190, 130, 40, "分支 A (Q=0.9)", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=10.5, weight=400)
c2 = f.box(400, 190, 130, 40, "分支 B (Q=0.4)", fill=C.white, stroke=C.line, tc=C.soft, fs=10.5, weight=400)
c3 = f.box(580, 190, 130, 40, "分支 C (未探)", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=10.5, weight=400)
for b in [c1, c2, c3]:
    f.elbow([(460, 128), (460, 156), (b["cx"], 156), (b["cx"], b["top"][1])], color=C.faint)
g1 = f.box(150, 290, 130, 40, "…更优", fill=C.green_s, stroke=C.green, tc="#166534", fs=10.5, weight=400)
f.elbow([(285, 230), (285, 260), (215, 260), (215, 286)], color=C.faint)
f.text(460, 380, "UCB1 平衡『利用(高 Q)』与『探索(低访问次数)』;LLM 提供策略先验与价值评估", 12.5, C.ink, 600)
f.note(460, 414, "AlphaGo → ToT → o1 风格推理模型的血脉:推理时多花算力 = 搜索更深(第 43.4/93.4 节)", 12, C.faint, anchor="middle")
f.save("fig-mcts")

# ---- 77 bdi (ch95) --------------------------------------------------------------
f = F(920, 380)
f.text(460, 30, "BDI:信念-愿望-意图(1988) 与 LLM Agent 的对照", 17, C.ink, 800)
rows = [
    ("信念 Belief", "对世界状态的知识", "≈ 上下文 + 检索到的事实(可能过时/有噪声)", C.blue),
    ("愿望 Desire", "想达成的目标集合", "≈ 用户目标 + 系统提示词中的偏好", C.teal),
    ("意图 Intention", "承诺执行的计划子集", "≈ 当前 plan 与进行中的工具调用链", C.indigo),
]
y = 76
for bdi, b, l, colr in rows:
    f.box(60, y, 200, 64, bdi, fill=SOFT[colr], stroke=colr, tc=colr, fs=13.5)
    f.text(290, y + 26, b, 12, C.soft, 600, anchor="start")
    f.text(290, y + 46, l, 12, C.ink, 500, anchor="start")
    y += 84
f.text(460, 340, "BDI 的现代启示:『意图』需要可撤销 —— 计划要能随信念更新而重审(对比 plan-execute 的 Replan)", 12, C.faint, 600)
f.note(460, 366, "PRSoar/ACT-R 认知架构 → 如今的『Agent 运行时』设计仍能看到影子:工作记忆、产生式规则、学习机制", 12, C.faint, anchor="middle")
f.save("fig-bdi")

# ---- 78 bandit (ch96) -------------------------------------------------------------
f = F(880, 380)
f.text(440, 30, "多臂老虎机:Agent 的『先试后定』决策", 17, C.ink, 800)
arms = [("工具 A\n已知好\nμ̂=0.8", C.teal), ("工具 B\n不确定\nμ̂=0.5±0.4", C.amber), ("工具 C\n全新\n未探索", C.indigo)]
for i, (t, colr) in enumerate(arms):
    f.box(110 + i * 220, 90, 180, 90, t, fill=C.white, stroke=colr, tc=colr, fs=12, weight=400)
    f.raw('<line x1="%d" y1="86" x2="%d" y2="60" stroke="%s" stroke-width="2"/>' % (200 + i * 220, 200 + i * 220, colr))
f.text(440, 226, "ε-greedy: 以 ε 概率随机探索,否则选当前最优  |  Thompson 采样: 按后验概率抽臂 —— Agent 工具选择的天然框架", 12.5, C.ink, 600)
f.group(90, 260, 700, 80, "应用场景")
f.text(110, 300, "多个检索源选谁? · 多个模型路由给谁? · A/B 新 prompt? —— 都是『探索-利用』问题", 12.5, C.soft, 400, anchor="start")
f.note(440, 366, "上下文Bandit(Contextual Bandit)加入特征 → 与 LLM 路由器结合是 2025 热门工程方向", 12, C.faint, anchor="middle")
f.save("fig-bandit")

# ---- 79 world model (ch97) ---------------------------------------------------------
f = F(920, 400)
f.text(460, 30, "世界模型:在『脑内』模拟,而不是每次都试真的", 17, C.ink, 800)
real = f.box(70, 90, 220, 90, "真实环境", "慢 · 贵 · 有风险\n(浏览器/机器人/生产库)", fill=C.gray_s, stroke=C.line, fs=12)
wm = f.box(370, 90, 220, 90, "学到的世界模型", "预测: 状态 s,动作 a\n→ 下一状态 s' 与奖励", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12)
plan = f.box(670, 90, 210, 90, "想象中规划", "Dyna 式: 在模型里\nrollout 千次选最优", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12)
f.arrow(290, 135, 366, 135, color=C.faint)
f.arrow(590, 135, 666, 135, color=C.faint)
f.elbow([(775, 180), (775, 250), (180, 250), (180, 184)], label="少量真实交互校准模型", color=C.faint, dash="5 4")
f.group(70, 280, 810, 90, "LLM 天然是文本世界的世界模型")
f.mtext(90, 316, ["代码解释器 = 可执行世界模型 · 浏览器模拟器 · 游戏引擎(Genie 系列:帧→帧可玩世界)", ""], 12.5, C.ink, 400, 1.9, anchor="start")
f.mtext(90, 344, ["风险:模型偏差会被规划放大 —— 『想象中必胜』≠『现实可行』,需定期回到真实环境校准。"], 12.5, C.ink, 400, 1.9, anchor="start")
f.save("fig-world-model")

# ---- 80 paper map (ch101) ----------------------------------------------------------
f = F(960, 520)
f.text(480, 32, "Agent 核心论文地图(按阅读顺序)", 18, C.ink, 800)
roots = [
    ("范式奠基", 70, ["InstructGPT (2022)", "ReAct (2022.10)", "Toolformer (2023.2)", "HuggingGPT (2023.3)"], C.indigo),
    ("推理增强", 280, ["CoT (2022.1)", "ToT (2023.5)", "Self-Refine (2023.3)", "Reflexion (2023.3)", "LATS (2023.10)"], C.teal),
    ("记忆与检索", 490, ["RAPTOR (2024)", "MemGPT (2023.10)", "Self-RAG (2023.10)", "GraphRAG (2024.4)"], C.blue),
    ("多智能体", 700, ["CAMEL (2023.3)", "MetaGPT (2023.8)", "AutoGen (2023.8)", "AgentVerse (2023.8)"], C.purple),
]
for name, x, papers, colr in roots:
    f.box(x, 70, 190, 44, name, fill=SOFT[colr], stroke=colr, tc=colr, fs=13.5)
    y = 140
    for p in papers:
        f.box(x + 8, y, 174, 38, p, fill="#ffffff", stroke=C.line, tc=C.ink, fs=10.5, weight=400)
        y += 46
f.box(70, 360, 820, 44, "训练与强化 → 见第 102 章专题地图(SFT/RLHF/DPO/RLVR/AgentRL 五波)", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=12.5)
f.box(70, 420, 820, 44, "评测与安全 → 见第 103 章专题地图(SWE-bench/WebArena/InjecAgent/AgentDojo)", fill=C.red_s, stroke=C.red, tc=C.red_d, fs=12.5)
f.note(480, 498, "阅读策略:每列自上而下;先读完『范式奠基』再横向扩展 —— 论文精读见第 100 章", 12, C.faint, anchor="middle")
f.save("fig-paper-map")

# ---- 81 framework map (ch105) -------------------------------------------------------
f = F(960, 520)
f.text(480, 32, "框架生态地图:按『抽象层级』放置", 18, C.ink, 800)
bands = [
    ("应用平台(托管)", "Manus · Devin · Claude Code · ChatGPT Agent · Dify Cloud", C.amber, C.amber_s),
    ("低代码编排", "Dify · Coze · n8n · Flowise · FastGPT", C.purple, C.purple_s),
    ("代码编排框架", "LangGraph · OpenAI Agents SDK · Claude Agent SDK · CrewAI · AutoGen(AG2) · LlamaIndex · PydanticAI · smolagents", C.indigo, C.indigo_s),
    ("协议与互操作", "MCP · A2A · AG-UI · OpenTelemetry GenAI", C.teal, C.teal_s),
    ("模型与推理底座", "OpenAI / Anthropic / Gemini / Qwen / DeepSeek · vLLM · Ollama · SGLang", C.blue, C.blue_s),
]
y = 80
for name, items, colr, colr_s in bands:
    f.box(60, y, 840, 64, name, items, fill=colr_s, stroke=colr, tc=colr, fs=13)
    y += 78
f.note(480, 492, "越往上越『开箱即用』但定制性低;越往下越自由但工程量大 —— 第 26 章决策树帮你选层", 12, C.faint, anchor="middle")
f.save("fig-framework-map")

# ---- 82 voice cascade (ch72) ---------------------------------------------------------
f = F(960, 400)
f.text(480, 30, "语音 Agent 的两条技术路线", 17, C.ink, 800)
f.group(60, 60, 400, 150, "级联式(传统,可控)")
f.mtext(80, 98, ["ASR(语音→文本) → LLM → TTS(文本→语音)", "✓ 每环节可独立优化/替换  ✗ 级联延迟 800ms+", "✗ 丢失语气/情感/副语言信息"], 11.5, C.soft, 400, 1.8, anchor="start")
f.group(520, 60, 380, 150, "端到端(新范式,拟人)")
f.mtext(540, 98, ["语音直接进多模态模型 → 语音直接出", "✓ 延迟 300ms 内 · 可打断 · 情感丰富", "✗ 黑盒调优难 · 幻觉不可见(无文本中间态)"], 11.5, C.soft, 400, 1.8, anchor="start")
f.raw('<rect x="60" y="240" width="840" height="80" rx="12" fill="%s" stroke="%s"/>' % (C.indigo_s, C.indigo))
f.mtext(480, 268, ["电话/实时对话的延迟预算: 用户感知『即时』< 500ms;打断(barge-in)与回声消除是工程生命线"], 12.5, C.indigo_d, 600, 1.8)
f.note(480, 372, "生产建议:客服等合规敏感场景用级联(要审计文本);陪伴/教练类体验优先端到端", 12, C.faint, anchor="middle")
f.save("fig-voice-cascade")

# ---- 83 appendix timeline (appA) ------------------------------------------------------
f = F(980, 560)
f.text(490, 32, "Agent 大事记(详见附录 A 全文)", 18, C.ink, 800)
y = 80
rows = [
    ("1950-1990", "符号主义时代", "图灵测试 · 达特茅斯 · BDI · Soar/ACT-R 认知架构", C.faint),
    ("1990-2012", "概率与学习", "贝叶斯网络 · RL 奠定(Q-learning/SARSA) · 深蓝", C.teal),
    ("2013-2016", "深度 RL", "DQN · AlphaGo:搜索+学习击败世界冠军", C.blue),
    ("2017-2021", "Transformer 纪元", "Attention · BERT · GPT-3 上下文学习 · 群体百模", C.indigo),
    ("2022", "对齐与推理", "InstructGPT/ChatGPT · CoT · ReAct · Toolformer", C.purple),
    ("2023", "Agent 元年", "AutoGPT · LangChain 爆发 · MetaGPT/AutoGen · MemGPT · GPTs", C.purple),
    ("2024", "工程化深耕", "SWE-bench Verified · MCP 发布 · o1 推理范式 · 计算机使用预览", C.amber),
    ("2025", "推理与自主", "DeepSeek-R1 开源复现 · Claude Code · Deep Research · A2A · Agent RL 化", C.amber),
    ("2026 →", "物理与世界模型", "Computer Use 成熟 · VLA 机器人 · 长时程 Agent · 世界模型训练", C.red),
]
for span, name, desc, colr in rows:
    f.raw('<rect x="60" y="%d" width="130" height="40" rx="8" fill="%s"/>' % (y, colr_s if colr != C.faint else C.gray_s))
    f.text(125, y + 25, span, 11.5, C.ink, 800)
    f.text(210, y + 17, name, 13, C.ink, 700, anchor="start")
    f.text(210, y + 35, desc, 11, C.soft, 400, anchor="start")
    y += 50
f.note(490, 544, "每一个拐点背后都是一篇论文与一次工程化 —— 全文与链接见附录 A", 12, C.faint, anchor="middle")
f.save("fig-appendix-timeline")

# ---- 84 interview radar (ch110) -------------------------------------------------------
f = F(880, 400)
f.text(440, 30, "Agent 工程师能力雷达(面试考察维度)", 17, C.ink, 800)
import math
cx, cy, R = 440, 225, 130
axes = ["LLM 原理", "提示工程", "Agent 架构", "数据与训练", "评测体系", "安全合规", "系统工程", "产品思维"]
vals = [0.7, 0.85, 0.9, 0.6, 0.8, 0.55, 0.75, 0.7]
n = len(axes)
pts = []
for i, (a, v) in enumerate(zip(axes, vals)):
    ang = math.pi * 2 * i / n - math.pi / 2
    x, y = cx + R * v * math.cos(ang), cy + R * v * math.sin(ang)
    pts.append((x, y))
for ring in (0.33, 0.66, 1.0):
    pp = [(cx + R * ring * math.cos(math.pi * 2 * i / n - math.pi / 2),
           cy + R * ring * math.sin(math.pi * 2 * i / n - math.pi / 2)) for i in range(n)]
    f.raw('<polygon points="%s" fill="none" stroke="%s" stroke-width="1"/>' % (" ".join("%s,%s" % (round(x), round(y)) for x, y in pp), C.line))
for i in range(n):
    f.raw('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>' % (cx, cy, cx + R * math.cos(math.pi * 2 * i / n - math.pi / 2), cy + R * math.sin(math.pi * 2 * i / n - math.pi / 2), C.line))
f.raw('<polygon points="%s" fill="%s" opacity="0.55" stroke="%s" stroke-width="2"/>' % (" ".join("%s,%s" % (round(x), round(y)) for x, y in pts), C.indigo_s, C.indigo))
for i, (a, v) in enumerate(zip(axes, vals)):
    ang = math.pi * 2 * i / n - math.pi / 2
    f.text(cx + (R + 26) * math.cos(ang), cy + (R + 26) * math.sin(ang) + 4, a, 11.5, C.ink, 700)
f.note(440, 382, "高分项通常是『Agent 架构 + 提示工程 + 评测』;数据训练维度对研究员岗要求更高", 12, C.faint, anchor="middle")
f.save("fig-interview-radar")

print("figures_c done")
