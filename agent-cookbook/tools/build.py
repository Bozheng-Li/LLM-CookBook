# -*- coding: utf-8 -*-
"""build.py — 全书构建: 侧栏注入 / 目录生成 / 搜索索引 / 单页打印版 / 统计.
支持自动根据页面层级（根目录 index.html vs chapters/*.html）计算正确的相对路径前缀，杜绝 404 死链！
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOC = json.load(open(os.path.join(ROOT, "tools", "toc.json"), encoding="utf-8"))
CH_DIR = os.path.join(ROOT, "chapters")


def esc(s):
    return html.escape(s, quote=False)


def all_chapters():
    out = []
    for p in TOC["parts"]:
        for ch in p["chapters"]:
            out.append((p, ch))
    return out


def sidebar_html(is_in_chapters=False):
    """
    is_in_chapters=False 时（针对 index.html）：链接为 chapters/ch001.html
    is_in_chapters=True 时（针对 chapters/*.html）：链接为 ch001.html
    """
    prefix = "" if is_in_chapters else "chapters/"
    parts_html = []
    for p in TOC["parts"]:
        items = "".join(
            f'<a href="{prefix}{c["file"]}"><span class="cn">{c["id"]:03d}</span>{esc(c["title"])}</a>'
            for c in p["chapters"])
        parts_html.append(
            f'<div class="toc-part"><div class="toc-part-head"><span class="num">{p["num"]}</span>'
            f'{esc(p["title"])}<span class="chev">▶</span></div>'
            f'<div class="toc-part-body">{items}</div></div>')
    return "".join(parts_html)


SIDEBAR_ROOT = sidebar_html(is_in_chapters=False)
SIDEBAR_CHAPTERS = sidebar_html(is_in_chapters=True)


def inject_sidebar(path, is_in_chapters=False):
    raw = open(path, encoding="utf-8").read()
    sidebar_content = SIDEBAR_CHAPTERS if is_in_chapters else SIDEBAR_ROOT
    
    # 替换已有侧边栏内容或标记
    if "<!--SIDEBAR-->" in raw:
        raw = raw.replace("<!--SIDEBAR-->", sidebar_content)
        open(path, "w", encoding="utf-8").write(raw)
        return True
    elif '<div class="toc-part">' in raw:
        # 已注入过侧边栏，更新全部 toc-part
        raw = re.sub(r'<div class="toc-part">[\s\S]*?<div class="sidebar-foot">',
                     sidebar_content + '\n  <div class="sidebar-foot">', raw, count=1)
        open(path, "w", encoding="utf-8").write(raw)
        return True
    return False


def chapter_nav(entries, idx):
    prev_e = entries[idx - 1] if idx > 0 else None
    next_e = entries[idx + 1] if idx < len(entries) - 1 else None
    def a(e, cls, label):
        t = e["title"]
        return f'<a class="{cls}" href="{e["file"]}"><span class="dir">{label}</span><span class="t">{esc(t)}</span></a>'
    prev = a(prev_e, "prev", "← 上一章") if prev_e else '<a class="prev" href="../index.html"><span class="dir">← </span><span class="t">返回首页</span></a>'
    nxt = a(next_e, "next", "下一章 →") if next_e else '<a class="next" href="../index.html"><span class="dir">→ </span><span class="t">返回首页</span></a>'
    return f'<nav class="chapter-nav">{prev}{nxt}</nav>'


def inject_nav(path, entries, idx):
    raw = open(path, encoding="utf-8").read()
    new_nav = chapter_nav(entries, idx)
    if '<nav class="chapter-nav">' in raw:
        raw = re.sub(r'<nav class="chapter-nav">[\s\S]*?</nav>', new_nav, raw, count=1)
    else:
        raw = raw.replace("</main>", new_nav + "\n</main>")
    open(path, "w", encoding="utf-8").write(raw)


def strip_tags(s):
    s = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", s)
    return re.sub(r"<[^>]+>", " ", s)


def build_search_index():
    idx = []
    for p, ch in all_chapters():
        fp = os.path.join(CH_DIR, ch["file"])
        if not os.path.exists(fp):
            continue
        raw = open(fp, encoding="utf-8").read()
        body = strip_tags(raw)
        body = re.sub(r"\s+", " ", body)
        idx.append({"file": ch["file"],
                    "title": f'第{ch["id"]}章 · {ch["title"]}',
                    "body": body[:2600]})
    for a in TOC["appendices"]:
        fp = os.path.join(CH_DIR, a["file"])
        if not os.path.exists(fp):
            continue
        raw = open(fp, encoding="utf-8").read()
        body = re.sub(r"\s+", " ", strip_tags(raw))
        idx.append({"file": a["file"], "title": a["title"], "body": body[:2600]})
    with open(os.path.join(ROOT, "assets", "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False)
    print(f"search-index.json: {len(idx)} entries, {os.path.getsize(os.path.join(ROOT,'assets','search-index.json'))//1024}KB")


def build_index_toc():
    fp = os.path.join(ROOT, "index.html")
    raw = open(fp, encoding="utf-8").read()
    cards = []
    for p in TOC["parts"]:
        items = "".join(
            f'<li><a href="chapters/{c["file"]}"><span class="cn">{c["id"]:03d}</span>{esc(c["title"])}</a></li>'
            for c in p["chapters"])
        cards.append(
            f'<div class="pt-card" id="part-{p["num"]}"><div class="pt-head"><span class="pt-num">{p["num"]}</span>'
            f'<h3>{p["icon"]} {esc(p["title"])}</h3></div>'
            f'<p class="pt-blurb">{esc(p["blurb"])}</p><ul>{items}</ul></div>')
    if '<div class="part-toc">' in raw:
        raw = re.sub(r'<div class="part-toc">[\s\S]*?</div>\s*<!--/TOC-GRID-->',
                     '<div class="part-toc">' + "".join(cards) + "</div>\n<!--/TOC-GRID-->", raw, count=1)
    elif "<!--TOC-GRID-->" in raw:
        raw = raw.replace("<!--TOC-GRID-->", '<div class="part-toc">' + "".join(cards) + "</div>\n<!--/TOC-GRID-->")
    open(fp, "w", encoding="utf-8").write(raw)
    print("index.html TOC injected")


def build_print():
    entries = all_chapters()
    body_parts = []
    # cover
    body_parts.append("""<section style="text-align:center;padding:220px 0 160px">
<h1 style="font-size:44px;margin:0">AI Agent Cookbook</h1>
<p style="font-size:20px;color:#666">从入门到精通的智能体全景手册</p>
<p style="color:#999">架构 · 机制 · 训练与强化 · 工程实战 · 论文与项目全景<br>CC BY-SA 4.0 · 开源书籍 · v1.0</p>
</section>""")
    body_parts.append("<h1 style='page-break-before:always'>目录</h1><ol style='font-size:13px;line-height:2'>")
    for p, ch in entries:
        body_parts.append(f'<li><b>第{p["num"]}部分 {esc(p["title"])}</b> — 第{ch["id"]}章 {esc(ch["title"])}</li>')
    body_parts.append("</ol>")
    for p, ch in entries:
        fp = os.path.join(CH_DIR, ch["file"])
        if not os.path.exists(fp):
            continue
        raw = open(fp, encoding="utf-8").read()
        m = re.search(r'<div class="content">([\s\S]*?)</main>', raw)
        inner = m.group(1) if m else ""
        inner = inner.replace('src="../assets/', 'src="assets/')
        inner = inner.replace('href="../assets/', 'href="assets/')
        inner = inner.replace('href="../index.html', 'href="index.html')
        # 将同级章节链接 chXXX.html 转换为 chapters/chXXX.html
        inner = re.sub(r'href="(ch\d{3}\.html|app[a-d]\.html)', r'href="chapters/\g<1>', inner)
        body_parts.append(f'<section style="page-break-before:always">{inner}</section>')
    for a in TOC["appendices"]:
        fp = os.path.join(CH_DIR, a["file"])
        if not os.path.exists(fp):
            continue
        raw = open(fp, encoding="utf-8").read()
        m = re.search(r'<div class="content">([\s\S]*?)</main>', raw)
        inner = (m.group(1) if m else "").replace('src="../assets/', 'src="assets/').replace('href="../assets/', 'href="assets/').replace('href="../index.html', 'href="index.html')
        inner = re.sub(r'href="(ch\d{3}\.html|app[a-d]\.html)', r'href="chapters/\g<1>', inner)
        body_parts.append(f'<section style="page-break-before:always">{inner}</section>')
    page = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<title>AI Agent Cookbook · 打印版</title><link rel="stylesheet" href="assets/css/style.css">
<style>@page {{ size: A4; margin: 16mm 14mm; }} .chapter-nav{{display:none}}</style></head>
<body><div class="main" style="margin:0"><div class="content" style="max-width:100%">{''.join(body_parts)}</div></div></body></html>"""
    out = os.path.join(ROOT, "print.html")
    open(out, "w", encoding="utf-8").write(page)
    print(f"print.html: {os.path.getsize(out)//1024}KB")


def stats():
    entries = all_chapters()
    n_ch = 0; n_fig = 0; n_code = 0; n_tbl = 0; n_words = 0; n_refs = 0
    figs_dir = os.path.join(ROOT, "assets", "figures")
    n_svg = len([f for f in os.listdir(figs_dir) if f.endswith(".svg")])
    for p, ch in entries:
        fp = os.path.join(CH_DIR, ch["file"])
        if not os.path.exists(fp):
            continue
        n_ch += 1
        raw = open(fp, encoding="utf-8").read()
        n_fig += len(re.findall(r'<figure class="figure"', raw))
        n_code += len(re.findall(r'class="codeblock"', raw))
        n_tbl += len(re.findall(r"<table", raw))
        n_refs += len(re.findall(r"arxiv\.org/(?:abs|pdf)/", raw))
        n_words += len(re.findall(r"[\u4e00-\u9fff]", strip_tags(raw)))
    n_app = sum(1 for a in TOC["appendices"] if os.path.exists(os.path.join(CH_DIR, a["file"])))
    return {"chapters": n_ch, "appendices": n_app, "figs": n_svg, "inline_figs": n_fig,
            "code": n_code, "tables": n_tbl, "cjk": n_words, "arxiv_refs": n_refs}


def inject_stats():
    s = stats()
    pages_est = int(s["cjk"] / 1050 + s["inline_figs"] * 0.45 + s["code"] * 0.35 + s["tables"] * 0.35)
    block = f"""<div class="stats-band">
<div class="stat"><div class="n">{s['chapters']}+{s['appendices']}</div><div class="l">章节数(正章+附录)</div></div>
<div class="stat"><div class="n">{s['cjk']//10000}万+</div><div class="l">汉字正文</div></div>
<div class="stat"><div class="n">{s['figs']}</div><div class="l">原创图表</div></div>
<div class="stat"><div class="n">{s['code']}</div><div class="l">代码示例</div></div>
<div class="stat"><div class="n">{s['arxiv_refs']}</div><div class="l">arXiv 引用</div></div>
<div class="stat"><div class="n">≈{pages_est}</div><div class="l">A4 打印页数</div></div>
</div>"""
    fp = os.path.join(ROOT, "index.html")
    raw = open(fp, encoding="utf-8").read()
    raw = re.sub(r"<!--STATS-->[\s\S]*?</div>\n\n    <section", block + "\n\n    <section", raw, count=1) \
        if "<!--STATS--><" not in raw else raw.replace("<!--STATS-->", block)
    if "<!--STATS-->" in raw:
        raw = raw.replace("<!--STATS-->", block)
    open(fp, "w", encoding="utf-8").write(raw)
    print("stats injected:", s, "est pages:", pages_est)
    return pages_est


def main():
    entries = all_chapters()
    n_inj = 0
    idx_fp = os.path.join(ROOT, "index.html")
    if os.path.exists(idx_fp) and inject_sidebar(idx_fp, is_in_chapters=False):
        n_inj += 1
    for i, (p, ch) in enumerate(entries):
        fp = os.path.join(CH_DIR, ch["file"])
        if os.path.exists(fp):
            if inject_sidebar(fp, is_in_chapters=True):
                n_inj += 1
            inject_nav(fp, [e for _, e in entries], i)
    for a in TOC["appendices"]:
        fp = os.path.join(CH_DIR, a["file"])
        if os.path.exists(fp):
            if inject_sidebar(fp, is_in_chapters=True):
                n_inj += 1
    print(f"sidebar injected into {n_inj} files")
    build_index_toc()
    pages = inject_stats()
    build_search_index()
    build_print()
    print("BUILD OK, est pages =", pages)


if __name__ == "__main__":
    main()
