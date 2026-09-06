# -*- coding: utf-8 -*-
"""figures_ch072.py — ch072 语音 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 72-1: 级联 vs 端到端语音 ----
f = F(940, 430)
f.text(470, 32, "语音 Agent 两条路线:级联管线 vs 端到端", 18, C.ink, 800)
# 级联
f.group(40, 70, 420, 250, "级联管线 (Pipeline)")
b1 = f.box(60, 120, 110, 60, "ASR", None, fill=C.teal_s, stroke=C.teal, fs=12)
b2 = f.box(195, 120, 110, 60, "LLM", None, fill=C.indigo_s, stroke=C.indigo, fs=12)
b3 = f.box(330, 120, 110, 60, "TTS", None, fill=C.amber_s, stroke=C.amber, fs=12)
f.arrow(170, 150, 195, 150, "", C.soft)
f.arrow(305, 150, 330, 150, "", C.soft)
f.note(60, 210, "+ 各段独立优化、可观测、可换件")
f.note(60, 232, "- 三段延迟叠加 (通常 800-1500ms)")
f.note(60, 254, "- 情感/语调信息在文本层丢失")
f.note(60, 285, "适合: 客服、工单等「内容优先」场景", 11, C.indigo_d)
# 端到端
f.group(490, 70, 420, 250, "端到端 (Speech-to-Speech)")
e1 = f.box(530, 120, 340, 60, "语音大模型 (音频 in → 音频 out)", None, fill=C.purple_s, stroke=C.purple, fs=12)
f.note(510, 210, "+ 感知副语言信息 (语气/情绪/打断意图)")
f.note(510, 232, "- 延迟更低 (300-600ms 可达)")
f.note(510, 254, "- 可观测性弱: 中间无文本, 调试与审计难")
f.note(510, 285, "适合: 陪伴、面试、情感交互等「感觉优先」场景", 11, C.indigo_d)
f.note(470, 355, "混合路线兴起: 端到端主干 + 文本旁路(日志/审计/工具调用) — 兼得感觉与可治理", 11.5, C.ink, anchor="middle")
f.note(470, 390, "延迟预算黄金线: 用户感知「对话自然」的往返延迟 &lt; 1 秒 — 语音 Agent 的第一工程指标", 11.5, C.red, anchor="middle")
f.save("fig-voice-pipeline")

# ---- fig 72-2: 打断处理状态机 ----
f = F(940, 380)
f.text(470, 32, "全双工对话的核心状态机:打断与轮次仲裁", 18, C.ink, 800)
s1 = f.box(60, 150, 170, 90, "聆听态", "VAD 监听用户", fill=C.teal_s, stroke=C.teal, fs=13)
s2 = f.box(330, 60, 170, 90, "思考态", "LLM 推理中\n(可被新输入打断)", fill=C.amber_s, stroke=C.amber, fs=12)
s3 = f.box(600, 150, 170, 90, "说话态", "TTS 播放中\n(监听是否被插话)", fill=C.indigo_s, stroke=C.indigo, fs=12)
s4 = f.box(330, 260, 170, 80, "仲裁", "打断信号分类:\n插话/附和/噪声", fill=C.purple_s, stroke=C.purple, fs=12)
f.arrow(230, 170, 330, 120, "用户开口", C.soft)
f.arrow(500, 150, 600, 190, "就绪", C.soft)
f.arrow(685, 240, 500, 300, "检测到插话", C.soft)
f.arrow(330, 300, 230, 240, "切换/继续", C.soft)
f.arrow(415, 150, 415, 260, "", C.soft)
f.note(470, 365, "副语言判断(「嗯哼」是附和不是打断)是端到端模型的优势区 — 级联管线需要额外的分类器补课", 11.5, C.faint, anchor="middle")
f.save("fig-voice-state-machine")
