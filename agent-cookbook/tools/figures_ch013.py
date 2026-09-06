# -*- coding: utf-8 -*-
"""figures_ch013.py — 第 13 章插图：评测集解剖、指标三层设计"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 13-2 评测集的解剖（新画） ------------------------------------------
f = F(960, 470)
f.text(480, 30, "评测集的解剖：分层构成与一条样本的字段", 17, C.ink, 800)
f.text(480, 52, "评测集是你产品的「考试大纲」：它决定你优化的方向，出错了比没有评测更糟", 12, C.faint)

# 顶部构成条
slices = [
    (60, 480, "核心真实样本 · 60%", C.indigo, C.indigo_s, C.indigo_d),
    (548, 160, "困难与边界 · 20%", C.teal, C.teal_s, C.teal_d),
    (716, 120, "历史事故回归 · 15%", C.red, C.red_s, C.red_d),
    (844, 88, "金丝雀 · 5%", C.amber, C.amber_s, C.amber_d),
]
for x, w, t, acc, acc_s, acc_d in slices:
    f.box(x, 76, w, 44, t, fill=acc_s, stroke=acc, tc=acc_d, fs=12)
f.arrow(60, 140, 932, 140, color=C.faint, sw=1.2, both=True)
f.text(480, 158, "宽度 ≈ 在评测集中的占比：跟着线上流量分布走，而不是跟着想象走", 11, C.faint)

# 四列说明
cols = [
    (60, "核心真实样本", C.indigo, C.indigo_s, C.indigo_d,
     ["来源：线上真实请求", "守住主流体验", "改动后指标不许回退"]),
    (288, "困难与边界", C.teal, C.teal_s, C.teal_d,
     ["超长输入、模糊指令", "多约束、专业术语", "推动改进的「拉力」"]),
    (516, "历史事故回归", C.red, C.red_s, C.red_d,
     ["线上踩过的每个坑", "修完立刻入库", "同坑永不二犯"]),
    (744, "金丝雀样本", C.amber, C.amber_s, C.amber_d,
     ["二三十条最敏感场景", "跑得快、天天跑", "几小时内发现劣化"]),
]
for x, t, acc, acc_s, acc_d, items in cols:
    f.group(x, 178, 212, 128, t, fill="#ffffff", stroke=acc, label_fill=acc_d, fs=12.5)
    for i, it in enumerate(items):
        f.text(x + 14, 216 + i * 26, it, 11, C.soft, 400, anchor="start")

# 一条样本的字段
f.group(60, 330, 500, 108, "一条评测样本的最小字段集", fill=C.gray_s, stroke=C.line, fs=12.5)
code = ['{"id": "case-0142",',
        ' "input": "用户原始输入",',
        ' "reference": "参考答案 / 要点清单",',
        ' "rubric": "判分标准（给裁判用）",',
        ' "tags": ["抽取", "长输入"], "difficulty": 3,',
        ' "source": "ticket#8817  ← 永远可溯源" }']
f.mtext(84, 362, code, 11, C.ink, 400, 1.55, anchor="start", mono=True)

# 三原则
f.group(590, 330, 310, 108, "构建三原则", fill=C.purple_s, stroke=C.purple, fs=12.5)
f.text(610, 364, "① 真实分布：来自线上而非想象", 11.5, C.purple_d, 600, anchor="start")
f.text(610, 390, "② 分层覆盖：按风险加权，而非随机", 11.5, C.purple_d, 600, anchor="start")
f.text(610, 416, "③ 防泄漏：评测集永不进提示示例", 11.5, C.purple_d, 600, anchor="start")
f.save("fig-eval-set")

# ---- 图 13-3 指标的三层设计（新画） ----------------------------------------
f = F(960, 430)
f.text(480, 30, "给质量打分的三层指标：成本换覆盖", 17, C.ink, 800)
f.text(480, 52, "规则指标客观但窄，人工评审准但贵，模型裁判居中——生产系统三层并用、互相校准", 12, C.faint)

rows = [
    (84, "第一层 · 规则指标", C.teal, C.teal_s, C.teal_d,
     ["精确匹配 / 通过单元测试", "JSON Schema 校验、引用命中",
      "字段级 F1（抽取任务）"],
     "成本 ≈ 0 · 客观可复现 · 只覆盖可形式化的子集"),
    (188, "第二层 · 模型裁判", C.indigo, C.indigo_s, C.indigo_d,
     ["按 rubric 打 1~5 分", "pairwise 对比新旧版本",
      "要点清单核对（引用覆盖率）"],
     "成本中等 · 覆盖广 · 有位置/长度/自我偏好偏差"),
    (292, "第三层 · 人工评审", C.purple, C.purple_s, C.purple_d,
     ["每版本抽 30~100 条", "双人标注 + 分歧仲裁",
      "定期抽检校准裁判指标"],
     "金标准 · 贵 · 用于给前两层「定标」"),
]
for y, t, acc, acc_s, acc_d, items, foot in rows:
    f.box(50, y, 220, 84, t, fill=acc_s, stroke=acc, tc=acc_d, fs=13.5)
    for i, it in enumerate(items):
        f.text(300, y + 26 + i * 22, "· " + it, 11.5, C.soft, 400, anchor="start")
    f.text(640, y + 48, foot, 11, acc_d, 600, anchor="start")

f.group(640, 60, 290, 90, "好指标的四个性质", fill="#ffffff", stroke=C.line, fs=12.5)
for i, it in enumerate(["与业务成功对齐，而非代理指标", "可分层：端到端成功率 × 分项",
                        "可复现：同输入同分数", "对改动敏感：能区分好坏版本"]):
    f.text(656, 92 + i * 20, "· " + it, 10.8, C.soft, 400, anchor="start")
f.note(480, 408, "代码与抽取任务从第一层开始就够；开放式生成任务才需要第二、三层——先问「这个任务的可验证面有多大」",
       12, C.faint, anchor="middle")
f.save("fig-metric-layers")
