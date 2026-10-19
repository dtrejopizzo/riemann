# NT_011–014 + NT_SYNTHESIS — review

Pen and paper. Labels: CONFIRMED / FIX / DOWNGRADE / NO-GO.

## NT_011 (model ζ̃ = ζ·R; Prop 11.1; Thm 11.2)
- **Prop 11.1: CONFIRMED.** At x = 0, each zero term (δ² − x²)/(x² + δ²)² equals 1/δ². A zero on the line contributes −1/x². The pairing and
  absolute convergence are standard.
- **(i) FE: CONFIRMED.** Under s ↦ 1 − s, each linear factor maps to −1 times a factor of the same orbit with ±γ₀ swapped. There are 4 sign flips
  in the numerator and 4 in the denominator, so R(1 − s) = R(s). The orbit is also stable under conjugation. Γ_ℝ and conductor 1 are unchanged.
- **Holomorphy: FIX (essential to the statement).** R has four poles at ½ ± 2δ ± iγ₀, all off the line, so ζ̃ is NOT entire away from s = 1, and
  ξ̃ is meromorphic, not entire. The class 𝓜 as written lists only "FE", so it tacitly allows poles. The statement must say this explicitly:
  𝓜 does not use holomorphy of ξ in the strip, its order-1 growth, or the Hadamard product.
  - Consequence: NT_012's own input (the Titchmarsh §9.6 local formula, which comes from holomorphy and Jensen) is NOT in 𝓜.
  - An entire variant can be built (ARGUED, not needed). Take ζ·exp(−c·e^{−((s−½)²+γ₀²)²/δ⁴}), which on the line is a real positive factor
    localized at ±γ₀. It is FE-invariant and entire, but of infinite order. So the honest NO-GO reads: no argument using only FE, the line
    identity and mean values, plus either holomorphy or order-1 growth but not both, can bound ℓ″ pointwise.
  - With both holomorphy and order 1 one has the Hadamard product, i.e. the zero geometry of Prop 11.1. The classification therefore stands.
- **(ii) Line positivity: CONFIRMED.** On the line R = Π_±(x² + δ²)/(x² + 4δ²) > 0. Note that the line identity Re ζ′/ζ = −½m holds for ANY
  FE-symmetric function real on the line, so (ii) adds nothing beyond (i).
- **(iii) Moments: CONFIRMED.** ∫log((x²+4δ²)/(x²+δ²))dx = 2π(2δ − δ), so the total is 4πδ ✓. The range of log|R| is [−2log 4, 0] ✓.
  1 − R^{2k} ≤ 2k·3δ²/(x²+4δ²) gives O_k(δ)·sup|ζ|^{2k} ✓.
- **(iv) Curvature: CONFIRMED, 3/(2δ²).** ∂²log(x²+a²) at 0 is 2/a², so 2/δ² − 2/(4δ²) = 3/(2δ²). The partner factor contributes O(δ²/γ₀⁴) ✓.
  ℓ̃′ − ℓ′ = O(δ²) at γ₀ (odd part), so X̃ − X = F̂₀²·3/(2δ²) + O(1) ✓.
- **FIX (wording).** "ℛ₁ does not involve ℓ" is not the right justification. ℛ₁ contains ζ′/ζ(3/2 + iγ₀), which changes by R′/R(3/2 + iγ₀) =
  [1/(1−δ) + 1/(1+δ) − 1/(1−2δ) − 1/(1+2δ)] + … = O(δ²). The conclusion is unchanged.
- **Verdict:** NO-GO for 𝓜 is CONFIRMED, with the class restated as above. Novelty: the model is DH-type. The new parts are the exact
  line-positivity and the 3/(2δ²) count.

## NT_012 (width √(T₀ log(1/T₀)))
- **Cited local formula: CONFIRMED with a FIX to the citation.** Titchmarsh Thm 9.6(A)/(B) gives log ζ(s) = Σ_{|t−γ|≤1} log(s − ρ) + O(log t)
  for −1 ≤ σ ≤ 2. NT_012's window |γ − t| ≤ 2 with |u − t| ≤ 1 is a harmless enlargement. Cite (B), not "integration of (A)".
