# BARRIER_Z_001 — Parity sectors of 𝔞_T on P_T: the "1e-14 degeneracy" is level smallness, not a hidden splitting

Phase 197, track Z. Memo, no audit yet. Row D OPEN.
Script: `scripts/z001_parity_split.py` (mpmath, exact rational c(u)-polynomials, NUMÉRICO, not interval).

## Corpus / index check and new reason
Index checked (README §phase 197 lines BARRIER_W/X/Y; parity entries X2, X4; Theorem P n₋ bounds; first-contact
obstruction; Kreĭn; INV_S_001 S2 frozen contacts; INV_U_001; W1–W3). The question "is the even/odd near-degeneracy
reported in BARRIER_Y_001 §2 a genuine exponentially small splitting (hidden intertwiner)?" is not in the index.
New reason: it is a diagnostic of an artefact reported in Y_001, settled by a parity-resolved multiprecision computation
that Y_001 declared necessary and did not perform. No route is reopened.

## 1. Exact parity decomposition (PROVED, elementary)
R F(t) = F(−t) preserves c_F(u) = ∫F(t)F(t−u)dt (c_{RF}(u) = c_F(−u) = c_F(u)), hence every term of eq:Aform, and
swaps the Tate functionals ∫F e^{±t/2}. So R commutes with 𝔞_T on P_T, and P_T = P_T^+ ⊕ P_T^− with
P_T^+ = {F even, ∫F cosh(t/2) = 0}, P_T^− = {F odd, ∫F sinh(t/2) = 0}; λ_A(T) = min(μ_+(T), μ_−(T)).
The sectors are exactly decoupled for every comb (the comb enters only through c(log n)), so any "near-symmetry" would
have to be an approximate intertwiner P_T^+ → P_T^−, not R.

## 2. Parity-resolved bottoms, Λ (NUMÉRICO; monomial Galerkin, dps = M+90; values are upper bounds)
| T | M | μ_even | μ_odd | μ_odd/μ_even |
|---|---|---|---|---|
| log2 | 32/40 | 1.06e-7 / 1.04e-7 | 1.13e-5 / 1.12e-5 | ≈107 |
| 0.8 | 48/56/64 | 6.13e-12 / 5.57e-12 / 5.42e-12 | 1.086e-9 / 1.033e-9 / 1.010e-9 | ≈186 |
| 0.9 | 48/56/64 | 8.3e-17 / 5.8e-17 / 5.0e-17 | 1.96e-14 / 1.77e-14 / 1.60e-14 | ≈320 |
| 1.0 | 48/56/64 | 1.8e-20 / 4.5e-21 / 2.5e-22 | 3.8e-18 / 1.5e-19 / 5.3e-20 | not converged |
| 1.1 | 48/56/64 | 3.7e-22 / 3.0e-25 / 3.8e-26 | 6.9e-20 / 9.1e-23 / 6.3e-24 | not converged |
| 1.2 | 48/56/64 | 1.1e-23 / 4.6e-27 / 2.8e-30 | 6.0e-24 / 1.2e-24 / 5.5e-28 | not converged |
| 1.3 | 48/56/64 | 5.6e-28 / 1.5e-30 / 2.4e-32 | 1.2e-25 / 2.6e-28 / 2.2e-30 | not converged |

Converged range (T ≤ 0.9, relative change ≲ 10% between M = 56 and 64): log μ_even and log μ_odd decay at the same
rate, ≈ −116 and −110 per unit T on [0.8, 0.9], and μ_odd − μ_even ≈ μ_odd(1 − O(10⁻²)). The splitting has no rate of
its own: it equals the larger level up to ~1%. For T ≥ 1 polynomial Galerkin with M ≤ 64 resolves neither level (both
keep dropping by orders of magnitude with M, below 10⁻¹⁹); in that range only upper bounds are available, and the sign
of μ_even − μ_odd flips with M (T = 1.2, M = 48). That flip is the M-instability seen in Y_001: it is truncation, not
physics.

## 3. Interpretation
- The Y_001 "degeneracy to 1e−14" means: both sector bottoms are ≤ 2·10⁻¹⁴ at T ≥ 0.9, i.e. below double precision.
  Their ratio is 10²–10³, not 1. No near-degenerate pair of nonzero levels, hence no exponentially small tunnelling
  splitting and no evidence of an approximate even↔odd intertwiner. Consistent with INV_S_001 S2 (no double well).
- Even sector is the minimizing one throughout the converged range (F⋆ even), matching Y_001 at T ≤ ½log5+0.01 and
  extending it to T = 0.8, 0.9; for T ≥ 1 the parity of F⋆ is undetermined at M ≤ 64.
- Both levels sit at the λ_A first-contact scale (cor:margin1 envelope; the corpus first-contact phenomenon). Record,
  no novelty. Item (2b) of the brief (test ℤ-specificity of an intertwiner on a_P, cΛ, Beurling combs) is void:
  there is no splitting to test.

## 4. Labels
- §1 parity decoupling: PROVED.
- §2 numbers: NUMÉRICO (non-interval mp, Galerkin upper bounds; converged only for T ≤ 0.9).
- Conclusion "splitting = level scale, no hidden symmetry": NUMÉRICO for T ≤ 0.9, OPEN for T ≥ 1 (needs a
  non-polynomial basis adapted to the near-kernel, e.g. the Sonin/prolate basis, to resolve levels below 10⁻²⁰).
- NO-GO (record): "hidden even/odd near-symmetry as a source of sign" — no such structure in the converged window.
