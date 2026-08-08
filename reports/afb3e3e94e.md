# https://trade.fyers.in/static/js/orddetail/js/1.1/script.min.js
ENDPOINT|ANY|/orders/details
ENDPOINT|GET|/orders/details
HOST|trade.fyers.in
NOTE|Order-details AJAX GET built as TRADEAPIURL+'/orders/details' with {orderId,segment,symbol}, contentType application/json, xhrFields withCredentials:true
NOTE|Response rows concatenated into HTML string and injected via .html()/#table append (DOM-style HTML injection risk if API fields are user-influenced)
NOTE|API fields include PAN_NO, CLIENT_ID, ORDER_VALIDITY, ORD_SOURCE_FLG - sensitive PII rendered client-side
NOTE|TRADEAPIURL is a runtime global defined outside this file; base host trade.fyers.in
