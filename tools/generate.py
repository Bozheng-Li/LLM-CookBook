# -*- coding: utf-8 -*-
"""
大模型技术 Cookbook — 站点生成器

读取 tools/toc.json(单一数据源),生成:
  1. assets/js/toc.js            知识树数据(供浏览器使用)
  2. assets/js/search-index.js   全站正文检索索引(供增强搜索)
  3. pages/<part>/index.html     每篇的目录页
  4. pages/<part>/<topic>.html   每个知识点页(已存在且被标记为精编的页面不覆盖)
  5. glossary.html               术语表(关键词聚合 + 反链)
  6. dependency.html             核心依赖脉络图

用法:  python tools/generate.py
"""

import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOC_JSON = os.path.join(BASE, "tools", "toc.json")

# 精编页面标记:含此标记的文件不会被覆盖
KEEP_MARK = "<!-- cookbook:handcrafted -->"

LEVEL_LABEL = {"basic": "入门", "inter": "进阶", "adv": "高级"}
PART_NUM = {p["id"]: p["num"] for p in []}  # 占位,运行时从 toc 取

CDN = """  <link rel="stylesheet" href="{root}assets/css/theme.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <link id="hljs-theme" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github.min.css">"""

SCRIPTS = """  <script src="{root}assets/js/toc.js"></script>
  <script src="{root}assets/js/search-index.js"></script>
  <script>window.ROOT = "{root}";</script>
  <script src="{root}assets/js/nav.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="{root}assets/js/render.js"></script>"""


def page_shell(title, root, part_id, topic_id, body, extra_head="", extra_script=""):
    """统一页面外壳"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} · 大模型技术 Cookbook</title>
{CDN.format(root=root)}
{extra_head}</head>
<body data-part="{part_id}" data-topic="{topic_id}">
  <header id="topbar"></header>
  <div class="layout">
    <nav id="sidebar"></nav>
    <main class="main">
      <div class="with-toc">
{body}
        <aside id="pageToc"></aside>
      </div>
    </main>
  </div>
{SCRIPTS.format(root=root)}
{extra_script}</body>
</html>
"""


def gen_toc_js(toc):
    """生成浏览器端的知识树数据"""
    data = json.dumps(toc, ensure_ascii=False, separators=(",", ":"))
    return (
        "/* 自动生成 — 由 tools/toc.json 派生,请勿直接编辑 */\n"
        "window.TOC = " + data + ";\n"
    )


def gen_search_index(toc):
    """扫描全站正文,生成检索索引(标题/关键词 + 正文片段)"""
    meta = {}
    for part in toc["parts"]:
        meta["pages/%s/index.html" % part["id"]] = {
            "title": part["title"], "level": "basic", "part": part["num"]
        }
        for t in part["topics"]:
            meta["pages/%s/%s.html" % (part["id"], t["id"])] = {
                "title": t["title"], "level": t["level"], "part": part["num"]
            }

    def extract_text(html):
        html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
        html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
        text = re.sub(r"<[^>]+>", " ", html)
        return re.sub(r"\s+", " ", text).strip()

    entries = []
    pages_dir = os.path.join(BASE, "pages")
    for root, dirs, files in os.walk(pages_dir):
        for f in files:
            if not f.endswith(".html"):
                continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, BASE).replace(os.sep, "/")
            if rel not in meta:
                continue
            with open(fp, "r", encoding="utf-8") as fh:
                txt = extract_text(fh.read())
            entries.append({
                "href": rel,
                "title": meta[rel]["title"],
                "level": meta[rel]["level"],
                "part": meta[rel]["part"],
                "text": txt[:2000]
            })
    entries.sort(key=lambda e: (e["part"], e["title"]))
    data = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))
    return (
        "/* 自动生成 — 由全站正文派生,请勿直接编辑 */\n"
        "window.SEARCH_INDEX = " + data + ";\n"
    )


