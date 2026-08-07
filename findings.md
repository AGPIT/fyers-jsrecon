# JS Recon Findings (fyers.in) — deep scan

_src 2026-08-07 20:55 UTC — 261 secret hits_

- `https://app.fyers.in/assets/packages/clevertap_plugin/assets/clevertap.js`
  `SECRET|other|none found`
- `https://assets.fyers.in/Lib/calculators/1.0/brokrage-calc.js`
  `SECRET|__cafinit__|b"zqthk presan".config .r {"tracechains":null,"convBasisIO":{"slot":360,"volatile":0.000026,"b":"BAY",STT:0.0001},"assumed":"noun"}`
- `https://assets.fyers.in/Lib/calculators/2.0/brokrage-calc.js`
  `SECRET|other|strike_price_is_uninitialized_undefined_reference`
- `https://assets.fyers.in/Lib/calculators/2.10/brokrage-calc.js`
  `SECRET|other|api-t1.fyers.in (trade v3 API host, no auth) — noted in SpanCalculator ajax request; no actual secret material present`
- `https://assets.fyers.in/Lib/calculators/2.11/brokrage-calc.js`
  `SECRET|other|no secrets found - only brokerage rate constants`
- `https://assets.fyers.in/Lib/calculators/2.14/brokrage-calc.js`
  `SECRET|NONE|no credentials found`
- `https://assets.fyers.in/Lib/calculators/2.15/brokrage-calc.js`
  `SECRET|internal_endpoint|https://api-t1.fyers.in/trade/v3/spancalc`
- `https://assets.fyers.in/Lib/calculators/2.16/brokrage-calc.js`
  `SECRET|other|none found`
- `https://assets.fyers.in/Lib/calculators/2.4/brokrage-calc.js`
  `SECRET|other|no secrets found in file`
- `https://assets.fyers.in/Lib/calculators/2.6/brokrage-calc.js`
  `SECRET|other|COMMODITY_FUTURES,COMMODITY_OPTIONS,NSE_COMMODITY_FUTURES,NSE_COMMODITY_OPTIONS - brokerage rate configs (rates/stt/lot sizes), not credentials`
- `https://assets.fyers.in/Lib/calculators/2.8/brokrage-calc.js`
  `SECRET|none`
- `https://assets.fyers.in/Lib/calculators/2.9/brokrage-calc.js`
  `SECRET|api_key|api-t1.fyers.in/trade/v3/spancalc (brokerage span-calc API endpoint)`
- `https://assets.fyers.in/fy_notifications/js/2.0/fyers-widget.min.js`
  `SECRET|NONE|no hardcoded credentials found (obfuscated app, strings like INTERVAL/NOTIFICATION only)`
- `https://assets.fyers.in/tv_lib/v29.4.0/charting_library.standalone.js`
  `SECRET|api_key|client_id:"0" (placeholder default, not a real credential)`
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
- `https://fundtransfer.fyers.in/v2/assets/js/owl.carousel.min.js`
  `SECRET|other|none_found`
- `https://fyers.in/_next/static/chunks/375-7524336be56b0456.js`
  `SECRET|other|none`
- `https://ipo.fyers.in/_next/static/chunks/5d803da5ef9d1718c712fe441612209655f8245f.99c7e57583a1a03459a9.js`
  `SECRET|other|none_found`
