# https://trade.fyers.in/static/js/orddetail/js/1.2/script.min.js
SECRET|other|auth_token referenced via global variable (defined externally, not in file)
ENDPOINT|GET|/orders/details
NOTE|Authorization header set to external global auth_token variable
NOTE|base URL is external global TRADEAPIURL variable (not embedded)
NOTE|order detail data injected into DOM via innerHTML from API response
NOTE|no hardcoded host/secrets present; credentials supplied at runtime
