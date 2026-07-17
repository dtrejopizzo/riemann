# Phase 14 — Strategic analysis: where (and where not) the ω-structure touches the zeros

**Author: David Alejandro Trejo Pizzo · 2026-06-05.**
The advisor's directive is the right one and supersedes the others: *do not refine FHK; find the first point
where the ω-structure interacts **exactly** with a sum over zeros / the explicit formula — something that is not
merely a statistic of values.* This document answers that question precisely. The answer has a sharp negative
half (the explicit formula is ω-blind) and a sharp positive half (the exact bridge is the **spectral theory of
moments**, Motohashi), and it redirects the RH attack accordingly.

---

## 1. The negative half: the explicit formula is ω-blind (a structural obstruction)

The Riemann–von Mangoldt explicit formula — the canonical *exact sum over zeros* — has as its arithmetic
variable the von Mangoldt function $\Lambda(n)$, supported on **prime powers** $n=p^a$. And there
$$
\omega(p^a)=1\qquad\text{for every prime power.}
$$
Therefore, for any weight $z$,
$$
\boxed{\ \Lambda(n)\,z^{\omega(n)}=z\,\Lambda(n)\quad\text{on the entire support of }\Lambda\ }
$$
so the ω-weight enters the explicit formula only as a **trivial overall factor $z$**. *The explicit formula
cannot see the ω-structure.* Equivalently: the interesting ω-content — the **large deviations of $\omega(n)$**,
the integers with *many* prime factors — lives on integers that are **orthogonal to the prime-power support** of
the explicit formula. The two structures sit on disjoint parts of $\NN$.

> **Consequence.** No amount of refining the ω-large-deviation / FHK picture will, by itself, produce a sum over
> zeros: the ω-structure is invisible to the explicit formula. This is a precise version of the advisor's worry
> that the ω-results are *statistics of values*, not a *zeros mechanism* — and it explains, structurally, why
> Phase-13 (maxima, moments, freezing) does not move RH.

## 2. Where they DO couple: the multiplicative convolution = the moments

Prime powers (where $\omega=1$) build the many-factor integers (where $\omega$ is large) only through the
**multiplicative (Dirichlet) convolution**: $d_k=\underbrace{1*\cdots*1}_{k}$, and $d_k(n)=k^{\omega(n)}$ on
squarefree $n$ (P14). The convolution is the moments:
$$
\frac1T\int_T^{2T}|\zeta(\half+it)|^{2k}\,dt\ \sim\ a_k\,g_k\,(\log T)^{k^2},\qquad a_k=\text{(ω-arithmetic)},\ \ g_k=\text{(zero/RMT)}.
$$
At **leading order the moment factorizes**: $a_k$ (the per-prime ω-weight, P14) and $g_k$ (the
zero-correlation / random-matrix factor) are a **product** — *decoupled*. So the leading moment does **not**
couple ω to the zeros either; the ω-classes give $a_k$, the zeros give $g_k$, separately.

> The coupling of ω and the zeros is therefore neither in the explicit formula (ω-blind) nor in the leading
> moment (factorized) — it is in the **off-diagonal** of the moment, the part beyond $a_kg_k(\log T)^{k^2}$.

## 3. The positive half: the exact bridge is the spectral theory of moments (Motohashi)

The off-diagonal of the $2k$-th moment is the **shifted-convolution / additive-divisor problem**
$\sum_n d_k(n)\,d_k(n+h)$, and *this* is where the ω/divisor structure meets the zeros — **exactly**, and as a
theorem for $k=2$:

> **Motohashi's formula (the first exact ω↔zeros bridge).** The fourth moment
> $\int_0^\infty|\zeta(\half+it)|^4\,g(t)\,dt$ has an **exact** expansion in terms of the **spectrum of the
> hyperbolic Laplacian** (the Maass-form eigenvalues $\{\tfrac14+\kappa_j^2\}$ and the holomorphic forms),
> together with the contribution of the zeta zeros / the continuous spectrum. Here $k=2$, $d_2=d=2^{\omega}$ on
> squarefree — the ω-structure — appears on one side, and the **zeros/automorphic spectrum** on the other,
> linked by an identity, not a statistic.

So the answer to *"where does the ω-structure touch the zeros exactly?"* is: **in the spectral theory of
moments**, through the off-diagonal, with Motohashi's formula the first proven instance. The general $k$
version is the **spectral theory of moments of $\zeta$** (conjecturally a $GL(k)$ automorphic spectral
identity), with the zeros appearing on the spectral side and the ω-large-deviations ($a_k$) on the arithmetic
side. This is exactly *"a sum over zeros / an exact identity that is not merely a statistic of values."*

## 4. The RH-directed redirection (the single question, sharpened)

The advisor's question — *can ω-large-deviation information produce new information about the zeros?* — now has
a precise form:

> **The bridge ω $\Rightarrow$ zeros runs through the off-diagonal / the spectral theory of moments, not the
> explicit formula.** The first exact point is Motohashi ($k=2$). The RH-directed program is therefore: study
> the **off-diagonal correlations of $d_k$** (the additive-divisor / shifted-convolution problem) and their
> **spectral (Motohashi / $GL(k)$) expansion**, where the zeros appear exactly, and ask whether the ω-large-
> deviation structure ($a_k$ via the many-factor integers) constrains the spectral/zero side.

This is genuinely RH-directed (it is *about* the zeros, via an exact identity), and it is the first place in the
whole program where the new ω-structure meets the zeros non-trivially and exactly. Honest caveats:
- It brings in the **automorphic spectrum** (Maass forms, the Kuznetsov/Motohashi machinery) — a whole new
  apparatus, deep and technical.
- The $k\ge3$ spectral theory of moments is **open** (the $GL(k)$ Motohashi analogue is conjectural) — this is
  the same wall as the moment problem, now in its spectral form.
- Whether the identity yields **new** constraints on the zeros (rather than re-expressing the moments) is the
  open question — but it is at least the right *kind* of object (an exact zeros/spectrum identity), which the
  ω-statistics alone are not.

## 5. Recommendation

- **Drop** the FHK-refinement and the positivity frontiers (blocked, as the advisor judges).
- **Adopt** the single RH-directed target: the **off-diagonal of the $d_k$ moments and its spectral expansion**
  (Motohashi for $k=2$; the $GL(k)$ frontier for general $k$) — the first exact bridge from the ω-structure to
  the zeros.
- **Be exacting** (per the advisor): at each step demand an exact identity, a sum over the spectrum/zeros, or an
  explicit formula — and reject anything that is only a statistic of values. The ω-blindness of §1 is the filter:
  if a proposed step factors through $\Lambda$ / prime powers, the ω-structure is trivial there and it is the
  wrong step.

### Next concrete milestone (M14.1)
Write out the additive-divisor correlation $\sum_{n\le x}d(n)d(n+h)$ and locate, explicitly, where the zeta
zeros enter its error term via Motohashi's spectral expansion — the first computation in which the ω/divisor
structure and the zeros appear in one exact identity. Then ask: does the ω-large-deviation weight ($z^{\omega}$,
$z>1$) on the divisor side correspond to a definite, controllable feature on the spectral/zero side?
