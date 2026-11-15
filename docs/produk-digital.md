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
