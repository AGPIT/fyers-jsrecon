#!/usr/bin/env python3
"""Collect the fyers JS inventory from the url-fyers corpus ONLY.

PRIMARY (only) source: https://raw.githubusercontent.com/riteshekbote/url-fyers/main/urls.txt
Every js URL in that file is inventoried; nothing is crawled or appended.

Strategy (network-friendly):
  - threaded but throttled download of NEW urls each run, capped per run
  - bodies stored in blobs/<sha>.js so the analyzer NEVER re-fetches
  - blob cache survives across runs via GitHub Actions cache (not git)

State: js-inventory.json [{url, host, size, sha256, analyzed, error}]
Migration: analyzed records missing the current pass marker (or carrying an
error) were processed by a broken pass -> reset for the deep pass to redo.
"""

import concurrent.futures
import hashlib
import json
import os
import ssl
import sys
import time
import urllib.parse
import urllib.request

CFG = json.load(open("config.json"))
MIN_SIZE = CFG["min_size_bytes"]
MAX_SIZE = CFG["max_size_bytes"]
URLS_TXT = CFG.get("urls_txt", "https://raw.githubusercontent.com/riteshekbote/url-fyers/main/urls.txt")
WORKERS = int(CFG.get("download_workers", 6))
MAX_DL = int(CFG.get("max_downloads_per_run", 3000))
PASS_MARKER = CFG.get("pass_marker", "deep1")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) fyers-jsrecon/2.0"}


def fetch(url, timeout=25, retries=2):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read(), r.status
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(0.4)
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


def looks_like_js(body):
    head = body[:512].lstrip().lower()
    if head.startswith(b"<!") or b"<html" in head or b"<head" in head:
        return False
    return True


def main():
    os.makedirs("blobs", exist_ok=True)
    urls = corpus_js_urls()
    if not urls:
        print("no urls; aborting")
        return 1

    prev = {}
    try:
        prev = {x["url"]: x for x in json.load(open("js-inventory.json"))}
    except Exception:
        pass

    # migration: reset records analysed by a broken pass (no marker / had error)
    for rec in prev.values():
        if rec.get("analyzed") and (rec.get("pass") != PASS_MARKER or rec.get("error")):
            rec["analyzed"] = False
            rec.pop("error", None)
            rec.pop("pass", None)

    # fetch-only-if-missing; blobs dir reused from cache where possible
    def grab(u):
        blob_path = None
        sha = None
        body = None
        if count_hits.get(u):
            return None
        body, status = fetch(u, timeout=20)
        if not body:
            return {"url": u, "host": urllib.parse.urlparse(u).netloc,
                    "size": 0, "analyzed": False, "error": f"fetch {status}"}
        if status != 200:
            return None
        if len(body) < MIN_SIZE or len(body) > MAX_SIZE:
            return None
        if not looks_like_js(body):
            return {"url": u, "host": urllib.parse.urlparse(u).netloc,
                    "size": len(body), "analyzed": False, "error": "html"}
        sha = hashlib.sha256(body).hexdigest()[:16]
        blob_path = os.path.join("blobs", sha + ".js")
        if not os.path.exists(blob_path):
            with open(blob_path, "wb") as f:
                f.write(body)
        count_hits[u] = 1
        return {
            "url": u,
            "host": urllib.parse.urlparse(u).netloc,
            "size": len(body),
            "sha256": sha,
            "analyzed": False,
            "map": None,
        }

    count_hits = {}
    new_urls = sorted(u for u in urls if u not in prev)
    new_urls = new_urls[:MAX_DL]

    fetched = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for item in ex.map(grab, new_urls):
            if item:
                fetched.append(item)

    inv = [prev[u] for u in sorted(prev)]
    inv.extend(sorted(fetched, key=lambda x: x["url"]))
    # prune stale-inv if cache missing? never; analyzer only inspects its set.

    with open("js-inventory.json", "w") as f:
        json.dump(inv, f, indent=1)
    analyzed = sum(1 for x in inv if x.get("analyzed"))
    pending = sum(1 for x in inv if not x.get("analyzed"))
    blobs = sum(len(f) for _, _, f in os.walk("blobs")) if os.path.isdir("blobs") else 0
    print(f"[inventory] total={len(inv)} analyzed={analyzed} pending={pending} "
          f"downloaded_this_run={len(fetched)} (cap {MAX_DL}) blobs={blobs}")


if __name__ == "__main__":
    sys.exit(main())