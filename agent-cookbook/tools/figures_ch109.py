# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 图 109-1: 开源贡献生命周期与 CI/CD 质量门禁流水线
f = F(940, 420)
f.box(40, 50, 240, 150, "1. Issue 提案与 RFC 论证\n• 需求/漏洞动机说明 (Why)\n• 架构变更影响面评估\n• 接口向后兼容性契约\n• 社区评审与 Label 认领", fill=C.blue_s, stroke=C.blue)
f.box(340, 50, 260, 150, "2. 本地开发与确定性测试\n• Git 分支规范 (feat/fix/...)\n• 单元与契约测试覆盖 (pytest)\n• 静态类型检查 (mypy/ruff)\n• check_chapter 质量门禁自检", fill=C.indigo_s, stroke=C.indigo)
f.box(640, 50, 260, 150, "3. GitHub Actions 自动化门禁\n• 全量规范校验 (Check All)\n• 依赖漏洞安全扫描\n• 页面排版渲染测试\n• 自动化评测与代码评审", fill=C.teal_s, stroke=C.teal)

f.arrow(280, 125, 340, 125, color=C.blue)
f.arrow(600, 125, 640, 125, color=C.indigo)

f.box(80, 250, 780, 140, "4. 社区合并与持续发布飞轮 (Continuous Delivery Loop)\n• Maintainer 双人同行审查 (Code Review) -> 合并至 master 分支\n• 自动化生成版本变更日志 (Semantic Release & CHANGELOG)\n• GitHub Pages & CDN 全球边缘实时同步部署\n• 贡献者致谢徽章更新与社区生态反哺激励", fill=C.purple_s, stroke=C.purple)

f.arrow(160, 200, 160, 250, color=C.blue)
f.arrow(470, 200, 470, 250, color=C.indigo)
f.arrow(770, 200, 770, 250, color=C.teal)

f.save("fig-open-source-contribution-lifecycle")
print("Saved fig-open-source-contribution-lifecycle.svg")

# 图 109-2: 本书长远技术演化与生态扩展路线图 (Roadmap & Ecosystem Evolution)
f2 = F(940, 360)
f2.box(40, 50, 190, 260, "Phase 1: 全景典籍筑基\n(已达成)\n\n• 113 章完整技术体系\n• 4 大附录及理论形式化\n• 80+ 矢量架构图谱\n• 10 个工业级全栈项目\n• 1000+ 印刷页全景覆盖", fill=C.green_s, stroke=C.green)
f2.box(260, 50, 200, 260, "Phase 2: 交互实验靶场\n(演进中)\n\n• 在线代码沙箱 (WebR/WASM)\n• 一键部署 Docker Compose\n• 交互式 Agent 拓扑仿真器\n• 多模型实时评测对比看板\n• 在线自测与认证题库", fill=C.blue_s, stroke=C.blue)
f2.box(490, 50, 200, 260, "Phase 3: 社区协同生态\n(规划中)\n\n• 多语言翻译 (英/日/法)\n• 社区插件市场与 Skill 库\n• 工业场景案例众包精选\n• 开放学术基准协同打榜\n• 开发者技术沙龙与研讨会", fill=C.amber_s, stroke=C.amber)
f2.box(720, 50, 180, 260, "Phase 4: 自主演化基座\n(未来探索)\n\n• Self-Evolving Agent 自动纠错\n• 实时监控 arXiv 自动生成补丁\n• 社区智能问答数字孪生\n• 神经符号世界模型实验\n• 通用超级智能体试验田", fill=C.red_s, stroke=C.red)

f2.arrow(230, 180, 260, 180, color=C.green)
f2.arrow(460, 180, 490, 180, color=C.blue)
f2.arrow(690, 180, 720, 180, color=C.amber)

f2.save("fig-cookbook-evolution-roadmap")
print("Saved fig-cookbook-evolution-roadmap.svg")
