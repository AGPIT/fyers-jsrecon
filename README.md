# fyers-jsrecon

DEEP full-file JavaScript security recon of `fyers.in` / `*.fyers.in`, driven by
**opencode** (`opencode/deepseek-v4-flash-free` — DeepSeek V4 Flash Free).

Inventory source is **exclusively the authoritative corpus**
[`riteshekbote/url-fyers/urls.txt`](https://github.com/riteshekbote/url-fyers/blob/main/urls.txt)
— every JS file on the fyers surface (6,993 URLs). Nothing else is crawled or
appended.

## How it works

Every **10 minutes** a GitHub Actions job runs one batch:

1. **collect.py** — pulls the corpus urls.txt, filters in-scope `.js`, diffs
   against prior state, refreshes `js-inventory.json` (URL, host, size, sha256,
   analyzed flag). Analyzed files are never re-fetched.
2. **analyze.py** — takes the next `JS_PER_RUN` (default 15) **largest
   unanalysed** files and for each:
   - **deterministic secret scan** — Google/AWS/GitHub/Slack/JWT/Stripe keys,
     basic-auth URLs, Firebase config, PEMs (a backstop that never misses)
   - **dynamic sink scan** — `eval`, `new Function`, `innerHTML`,
     `document.write`, `postMessage` + message listeners, `WebSocket`,
     service-worker registrations, `atob`, `localStorage`
   - **source-map hunt** — fetches `<url>.map`; when a map exists the
     reconstructed TS/ES sources are fed to opencode too (prefix `MAP`)
   - **opencode full-file pass** — the ENTIRE file is attached
     (`opencode run --file`) so analysis sees the whole content, not fragments
   - results merged into `reports/<sha>.md`; file marked analyzed
3. **endpoint probing** — every discovered API path is GET'd once (read-only,
   rate-limited, capped per run) and the status/type recorded, building the
   `attack-surface.md` map: which endpoints are open vs auth-gated
4. aggregates into `findings.md`, commits the trail

Because state persists, the pipeline walks through **every** file in the corpus
over time, deepest (largest) first, and re-checks the corpus every 10 min for
new URLs.

## Config

`config.json` — corpus url, scope, size caps, batch size, model,
endpoint probing toggle. Override per run: `JS_PER_RUN`, `JS_MODEL`,
`JS_PROBE=false`.

## Scope discipline

- Only `fyers.in` and `*.fyers.in` hosts are ever fetched or analyzed.
- Read-only: only GET requests; no active exploitation; probes capped + slowed.

## Output

- `js-inventory.json` — full state: every URL, size, sha256, analyzed flag
- `reports/` — one report per file (deterministic + sink + MAP + AI lines)
- `attack-surface.md` — live endpoint map: status | URL | content-type
- `findings.md` — aggregated secret/endpoint trail across all reports
