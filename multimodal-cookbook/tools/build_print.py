# -*- coding: utf-8 -*-
"""把全部章节合并为 print.html（用于打印/导出 PDF 统计页数）
用法: python tools/build_print.py
"""
import re, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "assets", "js", "manifest.js")
OUT = os.path.join(ROOT, "print.html")

def load_manifest():
    src = open(MANIFEST, encoding="utf-8").read()
    parts = []
    for pm in re.finditer(r'name:\s*"([^"]+)",\s*chapters:\s*\[(.*?)\]\}', src, re.S):
        pname, body = pm.group(1), pm.group(2)
        chs = []
        for cm in re.finditer(r'no:\s*"([^"]+)",\s*path:\s*"([^"]+)",\s*title:\s*"([^"]+)"', body):
            chs.append({"no": cm.group(1), "path": cm.group(2), "title": cm.group(3)})
        parts.append({"name": pname, "chapters": chs})
    return parts

def clean_chapter(html):
    # 去掉脚本、侧边栏、顶栏、返回顶部、上/下章导航（book.js 注入的为空壳）
    html = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.S)
    html = re.sub(r'<nav id="sidebar">.*?</nav>', '', html, flags=re.S)
    html = re.sub(r'<header id="topbar">.*?</header>', '', html, flags=re.S)
    html = re.sub(r'<button id="backtop">.*?</button>', '', html, flags=re.S)
    html = re.sub(r'<div id="progress-bar"></div>', '', html)
    html = html.replace('href="../assets/', 'href="assets/')
    html = html.replace('src="../assets/', 'src="assets/')
    m = re.search(r'<main class="content">(.*)</main>', html, re.S)
    body = m.group(1) if m else html
    return body

def main():
    parts = load_manifest()
    pages_css = """<style>
@page { size: A4; margin: 20mm 18mm; }
body { margin:0; font-family: -apple-system, "Segoe UI", "Noto Sans SC", "Microsoft YaHei", sans-serif; font-size: 15px; line-height: 1.75; color: #1e293b; }
.chapter { padding: 0 20px; max-width: 960px; margin: 0 auto; page-break-before: always; }
.chapter h1 { page-break-before: always; margin-top: 30px; margin-bottom: 20px; }
h2 { page-break-before: auto; margin-top: 28px; margin-bottom: 16px; }
.part-divider { page-break-before: always; page-break-after: always; height: 90vh; display: flex; flex-direction: column;
  justify-content: center; align-items: center; background: #1e3a8a; color: #fff; text-align: center; }
.part-divider h2 { font-size: 38px; border: none; color: #fff; margin: 0; }
pre, code { white-space: pre-wrap; word-break: break-all; font-size: 13.5px; line-height: 1.6; }
.box-tip, .box-warn, .box-paper, .box-theory, .box-recipe, .box-quiz, .box-history { page-break-inside: avoid; margin: 20px 0; padding: 18px 22px; }
table { page-break-inside: auto; margin: 20px 0; font-size: 14px; }
tr { page-break-inside: avoid; page-break-after: auto; }
p { margin-bottom: 14px; }
</style>"""
    doc = ["""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<title>多模态大模型 Cookbook · 合订打印版</title>
<link rel="stylesheet" href="assets/css/style.css">""" + pages_css + """
<script>window.MathJax={tex:{inlineMath:[["$","$"],["\\\\(","\\\\)"]],displayMath:[["$$","$$"],["\\\\[","\\\\]"]]},svg:{fontCache:"global"}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
</head><body>
<section class="chapter"><header class="book-header">
<div class="part-badge">Multimodal LLM Cookbook</div>
<h1 class="chapter-title">多模态大模型 Cookbook<br>从入门到精通 · 理论 · 实战 · 前沿</h1>
<div class="chapter-meta"><span>合订打印版 · 55 章</span><span>知识截止 2026-09</span></div>
</header></section>"""]
    total, missing = 0, []
    for pi, part in enumerate(parts):
        doc.append(f'<div class="part-divider"><h2>{part["name"]}</h2></div>')
        for ch in part["chapters"]:
            p = os.path.join(ROOT, "chapters", ch["path"])
            if not os.path.exists(p):
                missing.append(ch["path"]); continue
            html = open(p, encoding="utf-8").read()
            doc.append(f'<section class="chapter" id="ch{ch["no"]}">' + clean_chapter(html) + '</section>')
            total += 1
    doc.append("</body></html>")
    open(OUT, "w", encoding="utf-8").write("\n".join(doc))
    print(f"print.html written: {total} chapters ({len(missing)} missing: {missing})")

if __name__ == "__main__":
    main()
