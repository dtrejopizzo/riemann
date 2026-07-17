# Phase 10 — The cohomological turn: the one path that escapes the wrong-sign capstone, and the new mathematics it demands

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
The mandate: a path *more* novel than anything we have done, one that requires developing **new mathematics**.
The wrong-sign capstone (Part VII of the master document) tells us exactly what such a path must do, and there
is essentially **one** structure in mathematics known to do it. This document explains the rationale, the
program, our concrete entry point, a first computable milestone, and the honest horizon.

---

## 1. What the capstone demands of any new path

> **Capstone.** Every unconditional handle on the zeros is a *positivity* ($\ge0$), oriented to give
> **lower** bounds. RH is a one-sided **upper** constraint. Zero-level positivity is the wrong sign.

So a path that can cross must produce an **upper** bound — and the only way the capstone leaves open is a
positivity at a **higher level** (a cohomological / intersection-theoretic pairing) that *yields* the
zero-level upper bound by **duality**. This is not speculation: it is precisely how the **only** Riemann
Hypothesis humanity has ever proved — the **Weil conjectures for curves over finite fields** — was proved.

**The template (Weil/Grothendieck/Deligne).** For a curve $C/\mathbb F_q$, Frobenius $\mathrm{Frob}$ acts on
$H^1(C)$; RH is $|\text{eigenvalues}|=q^{1/2}$. The **upper** bound $|\alpha|\le q^{1/2}$ comes from the
**Hodge index theorem** on the surface $C\times C$: the intersection form is negative-definite on the
*primitive* cohomology, and applying this negative-definiteness to the graph of Frobenius (a Cauchy–Schwarz in
the intersection pairing) forces the eigenvalue bound. **A higher-level positivity (Hodge index) yields a
zero-level upper bound (RH) by duality.** The wrong-sign capstone is escaped because the positivity is *not on
the zeros* — it is on the intersection form of an algebraic **surface**, and duality flips it.

**The new path, in one line.** *Build, for $\operatorname{Spec}\mathbb Z$, the arithmetic analogue of the
surface $C\times C$ and its Hodge-index positivity — and RH follows by the same duality.* The missing
ingredient is the **cohomology theory** (and the surface) themselves. Constructing them is the new mathematics.

---

## 2. The program and its lineage

This is the deepest and most novel frontier, pursued in pieces by the field for decades:
- **Deninger's program:** an (conjectural) infinite-dimensional cohomology $H^1$ with an operator $\Theta$
  (an "infinitesimal Frobenius") such that $\zeta(s)=\det_\infty\!\big(\tfrac{1}{2\pi}(s-\Theta)\big)^{-1}$-type
  regularized determinants hold, and RH $=$ self-adjointness/positivity of a Lefschetz cup-product form. The
  cohomology is missing.
- **Connes–Consani's arithmetic/scaling site and "Riemann–Roch for $\operatorname{Spec}\mathbb Z$":** a topos
  and an intersection theory aiming at the surface and a Hodge-index analogue. Incomplete — the positivity
  (the analogue of Castelnuovo–Severi) is exactly what is open.
- **$\mathbb F_1$-geometry (the field with one element):** the program to see $\operatorname{Spec}\mathbb Z$ as
  a "curve over $\mathbb F_1$", so that base-change to "$\mathbb F_1$-bar" and a Frobenius give the Weil proof.
  $\mathbb F_1$ is not yet a rigorous enough object to run the argument.

Our program connects to this lineage through a concrete, already-built bridge: **the Weil explicit formula is
the candidate Lefschetz trace formula**, and **our localized Weil–Carleson form is the candidate intersection
form** on the primitive part. We can use what we have built to *constrain and partially construct* the missing
structure — which is a genuine, finite way to contribute to an otherwise infinite program.

---

## 3. Our concrete entry point (what we uniquely bring)

The dictionary, made explicit:

| Weil-conjectures object (curve $C/\mathbb F_q$) | Our object (for $\zeta$) |
|---|---|
| surface $C\times C$ | the hypothetical "arithmetic surface" $\overline{\operatorname{Spec}\mathbb Z}\times_{\mathbb F_1}\overline{\operatorname{Spec}\mathbb Z}$ |
| Lefschetz trace $\sum(\mathrm{Frob}^n\cdot\Delta)$ | the **Weil explicit formula** $\sum_\rho\hat g(\rho)=\text{arch}-\text{primes}$ |
| intersection form on $\mathrm{NS}$, Lorentzian sig. $(1,\rho{-}1)$ | the **Weil quadratic form** + a missing **ample/polarization** direction |
| Hodge index: neg.-definite on primitive part | **Weil positivity** $\mathfrak t\succeq0$ (= RH) |
| diagonal $\Delta$, Frobenius graph $\Gamma_{\mathrm{Frob}}$ | the diagonal / the prime correspondences (Frobenius at $p$) |

