# -*- coding: utf-8 -*-
"""v2 战役附加检查：论文/权威原图数、深入块数、外链数、图片引用有效性。

用法:
  python tools/check_v2.py pages/07-posttraining/dpo.html
  python tools/check_v2.py 07-posttraining
  python tools/check_v2.py all

检查项:
  - paper-figure 论文原图数量 >= 1
  - details.deep 深入块 >= 2
  - https 外链 >= 5
  - 本地图片引用（assets/...）文件存在性
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, 'pages')

REQ = dict(paper=1, deep=2, refs=5)


def analyze(path):
    html = open(path, encoding='utf-8', errors='ignore').read()
    d = dict(
        paper=len(re.findall(r'class="paper-figure"', html)),
        deep=len(re.findall(r'class="deep"', html)),
        refs=len(re.findall(r'href="https?://', html)),
        img_bad=[],
    )
    # 本地图片引用检查
    for m in re.finditer(r'<img[^>]+src="([^"]+)"', html):
        src = m.group(1)
        if src.startswith(('http', 'data:')):
            continue
        rel = src.lstrip('./').replace('/', os.sep)
        # 页面位于 pages/<part>/xxx.html，相对 src 基于页面目录
        page_dir = os.path.dirname(path)
        abs_p = os.path.normpath(os.path.join(page_dir, src))
        if not os.path.exists(abs_p):
            d['img_bad'].append(src)
    return d


def resolve(arg):
    if arg == 'all':
        return sorted(glob.glob(PAGES + '/**/*.html', recursive=True))
    p = arg if os.path.isabs(arg) else os.path.join(ROOT, arg)
    if os.path.isfile(p):
        return [p]
    d = os.path.join(PAGES, arg)
    if os.path.isdir(d):
        return sorted(glob.glob(d + '/*.html'))
    return []


def main():
    args = sys.argv[1:] or ['all']
    files = []
    for a in args:
        files += resolve(a)
    files = [f for f in files if not f.replace('\\', '/').endswith('/index.html')]
    if not files:
        print('no files matched:', args)
        return
    okc = 0
    for f in files:
        d = analyze(f)
        bad = [k for k in REQ if d[k] < REQ[k]]
        bad += [f'死图:{x}' for x in d['img_bad']]
        name = f.replace('\\', '/').replace(ROOT.replace('\\', '/') + '/', '')
        if bad:
            print(f'GAP {name}: 论文图={d["paper"]} 深入块={d["deep"]} 外链={d["refs"]} -> 缺 {" ".join(bad)}')
        else:
            print(f'OK  {name}: 论文图={d["paper"]} 深入块={d["deep"]} 外链={d["refs"]}')
            okc += 1
    print(f'\n达标 {okc}/{len(files)}')


if __name__ == '__main__':
    main()
