# The anchor framework: a ζ-free classification of zero-absence mechanisms

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
The audit's decisive test: *"Can you define 'anchor' without mentioning ζ, poles, Hilbert–Pólya, Weil, or RH? If
yes, you probably found a new object; if no, you are only seeing a pattern among examples."* This document answers
**yes** — the abstract object is a **Landau singularity** — and turns the heuristic into a structural framework:
a ζ-free definition, a theorem recovering de la Vallée Poussin as a special case, a common language for
Hilbert–Pólya / Weil / the P7 line, an explanation of why Littlewood and Motohashi lack an anchor, and a precise
restatement of the RH-directed question. Throughout, **proven** and **conjectural** are kept strictly separate
(the audit's warning about N8's over-reach is the governing constraint).

---

## 0. The ζ-free answer in one line

> **An anchor is a Landau singularity:** the forced real boundary singularity of the transform of a **positive
> (non-negative-coefficient) measure.** *(Landau, 1905: a Dirichlet series / Laplace transform with non-negative
> coefficients has a singularity at its real abscissa of convergence.)* No ζ, no "pole," no Hilbert–Pólya, no
> Weil, no RH appear in this definition. The pole of $\zeta$ at $s=1$ is merely the **instance** of this object
> for the prime measure.

## 1. The framework (all definitions ζ-free)

**Positivity datum.** A pair $(\nu,K)$: $\nu$ a positive (or positive-definite) measure/distribution on a
parameter space $U$, and $K$ a kernel, defining an analytic $F$ by $\log F(s)=\int_U K(s,u)\,d\nu(u)$. *(The
zeros of $F$ are the object of study; the positivity of $\nu$ is the only structural input.)*

**Sum rule.** A finite combination $\sum_j w_j\log|F(s_j)|$ ($w_j\in\mathbb R$) that is $\ge0$ **for free**,
because $\sum_j w_j\,\Re K(s_j,\cdot)\ge0$ pointwise on $\mathrm{supp}\,\nu$ and $\nu\ge0$. Positivity propagates
from $\nu$ to values of $\log|F|$.

**Anchor.** A point $s_*$ where $\int_U K(s_*,u)\,d\nu(u)=+\infty$ — the **principal (Landau) singularity** of the
transform of the positive measure $\nu$. By Landau's theorem this point is **real** and lies on the boundary of
convergence; the positivity of $\nu$ *forces* $\log|F(s)|\to+\infty$ there. This is "a place where $F$ is forced
large by the structure $\nu$ itself, not by the zeros of $F$" — the abstract content of the word *pole*.

**Tight vs. loose budget.** A sum rule's *budget* is the value of its positive part. The budget is **tight** if it
is pinned to a known finite/divergent value by an anchor (so a single extra zero overflows it ⟹ **absence**);
**loose** if it is merely estimated/bounded above (so it only limits the *number* of zeros ⟹ **density**).

## 2. Theorem A — the framework recovers de la Vallée Poussin

> **Theorem A (anchor ⟹ zero-free neighborhood).** Let $(\nu,K)$ be a positivity datum with an anchor $s_*$ at
> which $\log|F(s)|\ge M(s)\to+\infty$, and suppose there is a sum rule
> $w_0\log|F(s_0)|+w_*\log|F(s_*)|+(\text{budget bounded by }B)\ge0$ with $w_0>0$ placing weight on a test point
> $s_0$ near $s_*$. Then $F$ has no zero at $s_0$ once $s_0$ is within the anchor's **reach**
> $\delta = \delta(M,B)$ (the distance over which the positive-definite sum rule transports the anchor's
> divergence past the budget cost $B$).

**Specialization = de la Vallée Poussin.** Take $\nu=\sum_n\frac{\Lambda(n)}{\log n}\delta_{\log n}\ge0$ (the
prime measure), $K(s,u)=e^{-su}$, so $F=\zeta$. The anchor is the Landau singularity at $s_*=1$. The sum rule is
$3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\ge0$. The budget cost $B$ is the convexity growth
$\log|\zeta(\sigma+2it)|\ll\log t$. Theorem A returns the classical reach $\delta\asymp1/\log t$ — the de la
Vallée Poussin zero-free region. **The classical theorem is the $s_*=1$, prime-measure instance of Theorem A.**
*(This is the proven core; it requires no conjecture.)*

## 3. The classification — competing theories are one ingredient at different locations

In this language the "competing" routes are **the same construction, an anchor at a different location, via a
different positive structure**:

| mechanism | positive structure $\nu$ | anchor location $s_*$ | status |
|---|---|---|---|
| de la Vallée Poussin | prime measure | $\sigma=1$ (Landau, real abscissa) | **proven** (Theorem A) |
| Vinogradov–Korobov | prime measure + exp-sum input | $\sigma=1$, wider reach | proven (extra cancellation widens reach) |
| Hilbert–Pólya | spectral measure of a self-adjoint operator | the **real axis $=\sigma=\tfrac12$** (self-adjointness $\Rightarrow$ real spectrum) | conjectural (no operator) |
| Weil positivity | the Weil explicit-formula functional | $\sigma=\tfrac12$ via the functional equation | conjectural (sign undetermined) |
| P7 → T4 (this program) | the localized Weil–Gram measure | $\sigma=\tfrac12$, variational | conjectural ($=$ capstone) |
| function-field RH (Weil/Deligne) | intersection form on a surface | the diagonal (Hodge index $\Rightarrow$ positivity) | **proven** (geometric anchor exists) |

