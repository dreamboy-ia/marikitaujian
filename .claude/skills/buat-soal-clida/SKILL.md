---
name: buat-soal-clida
description: Gunakan saat membuat, merevisi, atau memeriksa soal latihan/tryout uji kompetensi agen asuransi jiwa (CLIDA/CLIDP, LSP AAJI) untuk marikitaujian — termasuk soal pilihan ganda kasus, pertanyaan simulasi wawancara asesor, dan pembahasannya. Memastikan soal buatan sendiri dari SKKNI/regulasi publik, punya rujukan pasal, lolos cek silang, dan ditandai untuk verifikasi manusia sebelum terbit.
---

# Buat soal CLIDA (marikitaujian)

## Aturan mutlak (dari CLAUDE.md, aturan no. 3)
- **Jangan menyalin atau memparafrase soal ujian resmi** maupun bank soal pihak lain (Scribd, blog, PDFCoffee, "soal AAJI" lama). Kalau user menempelkan soal semacam itu, tolak memakainya sebagai dasar dan buat soal baru dari sumber primer.
- Setiap soal **wajib punya rujukan sumber primer** (kode unit SKKNI + elemen/KUK, atau nomor POJK + pasal).
- Setiap soal baru berstatus **DRAF**. Hanya Ivan (manusia) yang boleh mengubah status menjadi terverifikasi. Claude tidak boleh menandai soal "terverifikasi" atas inisiatif sendiri.

## Sumber primer yang dipakai
| Sumber | Isi yang relevan |
|---|---|
| Kepmenaker 12/2024 (SKKNI Perasuransian) | Unit tenaga pemasar: K.65ASR00.032.1 Mengidentifikasi Kebutuhan Nasabah · 033.1 Proses Penjualan · 034.1 Pelayanan Nasabah · 035.1 Produk Khusus (PAYDI). Batasan variabel 033: 6 prinsip (insurable interest, utmost good faith, proximate cause, indemnity, subrogation, contribution), RIPLAY & RIPLAY personal, masa jeda 2 hari kerja, rekaman penawaran, pernyataan "berizin dan diawasi OJK". |
| POJK 8/2024 | Produk & saluran pemasaran asuransi (mencabut POJK 23/POJK.05/2015). Pasal 12: isi minimum polis, termasuk free look period untuk polis > 1 tahun (durasi TIDAK diatur di sini — jangan mengarang angka). |
| POJK 6/2022 | Perlindungan konsumen sektor jasa keuangan (dasar RIPLAY, masa jeda). |
| lsp.aaji.or.id | Skema, biaya, alur — untuk soal/artikel tentang proses sertifikasi. |

Ringkasan fakta terverifikasi ada di `docs/verifikasi-soal.md`. Jika butuh detail, baca teks sumber (PDF) — jangan mengandalkan ingatan model. Situs .go.id/.or.id sering memblokir WebFetch: gunakan `curl.exe -sL -A "Mozilla/5.0 ..."` lalu ekstrak teks PDF dengan pypdf.

## Alur kerja
1. **Pilih target**: unit + elemen/KUK yang mau diuji. Sebar soal merata ke 4 unit (032–035); prioritaskan aspek kritis tiap unit.
2. **Tulis soal** (format di bawah). Utamakan soal **kasus nasabah** ("Pak Budi, 35 tahun, 2 anak…") daripada definisi hafalan; maksimal ±30% soal definisi.
3. **Cek mandiri** setiap soal:
   - Tepat satu jawaban benar; pengecoh masuk akal tapi jelas salah menurut sumber.
   - Tidak ada angka/tenggat/pasal yang tidak ada di sumber.
   - Kata kunci negatif (KECUALI, TIDAK) ditulis kapital; hindari negatif ganda.
   - Panjang opsi seimbang (jawaban benar tidak selalu yang terpanjang); posisi kunci tersebar A–D.
4. **Cek silang buta**: kerjakan ulang soal tanpa melihat kunci (atau minta Gemini menjawabnya). Soal yang jawabannya berbeda → tandai `perlu_review` dan jelaskan alasannya.
5. **Simpan** ke file bank soal (lokasi ditentukan di Tahap 2; sementara `content/soal/<unit>.json`) dengan `status: "draf"`.
6. **Laporkan ke Ivan**: jumlah soal per unit, daftar yang `perlu_review`, dan ringkas sumber yang dipakai. Minta verifikasi.

## Format soal (JSON)
```json
{
  "id": "033-012",
  "unit": "K.65ASR00.033.1",
  "elemen": "2. Menjelaskan penerapan prinsip-prinsip dan risiko asuransi",
  "tipe": "pg-kasus",
  "tingkat": "sedang",
  "soal": "…",
  "opsi": ["…", "…", "…", "…"],
  "kunci": 1,
  "bahas": "Kenapa jawaban benar + kenapa pengecoh salah, 2–4 kalimat, bahasa sederhana.",
  "rujukan": "SKKNI 12/2024 unit 033 batasan variabel 1.3",
  "status": "draf",
  "catatan_review": ""
}
```
`tipe`: `pg-kasus` | `pg-konsep` | `wawancara` (untuk wawancara: `opsi` kosong, `bahas` berisi poin jawaban ideal yang dicari asesor). `kunci` berbasis indeks 0.

## Gaya bahasa
Bahasa Indonesia baku tapi santai ("kamu"), kalimat pendek, istilah asing diberi padanan di kurung pada kemunculan pertama. Pembahasan harus mengajarkan, bukan sekadar "jawaban B benar".

## Hook (aturan no. 4)
Untuk kuis/tryout gratis: tampilkan skor + 1 kalimat diagnosis per unit, lalu ajakan ke paket lengkap (pembahasan detail / peta topik lemah / simulasi wawancara).