- **Arithmetic: CONFIRMED.** w² ≳ T₀·log t·log(2/w)/a₀ with log t ≍ a₀ ≍ log(1/T₀), so w ≍ √(T₀ log(1/T₀)) ✓.
- **Prop 12.2: DOWNGRADE to ARGUED/heuristic.**
  - Its first sentence is an order-of-magnitude model, not a proof.
  - Its second sentence ("by NT_011 no 𝓜-argument reaches width → 0") does NOT follow from Thm 11.2. One off-line pair at scale δ changes
    ∫Xφ by O(δT₀/w²)·‖φ‖_∞ only, which is negligible against a₀w for δ ≪ w³. Excluding windows of width w → 0 needs a family of pairs at
    density ≈ 1/w. This is plausible but not written.
- **Status:** Thm 12.1 CONFIRMED. It improves NT_009's (T₀log)^{1/3}. Mechanism: archimedean dominance.

## NT_013 (part (b))
- **Prop 13.1: CONFIRMED.**
- **Thm 13.2 (σ-collapse): CONFIRMED for σ > 3/2, and the threshold is sharp for absolute convergence.** g(j) ≤ j^{σ−½}log j. There are ≍ T₀j
  values of m ≈ j, which gives Σ_j T₀ j^{½−σ}log j < ∞ ⟺ σ > 3/2.
- **Prop 13.3: CONFIRMED.** Chebyshev/dlVP give only ϑ = ½ ✓.
- **§3: ARGUED, CONFIRMED as labelled.** Recommendation (FIX): delete the sentence "Under D it holds (NT_005 Prop 5.5)". It is unnecessary
  for (b). Keeping it next to NT_014 invites an unwritten chaining that is excluded by convention. Keep the memos unchained.
- **Prop 13.5: DOWNGRADE PROVED → ARGUED.** The falsifier comb is only sketched. The lower bound Σ_r|K(r)|H^{−σ} ≥ c∫e^{(3/2−σ)u}E|cos u| needs
  |K(r)| to inherit |Ξ| shell-wise, i.e. no signed cancellation among the near-coincidence pairs defining K(r), and that is not shown. The class
  statement is very plausible, but "PROVED (sketch)" is not an honest label.

## NT_014 (b) and zero-free strips
- **Thm 14.1 (forward): CONFIRMED.** ĉ₀ = F̂₀² = O(τ^{−4}) with N(T) ≪ T log T gives absolute convergence of the ρ-sum. The ε is in fact
  unnecessary: |Ξ| ≪ e^{ϑ|u|}. FIX the wording: "main term killed by Tate" should read "pole term subtracted by definition of Ξ".
