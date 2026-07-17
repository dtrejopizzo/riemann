# Phase 11 — A genuinely new path: hyperbolicity / Jensen polynomials / stable-polynomial machinery

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
After seven languages of the wall — all reducing to (U), with the wrong-sign capstone holding even in the
capstone-escaping cohomological route — we open a path that is new to this program, recent in the field, built
on powerful modern machinery, and a **different kind of argument** (real-rootedness via interlacing, not
quadratic-form positivity) that plausibly escapes the capstone by a route distinct from Phase 10. Grounded by a
working computation (M11.1).

---

## 1. The reframing (real-rootedness, not positivity)

$$
\mathrm{RH}\iff \Xi(t)=\xi(\tfrac12+it)\in\text{Laguerre–Pólya class (all real zeros)}\iff
\text{every Jensen polynomial } J^{d,n}\text{ of }\Xi\text{ is HYPERBOLIC (real-rooted)},
$$
where, for the (even) Taylor coefficients $a(k)=\Xi^{(2k)}(0)/(2k)!$,
$$
J^{d,n}(X)=\sum_{j=0}^{d}\binom{d}{j}\,a(n+j)\,X^{j}.
$$
This is the **Pólya–Jensen criterion**. Crucially, *hyperbolicity* (a polynomial having only real roots) is
**not** a quadratic-form positivity — it is proved, in modern combinatorics, by **interlacing** and **stability
preservers**, mechanisms that are *not* of the "$\ge0$" form the wrong-sign capstone obstructs.

## 2. Why this might escape the wrong-sign capstone

The capstone: every unconditional handle is a positivity ($\ge0$, lower-bound oriented); RH is an upper
constraint. Hyperbolicity is different:
- **Marcus–Spielman–Srivastava (2013–15)** proved real-rootedness of families (solving Kadison–Singer, building
  Ramanujan graphs) by the **method of interlacing families** — bounding the *largest root* of an *expected
  characteristic polynomial* — with **no positivity certificate**. This is a genuinely non-positivity route to
  an *upper* control (the root location).
- **Borcea–Brändén** classified *all* linear operators preserving stability/real-rootedness. This gives a
  *toolbox of arithmetic-capable operations* that preserve hyperbolicity — a way for arithmetic to enter
  *without* an explicit-formula positivity (the obstruction N6 met).
- **Branden–Krasikov–Csordas** and the Turán/higher-order inequalities: hyperbolicity of $J^{d,n}$ for growing
  $d$ encodes *all orders* of the criterion at once, not just the quadratic (Li/Turán) order where positivity
  lives.

So the bet: real-rootedness via interlacing/stability is a mechanism for an **upper** root-location bound that
is **not** a zero-level positivity — the one structural feature the capstone says is required.

## 3. The recent partial result (why now)

**Griffin–Ono–Rolen–Zagier (PNAS 2019)** proved: for each fixed degree $d$, $J^{d,n}$ is hyperbolic for all
sufficiently large $n$, and its (rescaled) roots converge to those of the **Hermite polynomial** $H_d$ — the
GUE connection. This is genuine partial progress toward RH by this route, with the **uniformity in $d$** the
open frontier. It is recent, active, and uses exactly the hyperbolicity machinery.

## 4. Grounding (M11.1 — done, it works)

`experiments/M11_1_jensen_hyperbolicity.py` computed the Riemann $\Xi$ Taylor coefficients and tested the
criterion:
- $a(0)=0.4971=\xi(\tfrac12)$; signs **alternate** $+,-,+,-,\dots$ (the Laguerre–Pólya signature). ✓
- **Turán inequalities** $a(k)^2-a(k-1)a(k+1)>0$ hold for all tested $k$ (a *necessary* L–P condition). ✓
- **All Jensen polynomials** $J^{d,n}$ for $d=2,3,4,5$, $n=0,2,5$ are **hyperbolic** ($\max|\mathrm{Im\,root}|=0$).
  Consistent with RH. ✓

The object is concrete, computable with our tools, and behaves as RH predicts.

## 5. The honest open part, and the new mathematics

RH $=$ hyperbolicity of $J^{d,n}$ for **all** $d,n$. GORZ gives "each $d$, large $n$." The gap:
- **Uniformity in $d$** (the genuine open core, like every uniformity we met) — but here attackable by
  *interlacing families* (bound the largest non-real excursion uniformly) and *stability preservers* (build
  $J^{d,n}$ from hyperbolic building blocks by stability-preserving, arithmetic-carrying operations).
- **Honest caveat:** the *low*-degree hyperbolicity ($d=2$ = Turán = Li-coefficient positivity) IS a
  positivity, so it inherits the capstone there. The **bet is the high-degree régime**, where MSS-type
  interlacing replaces positivity. Whether the interlacing argument can be made arithmetic (carry the primes)
  and uniform is the new mathematics to develop — and it is genuinely different from everything in Phases 0–10.

## 6. Milestones

- **M11.2 — the interlacing structure.** Test whether $\{J^{d,n}\}_n$ form an **interlacing family** (roots of
  consecutive $n$ interlace), the precondition for the MSS method. If yes, the largest-root machinery applies.
- **M11.3 — stability-preserver realization.** Express the shift $n\to n+1$ and the degree raise $d\to d+1$ as
  Borcea–Brändén stability-preserving operators acting on the $\Xi$-coefficient sequence; identify where the
  **arithmetic** (the $\zeta$ data) enters the preserver — the escape from N6's arithmetic-blindness.
- **M11.4 — uniformity probe.** Quantify the *margin* of hyperbolicity (least root gap / discriminant) of
  $J^{d,n}$ as $d$ grows at fixed scaled height; does it stay bounded below (uniform, RH-viable) or shrink
  (the familiar marginality)? Compare to the GORZ Hermite limit. (Mirrors the M10 deep-run discipline.)
- **M11.5 — capstone test.** Determine, honestly, whether the high-degree interlacing argument reduces to a
  positivity (capstone again) or is genuinely positivity-free. This is the decisive question.

## 7. Honest assessment

- **Genuinely new to us, recent, powerful machinery, different mechanism** (real-rootedness, not positivity) —
  the strongest "new path" candidate after the capstone analysis, precisely because hyperbolicity is the one
  classical route to an *upper* (root-location) bound that is not a quadratic-form positivity.
- **Real partial result exists** (GORZ), and the modern toolbox (MSS interlacing, Borcea–Brändén) is exactly
  the kind that proves real-rootedness without positivity.
- **Honest risk:** it may reduce to the capstone in disguise (the low-degree positivity; the GORZ Hermite/GUE
  limit echoes pair correlation). M11.5 is the make-or-break: is the high-degree interlacing positivity-free?
- **Odds:** small (it is RH), but this is the first path in the program whose *mechanism* is structurally
  outside the positivity paradigm the capstone obstructs — which is exactly what the capstone said we need.

### Status / next
- Reframing + rationale + modern machinery + grounding (M11.1) — ✅.
- **Next: M11.2** (interlacing family structure) — the precondition for the MSS largest-root machinery, and the
  first test of whether the positivity-free route is open for $\Xi$.
