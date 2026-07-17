# C1 — Analytic decomposition of `b_bulk(λ)`, and an honest NO-GO for the Cesàro route

**Date:** 2026-06-26 · Phase 62, step C1.

## The decomposition

The Weil matrix is `A = L_arch − L_prime` (Doob-conjugated by the ground state `u₀`, support
`[0,L]`, `L = 2 log λ`). By the explicit formula, each entry splits as

```
A_ij(λ)  =  A_ij^smooth(λ)  +  A_ij^osc(λ)
A_ij^smooth = (archimedean kernel)  −  ∫₀^L f_ij(u) du            [PNT main term, bounded, smooth in λ]
A_ij^osc    = −Σ_ρ ĝ_ij(ρ, λ)                                      [zero-sum; the PNT error term]
```

The bulk band width `b_bulk(λ)` is a (nonlinear, Lanczos) functional of `A`. On the bounded
set established in C0 the Lanczos map `A ↦ b` is locally Lipschitz, so
`b_bulk = b_smooth + (fluctuation driven by A^osc)`, with `b_smooth` bounded and λ-smooth.

E91 confirmed this shape numerically for ζ: `b_bulk(λ) ≈ 0.13 + oscillation`, slope ≈ 0,
Cesàro mean converging.

## The hope, and why it fails (honest)

**Hope (O11 / the Phase 62 thesis):** the Cesàro average `(1/Λ)Σ_{λ≤Λ} A^osc(λ) → 0` is
**unconditional** — provable from the zero-count `N(T) ~ (T/2π)log T` alone, no zero locations.

**Why this is false.** Write a zero as `ρ = β + iγ`. The functional equation pairs `ρ` with
`1−ρ`. The zero-sum probed at band scale `L = 2 log λ` contributes, per conjugate pair, a term
of size

```
λ^{2β−1} · (oscillation in λ^{2iγ}).
```

- If `β = 1/2` (on the line): the factor is `λ⁰ = 1` → a **pure oscillation** `λ^{2iγ}`, and
  `(1/Λ)∫ λ^{2iγ} dλ/λ → 0`. Cesàro averaging works; summing over zeros converges by density.
- If `β ≠ 1/2` (off the line): the factor `λ^{2β−1}` is a **secular growth** (`β>1/2` branch of
  the pair). `(1/Λ)∫ λ^{2β−1} dλ/λ ~ λ^{2β−1}/(2β−1) → ∞`. Cesàro averaging does **not** remove it.

Zero-density estimates bound the *number* and the *imaginary parts* of zeros — they say nothing
about the *real parts*. So they cannot control the off-line growth term. **The Cesàro average
→ 0 is therefore equivalent in strength to "all `β = 1/2`", i.e. to RH itself — not an
unconditional lemma that would prove it.** Averaging over λ does not relieve the obstacle; it
relocates it but leaves it RH-equivalent.

## The falsador proves the point

DH (Davenport–Heilbronn) has genuine off-line zeros (`β ≠ 1/2`). Prediction of the above:
its `b_bulk(λ)` must show **secular growth `~ λ^{2β−1}`**, defeating any Cesàro average.
E90/E91 observed exactly this: DH `b_bulk` grows monotonically (slope +0.056, linear-ish on the
tested range), Cesàro mean never settles — while ζ stays flat (slope −0.002). A log–log fit gives
a DH growth exponent ≈ **0.43** vs ζ ≈ **−0.28** (≈0); the predicted `2β−1 ≈ 0.62` (DH's first
off-line zeros near `β ≈ 0.81`) has the right sign and order, the gap being expected since
`b_bulk` is a nonlinear Lanczos functional summing several zeros over the short range λ ≤ 22.
The falsador is
not a nuisance here; it is the **direct experimental signature** that off-line zeros turn the
oscillation into growth. This both validates the mechanism and refutes the unconditional claim.

## Verdict — C1: NO-GO for the Cesàro route as a *proof* of 2.3.F (with insight)

- The Cesàro average of the zero-sum is **not** unconditional; it converges **iff** zeros are on
  the line. So Cesàro-in-λ does **not** make 2.3.F / the boundedness L1 RH-neutral. This
  sharpens R10's "pointwise L1 touches the wall": **averaging does not move it off the wall.**
- What survives is a **detector**, not a proof: `b_bulk(λ)` bounded (Cesàro-convergent) ⟺ ζ's
  zeros on the line; DH's growth is the off-line control. This is consistent with — and adds a
  new, intrinsic-Jacobi instance of — the program's standing result that every honest route
  reduces to the wall.
- **Do not** record "2.3.F closed in Cesàro topology". That would be a false victory; the DH
  growth term refutes it directly.

## What this leaves open (honest)

The only way `b_bulk` boundedness becomes a genuine *input* (rather than RH-restated) is an
**independent** bound on `A^osc` that does not presuppose `β = 1/2` — i.e. a positivity/geometric
argument (the Weil-positivity / Hodge-index thread, MW-5 / Phase 61 Hodge route). Cesàro
averaging is not that argument. C2–C4 of the Phase 62 plan are therefore **withdrawn** as stated
(they assumed C1 closed); the live lever remains the geometric-positivity route, not λ-averaging.

Cross-refs: [E90_RESULTS.md](E90_RESULTS.md), [E91_RESULTS.md](E91_RESULTS.md),
[phase-61 OPEN-PROBLEMS O11](../phase-61-open-problems/OPEN-PROBLEMS.md),
NO-GO-LIST (entry added: "Cesàro-in-λ does not relieve the boundedness wall").
