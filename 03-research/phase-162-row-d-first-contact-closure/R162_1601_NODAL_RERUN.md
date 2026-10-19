# R162_1601 — Nodal rerun after the tail-sign fix, and the deletion test of R-C

Numerical check. **Everything here is UNCERTIFIED float.** It is guidance only, not proof.
Inputs: R162_1501 §4, R162_1590 (the bug `G=G+abs(sign)*tail`, now `sign*tail`), Paper 47 cor:convfail(i).
Script: `scripts/c3/t1601_nodal_rerun.py <zeta|del> <K list> <T list>`. It uses the same Galerkin setup as t1501:
Legendre basis, t-grid on [0,3000] plus the analytic tail, S counted on a 4001-point grid with |f| below 10⁻⁶·max
ignored, and K_F(a) = co·vec(a). The fixed t1501 scripts give the same numbers at K = 34.
Notation: λ is the bottom of the Tate-constrained parity block. r = ‖AF − λF‖ is the Tate residue. μ₁ < 0 and ψ are
the bottom eigenpair of the unconstrained A. u₂ is the second eigenvector of A.

## 1. ζ weights, K = 34 / 46 / 60

Even primitive bottom:

| T | λ (K=34 / 46 / 60) | S | K_F(a₁..a₄) (K=60, overall sign free) | r/λ | ⟨F,ψ⟩·abs(μ₁)/λ | abs⟨F,u₂⟩ |
|---|---|---|---|---|---|---|
| 0.30 | 6.92e-1 (all K) | 2 | .0556 .200 .469 .937 | 0.37 | — | 0 |
| 0.50 | 1.19e-2 (all K) | 2 | .192 .770 2.15 5.31 | 0.74 | 0.73 | 1.000 |
| 0.60 | 6.74e-5 / 6.68e-5 / 6.66e-5 | 2 | .228 .944 2.76 7.25 | 0.81 | — | 1.000 |
| 0.65 | 2.40e-6 / 2.35e-6 / 2.32e-6 | 2 | .241 1.01 3.00 8.09 | 0.84 | — | 1.000 |
| 0.70 | 5.94e-8 / 5.71e-8 / 5.62e-8 | 2 | .253 1.07 3.23 8.89 | 0.87 | — | 1.000 |
| 0.75 | 8.73e-10 / 7.68e-10 / 7.55e-10 | 2 | .262 1.12 3.42 9.57 | 0.90 | — | 1.000 |
| 0.78 | 6.14e-11 / 4.50e-11 / 4.17e-11 | 2 | .268 1.15 3.54 10.0 | 0.92 | — | 1.000 |
| 0.8047 | 6.65e-12 / 3.69e-12 / 3.27e-12 (certified ≈2.5e-12) | 2 | .272 1.17 3.62 10.3 | 0.93 | 0.93 | 1.000 |
| 1.0 | ~1e-15 (noise floor) | 2 | not stable in K (0.34 / 0.36 / 0.64 for a₁) | — | — | not stable |
| 1.2 | ~−1e-15 (noise floor) | 4 / 4 / 6 | not stable | — | — | — |

Odd primitive bottom: S = 3 (the minimum) at every T in [0.3, 0.8047] and for all three K. K_F(a₁..a₄) has one sign.
⟨F,ψ⟩ = 0 by parity. At 1.0–1.2 the values are noise (S = 3/5/9, λ < 0 at the 1e-16 level).

Unconstrained A: bottom S = 0 at every T. Prop N1 ✓ survives.

## 2. Which R162_1501 §4 claims survive

