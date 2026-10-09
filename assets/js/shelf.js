(() => {
  const root = document.querySelector("[data-shelf-header]");
  if (!root) return;
  const entries = [...document.querySelectorAll("[data-shelf-entry]")];
  const caption = root.querySelector("[data-shelf-caption]");
  const defaultCaption = caption.textContent;
  const motion = matchMedia("(prefers-reduced-motion: reduce)");

  function reveal(entry) {
    if (!entry) return;
    entry.focus({ preventScroll: true });
    entry.scrollIntoView({
      behavior: motion.matches ? "instant" : "smooth",
      block: "center",
    });
  }

  // Shuffle the whole inventory without replacement for a fresh shelf each visit.
  const shuffled = [...entries];
  for (let index = shuffled.length - 1; index > 0; index--) {
    const swap = Math.floor(Math.random() * (index + 1));
    [shuffled[index], shuffled[swap]] = [shuffled[swap], shuffled[index]];
  }

  root.querySelectorAll(".shelf-spine").forEach((spine, index) => {
    const entry = shuffled[index];
    if (entry) {
      spine.href = `#${entry.id}`;
      spine.dataset.title = entry.dataset.title;
      spine.setAttribute("aria-label", `Find ${entry.dataset.title} on the shelf`);
      spine.querySelector("span").textContent = entry.dataset.title;
    }
    const show = () => {
      caption.textContent = spine.dataset.title;
    };
    const reset = () => {
      caption.textContent = defaultCaption;
    };
    spine.addEventListener("pointerenter", show);
    spine.addEventListener("focus", show);
    spine.addEventListener("pointerleave", reset);
    spine.addEventListener("blur", reset);
    spine.addEventListener("click", (event) => {
      event.preventDefault();
      reveal(document.getElementById(spine.hash.slice(1)));
    });
  });
})();
