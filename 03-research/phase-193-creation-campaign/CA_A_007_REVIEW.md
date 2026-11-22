# CA_A_007 — Review

## Verdict
**§1 withdrawal ENDORSED (retry of N_012/W5/flowdet/W-cont). §2 boundary triples: CONFIRMED as a reduction to thm:parityschur/prop:polarcap (coordinates, (B″)). §3 Theorem 2 CONFIRMED PROVED — RP fails for every atomic comb; comb-generic, carries no sign; EXCLUDED as a mechanism. §6 index seed: pre-flagged.**

## 1. Claims
| claim | check | label |
|---|---|---|
| Lemma 1: 𝔞(f+Θf) = 2𝔞(f) + 2H_K(f) | Toeplitz form; cross terms ∫∫f(t)f(−s)K(t−s) = H_K(f), twice ✓. Caveat: f+Θf must lie in P_T for 𝔞_T to be the window form — the identity is for the Toeplitz form on L²(I_T) | CONFIRMED (Toeplitz level) |
| Thm 2 | f_ε symmetric about a = ½log n₀ ⇒ ∫f_ε(t)f_ε(log n₀ − t)dt = ‖f_ε‖² = 1 ✓; other atoms excluded for small ε ✓; archimedean/polar kernels continuous away from 0 (t+s ≈ 2a > 0) ✓ ⇒ H_K(f_ε) → −v_{n₀}/2 < 0 | CONFIRMED PROVED |
| Prop 1 (boundary triple ⇔ parity Schur) | Kreĭn formula (CITED) + thm:parityschur (internal) ✓; deficiency 2 = Tate moments ✓ | CONFIRMED as reduction |
| §4 one-liners | ARGUED, consistent with prop:shape-twist and (R)(4) | ACCEPTED |

## 2. Modifications: Thm 2 holds for every comb with an atom (O1–O8, O11, O15 survive) ⇒ the RP statement is comb-generic; boundary-triple Weyl function exists for every comb ⇒ (B″). EXCLUDED.
## 3. (R): no item met at a sign step. 4. REF-D: primitive-adapted triple = λ_A (REF-D, memo ✓). 5. Retry: NG-E1, phase-6-osterwalder-schrader-reflection G_p(π/log p) < 0 analogue (memo ✓), KEP 394/640, index §G.
## 6. §6 seed (index/spectral flow on the open ball) — pre-flag
Local constancy on the ball is automatic for any integer invariant, so "openness satisfied" adds nothing. An index that detects λ_A ≥ 0 must be the count n₋ of negative eigenvalues on P_T or a function of it; Paper 46 Theorem P (n₋ ≤ 5/7/8) and the inertia NO-GO (n₋ = ∞ in the full window for T > ½log2) are on record. Spectral flow along T between two windows equals the change of n₋ — so "propagate from a degenerate endpoint" is the first-contact problem (lem:firstcontact / Gate 1) in index language: REF-D unless the loop is closed and its flow computed from Euler × FE data. Also O13 (bounded windows) applies to any argument that stops at a finite T. Name the loop first.
Endorsed: "RP (per place or cross-place) carries the window sign" → NO (PROVED); index §G boundary triples → covered as coordinates.
