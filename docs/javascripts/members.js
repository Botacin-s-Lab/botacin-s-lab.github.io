/* Members page: adds an entry count next to each section heading.
   Material's instant navigation swaps page content without a reload, so this
   runs on every navigation through the document$ observable. */
document$.subscribe(function () {
  var article = document.querySelector(".md-content__inner");
  if (!article || !document.querySelector(".member-grid")) return;

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
});