def gen_glossary(toc):
    """术语表:按篇聚合关键词,反链到使用它的知识点"""
    root = ""
    groups = []
    for part in toc["parts"]:
        seen = {}
        for t in part["topics"]:
            for kw in t.get("keywords", []):
                if kw not in seen:
                    users = [tt for tt in part["topics"] if kw in tt.get("keywords", [])]
                    seen[kw] = users
        kws = sorted(seen.keys(), key=lambda k: (len(k), k))
        cells = []
        for kw in kws:
            users = seen[kw]
            links = "".join(
                '<a href="pages/%s/%s.html">%s</a>' % (part["id"], tt["id"], tt["title"])
                for tt in users
            )
            cells.append(
                '<div class="gloss-item"><div style="font-weight:600;margin-bottom:5px">%s</div>'
                '<div class="gi-links">%s</div></div>' % (kw, links)
            )
        groups.append(
            '<div class="gloss-group"><h3><span class="pnum" style="font-family:var(--font-mono);'
            'color:var(--brand)">%s</span>&nbsp; %s · 关键术语</h3>'
            '<div class="gloss-grid">%s</div></div>'
            % (part["num"], part["title"], "".join(cells))
        )

    body = f"""        <div class="container">
          <div id="breadcrumb"></div>
          <div class="page-head">
            <div class="meta"><span class="level basic" style="background:var(--brand-soft);color:var(--brand-deep)">资源</span></div>
            <h1>术语表</h1>
            <p class="lead">把全站出现过的核心术语按「篇」聚合,每个术语都反链到用到它的知识点。遇到不认识的词,先来这里按所在篇章定位。</p>
          </div>
          <div class="callout">
            <span class="callout-t">怎么用</span>术语按所属篇章分组,而不是按 A–Z 排序——这样你能顺着知识树的层级,在对应的语境里理解每个词。
          </div>
{chr(10).join(groups)}
          <div id="pager"></div>
        </div>"""
    return page_shell("术语表", root, "", "", body)


DEP_MERMAID = """flowchart TB
  subgraph F0["00 导论全景"]
    O0["什么是大模型"] --> O1["发展时间线"] --> O2["技术全景图"] --> O3["学习路径"]
  end
  subgraph F1["01 数学基础"]
    M1["线代基础"] --> M2["概率信息论"]
    M2 --> M3["微积分·反向传播"]
    M3 --> M4["优化算法"]
    M1 --> M5["神经网络基础"]
    M2 --> M5
  end
  subgraph F2["02 序列表示"]
    M5 --> R1["语言模型"] --> R2["分词"] --> R3["词嵌入"]
    M3 --> R4["RNN/LSTM"] --> R5["Seq2Seq"]
  end
  subgraph F3["03 Transformer"]
    R5 --> T1["注意力机制"] --> T2["多头注意力"] --> T3["Transformer 架构"]
    M2 --> T4["位置编码"]
    M5 --> T5["归一化"]
    M5 --> T6["FFN"]
    T1 --> T7["残差连接"]
  end
  subgraph F4["04 现代架构"]
    T3 --> A1["注意力变体"] --> A3["MoE 混合专家"]
    T3 --> A2["KV Cache"] --> A3
    A1 --> A4["线性·混合注意力"]
    A3 --> A5["长上下文"]
    T3 --> A6["多模态"]
  end
  subgraph F5["05 预训练"]
    T3 --> P1["预训练目标"] --> P2["数据工程"] --> P3["Scaling Laws"]
    P3 --> P4["分布式训练"] --> P5["训练稳定性·Muon"]
    P4 --> P6["混合精度"]
  end
  subgraph F6["06 后训练对齐"]
    P1 --> S1["SFT"] --> S2["PEFT/LoRA"]
    S1 --> S3["RLHF"] --> S4["DPO"]
    S3 --> S5["推理RL GRPO"]
    S1 --> S6["安全对齐"]
    S1 --> S7["蒸馏"]
  end
  subgraph F7["07 推理扩展"]
    S5 --> I1["解码策略"]
    S5 --> I2["推理时扩展"] --> I3["推理模型"]
    I2 --> I4["测试时训练 TTT"]
  end
  subgraph F8["08 效率部署"]
    A3 --> E1["量化"] --> E3["部署蒸馏"]
    A2 --> E2["剪枝稀疏"] --> E4["推测解码"]
    E1 --> E5["推理引擎"] --> E6["服务化成本"]
  end
  subgraph F9["09 应用范式"]
    I1 --> Q1["Prompt 工程"] --> Q2["RAG"]
    Q2 --> Q3["Agentic RAG"]
    Q2 --> Q4["上下文工程"]
    Q2 --> Q5["工具调用·MCP"]
    Q2 --> Q6["Agent 智能体"]
    Q2 --> Q7["结构化输出"]
  end
  subgraph F10["10 评估安全"]
    Q6 --> V1["评估基准"] --> V2["评估方法"]
    Q6 --> V3["幻觉治理"]
    V3 --> V4["安全·红队"] --> V5["治理合规"]
  end
  style F0 fill:#f1f3f6,stroke:#d0d5de
  style F1 fill:#eaf3de,stroke:#639922
  style F2 fill:#eaf3de,stroke:#639922
  style F3 fill:#e6f1fb,stroke:#185fa5
  style F4 fill:#e6f1fb,stroke:#185fa5
  style F5 fill:#faeeda,stroke:#ba7517
  style F6 fill:#faeeda,stroke:#ba7517
  style F7 fill:#eeedfe,stroke:#7f77dd
  style F8 fill:#eeedfe,stroke:#7f77dd
  style F9 fill:#eeedfe,stroke:#7f77dd
  style F10 fill:#fbeaf0,stroke:#993556"""