- `https://ipo.fyers.in/_next/static/chunks/5d803da5ef9d1718c712fe441612209655f8245f.99c7e57583a1a03459a9.js`
  `SECRET|other|none_found`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.cc87701246c10b9e245e.js`
  `SECRET|api_key|EFR7964223`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.cc87701246c10b9e245e.js`
  `SECRET|other|2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|api_key|68USODQMOF`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|api_key|EFR7964223`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|api_key|H4NMJ8X2NR`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|api_key|LCFY9OOX3D`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|other|2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|other|45ac1f5f538de93ff8a4e2ad77214266b04db8dbf50fabdaecc7a3ffadf60ad0`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|other|656b1386e20297a2d596d98b840200c1aac90998cc2bcfd00247c4479272a1e8`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f186fd3fb98cbef7977a.js`
  `SECRET|other|eedae6cd5dbb41660999947e13a4c9331e5c011ecd093a9e50bbaf8fbd083475`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|api_key|68USODQMOF`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|api_key|EFR7964223`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|api_key|H4NMJ8X2NR`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|api_key|ZT6P4L9YQB`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|jwt|0c3f7d40e9eced42c0be1b91185b882b4e69526952a1f5ce484f00e2c1d8a375`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|jwt|2a88a14a353274a2f35430038b6d81725e2d17d8064785d62965e4da78033e9f`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|jwt|45ac1f5f538de93ff8a4e2ad77214266b04db8dbf50cdbe2cc7a3ffadf60ad0`
- `https://ipo.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.f6fbd9dc97569273c050.js`
  `SECRET|jwt|8c81cd1e3826aef7d9367a8479e2f321a84e53dc723e9fbec2a3f9be2d9c2e1b7`
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
- `https://marketsmith.fyers.in/assets/vendor/bootstrap/js/bootstrap.bundle.min.js`
  `SECRET|api_key|ApiKeydownHandler (matches Bootstrap dropdown keydown, not a secret)`
- `https://partners.fyers.in/fyers_widget/fyers-widget.min.js`
  `SECRET|dev_url|http://127.0.0.1:46475/fy_notifications/js/data.json`
- `https://public.fyers.in/haircut-mf/assets/vendor/jquery/jquery.min.js`
  `SECRET|other|none`
- `https://sgb.fyers.in/_next/static/chunks/61fe32111765d6645b96fc3d8e2e36f3b2d36f0c.b3ba817385a4a55bb248.js`
  `SECRET|other|https://support.fyers.in/ (public support link, not a credential)`
- `https://sgb.fyers.in/_next/static/chunks/c8f7fe3b0e41be846d5687592cf2018ff6e22687.ab2fd25807e4ebb228cc.js`
  `SECRET|other|APP_ID prod=QMABZB5R01 (Fyers API app identifier)`
- `https://sgb.fyers.in/_next/static/chunks/c8f7fe3b0e41be846d5687592cf2018ff6e22687.ab2fd25807e4ebb228cc.js`
  `SECRET|other|appIdHash prod=b21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447 (client-side hash)`
- `https://sgb.fyers.in/_next/static/chunks/c8f7fe3b0e41be846d5687592cf2018ff6e22687.ab2fd25807e4ebb228cc.js`
  `SECRET|other|client_id=QMABZB5R01-101 (Fyers OAuth APP_ID/API client id, prod)`
- `https://sgb.fyers.in/_next/static/chunks/c930e9b61683ff946dd89c25b851ab337278c84b.38efa6cb924d0fcb8377.js`
  `SECRET|other|auth_code passed via URL query used directly as Authorization header`
- `https://sgb.fyers.in/_next/static/chunks/c930e9b61683ff946dd89c25b851ab337278c84b.38efa6cb924d0fcb8377.js`
  `SECRET|other|localStorage.auth_token read and set as Authorization header`
- `https://sgb.fyers.in/_next/static/chunks/c930e9b61683ff946dd89c25b851ab337278c84b.4853267f48716fd0cb10.js`
  `SECRET|other|auth_token from localStorage passed verbatim as Authorization header (JWT-style bearer token, no scheme prefix)`
- `https://sgb.fyers.in/_next/static/chunks/c930e9b61683ff946dd89c25b851ab337278c84b.d3a64d4a13fa91f39e0b.js`
  `SECRET|other|no hardcoded secrets found (auth_token read at runtime from localStorage)`
