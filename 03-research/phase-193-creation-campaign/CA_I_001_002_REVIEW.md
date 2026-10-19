# CA_I_001, CA_I_002, CA_I_SYNTHESIS — Review

## CA_I_001 — CONFIRMED; Theorem 3 is the notable new fact. Verdicts endorsed.
| claim | check |
|---|---|
| (0.1) Lévy form of m | Re ψ(¼+iτ/2) − ψ(¼) = ∫e^{−x/4}(1 − cos(τx/2))/(1−e^{−x})dx ≥ 0 ⇒ positive Lévy density ✓ (CITED P60-1) |
| Thm 1 (Beurling–Deny, positivity improving, simplicity, λ_A > λ₀) | (|F(t)|−|F(t+u)|)² ≤ (F(t)−F(t+u))², c_{|F|} ≥ c_F, Λ ≥ 0 ✓; Ouhabaz/Reed–Simon CITED ✓; h₀ > 0 ⇒ h₀ ∉ 𝒫_T ✓. Caveat §8.1 (form taken without the polar term; equal to 𝔞_T on 𝒫_T) is correct and necessary |
| Prop 1.1 | resolvent positive only below λ₀ < λ_A ✓; P_T not positivity preserving ✓ |
| Thm 2 (Markov class closed under O2, λ_A → −∞) | three-bump construction: |K| < u kills all cross overlaps ✓; 3-dim span meets codim-2 𝒫_T ✓ — NO-GO PROVED |
| Thm 3 (ξE entire, E nonconstant FE rational ⇒ non-Markov at T ≥ T_E) | Lemma 3.1: bumps f₁ − f₂ at distance u₀ ∉ log ℕ, c_{|F|} − c_F = 2(f₁⋆f₂) ≥ 0 ✓; Lemma 3.2: leading almost-periodic part; Case 2 (P ≤ 0 ⇒ negative mean ⇒ net real pole of E at ½±δ*) excluded by ξ(σ) > 0 on ℝ ✓ (CITED, classical). Window-form formula for general E: CONFIRMED for quartets (P47 prop:quartetmodel(ii)); for general rational E the explicit-formula bookkeeping is ARGUED — FIX: label it so |
| Remark 3.3 | non-entire twist is Markov and has λ_A → −∞ ✓ (L(δ)² > 0) — entireness is load-bearing ✓ |
| Lemma 4 (≥ 2 sign changes) | Chebyshev system argument ✓ |
| Prop 5 (rearrangement) | ✓ |
| Cor 6 (𝖯⋆ separation) | ✓ as a separation: (S⁺) is asymptotic (CA_H_002 review), so 𝖯⋆ is a property of the infinite object; O14 OPEN (ARGUED non-Markov). REF-D as a route ✓ |
**Assessment.** Thm 3 + Cor 6 give the first property set of the campaign not closed under any single declared modification (O14 open). It is not an admissible candidate: there is no inequality, and "𝖯⋆ ⇒ λ_A ≥ 0" has ζ as its only instance in the declared universe (REF-D). Record as the campaign's sharpest *separation* result. Not a structural clause for thm:shape (it is a positive characterization, not an exclusion).

## CA_I_002 — CONFIRMED (retries sharpened).
Prop 1.1 linear in a (B″) ✓; V3 falsified by DH — transversality ARGUED (F-DH) ✓ flagged. Prop 2.2 one-sidedness from SPEC_A Lemma S(iv) ✓. §3 uses Paper 48 thm:M(b) (super-exponential upper bound), internal and unrefereed — label CITED-internal; with only P47 cor:margin1 the frequency is still ≥ 15.449T-scale, conclusion (R)(6) unchanged. §4–§6 ✓.

## CA_I_SYNTHESIS — faithful. YES→NO moves ENDORSED (max-principle/Krein–Rutman/comparison → NO, PROVED; virial → NO with ARGUED DH transversality; boundary layer → NO).
