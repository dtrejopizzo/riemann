# L2_BUILD_025 — Lemma I in full (Theorem S closed); honest positioning; an explicit Euler × FE spectral density on Re s > 1

## Corpus check
L2_BUILD_024 (Theorem S, Lemma I ARGUED), L2_BUILD_010 (2Re(−ζ′/ζ)(½+iτ) = m − 2ΣRe 1/(s−ρ)), L2_BUILD_016 (copies on Re s = k/2), Paper 46
§subsec:KEP, Thm Z, lem:roughEF; L2_BUILD_011 (input map). grep "Re ξ′/ξ / Hadamard positivity / σ-family / homotopy of symbols /
Lagarias": phase-160 survey mentions Herglotz of ξ′/ξ as a REF-D structure (crossword I1 list); no memo builds the explicit positive
density D_σ for σ > 1 paired with a primitive profile. New: §1 (full proof), §3.

## 1. Lemma I and Theorem S, closed (PROVED; one standard density step CITED)
Profile (024 §2 with b > ½): g = e^{bt}1_{[0,a]}, b > ½, G₀ = g*g̃*g*g̃ (centred), F₀ = (¼−∂²)G₀ ∈ P_{T₀}, c₀ = c_{F₀}, ĉ₀ = F̂₀² with
F̂₀(τ) = (τ²+¼)|ĝ(τ)|⁴ > 0 on ℝ; as an entire function F̂₀(z)² = (z²+¼)²(ĝ(z)ĝ*(z))⁴, ĝ*(z) := conj ĝ(conj z), with zeros only at ±i/2 and at
2πk/a ± ib (|Im| = b > ½); the ±i/2 zeros are cancelled below.
Hypothesis: B := B_{F₀} positive definite (continuous, so |B| ≤ B(0) and B = ∫e^{iτd}dμ, μ ≥ 0 finite — Bochner, CITED).
Claim: λ_A(T) ≥ 0 for every T.
Proof. Step 1 (identity on compactly supported lag tests). For φ ∈ C_c^∞ with supp φ ⊂ [−R, R]:
 ∫Bφ = (1/2π)∫ m F̂₀² φ̂ dτ − Σ_{n ≤ e^{R+2T₀}} v_n (c₀*φ)(log n)   (finite sum; definition of B, c₀ even)   and   ∫Bφ = ∫φ̂ dμ (Bochner).
Step 2 (the target functional). Let G ∈ P_T be smooth with compact support in I_T, c_G its autocorrelation (smooth, supp ⊂ [−2T, 2T]),
ĉ_G = |Ĝ|² ≥ 0; ĉ_G is entire and vanishes to order 2 at ±i/2 (Ĝ(±i/2) = 0). Put ψ := ĉ_G/F̂₀² on ℝ. Then ψ ≥ 0, and ψ extends
holomorphically to the strip |Im z| < b (the ±i/2 zeros of F̂₀² are cancelled by those of ĉ_G; the other zeros have |Im z| = b), with rapid
decay in every closed substrip (ĉ_G rapidly decreasing on horizontal lines, |1/F̂₀²| polynomially bounded there). Hence ψ̌ (inverse Fourier
transform) satisfies |ψ̌(u)| ≤ C_β e^{−β|u|} for every β < b, and c₀*ψ̌ = c_G exactly (Fourier: ĉ₀ψ = ĉ_G).
Step 3 (approximation). χ ∈ C_c^∞, χ = 1 on [−1,1], 0 ≤ χ ≤ 1; φ_j(u) := ψ̌(u)χ(u/j) ∈ C_c^∞. As j → ∞:
 (a) φ_j → ψ̌ in L¹, so φ̂_j → ψ uniformly and sup_j‖φ̂_j‖_∞ < ∞; hence ∫φ̂_j dμ → ∫ψ dμ (μ finite) and ∫mF̂₀²φ̂_j → ∫mF̂₀²ψ (mF̂₀² ∈ L¹:
     F̂₀² = O(τ^{−4}), m = O(log|τ|)).
 (b) |(c₀*φ_j)(log n)| ≤ ‖c₀‖₁ sup_{|v−log n|≤2T₀}|ψ̌(v)| ≤ C n^{−β}, and Σ_n v_n n^{−β} = Σ 2Λ(n)n^{−½−β} < ∞ for β > ½ (choose ½ < β < b).
     Dominated convergence: Σ_n v_n(c₀*φ_j)(log n) → Σ_n v_n c_G(log n) (a finite sum, n < e^{2T}).
 So (1/2π)∫mĉ_G − Σ v_n c_G(log n) = lim_j ∫Bφ_j = lim_j ∫φ̂_j dμ = ∫ψ dμ ≥ 0. The left side is 𝔞_T(G) (eq:Aform; polar terms absent on P_T).
Step 4 (density). Smooth compactly supported primitive G are dense in P_T ∩ D_T for the form norm: mollification preserves the Tate
conditions (A(G*η) = A(G)∫η e^{t/2}, likewise B) and a slight dilation keeps the support inside I_T (as in lem:contA steps 1–3, CITED).
The form is continuous in the form norm, so 𝔞_T ≥ 0 on P_T ∩ D_T. ∎
**Theorem S (now PROVED, profile with b > ½): λ_A(T) ≥ 0 ∀T ⟺ B_{F₀} is positive definite on ℝ.**
Note: the condition b > ½ is exactly what makes the prime sum converge in Step 3(b): the profile must be "analytic beyond the polar line".

