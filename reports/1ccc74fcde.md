# https://verifiedpnl.fyers.in/static/js/main.606be587.js
ENDPOINT|ANY|/g,
ENDPOINT|ANY|/:id
NOTE|sink:new Function in: new Function("return this"
NOTE|sink:innerHTML in: .innerHTML=t
NOTE|sink:innerHTML in: .innerHTML="<svg>"+t.valueOf().toString()+"</svg>",t=se.firstChild
NOTE|sink:innerHTML in: .innerHTML="<script><\/script>",e=e.removeChild(e.firstChild)):"string"===typeof r.is?e=c.c
NOTE|sink:innerHTML in: .innerHTML=e
NOTE|sink:innerHTML in: .innerHTML=e),o}var c=Ot(e,n)
NOTE|sink:postMessage in: postMessage(null
ENDPOINT|POST|https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data
ENDPOINT|GET|https://login.fyers.in/?cb=https://verifiedpnl.fyers.in
HOST|api-a1-prod.fyers.in
HOST|api.fyers.in
HOST|alerts.fyers.in
HOST|trade.fyers.in
HOST|myaccount.fyers.in
HOST|login.fyers.in
HOST|insights.fyers.in
HOST|support.fyers.in
HOST|direct.fyers.in
HOST|thematic.fyers.in
HOST|ofs.fyers.in
HOST|pledge.fyers.in
HOST|ipo.fyers.in
HOST|assets.fyers.in
HOST|verifiedpnl.fyers.in
NOTE|Internal app API endpoint posts account verified-PnL data via post(Iv.pnl_url,e)
NOTE|Login flow is OAuth redirect to login.fyers.in with callback back to verifiedpnl
NOTE|Multiple fyers.in.sibling subdomains referenced; assets served from assets.fyers.in
NOTE|No exposed hardcoded secrets (api keys, tokens, credentials) found in the bundle
NOTE|sourcemap found: https://verifiedpnl.fyers.in/static/js/main.606be587.js.map (422 sources)
MAP SECRET|api_key|_FYERS (JWT session cookie parsed client-side in getUserDetails.js:33739, auth validity not server-verified; used to gate UI and sent to get-data endpoint)
MAP ENDPOINT|POST|https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data
MAP HOST|api-a1-prod.fyers.in
MAP HOST|login.fyers.in
MAP HOST|verifiedpnl.fyers.in
MAP NOTE|Auth flow relies solely on client-side decode of the `_FYERS` cookie (parseJwt.js:33786) checking `exp` only; comment in getUserDetails.js explicitly notes there are no authorized endpoints to validate the token server-side.
MAP NOTE|prod.js embeds production endpoints; no dev/staging/sandbox URLs present in bundle.
MAP NOTE|No hardcoded google/aws/github tokens, api keys, DB credentials, or private keys found in the 41k-line bundle.
