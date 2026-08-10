#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_paper_figs.py — 从 ar5iv 抓取 arXiv 论文原图（Figure）到本地资产目录。

用法:
  python tools/fetch_paper_figs.py <arxiv-id> <输出目录> [--filter 关键词] [--list-only] [--all]

示例:
  python tools/fetch_paper_figs.py 2201.11903 assets/figures/08-inference --filter "Chain-of-Thought"
  python tools/fetch_paper_figs.py 2005.11401 assets/figures/10-applications --list-only
  python tools/fetch_paper_figs.py 2205.14135 assets/figures/05-systems --all

行为:
  - 默认: 解析 ar5iv HTML，列出所有 figure（img + caption），按 --filter 匹配 caption 下载（不区分大小写）
  - --list-only: 只列出图清单，不下载
  - --all: 下载全部 figure（跳过明显的公式图 x1.png 等）
  - 输出文件命名: <输出目录>/fig<N>.png，同时打印每张图的 caption 与建议引用格式
"""
import argparse
import os
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def parse(html: str):
    """返回 [(img_abs_url, caption_text), ...]"""
    out = []
    # 提取 arxiv id 用于拼接绝对路径
    m = re.search(r'https?://ar5iv\.labs\.arxiv\.org/html/([\d.]+v?\d*)', html)
    if not m:
        m = re.search(r'href="https?://arxiv\.org/abs/([\d.]+v?\d*)"', html)
    arx = m.group(1) if m else None
    figs = re.findall(r'<figure[^>]*>(.*?)</figure>', html, re.S)
    for f in figs:
        im = re.search(r'<img[^>]+src="([^"]+\.(?:png|jpg|jpeg|svg))"', f)
        if not im:
            continue
        src = im.group(1)
        if src.startswith('data:'):
            continue
        if src.startswith('/html/'):
            abs_url = 'https://ar5iv.labs.arxiv.org' + src
        elif src.startswith('http'):
            abs_url = src
        else:
            abs_url = 'https://ar5iv.labs.arxiv.org/html/' + (arx or '') + '/' + src.lstrip('/')
        cap = re.sub(r'<[^>]+>', ' ', f)
        cap = re.sub(r'\s+', ' ', cap).strip()
        out.append((abs_url, cap))
    return out, arx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('arxiv_id', help='arXiv 编号，如 1706.03762')
    ap.add_argument('outdir', help='输出目录，如 assets/figures/03-transformer')
    ap.add_argument('--filter', default='', help='按 caption 关键词过滤（不区分大小写）')
    ap.add_argument('--list-only', action='store_true', help='只列出图清单')
    ap.add_argument('--all', action='store_true', help='下载全部非公式图')
    args = ap.parse_args()

    url = f'https://ar5iv.labs.arxiv.org/html/{args.arxiv_id}'
    print(f'[1/2] 拉取 {url} ...')
    try:
        html = fetch(url).decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'!! 拉取失败: {e}', file=sys.stderr)
        sys.exit(1)

    figs, arx = parse(html)
    print(f'      解析到 {len(figs)} 张图 (arxiv={arx})')
    if args.filter:
        figs = [(u, c) for u, c in figs if args.filter.lower() in c.lower()]
        print(f'      过滤 [{args.filter}] 后 {len(figs)} 张')

    for i, (u, c) in enumerate(figs, 1):
        short = c[:110].replace('\n', ' ')
        print(f'  [{i}] {u.split("/")[-1]}')
        print(f'      caption: {short}')

    if args.list_only:
        return

    os.makedirs(args.outdir, exist_ok=True)
    print(f'[2/2] 下载到 {args.outdir}/ ...')
    n = 0
    for i, (u, c) in enumerate(figs, 1):
        fn = f'fig{i}.png' if not u.endswith('.svg') else f'fig{i}.svg'
        dest = os.path.join(args.outdir, fn)
        try:
            data = fetch(u)
            with open(dest, 'wb') as f:
                f.write(data)
            print(f'  ✓ {fn} ({len(data)} bytes)  caption: {c[:80]}...')
            n += 1
        except Exception as e:
            print(f'  ✗ {fn} 下载失败: {e}', file=sys.stderr)
    print(f'完成，共下载 {n} 张图。引用格式示例:')
    print('  <figure class="paper-figure">')
    print(f'    <img src="../../{args.outdir}/fig1.png" alt="..." loading="lazy">')
    print('    <figcaption><span class="pf-title">图：...</span>')
    print(f'      <span class="pf-src">论文原图 · 作者, <em>标题</em>, 年份, Figure N · <a href="https://arxiv.org/abs/{args.arxiv_id}" target="_blank" rel="noopener">arXiv:{args.arxiv_id}</a></span>')
    print('    </figcaption></figure>')


if __name__ == '__main__':
    main()
