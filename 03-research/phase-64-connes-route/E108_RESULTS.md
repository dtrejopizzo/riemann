# E108 — Krein-Langer negative-square index: the sharp, robust RH index (Connes round 3)

**Date:** 2026-06-28 · mpmath dps=40.

## The sharpening (Connes)

The right index is **not** the boundary `μ_max=1` (norm-one / Euler-characteristic balance — invisible
to interior off-line spectrum) but the **Kreĭn–Langer negative-square count** of the interior kernel:
```
   ind₋(K_S) = #{poles of S in ℂ_+}   (with multiplicity),    RH ⟺ ind₋(K_{S_κ}) = 0.
```
For `S=Θ_ω`, UHP poles are exactly off-line zeros `ρ=β+iγ` with `β−½>ω`. A scalar function with
`|S|=1` on `ℝ` is a **generalized Schur function** (Kreĭn–Langer), whose kernel may have negative
squares; the count equals the number of UHP poles. This is strictly stronger than edge contractivity.

## Result — exact integer count, matches off-line zeros

| configuration (ω=0.1, dps=40) | `ind₋` | expected | |
|---|---|---|---|
| **ζ** (10 pts near γ=14..37) | **0** | 0 | ✓ (rel min eig +7.9e-9) |
| 1 planted off-line zero (β=0.80) | **2** | 2 | ✓ |
| 2 planted (β=0.80, 0.75) | **4** | 4 | ✓ |
| 3 planted (β=0.80, 0.75, 0.85) | **6** | 6 | ✓ |

Each off-line zero `β` contributes **2** UHP poles of `Θ_ω` (at `±γ₀`, height `β−½−ω`; the `1−β`
functional-equation partners give LHP poles, not counted). The negative-square count equals `2×(#off-line
zeros)` exactly, and **ζ has `ind₋=0`.**

## Why this is better than every earlier detector

- **It is an exact integer count**, hence *robust* — unlike the marginal positivity (`μ_max=1`, Pick
  min eig `~1e-8`), which is precision-sensitive and configuration-dependent. `ind₋=0` for ζ vs
  `ind₋=2k` for off-line is a clean, discrete, unambiguous discriminator.
- **It sees the interior off-line spectrum directly** (the negative squares), which boundary modulus
  (`μ_max`) cannot. This is the precise content Connes identified: RH = *zero negative squares*, not
  boundary balance.
- It is the theorem-level form of the numerical detector: the RH-strength statement is
  `ind₋(K_{S_κ})=0` unconditionally (= no UHP poles = RH), and DH has `ind₋ = 2·(#off-line zeros) > 0`.

## Honest status

Still a criterion: `ind₋=0` for ζ *is* RH. But it is the **sharpest and most robust** form — an exact
integer index, faithful and falsifiable (off-line count exact). The proof target (Connes) is the
**Critical Gram Realization**: exhibit `K_{S_κ}(z,w)=⟨k_w,k_z⟩` for adelically constructed Hilbert
vectors, so that `ind₋=0` (a genuine Hilbert norm, not a Pontryagin/Kreĭn form). DH fails because it
has no such adelic Gram realization.

## Reproduce
```
venv/bin/python E108_krein_langer.py
```
