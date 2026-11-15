import { json, readBody, clean, isEmail, normWa } from "./_util.js";

const PERAN = ["leader", "trainer", "agen", "komunitas", "lainnya"];
const TIM = ["1-10", "11-50", "51-200", "200+"];
const ALPHA = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // tanpa 0/O/1/I agar tidak tertukar

function makeCode(nama) {
  const base = nama.normalize("NFKD").replace(/[^A-Za-z]/g, "").toUpperCase().slice(0, 6) || "MITRA";
  const r = crypto.getRandomValues(new Uint8Array(4));
  return base + "-" + Array.from(r, (x) => ALPHA[x % ALPHA.length]).join("");
}

export async function onRequestPost({ request, env }) {
  let b;
  try { b = await readBody(request); } catch (e) { return json({ error: e.message }, 400); }
  if (b.website) return json({ error: "Gagal" }, 400);

  const nama = clean(b.nama, 80);
  const email = clean(b.email, 120).toLowerCase();
  const wa = normWa(clean(b.wa, 20));
  if (!nama) return json({ error: "Nama wajib diisi" }, 400);
  if (!isEmail(email)) return json({ error: "Email tidak valid" }, 400);
  if (!wa) return json({ error: "Nomor WhatsApp tidak valid" }, 400);
  if (b.setuju !== "ya") return json({ error: "Centang persetujuan ketentuan dulu" }, 400);

  const origin = new URL(request.url).origin;
  try {
    const existing = await env.DB.prepare("SELECT code FROM mitra WHERE email=?1").bind(email).first();
    if (existing) return json({ code: existing.code, link: `${origin}/?ref=${existing.code}` });

    for (let i = 0; i < 5; i++) {
      const code = makeCode(nama);
      try {
        await env.DB.prepare(
          "INSERT INTO mitra (code,nama,email,wa,peran,tim,kanal) VALUES (?1,?2,?3,?4,?5,?6,?7)"
        ).bind(code, nama, email, wa,
          PERAN.includes(b.peran) ? b.peran : "lainnya",
          TIM.includes(b.tim) ? b.tim : null,
          clean(b.kanal, 160) || null).run();
        return json({ code, link: `${origin}/?ref=${code}` });
      } catch (e) {
        if (!String(e.message || e).includes("UNIQUE")) throw e; // bentrok kode → coba lagi
      }
    }
    return json({ error: "Gagal membuat kode" }, 500);
  } catch (e) {
    return json({ error: "Server sedang bermasalah" }, 500);
  }
}

export const onRequest = () => json({ error: "Method not allowed" }, 405);
