
===== ANALYST 2026-08-07 15:54:54 UTC =====
[NEW] verifiedpnl.fyers.in: pnl_url → https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data; _FYERS JWT parsed client-side, "auth validity not server-verified", used to gate UI and forwarded to get-data.
[NEW] sgb.fyers.in: OAuth appId QMABZB5R01 (prod); auth_code from URL query used directly as Authorization header; auth_token read from localStorage used as bearer.
[NEW] trade.fyers.in datafeed bundles (v9.8–12.6 + Prod/1.2): identical hardcoded Fernet token_id sha256 568d3b6a1c8c1917f1aae50eb18f9aa63784f87cac78219d741f4e2604276534 embedded in HISTORY_TEST/SUB_DATA demos.
[NEW] trade.fyers.in/static/js/broker/12.1/bundle.min.js references dev/internal API: api.fyers.in/fydev/v1, api.fyers.in/vagator/v1, api.fyers.in/fy/cdsl/dev, wss://api-socket.fyers.in/dev/order, datapub.fyers.in:8862.
[NEW] trade.fyers.in/static/js/ordwin/js/6/orderwindow.min.js: plaintext-HTTP backend 13.235.24.249:8080 /gtt/orders (host out of scope).
[NEW] trade.fyers.in/static/js/broker/13/bundle.min.js: token_id passed via URL query to /edis/details, /edis/index, /edis/authCdsl.html (live 200).
[NEW] ipo.fyers.in + sgb.fyers.in: per-env Fyers APP_ID/client_id map (prod EFR7964223 / QMABZB5R01, dev 68USODQMOF / N43J3GIGOM, stag ZT6P4L9YQB/LCFY9OOX3D / AF0MATWSX3, local H4NMJ8X2NR) + appIdHash sha256 map.
[NEW] community.fyers.in/member/gtm.js: GUEST JWT (tokenType GUEST, entityId/permissions null, networkDomain fyers.bettermode.io) sha256 dd355d343f08f5afa224720fc934b4b6af4c949d28a60c1fd96d537c1d25fd14; Google API key sha256 5489cff6e418d5d3ff071ea17eb7d83b9b01aa21d6def7c013b4ac5c3750dc64.
[NEW] www.fyers.in: Zoho Forms formperma token sha256 baebb532c3070d3b99442a7c8cff3db91dde1aafb9848da5433943d03897cf69; GA4 G-JXG5NQ1WQJ / GTM-MB6PRVDG across all marketing JS.
[NEW] www.fyers.in/_next/static/*.js served with 200 text/html (SPA catch-all rewrite).
[NEW] dev.fyers.in + alerts.fyers.in JS fetch 0/HTML (inventory: unminified bundles referenced, currently unretrievable).
[PRIO] verifiedpnl.fyers.in get-data (api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data) | 6.70 | attack 6 business 9 tech 6 gate 5 cloud 5 fresh 8
[PRIO] trade.fyers.in/static/js/broker/12.1 dev endpoints (fydev/v1, vagator/v1, api-socket wss) | 5.95 | attack 6 business 6 tech 7 gate 4 cloud 6 fresh 7
[PRIO] sgb.fyers.in OAuth auth_code/token-in-URL → Authorization | 5.85 | attack 5 business 7 tech 7 gate 4 cloud 4 fresh 8
[PRIO] trade.fyers.in datafeed hardcoded Fernet token_id (v9.8–12.6) | 5.00 | attack 4 business 4 tech 5 gate 9 cloud 4 fresh 5
[PRIO] dev.fyers.in unminified bundles (broker 50.1, datafeed 20/24/34.3, init 30) | 5.15 | attack 6 business 5 tech 8 gate 2 cloud 3 fresh 6
[PRIO] ipo.fyers.in / sgb.fyers.in per-env APP_ID+appIdHash map | 4.75 | attack 3 business 5 tech 4 gate 7 cloud 3 fresh 8
[HYP] Verified-PNL get-data lacks server-side authz on the _FYERS JWT
class: IDOR
asset: api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data (called from verifiedpnl.fyers.in)
confidence: 55
reasoning: main.*.js parses _FYERS JWT client-side to gate UI and notes "auth validity not server-verified"; the decoded token is forwarded to get-data. If backend trusts the client-provided identity/entityId without verifying signature/expiry, other users' verified PNL is retrievable.
evidence_needed: get-data returns financial payload for a token whose JWT was forged (bad sig / alg=none) or an empty/invalid token, instead of 401.
verify_steps: AUTH_HELPED:1) curl -s -i -H "Authorization: <_FYERS cookie value>" https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data → baseline shape; 2) curl with tampered JWT payload (same header, modified sub/entityId, kept signature) → compare data; 3) curl with no/blank Authorization → observe 401 vs 200.
impact: read other users' trading/PNL data; account-level financial disclosure; High if confirmed.
testability: AUTH_HELPED
[HYP] Dev/internal API servers referenced from prod bundle accept unauthenticated requests
class: MISCONFIG
asset: https://api.fyers.in/fydev/v1 and https://api.fyers.in/vagator/v1 (from trade.fyers.in/static/js/broker/12.1/bundle.min.js)
confidence: 50
reasoning: prod bundle hardcodes dev routes fydev/v1, vagator/v1 and wss://api-socket.fyers.in/dev/order. Dev tiers commonly ship weaker auth; these are first-party *.fyers.in hosts so probing is in scope.
evidence_needed: any of these return 200/JSON (not 401/403/404-spa) for an unauthenticated GET.
verify_steps: AUTH_HELPED: curl -s -i https://api.fyers.in/fydev/v1/ ; curl -s -i https://api.fyers.in/vagator/v1/ ; then a resource guess e.g. https://api.fyers.in/fydev/v1/orders and /baskets with token_id= blank — passive read-only.
impact: access to dev trading/order/margin APIs or error-enumeration of internal resources; Medium-High if data returned.
testability: AUTH_HELPED
[HYP] SGB app reuses OAuth "auth_code" from URL as a durable bearer (no code-exchange), exposing a live credential in URLs
class: OATH
asset: sgb.fyers.in (OAuth callback → Authorization header)
confidence: 50
reasoning: bundle c930e9b6... reads auth_code from URL query and uses it directly as Authorization header, and stores auth_token in localStorage for the same header. A code that behaves as a reusable bearer (not one-time) leaks via Referer/history/logs.
evidence_needed: same auth_code value accepted on repeat/parallel requests (not single-use, long TTL), i.e. code == credential.
verify_steps: AUTH_HELPED: complete login to capture auth_code from redirect URL; replay the identical value as Authorization against the SGB API twice; observe 2nd call still authorized. Do not persist the value (hash-only logging).
impact: session/account takeover on SGB if code is long-lived; token theft via Referer otherwise; High if replayable.
testability: AUTH_HELPED
[PARKED] Verified-PNL server-side authz weakness (hypothesis 1): kept, survivor #1.
[PARKED] trade dev-endpoints MISCONFIG (hypothesis 2): kept, survivor #2.
[PARKED] sgb auth_code-reuse OATH (hypothesis 3): kept, survivor #3.
[PARKED] trade.fyers.in hardcoded Fernet token_id: below priority cut; also token is a datafeed-only token_id (market data), low impact even if active — not dropped for scope, parked for a low-priority PASSIVE check of `https://trade.fyers.in/static/js/datafeed/udf/12.6/...` datafeed endpoint accepting token sha256 568d3b6a... → evidence of leftover credential only.
[PARKED] 13.235.24.249:8080/gtt/orders plaintext backend: third-party IP host not under fyers.in scope → dropped (out of scope, not a rejection of the lead).
[PARKED] widgets.min.js api_keys 1341655KwEfgY (sha256 7b678b40...) / 984896EWiONu (sha256 db159866...): unknown purpose, no in-scope verify path → low confidence, parked.
[PARKED] dev.fyers.in / alerts.fyers.in unminified JS: fetch 0 / HTML (not retrievable from this context) → parked until live.
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js: GUEST JWT (tokenType=GUEST, entityId null, permissions null) is a public-by-design community guest token — not a finding.
[LEARN] REJECTED MISCONFIG @ www.fyers.in GA4 G-JXG5NQ1WQJ + GTM-MB6PRVDG: public marketing IDs, not secrets.
[LEARN] REJECTED AUTH @ ipo.fyers.in / sgb.fyers.in APP_ID/client_id + appIdHash map: OAuth client IDs are public identifiers sent in redirect URLs; hashes of the same — not credentials.
[LEARN] REJECTED OTHER @ www.fyers.in Zoho formperma token: public client-side form key, required by design.
[LEARN] REJECTED OTHER @ trade.fyers.in Google G-NTFX8XLKVH: GA4 measurement id, public.
[LEARN] REJECTED OTHER @ trade.fyers.in/static/js/broker/12 bundle "none" scan lines: empty matches, no claim.
[FINAL] 1) verifiedpnl get-data IDOR (conf 55, AUTH_HELPED)  2) api.fyers.in dev endpoints MISCONFIG (conf 50, AUTH_HELPED)  3) sgb auth_code-reuse OATH (conf 50, AUTH_HELPED)
[NEXT] PROBE: curl -s -i --max-time 15 "https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data" (no Authorization header) then retry with "Authorization: Bearer <empty>" and with a forged JWT whose signature is invalid; compare status/body. If any returns 200+financial payload → IDOR confirmed, escalate to full authz testing.
[LEARN] REJECTED OATH @ community.fyers.in: guest JWT is public-by-design (guest claims, null permissions) — class dead here.
[LEARN] REJECTED MISCONFIG @ www.fyers.in marketing assets: only public GA4/GTM/Zoho keys — class dead on marketing JS surface.
[LEARN] REJECTED AUTH @ ipo.fyers.in/sgb.fyers.in env maps: client IDs + appIdHash are public OAuth identifiers, not secrets — class dead for the "hardcoded APP_ID" lead.
[LEARN] REJECTED OTHER @ trade.fyers.in datafeed bundles: hardcoded token present but is a demo/datafeed token_id; class alive only if PASSIVE probe shows it still authenticates datafeed requests (pending).
[RISK] fyers-js: 62 — prod bundles embed per-environment OAuth client-ID/hash maps, a repeated hardcoded demo Fernet token_id across 15+ datafeed bundles, dev API + cleartext-HTTP backend references, client-side-only _FYERS JWT gating on a financial endpoint, and guest-token + analytics keys; most items are low-impact or public-by-design, but the combination signals loose secret hygiene in the trading surface, warranting AUTH_HELPED verification of the top-3 leads.

===== ANALYST 2026-08-07 17:30:33 UTC =====
[NEW] www.fyers.in /web/ Next.js app suite live (all 200): /web/options/option-chain, /web/options/strategy-builder/explore, /web/options/analytics, /web/option-scalper, /web/markets/screeners, /web/markets/news, /web/markets/markets-overview/all, /web/markets/analytics/heatmap, /web/symbol/NSE:ADANIPORTS-EQ, /web/mtf/about, /web/fia, /web/charts, /web/reports, /web/automate, /web/api-dashboard/user-apps; _next static chunks returned as 200 text/html (SPA catch-all → JS not analyzable).
[NEW] sgb.fyers.in app pages live (all 200): /details, /orders, /sgb, /updatesgb.
[NEW] sgb.fyers.in home-ac56cb0ac001d9ac5ef2.js: new OAuth client_id AEHNSK9PRW not in the prior per-env appId map.
[NEW] trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js dev-tier endpoints: api.fyers.in/anjuna/v1/margin, api.fyers.in/fydev/v1/baskets?token_id=, api.fyers.in/fydev/v1/margin/v1?token_id=, data.fyers.in/dev-fyers/mobileapi/user-settings (token_id passed in URL query).
[NEW] webtrader.fyers.in + http://fyers.in legacy JS in inventory (all fetch 0 / unresolved); bo-login.fyers.in/validate.js present (2.6 KB, unanalyzed).
[CHANGED] trade.fyers.in/edis/authCdsl.html?token_id= now live-confirmed 200 (previously code-reference only, from broker/13 bundle).
[CHANGED] dev-tier API footprint widened: broker/12.1 (fydev/v1, vagator/v1, api-socket/dev) now joined by ordwin/4.6 (anjuna/margin, fydev baskets, data.fyers.in dev mobileapi).
[PRIO] www.fyers.in /web/ webapp (option-chain, symbol, api-dashboard/user-apps) | 6.65 | attack 6 business 7 tech 6 gate 8 cloud 5 fresh 8
[PRIO] trade.fyers.in ordwin/4.6 dev-tier API refs (anjuna/v1/margin, fydev/v1/baskets) | 5.95 | attack 6 business 6 tech 7 gate 4 cloud 6 fresh 7
[PRIO] sgb.fyers.in live app pages (/details /orders /updatesgb) | 5.60 | attack 5 business 7 tech 6 gate 4 cloud 4 fresh 7
[HYP] www.fyers.in webapp exposes unauthenticated options/market-data JSON API
class: BUSLOGIC
asset: www.fyers.in (/web/options/option-chain, /web/symbol/NSE:ADANIPORTS-EQ)
confidence: 45
reasoning: Newly live Next.js App-Router routes (option-chain, strategy-builder/explore, screeners, symbol pages) render 200 for anonymous users; their _next static chunks are served as 200 text/html, so the backing JSON API is only reachable after source-grep. No endpoint/auth evidence in context yet.
evidence_needed: a JSON API baseURL/fetch target extracted from page JS that answers symbol/options queries with no session and no 403.
verify_steps: PASSIVE: `curl -s https://www.fyers.in/web/options/option-chain | grep -oE 'https?://[a-z0-9.-]+\.fyers\.in/[^"]+'` (repeat for /web/symbol/NSE:ADANIPORTS-EQ), then `curl -s -i <first discovered endpoint>` with no auth.
impact: unauthenticated market/analytics aggregation surface; Low-Medium unless an endpoint touches account data.
testability: AUTH_HELPED
[HYP] Dev-tier margin/basket APIs referenced by prod ordwin bundle are reachable with blank token_id
class: MISCONFIG
asset: api.fyers.in/anjuna/v1/margin, api.fyers.in/fydev/v1/baskets, data.fyers.in/dev-fyers/mobileapi/user-settings
confidence: 45
reasoning: Prod helper_min.js (ordwin 4.6) embeds dev routes incl. fydev/v1/baskets?token_id= and anjuna/v1/margin with token passed as URL query param; all first-party *.fyers.in hosts in scope. Prior fydev/v1 + vagator/v1 refs (broker/12.1) remain unverified.
evidence_needed: GET with blank/missing token_id returns JSON data or schema/error detail distinct from an auth wall (not 401/403 HTML).
verify_steps: AUTH_HELPED: `curl -s -i https://api.fyers.in/anjuna/v1/margin` ; `curl -s -i "https://api.fyers.in/fydev/v1/baskets?token_id="` ; `curl -s -i https://data.fyers.in/dev-fyers/mobileapi/user-settings`
impact: unauthenticated margin/basket/dev-settings visibility or internal schema/error disclosure; Medium if data returned.
testability: AUTH_HELPED
[HYP] SGB app trusts un-prefixed localStorage auth_token as bearer on live /orders, /details
class: AUTH
asset: sgb.fyers.in (/orders, /details, /updatesgb)
confidence: 50
reasoning: Bundle c930e9b6... reads auth_token from localStorage and sets it verbatim as the Authorization header (no Bearer scheme prefix); live SGB app pages return 200. If the SGB API is scheme-agnostic or does not strictly validate the token, the client-side gate is the only control.
evidence_needed: /orders or /details returns account data with no/dummy Authorization, or tolerates a malformed scheme while a valid token still works.
verify_steps: AUTH_HELPED: `curl -s -i https://sgb.fyers.in/orders` with no header, with `Authorization: <dummy>`, and `Authorization: Bearer <dummy>`; compare 200-data vs 401. Never persist a real token (hash-only logging).
impact: unauthorized read of SGB holdings/orders if authz is client-gated only; High.
testability: AUTH_HELPED
[PARKED] community.fyers.in GUEST JWT: public-by-design guest token (tokenType=GUEST, entityId/permissions null, ~4h expiry) — dropped, not a finding.
[PARKED] ipo.fyers.in / sgb.fyers.in APP_ID/client_id + appIdHash map (incl. new AEHNSK9PRW): public OAuth identifiers and their hashes — dropped.
[PARKED] www.fyers.in / trade.fyers.in GA4 G-JXG5NQ1WQJ, GTM-MB6PRVDG, G-NTFX8XLKVH, Zoho formperma: public analytics/forms keys — dropped.
[PARKED] verifiedpnl main.78f0294e.js `AIza[0-9A-Za-z_-]{` truncated google_key regex: no full value, unverifiable — scanner noise, parked.
[PARKED] trade.fyers.in datafeed Fernet token_id (sha256 568d3b6a…34): demo/datafeed token in HISTORY_TEST; parked pending low-priority PASSIVE check.
[PARKED] 13.235.24.249:8080 /gtt/orders plaintext backend: third-party IP, out of scope.
[PARKED] webtrader.fyers.in / http://fyers.in / bo-login.fyers.in legacy JS: fetch 0 / unretrievable from this context.
[FINAL] 1) www.fyers.in webapp BUSLOGIC (conf 45, prio 6.65)  2) ordwin/4.6 dev-tier endpoints MISCONFIG (conf 45, prio 5.95)  3) sgb localStorage auth_token AUTH (conf 50, prio 5.60)
[NEXT] PROBE: `curl -s https://www.fyers.in/web/options/option-chain | grep -oE 'https?://[a-z0-9.-]+\.fyers\.in/[^"'"'"' ]+'` to enumerate the webapp JSON API; then `curl -s -i <first discovered endpoint>` unauthenticated. Run in parallel: `curl -s -i https://api.fyers.in/anjuna/v1/margin` and `curl -s -i "https://api.fyers.in/fydev/v1/baskets?token_id="` — all passive, read-only.
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js: GUEST JWT is public-by-design (guest claims, null perms) — class dead here.
[LEARN] REJECTED AUTH @ ipo.fyers.in / sgb.fyers.in env maps (incl. AEHNSK9PRW): client IDs + appIdHash are public OAuth identifiers, not secrets — class dead for hardcoded-APP_ID lead.
[LEARN] REJECTED OTHER @ www.fyers.in / trade.fyers.in marketing JS: only public GA4/GTM/Zoho keys — class dead on marketing surface.
[LEARN] REJECTED OTHER @ trade.fyers.in vendor JS (jquery, bootstrap, charts, revolution.extension): ApiKeydownHandler + "none" matches are scanner noise — no claim.
[RISK] fyers-js: 63 — prod bundles embed per-env OAuth client-ID/hash maps, a repeated demo Fernet token_id across 15+ datafeed bundles, a growing dev-tier API footprint (fydev, vagator, anjuna, api-socket) referenced from prod bundles with token_id in URL query, client-side-only auth_token gating on SGB, client-side _FYERS JWT gating on a financial endpoint, and a brand-new unanalyzable Next.js webapp surface — most items are low-impact or public-by-design, but the accumulation signals loose secret/auth hygiene across the trading surface, warranting AUTH_HELPED verification of the 3 survivors.
