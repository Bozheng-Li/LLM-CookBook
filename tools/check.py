# -*- coding: utf-8 -*-
"""页面达标自检尺子。

用法:
  python tools/check.py pages/07-posttraining/dpo.html
  python tools/check.py 07-posttraining          # 整篇
  python tools/check.py all                      # 全站

统计口径（重要）:
  只统计 <main> 内的内容；正文净字数会剔除 mermaid 图内文字、<pre> 代码块、<script>，
  所以"堆图堆代码"不会让字数虚高，必须靠真正的讲解文字。
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, 'pages')
MAIN_RE = re.compile(r'<main\b[^>]*>(.*?)</main>', re.S | re.I)

BAR = dict(cn=5000, m=4, t=3, c=1, d=1, r=3)


def analyze(path):
    html = open(path, encoding='utf-8', errors='ignore').read()
    mo = MAIN_RE.search(html)
    body = mo.group(1) if mo else html
    prose = re.sub(r'<div class="mermaid".*?</div>', ' ', body, flags=re.S)
    prose = re.sub(r'<pre.*?</pre>', ' ', prose, flags=re.S)
    prose = re.sub(r'<script.*?</script>', ' ', prose, flags=re.S)
    prose = re.sub(r'<[^>]+>', ' ', prose)
    cn = len(re.findall(r'[\u4e00-\u9fff]', prose))
    kinds = set(re.findall(
        r'(flowchart|graph\s+(?:TD|LR|TB|RL)|sequenceDiagram|stateDiagram-v2|'
        r'mindmap|timeline|classDiagram|journey|pie|erDiagram|quadrantChart|gantt)',
        body))
    return dict(
        cn=cn,
        m=len(re.findall(r'class="mermaid"', body)),
        t=body.count('<table'),
        c=body.count('<pre'),
        d=body.count('<details'),
        r=len(re.findall(r'href="https?://', body)),
        kinds=len(kinds),
        hand='cookbook:handcrafted' in html,
    )


def verdict(d):
    bad = [k for k in BAR if d[k] < BAR[k]]
    if not d['hand']:
        bad.append('handcrafted')
    if d['kinds'] < 2:
        bad.append('图种类单一')
    return bad


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
        bad = verdict(d)
        rel = os.path.relpath(f, PAGES).replace('\\', '/')
        tag = 'OK ' if not bad else 'GAP'
        if not bad:
            okc += 1
        print('%s %-42s 字=%-5d 图=%-2d(%d种) 表=%-2d 码=%-2d 深=%-2d 链=%-2d %s'
              % (tag, rel, d['cn'], d['m'], d['kinds'], d['t'], d['c'], d['d'],
                 d['r'], ('缺:' + ','.join(bad)) if bad else ''))
    print('-' * 96)
    print('达标 %d / %d    达标线: 正文≥%d字 图≥%d(≥2种) 表≥%d 码≥%d 深入块≥%d 外链≥%d'
          % (okc, len(files), BAR['cn'], BAR['m'], BAR['t'], BAR['c'], BAR['d'], BAR['r']))


if __name__ == '__main__':
    main()
