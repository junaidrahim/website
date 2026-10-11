(() => {
  const root = document.querySelector("[data-bookcase]");
  if (!root) return;
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  const groups = [...root.querySelectorAll("[data-bookcase-rows]")].map(
    (container) => ({
      container,
      books: [...container.querySelectorAll("[data-book-id]")],
    }),
  );
  const allBooks = groups.flatMap((group) => group.books);
  const dialog = root.querySelector("dialog");
  let selected = null;
  let animation = null;
  let closing = false;
  let lastWidth = 0;
  // Pack real rows so each has its own shelf board, at every viewport width.
  function layout() {
    const active = document.activeElement;
    groups.forEach(({ container, books }) => {
      container.closest("section").hidden = false;
      const available = container.clientWidth - 24;
      const fragment = document.createDocumentFragment();
      let row,
        used = 0;
      books.forEach((book) => {
        const width = parseFloat(book.style.getPropertyValue("--book-width"));
        if (!row || used + width + 4 > available) {
          row = document.createElement("div");
          row.className = "bookcase-row";
          fragment.append(row);
          used = 0;
        }
        row.append(book);
        used += width + 4;
      });
      container.replaceChildren(fragment);
      container.closest("section").hidden = !container.childElementCount;
    });
    if (active?.matches("[data-book-id]") && active.isConnected)
      active.focus({ preventScroll: true });
  }

  function flightTransform(book) {
    const from = book.getBoundingClientRect();
    const to = dialog.getBoundingClientRect();
    return `translate(${from.x + from.width / 2 - to.x - to.width / 2}px, ${from.y + from.height / 2 - to.y - to.height / 2}px) scale(${from.width / to.width}, ${from.height / to.height}) rotateY(-35deg)`;
  }

  function openBook(book) {
    if (dialog.open) return;
    selected = book;
    for (const property of ["--cover-color", "--cover-ink", "--cover-accent"]) {
      const value = book.style.getPropertyValue(property);
      if (value) dialog.style.setProperty(property, value);
      else dialog.style.removeProperty(property);
    }
    const entry = document.getElementById(book.dataset.bookId);
    dialog.querySelector("h2").textContent = book.dataset.title;
    dialog.querySelector(".pulled-book-authors").textContent =
      book.dataset.authors;
    const drawing = book.querySelector(".bookcase-spine-art svg");
    const art = dialog.querySelector(".pulled-book-art");
    art.replaceChildren();
    art.hidden = !drawing;
    if (drawing) art.append(drawing.cloneNode(true));
    const status = dialog.querySelector(".pulled-book-status");
    status.replaceChildren();
    const stamp = entry.querySelector(".shelf-status");
    if (stamp) status.append(stamp.cloneNode(true));
    const note = entry.querySelector(".shelf-note p");
    const noteView = dialog.querySelector(".pulled-book-note");
    noteView.textContent = note?.textContent || "";
    noteView.hidden = !note;
    const link = entry.querySelector(":scope > a");
    const about = dialog.querySelector(".pulled-book-link");
    about.hidden = !link;
    if (link) about.href = link.href;
    else about.removeAttribute("href");
    dialog.showModal();
    document.body.classList.add("bookcase-open");
    book.classList.add("is-pulled");
    if (!motion.matches)
      animation = dialog.animate(
        [
          { transform: flightTransform(book), opacity: 0.4 },
          { transform: "translate(0, 0) scale(1) rotateY(0)", opacity: 1 },
        ],
        { duration: 420, easing: "cubic-bezier(.2,.7,.2,1)" },
      );
  }

  async function closeBook() {
    if (closing || !dialog.open) return;
    closing = true;
    animation?.cancel();
    if (!motion.matches && selected?.isConnected) {
      animation = dialog.animate(
        [
          { transform: "translate(0, 0) scale(1)", opacity: 1 },
          { transform: flightTransform(selected), opacity: 0 },
        ],
        { duration: 240, easing: "ease-in", fill: "forwards" },
      );
      try {
        await animation.finished;
      } catch {
        /* Reduced motion can cancel the return. */
      }
    }
    dialog.close();
    animation?.cancel();
    document.body.classList.remove("bookcase-open");
    selected?.classList.remove("is-pulled");
    selected?.focus({ preventScroll: true });
    closing = false;
  }

  allBooks.forEach((book) =>
    book.addEventListener("click", (event) => {
      event.preventDefault();
      openBook(book);
    }),
  );
  dialog.querySelector("button").addEventListener("click", closeBook);
  dialog.addEventListener("keydown", (event) => {
    if (event.key !== "Tab") return;
    const controls = [...dialog.querySelectorAll("a[href]")].filter(
      (control) => !control.hidden,
    );
    const title = dialog.querySelector("h2");
    if (!controls.length) {
      event.preventDefault();
      title.focus();
      return;
    }
    const first = controls[0];
    const last = controls[controls.length - 1];
    if (document.activeElement === title) {
      event.preventDefault();
      (event.shiftKey ? last : first).focus();
    } else if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });
  dialog.addEventListener("cancel", (event) => {
    event.preventDefault();
    closeBook();
  });
  dialog.addEventListener("click", (event) => {
    const bounds = dialog.getBoundingClientRect();
    if (
      event.target === dialog &&
      (event.clientX < bounds.left ||
        event.clientX > bounds.right ||
        event.clientY < bounds.top ||
        event.clientY > bounds.bottom)
    )
      closeBook();
  });
  motion.addEventListener("change", () => {
    if (motion.matches) animation?.cancel();
  });
  new ResizeObserver(([entry]) => {
    const width = Math.round(entry.contentRect.width);
    if (width !== lastWidth) {
      lastWidth = width;
      layout();
    }
  }).observe(root);
  layout();

  // Deep links and the no-JavaScript spine links also work in the text catalogue.
  function revealHash() {
    const id = location.hash.slice(1);
    const target = document.getElementById(id);
    if (target?.matches("[data-shelf-entry]")) {
      target.closest("details.shelf-catalogue").open = true;
      target.scrollIntoView({ behavior: "instant", block: "center" });
    }
  }
  addEventListener("hashchange", revealHash);
  revealHash();
})();
