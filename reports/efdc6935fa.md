# https://assets.fyers.in/Lib/widget/fyers-widget.js
NOTE|sink:innerHTML in: .innerHTML = item.body.replace(/\r?\n|\r/g, " ")
NOTE|sink:innerHTML in: .innerHTML = messageBarHTML()
NOTE|sink:innerHTML in: .innerHTML = "1/" + (window.notificationData.length)
NOTE|sink:innerHTML in: .innerHTML = (index + 1) + "/" + (window.notificationData.length)
SECRET|dev_url|http://localhost/Git/GitHub/fy_notifications/public.json
ENDPOINT|GET|https://public.fyers.in/messages/public.json
ENDPOINT|GET|https://assets.fyers.in/fy_notifications/
HOST|fyers.in
NOTE|cookie set with domain=fyers.in and insecure max-age from client-side time (manipulable)
NOTE|undeclared globals/typos: CONSTANTS.INVALID_TYPE (undefined, Popup_msg), notificationData referenced without window. prefix in renderMessageBar and restoreMessagebar
NOTE|FY_POPUP_DATA.INVALID_TYPE defined but unused; getPopup rejects with undefined CONSTANTS
