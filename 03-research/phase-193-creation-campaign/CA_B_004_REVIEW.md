# CA_B_004 — Review
Checked vs P47 prop:boundary, rem:fe, prop:finite(iv), lem:shape-ident; CA_B_001 review.

## Verdict
**EXCLUDED (B″: identity comb-generic, O1–O7 survive — memo agrees). Prop 1 CONFIRMED (restatement). One MAJOR FIX: the pole of g_X at s=1 makes J(σ) infinite at σ=1, so "J ∈ C^∞(½,2)" and the convexity chain (3.3) on [½,2] are false as written.**

## 1. Claims
| claim | check | label |
|---|---|---|
| Prop 1 (1.1) | ∂_σ log|γ|² = m at σ=½; ∂_σ log|Z_{<X,a}|² = −2Re P_{a,X} ✓ | CONFIRMED (prop:boundary + rem:fe rewritten) |
| (3.1) J″ = 4∫ω|g′|² − ∫ω″|g|² | Δ|g|² = 4|g′|² for holomorphic g; two integrations by parts in τ ✓ — valid on any σ-interval avoiding 1 | CONFIRMED on [½,1) and (1,2] |
| table: "g_X polynomially bounded on σ ≥ ½ except the pole; J ∈ C^∞(½,2)" | **false**: g_X(σ+iτ) ~ (s−1)^{−1}/Z_{<X}(1) near s=1, so ∫ω|g_X(σ+iτ)|²dτ ≍ π ω(0)|Z_{<X}(1)|^{−2}/|σ−1| → ∞ as σ→1. J is not defined at σ=1; J′ ~ ∓c/(σ−1)² is not integrable, so no "principal value plus residue" repairs (3.2) | FIX (major) |
| (3.3) "I_ζζ ≥ 0 ⟸ J convex on [½,2], J′(2) ≤ 0" | Even on [½,1): J″ ≥ 0 gives J′(½) ≤ J′(σ) for σ<1, and J′(σ) → +∞ as σ→1⁻ — the inequality points the wrong way; one needs some σ∈(½,1) with J′(σ) ≤ 0, i.e. control in the strip ½<σ<1, where |g_X| sees the zeros (R)(4). The (1,2] branch is disconnected from σ=½ | **NO-GO for the convexity route (PROVED from the pole asymptotics)** |
| J′(2) crude bound | b ≥ 0 but ω̂ has no sign; magnitude O(X^{−1}log X)‖ω̂‖_∞ ✓ | CONFIRMED |
| "(W_σ) false comb-generically" | sketch only | ARGUED |

## 2. Modifications
Identity holds for every comb with g_a := ζ/Z_{<X,a} (memo §2): O1–O7, O15 survive ⇒ **EXCLUDED** (lem:shape-ident). O8 quartets keep ζ and the comb ⇒ survive. The only ζ-specific datum (Euler tail at σ=2) is cut off from σ=½ by the pole.

## 3. (R): (4) NOT met for any use of the strip ½<σ<1 (now forced, §1); (5),(6),(7) not met (boundary O(X^{−1})); (11) not met.
## 4. REF-D: no sign produced; (W_σ) on [½,1) restricted to the matched piece would be a pointwise-in-σ positivity of the same type as the target piece I_ζζ — REF-D-adjacent, not claimed.
## 5. Retry: NT_013/014 obstruction escaped in the sense stated (no ζ′/ζ transported), but replaced by the pole barrier at σ=1 plus zero geometry in ½<σ<1. Endorse: "transport uses same ζ on both sides" → NO; add "J-transport across σ=1" → NO (pole).