- `https://sgb.fyers.in/_next/static/chunks/main-1f1bdab0e2f336010c3f.js`
  `SECRET|jwt|none`
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
- `https://sgb.fyers.in/_next/static/chunks/pages/home-0f59e652c9a6aefc2cf1.js`
  `SECRET|api_key|656b1386e20297a2d596d98b840200c1aac90998cc2bcf00247c4479272a1e8`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-0f59e652c9a6aefc2cf1.js`
  `SECRET|api_key|bar 21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-0f59e652c9a6aefc2cf1.js`
  `SECRET|other|QMABZB5R01`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-95c008466d659064a2f9.js`
  `SECRET|other|appIdHash dev: f35212e4c44c8bb9aabd2bc08e37c73a1c80073eabfdadcf5dae590e4b28d91c`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-95c008466d659064a2f9.js`
  `SECRET|other|appIdHash prod active: b21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-95c008466d659064a2f9.js`
  `SECRET|other|appIdHash staging: 39abc82e995e6c2e8ab69086650b1fa700300322a2fb0d846902e0804ca1bf0c`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|api_key|QMABZB5R01`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|api_key|b21f86d5bba39251763e49e4b10e71ec5bc99c4ef68fa94c1652ef3f36e82447`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|other|656b1386e20297a2d596d98b840200c1aac90998cc2bcfd00247c4479272a1e8`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|other|AEHNSK9PRW`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|other|H4NMJ8X2NR`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|other|N43J3GIGOM`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|other|e4ec93cf189f1d455cb428a86c9fa64b12498c2168b85116928a1f6e1514487b`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-ac56cb0ac001d9ac5ef2.js`
  `SECRET|other|f35212e4c44c8bb9aabd2bc08e37c73a1c80073eabfdadcf5dae590e4b28d91c`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|api_key|AF0MATWSX3`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|api_key|H4NMJ8X2NR`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|api_key|N43J3GIGOM`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|api_key|QMABZB5R01`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|other|appIdHash=656b1386e20297a2d596e98b840200c12247c4b7`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|other|appIdHash=b21f86d5bba39251763e49e4b10e71e59f3f36e82447`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|other|appIdHash=e4ec93ef63a9fa64b12498c2168b85116928a1f6e1514487b`
- `https://sgb.fyers.in/_next/static/chunks/pages/home-da82cc27d88581830b16.js`
  `SECRET|other|appIdHash=f35212e4c44c8bb9aabd2bc08e37c73a5dae590e4b28d91c`
- `https://signup.fyers.in/assets/packages/flutter_inappwebview_web/assets/web/web_support.js`
  `SECRET|other|none found`
- `https://subscriptions.fyers.in/assets/js/main-truedata.js`
  `SECRET|api_key|0KMS0EZVXI`
- `https://trade.fyers.in/30daysChallenge/live/lib/jquery/jquery.min.js`
  `SECRET|other|jquery 3.2.1 library (known standard minified jQuery; no embedded secrets detected)`
- `https://trade.fyers.in/Prod/1.2/bundle.min.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/Prod/1.2/fyers_common_modules.js`
  `SECRET|jwt|token (JWT user session token passed in Authorization header / `authorization` header of fetch calls)`
- `https://trade.fyers.in/Prod/1.2/orderWindow.min.js`
  `SECRET|none`
- `https://trade.fyers.in/Prod/1.2/posConv.min.js`
  `SECRET|other|https://public.fyers.in/messages/messagesLinks.json`
- `https://trade.fyers.in/Prod/1.2/trade-common.js`
  `SECRET|google_key|G-NTFX8XLKVH`
- `https://trade.fyers.in/Prod/1.2/trade.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M= (Fernet-format encrypted token hardcoded in HISTORY_TEST test data)`
- `https://trade.fyers.in/Prod/1.2/widgets.min.js`
  `SECRET|api_key|1341655KwEfgY`
- `https://trade.fyers.in/Prod/1.2/widgets.min.js`
  `SECRET|api_key|984896EWiONu`
- `https://trade.fyers.in/Prod/1.2/widgets.min.js`
  `SECRET|other|Authentication derived from document cookie (getCookie) plus a request header named "Authorization" carrying the login token; requests use withCredentials=true`
