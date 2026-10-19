# CA_B_008 — The concavity gap Γ: pre-screen and the two-minimizer angle bound (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed; no sign contact.**
Setting: measure combs ν on (0,2T); 𝔞^ν(F) = C_0 + Lev(c_F) − ⟨ν, c_F⟩ on unit F ∈ P_T ∩ D_T; b(ν) = inf 𝔞^ν (attained; compact resolvent).

## 1. Definitions and the one theorem (PROVED)
For ν_ζ = θν^{(1)} + (1−θ)ν^{(2)}, θ ∈ (0,1): A := 𝔞^{ν^{(1)}}, B := 𝔞^{ν^{(2)}}. Then 𝔞^{ν_ζ} = θA + (1−θ)B exactly, because the forms are
affine in ν and the archimedean part is the same. Put Γ := b(ν_ζ) − θb(ν^{(1)}) − (1−θ)b(ν^{(2)}) ≥ 0.
**Theorem 1 (angle bound).** Suppose b(ν^{(i)}) are simple with unit minimizers h_1, h_2 and spectral gaps g_1, g_2 (distance to the
rest of the spectrum on P_T). Then
  Γ ≥ min(θg_1, (1−θ)g_2) · (1 − |⟨h_1, h_2⟩|).
Proof. A − b_1 ≥ g_1(1 − P_1) and B − b_2 ≥ g_2(1 − P_2), with P_i the projection onto h_i. So θ(A−b_1) + (1−θ)(B−b_2) ≥ m(2 − P_1 − P_2),
m = min(θg_1,(1−θ)g_2). The nonzero eigenvalues of P_1 + P_2 are 1 ± |⟨h_1,h_2⟩|, so the bottom of 2 − P_1 − P_2 is 1 − |⟨h_1,h_2⟩|. ∎
Γ = 0 iff there is a common minimizer (CA_B_007 Prop 2).

## 2. Pre-screen
| screen | outcome |
|---|---|
| **REF-D** (can Γ be bounded below without b(ν_ζ)?) | **NO (PROVED, tautology).** Since 𝔞^{ν_ζ} = θA + (1−θ)B, at least one piece carries Λ's fluctuation. In the two-piece form with ν^{(1)} = ρ_κ (computable, b ≥ η_κ), B = (𝔞^{ν_ζ} − θA)/(1−θ) **exactly**. Then b(ν^{(2)}), h_2 and g_2 are spectral data of 𝔞^{ν_ζ} − θA, which is the target form minus an explicit positive form. Theorem 1 then reads λ_A ≥ θη_κ + inf(𝔞^{ν_ζ} − θA) + m(1 − |⟨h_A, h_B⟩|). Every term on the right except θη_κ is computed from 𝔞^{ν_ζ}. Splitting into k ≥ 3 pieces does not help: Σθ_iν^{(i)} = ν_ζ forces the fluctuation into the pieces, and each piece containing part of it (e.g. residue-class restrictions, which are O6-type) has a bottom as hard as, or harder than, the target |
| **O-list, O7 realignment test first** | the identity of §1 and Theorem 1 hold for **every** measure ν (only concavity and spectral calculus are used). Under O7, ν_ζ ↦ ν_ζ − kβ_z, so B ↦ B + kβ_z-term/(1−θ): h_2 moves, and at a witness (thm:wit-model(iii)) Γ < −θη_κ − (1−θ)b(ν^{(2)}). No contradiction. The quartet "realigns" exactly as much as the bottom requires, because Γ is defined from the bottoms. **Comb-generic: excluded by (B″) / lem:shape-ident.** Same for O1–O6, O8, O11, O15 |
| (R)(4) zeros | passes (no zero data) |
| (R)(5) window observables / W-pat, W-det, W-mom, W-loc | **fails.** The misalignment is a single overlap ⟨h_1,h_2⟩ of two window minimizers plus two gaps: a pattern of finitely many window observables (R)(5). prop:nyq-nopoint (no common diagonalization of the two Nyquist sectors) and thm:wh-angles (exact cot²-angle formula for two constant-weight bands) are coordinates of exactly this type. Theorem 1 is the rank-one analogue of thm:wh-angles: a coordinate, not a mechanism |
| (R)(6),(7) | Theorem 1 loses: Γ ≥ m(1 − |c|) is sharp only when the two minimizers are the only low modes. The arena has ≥ 12 modes (memory: phase 155 rounds 6–7), so g_2 is tiny and the bound is far from the margin |
| (R)(8) positive part with negative set | formally yes (A is the positive part) |
| (R)(3) non-linear | yes (through h_2), but only through spectral data of the target form |
| (R)(11) | **fails**: the sign step is "λ_A ≥ [terms computed from 𝔞^{ν_ζ}]", a restatement |
Verdict: **EXCLUDED** (REF-D tautology + (B″) + (R)(5)). Theorem 1 is recorded as a PROVED coordinate (two-minimizer angle bound).
**YES→NO:** "concavity gap as a non-linear sign carrier" → NO; "misalignment of archimedean and near-coincidence minimizers" → it is a
window observable (R)(5), NO.

## 3. Self-review
- Theorem 1: correct for simple bottoms. If a bottom is degenerate, replace P_i by the spectral projection and |⟨h_1,h_2⟩| by the cosine of
  the smallest principal angle. ✓
- The REF-D row is a structural tautology: any split of an affine form writes the target as a function of its own spectral data. This
  generalizes CA_B_007 §2 and closes the decomposition family (convex hull, gap, angle) as a whole. It also matches the earlier
  operative-constraint framing: the exclusion is (B″) + REF-D, not openness.
- Is there a residual? Only if one of the pieces is certifiable by an argument that uses ζ non-linearly and is not a bound on the target
  form itself, e.g. a piece whose comb is an Euler-product object with an exact FE. That is back to CA_B_003/005 (self-matching), and
  there the open question is the same: an inequality, not an identity, that uses Δ ≡ 0.
