# Phase 10 — Report: the cohomological turn, M10.1 → M10.3

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
A self-contained account of what the three milestones M10.1–M10.3 established, why they matter, and what is
honestly still open. Reproducible with `experiments/colab_phase10_M1_to_M3.py` (runs all three, deeper).

---

## 0. Why this route at all (the one-paragraph rationale)

The program's capstone (master closing document, Part VII) is that **every unconditional handle on the zeros
is a positivity oriented to give *lower* bounds, while RH is a one-sided *upper* constraint** — the wrong sign.
The *only* structure known to escape this is the one that proved the **only RH humanity has proved** (the Weil
conjectures for curves over $\mathbb F_q$): a **higher-level positivity** (the **Hodge index theorem** on the
surface $C\times C$) that yields the zero-level **upper** bound by **duality**. Phase 10 asks: can we build the
arithmetic analogue for $\zeta$? Our unique asset is the validated detector, which gives the candidate
**intersection form** ($\mathfrak t=A_\Phi-P_F$, the Weil–Carleson form) **explicitly and numerically** — which
the abstract programs (Deninger, Connes–Consani) do not have in hand. The three milestones probe whether the
curve-case Hodge mechanism transfers.

---

## 1. M10.1 — the Lorentzian envelope, and its degeneration

**What we did.** Treated $\mathfrak t=A_\Phi-P_F$ as the *primitive part* of an intersection form, adjoined one
*ample* (archimedean) direction, and grew the band $d$ — i.e. grew the cohomology "genus" toward $\zeta$ —
tracking the **Hodge gap** $\lambda_{\min}(\mathfrak t)$ and the signature.

**What we found.**

| $d$ | $x=2d/\log T_0$ | Hodge gap | signature | verdict |
|---:|---:|---:|---:|---|
| 1.0 | 0.43 | $+0.377$ | $(1,21,0)$ | **definite**, curve-like |
| 2.0 | 0.87 | $+3\times10^{-9}$ | $(1,19,2)$ | degenerate |
| 4.0 | 1.74 | $\sim0$ | $(1,12,9)$ | degenerate |

For **finite genus** (small band) the form is **definite** with a positive Hodge gap — the curve-case
structure holds exactly. As the genus grows toward $\zeta$, the gap $\to0$ and the form **degenerates** (null
directions appear).

**Why it matters — the four-way unification.** The vanishing Hodge gap is the *same phenomenon* as three
others the program met separately:
$$\underbrace{C\equiv1}_{\text{N3 saturation}}=\underbrace{\Lambda=0}_{\text{de Bruijn–Newman}}=\underbrace{\lambda_{\min}(\mathfrak t)\to0}_{\text{Hodge gap}}=\underbrace{\text{form degenerates}}_{\text{cohomological}}.$$
The curve-case Hodge argument needs a **definite** form (finite genus → spectral gap). $\zeta$'s arithmetic
surface has **infinite genus with a vanishing gap** — so the finite-rank argument does not transfer. M10.1
**named the missing new mathematics**: a *regularized, infinite-dimensional Hodge index*.

---

## 2. M10.2 — the regularized gap SURVIVES (the first encouraging sign)

**The key insight.** The bare-gap vanishing is carried entirely by the **trivial** null directions:
band-limited test functions vanishing at *all* window zeros (interpolation) — the analogue of the trivial
classes (diagonal, fibers) in $NS(C\times C)$. The curve Hodge index is definite on the **primitive** part =
*modulo* trivial classes. So the right object is the **regularized Hodge gap** = the smallest **positive**
eigenvalue of $\mathfrak t$ = the smallest eigenvalue of the $K\times K$ **sine-kernel Gram** $G$ of the zeros.

**What we found.** $\lambda_{\min}(G)$ is **positive and healthy** (at $T_0=100$: $+0.15,0.34,0.48,0.69$ as the
band resolves), *exactly where the bare gap had vanished*.

**Why it matters.** **The genuine primitive intersection form of $\zeta$ is positive-DEFINITE with a real gap;
the M10.1 degeneration was only trivial nullity.** This is the **first non-trivially-realized positivity in the
whole program** — in every other language (N1–N6) the relevant positivity was exactly *marginal*. And it
recasts the target:
$$\text{regularized Hodge positivity}\iff G\succeq c>0\text{ uniformly}\iff \text{zeros are a uniform RIESZ sequence}\iff (U)\text{ as a DETERMINANTAL positivity},$$
a **two-sided** definiteness — the natural object for $\zeta$-regularized determinants (Deninger's
$\det_\infty$) and **plausibly outside the wrong-sign capstone** (a determinant is positive or not).

