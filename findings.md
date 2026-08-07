# JS Recon Findings (fyers.in) — deep scan

_src 2026-08-07 06:40 UTC — 115 secret hits_

- `https://app.fyers.in/assets/packages/clevertap_plugin/assets/clevertap.js`
  `SECRET|other|none found`
- `https://community.fyers.in/locales/en.js`
  `SECRET|google_key|AIzaSyAOg7DiR0iacQPO7jlix_6MgWe3JXhfGtg`
- `https://community.fyers.in/locales/en.js`
  `SECRET|google_key|G-4WTYM45VL9`
- `https://community.fyers.in/locales/en.js`
  `SECRET|jwt|eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImZLR0cifQ.eyJpZCI6IkdVRVNUX3pLUEVralVHM2F1NUMzeSIsIm5ldHdvcmtJZCI6IlpLbHp5O`
- `https://community.fyers.in/member/gtm.js`
  `SECRET|google_key|AIzaSyAOg7DiR0iacQPO7jlix_6MgWe3JXhfGtg`
- `https://community.fyers.in/member/gtm.js`
  `SECRET|google_key|AIzaSyAOg7DiR0iacQPO7jlix_6MgWe3JXhfGtg`
- `https://community.fyers.in/member/gtm.js`
  `SECRET|jwt|eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImZLR0cifQ.eyJpZCI6IkdVRVNUX0xWV1c0VFRVTVlQOVdnQSIsIm5ldHdvcmtJZCI6IlpLbHp5O`
- `https://community.fyers.in/member/gtm.js`
  `SECRET|jwt|eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImZLR0cifQ.eyJpZCI6IkdVRVNUX0xWV1c0VFRVTVlQOVdnQSIsIm5ldHdvcmtJZCI6IlpLbHp5OWl3QnEiLCJuZXR3b3JrRG9tYWluIjoiZnllcnMuYmV0dGVybW9kZS5pbyIsInRva2VuVHlwZSI6IkdVRVNUIiwiZW50aXR5SWQiOm51bGwsInBlcm1pc3Npb25Db250ZXh0IjpudWxsLCJwZXJtaXNzaW9ucyI6bnVsbCwiaWF0IjoxNzg2MDI4MTU0LCJleHAiOjE3ODYwNDI1NTR9.lhrak6dQmTgIoWoaIMMWmsLldtRv1RKL-8aWn1UqtZSDX4d2FkOq5uOsZing6AWhXbPzVkrAc55hRX3N6NnN5A`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|APP_ID_68USODQMOF-101 (dev Fyers API client id)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|APP_ID_EFR7964223-101 (prod Fyers API client id)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|APP_ID_H4NMJ8X2NR-101 (dev/localhost Fyers API client id)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|APP_ID_ZT6P4L9YQB-101 (staging Fyers API client id)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|appIdHash_dev=45ac1f5f538de89ff8a4e2ad77214266b04db3ba2442d2db0d <- approximate`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|appIdHash_prod=2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-0147514f0742b47de057.js`
  `SECRET|other|appIdHash_stag=1260e9be57e09bf77b06e322504fbf42e164d40578592c6e149f2e3714a6ce0`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-15d40a0cbe3524f23f72.js`
  `SECRET|api_key|client_id EFR7964223 (prod Fyers app ID; dev=68USODQMOF, staging=LCFY9OOX3D/ZT6P4L9YQB, localhost=H4NMJ8X2NR)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-15d40a0cbe3524f23f72.js`
  `SECRET|other|appIdHash SHA-256 per env (prod 2a88a14a353274a2f35430038b6d8172..., dev 45ac1f5f53..., staging 1260e9be57..., local 656b13d202...)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|api_key|68USODQMOF-101 (Fyers APP_ID, dev)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|api_key|EFR7964223-101 (Fyers APP_ID/client_id, prod ipo.fyers.in)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|api_key|H4NMJ8X2NR-101 (Fyers APP_ID, localhost)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|api_key|LCFY9OOX3D-101 (Fyers APP_ID, staging)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|api_key|ZT6P4L9YQB-101 (Fyers APP_ID, staging/test)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|other|1260e9be57e09bf77b06e322504fbf502164d6a405785921c6e149f32a237d4ed0 (app hash staging)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|other|2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f (SHA-256 app hash)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|other|45ac1f5f538de93ff8a4e2ad77214266b04db8dbf50fabdaecc7a3ffadf60ad0 (app hash dev)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-744d25aaf61e7be379a9.js`
  `SECRET|other|656b1386e20297a202d596d98b8e2000c1aac90998cc2bcfd00247c4479272a1e8 (app hash local)`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|api_key|68USODQMOF`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|api_key|EFR7964223`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|api_key|H4NMJ8X2NR`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|api_key|LCFY9OOX3D`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|api_key|ZT6P4L9YQB`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|other|1260e9be57e09bf77b06e322504fbf042164d40578592c6e149f32a237d44ed0`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|other|2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|other|45ac1f5f538de93ff8a4e2ad77214266b04db8dbf50fabdaecc7a3ffadf60ad0`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|other|656b1386e20297a2d596d98b840200c1aac90998cc2bcfd00247c4479272a1e8`
- `https://ipo.fyers.in/_next/static/chunks/pages/details-b6dbd5b53b66ca0e06d7.js`
  `SECRET|other|eedae6cd5dbb41660999947e13a4c9331e5c011ecd093a9e50bbaf8fbd083475`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|1260e9be57e09bf77b06e322504fbf042164d40578592c6e149f32a237d44ed0`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|45ac1f5f538de93ff8a4e2ad77214266b04db8dbf50fabdaecc7a3ffadf60ad0`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|656b1386e20297a2d596d98b840200c1aac90998cc2bcfd00247c4479272a1e8`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|68USODQMOF`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|EFR7964223`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|H4NMJ8X2NR`
