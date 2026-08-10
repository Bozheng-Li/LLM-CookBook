#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_figs_all.py — 按 tools/fig-map.json 批量下载论文原图。

用法:
  python tools/fetch_figs_all.py            # 下载全部 status=todo 的图
  python tools/fetch_figs_all.py --part 03-transformer   # 只下某篇
  python tools/fetch_figs_all.py --list-only             # 只列出要下载的计划

输出:
  - 图片保存到 assets/figures/<part>/<topic>/fig<N>.png（沿用 fetch_paper_figs 约定）
  - 每页生成 assets/figures/<part>/<topic>/manifest.json：记录 文件->论文信息+caption
  - 控制台打印每张图的 caption 与建议引用格式
"""
import argparse
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read()


def parse_ar5iv(html: str):
    """ar5iv 解析：返回 [(abs_url, caption), ...]"""
    out = []
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
    return out


def parse_arxiv_html(html: str, arx_id: str):
    """arXiv 官方 HTML 解析：img src 形如 x1.png，需拼 https://arxiv.org/html/<id>/<file>"""
    out = []
    figs = re.findall(r'<figure[^>]*>(.*?)</figure>', html, re.S)
    for f in figs:
        im = re.search(r'<img[^>]+src="([^"]+\.(?:png|jpg|jpeg|svg))"', f)
        if not im:
            continue
        src = im.group(1)
        if src.startswith('data:'):
            continue
        if src.startswith('http'):
            abs_url = src
        else:
            fn = src.split('/')[-1]
            abs_url = f'https://arxiv.org/html/{arx_id}/{fn}'
        cap = re.sub(r'<[^>]+>', ' ', f)
        cap = re.sub(r'\s+', ' ', cap).strip()
        out.append((abs_url, cap))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', default='')
    ap.add_argument('--list-only', action='store_true')
    args = ap.parse_args()

    mapping = json.load(open(os.path.join(ROOT, 'tools', 'fig-map.json'), encoding='utf-8'))
    plan = []
    for part, topics in mapping.items():
        if part.startswith('_') or not isinstance(topics, dict):
            continue
        if args.part and part != args.part:
            continue
        for topic, info in topics.items():
            if info.get('status') != 'todo':
                continue
            for i, fig in enumerate(info.get('figs', []), 1):
                plan.append({
                    'part': part, 'topic': topic, 'info': info, 'fig': fig, 'idx': i
                })

    print(f'计划下载 {len(plan)} 张图\n')
    if args.list_only:
        for p in plan:
            print(f"  {p['part']}/{p['topic']} fig{p['fig']['n']} <- {p['info']['paper']} [{p['fig'].get('filter','')}] :: {p['fig']['use']}")
        return

    ok = fail = 0
    # 按 paper 分组，每篇只抓一次 HTML
    by_paper = {}
    for p in plan:
        key = (p['info']['paper'], p['info'].get('source', 'ar5iv'))
        by_paper.setdefault(key, []).append(p)

    for (arx_id, source), items in by_paper.items():
        url = f'https://arxiv.org/html/{arx_id}' if source == 'arxiv-html' else f'https://ar5iv.labs.arxiv.org/html/{arx_id}'
        print(f'[抓取] {arx_id} ({source}) -> {len(items)} 张')
        try:
            html = fetch(url).decode('utf-8', errors='ignore')
        except Exception as e:
            print(f'  !! 拉取失败: {e}')
            fail += len(items)
            continue
        figs = parse_arxiv_html(html, arx_id) if source == 'arxiv-html' else parse_ar5iv(html)

        # 匹配顺序: ① filter 关键词 ② caption 中 "Figure N" 编号 ③ 退化按序号
        for p in items:
            f = p['fig']
            outdir = os.path.join(ROOT, 'assets', 'figures', p['part'], p['topic'])
            os.makedirs(outdir, exist_ok=True)
            fn = f'fig{f["n"]}.png' if f.get('n') else f'fig{p["idx"]}.png'
            dest = os.path.join(outdir, fn)

            cand = None
            kw = f.get('filter', '').lower()
            if kw:
                cand = [x for x in figs if kw in x[1].lower()]
            if not cand and f.get('n'):
                cand = [x for x in figs if re.search(rf'figure\s*{f["n"]}\b', x[1], re.I)]
            if not cand:
                cand = figs[min(len(figs), p['idx']) - 1:p['idx']] or figs[:1]
            if not cand:
                print(f'  ✗ {p["part"]}/{p["topic"]} 无匹配图')
                fail += 1
                continue
            abs_url, caption = cand[0]
            try:
                data = fetch(abs_url)
                with open(dest, 'wb') as fh:
                    fh.write(data)
                print(f'  ✓ {p["part"]}/{p["topic"]}/{fn} ({len(data)} B)')
                print(f'      caption: {caption[:90]}')
                ok += 1
            except Exception as e:
                print(f'  ✗ {dest}: {e}')
                fail += 1

    print(f'\n完成: 成功 {ok} / 失败 {fail}')
    if fail:
        sys.exit(2)


if __name__ == '__main__':
    main()
