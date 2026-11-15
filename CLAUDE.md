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
- [ ] Validasi lapangan (cek format ujian, tanya agen, post Threads waitlist)
