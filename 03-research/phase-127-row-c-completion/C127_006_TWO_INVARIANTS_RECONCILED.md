# C127.006 — the two invariants of the series, reconciled

Date: 2026-09-12.  Status: `PROVED`.  Full statement: Paper 45 §12.

Closes the two items Paper 45's first draft had listed as open.

## 1. `I_A` and `T` have different domains; the radical question was ill-posed

`I_A` (row C) is a form on the **radial sector** `G_rad`: sections whose
coefficient depends only on the modulus.  `T` (Paper 43 §8) is a function on all
external classes.  Radial tests see only the modulus, and Paper 43 Thm. 9.3
separates two classes `u, u'` with `|u| = |u'| = 1` by

    T(E_u) − T(E_{u'}) = (v_p(1−u_p) − v_p(1−u'_p)) log p ≠ 0.

So `T` is strictly finer on a strictly larger space, and "is `rad(T) = rad(I_A)`"
is not a well-posed question: the second radical is a subspace of `G_rad`, the
first is not.  Paper 43's mixed sector is exactly the part of `G` that radial
tests cannot see — which is why row A needed the bigger category and rows C/D
live on the radial quotient, where Weil's criterion lives (`𝒯 = C_c^∞(R_{>0}^×)`).

What is needed and is proved (Paper 45 Thm. 12.4): clause **A.6 holds for the
intersection form** on `G_rad` — the radical is closed, a two-sided `†`-stable
ideal, the quotient is Hausdorff with continuous `⋆` and `†`, it contains the
two-dimensional nondegenerate ruling plane, and `I_A` is not identically zero on
its complement (take a primitive `F` with `\hat F` at high frequency: the Gamma
symbol grows like `log(τ/2)` while the prime sum is bounded by
`Σ_{n<e^{2T}}Λ(n)n^{−1/2}‖F‖²`).

## 2. `χ_A` is the shadow's character on the single-zero layer

The apparent difficulty: a fixed-point index at a point where **every** finite
coordinate vanishes is a **product** `∏_v τ_v(σ)`, while `χ_A` is a **sum** over
places.  Resolution: the product is the index at the **deepest** stratum; `χ_A`
is the contribution of the **single-zero layer**, where each surviving stratum
has exactly one normal direction and contributes exactly one factor.  The
difference is precisely the corner strata, and those vanish (Thm. 5.4).

So: **Thm. 5.4 is what turns a product over places into a sum over places** —
the multiplicative Euler datum into the additive explicit formula — and the
mechanism is the irrationality of `log p / log q`.

Consistency with Paper 44: its principal weight `w(Γ_n) = n^{−1/2}(n−1)` is an
instance of the deepest-stratum index, defined there (Thm. 3.3(iv)) as the
principal term of Paper 43's lattice sum, which is what it is.  It is not an
intersection number and is never used as one.  On the surviving labels `n = p^k`
the ramified half `n^{−1/2} = p^{−k/2}` is a **single** local factor, so the
weight `n^{−1/2}Λ(n)` is consistent with `χ_A` being a sum over places.