| R162_1501 claim | Status after the fix |
|---|---|
| Unconstrained bottom S = 0 | **Survives** |
| Even bottom S = 2 at 0.3, 0.5 | **Survives** |
| Level crossings with S = 6, 4, 4, 6 at 0.6–0.75 | **Artifact of the bug.** S = 2 throughout [0.3, 0.8047]. There is no crossing. The branch is u₂(A) from 0.5 on. |
| S = 2 at 0.78, 0.8047 | **Survives** (stable in K) |
| S = 2 at 1.0, 1.2 | **Not supported.** λ is at the 1e-15 noise floor, and S and the vector change with K. |
| Coincides with μ₂(A) | **Survives** on [0.5, 0.8047] (abs⟨F,u₂⟩ = 1.000) |
| K_F(a₁..a₄) one sign on the even bottom | **Survives** on [0.3, 0.8047]. The values change: at ½log5 they are .272, 1.17, 3.62, 10.3, not 0.48, 2.56, 10.3, 38.5. |
| ‖r‖/λ ≈ 0.57–0.59; ⟨F,ψ⟩ ≈ 0.6λ/abs(μ₁) | **Qualitatively survives** (r = O(λ), asymptotically Type I). The constant is ≈ 0.93 at ½log5, rising from 0.74 at T = 0.5. |
| Odd bottom S = 7 / 5, "not minimal" | **Artifact.** The odd bottom has S = 3, which is minimal, on [0.3, 0.8047]. |
| λ not converged for T ≥ 0.8 (4.4e-7) | Replaced. λ(½log5, even) = 6.6e-12 / 3.7e-12 / 3.3e-12 for K = 34/46/60. This decreases toward the certified 2.5e-12. |

## 3. Deletion model a = Λ·1_{n≥5}

For T < ½log5 no contact is active, so the form is purely archimedean.

| T | λ_even | S | K_F(a₁..a₄) | r | ⟨F,ψ⟩ | μ₁, μ₂ of A | λ_odd (S) |
|---|---|---|---|---|---|---|---|
| 0.46 | 2.62e-1 | 2 | .169 .668 1.82 4.35 | .266 | .139 | −1.62, −0.20 | 5.60e-1 (3) |
| 0.55 | 8.12e-2 | 2 | .273 1.16 3.48 9.46 | .273 | .140 | −1.84, −0.38 | 3.80e-1 (3) |
| 0.58 | 2.73e-2 | 2 | .315 1.37 4.28 12.2 | .276 | .141 | −1.90, −0.44 | 3.27e-1 (3) |
| **0.595818** (contact) | 0 (±1e-13) | **2** | **.339 1.50 4.77 13.9** | **.278** | **.141** | −1.94, −0.47 | ≈3.0e-1 (3) |
| 0.60 | −7.11e-3 | 2 | .346 1.53 4.90 14.4 | .278 | .141 | −1.95, −0.47 | 2.93e-1 (3) |
| 0.65 | −8.86e-2 | 2 | .431 2.00 6.85 21.7 | .284 | .142 | −2.05, −0.56 | 2.12e-1 (3) |

- K = 34 and K = 46 agree to all digits shown. Contact T_c = 0.595820 (K=34) and 0.595817 (K=46). This is consistent
  with Paper 47's 0.58–0.60 window and the ≈0.596 threshold.
- The contact vector is even, with S = 2 and K_F(a₁..a₄) all of one sign (positive).
- **It is not Type I.** r = 0.278 and ⟨F,ψ⟩ = 0.141 stay O(1) while λ → 0, so r/λ → ∞. F is orthogonal to u₂
  (abs⟨F,u₂⟩ = 0). A has two negative eigenvalues. The contact is a genuinely Tate-constrained vector, of Type II
  shape (F ∝ A⁻¹φ with a nonzero residue).

## 4. Verdict on R-C (float)

- **Weight-blind parts:** "S = 2" and "coherent sign of K_F(a₁..a₄)" hold for the deletion contact exactly as for ζ.
  They cannot separate ζ from deletion.
- **Not weight-blind:** the Type I property (r = O(λ), ⟨F,ψ⟩ = O(λ), contact vector ≈ a near-null eigenvector of the
  unconstrained A). ζ has it on [0.5, 0.8047]. Deletion violates it (r/λ = ∞ at contact).
- So R-C survives the deletion falsifier only in its (C1)/Type I clause. The nodal clause S = 2 alone is weight-blind.