> The unification the audit anticipated is now literal: **all of these manufacture a Landau-type anchor; they
> differ only in (a) the location ($\sigma=1$ vs $\sigma=\tfrac12$) and (b) the positive structure used to force
> the singularity there.** The pole gives an anchor at $\sigma=1$ unconditionally and for free; every route that
> would reach $\sigma=\tfrac12$ is a different attempt to force a Landau-type singularity **at the center**.

## 4. Why Littlewood and Motohashi lack an anchor (the ζ-free reason)

Both are positivity-based ($\int|\zeta|^2$, $\int|\zeta|^4$ are positive), so they *have* a positivity datum — but
its budget is **loose**: the mean value is *estimated from above*, with no Landau singularity pinning it at the
critical line. Landau's theorem places the prime measure's only forced singularity at $\sigma=1$, **not** at
$\sigma=\tfrac12$; so on the critical line these routes have no anchor to make the budget tight, and a loose
budget bounds only the *count* of zeros — **density, never absence.** This is exactly N8's square-root barrier,
now seen as a *corollary*: anchorless routes must *estimate* the loose budget, and estimating it to one-zero
precision is the square-root barrier.

## 5. The organizing conjecture (stated AS a conjecture)

> **Anchor Classification Conjecture (ACC).** Every unconditional proof of *absence* of zeros in a region is a
> positivity datum together with an anchor (a Landau-type forced singularity of a positive structure) whose reach
> covers the region. Equivalently: *no anchor ⟹ at best density.*

**Evidence (not proof):** every known unconditional analytic zero-free region (de la Vallée Poussin,
Vinogradov–Korobov, and their relatives) is positivity $+$ pole; the only **proven** RH (function field) is
positivity $+$ a geometric anchor (Hodge index). No known absence proof falls outside the scheme. **Counter-test
(open):** exhibit an unconditional absence proof with no positivity datum and no anchor — none is known. *(Proving
ACC would itself be the structural classification the audit asked for; it is not claimed here.)*

## 6. The RH-directed question, restated ζ-free (and what it is / isn't)

> **Q(anchor), ζ-free form.** Does there exist a **positive (or positive-definite) structure whose transform is
> forced to have a Landau-type singularity on the critical line $\sigma=\tfrac12$**, with reach covering a
> neighborhood — i.e., a center-anchor analogous to the prime measure's pole at $\sigma=1$?

- This is a **construction** problem (build a positive structure singular at the center), not a **cancellation**
  problem. It is therefore genuinely **different** from N8 and **was not collapsed** by any prior audit.
- It **subsumes** Hilbert–Pólya (the structure $=$ a self-adjoint spectral measure, singular on the real axis $=$
  the center) and Weil positivity (the structure $=$ the explicit-formula functional, anchored at the center by
  the functional equation) as **two concrete proposals for the same object**.
- **Honest caveats (no repeat of N8's over-reach):** (i) Q(anchor) **may** turn out RH-equivalent — Hilbert–Pólya
  and Weil are this question, and both are open at exactly the point where the center-anchor must be *forced*
  rather than *assumed*; I do **not** claim it is more elementary than RH. (ii) ACC is a **conjecture**; "every
  absence proof needs an anchor" is supported by all known cases but unproven. What *is* established is the ζ-free
  **definition** (Landau singularity), **Theorem A** (de la Vallée Poussin is the $s_*=1$ instance), and the
  **reframing** of RH as a center-anchor *construction*.

## 7. The proposed path (bold, but staged so each stage is checkable)

1. **Formalize** the positivity-datum / sum-rule / anchor framework and **prove Theorem A** in full generality
   (recovering de la Vallée Poussin and Vinogradov–Korobov as instances). *Fully rigorous; no conjecture.* This
   makes "anchor" a theorem-grade object.
2. **Express Weil positivity and the function-field Hodge anchor in the framework**, verifying both are
   "anchor at the center / diagonal." This tests the language on the one *proven* RH (function field) — if the
   geometric anchor fits, the framework is real.
3. **Attack Q(anchor) as a construction problem:** search for *any* positive structure with a forced (Landau-type)
   real singularity at $\sigma=\tfrac12$ — including non-arithmetic toy models (a positive measure engineered to
   have abscissa $\tfrac12$ relative to the relevant symmetry) to learn what *obstructs* a center-anchor. The
   obstruction itself, if one is found, is the next honest wall — and it will be a wall about *positive structures
   and their singularities*, not about cancellation.

**Assessment, honestly.** Are we "close"? The **framework** is real, ζ-free, and new as an organizing object, and
it converts RH into a sharply posed construction problem that the audits did **not** collapse. Whether the
construction *exists* is exactly Hilbert–Pólya/Weil and may be RH-hard — so I will not claim a short path to RH.
But the audit's own criterion is met: this is a direction that looks at the zeros' absence mechanism itself, is
not a reformulation-via-cancellation, and has not been disposed of. That is the boldest *honest* step available.
