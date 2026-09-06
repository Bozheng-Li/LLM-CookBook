# -*- coding: utf-8 -*-
"""figures_ch088.py — ch088 AI 驱动的渗透测试与红蓝对抗 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 88-1: 授权红蓝对抗与渗透测试 Agent 全景流水线
f = F(940, 420)
f.box(40, 60, 160, 110, "1. 资产侦察与拓扑\nReconnaissance\n授权子域名枚举\n开放端口与中间件扫描", fill=C.blue_s, stroke=C.blue)
f.box(240, 60, 170, 110, "2. 弱点建模与规划\nVulnerability Map\nCVE 知识库匹配\n攻击图谱推演 (DAG)", fill=C.indigo_s, stroke=C.indigo)
f.box(450, 60, 180, 110, "3. 无害化 PoC 验证\nSafe PoC Trigger\n带带外回连 (OOB dnslog)\n严格非破坏性原则", fill=C.amber_s, stroke=C.amber)
f.box(670, 60, 230, 110, "4. 蓝队防线与修补闭环\nBlue Team & Remediation\nWAF 动态拦截规则\n漏洞归因与补丁生成", fill=C.teal_s, stroke=C.teal)

f.arrow(200, 115, 240, 115, "目标指纹")
f.arrow(410, 115, 450, 115, "候选弱点")
f.arrow(630, 115, 670, 115, "验证报告 (PoC)")

# 底部蓝队自动化防御对抗环
f.elbow([(785, 170), (785, 240), (540, 240), (540, 170)], label="蓝队防御 Agent 动态更新 ModSecurity 规则，触发红队次级变异测试", color=C.red, label_pos=1)

# 底部安全守卫与授权交战规则
f.box(100, 290, 740, 100, "授权安全底线与交战规则 (Rules of Engagement - RoE)\n• 严格作用域锁死 (Scope Whitelist: 仅限授权 IP/域名，绝不越界攻击)\n• 破坏性动作零容忍 (严禁 DoS 流量攻击、数据篡改、脱库及持久化提权后门)\n• 审计全证据存证 (每一个 HTTP 请求与回包完整加密签署，保障可审计可复现)", fill=C.purple_s, stroke=C.purple)

f.save("fig-pentest-agent-arch")

# fig 88-2: 攻击树推演与防御加固对立状态机
f = F(940, 360)
f.pill(120, 70, "授权目标资产", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 150, 180, 80, "红队 Agent: 资产侦察\n发现暴露服务\nSpring Boot Actuator", fill=C.red_s, stroke=C.red)
f.box(280, 150, 180, 80, "红队 Agent: 探测弱点\n无害化探测 /env 端点\n证明敏感凭证外露", fill=C.amber_s, stroke=C.amber)
f.box(500, 150, 180, 80, "蓝队 Agent: 实时响应\n定位配置漂移\n生成 Nginx 屏蔽规则", fill=C.teal_s, stroke=C.teal)
f.box(720, 150, 180, 80, "防御闭环: 验证加固\n端点返回 403 Forbidden\n漏洞成功修补闭环", fill=C.green_s, stroke=C.green)

f.arrow(120, 95, 150, 150)
f.arrow(240, 190, 280, 190, "识别端点")
f.arrow(460, 190, 500, 190, "报警事件")
f.arrow(680, 190, 720, 190, "热修补发布")

f.save("fig-red-blue-confrontation")
print("ch088 figures generated successfully")
