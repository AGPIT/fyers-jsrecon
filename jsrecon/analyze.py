#!/usr/bin/env python3
"""DEEP analysis of the next per_run unanalysed fyers JS files.

Per file, in order:
  0. re-fetch body (read-only)
  1. deterministic secret + endpoint scan (never misses)          -> deterministic pass
  2. dynamic sink scan  (eval/new Function/innerHTML/postMessage/WebSocket/SW)
  3. source-map hunt    (same-URL `.map` -> reconstructed TS sources analysed too)
  4. opencode FULL-FILE pass (entire file attached via --file)
  5. endpoint probe     (read-only GET; auth-gated vs open) -> attack-surface.md
Then marks the inventory record analyzed. One batch per run.
"""

import hashlib
import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.parse
import urllib.request

CFG = json.load(open("config.json"))
PER_RUN = int(os.environ.get("JS_PER_RUN", CFG.get("per_run_files", 15)))
MODEL = os.environ.get("JS_MODEL", CFG.get("model", "opencode/deepseek-v4-flash-free"))
NET = os.environ.get("JS_PROBE", str(CFG.get("probe_endpoints", True))).lower() == "true"

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "fyers-jsrecon/2.0"}

SECRET_RE = {
    "google_key": r"AIza[0-9A-Za-z_-]{35}",
    "aws_key": r"AKIA[0-9A-Z]{16}",
    "github_token": r"gh[pousr]_[0-9A-Za-z]{36,60}",
    "slack_token": r"xox[baprs]-[0-9A-Za-z-]{10,}",
    "jwt": r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
    "stripe_key": r"(?i)sk_live_[0-9A-Za-z]{20,}",
    "basic_auth_url": r"(?i)https?://[^:\s/@]+:[^@\s/]+@",
    "firebase_cfg": r"(?i)(apiKey|projectId|authDomain|databaseURL)\s*[:=]\s*[\"'][^\"']{6,}",
    "private_pem": r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",
}
SINK_RE = [
    (r"eval\s*\([^)]{0,80}", "eval"),
    (r"new\s+Function\s*\([^)]{0,60}", "new Function"),
    (r"\.innerHTML\s*=[^;]{0,80}", "innerHTML"),
    (r"document\.write\s*\([^)]{0,60}", "document.write"),
    (r"postMessage\s*\([^)]{0,80}", "postMessage"),
    (r"addEventListener\(\s*['\"]message['\"]", "message listener"),
    (r"new\s+WebSocket\s*\([^)]{0,80}", "WebSocket"),
    (r"serviceWorker\.register", "service worker"),
    (r"localStorage\.[gs]etItem\([^)]{0,80}", "localStorage"),
    (r"atob\([^)]{0,60}", "atob"),
]
EP_RE = re.compile(r'["\'](/[a-zA-Z0-9_.~!$&\'()*+,;=:@/-]{2,})["\']')


def fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.read(), r.status
    except Exception:  # noqa: BLE001
        return None, 0


def scan_deterministic(content):
    findings = []
    for kind, pat in SECRET_RE.items():
        for m in sorted(set(re.findall(pat, content))):
            findings.append(f"SECRET|{kind}|{m[:120]}")
    seen = set()
    for m in EP_RE.finditer(content):
        ep = m.group(1)
        if len(ep) < 160 and not ep.startswith("//") and ep not in seen:
            seen.add(ep)
            findings.append(f"ENDPOINT|ANY|{ep}")
    return findings


def scan_sinks(content):
    out = []
    for pat, name in SINK_RE:
        for m in re.finditer(pat, content):
            snip = " ".join(m.group(0).split())[:100]
            line = f"NOTE|sink:{name} in: {snip}"
            if line not in out:
                out.append(line)
    return out


def hunt_source_map(url):
    """fetch <url>.map, return (map_url, {basename: source}) if a real JSON map."""
    for cand in (url + ".map", url.rsplit("?", 1)[0] + ".map"):
        body, status = fetch(cand)
        if not body or status != 200 or not body.lstrip().startswith(b"{"):
            continue
        try:
            j = json.loads(body)
        except Exception:
            continue
        if "sources" in j and isinstance(j.get("sources"), list):
            sources = {}
            for i, src in enumerate(j["sources"]):
                if i < len(j.get("sourcesContent", [])) and j["sourcesContent"][i]:
                    sources[os.path.basename(src)] = j["sourcesContent"][i]
            return cand, sources
    return None, None


def run_opencode(js_path, url):
    prompt = (
        "You are a JS security analyst for an authorized bug-bounty program "
        f"(scope: fyers.in/*.fyers.in). Analyze the ENTIRE attached file "
        f"(source {url}) — complete content, not fragments.\n\n"
        "Output STRICT blocks, one line each, no prose:\n"
        "SECRET|type|value\n"
        "ENDPOINT|method|path\n"
        "HOST|host\n"
        "NOTE|observation\n\n"
        "Report only what is actually in the file. Types: google_key, aws_key, "
        "github_token, jwt, api_key, db_credential, internal_endpoint, dev_url, "
        "other. If nothing sensitive or notable, output exactly:\nNONE_ANALYSABLE"
    )
    cmd = ["opencode", "run", prompt, "--model", MODEL, "--file", js_path]
    env = dict(os.environ)
    env["PATH"] = os.path.expanduser("~/.opencode/bin") + os.pathsep + env.get("PATH", "")
    for _ in range(2):
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=420, env=env)
            if r.stdout:
                return r.stdout.decode("utf-8", "ignore")
        except subprocess.TimeoutExpired:
            time.sleep(10)
    return ""


