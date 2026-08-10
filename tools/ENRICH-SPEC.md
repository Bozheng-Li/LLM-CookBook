# 章节内容深度充实规范（Beginner-Book 粒度）

> 本规范用于把每一页提升到「新手入门书籍」级别的细粒度深度。所有写手必须先读本文件，再读标杆页。
>
> **标杆页（已用脚本验证达标，照这两页对齐密度与写法）：**
> - `pages/03-transformer/positional-encoding.html` — 5657 字 / 5 图 4 种 / 5 表 / 3 码 / 3 深入块 / 8 外链
> - `pages/03-transformer/multi-head.html` — 5502 字 / 6 图 5 种 / 8 表
>
> ⚠️ 历史遗留提示：`pages/03-transformer/attention.html` 曾被当作标杆，实测只有 2399 字正文、0 外链，**不要再照它对齐**。

---

## 一、目标

当前多数页面偏「概览式」：图少、表少、缺例子、缺代码、缺动手环节。目标是把它们充实为**像书一样的细粒度讲解**——先给直觉，再讲机制，配上具体例子、数字、对比表、流程图、代码和可练习的小问题。

**不是**把已有正确内容删掉重写，而是**在保留原有准确内容的基础上大幅扩充**，优先补「真实价值」：例子、数字、对比、步骤、坑。

---

## 二、达标线（每页最低要求）

**唯一验收标准是脚本 `tools/check.py`，不是你的主观感觉，也不是你自己数出来的字符数。**

| 维度 | 最低要求 | 说明 |
|---|---|---|
| 正文中文字数 | **≥5000** | 见下方口径定义。上不封顶，写得越透越好 |
| Mermaid 图数量 | **≥4** 且**≥2 种类型** | 全用 flowchart 视为不达标 |
| 表格数量（`.table-wrap`） | **≥3** | |
| 代码块 | **≥1** | 实战篇建议更多，但每段都要配中文解读 |
| `<details class="deep">` 深入块 | **≥1** | 放推导、踩坑实录、参数调优记录 |
| 参考文献（真实 URL） | **≥3** | 必须是 `href="https://..."` 的外链 |
| 提示框 callout | ≥3 | 建议项，脚本不强制 |

### 字数口径（最容易搞错，务必看清）

脚本只统计 `<main>` 元素内的**中文汉字**，并且会**剔除**：

- `<div class="mermaid">` 里的图内文字
- `<pre>` 代码块
- `<script>` 脚本

**所以堆图、堆代码、堆英文术语都无法提高字数。** 常见误判：把"可见文本字符数"（含英文单词、标点、空格）当成字数，会虚高 3–4 倍。以脚本为准。

### 自检命令（每写完一页必须跑）

```bash
cd /e/大模型知识
/c/Users/Libozheng/.workbuddy/binaries/python/versions/3.13.12/python.exe tools/check.py 03-transformer   # 按篇
/c/Users/Libozheng/.workbuddy/binaries/python/versions/3.13.12/python.exe tools/check.py all              # 全站
```

输出逐页标注 `OK` / `GAP`，`GAP` 后面会写明缺哪一项。**只有显示 OK 才算完成。**

### 怎么把正文写厚（核心方法）

每个 `<h2>` 小节展开到 **600–900 字**，按这个节奏写：

1. **为什么需要** — 不做会怎样，用具体场景或反例引入
2. **机制是什么** — 讲清原理，必要时给公式（已加载 KaTeX，行内 `\(...\)`、块级 `$$...$$`）
3. **具体数字或算例** — 这是新手书籍与大纲的分水岭。带着读者算一遍
4. **失败模式与工程取舍** — 什么情况下会出问题，实际怎么权衡

**代码密集的页面（尤其 15-practice）**：每段代码前 150–300 字讲"这一步解决什么问题、为什么这么设计、有哪些替代方案"，代码后 200–400 字逐行解读关键参数的取值理由与常见报错。代码本身不计字数，但解读计入，且对新手最有用。

---

## 三、Mermaid 图的类型要求（禁止只用方框流程图）

**硬性要求：同一页至少 2 种不同图型，脚本会检查。** 全站曾出现过绝大多数页面 4–13 张图全是 flowchart 的情况，读者只能看到一堆方框。

- 必须包含：**至少 1 张 flowchart**（通常是「一图看懂」概览）。
- 其余图按需从下列类型中选，**必须类型多样**：
  - `sequenceDiagram`：训练循环、推理流程、多步交互、Agent 循环
  - `stateDiagram-v2`：状态机、训练稳定性、解码状态
  - `mindmap`：概念分类、方法族、能力地图
  - `timeline`：发展历史、版本演进
  - `classDiagram`：模块/类关系、架构组成
  - `journey`：用户体验/任务流程
  - `pie`：占比/分布（谨慎用，仅当确有比例数据）
- 图注 `<figcaption>` 必写，说明这张图在表达什么。
- 节点文本用双引号包裹；避免 `(` `)` `,` 等特殊字符，需换行用 `<br/>`。
- 可用 `style 节点ID fill:#xxx` 高亮关键节点（配色参考：`#e6f1fb`/`#185fa5` 蓝、`#eaf3de`/`#639922` 绿、`#faeeda`/`#ba7517` 橙、`#fcebeb`/`#a32d2d` 红）。

