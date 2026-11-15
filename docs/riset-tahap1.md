# Riset Tahap 1 — Validasi Niche (15 Nov 2026)

## Ringkasan
**Rekomendasi: Sertifikasi kompetensi agen asuransi jiwa — skema CLIDA dari LSP AAJI.**
Alasannya: ujian ini baru diwajibkan, pesertanya ratusan ribu, dan alat latihan untuk format barunya praktis belum ada.
Cadangan: Sertifikasi PBJ Level 1 (LKPP). WAPERD tidak direkomendasikan.

## Perbandingan

| Kriteria | CLIDA (LSP AAJI) | PBJ Level 1 (LKPP) | WAPERD (TICMI/LSP) |
|---|---|---|---|
| Wajib? | Ya. Wajib bagi tenaga pemasar asuransi jiwa mulai 1 Jul 2026 (POJK 23/2023), bertahap s.d. 2030 | Ya, untuk PPK/pokja/pengelola PBJ | Ya, untuk penjual reksa dana di bank |
| Calon peserta | 225–230 rb agen (AAJI); OJK menyebut 471.038 agen di SPRINT. Target 100 rb tersertifikasi tahun ini | Kekurangan JF Pengelola PBJ: butuh 19.064, baru ada 11.221 (Jun 2026). Ditambah PPK/ASN lain, puluhan ribu/tahun (angka nasional belum ketemu) | Tidak ada data. Kemungkinan ribuan/tahun |
| Biaya ujian resmi | Rp350.000 | Umumnya dibiayai instansi | Ujian ±Rp1,85 jt + pelatihan Rp1,65–4,2 jt |
| Pesaing | Hanya soal **lisensi AAJI lama** (2013–2015) di Scribd/blog/PDFCoffee. Untuk skema CLIDA yang baru belum ketemu tryout | **Banyak yang gratis**: 6 tryout di Pusdiklat BRIN, kuis Wayground, Studipedia, SlideShare. Pelatihan berbayar Rp5,5 jt+ | Tryout sudah dibundel di paket pelatihan Rp4 jt (ESG Solusi, TICMI) |
| Materi publik | SKKNI asuransi, POJK 23/2023, regulasi OJK, skema di situs LSP AAJI | Perpres 16/2018 jo. 12/2021 jo. 46/2025, Peraturan LKPP, materi resmi LKPP | Regulasi pasar modal (UU P2SK, POJK reksa dana) |
| Mau bayar Rp10–60 rb? | Tinggi. Kalau gagal, harus bayar ujian ulang Rp350 rb dan target kantor tertunda. Leader agency bisa beli untuk satu tim | Sedang, karena alternatif gratisnya banyak | Rendah, karena kantor biasanya membayarkan paket lengkap |
| Mudah dijangkau? | Sangat mudah. Agen aktif di medsos dan grup WA agency | Sedang (komunitas ASN, grup PBJ) | Sulit (karyawan bank) |

## Kenapa CLIDA
1. **Waktunya pas.** Kewajiban baru berlaku Juli 2026 dan LSP AAJI baru dapat izin OJK pada 29 Jul 2026. Ratusan ribu agen harus ujian bertahap sampai 2030, jadi pasarnya ada selama ±4 tahun.
2. **Bank soal lama sudah usang.** Soal yang beredar dibuat untuk ujian lisensi lama, bukan untuk unit kompetensi CLIDA. Siapa yang lebih dulu punya tryout CLIDA berbasis SKKNI punya peluang besar.
3. **Polanya sama dengan siapukom.** Ujiannya wajib, menyangkut penghasilan, pesertanya banyak, dan alat latihannya sedikit. Bedanya, agen asuransi sudah terbiasa jualan online, sehingga penyebaran dari mulut ke mulut lewat grup agency kemungkinan lebih cepat.
4. **Ada pembeli B2B.** Leader/agency manager dinilai dari jumlah agen yang lulus. Paket tim (mis. 10 akun) bisa jadi produk dengan harga tinggi.

## Risiko CLIDA (harus dicek sebelum membangun)
- **Format ujian belum diketahui.** Uji kompetensi BNSP sering menggabungkan tes tertulis, wawancara, dan portofolio. Kalau porsi pilihan gandanya kecil, nilai jual tryout turun. Produk bisa diperluas dengan simulasi wawancara dan contoh portofolio.
- Perusahaan asuransi besar mungkin menyediakan pelatihan internal gratis.
- Angka 225 rb vs 471 rb agen belum jelas. Pakai angka konservatif.
- Situs `lsp.aaji.or.id` tidak bisa diakses dari sesi cloud ini (diblokir jaringan), jadi detail skema dan unit kompetensi belum saya baca langsung.

