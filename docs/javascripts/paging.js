/* Paged lists: any element with class "paged" shows its rows a page at a
   time (data-size rows per page) with prev/next and numbered buttons.
   Without JavaScript every row stays visible. Runs via document$ so it also
   works with Material's instant navigation. */
document$.subscribe(function () {
  document.querySelectorAll(".paged").forEach(function (box) {
    if (box.querySelector(".pager")) return;
    var rows = Array.prototype.slice.call(box.querySelectorAll(":scope > .pub-row, :scope > .news-row"));
    var size = parseInt(box.getAttribute("data-size"), 10) || 5;
    var pages = Math.ceil(rows.length / size);
    if (pages < 2) return;

    var nav = document.createElement("nav");
    nav.className = "pager";
    nav.setAttribute("aria-label", "Pages");
    box.appendChild(nav);
    var page = 0;

    function show(p, scroll) {
      page = Math.max(0, Math.min(pages - 1, p));
      rows.forEach(function (r, i) {
        r.hidden = Math.floor(i / size) !== page;
      });
      nav.innerHTML = "";
      function button(label, target, opts) {
        var b = document.createElement("button");
        b.type = "button";
        b.textContent = label;
        if (opts && opts.disabled) b.disabled = true;
        if (opts && opts.current) { b.className = "current"; b.setAttribute("aria-current", "page"); }
        b.addEventListener("click", function () { show(target, true); });
        nav.appendChild(b);
      }
      button("Prev", page - 1, { disabled: page === 0 });
      for (var i = 0; i < pages; i++) button(String(i + 1), i, { current: i === page });
      button("Next", page + 1, { disabled: page === pages - 1 });
      var info = document.createElement("span");
      info.className = "pager-info";
      info.textContent = (page * size + 1) + "–" + Math.min(rows.length, (page + 1) * size) + " of " + rows.length;
      nav.appendChild(info);
      if (scroll) box.scrollIntoView({ block: "start", behavior: "smooth" });
    }

    // Deep links such as publications/#2019 must land on the right page.
    var start = 0;
    if (location.hash.length > 1) {
      var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      var idx = rows.indexOf(target);
      if (idx >= 0) start = Math.floor(idx / size);
    }
    show(start, false);
    if (start > 0 && rows.indexOf(document.getElementById(location.hash.slice(1))) >= 0) {
      document.getElementById(location.hash.slice(1)).scrollIntoView();
    }
  });
});
