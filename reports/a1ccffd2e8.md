# https://trade.fyers.in/static/js/common/4.1/fy_common.min.js
ENDPOINT|ANY|/watchlist/web
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_watchlistFlag",!1
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_watchlistFlag",!0
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_instantOrderFlag",!1
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_instantOrderFlag",!0
NOTE|sink:localStorage in: localStorage.getItem("fyerstrade_watchlistFlag"
NOTE|sink:atob in: atob(fy_cookie
SECRET|jwt|_FYERS cookie (JWT) - payload parsed: at_hash (used as token_id), poa_flag
ENDPOINT|GET|https://api.fyers.in/fydev/v1/watchlist/web
ENDPOINT|GET|https://data.fyers.in/dev-fyers/chartSettings/?token_id={tokenId}
ENDPOINT|POST|https://data.fyers.in/dev-fyers/chartSettings/
ENDPOINT|DELETE|https://data.fyers.in/dev-fyers/chartSettings/
HOST|api.fyers.in
HOST|data.fyers.in
HOST|login.fyers.in
NOTE|Authorization header set from _FYERS cookie token on all API calls
NOTE|Settings endpoint path contains dev-fyers, a dev/chart-settings API
NOTE|sendS3Request makes cross-domain GET requests with no auth headers
NOTE|loginURL var defined but not invoked in this file
