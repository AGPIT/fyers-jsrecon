# https://app.fyers.in/reports/pnl/flutter_bootstrap.js
ENDPOINT|ANY|/web/
ENDPOINT|ANY|/web/assets/packages/flutter_inappwebview_web/assets/web/web_support.js
ENDPOINT|ANY|/web/assets/packages/fy_ui/assets/gifs/loader_dark.gif
ENDPOINT|ANY|/web/assets/packages/fy_ui/assets/gifs/loader_light.gif
NOTE|sink:message listener in: addEventListener("message"
NOTE|sink:service worker in: serviceWorker.register
SECRET|google_key|286450098109-8e77ml77icehbhpvplp2645hqqm6rtope.apps.googleusercontent.com (prod OAuth client ID)
SECRET|google_key|902868841845-3qb23dhv0b5tnvj7u2vbkur48v93borq.apps.googleusercontent.com (staging OAuth client ID)
HOST|fyers.in
HOST|assets.fyers.in
HOST|www.gstatic.com
HOST|app.fyers.in
NOTE|File is a Flutter web bootstrap stub (flutter.js loader, dart2js/canvaskit); OAuth client IDs are public identifiers, not secrets, but confirm no client_secret is exposed elsewhere.
NOTE|Theme/user-settings fix clears userSettingsData cookie scoped to .fyers.in.
