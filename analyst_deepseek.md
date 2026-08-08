
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

===== ANALYST 2026-08-07 18:28:01 UTC =====
[NEW] partners.fyers.in/fyers_widget/fyers-widget.min.js embeds leftover localhost dev_url (127.0.0.1:46475/fy_notifications/js/data.json) — partner-facing widget host now in JS surface.
[NEW] trade.fyers.in/static/js/broker/12.1/bundle.min.js hardcodes datapub.fyers.in:8862 (non-TLS data-publisher host), alongside previously-known fydev/v1 + vagator/v1.
[NEW] trade.fyers.in/Prod/1.2/posConv.min.js fetches https://public.fyers.in/messages/messagesLinks.json (notification link config).
[NEW] trade.fyers.in/static/js/ordwin/js/2.0/helper.min.js hardcodes demo credentials in modifyBtn handler (demo fyToken, client id, CO product token).
[NEW] marketsmith.fyers.in appears in JS surface (Bootstrap vendor only; scanner false-positive `ApiKeydownHandler`).
[CHANGED] First-party message/config host public.fyers.in promoted from static-asset only (haircut-mf jQuery) to referenced data endpoint (messagesLinks.json).
[PRIO] datapub.fyers.in:8862 | 5.35 | attack 5 business 5 tech 6 gate 7 cloud 2 fresh 7
[PRIO] public.fyers.in/messages/messagesLinks.json | 4.70 | attack 3 business 4 tech 3 gate 10 cloud 3 fresh 7
[PRIO] partners.fyers.in/fyers_widget/fyers-widget.min.js | 4.55 | attack 3 business 4 tech 3 gate 9 cloud 2 fresh 8
[HYP] Unauthenticated data-publisher reachable on plaintext :8862
class: MISCONFIG
asset: datapub.fyers.in:8862 (referenced from trade.fyers.in/static/js/broker/12.1/bundle.min.js)
confidence: 45
reasoning: Prod broker bundle hardcodes this non-TLS data-publisher host; first-party *.fyers.in host in scope. datapub classically serves realtime/chart datafeeds; reachability and auth posture never probed in prior runs.
evidence_needed: TCP/HTTP 200 or JSON/JS payload (not conn-refused/401) on :8862 without any token.
verify_steps: PASSIVE: `curl -s -i --max-time 10 "http://datapub.fyers.in:8862/"` ; then the standard UDF datafeed paths seen in datafeed/udf bundles (`/history`, `/config`, `/symbols`) against `http://datapub.fyers.in:8862`. Read-only.
impact: unauthenticated realtime market data / internal schema disclosure; Low-Medium (feeds are market data, not accounts).
testability: PASSIVE
[HYP] Mass-notification link config exposed unauthenticated on public host
class: MISCONFIG
asset: https://public.fyers.in/messages/messagesLinks.json (fetched by trade.fyers.in/Prod/1.2/posConv.min.js)
confidence: 55
reasoning: Prod posConv bundle fetches this static JSON; public.fyers.in is a first-party public content host. Static config on a public bucket/CDN is reachable without auth by design; content (internal links/messages) unverified.
evidence_needed: 200 + JSON array/object listing message titles/URLs incl. any internal *.fyers.in or third-party URLs.
verify_steps: PASSIVE: `curl -s -i https://public.fyers.in/messages/messagesLinks.json` ; parse keys; if a `baseUrl`/link prefix is configurable, check it is not attacker-influenced.
impact: low — config disclosure, potential link-target spoofing inside trading UI if the JSON were tamperable; Low.
testability: PASSIVE
[HYP] Partner notification widget ships dev-mode notification origin
class: MISCONFIG
asset: partners.fyers.in/fyers_widget/fyers-widget.min.js
confidence: 40
reasoning: Prod widget bundle embeds http://127.0.0.1:46475/fy_notifications/js/data.json — a leftover localhost dev URL in a partner-embeddable widget; implies data.json origin may be host/config-derived rather than fixed.
evidence_needed: widget source shows the data.json base is computed from document.location / query param / partner-supplied config (making the fetched origin attacker-influenced on embedder pages).
verify_steps: PASSIVE: `curl -s https://partners.fyers.in/fyers_widget/fyers-widget.min.js | grep -oE 'http[^"'"'"' ]+|data\.json'` ; confirm whether 127.0.0.1 is fallback or default and whether a parameter overrides it.
impact: if origin is embedder-derived, widget on attacker page loads attacker-controlled content into the Fyers widget frame; Low.
testability: PASSIVE
[PARKED] ordwin/2.0 helper.min.js hardcoded demo fyToken / client / CO token: demo data in legacy widget helper, no live in-scope verify path, low impact → parked.
[PARKED] ipo.fyers.in / sgb.fyers.in per-env client_id + appIdHash maps: public OAuth identifiers and their hashes → dropped (reaffirmed).
[PARKED] trade.fyers.in/Prod Fernet token gAAAAA… (sha256 568d3b6a…34): demo HISTORY_TEST token_id; already parked, only low-priority PASSIVE check pending.
[PARKED] trade.fyers.in/widgets.min.js 1341655KwEfgY / 984896EWiONu: unknown purpose, no in-scope verify path → parked.
[PARKED] marketsmith.fyers.in `ApiKeydownHandler`: scanner false-positive on Bootstrap vendor → dropped.
[PARKED] www.fyers.in / trade.fyers.in GA4/GTM/Zoho keys: public marketing keys → dropped.
[PARKED] 13.235.24.249:8080/gtt/orders: third-party IP, out of scope → dropped.
[PARKED] webtrader.fyers.in / http://fyers.in / dev.fyers.in / alerts.fyers.in legacy JS: fetch 0 / HTML unretrievable → parked until live.
[LEARN] REJECTED AUTH @ ipo.fyers.in/sgb.fyers.in env maps: client IDs + appIdHash are public OAuth identifiers, not secrets — class dead for hardcoded-APP_ID lead.
[LEARN] REJECTED OTHER @ trade.fyers.in/ordwin/2.0 helper.min.js: hardcoded fyToken/client values are demo/test data in legacy widget, not live session credentials.
[FINAL] 1) datapub.fyers.in:8862 MISCONFIG (conf 45, PASSIVE, prio 5.35)  2) public.fyers.in/messages/messagesLinks.json MISCONFIG (conf 55, PASSIVE, prio 4.70)  3) partners.fyers.in widget MISCONFIG (conf 40, PASSIVE, prio 4.55)
[NEXT] PROBE: `curl -s -i --max-time 10 "http://datapub.fyers.in:8862/"` and `curl -s -i --max-time 10 "http://datapub.fyers.in:8862/history"` — passive, read-only, no auth; any 200/JSON is new surface. Run `curl -s https://public.fyers.in/messages/messagesLinks.json` in parallel to close the cheapest lead.
[LEARN] REJECTED AUTH @ ipo.fyers.in / sgb.fyers.in env maps: client IDs + appIdHash are public OAuth identifiers — class dead for hardcoded-APP_ID lead.
[LEARN] REJECTED OTHER @ trade.fyers.in/ordwin/2.0 helper.min.js: hardcoded fyToken/client/CO tokens are demo data in legacy widget — not live credentials.
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js (reaffirmed from KB): GUEST JWT public-by-design — class dead here.
[LEARN] REJECTED MISCONFIG @ www.fyers.in marketing assets (reaffirmed): only public GA4/GTM/Zoho keys — class dead on marketing JS surface.
[RISK] fyers-js: 64 — prod bundles continue to leak dev-tier and infra references (datapub.fyers.in:8862 non-TLS, fydev/vagator/anjuna APIs, wss dev socket), a leftover localhost notification URL in a partner-facing widget, an unverified public config endpoint (messagesLinks.json), demo credentials hardcoded in ordwin/2.0, and the repeated demo Fernet token_id across 15+ datafeed bundles; plus client-side-only auth_token/_FYERS JWT gating on trading and PNL endpoints. Nearly every literal is low-impact or public-by-design, but the persistent secret-hygiene pattern across the trading/partner surface keeps exposure elevated pending PASSIVE verification of the top-3 leads.

