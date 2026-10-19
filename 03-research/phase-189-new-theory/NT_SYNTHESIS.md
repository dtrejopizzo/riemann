# NT_SYNTHESIS — Phase 189: the two-metric group and the height flow

**Row D: OPEN. No certified negative
value; no sign contact at any step.** Referee reports: NT_001_004_REVIEW, NT_005_007_REVIEW, NT_008_010_REVIEW
(all fixes applied as dated errata). NT_011–014 not yet refereed.

## 1. Definitions
- Two-metric group G = ℚ_{>0}: ℓ(r) = |log r|, h(r) = log(ab) (r = a/b reduced); ℓ ≤ h with equality exactly on ℕ ∪ ℕ^{−1}; h − ℓ = 2 log den.
- Weil kernel K(r) = B_{F₀}(log r); D ⟺ K positive definite on G.
- Height flow K_σ = K·H^{−σ} = (e^{−σℓ}) × (denominator damping den^{−2σ}); D(σ) = PD of K_σ; positivity depth σ*(a).
- Bohr symbol Φ_σ on 𝕋^∞; damping kernel |L(σ,χ)|²/ζ(2σ); curve ι(τ) (characters m^{−iτ}).

## 2. PROVED (referee-confirmed unless noted)
1. h is CND; the flow preserves positivity; every finite-section bottom is nondecreasing in σ; D = ∩_{σ>0}D(σ); falsifiers have σ* > 0 (NT_001).
2. Euler-vector criterion (σ > 3/2); Harnack contraction with floor ζ(2δ)/ζ(δ)²; base theorem D(σ) for σ ≥ 3/2 + O(T₀/log(1/T₀)) (class-level) (NT_002).
3. Phase lines 3/2 (Chebyshev/absolute), 1 (ℓ²), ½ (Kakutani, ℓ²-failure); Steinhaus chaos formulation for σ > 1; amplification tolerance > 0
   above 1 given a margin (NT_003).
4. Centre collapse: on Euler tests at exponent ½, (Λχ)*1 replaces Λ exactly; ζ-tests positive (cheap); NO-GO as sign carrier (NT_004).
5. Curve reduction (σ > 3/2) and exact curve formula: coprime counting ζ(2σ−1)/ζ(2σ) × Re[F̂₀²(m + 2ζ′/ζ(w))] + discreteness remainder (NT_005).
6. **FE inside the flow (first Λ-specific results):** main factor = F̂₀²[ζ′/ζ(w) − ζ′/ζ(1−w)], odd under σ ↦ 2−σ; ℓ² line σ = 1 is the
   fixed line (explains the corpus's exact criticality); the curve symbol is regular at σ = 1 for Λ and has a pole for every finite
   modification, truncation, and (referee) Epstein/DH-type series; every truncation fails D(σ) as σ ↓ 1 (NT_006, Cor 6.5).
7. Value at σ = 1: V = −(F̂₀²(log|ζ(½+iτ)|)′)′/ζ(2) + Re ℛ₁; ℛ₁ = a₀ − 2Re(−ζ′/ζ)(3/2+iτ₀) + O(√T₀ log) (integrality at sparse scales)
   (NT_007, NT_008).
8. Weak (𝒱) at width ≍ √(T₀ log(1/T₀)) (unconditional; cheap mechanism) (NT_009, NT_012; NT_012 not yet refereed).
9. σ-derivative at σ = 1 (NT_010); D ⟹ strict (𝒱) (CONDITIONAL).

## 3. Classifications (NO-GO)
- Pointwise (𝒱) / pointwise bounds on ℓ″: the positive part of ℓ″ comes only from zeros off the line; model ζ̃ = ζ·R ⇒ NO-GO for
  FE + line identities + mean values (NT_011; referee concurs: zero geometry, inside cor:void's zero-information class).
- Part (b) (off-curve continuity, 1 < σ ≤ 3/2): ⟺ zero-free half-plane Re s > ½ + ϑ on (1+ϑ, 3/2] (forward PROVED, converse ARGUED) ⇒ NO-GO
  as a zero-free mechanism (NT_013, NT_014); absolute methods with sub-power PNT errors excluded (NT_013).
- Centre/Euler-direction families: cheap or exactly critical (NT_003 Thm 3.6 CONDITIONAL, NT_004).

## 4. Where the theory stands
All PROVED positivity (base theorem, ζ-tests, weak (𝒱)) is archimedean dominance; all Λ-specific content (NT_006–008) is structural, not
sign. Both open parts of P189.1 — pointwise (𝒱) and (b) — reduce to zero information, **except possibly through the Euler product of ζ used
on the critical line itself**, which the model ζ̃ (no Euler product) does not reproduce.

## 5. The remaining door (next target, stated precisely)
**Target E (Euler-on-the-line bound).** For the fixed narrow profile and |τ₀| ≤ C/T₀, prove
  (F̂₀²ℓ′)′(τ₀) ≤ ζ(2)·Re ℛ₁(τ₀),  ℓ(τ) = log|ζ(½+iτ)|,
by an argument that uses the Euler product of ζ on the line non-trivially — i.e. an input that FAILS for ζ̃ = ζ·R (NT_011) and for
Epstein/DH-type series — e.g. via the curve formula at σ slightly above 1 where ζ′/ζ(w) = −ΣΛ(n)n^{−w} is a convergent Euler-product
object for Re w > 1, transported to σ = 1 through the FE-odd factor (NT_006) together with the explicit ℛ_σ (NT_008). Any such argument must
state which property of the Euler product it uses that ζ̃ lacks; otherwise it falls under NT_011.
