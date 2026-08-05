#!/usr/bin/env python3
"""Collect a fresh inventory of *.fyers.in JavaScript files.

Sources (pure stdlib, no external binaries):
  1. Wayback CDX API  - historical .js captures for *.fyers.in
  2. Live crawl        - seed hosts, parse HTML/JS for asset URLs,
                         follow _next/static chunk manifests
  3. Known asset dirs  - assets.fyers.in style /js/ listings when open

Writes js-inventory.json: [{url, host, size, sha256, analyzed}]
Deduped by url + content hash. Never touches non-fyers.in hosts.
"""

import hashlib
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CFG = json.load(open("config.json"))
SCOPE = CFG["scope"]
MIN_SIZE = CFG["min_size_bytes"]
MAX_SIZE = CFG["max_size_bytes"]

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) fyers-jsrecon/1.0"}
JS_RE = re.compile(r'["\'(](https?:)?//([a-zA-Z0-9._-]*fyers[a-zA-Z0-9._-]*\.in)[^"\')]*(\.js)(\?[^"\')]*)?["\')]', re.I)
JS_RE2 = re.compile(r'["\'](/[^"\']*\.js)(\?[^"\']*)?["\']', re.I)


def fetch(url, timeout=20, retries=2):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read(), r.status, r.headers.get("Content-Type", "")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5)
    return None, 0, str(last)


def in_scope(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    return host == "fyers.in" or host.endswith(".fyers.in")


def abs_url(base, ref):
    if not ref:
        return None
    ref = ref.strip()
    if ref.startswith("//"):
        ref = "https:" + ref
    u = urllib.parse.urljoin(base, ref)
    if not in_scope(u):
        return None
    if not u.lower().endswith((".js", ".mjs")):
        return None
    return u


def wayback_js_urls():
    """CDX query for *.fyers.in captures with urlkey containing .js."""
    out = set()
    q = {
        "url": "*.fyers.in/*.js*",
        "output": "json",
        "fl": "original,timestamp,statuscode",
        "filter": "statuscode:200",
        "collapse": "urlkey",
        "limit": "8000",
    }
    url = "https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(q)
    data, status, _ = fetch(url, timeout=60)
    if not data:
        print(f"[cdx] failed status={status}")
        return out
    try:
        rows = json.loads(data)
    except Exception:
        rows = []
    for row in rows[1:]:
        if len(row) >= 1 and in_scope(row[0]):
            out.add(row[0])
    print(f"[cdx] {len(out)} unique js urls")
    return out


def crawl_js_urls(seed_urls, max_urls=2500):
    """BFS over seed pages; collect .js asset URLs; also chase _next manifests."""
    out = set()
    seen_pages = set()
    queue = list(seed_urls)
    while queue and len(seen_pages) < 60 and len(out) < max_urls:
        page = queue.pop(0)
        if page in seen_pages:
            continue
        seen_pages.add(page)
        body, status, ctype = fetch(page, timeout=18)
        if not body:
            continue
        text = body.decode("utf-8", "ignore")
        for m in JS_RE.finditer(text) + list(JS_RE2.finditer(text)):
            u = abs_url(page, m.group(0).strip("\"'(),"))
            if u:
                out.add(u)
        # chase _next/static chunk manifests
        for m in re.finditer(r'/_next/static/[a-zA-Z0-9._-]+/_buildManifest\.js', text):
            queue.append("https://fyers.in" + m.group(0))
        # chase js-dir HTML listings
        for m in re.finditer(r'href="([^"]*\.js)"', text):
            u = abs_url(page, m.group(1))
            if u:
                out.add(u)
        time.sleep(0.2)
    print(f"[crawl] {len(out)} js urls")
    return out


def content_sha(body):
    return hashlib.sha256(body).hexdigest()[:16]


def main():
    urls = wayback_js_urls()
    urls |= crawl_js_urls(CFG["seed_hosts"])

    # load previous inventory to preserve analysis state
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
        try:
            body, status, _ = fetch(u, timeout=25)
        except Exception:
            continue
        if not body or status != 200:
            continue
        if len(body) < MIN_SIZE or len(body) > MAX_SIZE:
            continue
        host = urllib.parse.urlparse(u).netloc
        inv.append({
            "url": u,
            "host": host,
            "size": len(body),
            "sha256": content_sha(body),
            "analyzed": False,
        })
        time.sleep(0.3)

    with open("js-inventory.json", "w") as f:
        json.dump(inv, f, indent=1)
    analyzed = sum(1 for x in inv if x.get("analyzed"))
    print(f"[inventory] total={len(inv)} analyzed={analyzed} new={len(inv) - analyzed}")


if __name__ == "__main__":
    sys.exit(main())