- `https://ipo.fyers.in/_next/static/chunks/pages/home-d194728825ab6f10a77d.js`
  `SECRET|api_key|LCFY9OOX3D`
- `https://sgb.fyers.in/_next/static/chunks/c8f7fe3b0e41be846d5687592cf2018ff6e22687.ab2fd25807e4ebb228cc.js`
  `SECRET|other|APP_ID prod=QMABZB5R01 (Fyers API app identifier)`
- `https://sgb.fyers.in/_next/static/chunks/c8f7fe3b0e41be846d5687592cf2018ff6e22687.ab2fd25807e4ebb228cc.js`
  `SECRET|other|appIdHash prod=b21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447 (client-side hash)`
- `https://sgb.fyers.in/_next/static/chunks/c8f7fe3b0e41be846d5687592cf2018ff6e22687.ab2fd25807e4ebb228cc.js`
  `SECRET|other|client_id=QMABZB5R01-101 (Fyers OAuth APP_ID/API client id, prod)`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|appIdHash=39abc82e995e6c2e8ab69086650b1fa700300322a2fb0d846902e0804ca1bf0c`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|appIdHash=656b1386e20297a2d596d98b840200c1aac90998cc2bcfd00247c4479272a1e8`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|appIdHash=b21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|appIdHash=f35212e4c44c8bb9aabd2bc08e37c73a1c80073eabfdadcf5dae590e4b28d91c`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|client_id=AF0MATWSX3 (staging appId)`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|client_id=H4NMJ8X2NR (local appId)`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|client_id=N43J3GIGOM (dev appId)`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-33907670c16c0471dfdd.js`
  `SECRET|other|client_id=QMABZB5R01 (prod Fyers SGB OAuth appId)`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-44ba022e9d10069c6970.js`
  `SECRET|api_key|APP_ID/client_id: QMABZB5R01-101 (prod), N43J3GIGOM-101 (dev), AF0MATWSX3-101 (staging), H4NMJ8X2NR-101 (localhost) - Fyers API client IDs`
- `https://sgb.fyers.in/_next/static/chunks/pages/details-44ba022e9d10069c6970.js`
  `SECRET|other|appIdHash sha256: b21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447 (prod), e4ec93cf189f1d455cb428a86c9fa64b12498c2168b85116928a1f6e15144876 (staging), f35212e4c46e40a1e0c2e1e2e4a40d13 (dev/commented), 39abc82e995e6c2e8ab69086650b1ed70a9730032e0a2e5e6c0e1e06ea910f0f801a1 (commented staging)`
