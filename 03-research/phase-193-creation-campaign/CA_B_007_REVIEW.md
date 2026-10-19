# CA_B_007 — Review
8331–8345 (O-list), lem:shape-quartet (l. 8429), lem:shape-ft (l. 8435), prop:quartetmodel (l. 7964), prop:finite(ii), thm:ceiling, prop:summable, cor:shape(a), lem:compact.

## Verdict
**Label correction CONFIRMED (P47: O7 = quartets, O8 = f_t). Prop 1 CONFIRMED (O7 PROVED from lem:shape-quartet verbatim; O8 ARGUED). Convex decomposition EXCLUDED (REF-D / class (D)), reductions checked. §3 concavity gap Γ: Prop 2 CONFIRMED; Γ as sign source = OPEN, pre-flagged REF-D — NOT an admissible candidate yet.**

## 1. Claims
| claim | check | label |
|---|---|---|
| Prop 1(a) O7 moves the point ν_ζ ↦ ν_ζ − kβ_z, set fixed | lem:shape-quartet: "keep the comb exactly…arithmetic side differs only by the a.c. part −kβ_z" ✓ | CONFIRMED PROVED |
| Prop 1(b) O8 point move along atoms off log ℕ | lem:shape-ft: frequencies m/√M not integers ✓; weights not reproduced | ARGUED (as labelled) |
| TV-ball of radius λ_A | |c_F| ≤ 1 ✓; = P47 l. 8348 in measure form | CONFIRMED (not new) |
| N_012 row: two-point decomposition forces t′ = 1/(1−θ) > 1 | ν₂ = ρ + (ν_ζ−ρ)/(1−θ) ✓ | CONFIRMED |
| ceiling row: Σθ_i r_i = 1, r_i ≤ 1 ⇒ r_i = 1 | ✓ (for nonnegative atomic pieces on log ℕ positive at all T) | CONFIRMED |
| class (D) row: concavity chain is linear in ν | ✓ cor:shape(a) | CONFIRMED |
| Prop 2: Γ = 0 ⟺ common minimizer | inf(A+B) = inf A + inf B iff a common minimizer exists, given attainment (lem:compact on P_T) ✓ | CONFIRMED PROVED |
| Γ ≥ θ₁θ₂·(misalignment quadratic) | needs spectral gaps | ARGUED |

## 2. Γ — pre-screen (not yet built)
- (B″): b(Σθν_i) = Σθb(ν_i) + Γ is an identity valid for every measure; any sign must come from a lower bound on Γ.
- REF-D test: Γ = b(ν_ζ) − Σθb(ν_i). With ν₁ = ρ_κ, ν₂ = λ_{t′} (t′>1, beyond Λ, where b(λ_{t′}) may be negative by thm:shape O4 for large t′), a lower bound Γ ≥ −Σθb(ν_i) is literally the target. It escapes only if the misalignment bound is computed from the two minimizers alone and those minimizers are themselves computable without b(ν_ζ). But the minimizer of λ_{t′} is as hard as the target's minimizer (same comb up to the factor t′ and the ρ-shift).
- O-list: O2/O4^ε move ν₂ along the line; O7 adds −kβ_z/(1−θ) to ν₂; a misalignment bound valid for any (ν₁, ν₂) pair is comb-generic ⇒ excluded unless it reads Λ's integrality in ν₂'s minimizer. Required next: name the property of ν₂'s minimizer that O7 (large k) and O2 destroy.
- (R)(6): Γ must be sensitive at scale λ_A; a second-order misalignment bound with spectral gap is O(gap·angle²) — the gap at the target is ≤ the margin ⇒ precision problem as in lem:shape-est.
Status: **OPEN — pre-flag REF-D (high)**.

## 3. Retry: N_012, thm:ceiling, prop:summable, thm:Z — all recorded; Γ itself not on record (closest: R162 "two sectors", W-coh). Endorsed move: "explicit convex inner set as sign carrier" → NO.