def gen_dependency(toc):
    """核心依赖脉络图:简化版前置关系"""
    root = ""
    body = f"""        <div class="container wide">
          <div id="breadcrumb"></div>
          <div class="page-head">
            <div class="meta"><span class="level adv" style="background:var(--brand-soft);color:var(--brand-deep)">资源</span></div>
            <h1>知识依赖图</h1>
            <p class="lead">每个知识点都不是孤岛。这张图给出「先学什么、后学什么」的推荐顺序——箭头表示前置关系。</p>
          </div>
          <p class="dep-note">这是一条<strong>主干依赖脉络</strong>的简化版:真实学习可以有很多分支与回环(比如先看应用再补原理)。把它当作导航而非铁律。</p>
          <figure class="figure">
            <div class="mermaid">
{DEP_MERMAID}
            </div>
            <figcaption>从数学基础到评估安全的核心依赖流向</figcaption>
          </figure>
          <div id="pager"></div>
        </div>"""
    return page_shell("知识依赖图", root, "", "", body)


def gen_part_index(part, toc):
    """生成某一篇的目录页"""
    root = "../../"
    counts = {"basic": 0, "inter": 0, "adv": 0}
    for t in part["topics"]:
        counts[t["level"]] += 1

    items = []
    for i, t in enumerate(part["topics"], 1):
        items.append(f"""          <a class="topic-item" data-lv="{t['level']}" href="{t['id']}.html">
            <span class="ti-idx">{i:02d}</span>
            <span class="ti-main">
              <span class="ti-title">{t['title']}</span>
              <span class="ti-desc">{t.get('desc','')}</span>
            </span>
            <span class="level {t['level']}">{LEVEL_LABEL[t['level']]}</span>
            <span class="ti-arrow"><svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3.5L10.5 8L6 12.5"/></svg></span>
          </a>""")

    frontier_tag = '<span class="tag-frontier">2026 前沿</span>' if part.get("frontier") else ""
    stat = " · ".join(
        f"{LEVEL_LABEL[k]} {v}" for k, v in counts.items() if v
    )

    body = f"""        <div class="container">
          <div id="breadcrumb"></div>
          <div class="page-head">
            <div class="meta">
              <span class="level basic" style="background:var(--brand-soft);color:var(--brand-deep)">{part['num']} 篇</span>
              {frontier_tag}
            </div>
            <h1>{part['title']}</h1>
            <p class="lead">{part['desc']}</p>
          </div>

          <div class="callout">
            <span class="callout-t">本篇共 {len(part['topics'])} 个知识点</span>{stat}。左侧可按难度筛选。
          </div>

          <div class="topic-list">
{chr(10).join(items)}
          </div>

          <div id="pager"></div>
        </div>"""

    return page_shell(f"{part['num']} {part['title']}", root, part["id"], "", body)


