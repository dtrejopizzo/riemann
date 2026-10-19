# L2_BUILD_026 — The FE reflection σ ↔ 1−σ on the σ-family: antisymmetric, so symmetrization is void

Notes taken (coordinator): Proposition H of 025 (Re ξ′/ξ ≥ 0 to the right of all zeros) is CLASSICAL (Lagarias-type positivity of ξ′/ξ in a
half-plane) — recorded as CITED-known, not new. Any σ-transport must be checked against cor:void (C_zeros), L2_BUILD_010 and N_BUILD_013 (exact
criticality), and must act on the comb at window level, not through zero location. 024/025 not edited (under referee review).

## Corpus check
025 §3 (D_σ, Prop H), 010 (2Re(−ζ′/ζ)(½+iτ) = m − 2ΣRe 1/(s−ρ), centre criticality), N_BUILD_013 (packet limits critical at every γ), Paper 47
cor:void, crossword I1 (Herglotz of ξ′/ξ listed among REF-D structures). New: §1 identity, §2 window-level family and its limit lemma, §3 verdict.

## 1. The spectral reflection is exactly antisymmetric (PROVED)
ξ(s) = ξ(1 − s) and ξ real on ℝ give ξ′/ξ(1 − s) = −ξ′/ξ(s) and ξ′/ξ(conj s) = conj ξ′/ξ(s). Hence for every σ and real τ (away from zeros):
  D_{1−σ}(τ) = 2Re ξ′/ξ(1 − σ + iτ) = −2Re ξ′/ξ(σ − iτ) = −2Re conj(ξ′/ξ(σ + iτ)) = −D_σ(τ).
Consequences: (a) D_σ + D_{1−σ} ≡ 0: every symmetric combination B^{(σ)} + B^{(1−σ)} vanishes identically; the antisymmetric one is 2B^{(σ)}.
**NO-GO (PROVED): no positivity mechanism can come from the FE-symmetrization of the spectral family; it carries no information.**
(b) At σ = ½: D_{½} = −D_{½}, so D_{½}(τ) = 0 for every real τ that is not the ordinate of a zero on the line. The boundary spectral density on
the critical line is identically zero apart from point masses at real zeros of Ξ. This is the pointwise form of L2_BUILD_010 (vanishing at
τ = 0 for any configuration) and of the exact criticality of N_BUILD_013: on the line the archimedean density and the prime density cancel
pointwise, and the entire sign of B = B_{F₀} lives in the singular part (on-line masses) and in the analytic-continuation pairing (off-line
residues) — never in a density.

## 2. The window-level (comb) family and its limit (PROVED)
For σ ∈ ℝ and d ∈ ℝ define, with the fixed profile F₀ (025 §1) and c₀ = c_{F₀},
  B^{comb}_σ(d) := (1/2π)∫e^{iτd}(m_σ(τ) + p_σ(τ))F̂₀(τ)²dτ − Σ_{n≥2}2Λ(n)n^{−σ}·½[c₀(d − log n) + c₀(d + log n)]
(m_σ = Re ψ((σ+iτ)/2) − log π, p_σ = 2Re[1/(σ+iτ) + 1/(σ−1+iτ)]; for each d the sum is finite). Then:
(i) B^{comb}_σ(d) is continuous in (σ, d) for σ ∈ (0, 1) ∪ (1, ∞) … and at σ = ½ equals B_{F₀}(d) (p_{½} ≡ 0, m_{½} = m, weights v_n).
(ii) For σ > 1, B^{comb}_σ = B^{(σ)} (absolute convergence), which is positive definite (Prop H, CITED-known).
(iii) (Limit lemma) If B^{comb}_σ is positive definite for a sequence σ_j ↓ ½, then B_{F₀} is positive definite (pointwise limits of positive
     definite functions are positive definite), hence λ_A ≥ 0 ∀T by Theorem S.
(iv) For ½ < σ < 1 the window-level object is a deformed problem: comb weights 2Λ(n)n^{−σ} (damped), archimedean symbol m_σ, and a polar
     term p_σ that no longer vanishes (p_σ(0) = 2(2σ − 1)/(σ(σ − 1)) < 0 for ½ < σ < 1): the Tate points of the fixed profile (±i/2) no longer
     annihilate the poles of the line-σ problem (at τ = ∓iσ, ∓i(σ−1) relative to the line).
*Proof.* (i): finite sums continuous in σ; the integral is continuous by dominated convergence (F̂₀² = O(τ^{−4}), m_σ = O(log|τ|),
p_σ bounded on compact σ-sets away from 0, 1 as a function of τ). (ii): rearrangement for σ > 1. (iii): Σs_ks_lB_{σ_j}(a_k − a_l) ≥ 0 passes to
the limit. (iv): direct computation. ∎

## 3. Verdict on σ-transport under the coordinator's constraint
- Spectral level: reflection is antisymmetric (§1) — void.
- Window level: transporting positive definiteness of B^{comb}_σ from σ > 1 down to ½ through (½, 1) requires, for each intermediate σ, a
  positivity statement for the deformed window problem of §2(iv). The difference B^{comb}_σ − B^{(σ)} (when the latter is defined by the
  boundary density) is, via the explicit formula as an identity, a sum of residues at zeros right of σ; so any proof that proceeds by
  controlling that difference is a zero-location argument, excluded as a mechanism by cor:void (C_zeros) — NOT built here.
- A comb-level route would have to prove positive definiteness of B^{comb}_σ directly from the damped comb and m_σ + p_σ, for σ ↓ ½. At
  σ = ½ + η, by §1(b) the density D_{½+η} is O(η) pointwise away from zeros (continuity of ξ′/ξ in σ), so the positive density is of size η
  while the comb terms are O(1): the margin vanishes linearly as σ → ½. No uniform-in-σ positivity is available from the density; the family
  is exactly critical at the endpoint (consistent with 010 / N_013). OPEN, with this explicit degeneration rate.

## 4. Review
- §1 is elementary and correct; it disposes of the symmetrization idea completely. (b) is a clean pointwise restatement of criticality.
- §2(i): continuity across σ = ½ verified (p_σ → 0, m_σ → m); near σ = 0, 1 there are singular terms, irrelevant for (½, 1).
- §2(iii) is the only positive structural statement: positivity on a sequence σ_j ↓ ½ suffices. PROVED.
- §3 "O(η) density near ½" is ARGUED (continuity of Re ξ′/ξ in σ away from zeros, uniformity in τ not proved).
- Labels: Prop H CITED-known (classical), no new positivity. No sign certified; no negative value of 𝔞_T for ζ.