- `https://trade.fyers.in/Prod/exception/bundle.min.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M= (hardcoded Fernet-format token_id in HISTORY_TEST/WS config)`
- `https://trade.fyers.in/Prod/popout/trade-common.js`
  `SECRET|other|No hardcoded secrets; auth uses runtime `_FYERS` cookie/JWT (JWT is base64url-decoded; token passed in URL query params)`
- `https://trade.fyers.in/api-login/redirect-uri/assets/vendor/bootstrap/js/bootstrap.bundle.min.js`
  `MAP SECRET|other|none`
- `https://trade.fyers.in/apiv2-login-ie-support/js/jquery.validate.js`
  `SECRET|other|none found`
- `https://trade.fyers.in/lib/sentry/bundle.tracing.min.js`
  `SECRET|other|https://github.com/getsentry/sentry-javascript (attribution URL, no secret)`
- `https://trade.fyers.in/lib/signalR/2.4.0/jquery.signalR.min.js`
  `SECRET|type|other|none found`
- `https://trade.fyers.in/production/v1.1/datafeed.min.js`
  `SECRET|other|Fernet-format datafeed token (token_id) gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/basket-order/assets/js/1.5/bo.min.js`
  `SECRET|other|no hardcoded secrets - secret_key read from localStorage, token_id passed in from caller`
- `https://trade.fyers.in/static/js/basket-order/assets/js/2.0/bo.min.js`
  `SECRET|other|secret_key read from localStorage and used to sign marketStat (MD5(keyword|timestamp|secret_key))`
- `https://trade.fyers.in/static/js/basket-order/assets/js/2.3/bo.min.js`
  `SECRET|other|fyToken runtime session token read from `_FYERS` cookie and sent as `Authorization` header (not a hardcoded key)`
- `https://trade.fyers.in/static/js/broker/11.4/bundle.min.js`
  `SECRET|other|no hardcoded credentials found; auth tokens are populated at runtime (e.g. getCookie("_FYERS"), Authorization header set from token variable)`
- `https://trade.fyers.in/static/js/broker/12.1/bundle.min.js`
  `SECRET|internal_endpoint|https://api.fyers.in/fy/cdsl/dev`
- `https://trade.fyers.in/static/js/broker/12.1/bundle.min.js`
  `SECRET|internal_endpoint|https://api.fyers.in/fydev/v1`
- `https://trade.fyers.in/static/js/broker/12.1/bundle.min.js`
  `SECRET|internal_endpoint|https://api.fyers.in/vagator/v1`
- `https://trade.fyers.in/static/js/broker/12.1/bundle.min.js`
  `SECRET|internal_endpoint|https://datapub.fyers.in:8862`
- `https://trade.fyers.in/static/js/broker/12.1/bundle.min.js`
  `SECRET|internal_endpoint|wss://api-socket.fyers.in/dev/order`
- `https://trade.fyers.in/static/js/broker/12/bundle.min.js`
  `SECRET|api_key|none`
- `https://trade.fyers.in/static/js/broker/12/bundle.min.js`
  `SECRET|aws_key|none`
- `https://trade.fyers.in/static/js/broker/12/bundle.min.js`
  `SECRET|db_credential|none`
- `https://trade.fyers.in/static/js/broker/12/bundle.min.js`
  `SECRET|github_token|none`
- `https://trade.fyers.in/static/js/broker/12/bundle.min.js`
  `SECRET|google_key|none`
- `https://trade.fyers.in/static/js/broker/12/bundle.min.js`
  `SECRET|jwt|none`
- `https://trade.fyers.in/static/js/broker/13/bundle.min.js`
  `SECRET|api_key|token_id (OAuth token identifier passed via query params to /edis/details, /edis/index, /edis/authCdsl.html)`
- `https://trade.fyers.in/static/js/broker/13/bundle.min.js`
  `SECRET|other|fy_token / access_token / refresh_token (OAuth token variable names referenced in code)`
