/* Members page: live search box and per-section counts.
   Material's instant navigation swaps page content without a reload, so this
   runs on every navigation through the document$ observable. */
document$.subscribe(function () {
  var input = document.getElementById("member-search");
  if (!input) return;

  var article = document.querySelector(".md-content__inner");
  var rows = article.querySelectorAll(".member-card, tbody tr");

  // Count entries under each level-2 heading (cards plus table rows).
  article.querySelectorAll("h2").forEach(function (h) {
    if (h.querySelector(".count")) return;
    var n = 0;
    for (var el = h.nextElementSibling; el && el.tagName !== "H2"; el = el.nextElementSibling) {
      n += el.querySelectorAll(".member-card, tbody tr").length;
    }
    if (n === 0) return;
    var s = document.createElement("span");
    s.className = "count";
    s.textContent = String(n).padStart(2, "0");
    h.appendChild(s);
  });

  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    rows.forEach(function (r) {
      r.hidden = q !== "" && r.textContent.toLowerCase().indexOf(q) === -1;
    });
  });
});
