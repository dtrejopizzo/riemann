# CC_001 — The mixed lag log 6 and the κ-Hessian in the laboratory T ∈ (½log6, 17/16] (track CC, phase 198)

Status: memo, not yet audited. Labels: PROVED / CONDITIONAL / ARGUED / NO-GO / OPEN / NUMÉRICO.
Row D remains OPEN.

## 0. Corpus / index check
ROUTES-TRIED-INDEX/README (phases 186–198; BARRIER_001 sign-carrier spec and Thm 3/5; BB_001; AA_001; BARRIER_Y_001),
04_PHASES_100-189 (Theorem X, W-fam, R186_036), phase 190 (near-coincidence, "no ζ-specific prime-side fact"),
phase 193 (frustrated cycle (m,2m)), INV_I I2/I4, R186_005 TB3-neg, N_018 (Bochner/Cauchy–Schwarz), grid R162_2300,
crossword . Concavity of λ in a scalar multiplier is BB_001 §2 (not reclaimed).
**New reason:** none of these takes the *per-prime* multi-parameter family a_κ and asks for the **second-order mixed
derivative ∂²λ/∂κ_2∂κ_3** (the only place where two different κ_p can multiply inside λ itself) or tests c_{h*}(log 6)
in the window where lag 6 is active and Λ is positive (Liu, CITED in P47) while a_2 is certified negative.
BB5 asked exactly this; CC answers it.

## 1. Exact window form (PROVED, elementary)
For T ≤ 17/16, e^{2T} < 8.38, so the prime powers in the window are 2,3,4,5,7 (and 8 iff T > ½log8 ≈ 1.0397). With
a_κ(p^k) = κ_p log p (P47 eq:Aform, v_n = 2a(n)/√n):
  a_T(F;κ) = Arch_T(F) − κ_2 L_2(F) − κ_3 L_3(F) − κ_5 L_5(F) − κ_7 L_7(F),
  L_2 = 2log2[2^{-1/2}c_F(log2) + 2^{-1}c_F(log4) + 2^{-3/2}c_F(log8)·1_{T>½log8}],  L_p = 2log p·p^{-1/2}c_F(log p) (p=3,5,7).
**(CC1) The lag log 6 does not occur:** a(6)=0, so a_T is affine in κ with coefficients functionals of c_F at
prime-power lags only. Hence λ(κ) = inf_F a_T(F;κ)/‖F‖² is concave on ℝ^4 and, at a simple bottom,
∂λ/∂κ_p = −L_p(h*) (Hellmann–Feynman). c_{h*}(log 6) enters neither λ nor ∇λ. (PROVED)

## 2. Where the two κ's do multiply: the Hessian (PROVED, standard perturbation theory)
Let S(κ) be the compression of a_T to P_T^± (each parity sector separately; R commutes, BARRIER_Z), simple bottom
λ with gap g > 0, reduced resolvent R_⊥ = (S − λ)^{-1} on h*^⊥. Then
  H_pq := ∂²λ/∂κ_p∂κ_q = −2⟨C_p h*, R_⊥ C_q h*⟩,   H ≼ 0,   |H_23|² ≤ H_22 H_33.            (CC2)
On ℝ (no compression) C_2C_3 would contain translations τ_{±log6} and τ_{±log(3/2)} — the semiring product and the
near-coincidence quotient enter **together and symmetrically**, as in BB2. On P_T the projection 1_{[−T,T]} and the Tate
constraint sit inside R_⊥, so H_23 is not a function of c_{h*}(log 6) at all. The only structural constraints on H are
negative semidefiniteness and Cauchy–Schwarz; **neither fixes the sign of H_23** (any off-diagonal sign is compatible
with H ≼ 0). (PROVED)

**(CC3) Edge bound (PROVED, trivial).** |c_F(u)| ≤ ‖F·1_{[u−T,T]}‖·‖F·1_{[−T,T−u]}‖. At T=1, u=log6, both strips have
length 2T−log6 ≈ 0.208: c_{h*}(log 6) is controlled by the edge mass of h*. Bochner positivity of [c_F(x_i−x_j)] on
{0,log2,log3,log6} (lags log2, log3, log(3/2), log6) holds for every F: comb-generic (N_018 family).

## 3. NO-GO CC4 (PROVED modulo simplicity; ARGUED at Λ): the cross-derivative is not ℤ-specific
Let positions u_p (u_p = log p for ℤ; Beurling-type: u_3 = log3 + δ). If the bottom is simple, S depends analytically on
(κ, u) and so do λ and H (Kato). The coincidence u_2 + u_3 = log 6 is codimension one and **log 6 is not a position of
the comb** (CC1); H_23 is continuous across δ = 0. So any sign of H_23 at ℤ holds on an open set of non-ℤ positions:
an open condition in positions cannot be ℤ-specific, clause (1) of the sign-carrier spec fails. At Λ itself the
bottom is numerically near-degenerate (§4), H ~ 1/g is not a stable object, which only worsens the situation.
The same continuity argument applies to the per-prime falsifier a_P (κ_P = 0): H is defined and continuous there.

