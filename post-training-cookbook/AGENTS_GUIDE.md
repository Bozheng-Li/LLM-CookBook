# 《大模型后训练实战 Cookbook》写作规范（供协作作者/Agent 使用）

本文件是全书唯一写作标准。所有章节必须严格遵循，保证 65 章风格完全一致。

## 0. 技术要求（必须 100% 遵守）

1. **文件位置**：所有章节写到 `chapters/` 目录，文件名与章节清单一致（见 `assets/js/manifest.js`）。UTF-8 编码。
2. **HTML 骨架**：完整复制 `chapters/_template.html` 的 `<head>`（title 改成本章）与 `<body>` 外层结构：
   - `<aside class="sidebar" id="sidebar"></aside>`（留空，nav.js 自动填充）
   - `<main class="content">` 包裹全部正文
   - `<header class="chapter-header">`：crumb（第 X 部分 · 部分名）、`<h1>`（第 N 章 · 标题）、`chapter-lead` 导语、`chapter-meta`（预计学习时长/难度星级/先修章节）
   - `<nav class="toc-box" id="auto-toc"></nav>`（留空，自动生成）
   - 结尾必须有：本章小结（h2）、自测题 `.quiz`（至少 3 题）、`参考文献`（h2 + `ol.refs`，至少 8 条）、`<footer class="chapter-footer"></footer>`
3. **公式**：MathJax，行内 `\( ... \)`，独立 `\[ ... \]`。**禁止**在公式环境内使用 Markdown。代码块内禁止出现 `\( \)`。
4. **代码**：`<div class="code-wrap"><span class="code-label">文件名或语言</span><pre class="code"><code class="language-python">...（HTML 转义 `<`、`>`、`&`）</code></pre></div>`。代码要完整、贴近真实可运行（超参、关键行注释用中文）。
5. **图片**：
   - 位图只能使用 `assets/figs/` 中已有的文件（清单见下），引用路径 `../assets/figs/xxx.png`，**必须**带 `<figure class="figure">` + figcaption（含论文出处与 arXiv 号）。
   - 鼓励并要求自绘内联 SVG 示意图（`<svg class="diagram" viewBox="0 0 720 H">`）：架构图、流程图、对比图、数据流转图。配色只用：`#2563eb`（主）、`#10b981`（绿）、`#f59e0b`（橙）、`#ef4444`（红）、`#8b5cf6`（紫），底色可用 `#eff6ff / #ecfdf5 / #fffbeb / #fef2f7 / #f5f3ff`，文字 `#1e293b`。每个 SVG 至少 720×180，文字用 `font-size="14~16"`，箭头用 marker。
6. **每章体量**（这是硬指标，缺一不可）：
   - 正文中文 ≥ 5000 字（不含代码与表格）；
   - ≥ 6 个 h2 大节 + 合理 h3；
   - ≥ 3 个代码块；≥ 2 个表格；≥ 2 个图（SVG 自绘 ≥ 1，位图可用 figs 清单）；
   - ≥ 8 篇参考文献（含 arXiv 号）；≥ 3 道自测题；
   - ≥ 2 个 callout（note/tip/warn/danger 至少各展所长）。
7. **标题层级**：h1 仅用于章题；h2 大节（编号如 `1.`、`2.`…）；h3 小节；禁止 h5 以下。
8. **链接**：站内链接用相对路径（如 `12-sft-fundamentals.html`）；论文用 `https://arxiv.org/abs/XXXX.XXXXX`；GitHub 项目用完整 URL。

## 1. 语言风格

- 简体中文，面向有深度学习基础但刚接触后训练的工程师/研究生：**先直觉、再公式、后代码**。
- 术语规范：首次出现写全称，格式 `监督微调（Supervised Fine-Tuning, SFT）`，之后可用缩写。
- 语言干净、具体、有判断力：直接给结论和数值（学习率、显存、数据量），避免"可能""或许"堆砌；避免营销腔、避免空洞排比。
- 每章开头导语 80~150 字；每节结尾给一句"小结句"。
- 批判性视角：讲方法时说清局限与失效场景，给出"什么时候不要用"。

