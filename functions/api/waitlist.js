import { json, readBody, clean, isEmail, normWa } from "./_util.js";

// Tambahkan slug ujian baru di sini saat membuka ujian baru.
const UJIAN = ["clida"];

export async function onRequestPost({ request, env }) {
  let b;
  try { b = await readBody(request); } catch (e) { return json({ error: e.message }, 400); }
  if (b.website) return json({ message: "Terima kasih, kamu sudah terdaftar." }); // honeypot: bot

  const nama = clean(b.nama, 80);
  const email = clean(b.email, 120).toLowerCase();
  const waRaw = clean(b.wa, 20);
  const wa = waRaw ? normWa(waRaw) : "";
  const ujian = UJIAN.includes(b.ujian) ? b.ujian : UJIAN[0];
  const status = /^[a-z-]{2,30}$/.test(String(b.status || "")) ? b.status : "lainnya";
  const ref = /^[A-Z0-9-]{3,32}$/.test(String(b.ref || "")) ? b.ref : null;
  const skorN = parseInt(b.skor, 10);
  const skor = Number.isFinite(skorN) && skorN >= 0 && skorN <= 100 ? skorN : null;

  if (!nama) return json({ error: "Nama wajib diisi" }, 400);
  if (!isEmail(email)) return json({ error: "Email tidak valid" }, 400);
  if (waRaw && !wa) return json({ error: "Nomor WhatsApp tidak valid" }, 400);

  try {
    // Email + ujian yang sama → perbarui data, tapi ref pertama tetap dipertahankan
    await env.DB.prepare(
      `INSERT INTO waitlist (ujian,nama,email,wa,status,ref,skor,sumber) VALUES (?1,?2,?3,?4,?5,?6,?7,?8)
       ON CONFLICT(email,ujian) DO UPDATE SET nama=excluded.nama, wa=COALESCE(excluded.wa,waitlist.wa),
       status=excluded.status, skor=COALESCE(excluded.skor,waitlist.skor), ref=COALESCE(waitlist.ref,excluded.ref)`
    ).bind(ujian, nama, email, wa || null, status, ref, skor, clean(request.headers.get("referer"), 200)).run();
  } catch (e) {
    return json({ error: "Server sedang bermasalah" }, 500);
  }
  const tambahan = {
    "agen-gagal": " Sambil menunggu, minta umpan balik dari asesor tentang unit yang dinilai belum kompeten, lalu mulai dari unit itu.",
    "leader": " Untuk menyiapkan satu tim sekaligus, daftar juga di program mitra (menu Jadi mitra): kamu dapat link khusus dan komisi 25%.",
    "calon-agen": " Sambil menunggu, baca artikel materi uji kompetensi untuk mengenal 4 unit yang diuji.",
  }[status] || "";
  return json({ message: `Terima kasih, ${nama}! Kamu sudah terdaftar. Kami kabari begitu tryout lengkap dibuka.${tambahan}` });
}

export const onRequest = () => json({ error: "Method not allowed" }, 405);
