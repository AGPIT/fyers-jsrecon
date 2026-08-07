# https://cdn.fyers.in/js/sdk/1.1.0/fyers-web-sdk-v3/index.min.js
ENDPOINT|ANY|/positions
ENDPOINT|ANY|/orders
ENDPOINT|ANY|/orders/sync
ENDPOINT|ANY|/multi-order/sync
ENDPOINT|ANY|/profile
ENDPOINT|ANY|/funds
ENDPOINT|ANY|/holdings
ENDPOINT|ANY|/tradebook
ENDPOINT|ANY|/marketStatus
ENDPOINT|ANY|/history
ENDPOINT|ANY|/quotes
ENDPOINT|ANY|/depth
ENDPOINT|ANY|/options-chain-v3
NOTE|sink:message listener in: addEventListener("message"
NOTE|sink:WebSocket in: new WebSocket(this.url,[t]
NOTE|sink:atob in: atob(n
ENDPOINT|POST|/api/v2/positions
ENDPOINT|POST|/api/v2/orders
ENDPOINT|POST|/api/v2/orders/sync
ENDPOINT|POST|/api/v2/multi-order/sync
ENDPOINT|POST|/api/v3/orders
ENDPOINT|POST|/api/v3/orders/sync
ENDPOINT|POST|/api/v3/multi-order/sync
ENDPOINT|POST|/api/v3/positions
ENDPOINT|POST|/data/symbol-token
ENDPOINT|POST|/depth
ENDPOINT|POST|/funds
ENDPOINT|POST|/history
ENDPOINT|POST|/holdings
ENDPOINT|POST|/marketStatus
ENDPOINT|POST|/options-chain-v3
ENDPOINT|POST|/profile
ENDPOINT|POST|/quotes
ENDPOINT|POST|/tradebook
HOST|api.fyers.in
HOST|api-t1.fyers.in
HOST|socket.fyers.in
NOTE|Client SDK only; auth passed by caller (access_token/secret_key), none hardcoded
NOTE|Supports production (api/v2) and preproduction (api/v3) endpoints in one build
NOTE|WSS trade socket ws://socket.fyers.in/trade/v3 and history socket wss://socket.fyers.in/hsm/v1-5/prod, client_id/auth not embedded
