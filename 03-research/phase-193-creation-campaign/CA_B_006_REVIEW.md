# CA_B_006 — Review
7083), def:shape-mods (l. 8346–8349: "a bounded perturbation q_T ↦ q_T + 𝔟 with ‖𝔟‖ ≤ λ_A" is already listed as a structural modification), prop:finite(ii), (R)(5),(6).

## Verdict
**Lemma B (i)–(iii) CONFIRMED PROVED — but already in P47 (prop:wit-sens ℓ¹ bound; l. 8348 bounded perturbation). (iv) "empty interior / not necessary" PROVED, trivial; its methodological reading is NOT endorsed (same non-sequitur as CA_B_005 §3). Scale statement: FIX (inequality reversed). §3: (R)(4) point ACCEPTED; convexity on [½,2] repeats the pole error (FIX). §6 superseded by CA_B_007.**

## 1. Claims
| claim | check | label |
|---|---|---|
| (i) L_T ≤ |N_T| | |c_F| ≤ ‖F‖² = 1 ✓ | CONFIRMED |
| (ii) concave, L_T-Lipschitz in ℓ^∞ | inf of affine; equivalent to prop:wit-sens (ℓ¹ in v) ✓ | CONFIRMED (= P47) |
| (iii) ball in 𝒱_T | ✓ | CONFIRMED |
| (iv) methodological ("must also establish λ ≥ 0 on B_T") | **non-sequitur**: a deduction "P ⇒ λ ≥ 0" makes no claim off P; the target's own certified proofs at T ≤ ½log5 use the exact vector. lem:transfer excludes a class only via a modified object *with P and negative bottom*. | NOT endorsed |
| Scale "radius λ_A/L_T ≤ 4·10⁹Te^{−17.449T}" | needs a LOWER bound L_T ≳ e^{2T}; only the upper bound L_T ≤ |N_T| is proved, which gives radius ≥ λ_A e^{−2T}. FIX: state "radius = λ_A/L_T ≤ λ_A ≤ 4·10⁹Te^{−15.449T}" (since L_T ≥ 1 trivially? only if some n gives |c_F(log n)| near 1 — take F concentrated so c_F(log 2) ≈ ... not automatic; safest: radius ≤ λ_A/L_T with L_T unbounded below unknown) | FIX |
| §2(a) "bounded functional" | P47's notion (def:shape-class: norm, moment, determinant, …, coherence functionals; prop:wit-sens) — consistent with the memo's reading ✓ | ACCEPTED |
| §2(c) inner set must be defined without λ_A | ✓ — correct and useful sharpening | ARGUED, endorsed |
| §3 (R)(4) for J_X: J is a quadratic form in boundary values of (s−1)g_X, no log | ✓ (Phragmén–Lindelöf representation, CITED) | ACCEPTED |
| §3 "(W_X) J_X convex on [½,2]" | J_X(σ) ≍ c/|σ−1| as σ→1: not finite at 1 (CA_B_004 review). Removing the pole by (s−1) changes J. | FIX (repeat) |
| J″ coefficient form for σ>1 | (log mn)² split ✓; ω̂ p.d. since ω ≥ 0 ✓ | CONFIRMED |

## 2. Modifications / (R) / REF-D / retry
Not a candidate object. Inner-set formulation: a set defined via λ_A is REF-D (memo ✓). Retry: G4F-R162_2801, P47 l. 8348. Endorsed: "Euler-tail class membership as sign carrier" → NO — but for the right reason: (W_X) controls only I_ζζ, not the window bottom; membership being a point property is not itself an exclusion.
