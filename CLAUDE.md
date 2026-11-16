# CLAUDE.md — marikitaujian

## Pemilik
- Ivan, karyawan kantoran 30-an ("Corporate Dad"), mencari penghasilan tambahan yang stabil.
- Bahasa kerja: Bahasa Indonesia.

## Aturan tetap
1. **Tanpa biaya tambahan** selain langganan Claude Pro, Gemini AI Plus, ElevenLabs Starter.
   Boleh: tier gratis (Cloudflare Pages/Workers/D1, Gemini API gratis) dan biaya per transaksi payment gateway.
2. **Hemat kuota Claude** (dipakai juga untuk proyek Pipit Learns): kerja efisien, jangan bolak-balik,
   **tanya dulu sebelum tugas besar**.
3. **TIDAK BOLEH menyalin/parafrase soal asli ujian resmi.** Soal harus buatan sendiri dari kisi-kisi &
   regulasi publik, dan **diverifikasi manusia sebelum terbit**.
4. Selalu sertakan **hook** yang menarik user untuk ikut tes atau membeli produk digital
   (tryout gratis, skor/peringkat, pembahasan terkunci, dsb).

5. **Persuasi jujur saja** (keputusan Ivan, 16 Nov 2026): boleh pakai psikologi marketing (loss aversion, anchoring,
   decoy, komitmen kecil, reciprocity, authority) tapi DILARANG timer palsu, angka pendaftar/penjualan palsu,
   testimoni karangan, atau kelangkaan yang tidak nyata. Angka sosial hanya dari data asli (D1/Mayar).
   Copy mengikuti skill antislop-copywriting (tanpa em dash, tanpa buzzword).
   Harga disetujui: E-book Wawancara Rp39rb · Bank Soal Rp49rb · Bundle Rp69rb (perdana Rp49rb untuk 100 pembeli pertama).
   Garansi uang kembali: BELUM disetujui.

## Ide proyek
Web latihan/tryout ujian **NICHE**. Inspirasi: post Threads @mashaaq21 (Nov 2026) tentang web tryout UPKP & UKOM ASN
(klaim 1.571 member, ±Rp16,2 jt/bulan; paket ±Rp10rb ×601, ±Rp44rb ×86, ±Rp64rb ×60). Pembeli datang dari post
Threads jujur + angka nyata, dan tryout gratis sebagai pancingan.

Pelajaran: kuncinya NICHE — ujian wajib, taruhannya karier, peserta banyak, alat latihan sedikit.

Kandidat niche: lisensi agen asuransi (AAJI/AAUI), sertifikasi PBJ (LKPP), manajemen risiko perbankan,
WAPERD/WPPE, psikotes rekrutmen BUMN/swasta, PCPM BI, OJK, sertifikasi industri yang sedang tumbuh.

## Rencana
- **Tahap 1 — Validasi** (riset, belum membangun): jumlah peserta/tahun, pesaing (harga, kualitas),
  ketersediaan kisi-kisi publik, tingkat kewajiban ujian → rekomendasi 1 niche. Hasil: `docs/riset-tahap1.md`.
- **Tahap 2 — MVP** (±2–3 minggu): landing page + 1 tryout gratis (30–50 soal + pembahasan) + 1 paket berbayar;
  mesin tryout (timer, skor, pembahasan, riwayat nilai); Cloudflare Pages (+ Workers/D1 untuk akun & akses);
  pembayaran via link payment gateway (Mayar, LinkQu, dsb — cek fee); alur soal: Gemini draf dari kisi-kisi → verifikasi manusia.
- **Tahap 3 — Distribusi**: Ivan TIDAK mau post Threads/medsos pribadi. Fokus: SEO (long-tail, tryout gratis terindeks), afiliasi leader agency, konten faceless (ElevenLabs), iklan hanya dari omzet (bukan modal awal).

## Status
- [x] CLAUDE.md dibuat
- [x] Tahap 1 riset desk selesai → rekomendasi CLIDA (LSP AAJI), lihat docs/riset-tahap1.md
- [x] Landing page + 5 artikel SEO + program mitra/afiliasi (Pages Functions + D1) — lihat docs/DEPLOY.md
- [x] Fakta artikel diverifikasi dari situs resmi (LSP AAJI, SKKNI 12/2024, POJK 8/2024) — lihat docs/verifikasi-soal.md
- [x] 5 soal contoh diverifikasi Ivan; situs LIVE di https://marikitaujian.pages.dev (D1 `marikitaujian`, APAC)
- Deploy ulang: `wrangler pages deploy --branch main` (login wrangler via OAuth sudah tersimpan di laptop Ivan)
- [x] Google Search Console terverifikasi, sitemap dikirim (16 Nov 2026)
- [x] Struktur MULTI-UJIAN: / = hub, /clida/ = landing CLIDA, /clida/artikel/<slug>; redirect 301 dari /artikel/*.
      Tambah ujian: entri EXAMS di tools/build.py + UJIAN di functions/api/waitlist.js + public/<ujian>/index.html.
- Gemini API key ada di env user GEMINI_API_KEY (baca dari registry, jangan dicetak). Free tier: pakai gemini-flash-latest (Pro kena 429).
- KEPUTUSAN 16 Nov 2026: pembayaran = Mayar produk e-book (opsi A, lihat docs/produk-digital.md); domain = marikitaujian.com via Cloudflare Registrar (Ivan yang membayar).
- Ekstensi Claude in Chrome sudah terpasang di Edge Ivan (cek dengan list_connected_browsers di sesi berikut).
- [ ] Beli domain → hubungkan ke Pages, ganti SITE di tools/build.py + canonical, kirim ulang sitemap di Search Console
- [ ] Pilot 18 soal (content/clida/soal) menunggu verifikasi Ivan; cek silang Gemini 10/10 cocok (indikasi soal terlalu mudah)
- Kerja lokal di Windows (PowerShell). Situs .go.id/.or.id kadang 403 untuk WebFetch → pakai curl.exe dengan User-Agent browser.
- [ ] Validasi via SEO: pantau pendaftar waitlist 4–6 minggu (Ivan tidak bisa tanya agen langsung)

## Struktur repo
- `public/` situs statis (Cloudflare Pages). `functions/api/` = endpoint `waitlist` & `mitra` (D1 binding `DB`).
- `content/<ujian>/artikel/*.html` sumber artikel → `python3 tools/build.py` membangun `public/<ujian>/artikel/`, sitemap, robots.
- Referral: `?ref=KODE` disimpan 60 hari di localStorage, ikut terkirim saat daftar waitlist. Komisi mitra 25% (dihitung manual dari D1).
- URL tanpa `.html` (Cloudflare Pages me-redirect .html → 308).
