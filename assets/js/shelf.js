(() => {
  const root = document.querySelector("[data-shelf-header]");
  if (!root) return;
  const entries = [...document.querySelectorAll("[data-shelf-entry]")];
  const caption = root.querySelector("[data-shelf-caption]");
  const defaultCaption = caption.textContent;
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  let previous = null;

  function reveal(entry) {
    if (!entry) return;
    entry.focus({ preventScroll: true });
    entry.scrollIntoView({
      behavior: motion.matches ? "instant" : "smooth",
      block: "center",
    });
    previous = entry;
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

  const button = root.querySelector("[data-shelf-random]");
  if (entries.length) button.hidden = false;
  button.addEventListener("click", () => {
    const choices = entries.filter(
      (entry) => entries.length === 1 || entry !== previous,
    );
    const entry = choices[Math.floor(Math.random() * choices.length)];
    root.querySelector("[data-shelf-announcement]").textContent =
      `Picked ${entry.dataset.title}`;
    reveal(entry);
  });
})();
