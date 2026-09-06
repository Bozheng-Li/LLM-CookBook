# -*- coding: utf-8 -*-
"""全书链接与结构完整性检查
用法: python tools/check_links.py
"""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")

def main():
    chapters = sorted(f for f in os.listdir(CH) if f.endswith(".html"))
    problems = []
    for f in chapters:
        html = open(os.path.join(CH, f), encoding="utf-8").read()
        # 内部锚点
        ids = set(re.findall(r'\bid="([^"]+)"', html))
        for href in re.findall(r'href="#([^"]+)"', html):
            if href and href not in ids:
                problems.append(f"{f}: 死锚点 #{href}")
        # 章间链接
        for href in re.findall(r'href="(ch[0-9][^"#]*)', html):
            if not os.path.exists(os.path.join(CH, href)):
                problems.append(f"{f}: 死链 chapters/{href}")
        # 图片
        for src in re.findall(r'<img[^>]*\ssrc="([^"]+)"', html):
            if src.startswith("http"): continue
            if not os.path.exists(os.path.join(CH, src)):
                problems.append(f"{f}: 缺图片 {src}")
        # 重复 id
        idlist = re.findall(r'\bid="([^"]+)"', html)
        dup = {i for i in idlist if idlist.count(i) > 1}
        if dup: problems.append(f"{f}: 重复id {sorted(dup)[:3]}")
        # h1 数量
        if html.count("<h1") != 1:
            problems.append(f"{f}: h1 数量={html.count('<h1')}")
    print(f"检查 {len(chapters)} 章，发现问题 {len(problems)} 个")
    for p in problems[:60]: print(" -", p)
    return problems

if __name__ == "__main__":
    main()
