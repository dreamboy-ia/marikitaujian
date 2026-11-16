#!/usr/bin/env python3
"""Bangun e-book "Panduan Wawancara Asesor & APL-02 CLIDA" dari content/clida/ebook/wawancara.json.
Hasil: dist/ebook-wawancara-clida.html lalu PDF lewat Edge headless:
  python tools/ebook.py            -> HTML + PDF
Folder dist/ tidak di-commit (produk berbayar).
"""
import json, pathlib, html, subprocess, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = json.loads((ROOT / "content/clida/ebook/wawancara.json").read_text(encoding="utf-8"))
OUT = ROOT / "dist"; OUT.mkdir(exist_ok=True)
H = html.escape
VERSI = "Versi 1.0 · " + datetime.date.today().strftime("%d/%m/%Y")
DRAF = D.get("status") == "draf"

CSS = """
@page{size:A4;margin:18mm 16mm 20mm}
*{box-sizing:border-box}
body{font-family:"Segoe UI",system-ui,sans-serif;color:#1c2321;font-size:10.5pt;line-height:1.55;margin:0}
h1,h2,h3{line-height:1.25;margin:0 0 8px;color:#0f5c4d}
h1{font-size:26pt}h2{font-size:16pt;margin-top:4px}h3{font-size:12pt}
.cover{height:257mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always;border-left:10px solid #0f5c4d;padding-left:22px}
.cover .tag{color:#d9822b;font-weight:700;letter-spacing:.04em}
.cover p{font-size:12pt;color:#5b6662;max-width:140mm}
.cover .foot{margin-top:40mm;font-size:9pt;color:#5b6662}
.bab{page-break-before:always}
.box{border:1px solid #e2e0d8;border-radius:8px;padding:10px 12px;margin:10px 0;background:#f7f6f2;page-break-inside:avoid}
.q{border-top:2px solid #0f5c4d;padding-top:8px;margin:16px 0 4px;page-break-inside:avoid}
.q .id{font-size:8.5pt;color:#5b6662}
.q .tanya{font-weight:700;font-size:11pt;margin:2px 0 6px}
.lbl{font-weight:700;font-size:9pt;color:#0f5c4d;text-transform:none;margin:6px 0 2px}
.contoh{background:#e8f1ee;border-radius:6px;padding:8px 10px}
.hindari{color:#8a2a1f}
ul{margin:2px 0 4px;padding-left:18px}li{margin:1px 0}
table{width:100%;border-collapse:collapse;font-size:9.5pt;margin:8px 0}
th,td{border:1px solid #cfcdc4;padding:5px 6px;text-align:left;vertical-align:top}
th{background:#e8f1ee}
.cb li{list-style:none;margin-left:-18px}.cb li::before{content:"\\2610  ";font-size:11pt}
.toc li{margin:4px 0}
.small{font-size:8.5pt;color:#5b6662}
.draf{position:fixed;top:40%;left:0;right:0;text-align:center;font-size:60pt;color:rgba(217,130,43,.12);transform:rotate(-30deg);z-index:-1}
"""

def li(xs): return "<ul>" + "".join(f"<li>{H(x)}</li>" for x in xs) + "</ul>"

U = D["unit"]; P = D["pertanyaan"]
parts = []
if DRAF: parts.append('<div class="draf">DRAF</div>')
parts.append(f"""<section class="cover">
<div class="tag">MARI KITA UJIAN · CLIDA</div>
<h1>Panduan Wawancara Asesor &amp; APL-02</h1>
<p>Persiapan uji kompetensi agen asuransi jiwa (skema CLIDA, LSP AAJI). Berisi {len(P)} pertanyaan wawancara per unit kompetensi beserta poin yang dicari asesor, contoh jawaban, panduan mengisi APL-02, dan checklist portofolio.</p>
<p class="foot">{VERSI}<br>Disusun dari SKKNI Bidang Perasuransian (Kepmenaker 12/2024) dan POJK 8/2024.<br>
Layanan latihan independen, tidak berafiliasi dengan AAJI, LSP AAJI, BNSP, maupun OJK.<br>
© 2026 Mari Kita Ujian. Untuk penggunaan pribadi pembeli. Dilarang menggandakan atau membagikan ulang.</p>
</section>""")

