# https://trade.fyers.in/static/js/datafeed/udf/9.11/bundle.js
NOTE|sink:WebSocket in: new WebSocket(_0x2e7fd7[_0x3ae6('0xaa'
SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=
ENDPOINT|GET|wss://data.fyers.in/dataSock (WebSocket) :: WS_URL hardcoded, used for realtime quotes/ticker
ENDPOINT|GET|https://public.fyers.in/sym_details/ (symbol metadata zip)
ENDPOINT|GET|{base}/config/
ENDPOINT|GET|{base}/time/
ENDPOINT|GET|{base}/symbols
ENDPOINT|GET|{base}/history/V4/
ENDPOINT|GET|{base}/quotes/V2/
ENDPOINT|GET|{base}/marks/V2/
ENDPOINT|GET|{base}/timescale_marks/
ENDPOINT|GET|{base}/level2data/
HOST|data.fyers.in
HOST|public.fyers.in
NOTE|Bundle is an obfuscated TradingView UDF datafeed + CryptoJS (AES/DES/RC4, EvpKDF/PasswordBasedCipher). The gAAAA... value is a Fernet-format token used as the WS message token_id; appears to be a client-embedded credential.
NOTE|Relative endpoints (config/time/symbols/history/quotes/marks/level2data) are appended to a runtime datafeed base URL; fetch() adds token_id from a global 'tokenId' variable to each request.
NOTE|'secret_key','Token','token_id','_key' strings are CryptoJS/code identifiers, not literal credentials; no AWS/GCP/GitHub keys or hardcoded JWT found.
