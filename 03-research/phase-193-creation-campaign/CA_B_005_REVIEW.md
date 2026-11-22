# CA_B_005 — Review
Checked vs P46 prop:wit-sens (L. 7083–7099), rem:wit-sens, cor:void, lem:degen, prob:region(6),(11), lem:shape-est(iii).

## Verdict
**Prop 2: CONFIRMED after FIX — but it is a direct corollary of P46 prop:wit-sens, NOT a new structural clause. §3's conclusion ("a sign argument using Δ≡0 must be valid on the ball") is a NON-SEQUITUR and the YES→NO move is NOT endorsed as stated. §4 ARGUED, accepted with scope.**

## 1. Prop 2, checked rigorously
(a) **Constant.** The memo writes |b_T(a)−b_T(Λ)| ≤ κ_T‖a−Λ‖_∞ "with κ_T the norm of the linear part (P46 notation)". In P46, κ_T := Σ_n v_n c_h(log n) for a real unit minimizer h (prop:wit-sens) — a *directional derivative* along v, not an operator norm; it can be 0 or negative (κ_T ≠ 0 is an open hypothesis, lem:shape-est(iii), A′). With κ_T as defined the inequality is false in general (κ_T = 0 would give b_T constant). **FIX:** P46 prop:wit-sens already proves |λ_A(T;v) − λ_A(T;v′)| ≤ Σ_n|v_n − v′_n| (ℓ¹ in the weights v_n = 2a(n)n^{−½}, since |c_F| ≤ ‖F‖²). Correct radius: the ℓ¹-ball Σ_n 2n^{−½}|a(n) − Λ(n)| < λ_A(T); in ℓ^∞ of a, radius λ_A(T)/(2Σ_{n<e^{2T}}n^{−½}) ≥ λ_A(T)/(4e^T). "Radius λ_A/κ_T" is wrong; λ_A/κ_T is the *upper* scale (beyond it (1+ε)Λ fails when κ_T>0), not a ball of positivity.
(b) **Strictness.** Needs λ_A(T) > 0 strictly; holds where P46 certifies a strictly positive bottom (e.g. Theorem C at ½log3, the ½log5 certificates). At windows with T ≤ ½log2 the δ₂ perturbation is invisible (2 ∉ N_T). FIX: state "T ∈ (½log2, ½log5] at certified windows".
(c) **Δ_{Λ+cδ₂}.** log Φ_a = log Φ_Λ + c2^{−s}/log 2; derivative −c2^{−s}; 2Re at ½+iτ: −2c·2^{−½}cos(τ log 2) ≢ 0 ✓.
(d) **Consistency with O2.** thm:shape(A) lists Λ+cδ₂ "for all c>0" as a falsifier — at the windows of its lemma (large T depending on c), not at fixed T. No contradiction ✓.
Conclusion: Prop 2 (corrected) = prop:wit-sens + certified λ_A>0 + one computation of Δ. **Label PROVED; novelty: none beyond the remark "(Inv) is false".** It is already the content of rem:wit-sens / (R)(6) ("sharp at the scale λ_A/κ_T") read in the other direction.

## 2. §3 — why the structural conclusion fails
"A sign argument whose load-bearing input is Δ ≡ 0 must also be valid on the ball where Δ ≢ 0": false. A valid proof of P(a) ⇒ b_T(a) ≥ 0 makes no claim about combs without P; positivity being open at a point does not oblige a proof to cover the neighbourhood. lem:transfer excludes a class only when a *modified object keeps the property set and has negative bottom*; on the ball the bottom is positive, so nothing is excluded. (The certified proofs at T ≤ ½log5 use the exact vector — a "thin" property — and are valid.) The correct, already-known constraint is the converse: a property **continuous in the weights** must be sharp at scale λ_A/κ_T (rem:wit-sens, (R)(6)); exact identities are excluded by (B″) only when comb-generic, and Δ≡0 is not comb-generic. Self-matching is excluded for a different reason: O8 (CA_B_003 review).
What does survive, uniformly in T: by cor:margin1 the ball radius ≤ 4·10⁹Te^{−15.449T} → 0, so any "openness" argument gives nothing uniform — again (R)(6), already in the paper.

## 3. Recommendation on the shape theorem
**Do not add a clause.** At most a one-line remark after prop:wit-sens: "positivity is open in the weights (ℓ¹-radius λ_A); hence no rigidity statement 'defect ⇒ negative bottom' holds at a fixed certified window" — PROVED, trivial corollary.

## 4. Modifications / (R) / REF-D / retry
Not a candidate object (no sign mechanism). §4 matching distances: bounded 𝔇 ⇒ (R)(5) ✓; unbounded 𝔇 ⇒ identification (O1/O7 undefined, W3′) ✓ — ARGUED, accepted. Retry: G4F-R162_2801 (quantitative Hamburger rigidity, DEAD) — §4 is its re-derivation.
Endorsed moves: "(Inv) / quantitative defect⇒negative bottom at fixed T" → NO (PROVED). NOT endorsed: "self-matching as sign carrier → NO because of openness" (correct verdict NO, wrong reason; the reason is O8).
