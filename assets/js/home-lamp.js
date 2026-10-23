// Homepage desk lamp: the shade glances toward a mouse pointer and the button toggles the light.
(() => {
  const lamp = document.querySelector(".home-lamp");
  const svg = lamp?.querySelector("svg");
  if (!svg) return;

  const upper = svg.querySelector(".lamp-upper");
  const shade = svg.querySelector(".lamp-shade");

  // Joint positions and the shade's resting direction, in viewBox units and screen degrees.
  const ELBOW = [56, 40];
  const HEAD = [28, 22];
  const REST_AXIS = 90 + 20;
  const SHADE_LIMIT = 24;
  const ARM_LIMIT = 5;
  const EASE_MS = 160;

  lamp.addEventListener("click", () => {
    const on = lamp.getAttribute("aria-pressed") !== "true";
    lamp.setAttribute("aria-pressed", String(on));
  });

  const finePointer = matchMedia("(hover: hover) and (pointer: fine)");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

  let shadeAngle = 0;
  let armAngle = 0;
  let shadeTarget = 0;
  let armTarget = 0;
  let frame = 0;
  let lastTime = 0;

  const clamp = (value, limit) => Math.min(limit, Math.max(-limit, value));

  const render = () => {
    shade.setAttribute("transform", `rotate(${shadeAngle.toFixed(2)})`);
    upper.setAttribute("transform", `rotate(${armAngle.toFixed(2)} ${ELBOW[0]} ${ELBOW[1]})`);
  };

  // Ease toward the target and stop scheduling frames once settled.
  const step = (now) => {
    const k = 1 - Math.exp(-(lastTime ? now - lastTime : 16) / EASE_MS);
    lastTime = now;
    shadeAngle += (shadeTarget - shadeAngle) * k;
    armAngle += (armTarget - armAngle) * k;
    const settled =
      Math.abs(shadeTarget - shadeAngle) < 0.05 && Math.abs(armTarget - armAngle) < 0.05;
    if (settled) {
      shadeAngle = shadeTarget;
      armAngle = armTarget;
    }
    render();
    frame = settled ? 0 : requestAnimationFrame(step);
  };

  const aim = (shadeDeg, armDeg) => {
    shadeTarget = shadeDeg;
    armTarget = armDeg;
    if (!frame) {
      lastTime = 0;
      frame = requestAnimationFrame(step);
    }
  };

  const rest = () => aim(0, 0);

  const follow = (event) => {
    if (event.pointerType !== "mouse") return;
    const pivot = new DOMPoint(HEAD[0], HEAD[1]).matrixTransform(svg.getScreenCTM());
    const dx = event.clientX - pivot.x;
    const dy = event.clientY - pivot.y;
    const delta = ((((Math.atan2(dy, dx) * 180) / Math.PI - REST_AXIS) % 360) + 540) % 360 - 180;
    // Behind the lamp, fade back to rest instead of flipping between the limits.
    const facing = Math.min(1, (180 - Math.abs(delta)) / 60);
    // A distant pointer earns a glance; a nearby one a closer look.
    const attention = Math.min(1, Math.max(0.35, 1 - Math.hypot(dx, dy) / 900));
    const shadeDeg = clamp(delta * 0.5 * facing * attention, SHADE_LIMIT);
    aim(shadeDeg, clamp(shadeDeg * 0.2, ARM_LIMIT));
  };

  const leave = (event) => {
    if (!event.relatedTarget) rest();
  };

  const configure = () => {
    window.removeEventListener("pointermove", follow);
    window.removeEventListener("mouseout", leave);
    window.removeEventListener("blur", rest);
    if (finePointer.matches && !reducedMotion.matches) {
      window.addEventListener("pointermove", follow, { passive: true });
      window.addEventListener("mouseout", leave);
      window.addEventListener("blur", rest);
      return;
    }
    cancelAnimationFrame(frame);
    frame = 0;
    shadeAngle = shadeTarget = armAngle = armTarget = 0;
    render();
  };

  finePointer.addEventListener("change", configure);
  reducedMotion.addEventListener("change", configure);
  configure();
})();
