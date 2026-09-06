# -*- coding: utf-8 -*-
"""Download key paper figures from ar5iv for the Multimodal LLM Cookbook."""
import urllib.request, re, os, json, time, sys

OUT = r"D:\multimodal-cookbook\assets\images\papers"
os.makedirs(OUT, exist_ok=True)
BASE = "https://ar5iv.labs.arxiv.org"

PAPERS = {
 "1706.03762":6,"2010.11929":6,"2103.00020":6,"1810.04805":3,"2005.14165":3,"1301.3781":2,
 "1512.03385":3,"1409.0575":2,"2103.14030":4,"2111.06377":4,"2106.08254":3,"2304.07193":3,
 "2304.02643":3,"2001.08361":2,"2203.15556":2,
 "1908.02265":4,"1908.07490":4,"1909.11790":3,"2004.06165":3,"2101.00520":3,"2202.03052":3,
 "2107.07651":3,"2201.12086":4,"2205.01917":3,"1707.05612":2,"1502.03044":2,"1612.00837":2,"1902.09506":2,
 "2303.15343":4,"2303.15389":3,"2304.14108":3,"2210.08402":3,
 "2204.14198":6,"2301.12597":6,"2304.08485":6,"2310.03744":5,"2408.03326":5,"2304.10592":4,
 "2305.06500":4,"2304.14178":4,"2308.12966":5,"2409.12191":5,"2502.13923":5,"2312.14238":4,
 "2404.16821":4,"2412.05271":4,"2408.01800":4,"2403.05525":4,"2404.14219":3,"2311.10782":4,
 "2406.16860":4,"2312.06742":3,"2402.07865":3,"2401.15947":3,"2302.14045":3,"2306.14824":3,
 "2209.06794":2,"2311.06242":3,
 "2405.09818":5,"2408.11039":4,"2409.18869":4,"2410.13848":4,"2501.17811":4,"2408.12528":3,
 "2206.08916":2,"2310.16013":3,"2307.08052":3,"2309.05519":3,
 "2306.15195":3,"2310.07704":3,"2311.03356":3,"2111.15664":3,"2210.03347":3,"2310.05110":3,
 "2307.02499":3,"2409.01704":3,"2007.00387":2,"2203.10244":2,"1904.08920":2,
 "1406.2661":3,"1711.00937":3,"2012.09841":3,"2006.11239":6,"2010.02502":3,"2112.10752":5,
 "2302.05543":5,"2208.12242":4,"2208.01618":3,"2307.01952":4,"2403.03206":4,"2205.11487":4,
 "2204.06125":3,"2102.12092":3,"2206.10789":3,"2301.00788":3,"2406.06525":3,"2404.02905":3,
 "2212.09748":4,"2408.06072":4,
 "2212.04356":4,"2310.13289":3,"2407.10759":3,"2306.05284":3,"2102.05095":3,"2106.13230":3,
 "2311.10122":4,"2311.17043":3,"2406.16852":3,"2405.21075":3,"2003.08934":4,"2308.04079":4,
 "2212.06817":3,"2307.15818":4,"2303.03378":4,"2406.09246":4,"2410.24164":4,"2402.15391":3,
 "2303.08128":3,"2303.04671":2,"2303.17580":3,"2211.11559":3,"2312.08914":4,"2501.12326":3,
 "2407.01449":4,"2410.05160":3,"2004.04906":2,"2005.11401":2,"2004.12832":2,"2404.07972":2,
 "2310.02215":3,"2311.16502":3,"2409.02813":2,"2307.06281":3,"2306.13394":2,"2305.10355":2,
 "2310.14566":2,"2403.14624":2,
 "2305.18290":3,"2402.03300":3,"2501.12948":4,"2203.02155":3,"2309.14525":3,"2405.16120":3,
 "2405.17220":3,"2402.01306":2,"2405.14734":2,"2106.09685":3,"2305.14314":3,
 "2205.14135":3,"2307.08691":3,"2407.08608":3,"2309.06180":4,"2302.13971":3,
}

UA = {"User-Agent": "Mozilla/5.0 (research-book-builder)"}

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read()

captions = {}
ok_papers = 0; ok_imgs = 0; fail = []
ids = sorted(PAPERS.keys())
for n, pid in enumerate(ids):
    try:
        html = fetch(f"{BASE}/html/{pid}").decode("utf-8", "ignore")
    except Exception as e:
        try:
            time.sleep(3)
            html = fetch(f"{BASE}/html/{pid}").decode("utf-8", "ignore")
        except Exception as e2:
            fail.append(pid); continue
    figs = re.findall(r'<figure\b[^>]*>(.*?)</figure>', html, re.S)
    want = PAPERS[pid]; got = 0; entries = []
    for blk in figs:
        if got >= want: break
        imgs = re.findall(r'<img[^>]*\ssrc="([^"]+)"[^>]*>', blk)
        if not imgs: continue
        # pick the widest image in the block
        best = None; bw = 0
        for m in re.finditer(r'<img[^>]*>', blk):
            tag = m.group(0)
            src = re.search(r'src="([^"]+)"', tag)
            w = re.search(r'\swidth="(\d+)"', tag)
            if not src: continue
            width = int(w.group(1)) if w else 300
            if width > bw: bw = width; best = src.group(1)
        if not best or bw < 160: continue
        cap = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', blk, re.S)
        capt = strip_tags(cap.group(1))[:400] if cap else ""
        url = best if best.startswith("http") else BASE + best
        ext = os.path.splitext(url)[1].lower() or ".png"
        fn = f"{pid}_{got}{ext}"
        try:
            data = fetch(url)
            if len(data) < 2500: continue
            with open(os.path.join(OUT, fn), "wb") as f: f.write(data)
            entries.append({"file": fn, "caption": capt, "bytes": len(data)})
            got += 1; ok_imgs += 1
        except Exception:
            continue
    if got: ok_papers += 1; captions[pid] = entries
    time.sleep(0.3)
    if (n+1) % 15 == 0: print(f"progress {n+1}/{len(ids)}", flush=True)

with open(os.path.join(OUT, "captions.json"), "w", encoding="utf-8") as f:
    json.dump(captions, f, ensure_ascii=False, indent=1)
print(f"DONE papers={ok_papers}/{len(ids)} images={ok_imgs} failed={fail}")
