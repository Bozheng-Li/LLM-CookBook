# -*- coding: utf-8 -*-
"""figures_ch011.py — 第 11 章插图: SDK 风格对比与本地推理栈"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 11-1 三大调用风格与统一抽象层 (新画) ------------------------------
f = F(960, 470)
f.text(480, 32, "三大调用风格：云端两家与本地一家", 18, C.ink, 800)
f.text(480, 56, "都是 HTTPS + JSON + SSE 流式，真正的差异在请求与响应的「形状」", 12.5, C.faint)

cards = [
    (40, "OpenAI 风格", C.indigo, C.indigo_s, C.indigo_d,
     ["POST /v1/chat/completions", "messages: [{role, content}]", "system 是一种消息角色",
      "工具: tools → tool_calls"],
     "生态事实标准 · Responses API 是新一代"),
    (350, "Anthropic 风格", C.amber, C.amber_s, C.amber_d,
     ["POST /v1/messages", "system 是顶级参数", "content 是 block 数组",
      "工具结果也是 block"],
     "max_tokens 必填 · usage 随响应返回"),
    (660, "本地推理", C.teal, C.teal_s, C.teal_d,
     ["Ollama / vLLM / llama.cpp", "均提供 OpenAI 兼容端点", "改 base_url 即可迁移",
      "权重与数据不出本机"],
     "隐私 · 成本 · 延迟可控"),
]
for x, title, acc, acc_s, acc_d, lines, foot in cards:
    f.group(x, 76, 280, 228, title, fill="#ffffff", stroke=acc, label_fill=acc_d, fs=14)
    for i, ln in enumerate(lines):
        f.box(x + 16, 112 + i * 38, 248, 30, ln, fill=acc_s, stroke="none",
              tc=C.ink, fs=11.5, rx=7, weight=500, mono=True)
    f.note(x + 16, 290, foot, 10.8, C.faint)
for x0 in (322, 632):
    f.arrow(x0, 190, x0 + 24, 190, color=C.faint)
for cx in (180, 490, 800):
    f.arrow(cx, 308, cx, 346, color=C.faint)

f.box(40, 350, 880, 56, "统一抽象层（LiteLLM / 自研 adapter）",
      "抹平字段与参数差异：messages、tools、stream、usage —— 应用代码只写一份",
      fill=C.purple_s, stroke=C.purple, tc=C.purple_d, fs=14, sub_fs=11.5)
f.note(480, 440, "原则：只抽象 90% 相同的部分；供应商差异用配置表达，而不是塞满 if-else",
       12, C.faint, anchor="middle")
f.save("fig-sdk-landscape")

# ---- 图 11-2 本地推理栈三种定位 (新画) -----------------------------------
f = F(960, 330)
f.text(480, 32, "本地推理栈：三种定位", 18, C.ink, 800)
cols = [
    (50, "Ollama", "一键运行本地模型", C.green, C.green_s, C.green,
     ["ollama pull / run 两步上手", "REST + OpenAI 兼容端点", "Modelfile 定制提示与参数",
      "适合：个人电脑与开发环境"]),
    (350, "vLLM", "生产级高吞吐服务", C.indigo, C.indigo_s, C.indigo_d,
     ["PagedAttention 显存分页", "连续批处理吃满 GPU", "vllm serve 起 OpenAI 兼容服务",
      "适合：并发线上的自托管服务"]),
    (650, "llama.cpp", "端侧与低资源友好", C.amber, C.amber_s, C.amber_d,
     ["GGUF 量化格式（Q4 / Q5 / Q8）", "CPU / Mac / 边缘设备可跑", "llama-server 提供兼容接口",
      "适合：离线、端侧、单机嵌入"]),
]
for x, name, tag, acc, acc_s, acc_d, items in cols:
    f.group(x, 60, 280, 224, "%s · %s" % (name, tag), fill="#ffffff",
            stroke=acc, label_fill=acc_d, fs=13)
    for i, it in enumerate(items):
        f.box(x + 16, 98 + i * 42, 248, 32, it, fill=acc_s, stroke="none",
              tc=C.ink, fs=11.5, rx=7, weight=500)
    y = 98 + 4 * 42 + 2
    f.note(x + 16, y, "本地权重 · 数据不出机器", 10.5, C.faint)
f.note(480, 316, "量化用少量质量损失换数倍内存与速度收益；本地小模型的函数调用能力参差，上线前需实测（第 88 章）",
       12, C.soft, anchor="middle")
f.save("fig-local-stack")
