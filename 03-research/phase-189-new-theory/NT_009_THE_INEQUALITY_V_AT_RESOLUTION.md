# NT_009 — The ℓ²-line inequality (𝒱): unconditional proof at resolution T₀^{1/3}; the pointwise statement reduced to a convexity
# bound for log|ζ(½+iτ)| on the spectral range

Phase 189, construction step 9. Notation of NT_005–008. Labels as before. Correction to the coordinator's
note: on the line, ℓ′(τ) = d/dτ log|ζ(½+iτ)| = −Im(ζ′/ζ)(½+iτ); Re(ζ′/ζ)(½+iτ) = −½m(τ) is the FE identity (R160_PD_R1 Lemma 2.1).

## Corpus check
grep "log|ζ(½+it)|" (R162_1003 sum–difference; phase 59/198 axiomatized gap; G2_B3_R2), "Jensen" (only Jensen polynomials, phase 138),
"weak positivity" + "resolution": no memo proves a resolution-limited version of a necessary pointwise inequality of D. **New:** Thm 9.1, Prop 9.2.

## 1. Sizes of the profile factors (PROVED)
‖F̂₀‖_∞² ≤ ‖F₀‖₁² ≤ 2T₀ and ‖(F̂₀²)′‖_∞ ≤ 2‖F₀‖₁‖tF₀‖₁ ≤ 2T₀², ‖(F̂₀²)″‖_∞ ≤ 2(‖tF₀‖₁² + ‖F₀‖₁‖t²F₀‖₁) ≤ 4T₀³
(supp F₀ ⊂ [−T₀, T₀], ‖F₀‖₂ = 1, Cauchy–Schwarz).
So X(τ) := (F̂₀²ℓ′)′(τ) = (F̂₀²)′ℓ′ + F̂₀²ℓ″ carries the small factors T₀², T₀.

## 2. Weak (𝒱) (PROVED, unconditional; one CITED bound)
Input (CITED, standard via Jensen's formula for ζ in discs of fixed radius around ½ + it): for |t| ≥ 2 and 0 < w ≤ 1,
∫_t^{t+w}|log|ζ(½+iu)||du ≪ log|t|; on |t| ≤ 2 the integral is bounded (log|f| is locally integrable for analytic f ≢ 0).
**Thm 9.1.** There are absolute c, T* such that for T₀ ≤ T*, every interval I ⊂ [−C/T₀, C/T₀] of length w ≥ w₀ := c(C)·(T₀ log(1/T₀))^{1/3}
(and w ≤ 1), and every φ ∈ C²_c(I) with φ ≥ 0 and ‖φ″‖_∞ ≤ 16‖φ‖_∞/w², ‖φ′‖_∞ ≤ 4‖φ‖_∞/w, ∫φ ≥ w‖φ‖_∞/4 (standard bump):
  ∫V(τ)φ(τ)dτ ≥ ½(a₀ − 3.1)∫φ > 0.
*Proof.* V = −X/ζ(2) + Re ℛ₁ (NT_007 Thm 7.1). By NT_008, Re ℛ₁ ≥ a₀ − 3.02 − o(1) on the range. Integrate by parts twice (φ compactly
supported; ℓ′ has only 1/(τ − γ)-type singularities at zeros on the line, and ∫Xφ is understood as −∫F̂₀²ℓ′φ′ = ∫ℓ(F̂₀²φ′)′, the
distributional derivative of the locally integrable ℓ): |∫Xφ| ≤ ‖(F̂₀²φ′)′‖_∞∫_I|ℓ| ≤ (2T₀·16/w² + 2T₀²·4/w)‖φ‖_∞·K log(2 + C/T₀).
With ∫φ ≥ w‖φ‖_∞/4, the ratio |∫Xφ|/(ζ(2)∫φ) ≤ K′T₀log(1/T₀)/w³ ≤ ½(a₀ − 3.1) for w ≥ w₀. ∎
**Reading.** Seen through any test of width ≥ T₀^{1/3}·(log)^{1/3}, the height flow on the ℓ² line is positive, with margin ≈ ½a₀. This is the
first positivity statement of the theory at σ = 1, the line where the coprime-counting pole and the FE meet. Its proof is NOT class-level in
form (it uses log|ζ(½+iτ)|, which exists only for ζ, and NT_008's exact ℛ₁), but its mechanism is still archimedean dominance: a₀ ≫ T₀-weighted
size of log|ζ|. Honest assessment: Λ-specific statement, cheap mechanism.

## 3. The pointwise statement (reduction; OPEN)
**Prop 9.2.** On |τ₀| ≤ C/T₀, (𝒱) holds at τ₀ whenever
  F̂₀(τ₀)²ℓ″(τ₀) + (F̂₀²)′(τ₀)ℓ′(τ₀) ≤ ζ(2)(a₀ − 3.1),
in particular whenever ℓ″(τ₀) ≤ ζ(2)(a₀ − 3.1)/(4T₀) and |ℓ′(τ₀)| ≤ ζ(2)(a₀ − 3.1)/(4T₀²). Near a zero γ of ζ on the line, X(τ) ~ −F̂₀(γ)²/(τ − γ)²
→ −∞ (favourable). ∎ (§1 sizes + NT_008.)
So pointwise (𝒱) on the spectral range is implied by a **one-sided convexity bound for log|ζ(½+iτ)|**: ℓ″ ≤ c·log(1/T₀)/T₀ and
|ℓ′| ≤ c·log(1/T₀)/T₀² where the latter is not near a zero on the line. No unconditional pointwise upper bound of ℓ″ is available from
identities or mean values (the partial-fraction formula for (ζ′/ζ)′ involves all zeros, and its sign depends on their position — not used,
). **OPEN**, and it is exactly where positivity at σ = 1 would have to be decided: the competition between the
second derivative of log|ζ| on the critical line (weighted by F̂₀² ≤ 2T₀) and the archimedean energy a₀ minus the 3/2-Div symbol.

## 4. Review
- §1 bounds: |∂^jF̂₀| ≤ ‖t^jF₀‖₁ ≤ T₀^j‖F₀‖₁ ✓.
- Thm 9.1: the double integration by parts is legitimate for ℓ ∈ L¹_loc with distributional derivatives; the identification of ∫Vφ with
  the distributional pairing requires V's singularities (at zeros on the line, +F̂₀²/(τ−γ)²) to be read as a positive non-integrable
  singularity: then ∫Vφ = +∞ ≥ bound trivially, or (principal-value reading) the integration-by-parts value. Stated: we prove the
  inequality for the distributional pairing −∫F̂₀²ℓ′φ′/ζ(2)-version. ✓ (This is the reading under which Cor 7.2's limit is taken.)
- The CITED Jensen-type bound: standard (Titchmarsh ch. 9 methods); not re-proved.
- Mechanism is archimedean dominance; NOT sign-carrying in the sense of the corpus (it would hold for any comb with the same remainder size —
  but such combs have no ℓ; so "class-level" is not even defined; flagged as cheap).
- **No sign contact.**

## Erratum note (after NT_008_010_REVIEW)
Citation: Titchmarsh Thm 9.6(A) + Thm 9.2 (local formula and zero counting). Thm 9.1 bounds the regularised (distributional) pairing
−∫F̂₀²ℓ′φ′/ζ(2) + ∫Re ℛ₁φ. Width w₀ ∝ (T₀ log(1/T₀)/a₀)^{1/3}. Pointwise (𝒱) is intrinsically zero geometry (NT_011): recorded as a NO-GO
for identities/mean values (class 𝓜), which lies inside cor:void's zero-information class.
