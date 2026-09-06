# -*- coding: utf-8 -*-
"""check_chapter.py — 章节硬性质量闸门.
用法: python tools/check_chapter.py chapters/ch016.html [更多文件...] | --all
退出码: 0=全部通过, 1=存在失败
"""
import re, sys, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOC = json.load(open(os.path.join(ROOT, "tools", "toc.json"), encoding="utf-8"))
ALL_FILES = {}
for p in TOC["parts"]:
    for ch in p["chapters"]:
        ALL_FILES[ch["file"]] = (p, ch)
for a in TOC["appendices"]:
    ALL_FILES[a["file"]] = (None, a)


def strip_tags(html):
    html = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", html)
    return re.sub(r"<[^>]+>", " ", html)


def check(path):
    issues, warns = [], []
    name = os.path.basename(path)
    if not os.path.exists(path):
        return [f"文件不存在: {path}"], []
    raw = open(path, encoding="utf-8").read()
    size = len(raw.encode("utf-8"))
    is_appendix = name.startswith("app")
    min_size, min_cjk = (20000, 3000) if is_appendix else (30000, 6000)
    if size < min_size:
        issues.append(f"体积 {size//1024}KB < {min_size//1024}KB 下限")
    cjk = len(re.findall(r"[\u4e00-\u9fff]", strip_tags(raw)))
    if cjk < min_cjk:
        issues.append(f"汉字数 {cjk} < {min_cjk}")
    for need, msg in [
        ('charset="UTF-8"', "缺少 UTF-8 声明"),
        ('assets/css/style.css', "未引入样式表"),
        ('assets/js/app.js', "未引入脚本"),
        ('class="chapter-header"', "缺少 chapter-header"),
        ('class="lead"', "缺少 lead 导语"),
        ('class="refs"', "缺少参考文献区"),
        ('class="chapter-nav"', "缺少上下章导航"),
        ('<figure class="figure"', "缺少插图 figure"),
        ('<div class="tbl-wrap">', "缺少表格 tbl-wrap"),
        ('class="callout', "缺少提示块 callout"),
    ]:
        if need not in raw:
            issues.append(msg)
    is_appendix = name.startswith("app")
    if not is_appendix and 'class="codeblock"' not in raw:
        issues.append("缺少代码块")
    if "<h1>" not in raw and 'h1">' not in raw:
        issues.append("缺少 h1")
    h2s = re.findall(r'<h2(?:\s+id="([^"]*)")?', raw)
    if len(h2s) < 5:
        issues.append(f"h2 数量 {len(h2s)} < 5")
    ids = [i for i in h2s if i]
    if len(ids) < len(h2s):
        warns.append("部分 h2 缺少 id")
    if len(ids) != len(set(ids)):
        issues.append("h2 id 重复")
    # images exist
    for m in re.finditer(r'src="([^"]+)"', raw):
        src = m.group(1)
        if src.startswith(("http", "data:")):
            continue
        p = os.path.normpath(os.path.join(os.path.dirname(path), src))
        if not os.path.exists(p):
            issues.append(f"图片不存在: {src}")
    # internal links exist (targets planned in TOC but not yet written -> warning)
    for m in re.finditer(r'href="([^"#]+\.html)', raw):
        href = m.group(1)
        if href.startswith("http"):
            continue
        base = os.path.basename(href)
        cand = [os.path.normpath(os.path.join(os.path.dirname(path), href)),
                os.path.normpath(os.path.join(ROOT, href))]
        if not any(os.path.exists(c) for c in cand):
            if base in ALL_FILES:
                warns.append(f"目标章节尚未创建: {base}")
            else:
                issues.append(f"站内链接无效: {href}")
    # placeholders
    for pat, fl in [(r"TODO", 0), (r"FIXME", 0), (r"占位符", re.I), (r"lorem ipsum", re.I), (r"待补充", 0), (r"待撰写", 0), (r"待完成", 0)]:
        if re.search(pat, raw, fl):
            issues.append(f"存在占位内容: {pat}")
    # unescaped < inside code blocks
    for m in re.finditer(r"<pre><code>([\s\S]*?)</code></pre>", raw):
        code = m.group(1)
        if re.search(r"<(div|span|p |a |img|table|pre|h\d)", code):
            issues.append("代码块内有未转义的 HTML 标签")
            break
    # refs count
    refs = re.search(r'<h2[^>]*id="refs"[\s\S]*$', raw)
    if refs:
        n = len(re.findall(r"<li>", refs.group(0)))
        if n < 4:
            issues.append(f"参考文献 {n} 条 < 4")
        if "arxiv.org" not in refs.group(0) and "github.com" not in refs.group(0):
            warns.append("参考文献缺少 arXiv/GitHub 链接")
    else:
        issues.append('缺少 id="refs" 的参考文献标题')
    if "本章小结" not in raw:
        issues.append("缺少本章小结")
    if "自测" not in raw:
        issues.append("缺少自测题")
    # figure caption numbering
    if re.search(r'fig-no">图', raw) is None:
        warns.append("图题缺少 fig-no 编号")
    return issues, warns


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    if args == ["--all"]:
        files = [os.path.join(ROOT, "chapters", f) for f in sorted(ALL_FILES.keys())]
    else:
        files = [a if os.path.isabs(a) else os.path.join(ROOT, a) for a in args]
    total_bad = 0
    for fp in files:
        issues, warns = check(fp)
        tag = "PASS" if not issues else "FAIL"
        print(f"[{tag}] {os.path.basename(fp)}  ({os.path.getsize(fp)//1024}KB)" if os.path.exists(fp)
              else f"[FAIL] {fp}")
        for i in issues:
            print(f"   ✗ {i}")
        for w in warns:
            print(f"   ⚠ {w}")
        total_bad += bool(issues)
    print(f"\n=== {len(files) - total_bad}/{len(files)} 通过 ===")
    sys.exit(1 if total_bad else 0)


if __name__ == "__main__":
    main()
