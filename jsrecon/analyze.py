#!/usr/bin/env python3
"""Analyze the next per_run_files unanalysed JavaScript files.

For every file:
  1. deterministic secret / endpoint scanners (backstop, never misses)
  2. opencode full-file deep pass (reads the ENTIRE attached file)

Appends one report per file under reports/, then aggregates into
findings.md. Marks the inventory analyzed so the next run moves on.
"""

import hashlib
import json
import os
import re
import subprocess
import ssl
import sys
import time
import urllib.request

CFG = json.load(open("config.json"))
PER_RUN = int(os.environ.get("JS_PER_RUN", CFG["per_run_files"]))
MODEL = os.environ.get("JS_MODEL", CFG["model"])
WORKDIR = "jsrecon/work"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

SECRET_RE = {
    "google_key": r"AIza[0-9A-Za-z_-]{35}",
    "aws_key": r"AKIA[0-9A-Z]{16}",
    "github_token": r"gh[pousr]_[0-9A-Za-z]{36,60}",
    "slack_token": r"xox[baprs]-[0-9A-Za-z-]{10,}",
    "jwt": r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
    "stripe_key": r"(?i)sk_live_[0-9A-Za-z]{20,}",
    "basic_auth_url": r"(?i)https?://[^:\s/@]+:[^@\s/]+@",
    "firebase_cfg": r"(?i)firebase[A-Za-z0-9_.:-]{0,40}(apiKey|projectId|databaseURL)[\"']?\s*[:=]\s*[\"'][^\"']{6,}",
}
EP_RE = re.compile(r'["\'](/[a-zA-Z0-9_.~!$&\'()*+,;=:@/-]{2,})["\']')


def scan_deterministic(content):
    findings = []
    for kind, pat in SECRET_RE.items():
        for m in sorted(set(re.findall(pat, content))):
            findings.append({"kind": "secret", "type": kind, "value": m[:120]})
    seen = set()
    for m in EP_RE.finditer(content):
        ep = m.group(1)
        if len(ep) < 160 and ep not in seen:
            seen.add(ep)
            findings.append({"kind": "endpoint", "type": "path", "value": ep})
    return findings


def run_opencode(js_path, url):
    prompt = (
        "You are a JS security analyst for an authorized bug-bounty program "
        f"(scope: fyers.in/*.fyers.in). Analyze the ENTIRE attached JavaScript file "
        f"(source {url}) complete, not just fragments.\n\n"
        "Output STRICT blocks, one per line, nothing else, no prose:\n"
        "SECRET|type|value\n"
        "ENDPOINT|method|path\n"
        "HOST|host\n"
        "NOTE|observation\n\n"
        "Report only things actually present in the file. Secret types: "
        "google_key, aws_key, github_token, jwt, api_key, db_credential, "
        "internal_endpoint, dev_url, other. "
        "If you see nothing sensitive or malformed, output exactly:\nNONE_ANALYSABLE"
    )
    cmd = ["opencode", "run", "--model", MODEL, "--file", js_path, prompt]
    env = dict(os.environ)
    env["PATH"] = os.path.expanduser("~/.opencode/bin") + os.pathsep + env.get("PATH", "")
    for attempt in range(2):
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=420, env=env)
            return r.stdout.decode("utf-8", "ignore")
        except subprocess.TimeoutExpired:
            time.sleep(10)
    return ""


def report_path(url):
    return os.path.join("reports", hashlib.sha256(url.encode()).hexdigest()[:10] + ".md")


def main():
    os.makedirs(WORKDIR, exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    inv = json.load(open("js-inventory.json"))
    todo = [x for x in inv if not x.get("analyzed")]
    todo.sort(key=lambda x: -x["size"])
    todo = todo[:PER_RUN]
    print(f"[todo] {len(todo)} files this run")

    for i, item in enumerate(todo, 1):
        url = item["url"]
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "fyers-jsrecon/1.0"})
            body = urllib.request.urlopen(req, timeout=30, context=CTX).read()
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(todo)}] download fail {url}: {e}")
            item["analyzed"] = True
            item["error"] = str(e)
            continue
        item["sha256"] = hashlib.sha256(body).hexdigest()[:16]
        item["size"] = len(body)
        if not body.lstrip().startswith((b"{", b"[", b"(", b"<!DOCTYPE", b"function", b"var ", b"const", b"let ", b"/*")):
            print(f"[{i}/{len(todo)}] skip non-js {url}")
            item["analyzed"] = True
            continue
        js_path = os.path.join(WORKDIR, f"js{i:03}.js")
        with open(js_path, "wb") as f:
            f.write(body)
        content = body.decode("utf-8", "ignore")

        parts = []
        try:
            det = scan_deterministic(content)
            for fnd in det:
                parts.append(f"SECRET|{fnd['type']}|{fnd['value']}")
        except Exception as e:  # noqa: BLE001
            parts.append(f"NOTE|deterministic error: {e}")

        out = run_opencode(js_path, url)
        for ln in out.splitlines():
            ln = ln.strip()
            if ln.startswith(("SECRET|", "ENDPOINT|", "HOST|", "NOTE|")) or ln == "NONE_ANALYSABLE":
                parts.append(ln)

        rp = report_path(url)
        with open(rp, "w") as f:
            f.write(f"# {url}\n")
            for ln in parts:
                f.write(ln + "\n")
        if not parts:
            with open(rp, "a") as f:
                f.write("NONE_ANALYSABLE\n")

        item["analyzed"] = True
        item["report"] = rp
        with open("js-inventory.json", "w") as f:
            json.dump(inv, f, indent=1)
        print(f"  [{i}/{len(todo)}] done {url} ({len(body)}B) -> {len(parts)} lines")
        time.sleep(1)

    print(aggregate())


def aggregate():
    lines = []
    if not os.path.isdir("reports"):
        return "no reports yet"
    for name in sorted(os.listdir("reports")):
        p = os.path.join("reports", name)
        body = open(p, errors="ignore").read()
        m = re.search(r"^# (.+)$", body, re.M)
        url = m.group(1) if m else p
        for ln in body.splitlines():
            if ln.startswith("SECRET|") and ln != "SECRET|":
                lines.append((url, ln))
    lines.sort()
    with open("findings.md", "w") as f:
        f.write("# JS Recon Findings (fyers.in scope)\n\n")
        f.write(f"_Generated {time.strftime('%Y-%m-%d %H:%M UTC')} — {len(lines)} secret lines_\n\n")
        for url, ln in lines[-600:]:
            f.write(f"- `{url}`\n  `{ln}`\n")
    return f"findings.md updated ({len(lines)} secret lines)"


if __name__ == "__main__":
    main()