## Cadangan: PBJ Level 1
Pembelinya ASN, sama seperti siapukom, dan sudah terbiasa ikut tryout. Kelemahannya, sudah banyak tryout gratis. Untuk bisa bersaing butuh kelebihan yang jelas, misalnya soal yang diperbarui sesuai Perpres 46/2025 (banyak soal gratis masih memakai aturan lama), pembahasan yang mengutip pasal, dan analisis kelemahan per topik.

## Temuan sampingan: USKP (Ujian Sertifikasi Konsultan Pajak)
±2.000 peserta Tingkat A per periode, beberapa periode setahun. Tingkat kelulusannya sangat rendah (Tingkat A 16–21%, Tingkat B ~5%). Taruhannya tinggi dan banyak yang mengulang. Layak divalidasi sebagai niche ke-2 setelah MVP pertama jalan.

## Payment gateway (catatan awal)
- Mayar: biaya admin tergantung produk/paket, biaya tarik dana Rp2.775 flat. Persentase pastinya perlu dicek di docs.mayar.id.
- BI memberlakukan MDR QRIS 0% untuk transaksi kecil usaha mikro mulai 1 Okt 2026 (batasnya Rp100 rb atau Rp500 rb, sumber berbeda). Ini menguntungkan paket Rp10–60 rb. Cek apakah gateway ikut meneruskan tarif ini.

## Alur soal dengan Gemini (penilaian awal)
Gemini cukup andal untuk **draf** soal konsep dari teks regulasi yang ditempelkan langsung ke prompt (bukan dari ingatan model). Kesalahannya biasanya di angka, tenggat, nomor pasal, dan aturan yang sudah direvisi. Alur yang disarankan:
1. Tempel teks sumber (SKKNI/POJK) → Gemini membuat soal + kunci + pembahasan + **kutipan pasal**.
2. Pemeriksaan silang otomatis (Gemini/Claude menjawab soal tanpa melihat kunci; soal yang jawabannya tidak cocok ditandai).
3. Verifikasi manusia (Ivan, atau agen berlisensi untuk CLIDA) sebelum terbit.
Ini akan diuji dengan 10 soal di awal Tahap 2.

## Langkah validasi murah (sebelum membangun, ±1 minggu)
1. Ivan membuka lsp.aaji.or.id secara manual: format ujian, unit kompetensi CLIDA, dan materi uji.
2. Tanya 3–5 agen/leader asuransi yang dikenal: sudah ujian? Formatnya seperti apa? Mau bayar Rp25–50 rb untuk tryout?
3. Satu post Threads/grup FB agen: "lagi bikin tryout gratis CLIDA, yang mau daftar tunggu?" Target ≥50 pendaftar dalam seminggu sebelum mulai coding.

## Sumber
- https://keuangan.kontan.co.id/news/industri-asuransi-jiwa-stabil-fokus-bergeser-ke-sertifikasi-dan-kualitas-agen
- https://investortrust.id/financial/112808/ojk-ingatkan-ratusan-ribu-agen-asuransi-untuk-miliki-sertifikasi-resmi-lsp-terbaru
- https://www.investortrust.id/financial/106770/tahun-ini-aaji-targetkan-100000-agen-asuransi-tersertifikasi
- https://www.antaranews.com/berita/5719632/aaji-memperkuat-kompetensi-sdm-asuransi-jiwa-dengan-pemanfaatan-ai
- https://lsp.aaji.or.id/ (via hasil pencarian)
- https://pbj.kotawaringinbaratkab.go.id/d_berita/lkpp-terbitkan-se-nomor-2-tahun-2026-percepatan-pemenuhan-pengelola-pbj-di-tengah-defisit-sdm
- https://jdih.lkpp.go.id/regulation/download/surat-edaran-kepala-lkpp-nomor-1-tahun-2024/1
- https://pusdiklat.brin.go.id/try-out-online-pbj/
- https://pusdiklatpemerintahanri.id/ujian-sertifikasi-pengadaan-barang-jasa-pemerintah/
- https://ticmi.co.id/program-schedule
- https://esgsolusi.id/sertifikasi-waperd/
- https://ikpi.or.id/?p=20521 ; https://ikpi.or.id/en/?p=22039
- https://docs.mayar.id/mor/fees.md
- https://www.rctiplus.com/news/detail/terkini/5453488/biaya-transaksi-qris-gratis-bagi-semua-merchant-mulai-1-oktober-2026
