# REVIEW_STATE — review notes, phase 205

## Audits
- AUDIT_205_SKELETON_001 (SKELETON_001): P3 correct but rewrite of lem:polarelim (canonical form
  M = 𝔢 − 2(ℓ_c² − ℓ_s²)); Φ_E = −𝓕_T = −R_Λ; (6.1) PROVED given (1.4), artifact slack; L205.★ REF-D (compression of
  prop:sharp(ii) to E_N^ev ∩ P_T), withdrawn; P1.c the only OPEN tool with content.

## Fixed facts (not to be re-audited)
- ker ℓ ∩ L²_ev = P_T^ev. In P_T: 𝔞_T = 𝔞^♯ − 𝓕_T (prop:sharp(ii)); Z_T = 𝔞^♯ − 𝓕_T on all of L²_ev (from (1.4)+(R1)).
- E_G = 𝔢 + (½sinh T − 1)ℓ² (even); = 𝔢 + (½sinh T + 1)ℓ_s² (odd).
- β_{½log15} = 1.903696; t₀′ = zero of m^♯ = 6.12587 (NUMERICAL); t₀ = 6.28984.
- c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²)), ‖χ_ev‖² = T + sinh T.

## Blacklist of rewrites (detect in upcoming rounds)
- pole + Chebyshev main term = kernel e^{−|s|/2} (lem:polarelim, B_001 L3.1, E_001 E.4, MORI15).
- Chebyshev remainder 𝓕_T / R_Λ / dR_Λ (prop:sharp, B_001, V_001 V.2.1).
- any "slack" that is (β_T − 2)ℓ²: it vanishes on P_T.

## Pending for round 2
- Verify that the architect withdraws L205.★, adopts (R1), corrects typos, prioritizes P1.c.
- Review P2a G_kl (k≠l) against independent quadrature if it enters P46.