- `https://trade.fyers.in/Prod/1.2/orderWindow.min.js`
  `SECRET|none`
- `https://trade.fyers.in/Prod/1.2/trade-common.js`
  `SECRET|google_key|G-NTFX8XLKVH`
- `https://trade.fyers.in/static/js/ordwin/js/6/orderwindow.min.js`
  `SECRET|other|hardcoded internal plaintext-HTTP backend endpoint 13.235.24.249:8080 serving /gtt/orders (deobfuscated from obfuscated string array "API_POINT")`
- `https://verifiedpnl.fyers.in/static/js/main.1b27d8c5.js`
  `SECRET|jwt|none found`
- `https://verifiedpnl.fyers.in/static/js/main.606be587.js`
  `MAP SECRET|api_key|_FYERS (JWT session cookie parsed client-side in getUserDetails.js:33739, auth validity not server-verified; used to gate UI and sent to get-data endpoint)`
- `https://verifiedpnl.fyers.in/static/js/main.78f0294e.js`
  `MAP SECRET|api_key|NO_KEY_FOUND`
- `https://verifiedpnl.fyers.in/static/js/main.78f0294e.js`
  `SECRET|google_key|AIza[0-9A-Za-z_-]{`
- `https://verifiedpnl.fyers.in/static/js/main.cf21f7c5.js`
  `MAP SECRET|other|none found`
- `https://verifiedpnl.fyers.in/static/js/main.cf21f7c5.js`
  `SECRET|api_key|pnl_url:https://api-a1-prod.fyers.in/myaccount/prod/verified-pnl/get-data (frozen config export, prod back-end URL)`
- `https://www.fyers.in/CompoundRateAssets/js/charts.js`
  `SECRET|other|no secrets found`
- `https://www.fyers.in/FibonacciCalculatorAssets/js/wcf_custom.js`
  `SECRET|google_key|G-JXG5NQ1WQJ`
- `https://www.fyers.in/FibonacciCalculatorAssets/js/wcf_custom.js`
  `SECRET|google_key|GTM-MB6PRVDG`
- `https://www.fyers.in/General-assets/js/app/controllers.js`
  `SECRET|other|google_tag_id_G-JXG5NQ1WQJ`
- `https://www.fyers.in/General-assets/js/app/controllers.js`
  `SECRET|other|google_tag_manager_GTM-MB6PRVDG`
- `https://www.fyers.in/General-assets/js/calender.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/General-assets/js/calender.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/General-assets/js/highcharts.js`
  `SECRET|google_key|G-JXG5NQ1WQJ`
- `https://www.fyers.in/General-assets/js/highcharts.js`
  `SECRET|google_key|GTM-MB6PRVDG`
- `https://www.fyers.in/General-assets/js/ion.rangeSlider.min.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/General-assets/js/ion.rangeSlider.min.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/General-assets/js/ion.rangeSlider.min.js`
  `SECRET|other|formperma token ZiaB9_3-KvEZZdnyxaY6d6LNb5vlmzYL8Ta3KcsV4xI (Zoho Forms)`
- `https://www.fyers.in/General-assets/js/jquery-1.7.2.min.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/General-assets/js/jquery-1.7.2.min.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/General-assets/js/jquery-ui-1.8.21.custom.min.js`
  `SECRET|other|G-JXG5NQ1WQJ (Google Analytics 4 property ID)`
- `https://www.fyers.in/General-assets/js/jquery-ui-1.8.21.custom.min.js`
  `SECRET|other|GTM-MB6PRVDG (Google Tag Manager container ID)`
- `https://www.fyers.in/General-assets/js/jquery.cookie.js`
  `SECRET|other|none`
- `https://www.fyers.in/GoalTracker-assets/js/calculators.js`
  `SECRET|google_key|G-JXG5NQ1WQJ (Google Analytics GA4 ID; public)`
