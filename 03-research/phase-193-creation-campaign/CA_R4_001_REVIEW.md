# CA_R4_001 (L*_j(θ) at ½log5 → ½log7) — Review

## Verdict
**CONFIRMED. OPEN as stated; no proof, no falsifier. Prop R4.2 upgrades H1 to a theorem and confirms my CA_R3_001 review: clause (iii) of 𝒞_θ is information-identical to the data, so L*_j(θ) is REF-D with no extra mechanism.**

## Checks
| item | check |
|---|---|
| §0 bookkeeping | T_j = 0.8047, T_{j+1} = 0.9730; new row atom is 5 (entered at 2T = log5), 7 enters at the endpoint ✓. Note: this step is already covered by cited Liu Thm B (17/16 ≥ 0.973) — so it is a *structural* test, not new coverage (memo ✓) |
| §1 | v₄ = 2log2/2 = log2 ✓; √35 < 7 ✓; (Ch) on [1,7) with μ(4) = 0: y ∈ [6,7) gives log720 − log6 − log2 = log60 = ψ(6) ✓ |
| Prop R4.1 | −du and polar pieces lie in span{e^{±s/2}𝟙_I}, killed by Π_P ✓ (= Prop Θ(a); comb-generic, see CA_R3_001 review) |
| Prop R4.2 | Möbius inversion bijective on functions of {1,…,6}; (Ch)+positions ⟺ (Λ(2),…,Λ(6)) ✓ PROVED, and it generalizes to every contact (self-review 2) ✓ |
| §3 | rank-one bound ⟨Φ,𝔄_j^{−1}Φ⟩ ≥ |⟨Φ,h*⟩|²/μ (h* bottom eigenvector) ✓; necessary condition |ℓ_e(h*)|² ≤ μ·𝔞_{½log7}(e) ✓; √(2.5·10⁻¹²) ≈ 1.6·10⁻⁶ at the certified lower bound (true μ may be larger) ✓ |
| §4 classification | defeating term = evaluation of 𝔄_j^{−1} on the four-atom exterior field: prime-side + archimedean, not zero-side, not (B′) ✓; "cannot be closed by identities" ARGUED ✓ (labelled) |
## Notes
- The one live line (exterior continuation of the EL equation, SPEC_A §3) is EI_001's exterior identity; by EI_001's review its sign content is Lemma S = D (REF-D). Pre-flag: expect the same.
- Process: no numerics run beyond closed forms ✓; no zero information ✓.
Endorsed: "L*_j(θ) cannot be proved in 𝒞_θ at the first uncertified contact" as ARGUED NO-GO (method level); "(Ch) adds information beyond the data" → NO (PROVED, Prop R4.2).
