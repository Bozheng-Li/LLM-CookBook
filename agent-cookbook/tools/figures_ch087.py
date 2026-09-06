# -*- coding: utf-8 -*-
"""figures_ch087.py — ch087 全栈 Web 前端开发与 GUI 测试 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 87-1: 全栈 Web 开发与视觉回归闭环流水线
f = F(940, 420)
f.box(40, 60, 160, 110, "1. 设计稿/需求感知\nFigma / UI 需求\n视觉布局提取\n组件原子分解 (Atomic)", fill=C.blue_s, stroke=C.blue)
f.box(240, 60, 170, 110, "2. 全栈代码生成\nReact/Tailwind/Next\nTypeScript 强类型\nREST/GraphQL 接口桩", fill=C.indigo_s, stroke=C.indigo)
f.box(450, 60, 180, 110, "3. 无头热重载与沙箱\nPlaywright / Vite HMR\n本地瞬时沙箱渲染\nDOM 树与控制台捕获", fill=C.amber_s, stroke=C.amber)
f.box(670, 60, 230, 110, "4. 视觉回归与多模态自愈\nVLM 像素级比对 (SSIM)\n控制台 JS 报错捕获\n自动修正 CSS / Hook (TDD)", fill=C.teal_s, stroke=C.teal)

f.arrow(200, 115, 240, 115, "组件规范")
f.arrow(410, 115, 450, 115, "JSX / CSS 代码")
f.arrow(630, 115, 670, 115, "渲染快照 / 日志")

# 底部视觉偏差自愈闭环
f.elbow([(785, 170), (785, 240), (540, 240), (540, 170)], label="视觉比对不一致 (SSIM < 0.95) 或 JS 崩溃: 提取差异坐标反思自愈", color=C.red, label_pos=1)

# 底部基础设施
f.box(100, 290, 740, 100, "工业级前端 Agent 基础设施支撑 (Web Engineering Infrastructure)\n• 虚拟浏览器沙箱: Playwright / Chromium 无头集群 (隔离网络与 Cookie 泄露)\n• 响应式多端探测: 自动在 Mobile (375px)、Tablet (768px)、Desktop (1440px) 三端截屏\n• 无障碍 A11y 审计: 自动化 Axe-core 扫描，确保 WCAG 2.1 规范无死角达标", fill=C.purple_s, stroke=C.purple)

f.save("fig-web-gui-agent-arch")

# fig 87-2: 视觉回归比对与差异热力图定位
f = F(940, 360)
f.box(60, 100, 190, 160, "Figma 设计稿基准\n(Design Baseline)\n• 按钮圆角: 8px\n• 强调色: #3B82F6\n• 间距: padding 16px\n(预期视觉金标)", fill=C.blue_s, stroke=C.blue)

f.box(300, 100, 190, 160, "当前渲染页面截屏\n(Current Render)\n• 按钮圆角: 0px (误设)\n• 强调色: #1D4ED8 (色偏)\n• 布局: 发生 24px 溢出\n(模型生成的初始代码)", fill=C.amber_s, stroke=C.amber)

f.box(540, 100, 160, 160, "SSIM 像素差分引擎\nPixel-by-Pixel Diff\n计算结构相似性\n高亮红色差异掩码\n(SSIM = 0.84 失败)", fill=C.red_s, stroke=C.red)

f.box(750, 100, 150, 160, "生成 CSS 修正补丁\nTailwind 修补\n`rounded-lg`\n`bg-blue-500`\n`overflow-hidden`", fill=C.green_s, stroke=C.green)

f.arrow(250, 180, 300, 180)
f.arrow(490, 180, 540, 180, "比对")
f.arrow(700, 180, 750, 180, "定位缺陷")

f.save("fig-visual-regression-diff")
print("ch087 figures generated successfully")
