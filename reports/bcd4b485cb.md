# https://subscriptions.fyers.in/assets/js/main_msi_1.4.js
NOTE|sink:atob in: atob(fy_cookie
SECRET|jwt|cookie `_FYERS` decoded client-side; `at_hash` claim extracted to global `tokenId` and logged via console.log (validate at lines 204-216)
SECRET|api_key|Authorization header set to raw `_FYERS` session cookie value on every subscriptions API request
ENDPOINT|GET|https://api.fyers.in/api/beta/subscriptions
ENDPOINT|POST|https://api.fyers.in/api/beta/subscriptions
ENDPOINT|GET|https://login.fyers.in/?cb={callback}
ENDPOINT|GET|https://subscriptions.fyers.in/status
ENDPOINT|GET|https://subscriptions.fyers.in/market-smith/
ENDPOINT|GET|https://subscriptions.fyers.in/true-data.html
ENDPOINT|GET|https://marketsmith.fyers.in/evaluation/
HOST|api.fyers.in
HOST|login.fyers.in
HOST|subscriptions.fyers.in
HOST|marketsmith.fyers.in
NOTE|Session persistence: cookie identified by name `_FYERS`; absence redirects to login.fyers.in
NOTE|Client trusts `subscriptions` API `data` string parsed with JSON.parse without schema validation
NOTE|`sub_global_id`/`plan_global_code` (caller-supplied) passed into `alert()` in activateSubscriptionApi() -> potential DOM-based alert/XSS sink
NOTE|`getCookie` handles only urlencoded cookies; token decoding `/` and `+` replacement is partial (no padding fix for base64url)
NOTE|Plan codes hardcoded: apibridge_m_1, msi_quarterly, msi_yearly, td_plan_a1/b/c
NOTE|Error-code compare mismatch: string `"-22"` vs numeric `-22` across subscription handlers
NOTE|Redirect destinations (status, market-smith, true-data, evaluation) are hardcoded full URLs
NOTE|client: `startApiBridge`/`startMarketSmith` call `validate('_FYERS')` before API use; on missing cookie forced external redirect
