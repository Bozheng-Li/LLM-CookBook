# -*- coding: utf-8 -*-
"""章节质量校验工具
用法: python tools/check_html.py chapters/ch01-xxx.html [最低可见字符数]
检查: 必需结构标记 / 可见文本字符数 / 重复 id / 未闭合标签近似检查 / 图片引用有效性
"""
import sys, re, os, json

def visible_text(html):
    html = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.S)
    html = re.sub(r'<style\b.*?</style>', ' ', html, flags=re.S)
    html = re.sub(r'<[^>]+>', ' ', html)
    html = html.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
    return re.sub(r'\s+', ' ', html)

def main():
    path = sys.argv[1]
    min_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 18000
    errs, warns = [], []
    if not os.path.exists(path):
        print(f"FAIL 文件不存在: {path}"); sys.exit(1)
    html = open(path, encoding="utf-8").read()
    vchars = len(visible_text(html))

    # 必需结构
    required = {
        "lang=zh-CN": '<html lang="zh-CN"',
        "样式表": '../assets/css/style.css',
        "侧边栏": 'id="sidebar"',
        "章节头部": 'class="book-header"',
        "上一章导航": 'class="pager"',
        "参考文献": 'class="refs"',
        "manifest": 'manifest.js',
        "book.js": 'book.js',
    }
    for name, pat in required.items():
        if pat not in html: errs.append(f"缺少必需元素: {name}")
    for box in ["box-theory", "box-paper", "box-recipe"]:
        if box not in html: warns.append(f"建议包含专栏: {box}")
    if "自测" not in html: warns.append("建议包含自测题(quiz)")
    if html.count("<h2") < 6: warns.append(f"h2 章节数偏少({html.count('<h2')})")

    # 重复 id
    ids = re.findall(r'\bid="([^"]+)"', html)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: errs.append(f"重复 id: {sorted(dup)[:5]}")

    # 标签配平近似
    for tag in ["div", "table", "figure", "section", "main", "ul", "ol", "pre"]:
        o = len(re.findall(fr'<{tag}[\s>]', html)); c = len(re.findall(fr'</{tag}>', html))
        if o != c: errs.append(f"标签不配平 <{tag}>: 开{o} 闭{c}")

    # 图片引用检查
    root = os.path.dirname(os.path.dirname(os.path.abspath(path)))
    for m in re.findall(r'<img[^>]*\ssrc="([^"]+)"', html):
        if m.startswith("http"): continue
        p = os.path.join(root, "chapters", m)
        if not os.path.exists(p): errs.append(f"图片不存在: {m}")

    # MathJax
    if "mathjax" not in html.lower(): warns.append("未引入 MathJax（含公式章节需要）")

    status = "PASS" if not errs and vchars >= min_chars else "FAIL"
    print(f"{status} {os.path.basename(path)} 可见字符={vchars} (要求≥{min_chars})")
    for e in errs: print(f"  [ERROR] {e}")
    for w in warns: print(f"  [warn] {w}")
    sys.exit(0 if status == "PASS" else 2)

if __name__ == "__main__":
    main()