- **Prop 14.2 (converse): ARGUED, CONFIRMED as labelled, with two FIXes.**
  1. The statement is garbled ("½ < Re ρ − … precisely with"). Restate: if (b) holds on (σ′, 3/2) and the continuous versions are
     real-analytic in σ, then there is no zero with Re ρ ∈ (σ′ − ½, 1) outside the exceptional ordinates {Im F̂₀(z_ρ)² = 0}.
  2. The location of the zeros of F̂₀² (±i/2 and |Im z| = b > ½) holds for the L2_025 profile. It must be cited as such (the "fixed narrow
     profile" must be that one).
- **The Conclusion "⟺": FIX.**
  - The converse carries the extra hypothesis of σ-analyticity of the continuous versions, and an exceptional set.
  - Correct form: (b) on (1+ϑ, 3/2] ⟸ zero-free half-plane (PROVED). (b) + σ-analyticity ⟹ zero-free half-plane off the exceptional set
    (ARGUED).
  - The NO-GO "(b) has no zero-free mechanism" is therefore NO-GO (ARGUED). It is consistent with Paper 47 cor:void (𝒞_zeros class).

## NT_SYNTHESIS
- **Item 8:** fine. Mark NT_012 as refereed (Thm 12.1 CONFIRMED; Prop 12.2 ARGUED).
- **§3, first bullet: FIX.** "referee concurs" refers to NT_008_010 review §NT_009 (zero geometry), not to the ζ̃ model. Add the holomorphy
  clause of 𝓜.
- **§3, second bullet: FIX.** Replace "⟺" by the one-way PROVED plus ARGUED-converse form above. Change "NO-GO" to "NO-GO (ARGUED)". Change
  "absolute methods excluded" to ARGUED.
- **§4 assessment: DOWNGRADE to HEURISTIC (a reading, not a theorem).**
  - "Every proved positivity is archimedean dominance" is accurate for NT_009/012 and the ζ-tests. For the base theorem (NT_002) it is
    absolute summability, i.e. class-level dominance. Acceptable as a reading.
  - "Both open parts reduce to zero information except via the Euler product on the line" is inaccurate for (b).
    - NT_014's argument (ARGUED) says ANY proof of (b) yields zero-free information, whatever the method. So the "Euler-product exception"
      does not apply to (b).
    - For pointwise (𝒱), the exception list must also include "holomorphy plus order 1 used jointly", which leads back to Prop 11.1.
  - Correct text: pointwise (𝒱) escapes 𝓜 only via inputs that ζ̃ lacks, namely the Euler product or holomorphy plus order 1 (the latter
    being zero geometry). Part (b) is zero-free information by NT_014 (ARGUED).
- **Target E as stated: FIX (precision).**
  1. τ₀ must not be an ordinate, or the inequality must be read in the limit. X → −∞ at on-line zeros, so the statement is trivially true
     there.
  2. Quantify T₀: one fixed T₀ ≤ T*, or every T₀ ≤ T*.
  3. Say whether the inequality is strict.
  4. ℛ₁ must be the full remainder of NT_008, not its leading terms.

## Target E route — verdict: EXCLUDED as stated (NO-GO by earlier work + an internal inconsistency)
1. **The inconsistency.** At σ slightly above 1, w = σ − ½ + iτ₀ has Re w slightly above ½, NOT > 1. ζ′/ζ(w) = −ΣΛ(n)n^{−w} converges
   absolutely only for σ > 3/2. The "convergent Euler-product object" exists only in the absolute region of the base theorem.
2. **Part (b) is in the way.** Transport from σ > 3/2 to σ = 1 must cross (1, 3/2]. Continuity of the symbol there is part (b), which NT_014
   (forward PROVED; converse ARGUED) places in the zero-free-information class excluded as a mechanism by cor:void. This is the same verdict as
   L2_BUILD_026 §3: the σ-transport difference is a residue sum at zeros right of σ.
3. **The FE-odd factor carries no information.** ζ′/ζ(w) − ζ′/ζ(1−w) is odd under σ ↦ 2 − σ. Reflection through it is the L2_BUILD_026 §1
   antisymmetry (D_{1−σ} = −D_σ): symmetrization is void (PROVED NO-GO). At σ = 1 the odd factor vanishes to first order, and the σ-derivative
   only returns X (NT_010). So no inequality is transported, only the identity.
4. **Conjugation does not help.** L2_BUILD_027: a deformed problem is not conjugate to the original one, so there is no conjugacy shortcut.

Remaining door, stated precisely: an inequality at σ = 1 itself (or uniformly on (1, 1+ε)) that uses multiplicativity of ζ on the line, i.e. a
property false for ζ̃ and for Epstein/DH series, and that is not a zero-free statement. Status: OPEN, with no candidate input identified.

## Summary
- CONFIRMED: Prop 11.1; Thm 11.2 (with the class restated); Thm 12.1; Thm 13.2; Prop 13.3; Thm 14.1.
- DOWNGRADE: Prop 12.2 → ARGUED; Prop 13.5 → ARGUED; NT_014 "⟺" → one-way + ARGUED converse; synthesis §4 → HEURISTIC.
- FIX: 7 (𝓜 holomorphy clause, ℛ₁ wording, Titchmarsh 9.6(B), the "Under D" sentence, the Prop 14.2 statement, the profile citation,
  Target E quantifiers).
- Target E route (σ-transport through the FE-odd factor): EXCLUDED by L2_026/027 + NT_014 + cor:void.
- No sign contact. Row D: OPEN.
