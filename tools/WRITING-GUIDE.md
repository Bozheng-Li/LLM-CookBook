# Cookbook 正文写作规范

> 所有知识点页面必须遵守本规范。参考样板：`pages/03-transformer/attention.html`、`pages/04-modern-arch/moe.html`、`pages/10-applications/rag.html`

---

## 一、铁律

1. **第二行必须是 `<!-- cookbook:handcrafted -->`** —— 没有这个标记，下次跑 `generate.py` 你写的内容会被占位骨架覆盖。
2. **中文正文用中文标点**，代码/配置/命令用 ASCII 直引号。
3. **不要编造**：数字、论文标题、URL、API 参数名，拿不准就不写，或写"具体以官方文档为准"。
4. **交叉引用用相对路径链接**，同篇内 `xxx.html`，跨篇 `../<part-id>/xxx.html`。Part 目录名见 `tools/toc.json`。
5. 只改自己负责的页面，不动 `toc.json`、`generate.py`、其他人的页面。

---

## 二、页面骨架（直接复制修改）

```html
<!DOCTYPE html>
<!-- cookbook:handcrafted -->
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【页面标题】 · 大模型技术 Cookbook</title>
  <link rel="stylesheet" href="../../assets/css/theme.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <link id="hljs-theme" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github.min.css">
</head>
<body data-part="【篇目录名】" data-topic="【词条id】">
  <header id="topbar"></header>
  <div class="layout">
    <nav id="sidebar"></nav>
    <main class="main">
      <div class="with-toc">
        <div class="container">
          <div id="breadcrumb"></div>
          <div class="page-head">
            <div class="meta">
              <span class="level basic">入门</span>
            </div>
            <h1>【标题】</h1>
            <p class="lead">【导语：2-3 句话，说清这一节解决什么问题、为什么重要。要有钩子，不要写"本节介绍…"】</p>
          </div>

          <!-- 正文主体 -->

          <div id="pager"></div>
        </div>
        <aside id="pageToc"></aside>
      </div>
    </main>
  </div>
  <script src="../../assets/js/toc.js"></script>
  <script src="../../assets/js/search-index.js"></script>
  <script>window.ROOT = "../../";</script>
  <script src="../../assets/js/nav.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="../../assets/js/render.js"></script>
</body>
</html>
```

难度标签三选一（与 `toc.json` 的 `level` 一致）：
```html
<span class="level basic">入门</span>
<span class="level inter">进阶</span>
<span class="level adv">高级</span>
```

---

## 三、正文结构（推荐顺序）

### 1. 一图看懂（必备，紧跟导语）

```html
<div class="overview-card">
  <div class="card-title">一图看懂</div>
  <p>【一句话讲透核心机制，最好带一个生活化类比】</p>
  <figure class="figure" style="background:transparent;border:none;padding:8px 0 0">
    <div class="mermaid">
flowchart LR
  A["输入"] --> B{"处理"}
  B --> C["输出"]
    </div>
    <figcaption>【图注：一句话说明这张图在表达什么】</figcaption>
  </figure>
</div>
```

**Mermaid 注意**：节点文本用双引号包裹；避免节点文本里出现 `(` `)` `,` 等特殊字符，需要时用 `<br/>` 换行。

### 2. 若干 `<h2>` 小节（3-6 个）

每节遵循 **提出问题 → 讲清机制 → 给出结论** 的顺序。不要罗列名词。

### 3. 要点速查（必备，倒数第二块）

```html
<h2>要点速查</h2>
<ul>
  <li><strong>本质</strong>：……</li>
  <li><strong>关键参数</strong>：……</li>
  <li><strong>常见坑</strong>：……</li>
</ul>
```

### 4. 接下来（必备，最后一块）

```html
<div class="callout">
  <span class="callout-t">接下来</span>
  【承上启下，链接 1-2 个相关页面】<a href="xxx.html">下一节标题</a>
</div>
```

---

## 四、可用组件

### 提示框

```html
<div class="callout tip"><span class="callout-t">一句话直觉</span>【类比或直觉解释】</div>
<div class="callout warn"><span class="callout-t">常见误区</span>【易错点】</div>
<div class="callout"><span class="callout-t">自定义标题</span>【中性说明】</div>
```

### 三列卡片

