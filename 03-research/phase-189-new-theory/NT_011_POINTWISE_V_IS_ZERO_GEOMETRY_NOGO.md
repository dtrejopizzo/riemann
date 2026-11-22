# NT_011 — Pointwise (𝒱) needs zero geometry: the positive part of ℓ″ is carried exactly by zeros off the line; NO-GO for the class
# "functional equation + line identities + moment/mean-value bounds"

Phase 189, construction step 11. Notation of NT_007–010. Labels as before. The zeros of ζ appear here ONLY
to classify a method (as the coordinator asked); no statement about their location is used or claimed, and no equivalence involving row D
is invoked.

## Corpus check
grep "Hadamard" + "log|ζ|", "Davenport–Heilbronn"/"DH" falsifier (Paper 46, G2_B3_R1, R160 gates: DH as a method falsifier for FE-only
arguments), "moment" + "L¹-stable", phase-138 CORPUS_CHECK (Pólya/Jensen-type criteria as restatements). The FE-only falsifier idea is
classical/corpus (DH); **new here:** the explicit local model ζ̃ = ζ·R with exact FE, identical line identity, moments within O(δ), and
ℓ̃″ forced up by 1.5/δ²; the exact sign split of ℓ″ (Prop 11.1) at the profile scale; the NO-GO Thm 11.2 for pointwise (𝒱).

## 1. Sign split of ℓ″ (PROVED; Hadamard product CITED)
Write ρ = ½ + δ_ρ + iγ_ρ for the nontrivial zeros (multiplicity counted). For τ not an ordinate,
  ℓ″(τ) = Σ_ρ (δ_ρ² − (τ − γ_ρ)²)/((τ − γ_ρ)² + δ_ρ²)² + a″(τ),
with a(τ) := −log|Γ_ℝ(½+iτ)| + log|½ + iτ| + log|−½ + iτ| + const (smooth, a″ = O(1/(1 + τ²))); the ρ-sum converges absolutely
(Σ 1/(1+γ²) < ∞).
*Proof.* ξ(s) = ½s(s−1)Γ_ℝ(s)ζ(s) = ξ(0)Π_ρ(1 − s/ρ) (pairing ρ with 1 − ρ for convergence; CITED). On s = ½ + iτ:
log|ξ| = Σ_ρ log|½ + iτ − ρ| + const (paired), and d²/dτ²·½log((τ−γ)² + δ²) = (δ² − (τ−γ)²)/((τ−γ)² + δ²)². ∎
**Prop 11.1.** The positive part of ℓ″ − a″ at τ is Σ_{ρ: |τ−γ_ρ|<|δ_ρ|} of positive terms; zeros with δ_ρ = 0 contribute −1/(τ−γ)² < 0.
So every positive contribution to ℓ″ (beyond O(1/τ²)) comes from zeros with δ_ρ ≠ 0 and |τ − γ_ρ| < |δ_ρ|: **an upper bound on ℓ″ is a
statement about the geometry of such zeros relative to τ** (together with the competing negative terms). ∎ (Immediate from the formula.)

## 2. The NO-GO (PROVED)
**Class 𝓜.** Arguments whose inputs about ζ on the critical line are: (i) the FE ξ(s) = ξ(1−s) with ζ's Γ_ℝ and conductor 1; (ii) the line
identity Re(ζ′/ζ)(½+iτ) = −½m(τ) (off ordinates), equivalently the phase derivative; (iii) finitely many bounds of the form
∫_I|log|ζ(½+iτ)||dτ ≤ B₁, ∫_I|ζ(½+iτ)|^{2k}dτ ≤ B_k, |∫ℓψ_j| ≤ c_j (fixed intervals I, fixed weights), each with any fixed slack η > 0.
**Thm 11.2.** No argument in 𝓜 yields a pointwise upper bound for ℓ″ on any interval J, and hence none yields pointwise (𝒱) on J from
NT_009 Prop 9.2-type reductions.
*Proof (model function).* Fix γ₀ ∈ J (γ₀ ≠ 0) with ζ(½ + iγ₀) ≠ 0, small δ > 0, and put
  R(s) := Π_{±}[(s − ½ − δ ∓ iγ₀)(s − ½ + δ ∓ iγ₀)] / [(s − ½ − 2δ ∓ iγ₀)(s − ½ + 2δ ∓ iγ₀)],   ζ̃ := ζ·R.
