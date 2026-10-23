// Homepage desk lamp: the shade glances toward a mouse pointer and the button toggles the light.
(() => {
  const lamp = document.querySelector(".home-lamp");
  const svg = lamp?.querySelector("svg");
  if (!svg) return;

  const upper = svg.querySelector(".lamp-upper");
  const shade = svg.querySelector(".lamp-shade");

  // The drawing declares its joints (viewBox units) and the shade's resting tilt (degrees).
  const point = (value) => value.split(" ").map(Number);
  const ELBOW = point(svg.dataset.elbow);
  const HEAD = point(svg.dataset.head);
  const REST_AXIS = 90 + Number(svg.dataset.rest);
  const SHADE_LIMIT = 24;
  const ARM_LIMIT = 5;
  // The lamp notices the pointer a beat late and ignores small shifts.
  const DELAY_MS = 120;
  const DEADBAND = 1.5;
  // Damped springs: the shade settles first and the upper arm follows the shade.
  const SHADE_SPRING = { omega: 9, zeta: 0.82 };
  const ARM_SPRING = { omega: 5.5, zeta: 0.95 };

  lamp.addEventListener("click", () => {
    const on = lamp.getAttribute("aria-pressed") !== "true";
    lamp.setAttribute("aria-pressed", String(on));
  });

  const finePointer = matchMedia("(hover: hover) and (pointer: fine)");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

  const shadeJoint = { angle: 0, velocity: 0, target: 0 };
  const armJoint = { angle: 0, velocity: 0, target: 0 };
  let samples = [];
  let frame = 0;
  let lastTime = 0;

  const clamp = (value, limit) => Math.min(limit, Math.max(-limit, value));

  const render = () => {
    shade.setAttribute("transform", `rotate(${shadeJoint.angle.toFixed(2)})`);
    upper.setAttribute(
      "transform",
      `rotate(${armJoint.angle.toFixed(2)} ${ELBOW[0]} ${ELBOW[1]})`,
    );
  };

  const spring = (joint, { omega, zeta }, dt) => {
    const acceleration =
      omega * omega * (joint.target - joint.angle) - 2 * zeta * omega * joint.velocity;
    joint.velocity += acceleration * dt;
    joint.angle += joint.velocity * dt;
  };

  const settled = (joint) =>
    Math.abs(joint.target - joint.angle) < 0.02 && Math.abs(joint.velocity) < 0.02;

  const step = (now) => {
    // Release pointer samples only after the reaction delay has passed.
    while (samples.length && samples[0].time <= now - DELAY_MS) {
      const { angle } = samples.shift();
      if (angle === 0 || Math.abs(angle - shadeJoint.target) > DEADBAND) shadeJoint.target = angle;
    }
    const dt = Math.min(lastTime ? now - lastTime : 16, 32) / 1000;
    lastTime = now;
    spring(shadeJoint, SHADE_SPRING, dt);
    armJoint.target = clamp(shadeJoint.angle * 0.2, ARM_LIMIT);
    spring(armJoint, ARM_SPRING, dt);

    if (!samples.length && settled(shadeJoint) && settled(armJoint)) {
      shadeJoint.angle = shadeJoint.target;
      armJoint.angle = armJoint.target;
      shadeJoint.velocity = armJoint.velocity = 0;
      render();
      frame = 0;
      return;
    }
    render();
    frame = requestAnimationFrame(step);
  };

  const aim = (angle) => {
    samples.push({ time: performance.now(), angle });
    if (!frame) {
      lastTime = 0;
      frame = requestAnimationFrame(step);
    }
  };

  const rest = () => aim(0);

  const follow = (event) => {
    if (event.pointerType !== "mouse") return;
    const pivot = new DOMPoint(HEAD[0], HEAD[1]).matrixTransform(svg.getScreenCTM());
    const dx = event.clientX - pivot.x;
    const dy = event.clientY - pivot.y;
    const distance = Math.hypot(dx, dy);
    // Right at the hinge the direction is meaningless; hold the current pose.
    if (distance < 24) return;
    const delta = ((((Math.atan2(dy, dx) * 180) / Math.PI - REST_AXIS) % 360) + 540) % 360 - 180;
    // Behind the lamp, fade back to rest instead of flipping between the limits.
    const facing = Math.min(1, (180 - Math.abs(delta)) / 60);
    // A distant pointer earns a glance; a nearby one a closer look.
    const attention = Math.min(1, Math.max(0.35, 1 - distance / 900));
    aim(clamp(delta * 0.5 * facing * attention, SHADE_LIMIT));
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
    samples = [];
    for (const joint of [shadeJoint, armJoint]) joint.angle = joint.velocity = joint.target = 0;
    render();
  };

  finePointer.addEventListener("change", configure);
  reducedMotion.addEventListener("change", configure);
  configure();
})();