def gen_topic_page(part, topic):
    """生成知识点占位页"""
    root = "../../"
    kws = "".join(f"<span>{k}</span>" for k in topic.get("keywords", []))
    frontier_tag = '<span class="tag-frontier">2026 前沿</span>' if topic.get("frontier") else ""

    body = f"""        <div class="container">
          <div id="breadcrumb"></div>
          <div class="page-head">
            <div class="meta">
              <span class="level {topic['level']}">{LEVEL_LABEL[topic['level']]}</span>
              {frontier_tag}
            </div>
            <h1>{topic['title']}</h1>
            <p class="lead">{topic.get('desc','')}</p>
          </div>

          <div class="overview-card">
            <div class="card-title">一图看懂</div>
            <p style="margin:0;color:var(--text-2);font-size:14px">
              本节的概览图解将在内容填充阶段补齐,用一张图建立对「{topic['title']}」的整体直觉。
            </p>
          </div>

          <h2>核心概念</h2>
          <div class="placeholder">
            <div class="ph-title">内容待填充</div>
            <div class="ph-sub">这里将展开「{topic['title']}」的核心定义、直觉解释与关键要点。</div>
            <div class="ph-kw">{kws}</div>
          </div>

          <h2>深入原理</h2>
          <details class="deep">
            <summary>展开:数学表达与推导</summary>
            <div class="deep-body">
              <p style="color:var(--text-3)">公式推导与数学表达待补充。</p>
            </div>
          </details>
          <details class="deep">
            <summary>展开:代码实现</summary>
            <div class="deep-body">
              <p style="color:var(--text-3)">最小可运行代码示例待补充。</p>
            </div>
          </details>

          <h2>要点速查</h2>
          <div class="placeholder">
            <div class="ph-title">速查表待填充</div>
            <div class="ph-sub">关键结论、对比表与常见坑位会汇总在这里。</div>
          </div>

          <div id="pager"></div>
        </div>"""

    return page_shell(topic["title"], root, part["id"], topic["id"], body)


def write(path, content):
    """写文件;若目标文件含精编标记则跳过"""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            if KEEP_MARK in f.read():
                return "skip"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "write"


def main():
    with open(TOC_JSON, "r", encoding="utf-8") as f:
        toc = json.load(f)

    stats = {"write": 0, "skip": 0}

    # 1. toc.js
    p = os.path.join(BASE, "assets", "js", "toc.js")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(gen_toc_js(toc))
    print("[toc.js] 已生成")

    # 2. search-index.js
    p = os.path.join(BASE, "assets", "js", "search-index.js")
    with open(p, "w", encoding="utf-8") as f:
        f.write(gen_search_index(toc))
    print("[search-index.js] 已生成")

    # 3. 术语表 + 依赖图
    r = write(os.path.join(BASE, "glossary.html"), gen_glossary(toc))
    stats[r] += 1
    r = write(os.path.join(BASE, "dependency.html"), gen_dependency(toc))
    stats[r] += 1
    print("[glossary.html / dependency.html] 已生成")

    # 4. 各篇目录页 + 知识点页
    for part in toc["parts"]:
        d = os.path.join(BASE, "pages", part["id"])
        r = write(os.path.join(d, "index.html"), gen_part_index(part, toc))
        stats[r] += 1
        for topic in part["topics"]:
            r = write(os.path.join(d, topic["id"] + ".html"), gen_topic_page(part, topic))
            stats[r] += 1
        print(f"  {part['num']} {part['title']}  ({len(part['topics'])} 个知识点)")

    total_topics = sum(len(p["topics"]) for p in toc["parts"])
    print(f"\n完成:{len(toc['parts'])} 篇 / {total_topics} 个知识点")
    print(f"     新写入 {stats['write']} 个文件,跳过精编页 {stats['skip']} 个")


if __name__ == "__main__":
    main()
