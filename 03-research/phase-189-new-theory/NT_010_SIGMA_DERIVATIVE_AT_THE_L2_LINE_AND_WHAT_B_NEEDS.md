# NT_010 — The σ-derivative of the curve symbol at σ = 1: V₁ = −(2/ζ(2))(γ − ζ′/ζ(2))·X + Re ∂_σℛ|₁; strict (𝒱) under D; positivity does
# not propagate upward for free; what the off-curve regularity (b) needs

Phase 189, construction step 10. Notation of NT_005–009. Labels as before.

## Corpus check
grep "derivative in σ", "∂_σ", "first contact" + "transversal" (NT_001 Lemma 1.7; N_012 Euler–Lagrange at t*, transversal crossing),
"γ − ζ′/ζ(2)", "Laurent" + "ζ(2σ−1)": no memo expands the coprime-counting pole against an FE-odd factor. **New:** Thm 10.1, Cor 10.2,
Prop 10.3, Prop 10.4.

## 1. Expansion at σ = 1 (PROVED; one ARGUED bound)
Write ε = σ − 1, X(τ₀) = (F̂₀²ℓ′)′(τ₀), G(σ, τ₀) the FE-odd main factor (NT_006 Thm 6.1).
**Thm 10.1.** For τ₀ with ζ(½ + iτ₀) ≠ 0:
  Φ^{curve}_{1+ε}(τ₀) = V(τ₀) + εV₁(τ₀) + O_{τ₀}(ε²),
  V = Re ℛ₁ − X/ζ(2),   V₁ = −(2/ζ(2))(γ − (ζ′/ζ)(2))·X + Re ∂_σℛ_σ|_{σ=1},