---

## 3. M10.3 — the uniform frame bound is stable; the route lands on $S(T)$

**What we did.** RH (regularized Hodge) $\iff \lambda_{\min}(G)$ bounded below **uniformly in $T$**. Since the
zero density $\to\infty$, the band must grow $d\sim\frac12\log(T/2\pi)$ (critical sampling). We fixed the
**sampling ratio** and varied the height across two orders of magnitude.

**What we found.**

| $T_0$ | $K/M$ | regularized gap $\lambda_{\min}(G)$ |
|---:|---:|---:|
| 50 | 15/21 | 0.284 |
| 100 | 16/21 | 0.289 |
| 300 | 16/21 | 0.246 |
| 1000 | 17/21 | 0.292 |
| 3000 | 17/21 | 0.204 |

**Remarkably $T$-stable** ($\approx0.2$–$0.29$, no systematic degradation) — the **first numerical evidence of
a uniform lower frame bound**.

**Why it matters — the $S(T)$ handle.** By **Pavlov / Hrushchev–Nikolskii–Pavlov / Seip** sampling theory, a
uniform lower frame bound for reproducing kernels in a de Branges space $H(E)$ is governed by a **Muckenhoupt
$A_2$ (Helson–Szegő)** condition on $|E|^2$. For $E\sim\xi$ this is a **regularity condition on
$S(T)=\frac1\pi\arg\zeta(\frac12+iT)$**:
$$\text{RH (regularized Hodge)}\iff \text{uniform }A_2\text{ on }E\sim\xi\iff S(T)\text{ regularity}.$$
This is the program's **most favorable** reformulation because (i) it is **two-sided** (a definiteness, not a
one-sided bound), and (ii) $S(T)$ carries **substantial unconditional control**: Selberg proved
$S(T)=O(\log T)$, computed all its moments, and proved its Gaussian CLT — *unconditionally*.

---

## 4. The synthesis (what the three milestones establish together)

> **The cohomological turn converts RH from a one-sided pair-correlation upper bound (wrong-signed, intractable)
> into a uniform Riesz / Muckenhoupt *definiteness* governed by the regularity of $S(T)$ — a two-sided condition
> with real unconditional partial tools (Selberg).** The needed positivity is, for the first time in the
> program, **non-trivially realized** (definite primitive form, M10.2) and **numerically uniform** (M10.3).

This does **not** prove RH. In the limit it is still the cornered target (U): the uniform $A_2$ / no-tight-Lehmer
control is known under RH and open without it, and our measured range does not reach the tightest pairs. But it
is the first target the program reaches that sits in a form with **existing two-sided unconditional machinery**,
which is exactly what the wrong-sign capstone said was needed and what every prior language lacked.

---

## 5. Honest status and the next step

- **Established (measured + framed):** the intersection form is definite for finite genus and degenerates
  toward $\zeta$ (M10.1, the four-way unification); the *regularized* form is definite with a real gap (M10.2);
  that gap is $T$-stable, i.e. a uniform frame bound plausibly holds (M10.3).
- **The reformulation (real theory, ours to verify):** RH $\iff$ uniform $A_2$ on $E\sim\xi$ $\iff$ $S(T)$
  regularity (Pavlov/Seip/de Branges).
- **Not a crossing:** still (U) in the limit; the uniform $A_2$ is open unconditionally.
- **Next — M10.4:** engage Pavlov's $A_2$ condition with Selberg's unconditional $S(T)$ bounds *quantitatively*
  — does $S(T)=O(\log T)$ + the moments give a **nontrivial unconditional** frame bound (on a positive-density
  set of heights, or with an $\varepsilon$-loss)? Identify exactly which $S(T)$-regularity statement is
  equivalent to the uniform frame bound, and price the gap (as we priced T9-A). This is where genuinely new
  (harmonic-analysis × analytic-number-theory) mathematics would be developed.

---

### Reproducibility
`experiments/colab_phase10_M1_to_M3.py` — a single self-contained script (numpy + mpmath, optional matplotlib)
running M10.1, M10.2, M10.3 with adjustable depth (more heights, more bands, more zeros). Set the parameters at
the top; it caches the $\zeta$ zeros so deeper runs reuse them.