## 2. 内容结构建议（可按章节微调）

1. 开篇：问题动机 + 一图流总览（SVG）
2. 历史与动机（关键论文脉络）
3. 核心原理（直觉 → 数学 → 算法伪代码）
4. 实现细节与工程要点（代码 + 超参表）
5. 实战案例或实验分析（数值、曲线描述、失败案例）
6. 与其他方法的对比（表格）
7. 常见坑与排查
8. 本章小结 + 自测题 + 参考文献

## 3. 位图配图清单（assets/figs/，只能用这些）

| 文件 | 内容 | 尺寸 | 建议用章 |
|---|---|---|---|
| transformer-arch.png | Transformer 架构（Attention Is All You Need 图1） | 1520×2239 竖图 | 03 |
| instructgpt-pipeline.png | InstructGPT 三阶段 RLHF 流程 | 1320×1020 | 18, 00 |
| scaling-laws.png | Scaling laws 效率示意（Kaplan 图） | 1265×507 | 04 |
| self-instruct.png | Self-Instruct 流程 | 687×1057 竖图 | 08 |
| evol-instruct.png | Evol-Instruct 演化流程 | 1600×900 | 08 |
| lora.png | LoRA 低秩分解示意 | 1249×396 | 14 |
| qlora.png | QLoRA NF4 量化示意 | 960×420 | 14 |
| cai.png | Constitutional AI 流程 | 2025×844 | 33 |
| zephyr.png | Zephyr dDPO 训练流程 | 2026×1008 | 22, 47 |
| dpo.png | DPO teaser（RLHF vs DPO 对比） | 2380×478 | 22 |
| simpo.png | SimPO 方法示意 | 1661×322 | 23 |
| kto.png | KTO 效用示意图 | 814×574 | 23 |
| orpo.png | ORPO 方法示意 | 2289×687 | 23 |
| spin.png | SPIN 自博弈流程 | 1010×375 | 49 |
| grpo.png | DeepSeekMath GRPO 流程 | 946×416 | 25 |
| dapo.png | DAPO 方法与结果 | 1528×611 | 25 |
| deepseek-r1.png | R1 论文 PPO vs GRPO 训练管线 | 2020×1300 | 26, 27 |
| deepseek-r1-aime.png | R1 蒸馏模型 AIME 曲线 | 5075×3271 | 30 |
| omegaprm.png | OmegaPRM 蒙特卡洛树搜索 | 2400×1500 | 28 |
| mtbench.png | MT-Bench / LLM-as-judge 界面 | 2746×1374 | 39 |
| llama2-winrate.png | Llama 2 胜率图 | 2025×1350 | 47 |
| tulu3.png | Tulu 3 后训练管线 | 2040×712 | 47, 07 |

## 4. 禁止事项

- 禁止引用不存在的文件/图片/链接；禁止编造实验数值——引用他人论文数据时给出出处。
- 禁止使用 Mermaid、外部 JS 图表库、CDN CSS（MathJax 与既有 head 内容之外不加任何外部资源）。
- 禁止修改 `assets/`、`index.html`、`manifest.js` 及其他章节文件——只写分配给你的文件。
- 禁止出现占位文本（"待补充""TODO""此处省略"）。
- 代码块内禁止出现连续 5 个以上空行；HTML 中禁止内联 `style`（caption 除外，可用给出的写法）。

## 5. 交付自检清单（写完每个文件后逐项核对）

- [ ] head 与模板一致（css/manifest/mathjax/nav 均已引入，title 已改）
- [ ] chapter-header 四件套齐全（crumb/h1/lead/meta）
- [ ] 正文 ≥ 5000 中文字；h2 ≥ 6；代码 ≥ 3；表格 ≥ 2；图 ≥ 2（含自绘 SVG ≥ 1）
- [ ] 所有 `<` `>` `&` 在代码块中已转义；公式不在代码块内
- [ ] 图片路径与 figs 清单完全一致
- [ ] 参考文献 ≥ 8 条且含 arXiv 号；自测题 ≥ 3 道；有本章小结
- [ ] 文件以 `</html>` 结尾，无截断