- `https://trade.fyers.in/static/js/broker/9.39/bundle.min.js`
  `SECRET|other|no hardcoded credentials found (bundle contains only obfuscated identifiers fyToken, rsToken, RS_TOKEN, CLIENT_ID as storage keys, not values)`
- `https://trade.fyers.in/static/js/broker/9.40/bundle.min.js`
  `SECRET|other|no hardcoded secrets; fyToken/rsToken/RS_TOKEN accessed at runtime`
- `https://trade.fyers.in/static/js/broker/9.42/bundle.min.js`
  `SECRET|api_key|CLIENT_ID (variable identifier, no literal value)`
- `https://trade.fyers.in/static/js/broker/9.55/bundle.min.js`
  `SECRET|none found in file`
- `https://trade.fyers.in/static/js/broker/9.93/bundle.min.js`
  `SECRET|none|none`
- `https://trade.fyers.in/static/js/broker/9.99/bundle.min.js`
  `SECRET|other|no hardcoded credentials (no AWS/Google/GitHub/JWT/DB keys); only public app_id "2" and runtime cookie-based session tokens`
- `https://trade.fyers.in/static/js/datafeed/udf/10.1/bundle.min.js`
  `SECRET|other|Authorization header set from "_FYERS" cookie; request param token_id injected at runtime`
- `https://trade.fyers.in/static/js/datafeed/udf/10.1/bundle.min.js`
  `SECRET|other|localStorage keys "secret_key" and "supportedResolutions" populated from config/ endpoint`
- `https://trade.fyers.in/static/js/datafeed/udf/10.1/bundle.min.js`
  `SECRET|other|runtime MD5 signing: symbol+timeStamp+secret_key(localStorage) hashed via CryptoJS.MD5, passed as marketStat param (no hardcoded key)`
- `https://trade.fyers.in/static/js/datafeed/udf/10.7/bundle.min.js`
  `SECRET|other|token_id Fernet token: gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M= (embedded in HISTORY_TEST sample)`
- `https://trade.fyers.in/static/js/datafeed/udf/10.8/bundle.min.js`
  `SECRET|other|none`
- `https://trade.fyers.in/static/js/datafeed/udf/10/bundle.min.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/11.3/bundle.min.js`
  `SECRET|other|no hardcoded secrets found (CryptoJS library routines only)`
- `https://trade.fyers.in/static/js/datafeed/udf/11.6/bundle.min.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M (Fernet-encrypted token embedded in history request /token_id, hardcoded in bundle)`
- `https://trade.fyers.in/static/js/datafeed/udf/12.1/bundle.min.js`
  `SECRET|api_key|secret_key (read from localStorage, sent as auth for symbol resolution)`
- `https://trade.fyers.in/static/js/datafeed/udf/12.1/bundle.min.js`
  `SECRET|jwt|token_id (encrypted JWT-like token used for HSM session auth)`
- `https://trade.fyers.in/static/js/datafeed/udf/12.2/bundle.min.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/12.6/bundle.min.js`
  `SECRET|api_key|Client session secret stored at localStorage["secret_key"], used with a unix-timestamp signature to authorize datafeed requests (HSM/WebSocket auth)`
- `https://trade.fyers.in/static/js/datafeed/udf/9.10/bundle.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/9.11/bundle.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/9.14/bundle.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M= (Fernet-encrypted token hardcoded as `token_id` in FYERS_OBJ.HISTORY_TEST)`
- `https://trade.fyers.in/static/js/datafeed/udf/9.18/bundle.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/9.23/bundle.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/9.3/bundle.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/9.33/bundle.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/datafeed/udf/9.36/bundle.js`
  `SECRET|other|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M= (Fernet-format token_id hardcoded in demo SUB_DATA frame)`
- `https://trade.fyers.in/static/js/datafeed/udf/9.8/bundle.js`
  `SECRET|api_key|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M= (hardcoded Fernet token used as token_id in FYERS_OBJ.HISTORY_TEST)`