## 2. Honest positioning
- Classical: positivity of the Weil distribution on all test functions of the form f*f̃ (Weil; CITED). Theorem S restricts the test class to
  ONE translation orbit {τ_dF₀}: by Bochner, positivity on finite combinations of translates of one profile already implies positivity on the
  whole primitive class. This is a known-in-spirit mechanism (a cyclic vector for the translation group under the positive form, with F̂₀ > 0
  making the orbit "total").
- Paper 46 KEP: per-window positive definiteness of the explicit-formula datum g on (−2T, 2T). Theorem S: one window-free function of one
  variable, B_{F₀}, no T. **Genuinely new is only "one fixed explicit profile, no T"**; the content is a reformulation, not a sign.

## 3. The constructive question: an explicit positive spectral density from Euler × FE (PROVED on Re s > 1; OPEN at ½)
For σ ∈ ℝ define the symbol family (s = σ + iτ)
  D_σ(τ) := 2Re (ξ′/ξ)(s) = m_σ(τ) + p_σ(τ) − Σ_n 2Λ(n)n^{−σ}cos(τ log n)   (σ > 1: absolutely convergent),
  m_σ := Re ψ(s/2) − log π, p_σ := 2Re[1/s + 1/(s−1)].
At σ = ½: m_{½} = m, p_{½} = 0, weights 2Λ(n)n^{−½} = v_n: D_{½} is σ_∞ (024) — formally; the pairing at ½ is the analytic one of Step 1.
**Proposition H (PROVED; Hadamard product of ξ and β ∈ [0,1] for all zeros, CITED: Euler product ⇒ no zeros in Re s > 1, FE ⇒ none in
Re s < 0).** For σ > 1, D_σ(τ) ≥ 0 for all τ (σ = 1 excluded: pole at s = 1 and non-absolute convergence), hence B^{(σ)}(d) := (1/2π)∫e^{iτd}D_σ(τ)F̂₀(τ)²dτ = (h_σ ⋆ h̃_σ)(d) with the EXPLICIT
ĥ_σ := √(D_σ)·F̂₀ (Γ-factor and an absolutely convergent Λ-series; no zero input in the formula).
*Proof.* ξ′/ξ(s) = Σ_ρ 1/(s − ρ) summed over pairs {ρ, 1 − ρ̄} (CITED). For ρ = β + iγ, x := σ − β, y := σ − 1 + β, t := τ − γ, the pair contributes
Re[1/(x+it) + 1/(y+it)] = (x + y)(xy + t²)/((x²+t²)(y²+t²)). For σ > 1 and 0 ≤ β ≤ 1: x, y > 0, x + y = 2σ − 1 > 0, so each pair term is ≥ 0. ∎
Discrimination (input map 011): the proof uses the Euler product (no zeros in Re s > 1) AND the FE (pairing ρ ↔ 1 − ρ̄, completion by Γ)
non-linearly (log-derivative). It does not apply to a_P / finmod (no FE: no pairing, ζ_a = ζE with E not FE-symmetric), to Epstein/DH (FE but
zeros in Re s > 1 exist, Davenport–Heilbronn CITED: the pair terms with β > σ can be negative), nor to Beurling systems without FE. ✓
Where it stops (PROVED structure): for ½ < σ < 1 a pair term is negative exactly where t² < −xy = (β − σ)(σ − 1 + β), i.e. only if σ < β (a zero
right of σ). At σ = ½, x + y = 0: the pointwise pair terms vanish identically off the line and the on-line zeros give point masses; the pairing
that defines B = B^{(½)} (Step 1) is the analytic continuation, NOT the boundary value of D_σ. So the explicit h_σ of Proposition H does not
continue to σ = ½ by a pointwise limit. OPEN: an explicit factorization B_{F₀} = h ⋆ h̃ at σ = ½ (any such h is equivalent to the target by
Theorem S + Bochner; constructing it without zero input is the problem).
Relation to the corpus: Herglotz-type positivity of ξ′/ξ in a half-plane is listed in the crossword (I1) among structures whose sign step is
D itself at σ = ½; Proposition H is its unconditional part on σ > 1, made explicit on the single-profile orbit.

## 4. Review
- §1 Step 2: holomorphy strip: zeros of ĝ(z) are 2πk/a + ib and of ĝ*(z) are 2πk/a − ib; with b > ½ the strip |Im z| < b contains only the
  ±i/2 zeros of F̂₀², cancelled by ĉ_G. Decay of ψ on horizontal lines: ĉ_G(z) for G smooth compactly supported decays faster than any power
  on each horizontal line; 1/F̂₀² grows at most polynomially away from its zeros (|ĝ| ≥ c/|b+iz| type bound on lines |Im z| ≤ β < b). Correct.
- Step 3(b): the decay rate β must exceed ½ for Σ 2Λ(n)n^{−½−β} < ∞ — that is why b > ½. Correct. Step 4 density CITED (standard).
- Theorem S now PROVED for the b > ½ profile. 024's statement with "b ≠ 0" is superseded by this hypothesis (024 not edited).
- §3: Proposition H is a classical computation (Hadamard pairing), stated with honest CITED inputs; its content for D is nil at σ = ½ and the
  memo says so. It does show, as the coordinator asked, an explicit positive spectral representation built from Euler × FE with no zero input,
  valid exactly on the half-plane where Euler alone already controls the zeros.
- No sign certified; no negative value of 𝔞_T for ζ.
