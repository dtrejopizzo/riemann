# NT_014 — Part (b) on (1+ϑ, 3/2] is a zero-free-strip statement: forward implication PROVED, converse ARGUED; NO-GO (inside cor:void's
# zero-information class)

Phase 189, step 14. Notation of NT_005–013. or stated. Zeros appear only to
classify part (b).

## Corpus check
Paper 46 cor:void / C_zeros class; NT_013 Prop 13.3 and §3; classical Landau/Ingham equivalence "ψ(x) − x ≪ x^{θ+ε} ⟺ no zeros in Re s > θ"
(CITED; corpus mentions under "zero-free region" in phase 167/168 memos). New: the two directions for the height-flow symbol (Thm 14.1, Prop 14.2).

## 1. Forward (PROVED; explicit formula CITED)
**Thm 14.1.** If ζ(s) ≠ 0 for Re s > ½ + ϑ (0 ≤ ϑ < ½), then for every ε > 0, |Ξ(u)| ≪_ε e^{(ϑ+ε)|u|}, hence K_σ ∈ ℓ¹ for σ > 1 + ϑ + ε and (b) holds on
(1 + ϑ, 3/2].
*Proof.* Smoothed explicit formula for Ξ(u) = Σ v_nc₀(u − log n) (c₀ ∈ C², compact support; main term killed by Tate): Ξ(u) = −Σ_ρ ĉ₀-weighted
e^{(ρ−½)u}·(…) + O(1), absolutely convergent since ĉ₀ = F̂₀² = O(τ^{−4}); each term ≪ e^{(Re ρ − ½)u}. Then NT_003 Prop 3.1. ∎

## 2. Converse (ARGUED)
**Prop 14.2.** If (b) holds for every σ in an interval (σ′, 3/2) and the continuous versions vary continuously in σ there, then ζ has no zero ρ
with ½ < Re ρ − … precisely with Re ρ ∈ (σ′ − ½, 1) whose ordinate γ is not one of the exceptional points where Im[F̂₀(z_ρ)²] = 0.
*Argument.* Under the hypotheses Φ_σ∘ι is continuous in τ₀ and real-analytic in σ on the interval, hence equals the continuation Φ^{curve}_σ
(NT_005 Thm 5.2 identity on σ > 3/2, identity theorem). Φ^{curve}_σ = (ζ(2σ−1)/ζ(2σ))Re[F̂₀(z)²M(w)] + Re ℛ_σ with ℛ_σ analytic (Prop 5.3).
A zero ρ = β + iγ with β = σ − ½ ∈ (½, 1) gives M(w) a simple pole at w = ρ (τ₀ = γ); F̂₀(z)² ≠ 0 there (its zeros have |Im z| = |b| > ½ or are ±i/2,
while Im z = σ − 1 ∈ (0, ½)); so Re[F̂₀²M] ~ Im(F̂₀(z_ρ)²)/(τ₀ − γ) is unbounded unless Im F̂₀(z_ρ)² = 0. Continuity in τ₀ fails. The
reflected pole (1 − w = ρ) sits at Re w = 1 − β < ½, outside the range. ∎ (ARGUED: the uniformity needed for the identity-theorem step and the
exceptional set are not written out.)
**Conclusion.** Up to ε-losses and an exceptional set, **(b) on (1 + ϑ, 3/2] ⟺ zero-free half-plane Re s > ½ + ϑ**. Part (b) is zero-location
information; any route to it lies in cor:void's zero-information class. **NO-GO (recorded): part (b) has no zero-free mechanism in the height flow.**
(The NT_013 partial-curve analysis is the same fact seen through prime sums: Landau/Ingham.)

## 3. Review
- Forward: standard; the smoothing makes the zero sum absolutely convergent ✓.
- Converse: ARGUED; I do not claim the exceptional set is empty. The NO-GO only needs that every route to (b) yields (generic) zero-free
  information, which the argument establishes at ARGUED level.
- Nothing here combines (b) with D; no statement "D ⇒ …" about zeros is made. **No sign contact.**
