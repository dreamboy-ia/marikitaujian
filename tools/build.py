#!/usr/bin/env python3
"""Bangun halaman artikel dari content/artikel/*.html + index artikel + sitemap.xml.
Format file konten: baris pertama JSON {"title","desc","date","h1"}, sisanya HTML isi artikel.
Jalankan: python3 tools/build.py
"""
import json, pathlib, html, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://marikitaujian.pages.dev"  # ganti jika pakai domain sendiri
SRC, OUT = ROOT / "content/artikel", ROOT / "public/artikel"
OUT.mkdir(parents=True, exist_ok=True)

ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' "
        "fill='%230f5c4d'/%3E%3Cpath d='M9 17l5 5 9-11' stroke='white' stroke-width='3.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")
HEAD = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Mari Kita Ujian</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="{icon}">
{ld}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="logo" href="/">Mari Kita <span>Ujian</span></a>
  <nav><a href="/#coba">Coba soal</a><a href="/artikel/">Artikel</a><a href="/mitra">Jadi mitra</a></nav>
</div></header>
<main><div class="wrap">
"""
FOOT = """
</div></main>
<footer><div class="wrap">
  <p>© 2026 Mari Kita Ujian. Layanan latihan independen, tidak berafiliasi dengan AAJI, LSP AAJI, BNSP, maupun OJK. Informasi di artikel bisa berubah; selalu cek sumber resmi.</p>
  <p><a href="/">Beranda</a> · <a href="/artikel/">Artikel</a> · <a href="/mitra">Program mitra</a></p>
</div></footer>
<script src="/assets/app.js" defer></script>
</body>
</html>
"""
CTA = """<div class="callout"><b>Sudah siap ujian?</b>
<p>Coba 5 soal latihan CLIDA gratis lengkap dengan pembahasan, lalu daftar akses tryout lengkap (gratis untuk pendaftar awal).</p>
<div class="cta-row"><a class="btn" href="/#coba">Coba 5 soal gratis</a><a class="btn ghost" href="/#daftar">Daftar tryout</a></div></div>"""

def fmt_date(d):
    bulan = "Januari Februari Maret April Mei Juni Juli Agustus September Oktober November Desember".split()
    y, m, dd = map(int, d.split("-"))
    return f"{dd} {bulan[m-1]} {y}"

posts = []
for f in sorted(SRC.glob("*.html")):
    first, body = f.read_text(encoding="utf-8").split("\n", 1)
    meta = json.loads(first)
    slug = f.stem
    url = f"{SITE}/artikel/{slug}"
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": meta["h1"], "description": meta["desc"],
          "datePublished": meta["date"], "dateModified": meta.get("updated", meta["date"]),
          "author": {"@type": "Organization", "name": "Mari Kita Ujian"}, "mainEntityOfPage": url}
    page = HEAD.format(title=html.escape(meta["title"]), desc=html.escape(meta["desc"]), url=url, ogtype="article", icon=ICON,
                       ld='<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>")
    page += f'<p class="crumb"><a href="/">Beranda</a> › <a href="/artikel/">Artikel</a></p>\n<article class="post">\n'
    page += f'<h1>{meta["h1"]}</h1>\n<p class="meta">Diperbarui {fmt_date(meta.get("updated", meta["date"]))}</p>\n'
    page += body.replace("<!--CTA-->", CTA) + "\n</article>" + FOOT
    (OUT / f"{slug}.html").write_text(page, encoding="utf-8")
    posts.append((slug, meta))

# index artikel
idx = HEAD.format(title="Artikel persiapan uji kompetensi agen asuransi jiwa (CLIDA)",
                  desc="Kumpulan panduan persiapan sertifikasi kompetensi agen asuransi jiwa: CLIDA, biaya dan alur ujian LSP AAJI, materi, dan tips asesmen.",
                  url=f"{SITE}/artikel/", ogtype="website", icon=ICON, ld="")
idx += '<article class="post"><h1>Artikel persiapan uji kompetensi</h1><div class="grid" style="grid-template-columns:1fr">\n'
for slug, m in posts:
    idx += f'<a class="card" href="/artikel/{slug}"><h3>{m["h1"]}</h3><p>{html.escape(m["desc"])}</p></a>\n'
idx += "</div>" + CTA + "</article>" + FOOT
(OUT / "index.html").write_text(idx, encoding="utf-8")

# sitemap
today = datetime.date.today().isoformat()
urls = [(f"{SITE}/", today), (f"{SITE}/mitra", today), (f"{SITE}/artikel/", today)]
urls += [(f"{SITE}/artikel/{s}", m.get("updated", m["date"])) for s, m in posts]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls) + "</urlset>\n"
(ROOT / "public/sitemap.xml").write_text(sm, encoding="utf-8")
(ROOT / "public/robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print(f"{len(posts)} artikel dibangun")
