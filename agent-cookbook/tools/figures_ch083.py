# -*- coding: utf-8 -*-
"""figures_ch083.py — ch083 复刻 Deep Research 深度调研 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 83-1: Deep Research 递归多阶段闭环架构
f = F(940, 430)
f.box(40, 60, 160, 110, "1. 规划分解器\nPlanner\n多层大纲生成\n子假设树分解", fill=C.blue_s, stroke=C.blue)
f.box(240, 60, 160, 110, "2. 并行搜索爬取\nSearcher\nTavily/Serp API\nJina Reader 提取", fill=C.indigo_s, stroke=C.indigo)
f.box(440, 60, 160, 110, "3. 事实抽取综合\nSynthesizer\n长文本交叉比对\n证据冲突仲裁", fill=C.amber_s, stroke=C.amber)
f.box(640, 60, 160, 110, "4. 证据反思核验\nVerifier\n信息缺口探测\n可信度评分剪枝", fill=C.red_s, stroke=C.red)
f.box(840, 60, 80, 110, "5. 终稿\nReporter\n万字长文\n引用树", fill=C.teal_s, stroke=C.teal)

f.arrow(200, 115, 240, 115, "子假设")
f.arrow(400, 115, 440, 115, "网页正文")
f.arrow(600, 115, 640, 115, "候选证据")
f.arrow(800, 115, 840, 115, "验证通过")

# 递归探索分支
f.elbow([(720, 170), (720, 240), (320, 240), (320, 170)], label="信息存在缺口 / 冲突: 生成次级查询触发深度递归探索 (Depth <= 3)", color=C.red, label_pos=1)

# 底部共享记忆底座
f.box(100, 290, 740, 100, "全局黑板架构与去重证据图谱 (Shared Knowledge Graph & Blackboard)\n• URL 访问布隆过滤器 (防死循环抓取)\n• 跨源事实一致性校验 (Truth Discovery 贝叶斯信度权重)\n• 上下文动态折叠压缩 (Context Compaction 保护 128k 窗口)", fill=C.purple_s, stroke=C.purple)

f.save("fig-deep-research-loop")

# fig 83-2: 动态假设树演进与剪枝
f = F(940, 360)
f.pill(120, 80, "顶层宏观研究课题", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 160, 180, 70, "子课题 A: 核心技术演进\n已验证: 充分论据", fill=C.green_s, stroke=C.green)
f.box(280, 160, 180, 70, "子课题 B: 商业成本度量\n缺口: 缺乏云厂商定价", fill=C.amber_s, stroke=C.amber)
f.box(500, 160, 180, 70, "子课题 C: 竞品性能测试\n伪证: 营销软文驳回", fill=C.red_s, stroke=C.red)

f.arrow(120, 100, 150, 160)
f.arrow(120, 100, 370, 160)
f.arrow(120, 100, 590, 160)

# 子分支扩展
f.box(280, 270, 180, 60, "二级查询: AWS/Azure\n批量爬取最新价格页面", fill=C.indigo_s, stroke=C.indigo)
f.arrow(370, 230, 370, 270, "生成次级搜索")

f.box(500, 270, 180, 60, "剪枝终止 (Pruned)\n标记为不可靠源", fill=C.gray_s, stroke=C.line)
f.arrow(590, 230, 590, 270, "证据不足剪枝")

f.save("fig-research-tree-prune")
print("ch083 figures generated successfully")
