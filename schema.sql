-- Jalankan sekali: npx wrangler d1 execute marikitaujian --remote --file=schema.sql
CREATE TABLE IF NOT EXISTS waitlist (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ujian TEXT NOT NULL DEFAULT 'clida',
  nama TEXT NOT NULL,
  email TEXT NOT NULL,
  wa TEXT,
  status TEXT,
  ref TEXT,
  skor INTEGER,
  sumber TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(email, ujian)
);
CREATE TABLE IF NOT EXISTS mitra (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL UNIQUE,
  nama TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  wa TEXT NOT NULL,
  peran TEXT,
  tim TEXT,
  kanal TEXT,
  aktif INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_waitlist_ref ON waitlist(ref);