(i) The zero/pole set of R is invariant under s ↦ 1 − s and s ↦ s̄, and R(1 − s) = R(s) (factor-by-factor check), so ξ̃ := ½s(s−1)Γ_ℝζ̃
satisfies ξ̃(s) = ξ̃(1 − s) with the same Γ_ℝ.
(ii) On the line, with x = τ ∓ γ₀: (ix − δ)(ix + δ)/((ix − 2δ)(ix + 2δ)) = (x² + δ²)/(x² + 4δ²) > 0, so R(½ + iτ) is real positive and arg ζ̃ = arg ζ
on the line: the line identity (ii) holds verbatim for ζ̃.
(iii) log|ζ̃| − log|ζ| = Σ_± log((x² + δ²)/(x² + 4δ²)) ∈ [−2log 4, 0], with ∫_ℝ|·|dτ = 2·2π(2δ − δ) = 4πδ; and |ζ̃|^{2k} = |ζ|^{2k}·∈[4^{−2k}, 1],
differing from |ζ|^{2k} by ≤ |ζ|^{2k}·min(1, 3δ²/x²)·4k, whose integral is ≤ C_k δ sup_{|τ∓γ₀|≤1}|ζ|^{2k}. So every input (iii) changes by
O_{k,γ₀}(δ) → 0: for δ small all inputs hold with the slack η.
(iv) ℓ̃″(γ₀) − ℓ″(γ₀) = [log(x² + δ²) − log(x² + 4δ²)]″|_{x=0} + O(1) = 2/δ² − 2/(4δ²) + O(1) = 3/(2δ²) + O(1) → +∞.
Hence 𝓜 cannot exclude ℓ″(γ₀) arbitrarily large. Since F̂₀(γ₀)² > 0 and X̃ = (F̂₀²ℓ̃′)′ ≥ F̂₀(γ₀)²·3/(2δ²) − O(1) at γ₀ while every 𝓜-input and the
discreteness remainder ℛ₁ (which does not involve ℓ) are unchanged up to O(δ), no 𝓜-argument proves X ≤ ζ(2)Re ℛ₁ at γ₀. ∎
**Scope.** ζ̃ has no Euler product: arguments that use the Euler product of ζ non-trivially (beyond the mean-value/moment level) are NOT
covered by this NO-GO. That is the only door left for pointwise (𝒱), and it is the coupling NT_005–006 already exhibit (ζ′/ζ at w, the
coprime counting) — but at σ = 1 that coupling has collapsed into ℓ (NT_007), so the Euler product would have to be used on the critical line.
Recorded in the master record as: **NO-GO (pointwise (𝒱) / pointwise ℓ″ bounds) for class 𝓜.**

## 3. Review
- Prop 11.1: standard; the pairing and absolute convergence of Σ(δ² − x²)/(x² + δ²)² ✓ (bounded by 1/x² for |x| ≥ 1).
- Thm 11.2(i): factors at ½ ± δ + iγ₀, ½ ± δ − iγ₀ form an orbit of {s ↦ 1−s, s ↦ s̄}; the ratio of two such orbit-products is FE-invariant ✓.
  (ii) ✓. (iv) the partner factor at −γ₀ contributes O(δ²/γ₀⁴) ✓.
- The model is not an L-function; that is the point of a method NO-GO (as with the corpus DH falsifier). It does not say anything about ζ.
- No sign is claimed; **no sign contact.**