**The key structural question (and our handle on it).** In the curve case the intersection form is *Lorentzian*
(signature $(1,N{-}1)$): one positive ("ample") direction, the rest negative; RH is the negative-definiteness on
the primitive (ample-orthogonal) part. **Our Weil–Carleson form is, instead, essentially positive** ($C\le1$,
$A_\Phi-P_F\succeq0$ for ζ). The reconciliation — and the new structure to find — is:

> **M10 thesis.** *The Weil–Carleson form is the restriction of a larger **Lorentzian** intersection form to
> its primitive part; the missing "ample direction" is the polarization of the arithmetic surface (morally, the
> archimedean place / the $\infty$-section). Identifying that ample class and the full Lorentzian structure —
> for which our detector gives the primitive block explicitly — is the concrete skeleton of the missing
> cohomology, and the place our computational machinery can actually build something.*

This escapes the wrong-sign capstone by construction: positivity lives on the *intersection form* (a Hodge
index), and RH is the induced *upper* bound — not a zero-level positivity.

---

## 4. The first computable milestone (M10.1)

**M10.1 — reconstruct the Lorentzian envelope.** Concretely and with our existing engine:
1. Take the Weil–Carleson Gram on a band-limited test space (the detector's $A_\Phi-P_F$, with its known
   primitive/positive block).
2. **Adjoin a candidate ample direction** $\ell$ (the archimedean "polarization": the constant/pole mode, or
   the $\infty$-section functional) and form the enlarged pairing $\widehat Q=\begin{pmatrix}-\kappa & b^{*}\\ b & A_\Phi-P_F\end{pmatrix}$.
3. **Test the Hodge-index signature:** does there exist a coupling $(\kappa,b)$ making $\widehat Q$ **Lorentzian**
   (exactly one positive eigenvalue) with the Weil form recovered as the restriction to $\ell^{\perp}$? If yes,
   we have an explicit *finite-dimensional model of the intersection form*, and the Hodge-index inequality on it
   reproduces the $\delta^2$ forced-negativity law (a check). If no, the ample direction is mis-identified —
   iterate.
4. **The payoff to look for:** whether the *self-intersection* of the prime correspondences (the diagonal
   restricted form) obeys the Castelnuovo–Severi inequality $\Gamma^2\le 2\,(\Gamma\!\cdot\!\Delta)\cdots$ in this
   model — the inequality that *is* RH in the curve case. Reproducing its **shape** (even numerically) would be
   the first concrete sign that the arithmetic surface has the right intersection theory.

This is buildable now, with the validated detector supplying the primitive block, and it is genuinely new: to
our knowledge no one has tried to *reconstruct the Lorentzian envelope* of the Weil form from the detector and
test the Castelnuovo–Severi shape numerically. It cannot prove RH (the surface/cohomology is still missing),
but it can **falsify or support** the surface picture concretely and identify the ample direction — a real,
finite first brick of the new mathematics.

---

## 5. Why this is the right "new mathematics" bet

- It is the **only** structure known to escape the wrong-sign capstone (higher-level Hodge positivity →
  zero-level upper bound), and it is **how the one proven RH was proved**. That is the strongest possible prior
  for a genuinely new direction.
- It **requires inventing mathematics** (the cohomology / the surface / $\mathbb F_1$), exactly as requested —
  but it is not pure speculation: it has a concrete dictionary to our built objects, and a computable first
  milestone.
- Our **unique contribution** is the detector: it gives the **primitive block** of the intersection form
  explicitly and numerically, which the abstract programs (Deninger, Connes–Consani) do not have in hand. We
  can *build and test the finite model*, which is a different and complementary mode of attack.

**Honest odds.** Constructing the arithmetic cohomology is a generational problem; full RH this way is $\ll1\%$
and decades-deep. But M10.1 is finite, novel, and either falsifies or sharpens the surface picture — and even a
negative result (the Lorentzian envelope does **not** close) would be a genuine structural theorem (a seventh
no-go, the first one *about the cohomological route*).

---

## 6. The methodology (unchanged, proven)

Precise milestones stated to prove or break (M10.1 first); verify-first with the engine; self-refute before
building; the anti-circularity gate against the six-language map; honest logging in the bitácora. The same
discipline that produced N1–N6 and the capstone — now aimed at the one structure that, in principle, could turn
the corner.

### Status / next
- Rationale (escape the capstone via Hodge-index duality, à la Weil conjectures) — ✅ stated.
- Program + lineage (Deninger, Connes–Consani, $\mathbb F_1$) + our dictionary — ✅ laid out.
- **Next: M10.1** — reconstruct the Lorentzian envelope of the Weil–Carleson form from the detector; test the
  Hodge-index signature and the Castelnuovo–Severi shape. Buildable now.
- Honest: a generational bet; M10.1 is the finite, novel first brick; either outcome is informative.
