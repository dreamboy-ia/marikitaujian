# Deploy ke Cloudflare Pages (gratis)

Butuh: akun Cloudflare (gratis) + Node.js di laptop. Sekitar 15 menit.

```bash
npm i -g wrangler@3                  # sekali saja
wrangler login                       # buka browser, izinkan
wrangler d1 create marikitaujian     # salin "database_id" yang muncul
#  → tempel ke wrangler.toml (ganti GANTI_DENGAN_ID_...)
wrangler d1 execute marikitaujian --remote --file=schema.sql
wrangler pages deploy                # pertama kali: pilih "create new project", nama: marikitaujian
```
Situs tayang di `https://marikitaujian.pages.dev`. Kalau nama itu sudah dipakai orang lain, ganti `SITE` di
`tools/build.py` dan URL canonical di `public/index.html` & `public/mitra.html`, lalu `python3 tools/build.py`.

Binding D1 terbaca dari `wrangler.toml`. Kalau form error "Server sedang bermasalah", cek di dashboard:
Workers & Pages → marikitaujian → Settings → Bindings → harus ada D1 `DB`.

## Setelah tayang
1. **Google Search Console** (gratis): tambahkan properti URL situs → verifikasi (tag HTML) → Sitemaps → kirim `sitemap.xml`.
2. Minta indeks manual untuk beranda + 5 artikel (URL Inspection → Request indexing).

## Melihat data pendaftar
Dashboard Cloudflare → Storage & Databases → D1 → marikitaujian → Console:
```sql
SELECT * FROM waitlist ORDER BY id DESC;
SELECT * FROM mitra ORDER BY id DESC;
-- pendaftar per mitra:
SELECT m.code, m.nama, COUNT(w.id) AS pendaftar FROM mitra m LEFT JOIN waitlist w ON w.ref = m.code GROUP BY m.code;
```

## Menambah artikel
Buat `content/artikel/<slug>.html` (baris 1 = JSON meta, sisanya HTML; `<!--CTA-->` = kotak ajakan),
jalankan `python3 tools/build.py`, lalu `wrangler pages deploy`.
