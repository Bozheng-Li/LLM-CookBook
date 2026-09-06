# -*- coding: utf-8 -*-
"""figures_ch085.py — ch085 企业级工作流自动化 Agent (Workflow & RPA) 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 85-1: 混合工作流自动化架构 (API + GUI RPA 双轨融合)
f = F(940, 420)
f.box(40, 60, 160, 110, "1. 业务意图解析\nIntent & State\n自然语言指令分解\n全局状态机初始化", fill=C.blue_s, stroke=C.blue)
f.box(240, 60, 180, 110, "2. 动作路由分发\nDual-Track Router\n确定性 OpenAPI 优先\n无 API 降级为 GUI RPA", fill=C.indigo_s, stroke=C.indigo)
f.box(460, 40, 190, 70, "轨 A: OpenAPI / Webhook\nCRM/ERP/钉钉/飞书\n毫秒级高并发事务幂等", fill=C.teal_s, stroke=C.teal)
f.box(460, 130, 190, 70, "轨 B: 无头 GUI RPA 自动化\nPlaywright/OSWorld\n视觉定位与表单点击", fill=C.amber_s, stroke=C.amber)
f.box(690, 60, 210, 110, "3. 事务审计与补偿\nSaga Compensator\n前置校验 / 人工审批 (HITL)\n失败级联逆向回滚", fill=C.purple_s, stroke=C.purple)

f.arrow(200, 115, 240, 115, "业务任务")
f.arrow(420, 85, 460, 75, "结构化接口")
f.arrow(420, 145, 460, 165, "老旧遗留系统")
f.arrow(650, 75, 690, 95)
f.arrow(650, 165, 690, 135)

# 底部失败重试与人工介入兜底
f.elbow([(795, 170), (795, 240), (555, 240), (555, 200)], label="GUI 异常超时或高危操作: 挂起状态机触发人类专家审批 (HITL)", color=C.red, label_pos=1)

# 底部可靠性基础设施
f.box(100, 290, 740, 100, "企业级可靠性基础设施 (Reliability & Safety Guardrails)\n• 幂等性令牌校验 (Idempotency Key，杜绝多重扣款/重复发信)\n• 细粒度 RBAC 权限矩阵 (只读/低危动作自动执行，高危转签审批)\n• 分布式 Saga 事务日志 (Temporal / Cadence 持久化工作流检查点)", fill=C.green_s, stroke=C.green)

f.save("fig-workflow-rpa-arch")

# fig 85-2: Saga 模式分布式事务逆向补偿流
f = F(940, 360)
f.pill(120, 70, "工作流启动", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

# 正向流水线
f.box(60, 150, 160, 70, "T1: 扣减库存\n调用 WMS 接口", fill=C.green_s, stroke=C.green)
f.box(260, 150, 160, 70, "T2: 扣除余额\n调用财务网关", fill=C.green_s, stroke=C.green)
f.box(460, 150, 160, 70, "T3: 开具发票\nRPA 登录税控盘", fill=C.red_s, stroke=C.red)

f.arrow(120, 95, 140, 150)
f.arrow(220, 185, 260, 185, "成功")
f.arrow(420, 185, 460, 185, "成功")

# 失败与逆向补偿
f.pill(690, 185, "T3 崩溃: 税控盘超时", fill=C.red_s, tc=C.red_d, stroke=C.red)
f.arrow(620, 185, 650, 185, "抛出异常")

f.box(260, 260, 160, 70, "C2: 逆向退款\n冲正账户余额", fill=C.amber_s, stroke=C.amber)
f.box(60, 260, 160, 70, "C1: 回滚库存\n释放预占库存量", fill=C.amber_s, stroke=C.amber)

f.arrow(690, 220, 340, 260, "触发 Saga 级联补偿")
f.arrow(260, 295, 220, 295, "完成")
f.pill(20, 295, "安全事务终止", fill=C.purple_s, tc=C.purple_d, stroke=C.purple)
f.arrow(60, 295, 40, 295)

f.save("fig-saga-compensation-flow")
print("ch085 figures generated successfully")