parts.append("""<section><h2>Daftar isi</h2><ol class="toc">
<li>Cara memakai e-book ini</li><li>Gambaran asesmen kompetensi CLIDA</li>
<li>Pertanyaan wawancara unit 032: Mengidentifikasi Kebutuhan Nasabah</li>
<li>Pertanyaan wawancara unit 033: Proses Penjualan</li>
<li>Pertanyaan wawancara unit 034: Pelayanan Nasabah</li>
<li>Pertanyaan wawancara unit 035: Produk Khusus (PAYDI)</li>
<li>Panduan mengisi APL-02 (asesmen mandiri)</li><li>Checklist portofolio per unit</li>
<li>Checklist hari uji</li><li>Sumber</li></ol>
<h2 style="margin-top:18px">1. Cara memakai e-book ini</h2>
<p>Asesor tidak mencari jawaban hafalan. Asesor ingin yakin kamu bisa melakukan pekerjaan agen dengan benar dan sesuai aturan. Karena itu:</p>
<ul><li>Baca pertanyaannya, lalu jawab dengan suara keras <b>sebelum</b> melihat contoh jawaban.</li>
<li>Bandingkan jawabanmu dengan daftar <i>yang dicari asesor</i>. Poin yang terlewat itulah yang perlu kamu latih.</li>
<li>Ganti contoh jawaban dengan pengalamanmu sendiri. Cerita nyata lebih meyakinkan daripada kalimat yang dihafal.</li>
<li>Latih bersama rekan: satu menjadi asesor, satu menjadi peserta.</li></ul>
<div class="box small">Pertanyaan di e-book ini disusun sendiri dari elemen kompetensi dan kriteria unjuk kerja (KUK) di SKKNI, bukan salinan soal resmi. Pertanyaan asesor yang sebenarnya bisa berbeda kalimatnya, tapi menggali kompetensi yang sama.</div>
</section>""")

parts.append("""<section class="bab"><h2>2. Gambaran asesmen kompetensi CLIDA</h2>
<p><b>Skema:</b> CLIDA (Certified Life Insurance Distribution Associate), jenjang kualifikasi 3, diselenggarakan LSP AAJI. Biaya yang tercantum di situs LSP AAJI: Rp350.000.</p>
<h3>Alur resmi (situs LSP AAJI)</h3>
<ol><li>Agen mengajukan pendaftaran ke perusahaan asuransi.</li><li>Perusahaan mengajukan sertifikasi agen ke LSP AAJI.</li>
<li>Agen melengkapi APL-01, APL-02, dan dokumen persyaratan dasar.</li><li>LSP AAJI menetapkan asesor kompetensi.</li>
<li>Asesor dan agen mengumpulkan bukti, lalu uji kompetensi dilaksanakan.</li><li>Hasil ditetapkan sesuai ketentuan BNSP.</li>
<li>LSP AAJI melakukan pleno berdasarkan rekomendasi asesor.</li><li>Sertifikat diterbitkan bagi agen yang kompeten.</li></ol>
<h3>Metode penilaian (SKKNI)</h3>
<p>Untuk unit tenaga pemasar, SKKNI menyebut penilaian dapat dilakukan dengan demonstrasi, praktik, atau simulasi di TUK, verifikasi bukti atau portofolio, wawancara, tes lisan, tes tertulis, dan/atau metode lain yang relevan. Kombinasi pastinya ditentukan LSP.</p>
<h3>Empat unit kompetensi tenaga pemasar</h3><table><tr><th>Kode</th><th>Unit</th><th>Aspek kritis</th></tr>""")
for k, u in U.items():
    parts.append(f"<tr><td>{H(u['kode'])}</td><td><b>{H(u['judul'])}</b><br><span class='small'>{H(u['ringkas'])}</span></td><td>{li(u['kritis'])}</td></tr>")
parts.append("</table></section>")

n = 3
for k, u in U.items():
    qs = [q for q in P if q["unit"] == k]
    parts.append(f'<section class="bab"><h2>{n}. Unit {k}: {H(u["judul"])}</h2><p class="small">{H(u["kode"])} · {len(qs)} pertanyaan</p><p>{H(u["ringkas"])}</p>')
    for q in qs:
        parts.append(f"""<div class="q"><div class="id">{H(q['id'])} · KUK {H(q['kuk'])}</div>
<div class="tanya">{H(q['tanya'])}</div>
<div class="lbl">Yang dicari asesor</div>{li(q['dicari'])}
<div class="lbl">Contoh jawaban</div><div class="contoh">{H(q['contoh'])}</div>
<div class="lbl">Hindari</div><div class="hindari">{H(q['hindari'])}</div></div>""")
    parts.append("</section>")
    n += 1