```html
<div class="grid g3">
  <div class="card">
    <div class="card-title">标题</div>
    <p style="font-size:13.5px;margin:0;color:var(--text-2)">说明文字</p>
  </div>
</div>
```
两列用 `g2`，四列用 `g4`。

### 表格（必须套 `.table-wrap`，否则窄屏溢出）

```html
<div class="table-wrap">
  <table>
    <thead><tr><th>列1</th><th>列2</th></tr></thead>
    <tbody><tr><td>值1</td><td>值2</td></tr></tbody>
  </table>
</div>
```

### 公式（KaTeX）

行内：`$O(n^2)$`　　独立成行：
```html
<div class="figure" style="text-align:center">
  $$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$
</div>
```

### 折叠深入块（放推导、完整代码、扩展阅读）

```html
<details class="deep">
  <summary>展开：【标题】</summary>
  <div class="deep-body">
    <p>【内容】</p>
  </div>
</details>
```

### 代码块

```html
<pre><code class="language-python">import torch

def foo(x):
    return x * 2</code></pre>
```

**注意**：HTML 里 `<` 要写成 `&lt;`，`&` 写成 `&amp;`。

---

## 五、写作风格

### 要这样写

- **先给直觉，再给形式**。先说"就像带着问题去图书馆找书"，再上公式。
- **用具体例子**。讲注意力就举 "The animal didn't cross the street because **it** was too tired" 这种能看出指代的句子。
- **讲清楚为什么**，不只是是什么。"为什么要除以 √dₖ" 比 "公式是这样" 有价值得多。
- **点出真实的坑**。工程师最需要的是"什么情况下会出问题"，这是文档和教程通常缺的部分。
- **数字要具体**。"显存占用大" → "7B 模型 FP16 权重约 14GB"。

### 不要这样写

- ❌ "本节将介绍……" / "综上所述……" / "随着人工智能的飞速发展……"
- ❌ 名词堆砌：把术语列一排却不解释关系
- ❌ 空泛的形容词："非常重要"、"极大提升"——给数字或不写
- ❌ 假装确定：不确定的事写"具体取决于实现"，不要编

### 篇幅

- 入门 basic：3000-4500 字，重直觉和例子
- 进阶 inter：4000-5500 字，机制讲透 + 工程细节 + 对比表
- 高级 adv：4500-6000 字，可用折叠块放推导和深度代码

字数指正文可见文本，不含 HTML 标签。**宁可丰富而扎实，不要精简而空洞。**

### 图表质量要求（升级）

- **Mermaid 图至少 2 张**：一张概览流程图（一图看懂），至少一张细节图（架构拆解 / 时序图 / 对比矩阵）
- 节点文本用双引号包裹，避免特殊字符，需要换行用 `<br/>`
- **时序图**用 `sequenceDiagram`，**状态转移**用 `stateDiagram-v2`，**对比**用表格不要用 Mermaid
- 图注（`<figcaption>`）不能省，要说明这张图在表达什么
- 复杂流程可以加颜色标注关键节点（`style 节点ID fill:#xxx`）

### 参考文献（新增）

每页末尾「接下来」之前，加一个参考文献区：

```html
<h2>参考文献与延伸阅读</h2>
<ul class="refs">
  <li>论文/文章标题 — 一句话说明它提供了什么 · <a href="https://..." target="_blank" rel="noopener">链接</a></li>
</ul>
```

要求：
- 至少 2-3 条，优先原始论文（arXiv）和官方文档
- 链接必须是你确认存在的真实 URL，**禁止编造**
- 如果不确定 URL 是否有效，写论文名称但不加链接，标注「搜索获取」
- 每条附一句话说明它与本页内容的关联

---

## 六、自检清单

写完每页逐项确认：

- [ ] 第二行有 `<!-- cookbook:handcrafted -->`
- [ ] `data-part` / `data-topic` 与文件路径一致
- [ ] 难度标签与 `toc.json` 的 `level` 一致
- [ ] 有「一图看懂」+ Mermaid 图
- [ ] 有「要点速查」
- [ ] 有「接下来」且链接路径正确
- [ ] 表格都套了 `.table-wrap`
- [ ] 代码块里的 `<` `&` 已转义
- [ ] 没有编造的数字、论文名、URL
- [ ] 中文用中文标点

验证命令：
```bash
python tools/migrate_v02.py --verify   # 死链校验
```
