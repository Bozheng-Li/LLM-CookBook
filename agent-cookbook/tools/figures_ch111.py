# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 图 111-1: 智能体高级工程面试四大核心考查支柱
f = F(940, 420)
f.box(40, 50, 240, 150, "1. 强化学习与后训练对齐\n• PPO / GRPO / DPO 算法机理\n• 过程奖励模型 (PRM) 训练\n• 策略熵坍缩与奖励黑客攻防\n• 弱到强泛化监督 (Weak-to-Strong)", fill=C.blue_s, stroke=C.blue)
f.box(340, 50, 260, 150, "2. 搜索规划与世界模型动力学\n• 蒙特卡洛树搜索 (MCTS) 四阶段\n• 测试期计算扩展律 (Test-Time Compute)\n• RSSM 状态空间与潜在想象 (Dreamer)\n• 启发式剪枝与价值引导搜索", fill=C.indigo_s, stroke=C.indigo)
f.box(640, 50, 260, 150, "3. 分布式系统与高并发工程\n• Actor 并发拓扑与事件流总线\n• Saga 事务补偿协议与逆向回滚\n• Redis Lua 幂等 Token 机制\n• 流式长连接背压与断点续生", fill=C.teal_s, stroke=C.teal)

f.arrow(280, 125, 340, 125, color=C.blue)
f.arrow(600, 125, 640, 125, color=C.indigo)

f.box(80, 250, 780, 140, "4. 极端场景故障容灾与安全防御纵深 (Resilience & Hardening)\n• 间接提示词注入 Spotlight 物理隔离与 CaMeL 双模型解耦\n• Linux gVisor / Firecracker 轻量级容器虚拟化物理沙箱\n• 上下文长程漂移纠偏与双向锚定强化机制\n• 确定性自动化判题 Harness 与端到端状态断言", fill=C.purple_s, stroke=C.purple)

f.arrow(160, 200, 160, 250, color=C.blue)
f.arrow(470, 200, 470, 250, color=C.indigo)
f.arrow(770, 200, 770, 250, color=C.teal)

f.save("fig-agent-interview-advanced-pillars")
print("Saved fig-agent-interview-advanced-pillars.svg")

# 图 111-2: 工业级高难故障复盘与架构解耦闭环 (Incident Post-Mortem Architecture)
f2 = F(940, 360)
f2.box(40, 50, 190, 260, "现场还原 (Incident)\n\n• 现象: 级联死循环\n• 表现: QPS 飙升 10 倍\n• 症状: Token 成本爆炸\n• 影响: 业务下游数据库锁死", fill=C.red_s, stroke=C.red)
f2.box(260, 50, 200, 260, "根因定界 (Root Cause)\n\n• 状态机隐式转换失效\n• 偶发 504 导致重试风暴\n• 缺乏动作去重指纹\n• 上下文丢失前置规则", fill=C.amber_s, stroke=C.amber)
f2.box(490, 50, 200, 260, "架构止血 (Containment)\n\n• 引入 Redis Lua 幂等排重\n• 全局步数硬阈值限制 (Max 10)\n• 动作哈希滑动窗口熔断\n• 降级至预置白名单模板", fill=C.blue_s, stroke=C.blue)
f2.box(720, 50, 180, 260, "长效治理 (Prevention)\n\n• 显式 Pregel 状态图解耦\n• 引入 gVisor 物理隔离\n• CI/CD 混沌工程回归注入\n• OpenTelemetry 全链路追踪", fill=C.green_s, stroke=C.green)

f2.arrow(230, 180, 260, 180, color=C.red)
f2.arrow(460, 180, 490, 180, color=C.amber)
f2.arrow(690, 180, 720, 180, color=C.blue)

f2.save("fig-incident-postmortem-arch")
print("Saved fig-incident-postmortem-arch.svg")
