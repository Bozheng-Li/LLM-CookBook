#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 Wikimedia Commons 搜索可商用图片(用于 Cookbook 配图)"""
import json, sys, urllib.request, urllib.parse

def search(q, limit=4):
    params = {
        'action': 'query', 'generator': 'search', 'gsrsearch': q,
        'gsrnamespace': '6', 'gsrlimit': limit,
        'prop': 'imageinfo', 'iiprop': 'url|extmetadata', 'iiurlwidth': 900,
        'format': 'json'
    }
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    req = urllib.request.Request(url, headers={'User-Agent': 'CookbookBot/1.0 (educational project)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    print(f'=== 搜索: {q} ===')
    for pid, p in d.get('query', {}).get('pages', {}).items():
        ii = p.get('imageinfo', [{}])[0]
        md = ii.get('extmetadata', {})
        u = ii.get('thumburl', ii.get('url', ''))
        if u.endswith(('.png', '.jpg', '.jpeg')):
            lic = md.get('LicenseShortName', {}).get('value', '?')
            desc = md.get('ImageDescription', {}).get('value', '')[:70]
            artist = md.get('Artist', {}).get('value', '?')[:50]
            print(f'FILE: {p.get("title","")[:70]}')
            print(f'  URL: {u[:130]}')
            print(f'  LIC: {lic} | DESC: {desc} | ARTIST: {artist}')

if __name__ == '__main__':
    for q in sys.argv[1:]:
        search(q)
