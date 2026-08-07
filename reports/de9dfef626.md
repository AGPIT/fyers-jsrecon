# https://trade.fyers.in/static/js/datafeed/udf/9.10/bundle.js
NOTE|sink:WebSocket in: new WebSocket(_0xd3dfx25a[_0x9487[300]].WS_URL
SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=
ENDPOINT|WS|wss://data.fyers.in/dataSock
ENDPOINT|GET|https://public.fyers.in/sym_details/
ENDPOINT|GET|{base}/config/
ENDPOINT|GET|{base}/symbols/V3/
ENDPOINT|GET|{base}/symbol_info
ENDPOINT|GET|{base}/search
ENDPOINT|GET|{base}/history/V4/
ENDPOINT|GET|{base}/quotes/V2/
ENDPOINT|GET|{base}/level2data/
HOST|data.fyers.in
HOST|public.fyers.in
NOTE|Fernet-format token (gAAAAA...) is a hardcoded credential-like value used as token_id header/query for the quotes/level2/history datafeed API; it is a dead string (index 304 unreferenced) in the obfuscation array but ships in the bundle
NOTE|REST base URL is injected at runtime via constructor (_datafeedUrl/_datafeedURL); only relative paths are hardcoded in this file
NOTE|WebSocket messages use protocol tags DATA_CONN, SUB_DATA, SUB_L2, SUBSCRIBE_TICKER, SUBSCRIBE_L2, UNSUBSCRIBE_*; binary packets decoded via getBigUint64/getInt32/getInt16 (tick/oi/diffoi/LTQ/L2_LTT)
NOTE|File is the TradingView UDF-compatible datafeed bundle (Datafeeds) bundling CryptoJS (AES/SHA/HMAC etc.); crypto usage carries no embedded secrets beyond the noted token