def run_and_collect(js_path, url, prefix=""):
    out = run_opencode(js_path, url)
    parts = []
    for ln in out.splitlines():
        ln = ln.strip()
        if ln.startswith(("SECRET|", "ENDPOINT|", "HOST|", "NOTE|")) or ln == "NONE_ANALYSABLE":
            parts.append(prefix + ln)
    return parts


def probe(cluster):
    """Read-only GET on (host,path) pairs; returns [(url, status, ctype)]."""
    out = []
    seen = set()
    count = 0
    for host, paths in sorted(cluster.items()):
        for path in sorted(paths):
            if count >= 400:
                return out
            u = f"https://{host}{path}"
            if u in seen:
                continue
            seen.add(u)
            body, status = fetch(u, timeout=12)
            ctype = ""
            if body:
                try:
                    req = urllib.request.Request(u, headers=UA)
                    with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
                        ctype = r.headers.get("Content-Type", "")[:40]
                except Exception:
                    pass
            if status in (200, 301, 302, 401, 403, 404, 405, 500):
                out.append((u, status, ctype))
            count += 1
            time.sleep(0.15)
    return out


def report_path(url):
    return os.path.join("reports", hashlib.sha256(url.encode()).hexdigest()[:10] + ".md")


def main():
    os.makedirs("jsrecon/work", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    inv = json.load(open("js-inventory.json"))
    todo = sorted([x for x in inv if not x.get("analyzed")], key=lambda x: -x["size"])[:PER_RUN]
    print(f"[todo] {len(todo)} files this run")

    cluster = {}
    for i, item in enumerate(todo, 1):
        url = item["url"]
        body, status = fetch(url)
        if not body or status != 200:
            item["analyzed"] = True
            item["error"] = f"fetch {status}"
            with open("js-inventory.json", "w") as f:
                json.dump(inv, f, indent=1)
            print(f"  [{i}/{len(todo)}] FETCH-FAIL {url}: {status}")
            continue
        item["size"] = len(body)
        item["sha256"] = hashlib.sha256(body).hexdigest()[:16]
        content = body.decode("utf-8", "ignore")

        parts = scan_deterministic(content) + scan_sinks(content)

        js_path = os.path.join("jsrecon", "work", f"js{i:03}.js")
        with open(js_path, "w", errors="ignore") as f:
            f.write(content)
        parts += run_and_collect(js_path, url)

        map_url, sources = hunt_source_map(url)
        if sources:
            joined = "\n\n".join(f"//== {k}\n" + v[:80000] for k, v in sources.items())
            with open(os.path.join("jsrecon", "work", "sm.js"), "w", errors="ignore") as f:
                f.write(joined)
            parts += ["NOTE|sourcemap found: " + map_url + f" ({len(sources)} sources)"]
            parts += run_and_collect(os.path.join("jsrecon", "work", "sm.js"), url + " (sourcemap)", "MAP ")
            item["map"] = map_url

        rp = report_path(url)
        with open(rp, "w") as f:
            f.write(f"# {url}\n")
            for ln in parts:
                f.write(ln + "\n")
            if not parts:
                f.write("NONE_ANALYSABLE\n")
        item["analyzed"] = True
        item["report"] = rp

        for ln in parts:
            if ln.startswith(("ENDPOINT|", "MAP ENDPOINT|")):
                path = ln.split("|", 2)[-1]
                if path.startswith("/"):
                    host = urllib.parse.urlparse(url).netloc
                    cluster.setdefault(host, set()).add(path)
        with open("js-inventory.json", "w") as f:
            json.dump(inv, f, indent=1)
        print(f"  [{i}/{len(todo)}] {url} ({item['size']}B) -> {len(parts)} lines")
        time.sleep(1)

    if NET and cluster:
        rows = probe(cluster)
        with open("attack-surface.md", "a") as f:
            for u, st, ct in rows:
                f.write(f"{st} | {u} | {ct}\n")
        print(f"[probe] {len(rows)} endpoint checks appended to attack-surface.md")

    print(aggregate())


def aggregate():
    lines = []
    for name in sorted(os.listdir("reports")):
        body = open(os.path.join("reports", name), errors="ignore").read()
        m = re.search(r"^# (.+)$", body, re.M)
        url = m.group(1) if m else name
        for ln in body.splitlines():
            if ln.startswith("SECRET|") or (ln.startswith("MAP SECRET|")):
                lines.append((url, ln))
    lines.sort()
    with open("findings.md", "w") as f:
        f.write("# JS Recon Findings (fyers.in) — deep scan\n\n")
        f.write(f"_src {time.strftime('%Y-%m-%d %H:%M UTC')} — {len(lines)} secret hits_\n\n")
        for url, ln in lines[-800:]:
            f.write(f"- `{url}`\n  `{ln}`\n")
    return f"findings.md updated ({len(lines)} secret lines)"


if __name__ == "__main__":
    main()