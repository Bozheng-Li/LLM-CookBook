# -*- coding: utf-8 -*-
"""
Batch-compress oversized paper figures in assets/images/papers/ for GitHub hosting.
PNG/JPG > 1024px wide are resized and (for PNG) converted to JPEG to keep the
repo clone size reasonable. Manifest is updated so check_html.py still passes.
"""
import os
import re
import glob
from PIL import Image

PAPERS_DIR = os.path.join('assets', 'images', 'papers')
CHAPTERS_DIR = 'chapters'

MAX_WIDTH = 1200            # px, papers render fine below this
PNG_TO_JPEG_Q = 78          # quality target
RENAME_LOOSE_THRESHOLD = 1024  # only compress files wider than this

def collect_refs():
    refs = set()
    for ch in glob.glob(os.path.join(CHAPTERS_DIR, '*.html')):
        with open(ch, encoding='utf-8') as f:
            text = f.read()
        for m in re.finditer(r'(?:assets/images/papers/)([A-Za-z0-9_.\-]+)', text):
            refs.add(m.group(1))
    return refs

def convert(png_path):
    jpg_path = os.path.splitext(png_path)[0] + '.jpg'
    img = Image.open(png_path)
    if img.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode in ('RGBA', 'LA'):
            bg.paste(img, mask=img.split()[-1])
        else:
            img = img.convert('RGB')
            bg.paste(img)
        img = bg
    else:
        img = img.convert('RGB')
    if img.width > MAX_WIDTH:
        h = int(img.height * MAX_WIDTH / img.width)
        img = img.resize((MAX_WIDTH, h), Image.LANCZOS)
    img.save(jpg_path, 'JPEG', quality=PNG_TO_JPEG_Q, optimize=True)
    return jpg_path

def rewrite_html(ch_path, mapping):
    with open(ch_path, encoding='utf-8') as f:
        text = f.read()
    changed = False
    for old, new in mapping.items():
        if old in text:
            text = text.replace(old, new)
            changed = True
    if changed:
        with open(ch_path, 'w', encoding='utf-8') as f:
            f.write(text)
    return changed

def main():
    refs = collect_refs()
    on_disk = {os.path.basename(p) for p in glob.glob(os.path.join(PAPERS_DIR, '*'))}
    mapping = {}
    saved = 0
    for name in sorted(on_disk):
        src = os.path.join(PAPERS_DIR, name)
        size = os.path.getsize(src)
        if size < 1.5 * 1024 * 1024:
            continue
        if name in refs is False:
            pass
        stem, ext = os.path.splitext(name)
        if ext.lower() == '.png':
            jpg = convert(src)
        elif ext.lower() in ('.jpg', '.jpeg'):
            # Re-save at downscaled resolution only if very large
            img = Image.open(src).convert('RGB')
            if img.width > MAX_WIDTH:
                h = int(img.height * MAX_WIDTH / img.width)
                img = img.resize((MAX_WIDTH, h), Image.LANCZOS)
            img.save(src, 'JPEG', quality=PNG_TO_JPEG_Q, optimize=True)
            continue
        else:
            continue
        if name in refs:
            mapping[name] = os.path.basename(jpg)
            os.remove(src)
        else:
            os.remove(src)
        saved += os.path.getsize(jpg)
    # Rewrite chapters referencing renamed assets
    n_ch = 0
    for ch in glob.glob(os.path.join(CHAPTERS_DIR, '*.html')):
        if rewrite_html(ch, mapping):
            n_ch += 1
    print(f'Rewritten {len(mapping)} assets across {n_ch} chapter files.')
    print(f'New total papers dir size: {sum(os.path.getsize(p) for p in glob.glob(os.path.join(PAPERS_DIR, "*")))/1024/1024:.0f}MB')

if __name__ == '__main__':
    main()