with γ − ζ′/ζ(2) = 0.5772… + 0.5699… = 1.1472… > 0 (CITED values).
*Proof.* G is odd about σ = 1 (NT_006), so G(1 + ε) = G′ε + O(ε³), G′ = ∂_σG(1) = −2X (NT_007 Thm 7.1). ζ(1 + 2ε) = 1/(2ε) + γ + O(ε) and
1/ζ(2 + 2ε) = 1/ζ(2) − 2ε ζ′(2)/ζ(2)² + O(ε²). Multiply: (ζ(2σ−1)/ζ(2σ))G = G′/(2ζ(2)) + ε(G′/ζ(2))(γ − ζ′/ζ(2)) + O(ε²). ℛ_σ is
real-analytic at σ = 1 (NT_005 Prop 5.3). ∎ (The vanishing of G″(1) by oddness is what makes the O(ε) coefficient this clean.)
**Bound on ∂_σℛ (ARGUED).** On |τ₀| ≤ C/T₀: Re ∂_σℛ|₁ = 2Re(ζ′/ζ)′(3/2 + iτ₀) + O(C²√T₀ log(1/T₀)), so |Re ∂_σℛ|₁| ≤ 2κ + o(1),
κ := Σ_nΛ(n)(log n)n^{−3/2} < ∞. (Differentiate NT_008's expansion; the error derivative by Cauchy's estimate on a complex σ-disc of radius ¼,
assuming NT_008's bound holds for complex σ there — same proof, not rewritten: ARGUED.)

## 2. Consequences
**Cor 10.2 (D ⟹ strict (𝒱) on the spectral range; PROVED modulo the ARGUED bound).** If D holds, then for T₀ small and |τ₀| ≤ C/T₀
(ζ(½+iτ₀) ≠ 0): V(τ₀) > 0.
*Proof.* Under D, Φ_σ∘ι = Φ^{curve}_σ ≥ c_σa₀ ≥ 0 for σ > 1 (NT_005 Prop 5.5 + NT_002 Cor 2.8). If V(τ₀) = 0 then X = ζ(2)Re ℛ₁ and
V₁ = −2(γ − ζ′/ζ(2))Re ℛ₁ + Re ∂_σℛ ≤ −2.29(a₀ − 3.1) + 2κ + o(1) < 0 for a₀ large (Lemma 2.6), so Φ_{1+ε}(ι(τ₀)) < 0 for small ε > 0. ∎
**Prop 10.3 (positivity does not propagate upward for free).** On the spectral range, to first order in ε > 0, curve positivity at σ = 1 + ε reads
  X(τ₀)·(1 + 2(γ − ζ′/ζ(2))ε) ≤ ζ(2)(Re ℛ₁ + ε Re ∂_σℛ|₁),
which is STRONGER than (𝒱) wherever X > ζ(2)Re∂_σℛ/(2(γ − ζ′/ζ(2))) = O(1). So the curve symbol DEcreases in σ exactly where the
log|ζ|-convexity term X is large; the σ-direction brings no new sign, and the binding constraint of (a) in the band 1 < σ < σ₁(F₀) is the
same single function X versus the arithmetic remainder. ∎ (Thm 10.1.)
**Reading.** The FE makes σ = 1 the "softest" point of the curve problem (the main factor vanishes there); moving up, the coprime-counting
factor ζ(2σ−1)/ζ(2σ) loses its pole and the FE-odd factor grows linearly with the sign of −X. Where (a) is hardest is therefore inside
(1, σ₁(F₀)), not at σ = 1. (Contrast: the true torus minimum m(σ) is nondecreasing (NT_001 Thm 1.3); the pointwise curve values are not.)

## 3. What (b) needs (Prop 10.4; PROVED equivalences, target OPEN)
(b) = existence, for 1 < σ ≤ 3/2, of a continuous version of Φ_σ on 𝕋^∞ restricting to Φ^{curve}_σ.
**Prop 10.4.** For 1 < σ ≤ 3/2 the following are equivalent: (i) (b); (ii) Φ_{σ′} (σ′ > 3/2, continuous) converges uniformly on 𝕋^∞ as σ′ ↓ σ
along the flow, i.e. the Poisson semigroup Φ_{σ′} = Q_{σ′−σ}⋆Φ_σ is uniformly Cauchy; (iii) the L² symbol Φ_σ (NT_003 Thm 3.4) is a.e. equal
to a continuous function. A sufficient condition is
  ∫_σ^{3/2+1}sup_θ|∂_{σ′}Φ_{σ′}(θ)|dσ′ < ∞,  ∂_{σ′}Φ_{σ′}(θ) = −Σ_r h(r)K(r)H(r)^{−σ′}χ_θ(r),
i.e. a uniform-in-θ bound for the height-weighted (h = log H) Weil series, integrable in σ′ down to σ.
*Proof.* (i)⟺(iii) by definition (continuous versions agree with the curve values by NT_005 Thm 5.1 density + continuity); (ii)⟹(iii):
Q_δ is an approximate identity as δ ↓ 0 (ρ_p = p^{−δ} → 1 for each p, product weakly → δ₀), so the uniform limit is a continuous
version; (iii)⟹(ii): Q_δ⋆ of a continuous function on a compact group converges uniformly. The sufficient condition integrates ∂_{σ′}. ∎
What it requires arithmetically: uniform (not mean-square) cancellation in Σ_{ℓ(r)∈[u,u+1]}h(r)H(r)^{−σ′}χ(r)Ξ(log r) for all characters χ,
in particular near the curve, at rate e^{−(σ′ − 1 + η)u}… beyond the unconditional prime-number-theorem error. On the curve itself this
cancellation is supplied by the FE/continuation (NT_005–006), not by absolute bounds; off the curve no mechanism is known. **OPEN.**

## 4. Review
- Thm 10.1: Laurent data ζ(1+2ε) = 1/(2ε) + γ + O(ε) ✓; G″(1) = 0 from oddness ✓ (G is real-analytic in σ near 1 off zeros).
- Cor 10.2 relies on: D (as hypothesis), NT_008 (PROVED), the ARGUED ∂ℛ bound. Label: PROVED modulo ARGUED bound. It is an implication
  from D (a consistency/strictness statement), not a sign proof.
- Prop 10.3 is a first-order statement; the O(ε²) term is τ₀-dependent (unbounded near zeros) — stated as first-order only.
- Prop 10.4 (ii)⟹(iii): Q_δ approximate identity on 𝕋^∞ — weak convergence of product of Poisson kernels to δ₀ as all ρ_p → 1 ✓.
- No zero-location reasoning used (zeros appear only as excluded points where ℓ′ is singular). **No sign contact.**

## Erratum note (after NT_008_010_REVIEW)
Cor 10.2 is CONDITIONAL (assumes D). Prop 10.3: the comparison with (𝒱) holds iff Re ∂_σℛ|₁ < 2(γ − ζ′/ζ(2))·Re ℛ₁ ≈ 2.294·Re ℛ₁ (true on the
spectral range for small T₀ by NT_008 and the ARGUED ∂ℛ bound), independently of X. "Hardest inside (1, σ₁)" is HEURISTIC.
