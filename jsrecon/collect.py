#!/usr/bin/env python3
"""Collect the fyers JS inventory from the url-fyers corpus ONLY.

PRIMARY (only) source: https://raw.githubusercontent.com/riteshekbote/url-fyers/main/urls.txt
Every js URL in that file is inventoried; nothing is crawled or appended.

State: js-inventory.json [{url, host, size, sha256, analyzed, error}]
Raw bodies are NOT stored in git (too large); the analyzer re-fetches.
"""

import concurrent.futures
import hashlib
import json
import re
import ssl
import sys
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


def fetch(url, timeout=25, retries=1):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read(), r.status
        except Exception as e:  # noqa: BLE001
            last = e
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
    if head.startswith(b"<!") or b"<html" in head or b"<head" in head or head.startswith(b"<script"):
        return False
    if body.startswith(b"{"):
        return True
    return True


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

    # migration: records analyzed without the deep-pass marker, or with a
    # recorded error, were processed by a broken pass — reset them so the
    # current deep pass re-analyses or retries them.
    pass_marker = CFG.get("pass_marker", "deep1")
    for rec in prev.values():
        if rec.get("analyzed") and (rec.get("pass") != pass_marker or rec.get("error")):
            rec["analyzed"] = False
            rec.pop("error", None)
            rec.pop("pass", None)

    new_urls = sorted(u for u in urls if u not in prev)
    max_downloads = int(CFG.get("max_downloads_per_run", 2500))
    new_urls = new_urls[:max_downloads]

    def grab(u):
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
                    "size": len(body), "analyzed": False, "error": "html"}  # retried later
        return {
            "url": u,
            "host": urllib.parse.urlparse(u).netloc,
            "size": len(body),
            "sha256": hashlib.sha256(body).hexdigest()[:16],
            "analyzed": False,
            "map": None,
        }

    fetched = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for item in ex.map(grab, new_urls):
            if item:
                fetched.append(item)

    inv = [prev[u] for u in sorted(prev)]
    inv.extend(sorted(fetched, key=lambda x: x["url"]))

    with open("js-inventory.json", "w") as f:
        json.dump(inv, f, indent=1)
    analyzed = sum(1 for x in inv if x.get("analyzed"))
    remaining = sum(1 for x in inv if not x.get("analyzed"))
    print(f"[inventory] total={len(inv)} analyzed={analyzed} pending={remaining} "
          f"downloaded_this_run={len(fetched)} (cap {max_downloads})")


if __name__ == "__main__":
    sys.exit(main())
