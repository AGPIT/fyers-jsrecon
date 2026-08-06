# JS Recon Findings (fyers.in) — deep scan

_src 2026-08-06 15:01 UTC — 44 secret hits_

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
