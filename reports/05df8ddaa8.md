# https://trade.fyers.in/Prod/1.2/trade-common.js
ENDPOINT|ANY|/profile/segments/mtf/enable
NOTE|sink:innerHTML in: .innerHTML=l(a.itemClassName,a.imageSrc,a.itemLabel,a.customHTML),d(a.itemClassName,"custom
NOTE|sink:innerHTML in: .innerHTML=l("product-menu-item","https://assets.fyers.in/global-components/trade-icons/top
NOTE|sink:innerHTML in: .innerHTML=`\n <div class="container">\n <span class="title screeners-link" st
NOTE|sink:innerHTML in: .innerHTML=e,$.isEmptyObject(TradeModules.exitPositionWindow.controller.exitAllData)&&Trade
NOTE|sink:innerHTML in: .innerHTML=e,document.querySelector("#bwModalBody").innerHTML=t,orderWindow.theme.applyThem
NOTE|sink:innerHTML in: .innerHTML=e
NOTE|sink:innerHTML in: .innerHTML=t.toString().replaceAll(",",""),TradeModules.basketWindow.events.attachBasketLis
NOTE|sink:innerHTML in: .innerHTML=s.toString().replaceAll(",",""),r.innerHTML=i.toString().replaceAll(",","")}asyn
NOTE|sink:message listener in: addEventListener("message"
NOTE|sink:localStorage in: localStorage.getItem("userSettingsData"
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_nonDraggable","true"
NOTE|sink:localStorage in: localStorage.getItem("_publicHoliday"
NOTE|sink:localStorage in: localStorage.setItem("_publicHoliday",JSON.stringify(t
NOTE|sink:localStorage in: localStorage.setItem("userSettingsData",e
NOTE|sink:localStorage in: localStorage.setItem("hidePnL",e
NOTE|sink:localStorage in: localStorage.getItem("userKodiSettingsData"
NOTE|sink:localStorage in: localStorage.setItem("userKodiSettingsData",e
NOTE|sink:localStorage in: localStorage.getItem("_mppData"
NOTE|sink:localStorage in: localStorage.setItem("_mppData",JSON.stringify(t
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_themeStyle","light"
NOTE|sink:localStorage in: localStorage.setItem("fyerstrade_themeStyle",serverDict["current_theme.name"]
NOTE|sink:atob in: atob(t
NOTE|Uses Bearer auth via cookie "_FYERS"
SECRET|google_key|G-NTFX8XLKVH
ENDPOINT|GET|https://trade.fyers.in/v1/snapshot
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/limit
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/peg
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/trail
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/step
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/sip
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/cancel
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/modify
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/resume
ENDPOINT|POST|https://api-t1.fyers.co.in/smart-order/pause
ENDPOINT|GET|https://api-t1.fyers.co.in/smart-order/history
ENDPOINT|GET|https://api-t1.fyers.co.in/smart-order/v2/orderbook
ENDPOINT|GET|https://api-g1.fyers.in/settings
ENDPOINT|GET|https://api-g1.fyers.in/settings/quick-trade
ENDPOINT|GET|https://api-g1.fyers.in/settings/quick-trade-immutable
ENDPOINT|POST|https://api-g1.fyers.in/settings/quick-trade/reset
ENDPOINT|GET|https://api-a1.fyers.in/marina/v1/ddpi/statusV2
ENDPOINT|POST|https://api-t2.fyers.in/fydev/v1/baskets
HOST|api-t1.fyers.co.in
HOST|api-t1.fyers.in
HOST|api-t2.fyers.in
HOST|api-g1.fyers.in
HOST|api-a1.fyers.in
HOST|trade.fyers.in
HOST|assets.fyers.in
HOST|login.fyers.in
HOST|fundtransfer.fyers.in
HOST|instaoptions.fyers.in
HOST|savedcharts.fyers.in
HOST|insights.fyers.in
HOST|marksmith.fyers.in
NOTE|Only finding of type google_key; no hardcoded JWT/long-term credentials in file