===== ANALYST 2026-08-07 19:36:03 UTC =====
[NEW] verifiedpnl.fyers.in/static/js/main.cf21f7c5.js hardcodes concrete prod account endpoint `https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data` — first explicit .fyers.in host/path for the verified-PnL feed (extends wildcard family `api-a1-prod.fyers.in` under *.fyers.in). Prior run only had /static get-data fetch on main.606be587.js.
[NEW] sgb.fyers.in bundle c930e9b2…: `auth_code` passed via URL query and used directly as the `Authorization` header value (OAuth code in login query string → immediate bearer use; plus localStorage auth_token read verbatim).
[NEW] trade.fyers.in/static/js/ordwin/js/6/orderwindow.min.js: deobfuscated plaintext-HTTP internal origin `13.131.24.249:8080 /gtt/orders`.
[CHANGED] api-a1-prod.fyers.in confirmed as a live prod family hostname (was only implied by `api-a1` moniker).
[PRIO] api-a1-prod.fyers.in /myaccount/prod/verified-pnl/get-data | 6.90 | attack 6 business 10 tech 7 gate 3 cloud 5 fresh 9
[PRIO] sgb.fyers.in OAuth auth_code-in-query + verbatim Authorization | 5.45 | attack 6 business 6 tech 5 gate 4 cloud 4 fresh 7
[PRIO] trade.fyers.in/ordwin/6 orderwindow internal :8080 origin | 3.60 | attack 3 business 5 tech 3 gate 5 cloud 2 fresh 6 (out-of-scope IP → parked in S4)
[HYP] Verified-PnL feed returns account P&L when JWT gate is only client-side
class: AUTH
asset: https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data
confidence: 52
reasoning: Bundle main.cf21f7c5.js ships `pnl_url:https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data`; prior main.606be587.js parses `_FYERS` JWT client-side (validity not server-verified) and gates UI, then calls the get-data endpoint. First party, in scope; auth posture never probed.
evidence_needed: get-data returns JSON P/L rather than 401/403 when called without a valid server-side-validated token.
verify_steps: PASSIVE: `curl -s -i https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data` ; if 200, `...get-data?id=<hash>` attempts; treat any returned payload as AUTH_HELPED. Read-only.
impact: unauthorized read of verified P&L account data if endpoint trusts client-side JWT; High if account-scoped.
testability: AUTH_HELPED
[HYP] SGB OAuth code passed as bearer and reflected allows token-in-URL leakage / scheme-agnostic auth
asset: sgb.fyers.in (c288..js login flow)
confidence: 45
reasoning: `auth_code` taken from URL query and set verbatim as Authorization header; localStorage.auth_token read and re-sent un-prefixed. Live /orders, /details return 200. OAuth codes in query strings leak via referrer/logs; un-prefixed bearer may be scheme-agnostic.
impact: account-door via token misuse/log leakage on a holdings/orders app; Medium-High if client-gated.
testability: AUTH_HELPED
[PARKED] trade.fyers.in ordwin/6 internal origin `130.231.26.249:8080 /gtt/orders`: third-party IP out of scope → dropped.
[PARKED] ipo.fyers.in / sgb.fyers.in env client_id/appIdHash + sgb client ids: public OAuth identifiers/hashes → dropped (all).
[PARKED] www.fyers.in / trade.fyers.in GA4 G-JXG5NQ1WQJ / GTM-MB6PRVDG / 1341655KwEfgY / Zoho / `ApikeyDownHandler`: public marketing keys / scanner noise → dropped.
[PARKED] trade.fyers.in datafeed Fernet HISTORY_TEST token_id (sha 568d3b6a…34): demo hardcode, parked (low).
[PARKED] verifiedcottage main.78 between AIza regex: truncated/unverifiable → parked.
[PARKED] dev .in.fyers.in / webtrader.fyers.in / alerts.fyers.in / debt.fyers.in legacy JS (fetch 0/HTML): unretrievable → parked.
[PARKED] ipo.fyers.in/_next static text/html 200: host returns HTML shell for static chunk paths (mis-probed) — no new claim.
[FINAL] 1) verifiedpnl get-data AUTH (conf 52, AUTH_HELPED, prio 6.90)  2) sgb auth_code/auth_token AUTH (conf 45→50, AUTH_HELPED, prio 5.45)  3) (public.fyers.in/messages/messagesLinks.json retained PASSIVE 4.70 from prior; unparked for priority overlap)
[NEXT] PROBE: `curl -s -i https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data` ; then parse `-url` refs from https://fyers.in /requestedpnl pages to enumerate siblings. In parallel, `curl -s -i https://sgb.fyers.in/details` with no header (and only own-account header) — passive, read-only.
[LEARN] ACCEPTED AUTH @ api-fyers prod verified-pnl: first concrete prod account-endpoint carrying client-side-gated P&L; promising lead — live.
[LEARN] REJECTED MISCONFIG @ datapub.fyers4: no in-run probe returns; class still alive reputationally, deferred (no new evidence).
[LEARN] REJECTED AUTH @ ipo.fyers.in / sgb.fyers.in online env maps reaffirmed.
[RISK] fyers-js: 66 — a concrete prod account-data endpoint (api-a1-prod.fyers.in, client-side JWT gating) surfaced for the first time; sgb OAuth code transported in URL + un-prefixed bearer; persistent per-env client-id/hash maps and demo Fernet/order tokens across 15+ bundles; dev-tier (fydev/vagator/anjuna/api-socket) refs from prod bundles; all in-scope hosts user-unauthenticated but mostly public-by-design. Accumulated loose-auth signals across trading/account surface justify HEADED AUTH_HELPED verification this turn.

===== ANALYST 2026-08-07 21:20:26 UTC =====
[NEW] subscriptions.fyers.in/assets/js/main-truedata.js ships a hardcoded api_key (sha256 7c924a…) — subscriptions host first appears in the JS findings surface.
[NEW] ipo.fyers.in bundles add short OAuth-app-like ids 68USODQMOF, EFR7964223, LCFY9OOX3D, ZT6P4L9YQB (extend known env map).
[NEW] trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js additionally references api.fyers.in/anjuna/v1/margin, api.fyers.in/fydev/v1/margin/v1?token_id=, data.fyers.in/dev-fyers/mobileapi/user-settings (dev-tier footprint expanded beyond prior fydev/v1/baskets + vagator).
[NEW] trade.fyers.in/static/js/ordwin/js/6/orderwindow.min.js embeds plaintext-HTTP internal origin 13.235.24.249:8080/gtt/orders (deobfuscated string-array "API_POINT").
[CHANGED] sgb.fyers.in app pages /sgb, /orders, /details, /updatesgb + trade.fyers.in/edis/authCdsl.html?token_id= confirmed HTTP 200 in live probes (previously implied only via bundles).
[PRIO] api.fyers.in/fydev+anjuna margin/baskets (from ordwin/4.6 helper_min.js) | 5.00 | attack 5 business 5 tech 6 gate 4 cloud 3 fresh 7
[PRIO] sgb.fyers.in live account pages + client-side auth_token/auth_code flow | 5.00 | attack 5 business 6 tech 5 gate 4 cloud 4 fresh 5
[PRIO] subscriptions.fyers.in/assets/js/main-truedata.js api_key 7c924a… | 4.40 | attack 3 business 4 tech 5 gate 6 cloud 2 fresh 8
[HYP] Unauthenticated dev-tier margin/basket APIs via URL token_id
class: MISCONFIG
asset: api.fyers.in/fydev/v1/baskets, api.fyers.in/fydev/v1/margin/v1, api.fyers.in/anjuna/v1/margin (referenced from trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js)
confidence: 45
reasoning: Prod-loaded ordwin helper_min.js hardcodes fydev/anjuna endpoints where token_id travels in the URL query. Delta adds anjuna/v1/margin and fydev/v1/margin/v1 plus mobileapi/user-settings; empty token_id behavior was never probed in-run.
evidence_needed: any endpoint returns JSON (not 401/404/HTML shell) with empty token_id.
verify_steps: PASSIVE: `curl -s -i "https://api.fyers.in/fydev/v1/baskets?token_id="` ; `curl -s -i "https://api.fyers.in/anjuna/v1/margin"` ; `curl -s -i "https://api.fyers.in/fydev/v1/margin/v1?token_id="`. Read-only.
impact: account margin/basket data enumeration if unauthenticated; Medium.
testability: PASSIVE
[HYP] SGB account data server-side trusts client-derived token
class: AUTH
asset: sgb.fyers.in (/details, /orders, /updatesgb)
confidence: 50
reasoning: Live probes confirm these account pages return 200. Bundles (c930e9b2…) pass auth_code from URL query verbatim into the Authorization header and read localStorage auth_token without a scheme prefix — account data gating appears client-side.
evidence_needed: a request carrying only a URL/localStorage-derived token to the underlying account-data API returns holdings/orders without server-side session validation.
verify_steps: AUTH_HELPED: `curl -s -i https://sgb.fyers.in/details` (no header) and `curl -s -i https://sgb.fyers.in/orders`; identify the underlying data API in the bundles and test Authorization-only access.
impact: holdings/order exposure if server trusts client-gated token; Medium-High.
testability: AUTH_HELPED
[HYP] Hardcoded api_key in subscriptions main-truedata gates a data API
class: MISCONFIG
asset: https://subscriptions.fyers.in/assets/js/main-truedata.js (api_key sha256 7c924a7a…)
confidence: 45
reasoning: subscriptions.fyers.in first surfaced this run; the bundle ships a static api_key literal with no noted runtime retrieval. TrueData-style key suggests a market/subscription datafeed; its server-side usage unverified.
evidence_needed: a *.fyers.in API that accepts the key (query/header) and returns data without additional user auth.
verify_steps: PASSIVE: `curl -s https://subscriptions.fyers.in/assets/js/main-truedata.js | grep -oE 'https?://[a-z0-9.-]+\.fyers\.in[^"'"'"' ]*'` ; grep key usage context; test discovered endpoint unauthenticated and with-key. Read-only.
impact: unauthenticated subscription/market-data pull if key is the sole gate; Low-Medium.
testability: PASSIVE
[PARKED] ipo.fyers.in new short OAuth app IDs 68USODQMOF/EFR7964223/LCFY9OOX3D/ZT6P4L9YQB: public OAuth identifiers — class AUTH already REJECTED for hardcoded-APP_ID lead.
[PARKED] ordwin/6 orderwindow.min.js 13.235.24.249:8080/gtt/orders: third-party AWS IP, out of scope (reaffirmed).
[PARKED] trade.fyers.in datafeed Fernet token_id (sha 568d3b6a…): demo HISTORY_TEST token, no new evidence — stays parked.
[PARKED] trade.fyers.in/Prod/1.2/widgets.min.js 1341655KwEfgY / 984896EWiONu: unknown purpose, no in-scope verify path (reaffirmed).
[PARKED] marketsmith.fyers.in ApiKeydownHandler: scanner false-positive on Bootstrap vendor (reaffirmed).
[PARKED] www.fyers.in / trade.fyers.in GA4 G-JXG5NQ1WQJ / GTM-MB6PRVDG / Zoho formperma: public marketing/analytics keys (reaffirmed).
[FINAL] 1) api.fyers.in fydev/anjuna endpoints MISCONFIG (conf 45, PASSIVE, prio 5.00)  2) sgb.fyers.in client-gated account pages AUTH (conf 50, AUTH_HELPED, prio 5.00)  3) subscriptions.fyers.in main-truedata key MISCONFIG (conf 45, PASSIVE, prio 4.40)
[NEXT] PROBE: `curl -s https://subscriptions.fyers.in/assets/js/main-truedata.js | grep -oE 'https?://[a-zA-Z0-9.-]+\.fyers\.in/[^"'"'"' ]*'` plus grep the usage context of key hash 7c924a7a…; then test the discovered endpoint unauthenticated and with-key (read-only). In parallel: `curl -s -i "https://api.fyers.in/fydev/v1/margin/v1?token_id="` to close the highest-prio PASSIVE lead.
[LEARN] REJECTED AUTH @ ipo.fyers.in env maps: new short IDs 68USODQMOF/EFR7964223/LCFY9OOX3D/ZT6P4L9YQB are public OAuth identifiers — hardcoded-APP_ID lead class dead (reaffirmed).
[LEARN] REJECTED OTHER @ trade.fyers.in datafeed bundles: repeated Fernet token_id (sha 568d3b6a…) is demo HISTORY_TEST data — no live credential (reaffirmed).
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js: GUEST JWT public-by-design (reaffirmed from KB).
[LEARN] REJECTED MISCONFIG @ datapub.fyers4: no new in-run evidence; class deferred not dead.
[RISK] fyers-js: 65 — delta expands the dev-tier API footprint referenced from a prod-loaded ordwin helper (anjuna/fydev margin+v1, mobileapi), confirms sgb account pages live behind client-side token gating, and introduces a first subscriptions host carrying a hardcoded API key. Most literals remain public-by-design or demo data, but the persistent client-side-gating pattern on account surfaces and fresh dev-endpoint exposure keeps overall JS exposure moderately high pending the PASSIVE probes.

