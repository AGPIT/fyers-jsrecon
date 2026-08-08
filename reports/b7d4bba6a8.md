# https://trade.fyers.in/apiv2-login-ie-support/js/login.js
NOTE|sink:innerHTML in: .innerHTML="Login Success!! :)"
NOTE|sink:innerHTML in: .innerHTML = err.message
NOTE|sink:innerHTML in: .innerHTML= dataFromServer.message
NOTE|sink:document.write in: document.write('<html lang="en"><head><title>Grant Access</title><meta char
SECRET|api_key|GSKZGJHIBV (app_id/api key in commented sample payload)
ENDPOINT|POST|https://api.fyers.in/api/v2/token
ENDPOINT|POST|https://api.fyers.in/api/preprod/token
HOST|api.fyers.in
HOST|trade.fyers.in
HOST|maxcdn.bootstrapcdn.com
HOST|ajax.googleapis.com
NOTE|login handles plaintext password + PAN/DOB, sends to /api/v2/token as JSON
NOTE|commented preprod/login endpoint api.preprod/token
NOTE|auth grant page written via document.write using server returned data, potential XSS
NOTE|commented data includes app_id=GSKZGJHIBV, redirect https://trade.fyers.in/api-login/redirect-uri/index.html, state sample_State, scope openid
NOTE|references dev/testing assets trade.fyers.in/testing_dontuse/appAccess/style.css and loginV2-Test.js
NOTE|uses window.location.assign(dataFromServer Directive container) for "308" open redirect risk
NOTE|password visibility toggle exists (passwordVisibility function)
NOTE|uses jQuery version 3.3.1 via CDN (outdated pre-PROJECT version, check vulnerabilities)