- `https://trade.fyers.in/static/js/datafeed/udf/9.9/bundle.js`
  `SECRET|jwt|gAAAAABa1N59RgFWfiG1JD_W5KO143HKlj9Ezz6HMInChy8ud97qUSx01m3CMeyFk--Rrp13NSSUaGzvtstiim9nILsCOT3y1jDWSqsl5bmM1B2CXOW0V-M=`
- `https://trade.fyers.in/static/js/exit-widget/assets/js/2.3/eo.min.js`
  `SECRET|other|auth_token and token_id are read from runtime variables (not hardcoded in file)`
- `https://trade.fyers.in/static/js/exit-widget/assets/js/2.5/eo.min.js`
  `SECRET|other|auth_token and token_id are passed as request variables (Authorization header + query param), not hardcoded values`
- `https://trade.fyers.in/static/js/hsweb/hslibo.js`
  `SECRET|other|No hardcoded credentials found; only runtime auth inputs (jwt, x-access-token, Sid, redis key) are passed in by caller`
- `https://trade.fyers.in/static/js/option-chain/assets/js/1.7/oc-main.min.js`
  `SECRET|other|localStorage key `secret_key` (I82) read via getItem and used to build authenticated API request params (symbol, dataReq, timestamp, marketStat, token_id) for the options-chain endpoint; no hardcoded secret value present`
- `https://trade.fyers.in/static/js/option-chain/assets/js/2.2/oc-main.min.js`
  `SECRET|potential_internal_secret|localStorage.getItem("secret_key") used in MD5 signing of API requests`
- `https://trade.fyers.in/static/js/orddetail/js/1.2/script.min.js`
  `SECRET|other|auth_token referenced via global variable (defined externally, not in file)`
- `https://trade.fyers.in/static/js/ordwin/js/2.0/helper.min.js`
  `SECRET|other|101000000014366`
- `https://trade.fyers.in/static/js/ordwin/js/2.0/helper.min.js`
  `SECRET|other|1100000005899114`
- `https://trade.fyers.in/static/js/ordwin/js/2.0/helper.min.js`
  `SECRET|other|51808097115-CO-1`
- `https://trade.fyers.in/static/js/ordwin/js/2.4/helper.min.js`
  `SECRET|other|fyToken:"101000000014366" (hardcoded demo token in modifyBtn handler)`
- `https://trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js`
  `SECRET|dev_url|https://data.fyers.in/dev-fyers/mobileapi`
- `https://trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js`
  `SECRET|dev_url|https://dev.fyers.in/orderwin-trade/static/js/ordwin/warning.svg`
- `https://trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js`
  `SECRET|internal_endpoint|https://api.fyers.in/anjuna/v1/margin`
- `https://trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js`
  `SECRET|internal_endpoint|https://api.fyers.in/fydev/v1/baskets?token_id=`
- `https://trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js`
  `SECRET|internal_endpoint|https://api.fyers.in/fydev/v1/margin/v1?token_id=`
- `https://trade.fyers.in/static/js/ordwin/js/4.6/helper_min.js`
  `SECRET|internal_endpoint|https://data.fyers.in/dev-fyers/mobileapi/user-settings`
- `https://trade.fyers.in/static/js/ordwin/js/6/orderwindow.min.js`
  `SECRET|other|hardcoded internal plaintext-HTTP backend endpoint 13.235.24.249:8080 serving /gtt/orders (deobfuscated from obfuscated string array "API_POINT")`
- `https://trade.fyers.in/static/js/widgets/js/2.2/widgets.min.js`
  `SECRET|api_key|fyToken (auth token, variable `tokenId`) — no hardcoded secret value present`
- `https://trade.fyers.in/static/js/widgets/js/2.3/widgets.min.js`
  `SECRET|other|no hardcoded secret value present; "secret_key" read from localStorage, MD5-combined into marketStat`
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
