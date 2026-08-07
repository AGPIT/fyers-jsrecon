# https://trade.fyers.in/static/js/datafeed/udf/9.18/bundle.js
ENDPOINT|ANY|/'&&(_0x90881d=
ENDPOINT|ANY|/'&&(_0x87d4a1=
NOTE|sink:WebSocket in: new WebSocket(_0x3309e7
SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=
ENDPOINT|GET|https://public.fyers.in/sym_details/{exchange}_{symbol}.zip
ENDPOINT|GET|config/
ENDPOINT|GET|history/V6/ (base URL configurable; adds ?token_id=)
ENDPOINT|GET|quotes/V2/ (adds ?token_id=)
ENDPOINT|GET|symbols/V3/ (adds ?token_id=)
ENDPOINT|GET|marks/V2/ (adds ?token_id=)
ENDPOINT|GET|search/V2/ (adds ?token_id=)
ENDPOINT|WS|wss://data.fyers.in/dataSock?token_id={token}
HOST|public.fyers.in
HOST|data.fyers.in
NOTE|Hardcoded Fernet token (gAAAAA prefix) used as default token_id in WebSocket HISTORY_TEST payload
NOTE|REST base URL not hardcoded; sendRequest() prefixes configurable _datafeedUrl to relative paths
NOTE|Auth relies on ?token_id= query param; secret_key read from localStorage (user session key, client-side)
NOTE|Bundle is TradingView UDF-compatible datafeed; includes bundled CryptoJS crypto library (standard)
