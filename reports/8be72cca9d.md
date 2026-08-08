# https://trade.fyers.in/Prod/1.2/logout.min.js
NOTE|Obfuscated with string-array + rotation (self-defending array, base64 fragments like 3248816GQxKWg) — no plaintext secrets
NOTE|Calls internal modules: FyTrade['exitPositionServer'](), broker['logoutUser'](), tradingContext['refreshTradingDetailsModal']()
NOTE|window['hawkeye'] feature flag gates TradeModules ResetPriceAlerts and FyTrade.exitPositionServer()
NOTE|Uses TradingView widget (tvWidget, 'tv_chart_container') and datafeed['resetCache']() / tvWidget refresh
NOTE|Window flags 'webChartFlag' and 'popoutChartFlag' control chart refresh flow; '#log-out-window', '#logout-modal', '#fy_overLay' UI selectors only
