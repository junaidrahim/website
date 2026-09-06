// Original wave field inspired by the YC event's animated grid.
// Small local DOM animation: no libraries, network requests, or reading-data access.
(() => {
  const root = document.querySelector("[data-shelf-wave]");
  if (!root) return;
  const grid = root.querySelector(".shelf-wave-grid");
  const cells = [...grid.children];
  const motion = matchMedia("(prefers-reduced-motion: reduce)");
  let visible = true;
  let frame = 0;
  let last = 0;
  let elapsed = 0;
  let columns = 1;
  let pointer = null;

  function draw(time) {
    const count = Math.min(cells.length, columns * 9);
    for (let index = 0; index < count; index++) {
      const x = index % columns;
      const y = Math.floor(index / columns);
      const depth = 1 + y / 8;
      const wave = Math.sin((x * 0.19) / depth + y * 0.65 - time * 0.7);
      const swell = Math.cos(x * 0.09 - y * 0.8 + time * 0.43);
      let intensity = 0.12 + 0.62 * Math.pow((wave + swell + 2) / 4, 1.6);
      if (pointer) {
        const distance = Math.hypot(
          (x + 0.5) / columns - pointer.x,
          (y + 0.5) / 9 - pointer.y,
        );
        intensity = Math.min(
          0.95,
          intensity + 0.5 * Math.exp(-distance * distance * 65),
        );
      }
      cells[index].style.opacity = intensity.toFixed(3);
    }
  }

  function tick(now) {
    if (last) elapsed += Math.min(now - last, 100) / 1000;
    last = now;
    draw(elapsed);
    frame = requestAnimationFrame(tick);
  }

  function sync() {
    cancelAnimationFrame(frame);
    frame = 0;
    last = 0;
    if (!motion.matches && visible && !document.hidden)
      frame = requestAnimationFrame(tick);
    else draw(elapsed);
  }

  new ResizeObserver(() => {
    columns = getComputedStyle(grid).gridTemplateColumns.split(" ").length;
    draw(elapsed);
  }).observe(grid);
  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    sync();
  }).observe(root);
  document.addEventListener("visibilitychange", sync);
  motion.addEventListener("change", () => {
    pointer = null;
    sync();
  });
  grid.addEventListener("pointermove", (event) => {
    if (motion.matches) return;
    const bounds = grid.getBoundingClientRect();
    pointer = {
      x: (event.clientX - bounds.left) / bounds.width,
      y: (event.clientY - bounds.top) / bounds.height,
    };
  });
  grid.addEventListener("pointerleave", () => {
    pointer = null;
  });
  grid.addEventListener("pointercancel", () => {
    pointer = null;
  });
  sync();
})();
