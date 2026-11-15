export const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });

export async function readBody(request) {
  const len = Number(request.headers.get("content-length") || 0);
  if (len > 4096) throw new Error("Data terlalu besar");
  try { return await request.json(); } catch { throw new Error("Format data tidak valid"); }
}

export const clean = (v, max) => String(v ?? "").trim().slice(0, max);
export const isEmail = (s) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(s);
export const normWa = (s) => {
  let d = String(s || "").replace(/[^\d+]/g, "").replace(/^\+/, "");
  if (d.startsWith("0")) d = "62" + d.slice(1);
  return /^62\d{8,13}$/.test(d) ? d : "";
};
