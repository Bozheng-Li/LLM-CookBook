# 《多模态大模型 Cookbook》写作规范（撰稿 Agent 必读）

本书是一部发布到 GitHub 的中文 HTML 技术手册，深度对标《大模型大全》（636 页）：
**完整数学推导 + 可运行代码 + 论文原图 + 对比表格 + 最佳实践 + 自测题**。
每位撰稿 Agent 在写任何章节前必须先完整阅读本文件，并遵守全部规则。

## 1. 语言与文风

- **正文语言**：简体中文。专业术语首次出现时给出英文原文，如 `交叉注意力（Cross-Attention）`。
- 论文标题、模型名、代码、超参数保留英文。不要整句翻译式腔调，用中文技术社区的自然表达。
- 面向读者：有 Python 与深度学习基础、想系统进入多模态领域的研究者/工程师。
- 语气：像一位资深导师手把手讲解——先直觉、再数学、再代码、再实践坑点。
- 禁止空洞套话（"随着人工智能的发展…"之类）。每一段都要有信息量。
- 数字与事实必须准确：年份、作者、会议、arXiv 编号不确定时宁可不写编号，也不要编造。

## 2. 章节文件规范

- 路径：`D:\multimodal-cookbook\chapters\<文件名>`（文件名见 `assets/js/manifest.js`，不得改名）。
- 章节是**自包含 HTML**。骨架如下（占位符替换成你的内容）：

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第 N 章 章节标题 · 多模态大模型 Cookbook</title>
<link rel="stylesheet" href="../assets/css/style.css">
<script>window.MathJax={tex:{inlineMath:[["$","$"],["\\(","\\)"]],displayMath:[["$$","$$"],["\\[","\\]"]]},svg:{fontCache:"global"}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
</head>
<body>
<div id="progress-bar"></div>
<nav id="sidebar"></nav>
<header id="topbar">
  <button id="menu-btn">☰</button>
  <div id="search-box"><input id="search-input" placeholder="搜索全书…"><div id="search-results"></div></div>
  <div class="topbar-actions"><button class="tb-btn" id="theme-btn">🌓 主题</button></div>
</header>
<main class="content"><div class="article">

<header class="book-header">
  <div class="part-badge">第X部分 · 部分名</div>
  <h1 class="chapter-title">第 N 章　章节标题</h1>
  <div class="chapter-meta"><span>预计阅读 90 分钟</span><span>难度 ★★★★☆</span><span>前置：第 A、B 章</span></div>
</header>

<div class="toc-mini"><b>本章目录</b><ol>
  <li><a href="#sec-1">1. …</a></li>  <!-- 列出全部 h2 -->
</ol></div>

<!-- ======== 正文：多个 <h2 id="sec-1">…</h2> 小节 ======== -->

<footer>
  <div class="refs">
    <h2 id="refs">参考文献与推荐阅读</h2>
    <ol>
      <li>Radford A, et al. <a href="https://arxiv.org/abs/2103.00020">Learning Transferable Visual Models From Natural Language Supervision</a>. ICML 2021. arXiv:2103.00020.</li>
      <!-- 每章 12–40 条，含 arXiv 链接 -->
    </ol>
  </div>
  <nav class="pager"></nav>
</footer>

</div></main>
<button id="backtop">↑</button>
<script src="../assets/js/manifest.js"></script>
<script src="../assets/js/book.js"></script>
</body>
</html>
```

- **不要**改动 `<nav id="sidebar">`、`<header id="topbar">`、`<nav class="pager">` 的内部内容（book.js 自动填充）。
- h2 必须带 id（`<h2 id="sec-3">`），id 用 `sec-数字`；其它 id 不得重复。
- 代码块统一写成：

```html
<div class="code-wrap"><div class="code-head"><span class="lang">python</span><button class="copy-btn">复制</button></div>
<pre><code># 代码（< > & 必须写成 &lt; &gt; &amp;）</code></pre></div>
```

## 3. 专栏盒子（本章必须多样化使用）

| class | 用途 | 标题示例 |
|---|---|---|
| `.box-theory` | 数学推导、定理 | 📐 理论推导：InfoNCE 下界 |
| `.box-recipe` | 配方/流程/超参数建议 | 🍳 实战配方：三阶段训练 |
| `.box-tip` | 经验技巧 | 💡 技巧：学习率 warmup 的经验值 |
| `.box-warn` | 常见错误与陷阱 | ⚠️ 陷阱：冻结视觉塔导致对齐失败 |
| `.box-paper` | 论文导读/推荐 | 📄 论文精读：BLIP-2（ICML 2023） |
| `.box-quiz` | 自测题（每章 3–6 题，末尾给答案或折叠提示） | ✏️ 自测 |
| `.box-history` | 历史脉络 | 🕰 历史一刻：2015 Show and Tell |

## 4. 插图规则（图文并茂是硬指标）

1. **论文原图**：先读 `D:\multimodal-cookbook\assets\images\papers\captions.json`（键为 arXiv ID，含 file/caption）。挑选与你的论述相关的图引用。引用格式：
   `<figure><img src="../assets/images/papers/2301.12597_0.png" loading="lazy" alt="Q-Former 结构"><figcaption>图 15-1　<b>BLIP-2 的 Q-Former 架构</b>（来源：Li et al., BLIP-2, arXiv:2301.12597）。图注用自己的话重新概括，不要照抄英文。</figcaption></figure>`
   - 图编号用「图 章号-序号」。每章引用论文原图 **≥3 张**（若 captions.json 中确无合适图则用 SVG 补足）。
2. **自绘 SVG 架构图/示意图**：每章至少 **2 张**内联 SVG（`<figure><svg viewBox="…" style="max-width:100%;background:#fff">…</svg><figcaption>图 N-M …</figcaption></figure>`）。要求：结构清晰、中文标注、配色使用 `#2563eb/#d97706/#10b981/#ef4444/#8b5cf6`、字体 `font-family="sans-serif" font-size="13"`、文字不能溢出边框。SVG 高度建议 220–420。
3. 每章图（原图+SVG）合计 **≥6 张**。
4. 严禁引用不存在于 captions.json 或 papers 目录的图片文件；严禁引用外网图片链接。

## 5. 数学公式

- 行内 `$E = mc^2$`，独立公式用 `<div class="math-block">$$…$$</div>`。
- 关键公式必须配推导步骤和每个符号的中文解释。
- 需要完整推导的内容（对比损失、扩散过程、LoRA 梯度等）放进 `.box-theory` 并分步编号。

## 6. 代码要求

- 每章 **≥4 段**可运行或接近可运行的代码（PyTorch / transformers / TRL / diffusers 等真实 API），单段 15–60 行。
- 代码中的 API 必须真实存在（如 `CLIPModel.from_pretrained("openai/clip-vit-base-patch32")`）。不确定的 API 用伪代码并注明。
- 关键行要有中文注释。

## 7. 表格要求

- 每章 **≥2 张**对比表（模型对比、方法对比、超参数范围、基准结果等），用 `.tbl-wrap` 包裹。

## 8. 长度要求（硬指标，用工具验收）

- **标准章**：可见文本（去标签）≥ 18000 字符。
- **核心大章**（3, 12, 15, 16, 17, 24, 25, 31, 34, 35, 40, 43, 46）：≥ 24000 字符。
- **ch00 指南**：≥ 12000 字符。附录类（50/51/52/53/54）：≥ 15000 字符（表格计入）。
- 写完后运行校验（在 `D:\multimodal-cookbook` 目录下）：
  `python tools/check_html.py chapters/chXX-xxx.html 18000`
  若 FAIL，继续扩充内容（加深推导、增加案例、增加表格）直到 PASS。

## 9. 长文件写法（重要）

单次 Write 太长会被截断。正确做法：把章节正文拆成 2–4 个片段文件（如 `ch12.p1.html`、`ch12.p2.html`、`ch12.p3.html`），最后用 Bash 合并：
`cat chapters/ch12.p1.html chapters/ch12.p2.html chapters/ch12.p3.html > chapters/ch12-clip.html && rm chapters/ch12.p*.html`
然后立即运行 check_html.py 验收。

## 10. 内容深度对标（每章都要达到）

1. **直觉**：这一技术解决什么问题？为什么必须这样设计？
2. **数学**：核心目标函数/推导完整给出，不跳步。
3. **架构**：SVG 图解 + 逐模块讲解（张量形状变化写清楚）。
4. **代码**：最小可运行示例。
5. **实验**：来自论文的关键数字（表格呈现），诚实标注来源。
6. **实践**：超参数配方、常见失败模式与排查。
7. **脉络**：该方向 2015→2026 的演进（放在 box-history 或专门小节）。
8. **论文**：必读论文 3–8 篇精读（box-paper），扩展论文列表进参考文献。
9. **自测**：3–6 道题（含答案要点）。

## 11. 禁止事项

- 禁止修改 `assets/`、`tools/`、`index.html`、`README.md`（只读）。
- 禁止引入除 MathJax CDN 外的任何外部资源。
- 禁止编造论文、数字、arXiv 编号；不确定就写模型/会议名，不写编号。
- 禁止整章只用列表堆砌；论述段与图/表/代码必须交错。
- 禁止 `<h1>` 出现两次；禁止使用 `<style>` 内联大段样式。