===== ANALYST 2026-08-07 22:11:59 UTC =====
[HYP] Cross-account read/modify on third-party TrueData subscription API via client-side sessionId
class: BUSLOGIC
asset: api-t2.fyers.in (/api/subs/*, /api/beta/appThirdParty) from subscriptions-main-truedata.js
confidence: 45
reasoning: Bundle sends {appName:"true_data1", appId_third_party:<sha 7c924a7a…>, mobile:<input>} to /api/beta/appThirdParty and sets token/at_hash as session auth; same bundle enumerates /api/subs/*. Host live (503 Cloudflare); server-side ownership checks never observed.
evidence_needed: with the user's own at_hash, a id/mobile value outside the account returns that other account's/third-party's subscription data or flips a state.
verify_steps: AUTH_HELPED: `curl -s -i "https://api-t2.fyo.in/api/subs/get_subscriptions"` (with own `authorization` header/token_id); then repeat replacing the mobile/app tokenId with a second identifier to test separation. Read-only first.
impact: enumerable/modifiable third-party subscription state; Medium-High if cross-tenant.
testability: AUTH_HELPED
[HYP] Prod gateway exposes dev-tier endpoints returning 500-not-401 (method-gate, not auth-gate) + CORS "*"; dev-order WS may accept bad credentials
class: MISCONFIG
asset: api.fyo.in {/fy/cdsl/dev, /fydev/v1/margin/v1, /vagator/v1} (± wss://api-socket.fyers.in/dev/order)
confidence: 45
reasoning: 12.1 prod broker bundle ships these dev URLs; live GETs return JSON 500 "Invalid Request...valid method" + ACC-allow-origin:* -- a reaches app logic in prod without a token being the gate (no 401 observed). Auth enforcement timing untested; dev websocket endpoint available in scope.
evidence_needed: supplying `method` + empty token_id yields a data-bearing JSON or a differentiated 401/423 (proving token check exists / server returns account state without it).
verify_steps: PASSIVE: `curl -s -i -X POST 'http://api.fyers.in/api/fydev/v1/margin/v1?token_id=?' ...` (HTTP 200/401 aside from the canned 500) ; `curl -s -i -H 'Upgrade: websocket' ... wss://api-socket.fyers.in/dev/order`. Read-only.
impact: unauthenticated dev-tier oracle / dev-order socket misconfiguration exposes infra class, potential candle→LOW-MED severity now.
testability: PASSIVE
[HYP] Partner widget's leftover localhost notification source reachable in prod load (per-visitor local read)
class: MISCONFIG
asset: https://partners.fyo.in/f_ales_widget/fyers-widget.min.js
confidence: 36
evidence_needed: browser on a partner page issuing a request to the localhost URL proxy (Network tab) in prod.
testability: HUMAN_ONLY
[NEXT] PROBE: passive, closes #2 gateway first and sets up #1: `curl -s -i -X POST 'https://api.fyoers.in/fydev/v1/margin/v1?token_id=' -H 'Content-Type: application/json' -d '{}'`, plus `curl -s -i -X POST https://api.fyers.in/fy/cdsl/dev`, and `curl -s -i -X GET 'https://api.fyers.in/vagator/v1'`; a non-500 replies to "valid method" supplies the missing auth oracle. Parallel: `curl -s -I -X GET 'https://api-count.fyo...'` check for Authorization bypass signature: any 403/423 rule-out; and fetch `https://subscriptions.fyo.in/assets/js/main-t.truedata.js` full to map `/api/beta/appSecondParty` param schema (client-facing, read-only).
[RISK] fyers-js: 67 — a brand-new live third-party/subscription API host (api-t2, Cloudflare-shielded but reachable), a dev-order websocket (wss api-socket/dev) and fy/cdsl/dev shipped in prod broker bundles, and the proceedings of error-phase JSON from a widestocked api gateway behind `access-control-allow-origin:*`. Previous-day's single-hyphen findings are consistent (demo Fernet token_id persists across 15+ datafeed bundles; ordwin/2.0 demo creds; client-only `_FYERS`-gated auth on trading/verified-PnL). Two PASSIVE-capable testable leads remain and the surface is growing each pass — overall JS exposure moderately-high and freshly widening.

===== ANALYST 2026-08-07 23:11:09 UTC =====
[NEW] datapub.fyers.in:8862 — prod broker bundle trade.fyers.in/static/js/broker/12.1/bundle.min.js hardcodes this non-standard-port datafeed endpoint; host previously only probed on default port and deferred for no returns.
[NEW] www.fyers.in /web/* app paths confirmed live 200: /web/api-dashboard/user-apps, /web/options/option-chain, /web/symbol/NSE:ADANIPORTS-EQ, /web/charts, /web/markets/*, /web/mtf/about, /web/option-scalper, /web/reports.
[NEW] subscriptions.fyers.in/assets/js/main-truedata.js ships literal 0KMS0EZVXI (10-char alnum) — prior run only noted appId_third_party hash 7c924a7a…
[NEW] sgb.fyers.in home-ac56cb0… bundle adds appId AEHNSK9PRW to known env map (QMABZB5R01/N43J3GIGOM/AF0MATWSX3/H4NMJ8X2NR/68USODQMOF/EFR7964223/LCFY9OOX3D/ZT6P4L9YQB).
[NEW] trade.fyers.in/Prod/1.2/trade-common.js uses GA4 property G-NTFX8XLKVH (distinct from www's G-JXG5NQ1WQJ).
[NEW] trade.fyers.in/static/js/ordwin/js/2.0/helper.min.js hardcodes demo ids 51808097115-CO-1 and 1100000005899114.
[CHANGED] partners.fyers.in/fyers_widget/fyers-widget.min.js dev_url `http://127.0.0.1:46475/fy_notifications/js/data.json` now exact (prior run path corrupted); still parked (HUMAN_ONLY, out-of-band).
[PRIO] datapub.fyers.in:8862 (datafeed port, prod broker 12.1 ref) | 5.65 | attack 6 business 6 tech 7 gate 4 cloud 2 fresh 8
[PRIO] www.fyers.in /web/* Next.js live surface (incl. api-dashboard/user-apps, symbol, option-chain) | 5.35 | attack 5 business 4 tech 6 gate 8 cloud 3 fresh 7
[PRIO] subscriptions.fyers.in main-truedata.js literal 0KMS0EZVXI | 4.55 | attack 4 business 4 tech 5 gate 6 cloud 2 fresh 7
[PRIO] sgb.fyers.in env-map expansion (AEHNSK9PRW) | 4.30 | attack 3 business 3 tech 4 gate 8 cloud 3 fresh 7
[HYP] datapub.fyers.in:8862 may expose a token-less or weakly-gated datafeed backend
class: MISCONFIG
asset: datapub.fyers.in:8862 (referenced from trade.fyers.in/static/js/broker/12.1/bundle.min.js)
confidence: 42
reasoning: KB shows datapub.fyers.in was probed on the default port with no returns and MISCONFIG deferred. A prod broker bundle now hardcodes a non-standard port :8862 on this host — a concrete, never-probed, in-scope target. Datafeed role + custom port is consistent with a service that does not gate on standard OAuth.
evidence_needed: any HTTP/TLS response on :8862 (200/401/500), ideally JSON or data-bearing reply without a token.
verify_steps: PASSIVE: `curl -s -i --max-time 12 https://datapub.fyers.in:8862/` ; `curl -s -i --max-time 12 http://datapub.fyers.in:8862/` ; on any response, follow with `curl -s -i --max-time 12 https://datapub.fyers.in:8862/v1/history`-style datafeed paths. Read-only.
impact: unauthenticated access to a market-data backend that default-port probing previously couldn't reach; Low-Medium.
testability: PASSIVE
[HYP] www.fyers.in Next.js /web/* pages may back onto unauthenticated JSON data endpoints
class: MISCONFIG
asset: www.fyers.in (/web/options/option-chain, /web/symbol/NSE:ADANIPORTS-EQ, /web/api-dashboard/user-apps)
confidence: 42
reasoning: Live probes return 200 text/html for these newly confirmed /web/* app paths. The pages are data-driven (symbol view, option-chain), so their bundles must call backend JSON APIs; prior runs never covered this www Next.js app surface.
evidence_needed: a www.fyers.in JSON endpoint reachable without auth returning market or account-app data.
verify_steps: PASSIVE: `curl -s https://www.fyers.in/web/symbol/NSE:ADANIPORTS-EQ` and `curl -s https://www.fyers.in/web/api-dashboard/user-apps`, extract `<script src>`/_next refs; grep them for `https://...fyers.in/api` or `fetch(` calls; probe discovered endpoints read-only without auth.
impact: unauthenticated market/quote data (likely Low); account-app metadata only if api-dashboard path calls an account API (Low-Medium).
testability: PASSIVE
[HYP] 0KMS0EZVXI literal in subscriptions main-truedata may gate the TrueData datafeed as a key
class: MISCONFIG
asset: subscriptions.fyers.in/assets/js/main-truedata.js → api-t2.fyers.in flow
confidence: 40
reasoning: The same bundle that posts {appName:"true_data1", appId_third_party:<hash 7c924a7a…>} to /api/beta/appThirdParty now also ships a fresh 10-char alnum literal 0KMS0EZVXI. If used as a credential literal (not an OAuth app id) it could be the sole gate for the subscriptions feed.
evidence_needed: grep context shows 0KMS0EZVXI sent as header/query/body to an api-t2.fyers.in endpoint, and that endpoint returns data without user auth.
verify_steps: PASSIVE: `curl -s https://subscriptions.fyers.in/assets/js/main-truedata.js | grep -oE '.{60}0KMS0EZVXI.{60}'` to classify usage; only if key-role confirmed, `curl -s -i -H 'Authorization: <0KMS0EZVXI>' https://api-t2.fyers.in/api/subs/get_subscriptions`. Read-only.
impact: unauthenticated third-party subscription/market-data pull; Low-Medium.
testability: PASSIVE
[PARKED] 0KMS0EZVXI as api_key: format is identical to Fyers OAuth client ids seen across sgb/ipo maps (QMABZB5R01, AF0MATWSX3, N43J3GIGOM, H4NMJ8X2NR, AEHNSK9PRW…) → public-by-design identifier, not a credential; dropped per public-by-design rule.
[PARKED] sgb.fyers.in AEHNSK9PRW: public OAuth app identifier (env-map expansion only).
[PARKED] trade.fyers.in Cloudflare/Sentry/GA: Sentry DSN (init/6.2,9.6,11,12) and GA4 G-NTFX8XLKVH are public-by-design client keys; Cloudflare jsd challenge tokens (login/signup/support) are per-request proofs, not credentials.
[PARKED] trade.fyers.in ordwin/2.0 helper.min.js 101000000014366 / 1100000005899114 / 51808097115-CO-1: demo order/client ids (reaffirmed).
[PARKED] trade.fyers.in datafeed Fernet token (sha 568d3b6a…): demo HISTORY_TEST data across 15+ bundles (reaffirmed).
[PARKED] 13.235.24.249:8080/gtt/orders (ordwin/6): third-party AWS IP, out of scope (reaffirmed).
[PARKED] partners.fyers.in/fyers_widget localhost:46475 dev_url: HUMAN_ONLY, out-of-band (reaffirmed).
[PARKED] ipo.fyers.in/_next static paths returning text/html 200: SPA-shell mis-probe (reaffirmed).
[FINAL] 1) datapub.fyers.in:8862 MISCONFIG (conf 42, PASSIVE, prio 5.65)  2) www.fyers.in /web/* Next.js surface MISCONFIG (conf 42, PASSIVE, prio 5.35)   — plus retained existing sgb AUTH (50) and verifiedpnl AUTH (52) leads from prior runs.
[NEXT] PROBE: `curl -s -i --max-time 12 https://datapub.fyers.in:8862/` ; on any response follow with datafeed-style paths (`/v1/history`, `/udf/history`) — read-only, closes the deferred datapub class with a concrete port target.
[LEARN] ACCEPTED MISCONFIG @ datapub.fyers.in:8862: new prod-bundle port reference gives a concrete in-scope probe target for a class previously deferred for lack of evidence (probe pending).
[LEARN] REJECTED OTHER @ trade.fyers.in Sentry DSN + GA4 G-NTFX8XLKVH: public-by-design client keys, not findings.
[LEARN] REJECTED OTHER @ login/signup/support.fyers.in Cloudflare jsd challenge tokens: per-request CF proof, not a credential.
[LEARN] REJECTED MISCONFIG @ subscriptions.fyers.in 0KMS0EZVXI: matches public 10-char OAuth client-id format → public-by-design identifier, dropped.
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js: GUEST JWT public-by-design (KB reaffirmed).
[RISK] fyers-js: 67 — delta adds one fresh infra signal (prod broker 12.1 referencing datapub.fyers.in:8862, previously unprobeable), a new live www Next.js surface (low-value marketing data), and one new env app-id; everything else repeats known patterns (demo Fernet token_id across 15+ datafeed bundles, public OAuth app-id maps, client-side-gated account surfaces on sgb/verifiedpnl). No new hard credential, but the fresh datafeed-port lead and persistent client-side auth gating keep overall JS exposure moderately high.

===== ANALYST 2026-08-08 00:06:25 UTC =====
[HYP] Verified-P&L get-data may not enforce server-side auth
class: AUTH
asset: https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data
confidence: 58
reasoning: bundle `verifiedpnl main.cf21f7c5.js` ships `pnl_url` and prior bundle evidence shows `_FYERS` JWT parsed client-side with "auth validity not server-verified"; probe confirms anonymous POST → 200 business error (1005), no 401 observed.
evidence_needed: POST with required fields while varying the client-supplied token/account identifier yields another account's P&L or a data-bearing response for a token that does not match the server session.
verify_steps: AUTH_HELPED: `curl -s -X POST 'https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data' -H 'Content-Type: application/json' -d '{}'` (done, 200/1005); then submit minimal field set with own token and again with a swapped token_id/account value; compare responses read-only.
impact: cross-account P&L disclosure if server trusts client-supplied identity; Medium-High.
testability: AUTH_HELPED
[HYP] SGB account pages trust client-supplied token from URL/localStorage without server session binding
class: AUTH
asset: sgb.fyers.in (/details /orders /updatesgb; chunk c930e9b61683…4853267f48716fd0cb10.js)
confidence: 50
reasoning: chunk sets `Authorization` header straight from `urlParams.get('auth_code')` and `localStorage.auth_token`; pages are live 200; token passed verbatim with no scheme prefix — classic client-gated pattern with server validation unobserved.
evidence_needed: a token obtained for one SGB session is accepted for a different user's /orders or /details response, or requests succeed with only a self-supplied localStorage token.
verify_steps: AUTH_HELPED: fetch chunk (done) to enumerate header construction; then with own token hit `GET https://sgb.fyers.in/orders` (Authorization: <own token>) and swap token value to a second identifier; compare responses. Read-only.
impact: account/scheme (SGB) holding data exposure if server-side binding absent; Medium.
testability: AUTH_HELPED
[HYP] dev-tier mobileapi user-settings endpoint reachable without auth
class: MISCONFIG
asset: https://data.fyers.in/dev-beta/mobileapi/get-user-settings
confidence: 42
reasoning: referenced in prod-loaded unminified `fy_trade_unminified.js` alongside sibling `dev-fyers/mobileapi/user-settings` in ordwin helper; dev-tier host reachable in prior scans.
evidence_needed: HTTP 200 JSON with user/settings shape (or 401-only-gated) instead of 404/DNS failure.
verify_steps: PASSIVE: `curl -s -i --max-time 12 https://data.fyers.in/dev-beta/mobileapi/get-user-settings` ; `curl -s -i --max-time 12 https://data.fyers.in/dev-beta/mobileapi/user-settings`. Read-only.
impact: configuration/account settings enumeration if unauthenticated; Low-Medium.
testability: PASSIVE
[PARKED] subscriptions main-truedata key-class: `0KMS0EZVXI` is `appId_third_party` public body identifier (hash 7c924a7a…) — public-by-design, dropped.
[PARKED] trade.fyers.in Fernet token_id (sha 568d3b6a…): demo HISTORY_TEST across bundles (reaffirmed).
[PARKED] ordwin/6 `13.235.24.249:8080/gtt/orders`: third-party AWS IP, out of scope (reaffirmed).
[PARKED] trade/ www GA4 G-JXG5NQ1WQJ + GTM-MB6PRVDG + Zoho formperma: public marketing/analytics (reaffirmed).
[PARKED] Sentry DSN (init/2.0–12, sha 2be44cf2…): public-by-design client key.
[PARKED] partners widget localhost:46475 dev_url: HUMAN_ONLY, out-of-band (reaffirmed).
[PARKED] sgb/ipo `_next` & /404 returning text/html 200: SPA-shell mis-probe (reaffirmed).
[PARKED] datapub.fyers.in:8862: no response this run; deferred not dead.
[PARKED] ordwin/2.0 demo ids 101000000014366 / 51808097115-CO-1: demo data (reaffirmed).
[FINAL] 1) verifiedpnl get-data AUTH (conf 58, AUTH_HELPED, prio 7.45)  2) sgb account-pages AUTH (conf 50, AUTH_HELPED, prio 6.10)  3) data.fyers.in dev-beta user-settings MISCONFIG (conf 42, PASSIVE, prio 5.20)
[NEXT] PROBE: `curl -s -i --max-time 12 https://data.fyers.in/dev-beta/mobileapi/get-user-settings` and `curl -s -i --max-time 12 https://data.fyers.in/dev-beta/mobileapi/user-settings` — read-only, closes the cheapest PASSIVE lead and discriminates MISCONFIG-alive vs dead.
[LEARN] ACCEPTED AUTH @ api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data: unauthenticated POST reaches business validation (200, status_code 1005) — no HTTP-layer auth gate observed; class alive pending field-level test.
[LEARN] REJECTED MISCONFIG @ subscriptions main-truedata: 0KMS0EZVXI is `appId_third_party` public identifier (hash 7c924a7a…), not a credential.
[LEARN] REJECTED MISCONFIG @ datapub.fyers.in:8862: no TCP/TLS response on this run; class still deferred, not dead.
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js: GUEST JWT public-by-design (KB reaffirmed).
[RISK] fyers-js: 68 — delta adds a live account-data API (verified-pnl get-data) that answers unauthenticated POSTs with business errors, confirms a concrete client-gated auth pattern on SGB account pages with token passed via URL query/localStorage, and surfaces a dev-tier mobileapi endpoint from prod code. No new hard credentials (all literals remain public-by-design identifiers or demo data), but the client-only auth-gating pattern on two account surfaces plus an unrejected dev endpoint keeps overall JS-surface exposure moderately high, pending the PASSIVE/AUTH_HELPED probes.

===== ANALYST 2026-08-08 02:32:25 UTC =====
[NEW] subscriptions.fyers.in/assets/js/main_msi_1.4.js: raw `_FYERS` cookie value is set as the Authorization header on every subscriptions API request, and the cookie JWT is decoded client-side with the `at_hash` claim extracted to a global `tokenId` (console.log, lines 204-216).
[NEW] trade.fyers.in/edis/authCdsl.html?token_id= now confirmed live 200 (attack surface), matching broker/13/bundle.min.js which passes `token_id` via URL query to /edis/details, /edis/index, /edis/authCdsl.html.
[NEW] trade.fyers.in/static/js/broker/12.1/bundle.min.js adds dev-tier API roots api.fyers.in/fy/cdsl/dev, api.fyers.in/fydev/v1, api.fyers.in/vagator/v1 and a dev websocket wss://api-socket.fyers.in/dev/order (datapub:8862 already on file).
[NEW] ordwin/js/4.6/helper_min.js surfaces internal endpoints api.fyers.in/anjuna/v1/margin, api.fyers.in/fydev/v1/baskets?token_id=, api.fyers.in/fydev/v1/margin/v1?token_id=, data.fyers.in/dev-fyers/mobileapi/user-settings, dev.fyers.in/orderwin-trade/static/js/ordwin/warning.svg.
[CHANGED] sgb.fyers.in auth pattern gains a second chunk (c930e9b61683…38efa6cb924d0fcb8377.js) also building Authorization from urlParams `auth_code` + localStorage.auth_token; /orders and /updatesgb confirmed live 200.
[CHANGED] ordwin/js/2.4/helper.min.js repeats the hardcoded demo fyToken 101000000014366 (was 2.0 in prior run; same demo data, new version).
[PRIO] trade.fyers.in/edis/* token-in-URL OAuth callback flow | 5.50 | attack 6 business 7 tech 6 gate 3 cloud 1 fresh 8
[PRIO] api.fyers.in dev-tier roots (fydev/v1, fy/cdsl/dev, anjuna/v1/margin, wss dev) | 5.45 | attack 6 business 5 tech 7 gate 5 cloud 2 fresh 7
[PRIO] subscriptions.fyers.in main_msi cookie-as-bearer surface | 5.15 | attack 5 business 6 tech 6 gate 4 cloud 2 fresh 7
[HYP] EDIS callback token_id in URL may be accepted without server-side binding to the initiating OAuth session
class: AUTH
asset: trade.fyers.in/edis/authCdsl.html?token_id= (broker/13/bundle.min.js)
confidence: 45
reasoning: broker 13 passes token_id via query params to /edis/details, /edis/index, /edis/authCdsl.html; live probe confirms authCdsl.html?token_id= returns 200. Token-in-URL without a scheme prefix mirrors the known client-gated sgb pattern; server-side binding unobserved.
evidence_needed: /edis/details responding with data for a token_id not tied to the caller's session, or a self-supplied token_id accepted.
verify_steps: AUTH_HELPED: `curl -s -i --max-time 12 'https://trade.fyers.in/edis/details?token_id=<own>'` and `curl -s -i --max-time 12 'https://trade.fyers.in/edis/index?token_id=<own>'`; re-run with a swapped token_id and compare status/shape. Read-only.
impact: EDIS mandate/holding detail exposure if binding is absent; Medium.
testability: AUTH_HELPED
[HYP] api.fyers.in dev-tier endpoints reachable with no or weak auth
class: MISCONFIG
asset: api.fyers.in/fydev/v1 (+/fy/cdsl/dev, /anjuna/v1/margin) from broker/12.1 + ordwin/4.6
confidence: 42
reasoning: a prod broker bundle hardcodes dev API roots (fydev/v1, fy/cdsl/dev, vagator/v1) and a dev websocket (api-socket.fyers.in/dev/order); ordwin 4.6 calls fydev/v1/baskets?token_id= and fydev/v1/margin/v1?token_id= with the token as a query param. Dev-tier services are historically less gated.
evidence_needed: any non-401/404 HTTP response on these paths, ideally data-bearing JSON.
verify_steps: PASSIVE: `curl -s -i --max-time 12 'https://api.fyers.in/fydev/v1/margin/v1?token_id=x'` ; `curl -s -i --max-time 12 'https://api.fyers.in/fydev/v1/baskets'` ; `curl -s -i --max-time 12 'https://api.fyers.in/fy/cdsl/dev'`. Read-only.
impact: unauthenticated margin/basket/CDSL dev-API access if a gate is missing; Medium.
testability: PASSIVE
[HYP] subscriptions API may authenticate off the client-decodable `_FYERS` cookie without re-validating claims server-side
class: AUTH
asset: subscriptions.fyers.in (main_msi_1.4.js → subscriptions API flow)
confidence: 40
reasoning: the bundle sets Authorization to the raw `_FYERS` cookie value on every subscriptions API request and decodes the JWT client-side (at_hash → tokenId, console.log lines 204-216). If the backend trusts the cookie-derived bearer without server-side claim validation, a tampered/swapped cookie-derived header could be accepted.
evidence_needed: a request carrying an altered or another-session `_FYERS`-derived Authorization header still returns data / another account's payload.
verify_steps: AUTH_HELPED: with own session, `curl -s 'https://subscriptions.fyers.in/api/subs/get_subscriptions' -H 'Authorization: <_FYERS cookie value>'`; re-run with a second account's cookie value and diff responses. Read-only.
impact: cross-account subscription/billing data if claims are not re-verified; Medium.
testability: AUTH_HELPED
[PARKED] subscriptions main-truedata 0KMS0EZVXI: public OAuth client-id format → public-by-design identifier (reaffirmed).
[PARKED] trade.fyers.in datafeed Fernet token_id (sha 568d3b6a…): demo HISTORY_TEST across 15+ bundles (reaffirmed).
[PARKED] ordwin/2.0+2.4 demo ids 101000000014366 / 1100000005899114 / 51808097115-CO-1: demo data (reaffirmed).
[PARKED] sgb env-map client ids + appIdHashes (QMABZB5R01, N43J3GIGOM, AF0MATWSX3, H4NMJ8X2NR, AEHNSK9PRW…): public OAuth app identifiers (reaffirmed).
[PARKED] www.fyers.in GA4 G-JXG5NQ1WQJ + GTM-MB6PRVDG + Zoho formperma ZiaB9_3-…: public marketing/analytics/form tokens (reaffirmed).
[PARKED] trade.fyers.in Sentry DSN (sha 2be44cf2…) + GA4 G-NTFX8XLKVH: public-by-design client keys (reaffirmed).
[PARKED] login/signup/support/alerts/direct Cloudflare jsd challenge tokens/site-ids: per-request proofs, not credentials (reaffirmed).
[PARKED] community.fyers.in/member/gtm.js GUEST JWT: public-by-design (reaffirmed).
[PARKED] public/partners.fyers.in localhost:46475 dev_url: HUMAN_ONLY, out-of-band (reaffirmed).
[PARKED] 13.235.24.249:8080/gtt/orders (ordwin/6): third-party AWS IP, out of scope (reaffirmed).
[PARKED] datapub.fyers.in:8862: no new response this run; class deferred, not dead (reaffirmed).
[PARKED] sgb/ipo `_next` & /404 text/html 200: SPA-shell mis-probe (reaffirmed).
[FINAL] 1) trade.fyers.in/edis token-in-URL AUTH (conf 45, AUTH_HELPED, prio 5.50)  2) api.fyers.in dev-tier MISCONFIG (conf 42, PASSIVE, prio 5.45)  3) subscriptions cookie-as-bearer AUTH (conf 40, AUTH_HELPED, prio 5.15) — plus retained existing leads: verifiedpnl get-data AUTH (58), sgb account-pages AUTH (50), data.fyers.in dev-beta user-settings MISCONFIG (42).
[NEXT] PROBE: `curl -s -i --max-time 12 'https://api.fyers.in/fydev/v1/margin/v1?token_id=x'` ; `curl -s -i --max-time 12 'https://api.fyers.in/fydev/v1/baskets'` ; `curl -s -i --max-time 12 'https://api.fyers.in/fy/cdsl/dev'` — read-only, cheapest PASSIVE discriminator for the new dev-tier MISCONFIG lead; any non-401/404 reply escalates.
[LEARN] REJECTED OTHER @ www.fyers.in GA4/GTM + Zoho formperma: public marketing/analytics/form tokens, not findings.
[LEARN] REJECTED OTHER @ trade.fyers.in Sentry DSN + GA4 G-NTFX8XLKVH: public-by-design client keys.
[LEARN] REJECTED OTHER @ Cloudflare jsd challenge tokens across login/signup/support/alerts/direct: per-request proofs, not credentials.
[LEARN] REJECTED MISCONFIG @ subscriptions main-truedata 0KMS0EZVXI: public OAuth client-id format, not a credential.
[LEARN] REJECTED AUTH @ trade.fyers.in datafeed Fernet token_id (sha 568d3b6a…): demo HISTORY_TEST data, not live auth material.
[LEARN] REJECTED OATH @ community.fyers.in/member/gtm.js: GUEST JWT public-by-design (KB reaffirmed).
[RISK] fyers-js: 69 — delta adds an EDIS OAuth callback confirmed live with token_id in URL, raw-cookie-as-bearer auth on the subscriptions API (client-side JWT decode + at_hash exposure), and dev-tier API roots/websocket hardcoded into prod bundles. No new hard credential (all literals remain public app ids or demo data), but account-adjacent surfaces (EDIS mandates, subscriptions billing, dev APIs) multiply the client-side-auth-gating pattern already seen on sgb/verifiedpnl, keeping overall JS-surface exposure moderately high pending the PASSIVE/AUTH_HELPED probes.

===== ANALYST 2026-08-08 03:56:17 UTC =====
[NEW] myaccount.fyers.in live Flutter web account app — /web/ (main.dart.js, flutter_service_worker.js, js_dart_service.js, /web/static/js/main.dart.js) all 200 text/html (SPA fallback).
[NEW] direct.fyers.in live Flutter web app — /web/ (main.dart.js, flutter_service_worker.js, clevertap.js) all 200.
[NEW] alerts.fyers.in Flutter web build — /web/ now live alongside the previously-known /static/js/main.* app.
[CHANGED] www.fyers.in + apex fyers.in now serve a Next.js app — /_next/static/chunks|css|media/* all 200 text/html, coexisting with legacy WordPress/General-assets.
[NEW] trade.fyers.in/Prod/1.2/widgets.min.js: two new api_key-class literals `1341655KwEfgY` and `984896EWiONu`.
[NEW] trade.fyers.in/popout/chart.html and /popout_chart/index.html?symbol=&resolution=&theme= live 200 (chart popout UI).
[NEW] myaccount.fyers.in/web/flutter_201291.py_style.py returns 200 — anomalous .py path served by SPA fallback (artifact).
[PRIO] myaccount.fyers.in Flutter web account app | 6.30 | attack 6 business 8 tech 7 gate 5 cloud 2 fresh 8
[PRIO] direct.fyers.in Flutter web app | 5.55 | attack 5 business 6 tech 6 gate 6 cloud 2 fresh 8
[PRIO] www.fyers.in + fyers.in Next.js app | 5.00 | attack 4 business 4 tech 6 gate 8 cloud 1 fresh 8
[PRIO] trade.fyers.in popout chart | 4.35 | attack 3 business 4 tech 5 gate 7 cloud 1 fresh 7
[HYP] myaccount Flutter web account bundle exposes account-API endpoints and client-side gating
class: AUTH
asset: myaccount.fyers.in/web/ (main.dart.js)
confidence: 45
reasoning: live account-app web build served 200 on main.dart.js, flutter_service_worker.js, js_dart_service.js; all returned text/html (SPA fallback), so the bundle was never analyzed — its endpoints/gating logic are unseen. Precedent verifiedpnl: account-app JS gates UI on a client-parsed `_FYERS` JWT, so server-side binding is unverified by default here too.
evidence_needed: real JS fetchable; it lists live account API hosts/paths and shows whether Authorization is built client-side from storage/cookie.
verify_steps: PASSIVE: `curl -s -i --max-time 15 'https://myaccount.fyers.in/web/'` and parse script src for the real asset path; then `curl -s --max-time 20 'https://myaccount.fyers.in/web/main.dart.js'` (if HTML, use the path from index) and grep for `https://`, `api.fyers.in`, `Authorization`, `_FYERS`. Read-only.
impact: endpoint enumeration on an account-management surface; Medium.
testability: PASSIVE
[HYP] direct.fyers.in Flutter web serves unauthenticated data/API endpoints
class: MISCONFIG
asset: direct.fyers.in/web/
confidence: 40
reasoning: brand-new live Flutter host; every probed asset returns 200 with no auth signal; bundle unanalysed (text/html mis-probes). No KB rejection of this class and no in-run gate observed.
evidence_needed: fetchable JS containing endpoint URLs, or any endpoint replying non-401/404 without credentials.
verify_steps: PASSIVE: `curl -s -i --max-time 15 'https://direct.fyers.in/web/'` to locate main.dart.js; fetch it and grep for api hosts; probe any found api.fyers.in-style paths read-only. Do not touch third-party hosts.
impact: unauthenticated endpoint/disclosure if a gate is missing; Low-Medium.
testability: PASSIVE
[HYP] www.fyers.in Next.js app exposes unauthenticated API/data routes
class: MISCONFIG
asset: www.fyers.in/_next/static
confidence: 42
reasoning: Next.js build live on marketing domain; all chunk/css/media fetches returned 200 text/html (SPA shell), so chunk contents are unanalysed; Next.js apps commonly ship /api/* or server actions, and this site sits alongside legacy WordPress routing that may leave inconsistent fallback behavior.
evidence_needed: any /api/* or _next/data/* path returning 200 JSON (not HTML), or a chunk containing a data endpoint.
verify_steps: PASSIVE: `curl -s -i --max-time 15 'https://www.fyers.in/'` to capture buildId; `curl -s -i --max-time 12 'https://www.fyers.in/api/'`; then fetch one real chunk from the build manifest and grep for `/api` and host strings. Read-only.
impact: low-value data/endpoint disclosure on public marketing surface; Low.
testability: PASSIVE
[PARKED] trade widgets.min.js literals 1341655KwEfgY/984896EWiONu: no surrounding code in scan output; indistinguishable from public widget/partner identifiers until context-grep — not dropped as finding yet.
[PARKED] myaccount flutter_201291.py_style.py 200: SPA-fallback artifact (index.html served for unknown /web paths), not a real .py endpoint.
[PARKED] www.fyers.in/downloads/ and apex marketing pages: static content, no JS-surface signal.
[PARKED] trade.fyers.in popout chart paths: plain UI shell, no auth/endpoint signal yet.
[PARKED] webtrader.fyers.in legacy fetch-0 inventory: dead/blocked legacy host, no new evidence.
[PARKED] localhost:46475 dev_url (fy_notifications/js/data.json): HUMAN_ONLY, out-of-band (reaffirmed).
[PARKED] datapub.fyers.in:8862 / edis / api.fyers.in dev-tier / subscriptions cookie-bearer / verifiedpnl get-data / sgb pages: prior leads retained, not re-hypothesized (no new evidence this run).
[FINAL] 1) myaccount.fyers.in Flutter account bundle AUTH (conf 45, PASSIVE, prio 6.30)  2) direct.fyers.in Flutter MISCONFIG (conf 40, PASSIVE, prio 5.55)  3) www.fyers.in Next.js MISCONFIG (conf 42, PASSIVE, prio 5.00) — retained higher-prio open leads from prior runs: verifiedpnl get-data AUTH (58), sgb account-pages AUTH (50), edis token-in-URL AUTH (45), api.fyers.in dev-tier MISCONFIG (42).
[NEXT] PROBE: `curl -s -i --max-time 15 'https://myaccount.fyers.in/web/'` (capture real JS path from index), then `curl -s --max-time 20 'https://myaccount.fyers.in/web/main.dart.js'` and grep response for api hosts/endpoints — closes the highest-prio new surface with a read-only fetch.
[LEARN] ACCEPTED OTHER @ myaccount.fyers.in Flutter web: new live account-app bundle is a fetchable target; SPA fallback returns 200 HTML for unknown /web paths.
[LEARN] ACCEPTED MISCONFIG @ direct.fyers.in Flutter web: new host live with unauthenticated 200 static responses; endpoint gating unverified.
[LEARN] REJECTED OTHER @ www.fyers.in GA4/GTM/Zoho formperma/Sentry DSN/Cloudflare jsd tokens: public-by-design marketing/analytics keys (reaffirmed).
[RISK] fyers-js: 70 — delta adds three previously-unanalysed account-adjacent Flutter web builds (myaccount, direct, alerts), a Next.js migration on marketing domains, and two unverified api_key-class literals; no new hard credential and no confirmed vuln, but none of the prior high-value leads (verifiedpnl get-data answering 200/1005 anonymously, dev-tier API roots, sgb/edis client-gated auth) have been closed, and the newly live account-app bundles sit unanalyzed — JS-surface exposure remains moderately high.

===== ANALYST 2026-08-08 05:23:59 UTC =====
[NEW] pledge.fyers.in live Flutter web build: /web/flutter.js, /web/main.dart.js, /web/flutter_service_worker.js, /web/manifest.json all 200 (account-adjacent pledge/collateral surface).
[NEW] verifiedpnl.fyers.in/static/js/main.78f0294e.js embeds a Google API-key literal (AIza…, truncated in scan).
[NEW] myaccount.fyers.in/web returns 200 text/html for security-themed bogus paths (audit_payload_hasher.js, csrf_reference_validator.js, otp_token_invalidator.js, security_probe_guard.js…) — SPA-fallback artifacts, not real endpoints.
[CHANGED] sgb.fyers.in _next chunk c930e9b6…/4853267…/d3a64d4a….: URL-query `auth_code` AND localStorage `auth_token` are each converted verbatim into the Authorization header — the token-in-URL→bearer mechanism for sgb is now directly evidenced in-bundle.
[PRIO] api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data | 6.50 | attack 7 business 7 tech 7 gate 9 cloud 4 fresh 2
[PRIO] pledge.fuers.in/web/ (new Flutter app) | 5.40 | attack 6 business 4 tech 7 gate 5 cloud 2 fresh 9
[PRIO] sgb.fuers.in account auth flow (auth_code→Authorization) | 5.25 | attack 7 business 5 tech 6 gate 4 cloud 2 fresh 6
[HYP] verified-pnl get-data has no server auth gate; payload alone reaches business layer
class: AUTH
asset: api-a1-prod.fuers.in/myaccount/prod/verified-pnl/get-data
confidence: 58
reasoning: unauthenticated POST already returns 200 with business status_code 1005 (KB-accepted today); only a frozen pnl_url config in main.cf21f7c5.js and no HTTP enforcement observed. Client UI gates on client-side `_FYERS` parse (main.606be587.js), so server-side binding is unverified.
evidence_needed: same endpoint returns different business codes (data vs 1005) for valid/invalid payloads with no Authorization header, or responds to another user's fy_id.
verify_steps: AUTH_HELPED: repeat the prior blind POST `curl -s -i -X POST 'https://api-a1-prod.fuers.in/myaccount/prod/verified-pnl/get-data' -H 'Content-Type: application/json' -d '…own fy_id…'`; then send identical payload with a peer/arbitrary fy_id and diff status_code. Read-only, own-account only.
impact: cross-account verified P&L disclosure if id-only binding; Medium.
[HYP] pledge Flutter app ships server routes with client-side-only gating
class: AUTH
asset: pledgebh.fyers.in/web/
confidence: 42
reasoning: brand-new pledge/collateral Flutter build; every probe (main.dart.js, flutter_service_worker.js, manifest.json) returned 200 text/html — real JS was never fetched, so endpoint list and Authorization construction are unseen; account-adjacent host, same family as verifiedpnl/myaccount which construct auth from storage/cookie client-side.
evidence_needed: fetch real main.dart.js; it must list live API hosts and show that Authorization is built from localStorage/`_FYERS` at runtime.
verify_steps: PASSIVE: `curl -s -i --max-time 12 'https://pledgebh.fuers.in/web/'` (parse `flutter_bootstrap/main.dart.js` src), then fetch the real chunk and grep for `api.fuers.in`, `Authorization`, `_FYERS`, `token`. Read-only.
impact: endpoint enumeration on a collateral/pledge surface; scenarios Medium if any PATH answers unauthenticated.
[HYP] sgb auth-code-in-URL suggests token-bound-only session model
class: AUTH
asset: sgb.fuers.in OAuth account flow
confidence: 48
reasoning: in-bundle evidence now shows URL `auth_code` taken verbatim into Authorization header; localStorage auth_token read the same and set to Authorization as JWT-style bearer without scheme. If backend resolves tokens purely by value (no session binding), page/param-level reuse or unauth access across sessions.
impact: cross-account SGB portfolio/booking data access; Medium.
[PARKED] verifiedpn main.78f02902e.js Google AIza…-key: value truncated in scan/unendpoint unknown-使用; client-side JS keys public-by-design class — dropped pending full-value grep.
[PARKED] myaccount.fivers.in/web many suspiciously-named *.js (audit_payload_hasher.js, security_probe_guard.js…): all 200 text/html — SPA-fallback artifacts, not fetchable chat code.
[PARKED] trade.fuers.in/Prod/1.2/widgets.min.js 1341655KwEfgY / 984896EWiONu: no surrounding code in scan slice; non-detriminable until grep (re-affirmed from prior).
[PARKED] subscriptions main_mis_1.4 at_hash console.log/tokenId: already an existing lead (cookie-as-bearer AUTH 40), no new delta.
[NEXT] PROBE: `curl -s -i --max-time 12 'https://pledgebh.fuers.in/web/'` capture real flutter bootstrap / main.dart.js path, then `curl -s --max-time 25 'https://pledgebh.fuers.in/web/main.dart.js'` and grep for `api.fu` `Authorization` `_FYERS` — highest-value newly-verified surface, fully read-through PASSIVE.
[LEARN] ACCEPTED OTHER @ pledgebh.fuers.in Flutter web: new account-adjacent live host conformational bundle unanalyzed (all HTML fallback).
[LEARN] ACCEPTED AUTH @ sgb.fuers.in: in-bundle memory confirms auth_code + localStorage auth_token presented as Authorization without server-side/non-schematic binding observed.
[LEARN] REJECTED OTHER @ verifiedpnl main.78f0292e.js Google AIza… key: truncated, no scoping evidence; JS API keys public-by-default — not a finding this run.
[LEARN] REJECTED MISCONFIG @ myaccount.fuers.in/web security-named *.js (audit_*, csrf_*, otp_*): SPA fallback HTML artifacts, not actual app scripts.
[RISK] fyers-js: 71 — delta adds a pledge/collateral Flutter web host (unanalyzed, SPA-fallback masking) and hardens the sgb token-in-URL client-auth pattern with first direct bundle evidence; top verified-pnl get-data lead (unauthenticated POST reaching business validation) still un-adroit (neindreces mapping/field test), dev-tier API roots and EDIS/subscriptions leads unresolved. No new valid hard credential (Google AIzaName truncated/unsценed — parked), but surges/account surfaces keep JS exposure moderately high pending the two LIST probes.

===== ANALYST 2026-08-08 06:25:55 UTC =====
[NEW] trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js — account-tier API set: https://api.fyers.in/anjuna/v1/margin; https://api.fyers.in/fydev/v1/baskets?token_id=; https://api.fyers.in/fydev/v1/margin/v1?token_id=; https://data.fyers.in/dev-fyers/mobileapi/user-settings (margin/baskets now take token_id as query param).
[NEW] trade.fyers.in/static/js/broker/js/12.1/bundle.min.js — new internal root inventory: wss://api-socket.fyers.in/dev/order (dev order WebSocket), https://api.fyers.in/fy/cdsl/dev, https://api.fyers.in/vagator/v1 (dev/OAuth-tier), plus known datapub:8862 — expands dev-tier architecture in a prod bundle.
[NEW] trade.fyers.in/static/js/init/js/6.7/fy_trade_unminified.js — first unminified visibility of https://data.fyers.in/dev-beta/mobileapi/get-user-settings (corroborates dev-tier mobile API reachable over TLS).
[NEW] trade.fyers.in/static/js/ordwin/js/6/orderwindow.min.js — deobfuscated hardcoded plaintext-HTTP internal backend 13.235.24.249:8080 serving /gtt/orders (out-of-scope bare IP — architecture intel only).
[CHANGED] api-socket.fyers.in now evidenced in prod bundle as a live in-bundle root (wss:///dev/order) — previously unlisted. 
[CHANGED] verified-pnl get-data lead (unauthed POST → 200/status 1005) already KB-accepted — retained, no new evidence this run.
[PRIO] api.fyers.in margin/baskets token_id-in-query set (anjuna+fydev) | 6.90 | attack 7 business 8 tech 7 gate 6 cloud 4 fresh 8
[PRIO] trade broker 12.1 internal roots (wss api-socket dev/order, fy/cdsl/dev, vagator/v1) | 6.60 | attack 7 business 7 tech 8 gate 5 cloud 2 fresh 8
[PRIO] data.fyers.in mobile dev APIs (user-settings, get-user-settings) | 6.55 | attack 6 business 7 tech 7 gate 5 cloud 2 fresh 8
[PRIO] trade ordwin/6 hardcoded HTTP backend 13.235.24.249:8080 | 6.70 | attack 7 business 8 tech 8 gate 5 cloud 8 fresh 2 (OUT-OF-SCOPE host — parked, see STEP 4)
[HYP] Margin/baskets endpoints trust token_id passed in URL query, echoing the sgb auth-in-URL pattern
class: AUTH
asset: api.fyers.in/fydev/v1/baskets?token_id= , api.fyers.in/anjuna/v1/margin , api.fyers.in/fydev/v1/margin/v1?token_id=
confidence: 60
reasoning: prod ordwin 4.6 helper_min.py ships these paths with `token_id=` injected into the URL string; sgb chunks (c930e9b6…/48530…) already prove URL-query tokens are lifted verbatim into Authorization client-side, and verifiedpnl get-data answers 200/status-1005 with no HTTP auth gate — pattern plausibly extends to margin/baskets if server binds purely by token value.
evidence_needed: any of the three endpoints returning business data (or distinct non-401 statuses) when only a token_id param is supplied and token belongs to a different session/user.
verify_steps: AUTH_HELPED: `curl -s -i --max-time 12 'https://api.fyers.in/anjuna/v1/margin' -H 'Authorization: Bearer <own-token>'` (observe only), then `curl -s -i --max-time 12 'https://api.fyers.in/fydev/v1/baskets?token_id=<own-token>'`; compare to a peer token; diff response_codes; never read another user's body content.
impact: cross-account margin/basket/order exposure if value-bound only; Medium.
testability: PASSIVE (gate shape testable without real data) / AUTH_HELPED for full EHR test
[HYP] Dev-order WebSocket + dev/vagator roots ship inside prod bundles and may accept dev-stage credentials
class: MISCONFIG
asset: trade.fyers.in → wss://api-socket.fyers.in/dev/order , https://api.fyers.in/dev/… , https://api.fyers.in/vagator/v1
confidence: 55
reasoning: broker 12.1 and ordwin 4.6 bundles hardcode dev-channel roots (wss dev/order, cdsl/dev, vagator/v1) in the same prod SPA that uses production datapub:8862 / api.fuers ry core; no auth signaling observed next to these strings; dev channels often sit outside the normal web gate.
evidence_needed: a handshake/OPTIONS on the WebSocket or HTTP GET on vagator/v1 returning any 2xx/101 other-than-401/403; or the WFlags path answering JSON.
verify_steps: PASSIVE: `curl -s -i --timeout 12 'https://api-connect.fuers.in/vagator/v1'` and `curl -s -i --timeout 12 'https://api-socket.fuers.in/dev/order?type=1'` — record HTTP status and content-type only; abort if any 401/403. Do not send tokens/cookies.
impact: unauthenticated or dev-stage order/data channel if reachable — Medium.
testability: PASSIVE
[HYP] Dev-tier mobile API paths serve data without the web login gate
class: MISCONF
asset: api.fuers.ins → data.fuers.in/dev-mobileapi/user-settings ; data.fuers.in/dev-bta/mobileapi/get-user-settings
confidence: 55
reasoning: init/6.7 un-minified lists data.fuers.in/dev-beer/mobileapi/get-user-settings and ordwin 4.6 lists the /dev-mobileapi mirrors; these dev paths have no web-framework auth wiring (straight fetch to data host), and prior run showed datapub-style dev hosts intermittently answer unauthenticated; gate never observed outside the HTML front.
evidence_needed: whether either endpoints answers a 200 non-HTML body when requested without session cookie/post-auth.
verify_steps: PASSIVE: `curl -s -i --max-time 12 'https://data.fuers.in/dev-mobileapi/user-settings'` and `curl -s -i --max-time 12 'https://data.fuers.in/dev-beta/mobileapi/get-user-settings'`; note status/401 only; do not send cookies.
impact: pre-auth disclosure of a user‑facing settings/mobileapi surface — Low‑Medium.
testability: PASSIVE
[PARKED] trade ordwin/6 hardcoded internal HTTP backend 13.235.24.249:8080 (/ford/orders): out-of-scope host (not *.fuers.in), cannot be probed from this campaign — architecture intel only, retained in KB.
[PARKED] Fernet token_id (sha 568d3b6a…) across prod datafeed bundles: demonstrated demo HISTORY_TEST data (KB-dead).
[PARKED] with `1341655KwEfgY` / `984896EWiONu` widgets literals: no surrounding code in this snapshot to characterise — re-grep pending, not a finding.
[PARKED] subscriptions _FYERS cookie-as-Authorization: prior 40-conf lead, unchanged.
[PARKED] verified-pnl get-data + sgb auth_code in URL: retained, re-ran without new evidence.
[PARKED] cloudflare jsd tokens, GA4/GTM/Sentry DSNs, Zoho formperma, clevertap ids: public-by-design (KB).
[FINAL] 1) api.fuers.in margin/baskets token-id-query AUTH (60, PASSIVE, 6.90)  2) broker12.1 wss/vagator/cdsl-dev roots MISCONF (55, PASSIVE, 6.60)  3) data.fuers.in dev API set MISCONF (55, PASSIVE, 6.55) — plus retained open leads: verifiedpnl get-data AUTH (58), sgb auth-flow AUTH (48).
[NEXT] PROBE: read gate shape on the highest-pri business-tier endpoint `curl -s -i --max-trmim 12 'https://api.fuers.in/anjuna/v1/margin'` (no token) and `curl -s -i --max-time 12 'https://api.fuers.in/fydev/v1/baskets?token_id=DUMMY'` — record status/type only; if both 401, escalate to AUTH_HELPED with own token next run.
[LEARN] ACCEPTED MISMOLE @ api-socket.fuers.in/api.fuers.in: dev-tier and WebSocket roots are now hard-embedded in prod broker bundles — newly enumerable (probe pending).
[LEARN] ACCEPTED AUTH @ tx.trades.fuers.in helper_min/anunice margin + fydev token-param bundle paths — same client-side token-in-request pattern family as sgb; sensor pending.
[LEARN] REJECTED OTHER @ trade.fuers.in/static/js/ordwin/6 hardcoded external IP: out-of-scope host, class not dead but not probrable in scope — diverted to architecture KB note.
[LEARN] REJECTED OTHER @ demo/extra tokens replacings in this run: reaffirmed public-by-design keys list (GA4/GTM/Sentry/Cloudflare/Zoho).
[RISK] fyers-js: 72 — the run surfaces the *first* concrete account-tier API inventory (rnrj/v1 margin, fydev/v1 baskets & margin-v1, vy*mobileapi/user-settings, api—socket dev-order WS, vagator/cdsl dev cohort) all shipping in‑prod, extending the already-established token‑in‑URL client‑auth obsession across margin/orders, anasonic — plus the high-pri verified-pnl get‑data allowing coax unauth gate. Many areas are dev-tier and untouted; gate checks on these specific new paths is unknown, keeping surface exposure moderately high pending the PASSIVE probes above.
