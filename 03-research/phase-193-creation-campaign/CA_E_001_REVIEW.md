# CA_E_001 — Review
Checked vs P47 thm:oneprofile, prop:AM(i), §subsec:oneprofile; my CA_E_000 pre-flag.

## Verdict
**Lemma 0, Lemma 1, Theorem 1, Cor 1.1, Cor 1.2, Theorem 2: CONFIRMED PROVED. EXCLUDED as sign steps ((B″), REF-D) — memo agrees. Pre-flag resolved: the theorems concern the global target via prop:AM(i) (PD on G = ℚ_{>0}^×), so neither the M-cutoff nor the window compression enters; self-review 4 correctly leaves fixed-T compression to the closed Sonin/WH walls.**

## 1. Checks
| claim | check |
|---|---|
| Lemma 0 | finite Q ⊂ G scales into ℕ by a common denominator, φ is ratio-invariant ✓; prop:AM(i) ✓ |
| Lemma 1 | PD on the dense subgroup log G + continuity ⇒ PD on ℝ ✓; μ_φ = ι_*ν by uniqueness of Fourier–Stieltjes transforms on Ĝ ✓; ι injective (two primes suffice) ✓ |
| Thm 1 | induction: g_b PD on ℤ^{S′}; b ↦ ρ_b Hermitian measure-valued; for each Borel E, w ↦ ρ_w(E) PD ⇒ |ρ_w(E)| ≤ ρ₀(E) ⇒ ρ_w = h_wρ₀; a.e. PD of w ↦ h_w(θ) via countably many rational b ✓; κ = κ_θ⊗ρ₀ ≥ 0 with κ̂ = f ✓; projective consistency ⇒ μ on Ĝ ✓. Sound |
| Cor 1.2 | positive Schur multipliers are CP (Paulsen, CITED) ✓ |
| Thm 2 | μ_{gb} = μ_g ∗ μ_b; μ_φ(ι(ℝ)) = ∫μ_g(ι(ℝ) − y)dμ_b(y) ✓; (a) fibre over θ′ is ≤ 1 point, atomless g_p ⇒ 0 ✓; (b) Steinhaus: a σ-compact subgroup of positive Haar measure is open, hence = Ĝ (connected) ✗ ⇒ null ✓; 𝖡(0) > 0 (Fact 0) gives the contradiction ✓ |
| Remark (line-type factors ⇒ ν = ν₁∗ν₂ ⇒ zero side or C–S) | ARGUED ✓ labelled |

## 2. Screens
B″ ✓ (every comb with 𝖡(0) > 0); O7–O12 survive ✓; (R)(11) ✗; [crit] n/a. FE-genericity: comb-generic, hence a fortiori survives Epstein x²+5y² (as a statement on its own 𝖡). No numerics run ✓; Cor 1.1 off-line Fejér means: a falsifier search only — not strictly necessary, agree not to run.
## 3. Index: "quantum-information positivity (CP, Choi, entanglement witnesses, decomposability, NC hierarchies, product-state kernels) on the window target → collapses to μ_φ ≥ 0 (CA_E_001 Thm 1, Cor 1.2, PROVED); Schur factorization through atomless-local or Haar-a.c. PD kernels → NO-GO (Thm 2, PROVED)". ENDORSED.