- `https://www.fyers.in/GoalTracker-assets/js/calculators.js`
  `SECRET|other|GTM-MB6PRVDG (Google Tag Manager container; public)`
- `https://www.fyers.in/GoalTracker-assets/js/wcf_custom.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/GoalTracker-assets/js/wcf_custom.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/ReferalEarningCalcAssets/js/calculators.js`
  `SECRET|none|no secrets in visible content`
- `https://www.fyers.in/ShortTermReturnsAssets/js/calculators.js`
  `SECRET|google_key|G-JXG5NQ1WQJ`
- `https://www.fyers.in/ShortTermReturnsAssets/js/calculators.js`
  `SECRET|google_key|GTM-MB6PRVDG`
- `https://www.fyers.in/brokerageComparisonAssets/js/calculators.js`
  `SECRET|other|analytics_tracking_id G-JXG5NQ1WQJ (Google Analytics)`
- `https://www.fyers.in/brokerageComparisonAssets/js/calculators.js`
  `SECRET|other|analytics_tracking_id GTM-MB6PRVDG (Google Tag Manager)`
- `https://www.fyers.in/disciplineDiary/js/wcf_custom.js`
  `SECRET|none|none`
- `https://www.fyers.in/sipcalculatorAssets/js/calculators.js`
  `SECRET|google_key|G-JXG5NQ1WQJ`
- `https://www.fyers.in/sipcalculatorAssets/js/calculators.js`
  `SECRET|google_key|GTM-MB6PRVDG`
- `https://www.fyers.in/sipcalculatorAssets/js/calculators.js`
  `SECRET|other|ZiaB9_3-KvEZZdnyxaY6d6LNb5vlmzYL8Ta3KcsV4xI`
- `https://www.fyers.in/trading/js/bootstrap.min.js`
  `SECRET|google_key|G-JXG5NQ1WQJ`
- `https://www.fyers.in/trading/js/bootstrap.min.js`
  `SECRET|google_key|GTM-MB6PRVDG`
- `https://www.fyers.in/trading/js/flexslider.min.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/trading/js/flexslider.min.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/trading/js/gen_validatorv31.js`
  `SECRET|other|none_found`
- `https://www.fyers.in/trading/js/parallax.js`
  `SECRET|other|G-JXG5NQ1WQJ (Google Analytics)`
- `https://www.fyers.in/trading/js/parallax.js`
  `SECRET|other|GTM-MB6PRVDG (GTM container)`
- `https://www.fyers.in/trading/js/pivottrading.js`
  `SECRET|other|G-JXG5NQ1WQJ (GA4 measurement ID, non-sensitive)`
- `https://www.fyers.in/trading/js/pivottrading.js`
  `SECRET|other|GTM-MB6PRVDG (GTM container ID, non-sensitive)`
- `https://www.fyers.in/trading/js/scripts.js`
  `SECRET|google_key|G-JXG5NQ1WQJ`
- `https://www.fyers.in/trading/js/scripts.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/trading/js/smooth-scroll.min.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/trading/js/smooth-scroll.min.js`
  `SECRET|other|GTM-MB6PRVDG`
- `https://www.fyers.in/trading/js/spectragram.min.js`
  `SECRET|other|GA4 ID G-JXG5NQ1WQJ (public analytics, not a secret)`
- `https://www.fyers.in/trading/js/spectragram.min.js`
  `SECRET|other|GTM container GTM-MB6PRVDG (public tag manager, not a secret)`
- `https://www.fyers.in/trading/js/twitterfetcher.min.js`
  `SECRET|other|G-JXG5NQ1WQJ (GA4 tag, public marketing id)`
- `https://www.fyers.in/trading/js/twitterfetcher.min.js`
  `SECRET|other|GTM-MB6PRVDG (GTM container, public marketing id)`
- `https://www.fyers.in/wp-content/plugins/tlp-team/assets/js/imagesloaded.pkgd.min.js`
  `SECRET|other|G-JXG5NQ1WQJ`
- `https://www.fyers.in/wp-content/plugins/tlp-team/assets/js/imagesloaded.pkgd.min.js`
  `SECRET|other|GTM-MB6PRVDG`
