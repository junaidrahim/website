// Post margins: the table of contents tracks the section being read, and footnotes are copied
// beside their references as sidenotes. Without this script the contents stay open inline and
// the footnotes stay at the end of the post.
(() => {
  const toc = document.querySelector(".post-toc");
  if (toc) {
    // Fixed in the margin it is always open; inline on narrow screens it starts collapsed.
    const wide = matchMedia("(min-width: 85rem)");
    const sync = () => {
      toc.open = wide.matches;
    };
    sync();
    wide.addEventListener("change", sync);

    const links = [...toc.querySelectorAll('a[href^="#"]')];
    const headings = links.map((link) => document.getElementById(decodeURIComponent(link.hash.slice(1))));
    let frame = 0;
    const highlight = () => {
      frame = 0;
      let current = -1;
      headings.forEach((heading, index) => {
        if (heading && heading.getBoundingClientRect().top < innerHeight / 3) current = index;
      });
      links.forEach((link, index) => link.classList.toggle("is-active", index === current));
    };
    addEventListener(
      "scroll",
      () => {
        if (!frame) frame = requestAnimationFrame(highlight);
      },
      { passive: true },
    );
    highlight();
  }

  const content = document.querySelector(".single-content");
  if (!content) return;
  const refs = [...content.querySelectorAll("a.footnote-ref")].filter((ref) => !ref.closest(".footnotes"));
  if (!refs.length) return;

  // Endnotes are hidden only when every reference has a sidenote, so no note goes missing.
  let complete = true;
  for (const ref of refs) {
    const note = document.getElementById(decodeURIComponent(ref.hash.slice(1)));
    const anchor = ref.closest("sup") ?? ref;
    if (!note || !anchor.closest("p, li") || anchor.closest("table, h1, h2, h3, h4, h5, h6")) {
      complete = false;
      continue;
    }
    const sidenote = document.createElement("span");
    sidenote.className = "sidenote";
    sidenote.setAttribute("role", "note");
    const number = document.createElement("sup");
    number.textContent = ref.textContent;
    sidenote.append(number, " ");
    [...note.children].forEach((block, index) => {
      const copy = block.cloneNode(true);
      copy.querySelectorAll(".footnote-backref").forEach((backref) => backref.remove());
      if (index) sidenote.append(document.createElement("br"));
      sidenote.append(...(copy.tagName === "P" ? copy.childNodes : [copy]));
    });
    anchor.after(sidenote);
  }
  if (complete) content.classList.add("has-sidenotes");
})();
