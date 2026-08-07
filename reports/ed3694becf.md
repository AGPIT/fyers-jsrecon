# https://trade.fyers.in/static/js/init/4.0/fy_trade.min.js
SECRET|api_key|tokenId (user session token referenced in URL query string, value not in this file)
ENDPOINT|GET|https://data.fyers.in (UDFCompatibleDatafeed base)
ENDPOINT|GET|https://data.fyers.in/NSE/FO
ENDPOINT|GET|https://data.fyers.in/NSE/CM
ENDPOINT|GET|https://data.fyers.in/NSE/CD
ENDPOINT|GET|https://data.fyers.in/BSE/CM
ENDPOINT|GET|https://data.fyers.in/MCX/COM
ENDPOINT|GET|https://data.fyers.in/savechart
ENDPOINT|GET|https://data.fyers.in/snapshot
ENDPOINT|GET|https://data.fyers.in/mobileapi/get-user-settings?token_id=<tokenId>
ENDPOINT|GET|https://fundtransfer.fyers.in/v2/
ENDPOINT|GET|https://myaccount.fyers.in
ENDPOINT|GET|https://savedcharts.fyers.in
ENDPOINT|GET|https://alerts.fyers.in/dashboard/?symbol=
ENDPOINT|GET|https://fyers.gocharting.com
ENDPOINT|GET|https://tradingview.fyers.in/fundamentals/?company=
ENDPOINT|GET|https://tradingview.fyers.in/technicals/
ENDPOINT|GET|https://tradingview.fyers.in/economic-calendar/
ENDPOINT|GET|https://tradingview.fyers.in/forex/
ENDPOINT|GET|https://marketsmith.fyers.in/evaluation/
HOST|data.fyers.in
HOST|fundtransfer.fyers.in
HOST|myaccount.fyers.in
HOST|savedcharts.fyers.in
HOST|alerts.fyers.in
HOST|fyers.gocharting.com
HOST|tradingview.fyers.in
HOST|marketsmith.fyers.in
NOTE|User session token (tokenId) appended as query param `token_id` to get-user-settings AJAX call — token exposure in URLs, history, and proxy/access logs
NOTE|Charts storage uses charts_storage_api_version 1.2, client_id "trading_platform", charts_storage_url https://data.fyers.in/savechart
NOTE|TradingView widget library_path /lib/tvclib/1.19.0/, datafeed via UDFCompatibleDatafeed
NOTE|Default symbol NSE:NIFTY50-INDEX; timezone Asia/Kolkata; locale lang=en
