# https://assets.fyers.in/Lib/hawkeye/hawkeye.js
NOTE|sink:localStorage in: localStorage.getItem('access_token'
NOTE|sink:localStorage in: localStorage.setItem('access_token', token
NOTE|sink:atob in: atob(tokenParts[1]
SECRET|jwt|localStorage.getItem('access_token') JWT with exp claim decoded via atob
ENDPOINT|POST|https://api-t1.fyers.in/fe_hwk_logs/log
ENDPOINT|GET|https://api-t1.fyers.in/fe_hwk_logs/generate-token
HOST|api-t1.fyers.in
NOTE|Token stored in localStorage and auto-regenerated on 401 expiry; offline mode skips sends
NOTE|401 handler retries log send recursively after token regen (potential loop)
NOTE|JWT is fetched client-side from generate-token endpoint and reused for log auth
NOTE|fyId param passed alongside msg in log payload
