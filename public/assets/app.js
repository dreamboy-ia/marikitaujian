// Mari Kita Ujian — tracking referral, kuis contoh, dan form.
(function () {
  "use strict";
  var REF_KEY = "mku_ref";
  var REF_DAYS = 60;

  // 1) Simpan kode referral dari ?ref=KODE (berlaku 60 hari, klik terakhir yang dihitung)
  function saveRef() {
    try {
      var p = new URLSearchParams(location.search);
      var r = (p.get("ref") || "").trim().toUpperCase();
      if (r && /^[A-Z0-9-]{3,32}$/.test(r)) {
        localStorage.setItem(REF_KEY, JSON.stringify({ code: r, exp: Date.now() + REF_DAYS * 864e5 }));
      }
    } catch (e) {}
  }
  function getRef() {
    try {
      var v = JSON.parse(localStorage.getItem(REF_KEY) || "null");
      if (v && v.exp > Date.now()) return v.code;
    } catch (e) {}
    return "";
  }
  saveRef();

  // 2) Kuis contoh
  function initQuiz(root) {
    var data;
    try { data = JSON.parse(document.getElementById(root.dataset.src).textContent); } catch (e) { return; }
    var i = 0, score = 0;
    function render() {
      if (i >= data.length) return done();
      var q = data[i];
      root.innerHTML =
        '<div class="progress"><i style="width:' + (i / data.length) * 100 + '%"></i></div>' +
        '<div class="q"><div class="q-meta"><span>Soal ' + (i + 1) + " dari " + data.length + "</span><span>" + q.topik + "</span></div>" +
        '<p class="q-text"></p><div class="opts"></div><div class="after"></div></div>';
      root.querySelector(".q-text").textContent = q.soal;
      var box = root.querySelector(".opts");
      q.opsi.forEach(function (o, k) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "opt";
        b.textContent = String.fromCharCode(65 + k) + ". " + o;
        b.onclick = function () { answer(k); };
        box.appendChild(b);
      });
    }
    function answer(k) {
      var q = data[i];
      var btns = root.querySelectorAll(".opt");
      btns.forEach(function (b, j) {
        b.disabled = true;
        if (j === q.kunci) b.classList.add("right");
        else if (j === k) b.classList.add("wrong");
      });
      if (k === q.kunci) score++;
      var after = root.querySelector(".after");
      var ex = document.createElement("div");
      ex.className = "expl";
      ex.textContent = (k === q.kunci ? "Benar. " : "Belum tepat. ") + q.bahas;
      after.appendChild(ex);
      var nx = document.createElement("button");
      nx.type = "button"; nx.className = "btn"; nx.style.marginTop = "14px";
      nx.textContent = i + 1 < data.length ? "Soal berikutnya →" : "Lihat skor";
      nx.onclick = function () { i++; render(); };
      after.appendChild(nx);
      nx.focus();
    }
    function done() {
      var pct = Math.round((score / data.length) * 100);
      var verdict = pct >= 80 ? "Dasarnya sudah kuat. Uji diri dengan tryout lengkap sebelum hari-H."
        : pct >= 60 ? "Lumayan, tapi masih ada celah. Di ujian sungguhan soalnya lebih banyak dan lebih detail."
        : "Masih banyak yang perlu diulang. Lebih baik ketahuan sekarang daripada saat ujian.";
      root.innerHTML =
        '<div class="q"><p class="note">Skor kamu</p><div class="score">' + score + "/" + data.length + " (" + pct + "%)</div>" +
        "<p>" + verdict + "</p>" +
        '<p class="note">Ini baru ' + data.length + " soal. Tryout lengkap CLIDA (40 soal, timer, pembahasan tiap soal, dan peta topik lemah) dibuka gratis untuk pendaftar awal.</p>" +
        '<div class="cta-row"><a class="btn" href="#daftar">Daftar akses tryout gratis</a>' +
        '<button type="button" class="btn ghost" id="qz-again">Ulangi</button></div></div>';
      document.getElementById("qz-again").onclick = function () { i = 0; score = 0; render(); };
      try { localStorage.setItem("mku_quiz_score", String(pct)); } catch (e) {}
    }
    render();
  }
  document.querySelectorAll("[data-quiz]").forEach(initQuiz);

  // 3) Form (waitlist & mitra)
  document.querySelectorAll("form[data-endpoint]").forEach(function (form) {
    var refInput = form.querySelector('input[name="ref"]');
    if (refInput && !refInput.value) refInput.value = getRef();
    var scoreInput = form.querySelector('input[name="skor"]');
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (scoreInput) { try { scoreInput.value = localStorage.getItem("mku_quiz_score") || ""; } catch (e) {} }
      var out = form.querySelector(".out");
      var btn = form.querySelector('button[type="submit"]');
      var body = {};
      new FormData(form).forEach(function (v, k) { body[k] = String(v).trim(); });
      btn.disabled = true; out.innerHTML = "";
      fetch(form.dataset.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok) throw new Error(res.j.error || "Gagal mengirim");
          if (res.j.link) {
            out.innerHTML = '<div class="msg ok">Pendaftaran mitra berhasil. Kode kamu: <b></b></div>' +
              '<div class="reflink"><input readonly><button type="button" class="btn">Salin link</button></div>' +
              '<p class="note">Bagikan link ini. Setiap orang yang mendaftar dan membeli lewat link ini dicatat atas nama kamu.</p>';
            out.querySelector("b").textContent = res.j.code;
            var inp = out.querySelector("input"); inp.value = res.j.link;
            out.querySelector(".reflink .btn").onclick = function () {
              inp.select();
              (navigator.clipboard ? navigator.clipboard.writeText(res.j.link) : Promise.reject()).then(
                function () { this.textContent = "Tersalin ✓"; }.bind(this),
                function () { document.execCommand("copy"); }
              );
            };
          } else {
            out.innerHTML = '<div class="msg ok"></div>';
            out.firstChild.textContent = res.j.message || "Terima kasih, kamu sudah terdaftar.";
            form.reset();
          }
        })
        .catch(function (e) {
          out.innerHTML = '<div class="msg err"></div>';
          out.firstChild.textContent = e.message + ". Coba lagi sebentar lagi.";
        })
        .finally(function () { btn.disabled = false; });
    });
  });
})();