## 4. Numerics (NUMÉRICO, mpmath 30–40 digits, monomial basis, not interval)
Script `scripts/cc001_cross_hessian.py` (reuses z001_parity_split; outputs `scripts/o_*.txt`).
| case (T=1 unless noted) | sector | λ | gap | H_23 | corr = H_23/√(H_22H_33) | c_{h*}(log6) |
|---|---|---|---|---|---|---|
| Λ, M=12 | even/odd | 1.3e-7 / 8.8e-6 | 1.7e-3 / 8.8e-3 | −43.4 / +18.1 | −0.96 / +0.996 | 2.5e-4 / −3.0e-3 |
| Λ, M=14 | even/odd | 9.6e-8 / 8.5e-6 | 1.0e-3 / 8.2e-5 | +13.5 / +2000 | +0.13 / +0.9999 | 2.1e-4 / −3.6e-3 |
| Λ, M=16 | even/odd | 9.6e-8 / 3.6e-8 | 3.1e-6 / 2.8e-5 | +3083 / +12723 | +0.84 / +0.9999 | 2.0e-4 / −7.5e-5 |
| Λ, T=0.92 / 1.05 (M=14), even | | 1.6e-6 / 7.1e-8 | 6e-5 / 4e-4 | +1123 / −191 | +0.997 / −0.84 | 5e-6 / 7e-4 |
| κ_2=0 (a_2) | even/odd | −0.534 / −0.516 | 0.23 / 0.18 | −0.0070 / −0.0117 | −0.79 / −0.80 | 0.015 / −0.077 |
| κ_3=0 (a_3) | even/odd | −0.631 / −0.592 | 0.51 / 0.97 | −0.011 / −0.0055 | −0.52 / −0.19 | 0.058 / −0.113 |
| Beurling δ=−0.02 | even/odd | −0.089 / −0.066 | 0.13 / 0.11 | +2.59 / +3.82 | +0.88 / +0.999 | 0.073 / −0.029 |
| Beurling δ=+0.02 | even/odd | −0.083 / −0.093 | 0.044 / 0.096 | +0.88 / +2.95 | +0.19 / +0.78 | 0.005 / −0.041 |
| Beurling δ=+0.1 | even/odd | −0.391 / −0.443 | 0.22 / 0.46 | −0.198 / +0.441 | −0.17 / +0.65 | −0.023 / −0.085 |

Readings. (a) At Λ the bottom is near-degenerate and the gap shrinks with M: the Hessian is not converged and H_23
changes sign with M, T and sector — no sign is a stable feature. (b) At the falsifiers (gap O(1)) H_23 is small and
negative; at Beurling positions it is mostly positive: sign varies with the comb, not with the ℤ coincidence.
(c) |c_{h*}(log6)| ≲ 7e-4 (even) at Λ versus 1e-2–1e-1 elsewhere, but log 6 has no weight in λ (CC1); by CC3 this is the
small edge mass of the near-kernel minimizer (edge-law family), ARGUED comb-generic, not a semiring effect.
(d) λ itself is position-fragile: δ = ±0.02 already makes λ ≈ −0.08 (first-order effect through ∇λ and the moved
positions, not through log 6).

## 5. Answer to the questions
(1) The window form contains no log-6 term; c_{h*}(log 6) cannot separate κ=(1,1,1) from κ_2=0 at first order (CC1).
Any inequality between c(log6), c(log2), c(log3) valid for all F (Bochner, CS, edge) is comb-generic.
(2) Proved: concavity/H ≼ 0, Cauchy–Schwarz on H_23, edge bound; no sign theorem for H_23 exists from these (CC2).
(3) The cross-derivative sign is not ℤ-specific (CC4; numerics show sign changes in all directions).
**NO-GO (BB5 residue, within the class "second-order κ-interaction at the minimizer"):** closed. BB5 is CLOSED as stated.

## 6. Six clauses / barrier
(1) comb-generic: fails (CC2, CC4); (2) no cone on log ζ; (3) no integrality used; (4) n/a; (5) no FE coupling;
(6) no ∂log crossing. Barrier (BARRIER_001 Thm 3): CC1/CC2 are (i) comb-generic; concavity bounds are (iii) REF-D.

## 7. Verdict
Window form PROVED; log 6 absent from λ and ∇λ PROVED; Hessian formula, H ≼ 0, CS PROVED; edge bound PROVED;
CC4 NO-GO PROVED for simple bottoms, ARGUED at Λ (near-degenerate numerically). Numerics NUMÉRICO. No sign. Row D OPEN.
Do not retry: per-prime κ-Hessian / cross-derivative sign, c_{h*}(log 6)-based separation, Bochner on {0,log2,log3,log6}.
