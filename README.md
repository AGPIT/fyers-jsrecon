# fyers-jsrecon

Full-file JavaScript security recon of `fyers.in` / `*.fyers.in`, driven by
**opencode** (free `deepseek-v4-flash` / `mimo-2.5` models on OpenCode Zen).

## How it works

Every ~25 minutes a GitHub Actions job:

1. **collect.py** — builds the JS inventory for the whole fyers domain:
   - Wayback CDX captures (historical `.js` for `*.fyers.in`)
   - live crawl of seed hosts (`fyers.in`, `api-fyers`, `community`, `assets`),
     chasing `_next/static` chunk manifests
   - dedup by URL + content hash; state preserved in `js-inventory.json`
2. **analyze.py** — takes the next batch (`JS_PER_RUN`, default 15) of the
   **largest unanalysed** files and for each:
   - deterministic scanners (Google/AWS/GitHub/JWT/Stripe/Firebase keys,
     path endpoints) — a backstop that never misses
   - **opencode full-file deep pass** — the whole file is attached
     (`opencode run --file`) so nothing is read from fragments only
   - merges both into `reports/<sha>.md`, marks the file analyzed
3. aggregates the batch into `findings.md`
4. commits everything so the bot researchers can consume the trail

Because state persists across runs, the pipeline walks through **every**
reachable JS file on the domain over time — not just the homepage bundle.

## Config

`config.json` — scope, size caps, per-run batch size, model,
seed hosts. Override per run via `JS_PER_RUN` / `JS_MODEL`.

## Scope discipline

- Only `fyers.in` and `*.fyers.in` hosts are ever fetched or analyzed.
- Read-only: only GETs; no active exploitation.

## Output

- `js-inventory.json` — full state: every URL, size, sha256, analyzed flag
- `reports/` — one file per analyzed file (deterministic + AI lines)
- `findings.md` — aggregated secret/endpoint trail