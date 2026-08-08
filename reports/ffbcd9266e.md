# https://marketsmith.fyers.in/assets/js/marketSmith.js
ENDPOINT|ANY|/evaluation/Evaluation.html
NOTE|sink:innerHTML in: .innerHTML = userState), "Premium" == userState ? ((document.getElemen
NOTE|sink:innerHTML in: .innerHTML = "Error"), (window.location = login_url + origin + "/evaluation/Evaluation.html"
NOTE|sink:innerHTML in: .innerHTML = user.userState), "Premium" === user.userState ? ((document.ge
NOTE|sink:innerHTML in: .innerHTML = uid)
NOTE|sink:atob in: atob(fy_cookie
NOTE|sink:atob in: atob(base64
SECRET|jwt|_FYERS cookie JWT (base64url payload decoded via atob in extractFyersIDFromToken, fy_id claim)
SECRET|api_key|authToken forwarded in query string to marketsmithindia.com by generateMSIToken
ENDPOINT|GET|https://api.fyers.in/api/beta/get_msiuser_details
ENDPOINT|GET|https://public.fyers.in/sym_details/BSE_CM.json
ENDPOINT|GET|https://marketsmithindia.com/mstool/fyers/generateMSIToken
ENDPOINT|GET|https://marketsmithindia.com/mstool/fyers/deleteMSIToken
HOST|api.fyers.in
HOST|public.fyers.in
HOST|login.fyers.in
HOST|login.fyers.co.in
HOST|login.fydev.tech
HOST|subscriptions.fyers.co.in
HOST|subscriptions.fydev.tech
HOST|subscriptions.fyers.in
HOST|marketsmithindia.com
HOST|app.fyers.in
NOTE|_FYERS cookie value used directly as Authorization header to api.fyers.in without validation
NOTE|Dev/staging URLs exposed (fydev.tech, subscriptions-dev.fyers.co.in, subscriptions-staging.fyers.co.in)
NOTE|JWT decoded client-side from cookie without signature verification
NOTE|authToken and userAgent sent to third-party marketsmithindia.com in query string (token leakage risk)
NOTE|login_url built by string concatenation without encoding (open redirect / injection surface)
NOTE|get_msiuser_details is an internal-looking beta API endpoint
NOTE|redirectUpgrade opens app.fyers.in/symbol via window.open
NOTE|msiIframe src set from msiUrl without allowlist check before assignment in symbolDataContent
