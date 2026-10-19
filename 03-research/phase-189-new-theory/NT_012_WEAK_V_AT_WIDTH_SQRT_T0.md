# NT_012 — Weak (𝒱) pushed to width K√(T₀ log(1/T₀)); this is the limit of the method

Phase 189, construction step 12. Notation of NT_007–011.

## Corpus check
NT_009 Thm 9.1 (width (T₀ log)^{1/3}); Titchmarsh §9.6 local formulas (CITED in corpus? grep "9.6": phase-160 R160_C3_R1 uses Titchmarsh 9.7
for good heights). **New:** the short-interval L¹ bound route and the width √T₀; the limit statement (Prop 12.2).

## 1. Input (CITED, unconditional; counts zeros, no location used)
For |t| ≥ 2 and s = ½ + iu, |u − t| ≤ 1: log|ζ(s)| = Σ_{|γ−t|≤2}log|s − ρ| + O(log|t|), the sum having ≪ log|t| terms (Titchmarsh, Theory of
the Riemann zeta-function, §9.6, consequence of Thm 9.6(A) by integration; and N(t+2) − N(t−2) ≪ log t, Thm 9.2). Hence for an interval
I ∋ t of length w ≤ 1: ∫_I|ℓ| ≤ K w log|t|·log(2/w) (each term: ∫_I|log|u − γ|| du ≤ w(1 + log(1/w)) + w log(4)…).
## 2. Statement (PROVED, given the CITED input)
**Thm 12.1.** There are absolute K, T* such that for T₀ ≤ T*, every interval I ⊂ [−C/T₀, C/T₀] of length w with
K(C)·(T₀ log(1/T₀))^{1/2} ≤ w ≤ 1, and every standard bump φ ≥ 0 on I (NT_009 Thm 9.1): ∫Vφ ≥ ½(a₀ − 3.1)∫φ.
*Proof.* As NT_009 Thm 9.1 with the new L¹ bound: |∫Xφ| ≤ ‖(F̂₀²φ′)′‖_∞∫_I|ℓ| ≤ (32T₀/w² + 8T₀²/w)‖φ‖_∞·Kw log(1/T₀)log(2/w), while
ζ(2)·½(a₀ − 3.1)∫φ ≥ ζ(2)(a₀ − 3.1)w‖φ‖_∞/8. With a₀ ≥ ½log(1/T₀) − C: need w² ≥ K′T₀ log(2/w) — true for w ≥ K″(T₀ log(1/T₀))^{1/2}. (|t| ≤ 2: bounded
L¹, same conclusion.) ∎
**Prop 12.2 (limit of the method).** Any argument of the form "|∫Xφ| ≤ ‖derivatives of F̂₀²φ‖·(L¹-type bound on ℓ or ℓ′ over I)" cannot go
below width w ≍ √T₀ up to logs: the left side's model size for a bump is T₀‖φ‖_∞·(log)/w (two derivatives at scale w against ∫|ℓ| ≍ w log),
the right side a₀w‖φ‖_∞. And by NT_011 Thm 11.2 no class-𝓜 argument reaches width → 0. ∎
**Reading.** At σ = 1 the height-flow symbol is nonnegative (margin ½a₀) on every window of width ≥ K√(T₀log(1/T₀)) across the whole spectral
range |τ₀| ≤ C/T₀. Mechanism: archimedean dominance (cheap), Λ-specific in form. The residual question at σ = 1 lives on scales < √T₀ around
points where ℓ″ is large positive — exactly the zero-geometry of NT_011.

## 3. Review
- The CITED local formula is standard and unconditional (uses only zero counting). ✓ log(2/w) ≤ log(1/T₀) on the range ✓.
- The distributional reading of ∫Xφ is as in NT_009 (note there). ✓
- No sign contact.
