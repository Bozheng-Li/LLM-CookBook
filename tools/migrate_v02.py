# -*- coding: utf-8 -*-
"""
大模型技术 Cookbook — v0.1 → v0.2 目录重构迁移脚本

把 tools/toc.proposed.json（15 篇 / 96 条）切换为正式的 tools/toc.json（11 篇 / 62 条），
并处理 generate.py 不会替你做的三件事:

  1. 精编页(带 <!-- cookbook:handcrafted --> 标记)迁移到新的篇目录，避免被当成孤儿页留在原地
  2. 精编页内部的交叉引用重写   —— 例如 moe.html 里的 ../05-pretraining/distributed-training.html
                                    在新结构下必须变成 ../06-pretraining/distributed-training.html
  3. index.html 等根级页面里的硬编码链接重写

最后做一次全站内部链接校验，确保零死链。

用法:
    python tools/migrate_v02.py --dry-run    # 预演，只打印将要发生的变更，不写任何文件
    python tools/migrate_v02.py              # 实际执行(执行前自动备份)
    python tools/migrate_v02.py --verify     # 只跑死链校验，不做迁移

回滚:
    迁移前会把 pages/、tools/toc.json、index.html、glossary.html、dependency.html
    整体复制到 .backup-<时间戳>/ 目录，直接覆盖回来即可。
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOC_CUR = os.path.join(BASE, "tools", "toc.json")
TOC_NEW = os.path.join(BASE, "tools", "toc.proposed.json")
PAGES = os.path.join(BASE, "pages")
KEEP_MARK = "<!-- cookbook:handcrafted -->"

# 根目录下会引用 pages/ 的页面
ROOT_PAGES = ["index.html", "glossary.html", "dependency.html"]

# 退役词条 -> 承接词条。
#
# 词条被合并或删除后，旧站点里指向它的链接会变成死链 —— 比如 index.html 现在
# 就链着 07-inference/ttt.html，而 ttt 已被并入 inference-scaling。
# 承接关系没法从两份 toc 自动推导（谁并进了谁是编辑决策），必须在这里显式声明。
#
# 新增一条合并时，记得在这里补一行，否则收尾的死链校验会拦下来。
RETIRED_REDIRECT = {
    "rnn-lstm": "pre-transformer",
    "seq2seq": "pre-transformer",
    "distillation-post": "distillation",
    "distillation-deploy": "distillation",
    "ttt": "inference-scaling",
    "pruning": "quantization",
    "embedding-models": "rag",
    "embodied-world-model": "tech-map",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def topic_map(toc):
    """topic_id -> part_id"""
    return {t["id"]: p["id"] for p in toc["parts"] for t in p["topics"]}


def part_map(old_toc, new_toc):
    """
    旧 part_id -> 新 part_id
    用 topic 集合的重叠度推断。一个旧篇被拆成多个新篇时，取重叠最多的那个。
    """
    result = {}
    for op in old_toc["parts"]:
        old_ids = {t["id"] for t in op["topics"]}
        best, best_n = None, 0
        for np_ in new_toc["parts"]:
            n = len(old_ids & {t["id"] for t in np_["topics"]})
            if n > best_n:
                best, best_n = np_["id"], n
        result[op["id"]] = best if best else op["id"]
    return result


def build_rewrites(old_toc, new_toc):
    """构造 '旧相对路径片段 -> 新相对路径片段' 的重写表"""
    old_t, new_t = topic_map(old_toc), topic_map(new_toc)
    pm = part_map(old_toc, new_toc)

    rules = {}
    # 词条页：仍然存在，但换篇了
    for tid, op in old_t.items():
        np_ = new_t.get(tid)
        if np_ and np_ != op:
            rules[f"{op}/{tid}.html"] = f"{np_}/{tid}.html"

    # 词条页：已退役，重定向到承接词条
    unmapped = []
    for tid, op in old_t.items():
        if tid in new_t:
            continue
        heir = RETIRED_REDIRECT.get(tid)
        if heir is None:
            unmapped.append(tid)
            continue
        heir_part = new_t.get(heir)
        if heir_part is None:
            unmapped.append(tid)
            continue
        rules[f"{op}/{tid}.html"] = f"{heir_part}/{heir}.html"

    if unmapped:
        print("  警告: 以下词条已退役但没有登记承接目标，指向它们的链接会变成死链:")
        for tid in unmapped:
            print(f"        {tid}  -> 请在 migrate_v02.py 的 RETIRED_REDIRECT 中补一行")

    # 篇目录页
    for op, np_ in pm.items():
        if np_ != op:
            rules[f"{op}/index.html"] = f"{np_}/index.html"
    return rules, pm, old_t, new_t


def find_handcrafted():
    out = {}
    for part in sorted(os.listdir(PAGES)):
        d = os.path.join(PAGES, part)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".html"):
                continue
            p = os.path.join(d, fn)
            with open(p, encoding="utf-8") as f:
                if KEEP_MARK in f.read():
                    out[f"{part}/{fn}"] = p
    return out


def apply_rewrites_to_file(path, rules, dry):
    """
    把 rules 应用到单个 html 文件，返回 (替换次数, 是否有变化)。

    用单次正则扫描而不是逐条 str.replace，避免链式替换 ——
    即 A 规则的新值恰好是 B 规则的旧值时，被连续替换两次。
    当前规则集不存在这种交集，但目录未来还会调整，这里防死。
    """
    with open(path, encoding="utf-8") as f:
        html = f.read()
    if not rules:
        return 0, False

    # 长的模式优先，避免短模式抢先匹配
    pattern = re.compile("|".join(re.escape(k) for k in sorted(rules, key=len, reverse=True)))
    hits = []

    def repl(m):
        hits.append(m.group(0))
        return rules[m.group(0)]

    new_html = pattern.sub(repl, html)
    if hits and not dry:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
    return len(hits), new_html != html


def verify_links():
    """扫描全站 html，校验所有指向 pages/ 的内部链接都真实存在"""
    bad = []
    targets = []
    for fn in ROOT_PAGES:
        p = os.path.join(BASE, fn)
        if os.path.exists(p):
            targets.append((p, BASE))
    for part in sorted(os.listdir(PAGES)):
        d = os.path.join(PAGES, part)
        if os.path.isdir(d):
            for fn in sorted(os.listdir(d)):
                if fn.endswith(".html"):
                    targets.append((os.path.join(d, fn), d))

    for path, base_dir in targets:
        with open(path, encoding="utf-8") as f:
            html = f.read()
        for href in re.findall(r'href="([^"#?]+\.html)"', html):
            if href.startswith(("http://", "https://", "//")):
                continue
            # 跳过 JS 里拼接出来的动态 href，例如  pages/' + p.id + '/index.html
            if any(ch in href for ch in ("'", "+", "$", "{", "`")):
                continue
            resolved = os.path.normpath(os.path.join(base_dir, href))
            if not os.path.exists(resolved):
                bad.append((os.path.relpath(path, BASE).replace("\\", "/"), href))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只预演不写文件")
    ap.add_argument("--verify", action="store_true", help="只做死链校验")
    args = ap.parse_args()

    if args.verify:
        bad = verify_links()
        if bad:
            print(f"发现 {len(bad)} 处死链:")
            for src, href in bad:
                print(f"  {src}  ->  {href}")
            sys.exit(1)
        print("死链校验通过，全站内部链接均有效。")
        return

    dry = args.dry_run
    tag = "[预演] " if dry else ""

    if not os.path.exists(TOC_NEW):
        print(f"找不到 {TOC_NEW}")
        sys.exit(1)

    old_toc, new_toc = load(TOC_CUR), load(TOC_NEW)
    rules, pm, old_t, new_t = build_rewrites(old_toc, new_toc)

    print("=" * 66)
    print(f"{tag}v0.1 → v0.2 目录重构迁移")
    print("=" * 66)
    print(f"  {len(old_toc['parts'])} 篇 / {len(old_t)} 条  →  "
          f"{len(new_toc['parts'])} 篇 / {len(new_t)} 条")
    retired = sorted(set(old_t) - set(new_t))
    print(f"  退役词条 {len(retired)} 条: {', '.join(retired)}")
    print(f"  路径重写规则 {len(rules)} 条")
    print()

    # ---------- 1. 备份 ----------
    if not dry:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        bak = os.path.join(BASE, f".backup-{stamp}")
        os.makedirs(bak, exist_ok=True)
        shutil.copytree(PAGES, os.path.join(bak, "pages"))
        shutil.copy2(TOC_CUR, os.path.join(bak, "toc.json"))
        for fn in ROOT_PAGES:
            p = os.path.join(BASE, fn)
            if os.path.exists(p):
                shutil.copy2(p, os.path.join(bak, fn))
        print(f"[1/6] 已备份到 {os.path.relpath(bak, BASE)}/")
    else:
        print("[1/6] 备份 pages/ + toc.json + 根级页面")

    # ---------- 2. 迁移精编页 ----------
    hand = find_handcrafted()
    print(f"[2/6] 精编页 {len(hand)} 个:")
    for rel, src in hand.items():
        part, fn = rel.split("/")
        tid = fn[:-5]
        np_ = new_t.get(tid)
        if np_ is None:
            print(f"       ! {rel} 对应词条已退役，保留原处不动，请人工处理")
            continue
        if np_ == part:
            print(f"       - {rel}  路径不变")
            continue
        dst = os.path.join(PAGES, np_, fn)
        print(f"       > {rel}  ->  {np_}/{fn}")
        if not dry:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            # 页面正文里的 data-part 必须跟着目录一起改。
            # nav.js 靠它做侧边栏高亮、面包屑和上下页导航 —— 不改就是静默失效，
            # 页面能打开、看着正常，只有导航状态不对，很难在验收时发现。
            with open(dst, encoding="utf-8") as f:
                html = f.read()
            fixed = re.sub(r'(<body[^>]*data-part=")[^"]*(")',
                           lambda m: m.group(1) + np_ + m.group(2), html, count=1)
            if fixed != html:
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(fixed)
                print(f"       {'':9}data-part -> {np_}")

    # ---------- 3. 清理旧结构 ----------
    new_parts = {p["id"] for p in new_toc["parts"]}
    print("[3/6] 清理旧的骨架页与废弃篇目录")
    for part in sorted(os.listdir(PAGES)):
        d = os.path.join(PAGES, part)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".html"):
                continue
            p = os.path.join(d, fn)
            with open(p, encoding="utf-8") as f:
                if KEEP_MARK in f.read():
                    continue  # 精编页永不删除
            tid = fn[:-5]
            stale = (part not in new_parts) or \
                    (tid != "index" and new_t.get(tid) != part)
            if stale and not dry:
                os.remove(p)
        if not dry and os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)

    # ---------- 4. 切换 toc ----------
    print("[4/6] tools/toc.proposed.json  ->  tools/toc.json")
    if not dry:
        shutil.copy2(TOC_NEW, TOC_CUR)

    # ---------- 5. 生成 ----------
    print("[5/6] 运行 tools/generate.py")
    if not dry:
        r = subprocess.run([sys.executable, os.path.join(BASE, "tools", "generate.py")],
                           capture_output=True, text=True, encoding="utf-8", cwd=BASE)
        for line in (r.stdout or "").strip().splitlines():
            print("       " + line)
        if r.returncode != 0:
            print("       生成失败:")
            print((r.stderr or "").strip())
            sys.exit(1)

    # ---------- 6. 重写残留链接 ----------
    print("[6/6] 重写精编页与根级页面中的硬编码链接")
    total = 0
    scan = [os.path.join(BASE, f) for f in ROOT_PAGES if os.path.exists(os.path.join(BASE, f))]
    for part in sorted(os.listdir(PAGES)):
        d = os.path.join(PAGES, part)
        if os.path.isdir(d):
            scan += [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".html")]
    for p in scan:
        n, changed = apply_rewrites_to_file(p, rules, dry)
        if n:
            total += n
            print(f"       {os.path.relpath(p, BASE).replace(chr(92), '/'):46} {n} 处")
    print(f"       共重写 {total} 处链接")

    print()
    if dry:
        print("预演结束，未改动任何文件。确认无误后去掉 --dry-run 重新执行。")
        return

    bad = verify_links()
    if bad:
        print(f"迁移完成，但仍有 {len(bad)} 处死链需要人工处理:")
        for src, href in bad:
            print(f"  {src}  ->  {href}")
        sys.exit(1)
    print("迁移完成，死链校验通过。")


if __name__ == "__main__":
    main()