---

## 四、表格要求

- 所有表格必须套 `<div class="table-wrap"><table>...</table></div>`，否则窄屏溢出。
- 表格类型建议：对比表（A vs B vs C）、参数表、优缺点表、选型决策表、时间线表、参考清单表。
- 表头用 `<thead>`，数据用 `<tbody>`；关键单元格加 `<strong>`。

---

## 五、正文结构（推荐顺序，可据主题调整）

1. **一图看懂**（overview-card + flowchart）— 一句话讲透核心，配生活化类比。
2. **3–8 个 `<h2>` 小节**，每节遵循：提出问题 → 讲清机制 → 给具体例子/数字 → 下结论。不要罗列名词。
3. 适当用 `<h3>` 拆子点。
4. **要点速查**（`<h2>要点速查</h2>` + `<ul>`）— 保留并扩充。
5. **参考文献与延伸阅读**（`<h2>参考文献与延伸阅读</h2>` + `<ul class="refs">`）— 保留并扩充。
6. **接下来**（callout，含正确的相对路径链接）。

---

## 六、写作风格（必须做到）

- 先给直觉再给形式：先说「像带着问题去图书馆找书」，再上公式。
- 用具体例子：讲注意力举指代消解句；讲量化举「7B 模型 FP16 权重约 14GB」这种具体数字。
- 讲清「为什么」：不只是「是什么」。
- 点出真实坑：工程师最需要的「什么情况下会出问题」。
- 数字要具体；拿不准就写「具体以官方文档为准」，禁止编造。

---

## 七、Chart.js 图表（可选，但鼓励在量化场景使用）

当页面有自然的数量对比（规模律曲线、显存占用、基准分数、成本对比、参数量）时，可用交互图表替代静态图。模板：

```html
<div class="chart-box"><canvas id="chart-<唯一id>"></canvas></div>
<script>
(function(){
  if (typeof Chart === 'undefined') return;
  var ctx = document.getElementById('chart-<唯一id>');
  if (!ctx) return;
  var ch = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['标签A','标签B','标签C'],
      datasets: [{ label:'系列名', data:[10,20,30],
        backgroundColor: window.CB_COLORS.blueSoft,
        borderColor: window.CB_COLORS.blue, borderWidth:1.5 }]
    },
    options: { responsive:true, maintainAspectRatio:false,
      plugins:{ legend:{ display:true } },
      scales:{ y:{ beginAtZero:true } } }
  });
  if (window.CB_CHARTS) window.CB_CHARTS.push(ch);
})();
</script>
```

配色用 `window.CB_COLORS`（blue/amber/green/red/purple/teal/gray 各含主色与 Soft 浅色）。**若不确定数据准确性，改用表格，不要编造数字。**

---

## 八、铁律（违反即废稿）

1. 第二行必须是 `<!-- cookbook:handcrafted -->`（保留原有，勿删）。
2. `data-part` / `data-topic` 与文件路径一致（勿改）。
3. 难度标签（`basic`/`inter`/`adv`）与 `toc.json` 一致（勿改）。
4. 中文正文用中文标点「，。；：」；代码/命令用 ASCII 直引号。
5. 不编造：数字、论文标题、URL、API 参数名——拿不准就不写或写「以官方文档为准」。
6. 交叉引用用相对路径：同篇 `xxx.html`，跨篇 `../<part-id>/xxx.html`。Part 目录名见 `tools/toc.json`。
7. **只改自己负责的页面**，不动 `toc.json`、`generate.py`、其他人的页面。
8. 代码块里 `<` 写成 `&lt;`，`&` 写成 `&amp;`。
9. 参考文献链接必须是你确认存在的真实 URL（arXiv 优先）；不确定是否有效就写论文名不加链接，标注「搜索获取」。

---

## 九、自检清单（每页写完逐项确认）

- [ ] 第二行有 `<!-- cookbook:handcrafted -->`
- [ ] `data-part` / `data-topic` 与文件路径一致
- [ ] 难度标签与 `toc.json` 的 `level` 一致
- [ ] 有「一图看懂」+ 至少 1 张 flowchart
- [ ] Mermaid 图数量达标且类型多样（并非全是 flowchart）
- [ ] 表格数量达标且都套了 `.table-wrap`
- [ ] 有代码块（如主题可实现）且 `<`/`&` 已转义
- [ ] 有 ≥1 个 `<details class="deep">` 深入块
- [ ] 有「要点速查」「参考文献」「接下来」
- [ ] 参考文献 ≥3 条，链接真实不编造
- [ ] 没有编造的数字、论文名、URL
- [ ] 中文用中文标点
- [ ] 交叉链接路径正确，无指向不存在页面的死链

---

## 十、输出方式

把充实后的完整 HTML **写回原文件路径**（覆盖）。保留原有正确的章节，重点在扩充。写完后用中文简要回报：每页扩充后的 Mermaid 图数、表格数、是否含代码/Chart.js、参考文献条数。
