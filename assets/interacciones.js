/* Interacciones sin backend ni rx.State: modo claro/oscuro y botón "Copiar correo" */
document.addEventListener("click", function (e) {
  if (!e.target.closest("[data-toggle-theme]")) return;
  var r = document.documentElement, n = r.classList.contains("dark") ? "light" : "dark";
  r.classList.remove("light", "dark"); r.classList.add(n); r.style.colorScheme = n;
  try { localStorage.setItem("theme", n); } catch (_) {}
});
document.addEventListener("click", function (e) {
  var b = e.target.closest("[data-copy]");
  if (!b) return;
  var texto = b.getAttribute("data-copy"), original = b.getAttribute("data-label") || b.textContent;
  b.setAttribute("data-label", original);
  function ok() { b.textContent = "¡Copiado!"; setTimeout(function () { b.textContent = original; }, 1800); }
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(texto).then(ok, function () { location.href = "mailto:" + texto; });
  } else { location.href = "mailto:" + texto; }
});
/* Video de demostración: abre el <dialog>, reproduce y pausa al cerrar */
document.addEventListener("click", function (e) {
  var b = e.target.closest("[data-open-dialog]");
  if (!b) return;
  var d = document.getElementById(b.getAttribute("data-open-dialog"));
  if (!d || !d.showModal) return;
  if (!d.dataset.ready) {
    d.dataset.ready = "1";
    d.addEventListener("close", function () { var v = d.querySelector("video"); if (v) v.pause(); });
    d.addEventListener("click", function (ev) { if (ev.target === d || ev.target.closest("[data-close-dialog]")) d.close(); });
  }
  d.showModal();
  var v = d.querySelector("video");
  if (v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
});
