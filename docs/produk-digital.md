# Rencana produk digital (draf, 16 Nov 2026)

## Tangga produk (hook → bayar)
| Produk | Isi | Harga usulan | Status |
|---|---|---|---|
| Kuis gratis | 5 soal + skor (beranda) | Gratis | Live |
| Tryout gratis | 40 soal, timer, skor per unit | Gratis (tukar email) | Butuh mesin tryout + 40 soal terverifikasi |
| **E-book 1: Bank Soal CLIDA** | 150–200 soal kasus + pembahasan + rujukan pasal, per unit 032–035 | Rp49.000 | Butuh bank soal terverifikasi |
| **E-book 2: Panduan Wawancara Asesor & APL-02** | ±30 pertanyaan wawancara + poin jawaban ideal, contoh isi APL-02, checklist portofolio | Rp39.000 | Pilot 8 pertanyaan sudah ada |
| Bundle 1 + 2 | — | Rp69.000 | — |
| Paket tim (leader) | Bundle × 10 akun/lisensi | Rp390.000 | — |

Patokan harga: siapukom Rp10rb–64rb; biaya uji CLIDA Rp350rb (gagal = bayar lagi).

## Penjualan & pengiriman: Mayar
- Upload PDF sebagai produk digital → link unduhan dikirim otomatis ke email pembeli setelah bayar.
- Fitur afiliasi Mayar menghitung & mentransfer komisi otomatis → program mitra kita bisa memakai ini
  (link mitra di web diarahkan ke link afiliasi Mayar). Komisi tetap 25%.
- Fee: ±3–4% per transaksi untuk produk digital (cek angka pasti di mayar.id/pricing saat daftar).
- Akun Mayar HARUS dibuat Ivan sendiri (data diri/KYC, rekening pencairan).

## Pembuatan PDF (gratis)
Soal disimpan di `content/soal/*.json` (satu sumber) → skrip membangun HTML cetak → PDF via Chromium/Edge headless
(`msedge --headless --print-to-pdf`). Watermark nama pembeli tidak didukung tanpa backend; cukup footer hak cipta
+ larangan menyebarkan.

## Urutan kerja
1. Ivan verifikasi 18 item pilot (`content/soal/`).
2. Lengkapi bank soal bertahap (±40 soal/sesi kerja untuk hemat kuota) → verifikasi tiap batch.
3. E-book 2 lebih dulu (lebih kecil, pembeda, tidak ada pesaing) → jual via Mayar.
4. Mesin tryout + E-book 1.

## Perbandingan payment gateway (16 Nov 2026)
Contoh e-book Rp49.000:
| Opsi | Biaya/transaksi (QRIS) | Biaya (VA) | Kirim file otomatis | Afiliasi | Kerja teknis |
|---|---|---|---|---|---|
| Mayar Starter | 4% + 0,7% ≈ Rp2.300 | 4% + Rp4.000 ≈ Rp5.960 | Ya | Ya, komisi otomatis | Nol |
| Duitku / Tripay / Midtrans (langsung) | ±0,7% ≈ Rp340 (QRIS ≤Rp100rb bisa 0% per kebijakan BI Okt 2026) | Rp1.500–4.000 | Tidak — harus bangun sendiri (webhook + email) | Tidak — pakai sistem mitra kita | Sedang–besar |
| LinkQu | Tarif merchant tidak dipublikasikan; fokus utamanya transfer | — | Tidak | Tidak | Sedang |
| Scalev | +5% fee ePayment | — | Ya | Ya | Kecil |
Sumber: docs.mayar.id/mor/fees (Starter 4% e-book, QRIS 0,7%, VA Rp4.000, withdraw Rp2.775); artikel perbandingan 2026.
Keputusan: mulai dengan Mayar (tanpa coding, afiliasi otomatis). Pindah ke gateway langsung setelah ada akun/tryout online berbayar
atau penjualan > ±300/bulan (selisih fee mulai lebih besar dari waktu kerja). Arahkan pembeli ke QRIS (fee terendah).
