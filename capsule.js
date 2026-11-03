/**
 * Capsule: five scholastic syllabus capsules set in a rounded plinth.
 * The capsule under the pointer lifts on its own spring and takes the bright stroke,
 * while its neighbours respond with subtle distance-based resonance.
 * At rest each capsule holds its distinct syllabus height.
 * The slider controls lift height.
 */
const {
  Cam, clamp, facing, fit, prism, proj, rings, unproj, spring, stepS,
  mk, place, pointer, put, register, disposer, solid,
} = HL;

const N = 5, CW = 18, CD = 26, GAP = 12, PITCH = CW + GAP;
const PLINTH_H = 6;
const REST_H = [24, 32, 26, 30, 22];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  const totalW = N * PITCH - GAP;
  const margin = 8;
  const maxLift = value;

  const C = Cam(45, 0.5, 1.6);
  fit(C, [
    [-margin, -margin, -PLINTH_H],
    [totalW + margin, CD + margin, -PLINTH_H],
    [totalW + margin, -margin, -PLINTH_H],
    [-margin, CD + margin, -PLINTH_H],
    [0, 0, 36 + maxLift],
    [totalW, CD, 36 + maxLift],
  ], 200, 166);

  const P = proj(C), front = facing(C);
  const g = mk("g", {}, svg);

  // Plinth base
  const [baseRing, baseInner] = rings(-margin, -margin, totalW + margin, CD + margin, 8, 2);
  put(solid(g), prism(P, front, baseRing, baseInner, -PLINTH_H, 0));

  // Five capsules arranged left to right
  const capsules = [];
  for (let i = 0; i < N; i++) {
    const x0 = i * PITCH;
    const y0 = 0;
    const x1 = x0 + CW;
    const y1 = y0 + CD;
    const h0 = REST_H[i];
    const [ring, inner] = rings(x0, y0, x1, y1, CW / 2, 1.2);
    const el = solid(g);
    const sp = spring(h0, { eps: 0.05 });

    // Status indicator dot riding top of capsule
    const dot = mk("circle", { r: 1.2, class: i === 1 ? "dot m" : "dot off" }, g);

    capsules.push({ i, x0, x1, y0, y1, h0, ring, inner, el, sp, dot, drawn: NaN });
  }

  let activeIdx = -1;
  let overPt = null;

  function drawCapsule(c) {
    const h = Math.max(2, c.sp.x);
    if (h === c.drawn) return;
    c.drawn = h;
    put(c.el, prism(P, front, c.ring, c.inner, 0, h));

    // Place dot at top centre
    const cx = (c.x0 + c.x1) / 2;
    const cy = (c.y0 + c.y1) / 2;
    place(c.dot, P(cx, cy, h));
  }

  const loop = register(stage, (dt) => {
    let moving = false;
    for (const c of capsules) {
      if (stepS(c.sp, dt)) moving = true;
      drawCapsule(c);
    }
    return moving;
  });
  bag.add(loop.unregister);

  function retarget() {
    for (let i = 0; i < N; i++) {
      const c = capsules[i];
      if (activeIdx < 0) {
        c.sp.t = c.h0;
        c.el.sil.classList.remove("hi");
        c.dot.setAttribute("class", i === 1 ? "dot m" : "dot off");
      } else {
        const dist = Math.abs(i - activeIdx);
        const lift = dist === 0 ? maxLift : Math.max(0, maxLift * 0.35 - dist * 3);
        c.sp.t = c.h0 + lift;
        c.el.sil.classList.toggle("hi", i === activeIdx);
        c.dot.setAttribute("class", i === activeIdx ? "dot" : "dot off");
      }
    }
    read.textContent = activeIdx >= 0 ? `capsule 0${activeIdx + 1}` : "rest";
    loop.wake();
  }

  function pick([sx, sy]) {
    const pt = unproj(C, sx, sy, 0);
    if (!pt) return -1;
    const [wx, wy] = pt;
    if (wy < -margin || wy > CD + margin) return -1;
    for (let i = 0; i < N; i++) {
      const c = capsules[i];
      if (wx >= c.x0 - GAP / 2 && wx <= c.x1 + GAP / 2) return i;
    }
    return -1;
  }

  bag.add(pointer(stage, {
    move: (p) => {
      const next = pick(p);
      if (next !== activeIdx) {
        activeIdx = next;
        retarget();
      }
    },
    leave: () => {
      if (activeIdx !== -1) {
        activeIdx = -1;
        retarget();
      }
    },
  }));

  bag.add(() => svg.replaceChildren());

  return {
    set: (v) => {
      retarget();
    },
    destroy: bag.dispose,
  };
}

hairline({
  name: "capsule",
  means: "Five study capsules in a dock lift and illuminate under the pointer.",
  rules: [1, 4, 5, 8, 9],
  range: [12, 22, 32],
  tour: [[140, 160], [200, 150], [260, 160], null],
  mount,
});
