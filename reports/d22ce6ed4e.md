# https://assets.fyers.in/Lib/calculators/2.6/brokrage-calc.js
SECRET|other|COMMODITY_FUTURES,COMMODITY_OPTIONS,NSE_COMMODITY_FUTURES,NSE_COMMODITY_OPTIONS - brokerage rate configs (rates/stt/lot sizes), not credentials
ENDPOINT|POST|/trade/v3/spancalc
HOST|api-t1.fyers.in
NOTE|SpanCalculator.sendatekt.php block newText via $.ajax POST to spancalc; response fields individual_info/span/expo/total/benefit. Unused vars and dead code present (max_stop_loss_price_range parseFloat no-op; getEquityData returns BRL). No hardcoded secrets or credentials detected.
