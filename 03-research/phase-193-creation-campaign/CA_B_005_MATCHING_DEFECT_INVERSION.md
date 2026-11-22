# CA_B_005 — Strongest form of self-matching: can "matching defect ⇒ negative bottom" be inverted? (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed.**

## 0. Corpus check
CA_B_003 (Theorem 1: Δ_a ≡ 0 ⟺ FE; Cor via Hamburger, CONDITIONAL); P46 prop:finite(iv) (the window matrix is affine in the weights),
(R)(6) (sensitivity at scale λ_A/κ_T), lem:shape-margin; index W3′, N_009/010, G4F-R162_2801 (quantitative Hamburger rigidity, DEAD).

## 1. The statement one would want
(Inv) For combs a in a class 𝒞 ∋ Λ: bottom_T(a) ≥ 0 ⟹ Δ_a ≡ 0, i.e. (contrapositive) any matching defect forces a negative window bottom.
Inverted, together with Δ_Λ ≡ 0, it would not give the sign (wrong direction); what is needed is (Inv*) Δ_a ≡ 0 ⟹ bottom_T(a) ≥ 0. The
coordinator's question is whether a quantitative (Inv) — "defect ≥ δ ⇒ bottom ≤ −f(δ)" — could be inverted into (Inv*) by a continuity/rigidity
argument (bottom ≥ −f(dist(a,{Δ=0})) and equality structure at Δ = 0).

## 2. Proposition 2 (positivity is open, matching is thin; PROVED at certified windows)
Fix T with λ_A(T) > 0 (PROVED in P46 for T ≤ ½log5 by the certificates). The bottom b_T(a) is the least eigenvalue of a finite matrix affine
in (a(n))_{n<e^{2T}} (prop:finite(iv)), hence |b_T(a) − b_T(Λ)| ≤ κ_T‖a − Λ‖_{ℓ^∞} with κ_T the norm of the linear part (P46 notation).
So every comb with ‖a − Λ‖ < λ_A(T)/κ_T has b_T(a) > 0. Among them are a = Λ + cδ₂, 0 < c < λ_A/κ_T, for which
Φ_a = γζ·exp(c2^{−s}/log 2) and Δ_a(τ) = −2c·2^{−½}cos(τ log 2) ≢ 0. Hence (Inv) is **false** at every window with λ_A > 0, and no
quantitative form f(δ) with f(δ) > 0 for δ > 0 holds in the ℓ^∞-small regime. ∎
Under the premise that positivity holds at every T, the same holds at every T (CONDITIONAL on that premise, used only to state
scope, not as an input to a sign).

## 3. Consequence for self-matching as a mechanism (PROVED, from Prop 2)
The set {Δ_a ≡ 0} is (Hamburger, CONDITIONAL) the single point Λ, while {b_T ≥ 0} contains an ℓ^∞-ball of radius λ_A/κ_T around Λ. A sign
argument whose load-bearing input is Δ ≡ 0 must therefore also be valid on the ball where Δ ≢ 0, i.e. it must use Δ ≡ 0 only through a
quantity that is **continuous in a at scale λ_A/κ_T** — exactly (R)(6). An exact identity (Δ ≡ 0) cannot be that quantity by itself:
any proof "Δ_a ≡ 0 ⇒ b_T(a) ≥ 0" proves nothing about the ball and is a proof only if it also controls b_T on combs that it does not
characterize. So self-matching can enter only as bookkeeping beside a continuous quantity — the same conclusion as (R)(11) for exact identities.
**YES→NO:** "self-matching (Δ ≡ 0) as the sign-carrying property" → NO (PROVED at certified windows).

## 4. What would survive: a matching *distance*
The surviving shape: a functional 𝔇_T(a) ≥ 0, continuous at scale λ_A/κ_T, with 𝔇_T(Λ) = 0 forced by Δ_Λ ≡ 0, and an inequality
b_T(a) ≥ c_T − 𝔇_T(a). For this to be ζ-specific, c_T must be produced from Δ_Λ ≡ 0 jointly with Euler (Hamburger is the uniqueness, not the
inequality). Natural 𝔇: ∫F̂₀²|Δ_a|²dτ restricted to the window — but Δ_a on the line is a finite trigonometric polynomial in the modified
weights plus the γ-term, so 𝔇 is a bounded quadratic functional of the weights: excluded by (R)(5) ("not a bounded functional of the
weights"). An unbounded 𝔇 must look at Φ_a off the line (where continuation of Z_a is needed — undefined for a_P, Beurling): for those
combs 𝔇 = ∞ and the inequality is empty, i.e. it is identification again. NO-GO (ARGUED) for matching distances of either type.

## 5. Self-review
- Prop 2 uses only Lipschitz continuity of the least eigenvalue of a symmetric matrix in an affine parameter (Weyl) and λ_A > 0 at certified
  windows: PROVED. The formula for Δ_{Λ+cδ₂}: log Φ_a = log Φ_Λ + c2^{−s}/log 2, Re of the derivative at ½+iτ is −c Re 2^{−½−iτ} → as stated ✓.
- §4 is ARGUED (two exhaustive-looking cases, not a theorem over all 𝔇).
- No sign contact; no negative value.
