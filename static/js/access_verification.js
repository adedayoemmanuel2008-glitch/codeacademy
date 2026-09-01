/* =============================================
   ACCESS_VERIFICATION.JS
   SEA TECH / Code Academy
============================================= */

document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("access_code");
  const form = document.querySelector(".verification-form");
  const btn = document.querySelector(".verification-submit");

  /* ── Auto uppercase and trim as user types ── */
  if (input) {
    input.addEventListener("input", function () {
      const pos = this.selectionStart;
      this.value = this.value.replace(/\s/g, "");
      this.setSelectionRange(pos, pos);
    });
  }

  /* ── Loading state on submit ── */
  if (form && btn) {
    form.addEventListener("submit", function () {
      btn.textContent = "Verifying...";
      btn.disabled = true;
      btn.style.opacity = "0.8";
    });
  }
});
