# N8 — The density→absence gap, characterized: it is the square-root cancellation barrier (= the capstone)

**Author: David Alejandro Trejo Pizzo · 2026-06-05.**
The audit's directive: after two distinct exact-zeros-facing theories (Littlewood, Motohashi) hit the *same*
wall, stop seeking techniques and **characterize the wall itself** — the precise logical ingredient missing to
pass from *density* ("few off-line zeros") to *absence* ("none"). This is that characterization. It is not a
technique and not a computation; it is a precise statement of the gap, and it unifies the gap with every
obstruction the program has named.

---

## 1. The exact zeros-facing tools all reduce to a cancellation estimate

Each unconditional tool that touches the zeros *exactly* expresses a zero-quantity as an oscillating sum/integral
whose size is the object of control:

- **Explicit formula:** $\sum_\rho h(\gamma_\rho)=\widehat{(\text{arch})}-\sum_n\Lambda(n)n^{-1/2}g(\log n)$ — the
  zero side equals a **prime sum** $\sum_n\Lambda(n)n^{-1/2}(\cdots)$, an oscillating cancellation.
- **Littlewood:** $\sum_{\beta>\sigma_0}(\beta-\sigma_0)=\frac1{2\pi}\int_0^T\log|\zeta(\sigma_0+it)|\,dt+O(\log T)$,
  and $\int\log|\zeta|$ is governed by the same prime-sum cancellation $\re\sum_p p^{-\sigma_0-it}$.
- **Motohashi:** the fourth moment $\int|\zeta(\half+it)|^4$ off-diagonal $=\sum_n d(n)d(n+h)$, whose error is a
  cancellation controlled spectrally; the bound feeds a zero-density estimate $N(\sigma,T)$.

In every case the controllable quantity is the **amount of cancellation** in an oscillating sum over primes
(equivalently, the fluctuation of $\log|\zeta|$ / the error term in the prime count).

## 2. What the tools deliver vs. what absence requires

| | cancellation achieved | zero-statement |
|---|---|---|
| unconditional (Littlewood, Motohashi, …) | **power-saving:** $\ll x^{1-\delta}$ (or $o(T)$, or $T^{c(1-\sigma)}$) | **density** ($N(\sigma,T)$ small) |
| Riemann Hypothesis | **square-root:** $\ll x^{1/2+\varepsilon}$ | **absence** ($N(\sigma,T)=0$, $\sigma>\half$) |

The aggregate $\sum_{\beta>\sigma_0}(\beta-\sigma_0)\ge0$ is a sum of **positive** terms; bounding it by a
power-saving amount $o(T)$ forces only a *small proportion* of large terms (density). To force the sum to be
**$O(1)$** — small enough that, term by term, no $\beta>\sigma_0$ survives — one needs the integral / prime sum
controlled to **square-root** size. **A single off-line zero contributes $O(1)$; the unconditional aggregate is
power-saving-but-growing; so one zero is below the resolution.** Closing the gap is precisely raising the
cancellation from power-saving to square-root.

## 3. The characterization (N8)

> **N8.** *The density→absence gap is the **square-root cancellation barrier**: every exact zeros-facing tool
> controls a prime-sum cancellation only to **power-saving** ($x^{1-\delta}$), which yields **density**; absence
> (RH) requires **square-root** cancellation ($x^{1/2+\varepsilon}$), which yields **absence**. The missing
> logical ingredient is therefore not a new statistic or technique but **square-root cancellation itself** — and
> square-root cancellation for these sums **is** the Riemann Hypothesis.* The gap is **RH-equivalent**, not a
> separable sub-ingredient.

This is why **two very different theories fail in exactly the same way:** Littlewood and Motohashi are both
limited by the **same universal barrier** — the square-root barrier of analytic number theory, the line between
"as cancellative as a generic pseudorandom sequence allows one to *prove*" ($x^{1-\delta}$) and "as cancellative
as a *random* sequence" ($x^{1/2}$). The wall is not in either theory; it is the barrier itself.

## 4. The unification (why this is the same wall, from a fourth side)

Square-root cancellation is an **upper** bound on a signed/oscillating sum (the *absence of bias*). This is
exactly the **wrong-sign capstone** seen from the cancellation angle:
- **Lower-bound / positivity tools** (Weil $\ge0$, the $3\!+\!4\cos\theta\!+\!\cos2\theta$ device, the moment
  diagonal) are unconditional and give existence / lower bounds / density.
- **Square-root cancellation** is the **upper** control — the absence of an anomalous accumulation — which is the
  one-sided upper constraint RH demands.

Thus the four obstructions the program named are one wall, seen from four sides:
$$
\underbrace{\text{wrong-sign capstone}}_{\text{lower-bound tools, wrong sign}}=
\underbrace{N7}_{\text{statistics describe, not force}}=
\underbrace{\text{meta-obstruction}}_{\text{no deterministic non-positivity absence}}=
\underbrace{N8}_{\text{power-saving}\not\to\text{square-root}} .
$$
The density→absence gap is the square-root barrier; the square-root barrier is the upper-cancellation; the
upper-cancellation is the capstone; the capstone is RH. They are facets of a single object: **the absence of an
unconditional square-root / upper-cancellation control of the relevant sums.**

## 5. What this settles, and what it does not

- **Settles (the deliverable the audit asked for):** the missing ingredient is *square-root cancellation*, and
  it is **RH-equivalent** — the density→absence gap is **not** a separable logical step that a clever combination
  of existing tools could supply; it is the central barrier itself. This is why Littlewood and Motohashi, though
  different, stop at the identical place, and why no further *statistic* will help.
- **Does not settle:** whether the square-root barrier can be crossed for $\zeta$. That is RH. The program has now
  shown — from positivity (8 paradigms), from dynamics (N5), from the probabilistic side (N7), from the
  cohomological side (P13), and now from the cancellation side (N8) — that **every accessible route reaches the
  same square-root / upper-cancellation barrier, and no available mechanism crosses it.**

## 6. Consequence for the program (RH-directed)

- The exact zeros-facing lines (explicit formula, Littlewood, Motohashi) are the **right** lines, but they are
  all stopped at the **same** barrier (square-root), which N8 identifies as RH-equivalent. So *refining* them
  will not cross; only an unconditional **square-root cancellation** input would, and that input is RH.
- The honest frontier is therefore unchanged in location but now **precisely named**: an unconditional
  square-root cancellation / upper-bound for $\sum_p p^{-\sigma-it}$ (equivalently the prime count error term,
  equivalently the Möbius/Λ sums), uniform — which is the Riemann Hypothesis, and for which no current mechanism
  (positivity, dynamics, statistics, cohomology, cancellation) provides an unconditional handle.

### Status
- N8 (density→absence $=$ power-saving$\,\not\to\,$square-root $=$ the square-root barrier, RH-equivalent) — ✅
  characterized.
- Unification: capstone $=$ N7 $=$ meta-obstruction $=$ N8 — ✅, one wall from four sides.
- The wall is the square-root / upper-cancellation barrier; crossing it is RH; no available mechanism does. The
  program's map of the wall is, with N8, complete from the cancellation side as well.
