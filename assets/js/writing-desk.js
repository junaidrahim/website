// The homepage lamp uses the site's existing light/dark color-scheme classes.
(() => {
  const lamp = document.querySelector(".desk-switch");
  if (!lamp) return;
  const isDark = () => getComputedStyle(document.body).colorScheme === "dark";
  lamp.setAttribute("aria-pressed", String(isDark()));
  const toggle = () => {
    const dark = !isDark();
    document.body.classList.toggle("dark", dark);
    document.body.classList.toggle("light", !dark);
    lamp.setAttribute("aria-pressed", String(dark));
  };
  lamp.addEventListener("click", toggle);
  lamp.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      if (!event.repeat) toggle();
    }
  });
})();
