#!/usr/bin/env python3
"""Collect the fyers JS inventory from the url-fyers corpus ONLY.

PRIMARY (only) source: https://raw.githubusercontent.com/riteshekbote/url-fyers/main/urls.txt
Every js URL in that file is inventoried; nothing is crawled or appended.

State: js-inventory.json [{url, host, size, sha256, analyzed, error}]
Raw bodies are NOT stored in git (too large); the analyzer re-fetches.
"""

import hashlib
import json
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request

CFG = json.load(open("config.json"))
MIN_SIZE = CFG["min_size_bytes"]
MAX_SIZE = CFG["max_size_bytes"]
URLS_TXT = CFG.get("urls_txt", "https://raw.githubusercontent.com/riteshekbote/url-fyers/main/urls.txt")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) fyers-jsrecon/2.0"}


def fetch(url, timeout=60, retries=2):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read(), r.status
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.2)
    return None, 0


def in_scope(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    return host == "fyers.in" or host.endswith(".fyers.in")


def corpus_js_urls():
    out = set()
    body, status = fetch(URLS_TXT, timeout=90)
    if not body:
        print(f"[corpus] failed status={status}")
        return out
    for line in body.decode("utf-8", "ignore").splitlines():
        line = line.strip()
        if not line or not line.lower().endswith((".js", ".mjs")):
            continue
        if in_scope(line):
            out.add(line)
    print(f"[corpus] {len(out)} js urls from url-fyers corpus (authoritative list)")
    return out


def main():
    urls = corpus_js_urls()
    if not urls:
        print("no urls; aborting")
        return 1

    prev = {}
    try:
        prev = {x["url"]: x for x in json.load(open("js-inventory.json"))}
    except Exception:
        pass

    inv = []
    for u in sorted(urls):
        if u in prev:
            inv.append(prev[u])
            continue
        body, status = fetch(u, timeout=20)
        if not body or status != 200:
            continue
        if len(body) < MIN_SIZE or len(body) > MAX_SIZE:
            continue
        inv.append({
            "url": u,
            "host": urllib.parse.urlparse(u).netloc,
            "size": len(body),
            "sha256": hashlib.sha256(body).hexdigest()[:16],
            "analyzed": False,
            "map": None,
        })
        time.sleep(0.2)

    with open("js-inventory.json", "w") as f:
        json.dump(inv, f, indent=1)
    analyzed = sum(1 for x in inv if x.get("analyzed"))
    print(f"[inventory] total={len(inv)} analyzed={analyzed} pending={len(inv) - analyzed}")


if __name__ == "__main__":
    sys.exit(main())
