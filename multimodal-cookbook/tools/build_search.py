# -*- coding: utf-8 -*-
"""生成 assets/js/search-index.json（章节标题 + h2/h3 标题级搜索索引）
用法: python tools/build_search.py
"""
import re, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_manifest():
    src = open(os.path.join(ROOT, "assets", "js", "manifest.js"), encoding="utf-8").read()
    out = []
    for cm in re.finditer(r'no:\s*"([^"]+)",\s*path:\s*"([^"]+)",\s*title:\s*"([^"]+)"', src):
        out.append((cm.group(1), cm.group(2), cm.group(3)))
    return out

def main():
    index = []
    for no, path, title in load_manifest():
        p = os.path.join(ROOT, "chapters", path)
        if not os.path.exists(p):
            continue
        html = open(p, encoding="utf-8").read()
        pth = "chapters/" + path if not path.startswith("http") else path
        chap = f"第 {no} 章 {title}"
        entries = [{"p": pth, "t": title, "h": "", "c": chap, "k": chap}]
        for hm in re.finditer(r'<h([23])[^>]*id="[^"]*"[^>]*>(.*?)</h\1>', html, re.S):
            txt = re.sub(r'<[^>]+>', '', hm.group(2))
            txt = re.sub(r'\s+', ' ', txt).strip()
            if txt:
                entries.append({"p": pth + "#" , "t": title, "h": txt, "c": chap, "k": txt})
        index.extend(entries)
    out = os.path.join(ROOT, "assets", "js", "search-index.json")
    json.dump(index, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"search-index.json: {len(index)} entries from {len(load_manifest())} chapters")

if __name__ == "__main__":
    main()
