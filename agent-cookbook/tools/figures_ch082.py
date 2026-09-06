# -*- coding: utf-8 -*-
"""figures_ch082.py — ch082 自动化数据分析师 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 82-1: 自动化数据分析师 Agent 全景流水线
f = F(940, 420)
# Step 1: Schema 探测与语义字典生成
f.box(40, 60, 180, 110, "1. Schema 探测\n字段语义词典\n缺失值分布扫描", sub="元数据提取", fill=C.blue_s, stroke=C.blue)

# Step 2: 意图解析与 Text-to-SQL / Code 生成
f.box(270, 60, 180, 110, "2. 意图解析与生成\n自然语言转 SQL\nPandas 分析脚本", sub="防注入安全过滤", fill=C.indigo_s, stroke=C.indigo)

# Step 3: 安全隔离沙箱执行
f.box(500, 60, 180, 110, "3. 安全沙箱执行\nWasm/Docker 沙箱\n超时与内存熔断", sub="报错自动捕获", fill=C.amber_s, stroke=C.amber)

# Step 4: 图表渲染与业务洞察生成
f.box(730, 60, 180, 110, "4. 可视化 & 洞察\nPlotly 图表渲染\n业务归因分析报告", sub="异常根因挖掘", fill=C.teal_s, stroke=C.teal)

# 箭头连接
f.arrow(220, 115, 270, 115, "数据字典")
f.arrow(450, 115, 500, 115, "SQL / Python")
f.arrow(680, 115, 730, 115, "表格结果")

# 底部反馈与修正循环 (pts: list of tuples)
f.elbow([(590, 170), (590, 240), (360, 240), (360, 170)], label="执行报错自愈重试 (Max 3次)", color=C.red, label_pos=1)

# 底部安全防御护栏
f.box(160, 290, 620, 90, "沙箱安全治理与数据防泄漏护栏\n• 只读账号连接 (SELECT 权限锁死，阻断 DROP/UPDATE/DELETE)\n• 网络隔离沙箱 (禁止 socket 出网，彻底杜绝数据外传)\n• 限制最大返回行数 (LIMIT 1000 保护，防 OOM 内存溢出)", fill=C.purple_s, stroke=C.purple)

f.save("fig-data-agent-arch")

# fig 82-2: Text-to-SQL 自愈重试状态机
f = F(940, 360)
f.pill(120, 170, "用户业务提问", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)
f.box(240, 120, 150, 100, "SQL 生成模型\nFew-shot 示例注入\nSchema 约束生成", fill=C.indigo_s, stroke=C.indigo)
f.box(440, 120, 150, 100, "只读数据库校验\n执行 SQL 查询\n提取前 10 行样例", fill=C.teal_s, stroke=C.teal)
f.pill(720, 120, "执行成功: 汇总分析", fill=C.green_s, tc=C.ink, stroke=C.green)
f.box(640, 180, 160, 90, "语法/逻辑报错\n捕获 SQL 异常栈\n提取缺少字段", fill=C.red_s, stroke=C.red)

f.arrow(190, 170, 240, 170, "NL Query")
f.arrow(390, 170, 440, 170, "生成的 SQL")
f.arrow(590, 150, 640, 125, "成功")
f.arrow(590, 190, 640, 225, "抛出异常")
f.elbow([(720, 270), (720, 310), (315, 310), (315, 220)], label="反馈回填: 带着错误提示重新修正", color=C.amber, label_pos=1)

f.save("fig-text2sql-self-healing")
print("ch082 figures generated successfully")
