import os, re, glob

base = r'E:\大模型知识\pages'
files = sorted(glob.glob(base + '/**/*.html', recursive=True))

def analyze(path):
    with open(path, encoding='utf-8', errors='ignore') as f:
        html = f.read()
    mermaid = len(re.findall(r'class="mermaid"', html)) + len(re.findall(r'```mermaid', html))
    tables = len(re.findall(r'class="table-wrap"', html)) + html.count('<table')
    handcrafted = 'cookbook:handcrafted' in html
    text = re.sub(r'<[^>]+>', ' ', html)
    cn = len(re.findall(r'[\u4e00-\u9fff]', text))
    code = html.count('<pre') + html.count('class="language-')
    details = html.count('<details')
    ref_block = len(re.findall(r'参考文献|References|references', html))
    mtime = os.path.getmtime(path)
    return dict(mermaid=mermaid, tables=tables, handcrafted=handcrafted,
                cn=cn, code=code, details=details, refs=ref_block, mtime=mtime)

results = {}
for fp in files:
    parts = fp.split(os.sep)
    part = parts[-2]
    topic = os.path.basename(fp).replace('.html', '')
    results.setdefault(part, {})[topic] = analyze(fp)

# acceptance: basic>=4 mer, >=3 tbl, >=1 code, >=1 details, hc preserved, cn>=4000 rough
def ok(d):
    return d['mermaid'] >= 4 and d['tables'] >= 3 and d['code'] >= 1 and d['details'] >= 1 and d['handcrafted']

total_ok = total = 0
for part in sorted(results):
    print(f"\n=== {part} ===")
    for topic in sorted(results[part]):
        d = results[part][topic]
        total += 1
        good = ok(d)
        total_ok += 1 if good else 0
        status = 'OK ' if good else 'GAP'
        print(f"  [{status}] {topic:28s} cn={d['cn']:5d} mer={d['mermaid']:2d} tbl={d['tables']:2d} det={d['details']:2d} code={d['code']:2d} hc={int(d['handcrafted'])}")
print(f"\nSUMMARY: {total_ok}/{total} pages meet beginner-book bar")