parts.append(f"""<section class="bab"><h2>{n}. Panduan mengisi APL-02 (asesmen mandiri)</h2>
<p>APL-02 adalah formulir tempat kamu menilai diri sendiri: untuk setiap kriteria unjuk kerja (KUK), apakah kamu sudah <b>kompeten (K)</b> atau <b>belum kompeten (BK)</b>, beserta bukti yang mendukung. Asesor memakai APL-02 untuk merencanakan apa yang perlu digali. Format resmi diberikan oleh LSP AAJI dan bisa berbeda dari contoh di bawah.</p>
<h3>Prinsip mengisi</h3>
<ul><li><b>Jujur.</b> Klaim K yang tidak didukung bukti akan digali habis saat wawancara.</li>
<li><b>Bukti spesifik.</b> Tulis bukti yang bisa ditunjukkan, bukan kalimat umum seperti "sudah biasa".</li>
<li><b>Samarkan data nasabah.</b> Hitamkan nama, nomor identitas, dan alamat sebelum melampirkan dokumen.</li>
<li><b>Satu bukti bisa dipakai untuk beberapa KUK</b>, asalkan memang relevan.</li></ul>
<h3>Contoh baris (unit 032)</h3>
<table><tr><th>KUK</th><th>Pertanyaan asesmen mandiri</th><th>K/BK</th><th>Bukti yang relevan</th></tr>
<tr><td>1.2</td><td>Dapatkah saya mengumpulkan informasi dan kebutuhan asuransi calon nasabah melalui daftar pertanyaan sesuai prosedur?</td><td>K</td><td>Lembar fact finding 2 calon nasabah (data disamarkan)</td></tr>
<tr><td>1.4</td><td>Dapatkah saya mengonfirmasi kebutuhan calon nasabah sesuai ketentuan?</td><td>K</td><td>Catatan ringkasan kebutuhan yang disetujui nasabah</td></tr>
<tr><td>3.4</td><td>Dapatkah saya menjelaskan konsekuensi pilihan produk sesuai ketentuan organisasi?</td><td>K</td><td>Catatan pertemuan saat nasabah memilih uang pertanggungan lebih kecil</td></tr>
<tr><td>1.5</td><td>Dapatkah saya menilai risiko calon nasabah sesuai kebijakan, peraturan, dan standar organisasi?</td><td>BK</td><td>(Belum punya bukti. Latih dengan alat bantu penilaian risiko dari kantor sebelum asesmen.)</td></tr></table>
<p class="small">Menandai BK bukan aib. Itu menunjukkan kejujuran, dan kamu bisa menyiapkan bukti atau latihan sebelum hari uji.</p></section>""")
n += 1

parts.append(f'<section class="bab"><h2>{n}. Checklist portofolio per unit</h2><p>Kumpulkan dalam satu map atau folder digital, diurutkan per unit. Samarkan semua data pribadi nasabah.</p>')
for k, u in U.items():
    parts.append(f"<h3>Unit {k}: {H(u['judul'])}</h3><ul class='cb'>" + "".join(f"<li>{H(x)}</li>" for x in u["portofolio"]) + "</ul>")
parts.append("</section>")
n += 1

parts.append(f"""<section><h2 style="margin-top:18px">{n}. Checklist hari uji</h2><ul class="cb">
<li>Dokumen asli dan salinan yang diminta LSP (cek pemberitahuan dari perusahaan atau LSP)</li>
<li>Map portofolio yang sudah diurutkan per unit</li><li>Salinan APL-01 dan APL-02 yang sudah kamu isi</li>
<li>Datang lebih awal ke TUK, atau cek perangkat dan koneksi bila asesmen daring</li>
<li>Latihan menjawab 5 pertanyaan acak dari e-book ini dengan suara keras pada malam sebelumnya</li>
<li>Tidur cukup</li></ul></section>""")
n += 1

parts.append(f"""<section class="bab"><h2>{n}. Sumber</h2><ul>
<li>Keputusan Menteri Ketenagakerjaan Nomor 12 Tahun 2024 tentang SKKNI Kategori Aktivitas Keuangan dan Asuransi, Bidang Perasuransian: unit K.65ASR00.032.1 sampai K.65ASR00.035.1 (elemen, KUK, batasan variabel, panduan penilaian).</li>
<li>Peraturan OJK Nomor 8 Tahun 2024 tentang Produk Asuransi dan Saluran Pemasaran Produk Asuransi, Pasal 12.</li>
<li>LSP AAJI, lsp.aaji.or.id: skema CLIDA, alur proses pendaftaran, biaya (diakses 16 November 2026).</li></ul>
<div class="box small">Informasi biaya, alur, dan format formulir dapat berubah. Selalu ikuti ketentuan terbaru dari LSP AAJI dan perusahaanmu. E-book ini adalah bahan latihan dan tidak menjamin hasil asesmen.</div>
<p class="small">{VERSI} · © 2026 Mari Kita Ujian · marikitaujian.pages.dev</p></section>""")

doc = f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Panduan Wawancara Asesor &amp; APL-02 CLIDA</title><style>{CSS}</style></head><body>{"".join(parts)}</body></html>'
hp = OUT / "ebook-wawancara-clida.html"; hp.write_text(doc, encoding="utf-8")

edge = shutil.which("msedge") or r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf = OUT / ("ebook-wawancara-clida" + ("-DRAF" if DRAF else "") + ".pdf")
subprocess.run([edge, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", hp.as_uri()],
               check=True, timeout=120, capture_output=True)
print("PDF:", pdf, pdf.stat().st_size // 1024, "KB")
