# -*- coding: utf-8 -*-
"""figures_a.py — 导论/基础/核心机制篇插图 (fig 01-40)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 01 学习路径 (ch2) -------------------------------------------------
f = F(960, 430)
f.text(480, 40, "AI Agent 学习路径总览", 19, C.ink, 800)
f.text(480, 64, "三条路线共享同一套地基，可在任意路口切换", 12.5, C.faint)
top = f.box(370, 92, 220, 56, "共同地基", "第 1 部分 · LLM 与提示工程", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
paths = [
    (40, C.teal, C.teal_s, C.teal_d, "🧱 入门者路线", "建立直觉、跑通第一个 Agent", ["ch14–17 核心机制", "ch26–27 技术栈与手写", "ch81–88 八个实战项目"]),
    (360, C.indigo, C.indigo_s, C.indigo_d, "🛠 工程师路线", "把 Agent 做成可靠的产品", ["ch17–25 全部机制", "ch28–37 框架与协议", "ch50–57 评测与 CI"]),
    (680, C.purple, C.purple_s, C.purple_d, "🔬 研究者路线", "理解原理并推进前沿", ["ch38–49 训练与强化", "ch91–98 理论基础", "ch99–104 论文地图"]),
]
for x, acc, acc_s, acc_d, title, sub, items in paths:
    f.elbow([(top["cx"], 148), (top["cx"], 178), (x + 120, 178), (x + 120, 206)], color=C.faint, sw=1.5)
    f.box(x, 206, 240, 54, title, sub, fill=acc_s, stroke=acc, tc=acc_d)
    f.group(x, 272, 240, 130, "主线章节", fill="#ffffff", stroke=C.line)
    f.mtext(x + 20, 310, items, 12, C.soft, 400, 1.8, anchor="start")
f.note(480, 424, "全书 113 章 + 4 附录 · 每章末尾配有「小结—自测—延伸阅读」三件套", 11.5, C.faint, anchor="middle")
f.save("fig-learning-paths")

# ---- 02 历史时间线 (ch3) ------------------------------------------------
f = F(960, 470)
f.text(480, 36, "Agent 思想与实现的七十年", 19, C.ink, 800)
y = 250
f.raw('<line x1="50" y1="%d" x2="910" y2="%d" stroke="%s" stroke-width="3"/>' % (y, y, C.line))
events = [
    (1950, "图灵测试", "图灵《计算机器与智能》", C.faint, "above"),
    (1956, "达特茅斯会议", "「人工智能」命名", C.faint, "below"),
    (1977, "BDI / 符号Agent", "Belief-Desire-Intention", C.teal, "above"),
    (1986, "Soar 认知架构", "通用认知模型", C.teal, "below"),
    (1997, "深蓝", "搜索+评估函数", C.teal, "above"),
    (2013, "Word2Vec / DQN", "深度强化学习觉醒", C.blue, "below"),
    (2017, "Transformer", "Attention Is All You Need", C.indigo, "above"),
    (2020, "GPT-3", "上下文学习涌现", C.indigo, "below"),
    (2022, "ChatGPT / ReAct", "对话智能体 + 推理行动范式", C.indigo, "above"),
    (2023, "AutoGPT / 工具调用", "Agent 元年", C.purple, "below"),
    (2024, "SWE-bench / MCP", "工程化与协议标准化", C.purple, "above"),
    (2025, "RLVR / o1→R1", "推理模型与 Deep Research", C.amber, "below"),
    (2026, "Computer Use 时代", "Agent 直接操作数字世界", C.amber, "above"),
]
import math
for i, (year, title, sub, colr, pos) in enumerate(events):
    x = 50 + i * (860 / (len(events) - 1))
    f.raw('<circle cx="%d" cy="%d" r="6" fill="%s"/>' % (x, y, colr))
    f.text(x, y + (26 if pos == "below" else -38), str(year), 12.5, colr, 800)
    if pos == "below":
        f.mtext(x, y + 44, wrap(title, 90, 12), 12, C.ink, 700, 1.35)
        f.mtext(x, y + 44 + len(wrap(title, 90, 12)) * 15 + 2, wrap(sub, 110, 10.5), 10.5, C.faint, 400, 1.3)
    else:
        f.mtext(x, y - 58, wrap(title, 90, 12), 12, C.ink, 700, 1.35, anchor="middle")
        f.mtext(x, y - 58 + len(wrap(title, 90, 12)) * 14 + 1, wrap(sub, 110, 10.5), 10.5, C.faint, 400, 1.3)
f.note(480, 448, "符号主义 → 认知架构 → 深度学习 → LLM → 工具增强 → 强化训练 → 物理与世界模型", 12, C.faint, anchor="middle")
f.save("fig-history-timeline")

# ---- 03 Transformer block (ch4) ------------------------------------------
f = F(760, 560)
f.text(380, 34, "Decoder-only Transformer 单层结构", 17, C.ink, 800)
bx, bw = 230, 300
flow = [
    ("输入 Embedding + 位置编码", C.gray_s, C.line, C.ink, 62, 40),
    ("Masked Multi-Head Self-Attention", C.indigo_s, C.indigo, C.indigo_d, 142, 46),
    ("Add & LayerNorm", C.gray_s, C.line, C.ink, 228, 34),
    ("前馈网络 FFN（4× 扩展）", C.teal_s, C.teal, C.teal_d, 302, 46),
    ("Add & LayerNorm", C.gray_s, C.line, C.ink, 388, 34),
    ("输出分布 Softmax(logits)", C.amber_s, C.amber, C.amber_d, 462, 40),
]
boxes = []
for label, fill, stroke, tc, y0, h in flow:
    boxes.append(f.box(bx, y0, bw, h, label, fill=fill, stroke=stroke, tc=tc, fs=13.5))
for i in range(len(boxes) - 1):
    a, b = boxes[i], boxes[i + 1]
    f.arrow(a["cx"], a["bottom"][1], b["cx"], b["top"][1], color=C.faint)
# residuals
for src, dst in [(0, 2), (2, 4)]:
    a, b = boxes[src], boxes[dst]
    sx = bx + bw
    f.elbow([(sx + 14, a["bottom"][1]), (sx + 46, a["bottom"][1]), (sx + 46, b["cy"]), (sx + 14, b["cy"])],
            color=C.purple, sw=1.5, dash="5 4")
f.text(bx + bw + 58, 300, "残差", 12, C.purple, 700)
f.text(bx + bw + 58, 316, "连接", 12, C.purple, 700)
f.group(30, 110, 160, 250, "为什么 Agent 关心?")
f.mtext(48, 152, ["• 注意力 = 读上下文", "  的方式,决定长文", "  检索能力", "• KV Cache 决定多轮", "  对话的成本曲线", "• 上下文窗口 = Agent", "  的『工作记忆』上限"], 11.8, C.soft, 400, 1.75, anchor="start")
f.note(380, 540, "同一结构堆叠 N 层(32~100+),参数量从 7B 到 1T 不等", 12, C.faint, anchor="middle")
f.save("fig-transformer-block")

# ---- 04 自回归生成 (ch4) -------------------------------------------------
f = F(900, 330)
f.text(450, 34, "自回归生成:一次只预测下一个 Token", 17, C.ink, 800)
seq = ["<用户>", "帮我", "订", "明天", "的", "机票"]
x = 60
cells = []
for s in seq:
    w = tw(s, 14) + 24
    f.box(x, 80, w, 40, s, fill=C.gray_s, stroke=C.line, fs=14)
    cells.append((x, w))
    x += w + 8
last = x - 8
f.box(x + 8, 80, 110, 40, "? 下一个", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=14)
f.arrow(last + 14, 100, x + 2, 100, color=C.amber)
cand = [("北京", 0.42, C.indigo), ("上海", 0.31, C.teal), ("杭州", 0.12, C.blue), ("其他…", 0.15, C.faint)]
cx0 = x + 63
f.text(cx0, 158, "概率分布 P(next token | 前文)", 12.5, C.soft, 700)
bx0 = cx0 - 210
for i, (tok, p, colr) in enumerate(cand):
    yy = 182 + i * 30
    f.text(bx0, yy + 12, tok, 12.5, C.ink, 600, anchor="start")
    f.raw('<rect x="%d" y="%d" width="%d" height="16" rx="4" fill="%s" opacity="0.85"/>'
          % (bx0 + 60, yy, p * 280, colr))
    f.text(bx0 + 60 + p * 280 + 10, yy + 12.5, "%.2f" % p, 11, C.faint, 600, anchor="start")
f.group(660, 150, 210, 130, "Agent 视角")
f.mtext(678, 188, ["下一个 token 完全由", "「已生成的全部内容」", "决定 —— 这就是为什么", "上下文管理 = 一切。"], 12, C.soft, 400, 1.7, anchor="start")
f.note(450, 316, "生成 = 循环:拼接 → 前向 → 采样 → 拼接 … 直到 <eos> 或触发工具调用", 12, C.faint, anchor="middle")
f.save("fig-autoregressive")

# ---- 05 tokenizer (ch5) --------------------------------------------------
f = F(920, 300)
f.text(460, 32, "同一个问题,不同语言/写法的 Token 数量不同", 17, C.ink, 800)
rows = [
    ("What is the capital of France?", "7 tokens", 0.55, C.blue),
    ("法国的首都是哪里?", "12 tokens", 0.85, C.indigo),
    ("法国的首都是哪里?请给出简短答案。", "29 tokens", 1.7, C.purple),
]
yy = 80
for text, label, scale, colr in rows:
    w = tw(text, 13.5) + 28
    f.box(70, yy, w, 40, text, fill="#ffffff", stroke=C.line, fs=13.5, weight=400)
    f.raw('<rect x="70" y="%d" width="%d" height="8" rx="4" fill="%s"/>' % (yy + 52, 130 + scale * 260, colr))
    f.text(70 + 130 + scale * 260 + 14, yy + 60, label, 12.5, colr, 700, anchor="start")
    yy += 78
f.group(640, 66, 240, 170, "对 Agent 的意义")
f.mtext(658, 104, ["1 Token ≈ 0.75 个英文", "单词 ≈ 0.5 个汉字;", "中文任务的上下文", "成本约为英文的 1.5~2 倍,", "预算要按 Token 记账。"], 12, C.soft, 400, 1.7, anchor="start")
f.note(460, 282, "Tokenizer 把文本切成子词单元(BPE/tiktoken),计费、限速、上下文窗口全部按 Token 计", 12, C.faint, anchor="middle")
f.save("fig-tokenizer")

# ---- 06 sampling (ch5) ---------------------------------------------------
f = F(900, 360)
f.text(450, 32, "采样策略:确定性与多样性的旋钮", 17, C.ink, 800)
dists = [("temperature = 0\n(greedy)", "永远选最高分", "适合:工具调用\n代码生成", C.indigo, C.indigo_s),
         ("top-p = 0.9\n(nucleus)", "只从累计概率 90%\n的候选中采样", "适合:文案创意\n对话润色", C.teal, C.teal_s),
         ("temperature = 1.2\n(high)", "分布更平坦\n更容易出惊喜/胡话", "适合:头脑风暴\n数据增强", C.amber, C.amber_s)]
for i, (t1, t2, t3, colr, colr_s) in enumerate(dists):
    x = 50 + i * 290
    f.box(x, 70, 260, 66, t1, fill=colr_s, stroke=colr, tc=colr, fs=13)
    f.text(x + 130, 160, t2, 12.5, C.soft, 400)
    f.box(x + 20, 182, 220, 54, t3.replace("\n", " · "), fill="#ffffff", stroke=C.line, fs=11.5, weight=400, tc=C.soft)
    # mini distribution
    bx = x + 40
    hs = [(0.9, colr), (0.55, colr), (0.32, C.faint), (0.2, C.faint), (0.12, C.faint)]
    if i == 2: hs = [(0.42, colr), (0.38, colr), (0.34, colr), (0.3, colr), (0.26, colr)]
    for j, (hh, c2) in enumerate(hs):
        f.raw('<rect x="%d" y="%d" width="26" height="%d" rx="3" fill="%s"/>'
              % (bx + j * 38, 320 - hh * 100, hh * 100, c2))
    f.raw('<line x1="%d" y1="321" x2="%d" y2="321" stroke="%s" stroke-width="1.5"/>' % (bx - 6, bx + 38 * 5 - 6, C.line))
f.note(450, 348, "Agent 实战默认值:工具调用与规划步 temperature≈0~0.3;创作与改名类步骤可放宽", 12, C.faint, anchor="middle")
f.save("fig-sampling")

# ---- 07 prompt anatomy (ch6) ----------------------------------------------
f = F(920, 470)
f.text(460, 32, "一个工业级系统提示词的解剖", 17, C.ink, 800)
segs = [
    ("① 身份与角色", "你是 Acme 的订单客服 Agent,代表公司语气……", C.indigo, C.indigo_s),
    ("② 能力与工具", "可调用 search_orders / refund / escalate 三个工具……", C.teal, C.teal_s),
    ("③ 行为准则", "先澄清再行动;不确定时询问;禁止承诺退款上限以外的金额……", C.amber, C.amber_s),
    ("④ 输出契约", "始终以 JSON {intent, slots, confidence} 结尾……", C.blue, C.blue_s),
    ("⑤ 示例 (few-shot)", "…输入/输出示例 2~5 条,覆盖边界情况…", C.purple, C.purple_s),
    ("⑥ 上下文注入", "<user_profile>…</user_profile> <history>…</history>", C.green, C.green_s),
]
y = 60
for title, body, colr, colr_s in segs:
    h = 54
    f.box(60, y, 800, h, "", fill=colr_s, stroke=colr, rx=9)
    f.text(84, y + 24, title, 13.5, colr, 800, anchor="start")
    f.text(84, y + 42, body, 12, C.soft, 400, anchor="start")
    y += h + 10
f.note(460, y + 22, "调试系统提示词时,按这六段逐一隔离变量 —— 一次只改一段", 12, C.faint, anchor="middle")
f.save("fig-prompt-anatomy")

# ---- 08 CoT compare (ch6) -------------------------------------------------
f = F(960, 380)
f.text(480, 32, "Chain-of-Thought:把「暗自计算」变成「显式草稿」", 17, C.ink, 800)
# left: direct
f.group(50, 60, 400, 260, "直接提问", fill="#ffffff")
f.box(80, 96, 340, 40, "Q: 罗杰有 5 个网球,又买 2 罐,每罐 3 个。一共?", fill=C.gray_s, stroke=C.line, fs=12, weight=400)
f.box(80, 156, 340, 46, "A: 11 个 ❌ (直接跳到答案)", fill=C.red_s, stroke=C.red, tc=C.red_d, fs=12.5)
f.mtext(250, 232, ["模型被迫一步到位,", "多步算术极易『心算翻车』。"], 12, C.faint, 400, 1.7)
# right: cot
f.group(510, 60, 400, 260, "加一句「让我们一步一步思考」", fill="#ffffff")
f.box(540, 96, 340, 40, "Q: (同一个问题)", fill=C.gray_s, stroke=C.line, fs=12, weight=400)
f.box(540, 150, 340, 60, "思考: 已有 5 个;2 罐 × 3 个 = 6 个;\n5 + 6 = 11", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12, weight=400)
f.box(540, 226, 340, 40, "A: 11 个 ✓", fill=C.green_s, stroke=C.green, tc="#166534", fs=12.5)
f.arrow(450, 190, 505, 190, color=C.faint, sw=1.6)
f.text(477, 178, "CoT", 12.5, C.indigo, 800)
f.note(480, 352, "推理 Token 是『工作内存的外化』;ReAct 把同一思想推广到「思考 + 行动」交替", 12, C.faint, anchor="middle")
f.save("fig-cot-compare")

# ---- 09 prompt chain (ch7) ------------------------------------------------
f = F(960, 300)
f.text(480, 32, "提示链:一次复杂任务 = 多个简单任务的流水线", 17, C.ink, 800)
steps = [("抽取", "从原文抽结构化要点"), ("扩展", "每个要点写成段落"), ("检查", "对照原文核对事实"), ("定稿", "统一语气并排版")]
x = 60
cs = []
for i, (t, s) in enumerate(steps):
    b = f.box(x, 80, 180, 70, t, s, fill=C.indigo_s if i % 2 == 0 else C.teal_s,
              stroke=C.indigo if i % 2 == 0 else C.teal, tc=C.indigo_d if i % 2 == 0 else C.teal_d)
    cs.append(b)
    if i < 3:
        f.arrow(b["right"][0] + 4, 115, b["right"][0] + 34, 115, color=C.faint)
    x += 214
f.pill(480, 200, "每一步只做一件事 → 每一步都可单独测试、缓存、替换模型", fill=C.amber_s, tc=C.amber_d, fs=12.5)
f.note(480, 268, "失败排查从『整条链』缩小到『单步』;这正是 Agent 可维护性的来源", 12, C.faint, anchor="middle")
f.save("fig-prompt-chain")

# ---- 10 self-consistency (ch7) --------------------------------------------
f = F(900, 380)
f.text(450, 32, "Self-Consistency:采样多条思路,投票取众数", 17, C.ink, 800)
q = f.box(350, 64, 200, 44, "同一问题 + CoT", fill=C.gray_s, stroke=C.line)
import math
routes = [("推理路径 A → 42", 3, C.indigo, C.indigo_s), ("推理路径 B → 17", 1, C.faint, C.gray_s),
          ("推理路径 C → 42", 3, C.indigo, C.indigo_s), ("推理路径 D → 42", 3, C.indigo, C.indigo_s)]
for i, (label, votes, colr, colr_s) in enumerate(routes):
    y = 150 + i * 52
    f.elbow([(450, 108), (450, 126), (200, 126), (200, y + 22), (240, y + 22)], color=C.faint, sw=1.4, dash="4 4")
    f.box(240, y, 250, 44, label, fill=colr_s if votes > 1 else "#ffffff", stroke=colr, tc=C.ink if votes > 1 else C.faint, fs=12.5)
ans = f.box(600, 240, 220, 60, "最终答案: 42", "4/4 条路径投票 · 置信度高", fill=C.green_s, stroke=C.green, tc="#166534", fs=14)
for i in range(4):
    y = 150 + i * 52
    f.elbow([(490, y + 22), (600 + 110, y + 22), (600 + 110, 236)], color=C.faint, sw=1.4, dash="4 4")
f.note(450, 358, "代价:成本 × N;常用于数学/代码等可自动判分的场合,与多数投票(Majority Vote)配合", 12, C.faint, anchor="middle")
f.save("fig-self-consistency")

# ---- 11 constrained decoding (ch8) -----------------------------------------
f = F(920, 360)
f.text(460, 32, "受约束解码:让『生成』服从『Schema』", 17, C.ink, 800)
f.box(60, 70, 240, 60, "Prompt + JSON Schema", "目标结构作为硬约束", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
f.box(380, 70, 200, 60, "解码器", "每一步屏蔽非法 Token", fill=C.teal_s, stroke=C.teal, tc=C.teal_d)
f.box(660, 70, 200, 60, '合法输出\n{"city": "北京"}', "100% 可解析", fill=C.green_s, stroke=C.green, tc="#166534", fs=12)
f.arrow(300, 100, 376, 100, color=C.faint)
f.arrow(580, 100, 656, 100, color=C.faint)
f.group(60, 170, 380, 150, "无约束(祈祷式)")
f.mtext(80, 208, ['模型输出:  好的!这是您要的 JSON:\n```json\n{"city": "北京", }'], 11.5, C.soft, 400, 1.6, anchor="start")
f.pill(250, 296, "解析失败率 2%~15%", fill=C.red_s, tc=C.red_d, fs=12)
f.group(520, 170, 340, 150, "Grammar 约束(GBNF / Outlines)")
f.mtext(540, 208, ["状态机屏蔽非法续写,\n括号、引号、逗号逐一校验"], 11.5, C.soft, 400, 1.6, anchor="start")
f.pill(690, 296, "解析失败率 ≈ 0%", fill=C.green_s, tc="#166534", fs=12)
f.note(460, 342, "OpenAI Structured Outputs / vLLM guided decoding / llama.cpp GBNF 都是这一思想", 12, C.faint, anchor="middle")
f.save("fig-constrained-decoding")

# ---- 12 hallucination (ch9) -------------------------------------------------
f = F(920, 400)
f.text(460, 32, "幻觉的三副面孔", 17, C.ink, 800)
cards = [
    ("事实性幻觉", "编造不存在的事实", "「GPT-5 于 2024 年发布,拥有 10 万亿参数」", C.red, C.red_s),
    ("忠实性幻觉", "回答与给定资料矛盾", "资料说『退款需 7 天』,回答却写『即时到账』", C.amber, C.amber_s),
    ("能力幻觉", "自信地使用不存在的能力", "调用一个从未注册过的工具 get_weather_2025", C.purple, C.purple_s),
]
for i, (t, s, ex, colr, colr_s) in enumerate(cards):
    x = 50 + i * 285
    f.box(x, 64, 265, 150, "", fill=colr_s, stroke=colr, rx=12)
    f.text(x + 132, 96, t, 15, colr, 800)
    f.text(x + 132, 120, s, 12.5, C.soft, 600)
    f.text(x + 132, 152, "例", 11, colr, 800)
    f.mtext(x + 132, 172, wrap(ex, 220, 11), 11, C.soft, 400, 1.6)
f.group(50, 240, 820, 120, "成因与对策")
f.mtext(70, 278, ["成因: 下一 Token 预测只求『局部合理』,不求『全局为真』;训练目标奖励流畅而非诚实。"], 12.5, C.ink, 600, 1.7, anchor="start")
f.mtext(70, 304, ["对策: 检索接地(RAG) · 引用与归因 · 不确定性表达(『我不确定』也是答案) · 工具校验 · 事后事实核查 Agent。"], 12.5, C.ink, 600, 1.7, anchor="start")
f.note(460, 382, "幻觉不是 bug 而是机制的副产品 —— Agent 的职责是给它装上『围栏』", 12, C.faint, anchor="middle")
f.save("fig-hallucination")

# ---- 13 embedding space (ch10) ---------------------------------------------
f = F(860, 420)
f.text(430, 32, "语义向量空间:意义相近 → 距离相近", 17, C.ink, 800)
f.raw('<circle cx="400" cy="240" r="150" fill="%s" opacity="0.5"/>' % C.indigo_s)
f.raw('<circle cx="620" cy="150" r="90" fill="%s" opacity="0.6"/>' % C.teal_s)
f.raw('<circle cx="560" cy="330" r="90" fill="%s" opacity="0.6"/>' % C.amber_s)
f.text(300, 128, "编程语言", 12.5, C.indigo_d, 700)
f.text(620, 108, "烹饪", 12.5, C.teal_d, 700)
f.text(560, 384, "旅游", 12.5, C.amber_d, 700)
pts = [("Python", 330, 200), ("Java", 380, 260), ("编译器", 420, 310), ("算法", 300, 280),
       ("烤箱", 640, 170), ("菜谱", 590, 200), ("东京", 545, 320), ("签证", 600, 350)]
for name, x, y in pts:
    colr = C.indigo if x < 520 and y < 290 else (C.teal if y < 250 else C.amber)
    f.raw('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x, y, colr))
    f.text(x, y - 11, name, 11, C.ink, 600)
q = (470, 245)
f.raw('<circle cx="%d" cy="%d" r="9" fill="%s" stroke="#fff" stroke-width="2"/>' % (q[0], q[1], C.red))
f.text(q[0] + 2, q[1] - 15, "查询: '垃圾回收'", 12, C.red, 800)
f.raw('<line x1="%d" y1="%d" x2="380" y2="260" stroke="%s" stroke-width="1.6" stroke-dasharray="5 4"/>' % (q[0], q[1], C.red))
f.raw('<line x1="%d" y1="%d" x2="330" y2="200" stroke="%s" stroke-width="1.2" stroke-dasharray="5 4"/>' % (q[0], q[1], C.red))
f.note(430, 412, "文本 → Embedding → 高维向量(768~3072 维);余弦相似度检索;这是 RAG 与长期记忆的地基", 12, C.faint, anchor="middle")
f.save("fig-embedding-space")

# ---- 14 api patterns (ch12) -------------------------------------------------
f = F(920, 420)
f.text(460, 32, "调用 LLM API 的四种必备工程姿势", 17, C.ink, 800)
cards = [
    ("指数退避重试", "429/5xx → 1s, 2s, 4s…\n最多 6 次 + 抖动", C.indigo, C.indigo_s),
    ("客户端限流", "令牌桶:按 TPM/RPM\n本地排队,避免雪崩", C.teal, C.teal_s),
    ("流式输出", "SSE 逐 Token 推送,\n首字延迟 < 1s", C.purple, C.purple_s),
    ("成本护栏", "每次调用记账;\n超预算自动降级模型", C.amber, C.amber_s),
]
for i, (t, s, colr, colr_s) in enumerate(cards):
    x = 50 + i * 212
    f.box(x, 70, 192, 110, t, fill=colr_s, stroke=colr, tc=colr, fs=14)
    f.mtext(x + 96, 130, s.split("\n"), 11.5, C.soft, 400, 1.7)
f.group(50, 210, 820, 170, "一次『礼貌』的失败重试")
f.lane(60, 250, 800, 116, "时间线 →", w_head=90)
f.text(170, 274, "请求 → 429 Too Many Requests", 11.5, C.red, 600, anchor="start")
f.text(170, 296, "等待 1.2s(基础 × 随机抖动)", 11.5, C.soft, 400, anchor="start")
f.text(170, 318, "请求 → 429 → 等待 2.8s → 请求 → 200 OK ✓", 11.5, C.green, 600, anchor="start")
f.note(460, 402, "生产 Agent 的可用性 = 模型质量 × 工程鲁棒性;后者便宜且立竿见影", 12, C.faint, anchor="middle")
f.save("fig-api-patterns")

# ---- 15 eval loop (ch13) ----------------------------------------------------
f = F(880, 400)
f.text(440, 32, "评测驱动的开发闭环", 17, C.ink, 800)
b1 = f.box(80, 80, 180, 56, "① 固定测试集", "50~500 条真实场景", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
b2 = f.box(340, 80, 180, 56, "② 跑改动版本", "新 Prompt / 新模型", fill=C.teal_s, stroke=C.teal, tc=C.teal_d)
b3 = f.box(600, 80, 200, 56, "③ 打分", "规则 / 模型裁判 / 人工", fill=C.amber_s, stroke=C.amber, tc=C.amber_d)
b4 = f.box(600, 230, 200, 56, "④ 显著性检验", "别被 ±2% 噪声骗了", fill=C.purple_s, stroke=C.purple, tc=C.purple_d)
b5 = f.box(340, 230, 180, 56, "⑤ 归因分析", "看失败案例,不改感觉", fill=C.blue_s, stroke=C.blue, tc=C.blue_d)
b6 = f.box(80, 230, 180, 56, "⑥ 迭代", "带着证据回到 ①", fill=C.green_s, stroke=C.green, tc="#166534")
for a, b in [(b1, b2), (b2, b3)]:
    f.arrow(a["right"][0], a["cy"], b["x"], b["cy"], color=C.faint)
f.arrow(b3["bottom"][0], b3["bottom"][1], b4["top"][0], b4["top"][1], color=C.faint)
f.arrow(b4["left"][0], b4["cy"], b5["right"][0], b5["cy"], color=C.faint)
f.arrow(b5["left"][0], b5["cy"], b6["right"][0], b6["cy"], color=C.faint)
f.elbow([(b6["cx"], b6["top"][1]), (b6["cx"], 62), (b1["cx"], 62), (b1["cx"], b1["top"][1])], color=C.faint)
f.note(440, 360, "没有评测集的 Prompt 调优 = 没有测试的代码重构;『感觉变好了』在统计上毫无意义", 12, C.faint, anchor="middle")
f.save("fig-eval-loop")

# ---- 16 autonomy ladder (ch14) -----------------------------------------------
f = F(920, 430)
f.text(460, 32, "自主性光谱:从 Workflow 到全自主 Agent", 17, C.ink, 800)
levels = [
    ("L0", "纯提示", "单次问答,无工具", C.faint, C.gray_s),
    ("L1", "工作流", "固定管线,人编排每一步", C.blue, C.blue_s),
    ("L2", "路由器", "LLM 决定走哪条预设路径", C.teal, C.teal_s),
    ("L3", "工具循环", "LLM 在循环中自选工具(ReAct)", C.indigo, C.indigo_s),
    ("L4", "自规划", "自行分解任务、自反思、跨多步", C.purple, C.purple_s),
    ("L5", "全自主", "长时程自驱,自建工具与子任务", C.amber, C.amber_s),
]
x = 55
for code, name, desc, colr, colr_s in levels:
    h = 64 + (len(levels) - 1 - int(code[1])) * 8
    f.box(x, 330 - h, 128, h, "", fill=colr_s, stroke=colr, rx=10)
    f.text(x + 64, 330 - h + 26, code, 15, colr, 800)
    f.text(x + 64, 330 - h + 46, name, 12.5, C.ink, 700)
    f.mtext(x + 64, 330 - h + 66, wrap(desc, 108, 10.5), 10.5, C.soft, 400, 1.5)
    x += 140
f.arrow(60, 356, 860, 356, color=C.faint, sw=2, both=True)
f.text(120, 376, "可控性、可预测性 ↑", 12, C.blue, 700, anchor="start")
f.text(800, 376, "能力上限、不确定性 ↑", 12, C.amber, 700, anchor="end")
f.note(460, 410, "Anthropic《Building effective agents》:能用 Workflow 解决就别上 Agent —— 自主性是成本,不是勋章", 12, C.faint, anchor="middle")
f.save("fig-autonomy-ladder")

# ---- 17 agent anatomy (ch14) -------------------------------------------------
f = F(900, 470)
f.text(450, 32, "一个 LLM Agent 的解剖图", 17, C.ink, 800)
brain = f.box(330, 70, 240, 74, "🧠 LLM(策略中枢)", "读上下文 → 决定下一步", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=14)
parts = [
    (60, "📋 任务与目标", "用户请求、成功标准、约束", C.blue, C.blue_s),
    (330, "🧰 工具集", "函数 Schema、MCP、API", C.teal, C.teal_s),
    (600, "💾 记忆", "短期上下文 + 长期存储", C.amber, C.amber_s),
]
pb = []
for x, t, s, colr, colr_s in parts:
    pb.append(f.box(x, 200, 240, 62, t, s, fill=colr_s, stroke=colr, tc=colr, fs=13.5))
env = f.box(300, 330, 300, 60, "🌍 环境(External World)", "文件系统 · Web · API · 人", fill=C.gray_s, stroke=C.line, fs=13.5)
xs = [brain["cx"] - 120, brain["cx"], brain["cx"] + 120]
for b, sx in zip(pb, xs):
    f.arrow(sx, brain["bottom"][1], b["top"][0], b["top"][1], color=C.faint)
    f.arrow(b["bottom"][0], b["bottom"][1], sx, env["top"][1], color=C.faint)
    f.elbow([(sx + 26, env["top"][1]), (sx + 26, b["bottom"][1] + 30), (b["bottom"][0] + 60, b["bottom"][1] + 30),
             (b["bottom"][0] + 60, b["bottom"][1] + 4)], color=C.faint, sw=1.2, dash="4 4")
f.note(450, 428, "Agent = LLM + 工具 + 记忆 + 环境 + 循环;每个部件都会在后续章节单独展开", 12, C.faint, anchor="middle")
f.save("fig-agent-anatomy")

# ---- 18 agent loop (ch15) ------------------------------------------------------
f = F(880, 480)
f.text(440, 32, "Agent Loop:感知 → 思考 → 行动 → 观察", 17, C.ink, 800)
task = f.box(330, 60, 220, 48, "任务 + 工具 + 记忆", "初始化上下文", fill=C.gray_s, stroke=C.line, fs=13)
p1 = f.pill(440, 156, "①  感知 Perceive", fill=C.blue_s, tc=C.blue_d, fs=13.5)
p2 = f.pill(440, 216, "②  推理 & 决策 Reason", fill=C.indigo_s, tc=C.indigo_d, fs=13.5)
p3 = f.pill(440, 276, "③  行动 Act(调用工具)", fill=C.teal_s, tc=C.teal_d, fs=13.5)
p4 = f.pill(440, 336, "④  观察 Observe(结果回填)", fill=C.amber_s, tc=C.amber_d, fs=13.5)
f.arrow(440, 108, 440, 132, color=C.faint)
f.arrow(440, 174, 440, 198, color=C.faint)
f.arrow(440, 234, 440, 258, color=C.faint)
f.arrow(440, 294, 440, 318, color=C.faint)
d = f.diamond(700, 336, 130, 74, "完成?\n预算耗尽?")
f.elbow([(440, 354), (440, 390), (635, 390), (635, 376)], color=C.faint, sw=1.8)


f.elbow([(700, 373), (700, 416), (150, 416), (150, 156), (370, 156)], color=C.indigo, sw=1.8)
f.text(430, 408, "否 → 带着观察继续循环", 11.5, C.indigo, 700)
f.arrow(700, 299, 700, 130, label="是", color=C.green, sw=1.8)
f.box(620, 96, 160, 40, "✓ 交付结果", fill=C.green_s, stroke=C.green, tc="#166534", fs=13.5)
f.note(440, 462, "整个『循环体』就是一段 while:LLM 每轮输出要么是工具调用,要么是最终回答", 12, C.faint, anchor="middle")
f.save("fig-agent-loop")

# ---- 19 loop budget (ch15) -----------------------------------------------------
f = F(900, 380)
f.text(450, 32, "失控的循环:三种必须预设的『刹车』", 17, C.ink, 800)
rows = [
    ("步数上限", "max_steps = 25", "防止『无限重试同一失败调用』", C.red, C.red_s),
    ("预算上限", "max_cost = $2.00", "Token/工具费用双记账,超限优雅退出", C.amber, C.amber_s),
    ("时间上限", "timeout = 300s", "单工具超时 + 全局截止时间", C.blue, C.blue_s),
]
y = 70
for t, code, desc, colr, colr_s in rows:
    f.box(60, y, 200, 58, t, fill=colr_s, stroke=colr, tc=colr, fs=14)
    f.box(280, y, 250, 58, code, fill="#ffffff", stroke=C.line, fs=12.5, mono=True, tc=C.ink, weight=400)
    f.text(560, y + 34, desc, 12.5, C.soft, 400, anchor="start")
    y += 78
f.group(60, 300, 780, 60, "")
f.text(80, 336, "优雅退出 > 硬崩溃:超限时输出『已完成 X,卡在 Y,建议 Z』—— 永远给用户一个可用的答案", 12.5, C.ink, 600, anchor="start")
f.save("fig-loop-budget")

# ---- 20 ReAct (ch16) -----------------------------------------------------------
f = F(920, 520)
f.text(460, 30, "ReAct:Thought → Action → Observation 交替轨迹", 17, C.ink, 800)
f.box(60, 60, 250, 46, "用户: 谁获得了 2020 年\n奥斯卡最佳影片?", fill=C.gray_s, stroke=C.line, fs=12, weight=400)
trace = [
    ("Thought", "最佳影片是电影奖项,我需要查 2020 年(第 92 届)的结果。", C.indigo, C.indigo_s),
    ("Action", "search(query=\"92nd Academy Awards Best Picture\")", C.teal, C.teal_s),
    ("Observation", "第 92 届奥斯卡最佳影片:《寄生虫》(Parasite, 2019)", C.amber, C.amber_s),
    ("Thought", "结果指向《寄生虫》。为确认上映年份与获奖年份,再查一次。", C.indigo, C.indigo_s),
    ("Action", "search(query=\"Parasite film release year\")", C.teal, C.teal_s),
    ("Observation", "《寄生虫》2019 年上映,2020 年获最佳影片。", C.amber, C.amber_s),
    ("Thought", "证据一致,可以回答。", C.indigo, C.indigo_s),
    ("Final Answer", "2020 年奥斯卡最佳影片是韩国电影《寄生虫》。", C.green, C.green_s),
]
y = 128
for kind, txt, colr, colr_s in trace:
    h = 34 if kind != "Final Answer" else 40
    f.box(360, y, 500, h, "", fill=colr_s, stroke=colr, rx=8)
    f.text(378, y + 22, kind, 12, colr, 800, anchor="start")
    f.text(378 + tw(kind, 12) + 14, y + 22, txt if tw(txt, 11) < 420 else txt[:34] + "…", 11.5, C.ink, 400, anchor="start")
    y += h + 8
f.arrow(310, 106, 350, 140, color=C.faint)
f.group(40, 200, 280, 200, "为什么有效")
f.mtext(56, 240, ["• 思考外置 → 可审计", "• 行动后有真实反馈,", "  纠正推理方向", "• 比 CoT 多了『世界』,", "  比 Act-only 多了『脑』"], 12, C.soft, 400, 1.75, anchor="start")
f.note(460, 500, "Yao et al., 2022 · HotpotQA/Fever/ALFWorld/WebShop 全面超越 CoT 与 Act-only 基线", 12, C.faint, anchor="middle")
f.save("fig-react")

# ---- 21 fc sequence (ch17) ------------------------------------------------------
f = F(920, 440)
f.text(460, 30, "Function Calling 的完整时序", 17, C.ink, 800)
lanes = [("你的应用", 120, C.blue), ("LLM API", 460, C.indigo), ("外部工具", 780, C.teal)]
for name, x, colr in lanes:
    f.box(x - 80, 60, 160, 40, name, fill=colr_s if colr != C.blue else C.blue_s, stroke=colr, tc=colr, fs=13.5)
f.raw('<line x1="120" y1="100" x2="120" y2="400" stroke="%s" stroke-width="1.2" stroke-dasharray="3 4"/>' % C.line)
f.raw('<line x1="460" y1="100" x2="460" y2="400" stroke="%s" stroke-width="1.2" stroke-dasharray="3 4"/>' % C.line)
f.raw('<line x1="780" y1="100" x2="780" y2="400" stroke="%s" stroke-width="1.2" stroke-dasharray="3 4"/>' % C.line)
steps = [
    (120, 460, "① 发送消息 + 工具清单(JSON Schema)", C.blue, 130),
    (460, 460, "② 模型决定:调用 get_weather(city=\"北京\")", C.indigo, 175),
    (460, 120, "③ 返回 tool_call(名称+参数)", C.indigo, 220),
    (120, 780, "④ 应用真正执行工具调用", C.blue, 265),
    (780, 120, "⑤ 返回结果 {temp: 25}", C.teal, 310),
    (120, 460, "⑥ 结果注入上下文,再次请求", C.blue, 355),
    (460, 120, "⑦ 模型综合回答:北京今天 25°C,晴", C.indigo, 395),
]
for x1, x2, label, colr, y in steps:
    if x1 == x2:
        f.raw('<rect x="%d" y="%d" width="8" height="14" fill="none"/>' % (x1 - 4, y))
        f.text(x1 + 20, y + 8, label, 11.5, colr, 600, anchor="start", style='paint-order:stroke;stroke:#fff;stroke-width:3px;')
    else:
        f.arrow(x1 + (14 if x2 > x1 else -14), y, x2 - (14 if x2 > x1 else -14), y, color=colr, sw=1.7)
        f.text((x1 + x2) / 2, y - 8, label, 11.5, colr, 600, style='paint-order:stroke;stroke:#fff;stroke-width:3.5px;')
f.note(460, 424, "关键认知:『调用工具』的永远是你的代码,模型只输出意图 —— 这就是安全边界的来源", 12, C.faint, anchor="middle")
f.save("fig-fc-sequence")

# ---- 22 parallel tools (ch17) ---------------------------------------------------
f = F(880, 360)
f.text(440, 30, "并行工具调用:一次规划,多次执行", 17, C.ink, 800)
m = f.box(340, 60, 200, 50, "LLM 单次响应", "输出 3 个 tool_call", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
tools = ["get_weather(北京)", "get_weather(上海)", "get_flight(PEK→SHA)"]
tx = []
for i, t in enumerate(tools):
    b = f.box(60 + i * 270, 180, 230, 46, t, fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12.5)
    tx.append(b)
    f.elbow([(m["cx"], m["bottom"][1]), (m["cx"], 130), (b["cx"], 130), (b["cx"], b["top"][1])], color=C.faint)
f.pill(440, 280, "并发执行(线程/asyncio) → 3 个结果一次性回填 → 总延迟 ≈ 最慢者", fill=C.amber_s, tc=C.amber_d, fs=12.5)
f.note(440, 336, "注意:并行调用间不能有依赖;有依赖时退化为串行,并让模型明确说明顺序", 12, C.faint, anchor="middle")
f.save("fig-parallel-tools")

# ---- 23 planning tree (ch18) ----------------------------------------------------
f = F(920, 440)
f.text(460, 30, "任务分解:递归把目标变成可执行的叶子", 17, C.ink, 800)
root = f.box(360, 60, 200, 46, "目标: 发布产品官网", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=13.5)
subs = [("设计页面", 90, C.teal), ("写文案", 390, C.teal), ("部署上线", 690, C.teal)]
sb = []
for t, x, colr in subs:
    b = f.box(x, 170, 140, 44, t, fill=colr_s, stroke=colr, tc=colr, fs=12.5)
    sb.append(b)
    f.elbow([(root["cx"], root["bottom"][1]), (root["cx"], 130), (b["cx"], 130), (b["cx"], b["top"][1])], color=C.faint)
leaves = [("线框图", 60), ("配色/字体", 170), ("首页文案", 360), ("定价页文案", 470), ("买域名", 630), ("CI/CD", 730)]
for t, x in leaves:
    f.box(x, 290, 120, 40, t, fill="#ffffff", stroke=C.line, fs=11.5, weight=400)
for b, (l1, x1), (l2, x2) in [(sb[0], leaves[0], leaves[1]), (sb[1], leaves[2], leaves[3]), (sb[2], leaves[4], leaves[5])]:
    f.elbow([(b["cx"], b["bottom"][1]), (b["cx"], 260), ((x1 + 60 + x2 + 60) / 2, 260)], color=C.faint, dash="4 4")
    f.elbow([((x1 + 60 + x2 + 60) / 2, 260), (x1 + 60, 260), (x1 + 60, b["bottom"][1] + 34)], color=C.faint, dash="4 4") if False else None
    f.arrow((x1 + 60 + x2 + 60) / 2 - 30, 268, x1 + 60, 286, color=C.faint, sw=1.2)
    f.arrow((x1 + 60 + x2 + 60) / 2 + 30, 268, x2 + 60, 286, color=C.faint, sw=1.2)
f.pill(460, 380, "叶节点 = 一次工具调用就能完成的原子任务;分解深度 2~3 层通常足够", fill=C.amber_s, tc=C.amber_d, fs=12.5)
f.note(460, 424, "Tree of Thoughts / LLM+P / HTN 的共同直觉:先『横向展开』,再『纵向执行』", 12, C.faint, anchor="middle")
f.save("fig-planning-tree")

# ---- 24 plan-execute (ch18) -----------------------------------------------------
f = F(900, 420)
f.text(450, 30, "Plan-and-Execute:计划者与执行者分离", 17, C.ink, 800)
pl = f.box(80, 80, 200, 60, "🧭 Planner 规划者", "强模型 · 低频调用", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
ex = f.box(80, 240, 200, 60, "⚙️ Executor 执行者", "快模型 · 高频调用", fill=C.teal_s, stroke=C.teal, tc=C.teal_d)
plan = f.box(400, 80, 220, 110, "计划清单", "1. 检索 A\n2. 检索 B\n3. 汇总 C", fill="#ffffff", stroke=C.line, fs=12.5, weight=400)
re_ = f.diamond(510, 300, 150, 70, "结果\n符合预期?")
done = f.box(720, 270, 140, 56, "✓ 完成", fill=C.green_s, stroke=C.green, tc="#166534", fs=13.5)
f.arrow(pl["right"][0], pl["cy"], plan["x"], plan["cy"], label="生成计划", color=C.faint)
f.arrow(plan["left"][0] - 20, 200, 180, 236, color=C.faint)
f.text(300, 226, "逐步分发", 11.5, C.faint, 600)
f.elbow([(ex["right"][0], ex["cy"]), (435, ex["cy"]), (435, 300), (435, 300)], color=C.faint)
f.arrow(435, 300, 435, 300) if False else None
f.arrow(280, 300, 435, 300, color=C.faint, label="执行步骤")
f.arrow(585, 300, 640, 300, label="否 → 重规划", color=C.red, dash="5 4")
f.elbow([(510, 265), (510, 200), (622, 200)], color=C.green, sw=1.6)
f.text(560, 214, "是", 12, C.green, 700)
f.note(450, 392, "省钱的经典结构:贵模型只做一次规划,便宜模型执行 N 步;失败时回到 Planner 重规划(Replan)", 12, C.faint, anchor="middle")
f.save("fig-plan-execute")

# ---- 25 memory tiers (ch19) -----------------------------------------------------
f = F(920, 460)
f.text(460, 30, "记忆的四个层次:容量与持久性的交换", 17, C.ink, 800)
tiers = [
    ("工作记忆", "当前上下文窗口", "KB 级 · 会话内 · 每轮全量读写", 120, C.indigo, C.indigo_s),
    ("情景记忆", "历史对话与轨迹", "MB 级 · 可检索回放(向量库)", 90, C.teal, C.teal_s),
    ("语义记忆", "提炼后的知识/事实", "用户偏好、领域知识(知识库/图谱)", 60, C.amber, C.amber_s),
    ("程序记忆", "技能与经验", "系统提示词、可复用 Skill、微调权重", 40, C.purple, C.purple_s),
]
y = 70
for name, sub, desc, h, colr, colr_s in tiers:
    f.box(80, y, 250, h, name, sub, fill=colr_s, stroke=colr, tc=colr, fs=13.5)
    f.text(370, y + h / 2 - 4, desc, 12, C.soft, 400, anchor="start")
    y += h + 18
f.arrow(340, 90, 340, y - 40, color=C.faint, sw=1.6, both=True)
f.text(352, 250, "读写", 11.5, C.faint, 600, anchor="start")
f.group(560, 70, 320, 330, "设计问题")
f.mtext(578, 108, ["• 什么进工作记忆?", "  (相关性 × 新鲜度 × 重要度)", "• 何时写入长期记忆?", "  (显式保存 vs 自动萃取)", "• 何时检索回来?", "  (每轮? 按需触发?)", "• 记忆冲突如何裁决?", "  (时间戳 + 置信度)"], 12, C.soft, 400, 1.8, anchor="start")
f.note(460, 442, "MemGPT/Letta、ChatGPT Memory、Claude 的 memory tool 都在这一坐标系里做取舍", 12, C.faint, anchor="middle")
f.save("fig-memory-tiers")

# ---- 26 memgpt (ch19) -----------------------------------------------------------
f = F(920, 400)
f.text(460, 30, "MemGPT:把 LLM 当操作系统,记忆分页换入换出", 17, C.ink, 800)
f.box(80, 70, 320, 70, "主存(Main Context)", "提示词 + 对话历史(窗口内)", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
f.box(520, 70, 320, 70, "外存(External Storage)", "向量库 / 数据库 / 文件(窗口外)", fill=C.teal_s, stroke=C.teal, tc=C.teal_d)
f.arrow(400, 92, 520, 92, label="页出: 满了就归档", color=C.faint)
f.arrow(520, 118, 400, 118, label="页入: 需要时检索", color=C.faint)
f.group(80, 180, 760, 150, "自我编辑的记忆指令(self-editing memory)")
f.mtext(100, 220, ['模型自己决定何时调用 memory_replace("user.pref", "不喜欢太技术的解释") —— 就像操作系统的 mmap/换页,'], 12.5, C.ink, 400, 1.8, anchor="start")
f.mtext(100, 244, ['把「记住什么、忘记什么」的决策权交给模型本身,而不是靠外置启发式规则。'], 12.5, C.ink, 400, 1.8, anchor="start")
f.pill(460, 320, "这一思想直接演化为 Claude 的 memory tool 与 Letta 的 MemGPT 服务器", fill=C.amber_s, tc=C.amber_d, fs=12)
f.note(460, 380, "Packer et al., 2023 «MemGPT: Towards LLMs as Operating Systems»", 12, C.faint, anchor="middle")
f.save("fig-memgpt")

# ---- 27 rag pipeline (ch20) -----------------------------------------------------
f = F(960, 480)
f.text(480, 30, "Naive RAG 全流程:离线索引 + 在线检索生成", 17, C.ink, 800)
# offline
f.group(40, 60, 880, 150, "离线 · 索引管线(一次构建,多次查询)", fill="#ffffff")
chevron_flow(f, 70, 108, 820, 62, ["文档加载\nPDF/HTML/DB", "清洗与分块\nChunking", "向量化\nEmbedding", "入库存索引\nVector Store / BM25"], gap=14)
# online
f.group(40, 240, 880, 190, "在线 · 查询管线(每次提问)", fill="#ffffff")
q = f.box(70, 300, 130, 56, "用户提问", fill=C.blue_s, stroke=C.blue, tc=C.blue_d)
f.arrow(q["right"][0], q["cy"], 240, 328, color=C.faint)
f.box(240, 300, 150, 56, "查询向量化", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
f.arrow(390, 328, 430, 328, color=C.faint)
vs = f.cylinder(490, 328, 110, 74, "向量库\n+ 关键词索引")
f.arrow(545, 328, 585, 328, label="Top-K", color=C.faint)
f.box(585, 300, 120, 56, "重排序\nRerank", fill=C.purple_s, stroke=C.purple, tc=C.purple_d, fs=12.5)
f.arrow(705, 328, 745, 328, color=C.faint)
f.box(745, 300, 150, 56, "拼上下文 → LLM\n生成带引用答案", fill=C.green_s, stroke=C.green, tc="#166534", fs=12)
f.note(480, 460, "两个常见误区:分块比模型更重要;没有评估集的 RAG 调优全是玄学", 12, C.faint, anchor="middle")
f.save("fig-rag-pipeline")

# ---- 28 chunking (ch20) ---------------------------------------------------------
f = F(920, 400)
f.text(460, 30, "分块策略:粒度决定召回的上限", 17, C.ink, 800)
strats = [
    ("固定长度", "每 512 token 切一刀", "简单粗暴,切断语义", C.faint),
    ("递归分隔", "段落 → 句子 → 词逐级回退", "LangChain 默认,通用首选", C.teal),
    ("语义分块", "相邻句向量突变处切分", "质量高,成本高", C.indigo),
    ("结构感知", "按标题/代码块/表格切", "Markdown/代码文档最佳", C.purple),
]
for i, (t, s, d, colr) in enumerate(strats):
    x = 50 + i * 212
    f.box(x, 64, 192, 96, t, s, fill="#ffffff", stroke=colr, tc=colr, fs=13.5)
    f.text(x + 96, 140, d, 10.5, C.soft, 400)
# doc visualization
f.group(50, 190, 820, 150, "一块好 chunk 的样子")
f.raw('<rect x="90" y="230" width="180" height="80" rx="8" fill="%s" stroke="%s"/>' % (C.teal_s, C.teal))
f.mtext(180, 262, ["✓ 一个完整语义", "✓ 自含上下文", "✓ 200~800 token"], 11, C.teal_d, 600, 1.6)
f.raw('<rect x="320" y="230" width="180" height="80" rx="8" fill="%s" stroke="%s"/>' % (C.red_s, C.red))
f.mtext(410, 262, ["✗ 句子被拦腰切断", "✗ 指代丢失(『它』)", "✗ 表格被拆散"], 11, C.red_d, 600, 1.6)
f.text(640, 266, "经验值:重叠 10%~20%,\n保留章节标题作为前缀", 11.5, C.soft, 400)
f.note(460, 378, "先问『这段文字将来要回答什么问题』—— 好的 chunk 是一个独立的答案单元", 12, C.faint, anchor="middle")
f.save("fig-chunking")

# ---- 29 hybrid rerank (ch20) ----------------------------------------------------
f = F(920, 380)
f.text(460, 30, "混合检索 + 重排:两阶段漏斗", 17, C.ink, 800)
q = f.box(60, 150, 120, 50, "Query", fill=C.blue_s, stroke=C.blue, tc=C.blue_d)
v = f.box(240, 90, 170, 56, "向量检索\n(语义, 召回广)", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12)
k = f.box(240, 200, 170, 56, "BM25 检索\n(关键词, 精确匹配)", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12)
f.arrow(q["right"][0], 165, 240, 118, color=C.faint)
f.arrow(q["right"][0], 185, 240, 228, color=C.faint)
rr = f.box(480, 130, 150, 86, "合并去重\nRRF 融合\nTop 50", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=12.5)
f.arrow(410, 118, 480, 160, color=C.faint)
f.arrow(410, 228, 480, 190, color=C.faint)
ce = f.box(700, 130, 160, 86, "Cross-Encoder\n重排 → Top 5", "慢但准,只算候选", fill=C.purple_s, stroke=C.purple, tc=C.purple_d, fs=12.5)
f.arrow(630, 173, 700, 173, label="候选", color=C.faint)
f.note(460, 300, "为什么两层?向量管『意思相近』,BM25 管『专名/型号/代码精确命中』;Reranker 管『逐对精比』", 12, C.faint, anchor="middle")
f.note(460, 330, "工业界共识:升级 Reranker 的收益常常大于升级 Embedding 模型", 12, C.faint, anchor="middle")
f.save("fig-hybrid-rerank")

# ---- 30 agentic rag (ch21) ------------------------------------------------------
f = F(880, 460)
f.text(440, 30, "Agentic RAG:让模型自己决定『检索什么、够不够』", 17, C.ink, 800)
d1 = f.diamond(440, 110, 220, 64, "问题需要检索吗?\n(简单问题直接答)")
a1 = f.box(120, 90, 180, 50, "直接回答", fill=C.green_s, stroke=C.green, tc="#166534", fs=12.5)
f.arrow(330, 110, 304, 110, label="否", color=C.green)
f.box(560, 170, 200, 50, "生成查询(可改写/分解)", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12)
f.arrow(440, 142, 560, 185, label="是", color=C.faint)
f.box(560, 250, 200, 50, "执行检索 Top-K", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12.5)
f.arrow(660, 220, 660, 246, color=C.faint)
d2 = f.diamond(440, 340, 230, 66, "证据足够支撑答案吗?")
f.arrow(560, 275, 555, 307, color=C.faint)
f.box(120, 315, 210, 50, "综合生成 + 引用", fill=C.green_s, stroke=C.green, tc="#166534", fs=12.5)
f.arrow(325, 340, 310, 340, label="是", color=C.green)
f.elbow([(440, 373), (440, 420), (660, 420), (660, 300), (690, 300)], label="否 → 换查询/换源重试", color=C.red, dash="5 4")
f.note(440, 446, "Self-RAG/CRAG 的核心:把『检索够不够』变成显式判断步骤,而不是一次性管线", 12, C.faint, anchor="middle")
f.save("fig-agentic-rag")

# ---- 31 graphrag (ch21) ---------------------------------------------------------
f = F(920, 400)
f.text(460, 30, "GraphRAG:把语料组织成实体关系图再检索", 17, C.ink, 800)
f.group(50, 60, 380, 280, "传统向量 RAG")
f.mtext(70, 96, ["检索『与问题相似』的段落,", "适合:事实查找、局部问答", "", "短板:跨文档、多跳问题", "『A 公司的 CEO 投资过 B 吗?』"], 12, C.soft, 400, 1.8, anchor="start")
f.group(490, 60, 380, 280, "GraphRAG(Microsoft, 2024)")
nodes = [("张三", 560, 130, C.indigo), ("A 公司", 720, 110, C.teal), ("B 公司", 780, 200, C.teal),
         ("X 基金", 640, 220, C.purple), ("收购", 700, 300, C.amber)]
for n, x, y, colr in nodes:
    f.raw('<ellipse cx="%d" cy="%d" rx="42" ry="20" fill="%s" stroke="%s"/>' % (x, y, C.white, colr))
    f.text(x, y + 4, n, 11.5, colr, 700)
f.raw('<line x1="602" y1="130" x2="678" y2="112" stroke="%s" stroke-width="1.4"/>' % C.line)
f.raw('<line x1="680" y1="128" x2="745" y2="188" stroke="%s" stroke-width="1.4"/>' % C.line)
f.raw('<line x1="602" y1="146" x2="622" y2="206" stroke="%s" stroke-width="1.4"/>' % C.line)
f.raw('<line x1="664" y1="234" x2="688" y2="286" stroke="%s" stroke-width="1.4"/>' % C.line)
f.text(646, 172, "任CEO", 10.5, C.faint, 600, style='paint-order:stroke;stroke:#fff;stroke-width:3px;')
f.text(736, 160, "投资", 10.5, C.faint, 600, style='paint-order:stroke;stroke:#fff;stroke-width:3px;')
f.mtext(505, 340, ["先离线抽取实体+关系+社区摘要,", "查询时沿图多跳遍历,擅长全局性问题。"], 12, C.soft, 400, 1.7, anchor="start")
f.note(460, 380, "取舍:GraphRAG 索引成本 10×+,换多跳推理能力;向量 RAG 仍是 80% 场景的答案", 12, C.faint, anchor="middle")
f.save("fig-graphrag")

# ---- 32 reflexion (ch22) --------------------------------------------------------
f = F(900, 440)
f.text(450, 30, "Reflexion:失败不是终点,是可复用的语言经验", 17, C.ink, 800)
actor = f.box(80, 90, 200, 56, "Actor 行动者", "生成轨迹并执行任务", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
ev = f.box(360, 90, 180, 56, "Evaluator 评估", "测试/判分: 成功?", fill=C.amber_s, stroke=C.amber, tc=C.amber_d)
selfref = f.box(620, 90, 220, 56, "Self-Reflect 自省", "用语言总结失败原因", fill=C.purple_s, stroke=C.purple, tc=C.purple_d, fs=12.5)
mem = f.cylinder(730, 250, 150, 70, "情节记忆\n(语言化教训)")
f.arrow(280, 118, 360, 118, color=C.faint)
f.arrow(540, 118, 620, 118, label="失败", color=C.red)
f.elbow([(730, 146), (730, 215)], color=C.faint, label="写入教训")
f.elbow([(655, 250), (180, 250), (180, 150)], label="下次带上教训重试", color=C.indigo, sw=1.8)
f.box(360, 300, 180, 50, "✓ 成功 → 交付", fill=C.green_s, stroke=C.green, tc="#166534", fs=12.5)
f.elbow([(450, 146), (450, 296)], color=C.green, sw=1.6)
f.text(470, 226, "是", 12, C.green, 700)
f.note(450, 400, "语言化反馈替代梯度更新:HF Trivia/SWAN/ALFWorld 上大幅超越同模型无反思基线", 12, C.faint, anchor="middle")
f.note(450, 424, "代价:每轮反思 ≈ +2~3 次调用;对『不可判定任务』可能自我误导 —— 见 22.4 节", 12, C.faint, anchor="middle")
f.save("fig-reflexion")

# ---- 33 context budget (ch23) ---------------------------------------------------
f = F(920, 430)
f.text(460, 30, "上下文预算:200K Token 怎么花才值?", 17, C.ink, 800)
total = 640
bx, by = 120, 90
segs = [
    ("系统提示词 + 工具 Schema", 0.10, C.indigo, "常驻 · 精心设计"),
    ("任务与目标", 0.05, C.blue, "明确成功标准"),
    ("对话历史(压缩后)", 0.20, C.teal, "滚动摘要"),
    ("检索资料(RAG)", 0.30, C.amber, "按需注入,宁缺毋滥"),
    ("工具结果(本轮)", 0.25, C.purple, "大结果落盘,只回摘要"),
    ("输出预留", 0.10, C.green, "给模型留思考空间"),
]
x = bx
for name, frac, colr, tip in segs:
    w = total * frac
    f.raw('<rect x="%d" y="%d" width="%d" height="70" fill="%s" opacity="0.85" stroke="#fff" stroke-width="2"/>' % (x, by, w, colr))
    if frac >= 0.15:
        f.text(x + w / 2, by + 32, "%.0fK" % (200 * frac), 13, "#fff", 800)
        f.text(x + w / 2, by + 52, name.split(" ")[0], 10, "#fff", 600)
    x += w
f.text(bx + total / 2, by + 94, "← 200K Token 上下文窗口的理想分配(比例为经验参考,随任务调整) →", 12, C.faint, 600)
f.group(80, 220, 760, 160, "三条军规")
f.mtext(100, 258, ["1. 上下文是稀缺资源:每一行都要『值回票价』,与任务无关的信息是负资产。"], 12.5, C.ink, 400, 1.9, anchor="start")
f.mtext(100, 288, ["2. 中间产物落盘:大文件、长输出写入文件/数据库,上下文里只留指针 + 摘要。"], 12.5, C.ink, 400, 1.9, anchor="start")
f.mtext(100, 318, ["3. 重要内容放两端:注意力对首尾更敏感(U-shaped),关键约束写进系统提示词与最近消息。"], 12.5, C.ink, 400, 1.9, anchor="start")
f.save("fig-context-budget")

# ---- 34 compaction (ch23) -------------------------------------------------------
f = F(920, 400)
f.text(460, 30, "上下文压缩:滚动摘要 + 结构化笔记", 17, C.ink, 800)
# before
f.group(50, 60, 380, 200, "压缩前 · 97% 满")
for i, (t, colr) in enumerate([("系统提示词", C.indigo), ("历史消息 ×58", C.teal), ("工具大输出 ×12", C.amber), ("检索资料 ×6", C.purple)]):
    f.raw('<rect x="70" y="%d" width="340" height="34" rx="7" fill="%s" opacity="0.25"/>' % (96 + i * 40, colr))
    f.text(90, 118 + i * 40, t, 11.5, C.ink, 600, anchor="start")
f.text(240, 274, "状态:早期关键约束已被『稀释』,模型开始遗忘目标", 11, C.red, 600)
# arrow
f.arrow(440, 160, 480, 160, color=C.faint, sw=2)
f.text(460, 146, "压缩", 12, C.indigo, 800)
# after
f.group(490, 60, 380, 200, "压缩后 · 45% 满")
for i, (t, colr) in enumerate([("系统提示词(原样保留)", C.indigo), ("滚动摘要(自 history 提炼)", C.teal), ("关键事实便签(结构化 JSON)", C.amber), ("最近 6 条消息(原样)", C.purple)]):
    f.raw('<rect x="510" y="%d" width="340" height="34" rx="7" fill="%s" opacity="0.35"/>' % (96 + i * 40, colr))
    f.text(530, 118 + i * 40, t, 11.5, C.ink, 600, anchor="start")
f.text(680, 274, "约束不丢、线索不断、窗口可继续工作数小时", 11, C.green, 600)
f.note(460, 330, "Claude Code 的 /compact、Cursor 的 repo map、Letta 的分页记忆都是同一模式的不同实现", 12, C.faint, anchor="middle")
f.note(460, 358, "铁律:压缩是有损操作 —— 必须先写入『不可丢失事实清单』,再执行摘要", 12, C.faint, anchor="middle")
f.save("fig-compaction")

# ---- 35 multiagent topologies (ch24) ---------------------------------------------
f = F(960, 430)
f.text(480, 30, "四种主流多 Agent 拓扑", 17, C.ink, 800)
def node(x, y, t, colr=C.indigo, big=False):
    r = 22 if big else 17
    f.raw('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, y, r, C.white, colr))
    f.text(x, y + 4, t, 11 if not big else 12, colr, 700)
# 1 orchestrator
ox = 120
f.text(ox + 100, 76, "① 中心化编排", 13, C.ink, 700)
node(ox + 100, 110, "O", C.indigo, True)
node(ox + 40, 180, "A", C.teal); node(ox + 100, 190, "B", C.teal); node(ox + 160, 180, "C", C.teal)
for wx in (ox + 40, ox + 100, ox + 160):
    f.raw('<line x1="%d" y1="128" x2="%d" y2="166" stroke="%s" stroke-width="1.4"/>' % (ox + 100, wx, C.line))
f.text(ox + 100, 218, "并行分派 · 结果汇总", 10.5, C.faint)
# 2 pipeline
px = 350
f.text(px + 90, 76, "② 流水线", 13, C.ink, 700)
node(px + 20, 120, "写", C.teal); node(px + 95, 120, "审", C.amber); node(px + 170, 120, "发", C.indigo)
f.raw('<line x1="375" y1="120" x2="440" y2="120" stroke="%s" stroke-width="1.4" marker-end="url(#mp)"/>' % C.line)
f.text(px + 95, 160, "阶段固定 · 交接明确", 10.5, C.faint)
# 3 debate
dx = 620
f.text(dx + 110, 76, "③ 辩论/评审", 13, C.ink, 700)
node(dx + 50, 125, "正", C.blue); node(dx + 170, 125, "反", C.red)
node(dx + 110, 185, "裁", C.indigo, True)
f.raw('<line x1="675" y1="140" x2="715" y2="170" stroke="%s" stroke-width="1.4"/>' % C.line)
f.raw('<line x1="785" y1="140" x2="745" y2="170" stroke="%s" stroke-width="1.4"/>' % C.line)
f.text(dx + 110, 218, "多视角交叉验证", 10.5, C.faint)
# 4 swarm
sx = 850
f.text(sx + 55, 76, "④ 去中心群聊", 13, C.ink, 700)
node(sx + 20, 120, "A", C.teal); node(sx + 90, 105, "B", C.purple); node(sx + 70, 175, "C", C.amber)
f.raw('<line x1="872" y1="130" x2="930" y2="115" stroke="%s" stroke-width="1.2"/>' % C.line)
f.raw('<line x1="880" y1="140" x2="908" y2="168" stroke="%s" stroke-width="1.2"/>' % C.line)
f.text(sx + 55, 218, "自由对话 · 动态接管", 10.5, C.faint)
f.group(50, 250, 860, 130, "何时用多 Agent?")
f.mtext(70, 288, ["✓ 上下文装不下(隔离爆炸式工具结果)  ✓ 需要真正独立的视角(辩论)  ✓ 角色职责天然不同(写作vs审校)"], 12.5, C.ink, 400, 1.9, anchor="start")
f.mtext(70, 318, ["✗ 能单 Agent 解决就别拆 —— 每次交接都可能丢信息;通信成本随 Agent 数平方增长。"], 12.5, C.ink, 400, 1.9, anchor="start")
f.save("fig-ma-topologies")

# ---- 36 orchestrator workers (ch24) -----------------------------------------------
f = F(920, 440)
f.text(460, 30, "Orchestrator-Workers:可扩展的标准架构", 17, C.ink, 800)
orch = f.box(330, 70, 260, 62, "🧭 Orchestrator", "拆解 · 分派 · 汇总 · 交付", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=14)
ws = [("研究员 A\n(文献)", C.teal), ("研究员 B\n(数据)", C.teal), ("写作员\n(综合)", C.purple), ("审查员\n(事实核查)", C.amber)]
wb = []
for i, (t, colr) in enumerate(ws):
    b = f.box(50 + i * 215, 220, 185, 62, t, fill=colr_s, stroke=colr, tc=colr, fs=12.5)
    wb.append(b)
    f.elbow([(orch["cx"], orch["bottom"][1]), (orch["cx"], 160), (b["cx"], 160), (b["cx"], b["top"][1])],
            color=C.faint)
    f.elbow([(b["cx"] + 30, b["bottom"][1]), (b["cx"] + 30, 330), (orch["cx"], 330), (orch["cx"], orch["bottom"][1] + 4)],
            color=C.faint, sw=1.2, dash="4 4")
f.text(460, 360, "↑ 每个工作 Agent:独立上下文 · 只回摘要与产物 · 失败不影响同伴", 12, C.soft, 600)
f.note(460, 412, "Claude Code 的 Sub-agent、Deep Research 的并行检索、Map-Reduce 摘要 —— 全是这一模式", 12, C.faint, anchor="middle")
f.save("fig-orchestrator-workers")

# ---- 37 hitl (ch25) ---------------------------------------------------------------
f = F(920, 400)
f.text(460, 30, "Human-in-the-Loop:把危险动作拦在闸门前", 17, C.ink, 800)
a = f.box(70, 150, 160, 56, "Agent 请求", "执行 rm -rf ./dist", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=12.5)
d = f.diamond(370, 178, 180, 80, "风险分级")
f.arrow(230, 178, 280, 178, color=C.faint)
lv = [("低风险:只读操作", "自动放行", C.green), ("中风险:写入/发送", "记录日志 + 事后审计", C.amber), ("高风险:删除/支付/生产", "必须人工审批", C.red)]
for i, (t, act, colr) in enumerate(lv):
    y = 80 + i * 90
    f.box(560, y, 300, 56, t, act, fill=colr_s, stroke=colr, tc=colr, fs=12.5)
    f.arrow(460, 178, 560, y + 28, color=C.faint, sw=1.2)
f.pill(370, 300, "等待批准 ≠ 阻塞线程:检查点持久化,人批准后从断点恢复", fill=C.blue_s, tc=C.blue_d, fs=12)
f.note(460, 372, "LangGraph interrupt / OpenAI SDK approvals / Claude Code 权限弹窗 —— 模式一致:中断-恢复", 12, C.faint, anchor="middle")
f.save("fig-hitl")

print("figures_a done")
