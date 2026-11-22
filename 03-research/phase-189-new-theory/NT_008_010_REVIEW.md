# NT_008–010: referee report

Independent referee, working by hand only (no numerics beyond standard constants). The report
does not invoke or reason from any equivalence involving row D. Verdicts: CONFIRMED / FIX / DOWNGRADE.

## NT_008: the discreteness remainder ℛ₁
- **Thm 8.1 at σ = 1: CONFIRMED (with FIX on the proof constants).**
  - Sparse scales (L ≤ 1/(10T₀)): the window has length ≤ 5T₀L < 1, so it contains only L ✓. The diagonal k^{−s̄}(kn)^{−s} = k^{−2σ}n^{−s} with the
    comb weight v_n ∝ Λ(n)n^{−½} gives ζ(2σ)·2ΣΛ(n)n^{−σ−½−iτ₀} = 2ζ(2σ)(−ζ′/ζ)(σ+½+iτ₀) ✓. The truncation tail of the double sum,
    Σ_k k^{−2}Σ_{n>N/k}Λ(n)n^{−3/2} ≪ N^{−½}, is O(√T₀) ✓.
  - **FIX (A off-diagonal):** the line "≤ C₀T₀k^{2−σ}·(k^{−1})" is unjustified. With 1/d ≤ k/j for m = k ± j, the correct estimate is
    8T₀k·Σ_j j^{−1}e^{−5j/(2k)}·k^{−σ} ≪ T₀k^{1−σ}log(k+1). Weighted by k^{−σ} and summed over k ≤ 1/(10T₀), this gives O(T₀log²(1/T₀)), which is
    still inside the stated error. The conclusion is unaffected.
  - EM scales: (5T₀L)·L^{−σ−2}(C/T₀)² = O(C²L^{−σ−1}/T₀). Weighted by L^{−½}log L and summed from 10/T₀, this is O(C²√T₀ log) ✓. The transition band is ✓.
  - **FIX (uniform-σ clause):** the sentence "up to a T₀^{¼}-loss absorbed in K… stated with √T₀" contradicts itself. Restate it as
    ℛ_σ = a₀ − 2Re(−ζ′/ζ)(σ+½+iτ₀) + O_C(T₀^{¼}log(1/T₀)) for |σ−1| ≤ ¼, or delete it. NT_010's ARGUED bound only needs o(1), so it survives
    either way.
- **Constant: CONFIRMED.** Re(−ζ′/ζ)(3/2+it) = ΣΛ(n)n^{−3/2}cos(t log n). Its absolute value is ≤ ΣΛ(n)n^{−3/2} = −ζ′/ζ(3/2) = 1.5052…,
  with equality only at t = 0 (cos(t log 2) = 1 and cos(t log 3) = 1 cannot both hold for t ≠ 0). So −2Re(·) ∈ [−3.0104, 3.0104], the
  maximum of |·| is at t = 0, and ℛ₁ ≥ a₀ − 3.02 is correct with o(1) slack.
- **Integrality bookkeeping: CONFIRMED.** ℤ enters only through the sparse scales L ≲ 1/T₀, where the window sees ≤ 1 integer, and through the
  exact diagonal m = k. Above 10/T₀ the comb behaves like Lebesgue measure up to EM errors. The "3/2 shift" comes from H(n)^{−1}·n^{−½}, which
  is bookkeeping and not a new mechanism.
- Restriction |τ₀| ≤ C/T₀: honestly flagged ✓.

## NT_009: (𝒱) at resolution
- **§1 sizes: CONFIRMED.**
- **CITED bound: FIX (source).** Name the exact source. Titchmarsh (2nd ed., Heath-Brown) Thm 9.6(A) gives
  ζ′/ζ(s) = Σ_{|t−γ|<1}(s−ρ)^{−1} + O(log t) for −1 ≤ σ ≤ 2. Integrating in σ from 2 down to ½ (Titchmarsh §9.6, the step leading to Thm 9.6(B)) gives
  log|ζ(½+iu)| = Σ_{|u−γ|<1}log|½+iu−ρ| + O(log u).
  With N(t+1) − N(t) ≪ log t (Thm 9.2) and ∫_I|log|u−γ||du ≪ 1 per zero, this yields ∫_t^{t+w}|log|ζ(½+iu)||du ≪ log t for w ≤ 1, which is the
  form used. The bound uses zero counting only, not zero location. The phrase "Jensen in discs" is acceptable but imprecise.
- **Thm 9.1: CONFIRMED with a FIX on the reading.**
  - The integration by parts is correct: ∫(F̂₀²ℓ′)′φ = −∫F̂₀²ℓ′φ′ = ∫ℓ(F̂₀²φ′)′.
  - The constants are correct: ‖(F̂₀²φ′)′‖ ≤ (8T₀²/w + 32T₀/w²)‖φ‖_∞. The ratio is ≤ 128K·T₀log(1/T₀)/(ζ(2)w³). So w₀ ∝ (T₀log(1/T₀)/a₀)^{1/3}.
    The stated w₀ holds and is slightly conservative.
  - **FIX:** the object bounded is the *finite-part* distribution. Its distributional ℓ″ near an on-line zero is −fp(τ−γ)^{−2}, not the pointwise
    function. So Thm 9.1 is a statement about the regularised pairing, and it does not imply anything pointwise. The own-review already
    says this, but the theorem statement must carry it.
  - Mechanism: archimedean dominance plus a mean value of log|ζ|. Labels: PROVED for the weak form, CITED input. Honest.
- **Point 2, the pointwise reduction: DOWNGRADE of the §3 framing. Verdict below.**
  By Hadamard, ℓ(τ) = Σ_ρ log|½+iτ−ρ| + (smooth archimedean term, with second derivative O(1/|τ|)), with the usual pairing for convergence. Hence
    ℓ″(τ) = Σ_ρ (δ_ρ² − y_ρ²)/(δ_ρ² + y_ρ²)² + O(1/|τ|),   δ_ρ = β−½,  y_ρ = τ−γ.
  - On-line zeros contribute −1/y² < 0.
  - An off-line zero contributes a positive term when |y| < |δ|, with peak 1/δ² at τ = γ.
  - At τ = γ for an isolated off-line pair, ℓ′(γ) ≈ 0 by symmetry, and the neighbours (spacing ≍ 1/log γ) contribute ≍ −log²γ.
  So X(γ) ≈ F̂₀(γ)²(δ^{−2} − O(log²γ)), and (𝒱) fails at γ as soon as F̂₀(γ)²/δ² ≳ ζ(2)(a₀ + 3).
  - **Precise verdict.** Pointwise (𝒱) on |τ₀| ≤ C/T₀, and not just Prop 9.2's sufficient condition, is intrinsically a statement about zero
    geometry. Up to the bounded remainder ℛ₁ ∈ [a₀−3.02, a₀+3.02], it is equivalent to a quantitative local exclusion: no zero ρ with
    |γ| ≲ C/T₀ and 0 < |β−½| ≲ |F̂₀(γ)|/√(ζ(2)a₀) that is not compensated by nearby on-line zeros.
    The partial-fraction formula is an identity, so this is not avoidable bookkeeping. Every true upper bound on ℓ″ at this scale *is* such an
    exclusion. Mean values (Thm 9.1) cannot see it, because a single off-line pair changes ∫_I|ℓ| by O(δ·log(1/δ)) only.
    Therefore pointwise (𝒱) cannot follow "from identities and mean values alone". It lies in the zero-configuration class of Paper 46 cor:void
    (𝒞_zeros, i.e. statements decided by the zero configuration), or in its exact analogue for the curve symbol.
    NT_009 §3's "OPEN, exactly where positivity at σ = 1 would have to be decided" should be rewritten as **OPEN; reformulated as a
    local zero-exclusion statement in 𝒞_zeros. The identity/mean-value class is NO-GO by the Hadamard computation above.**
  - Also correct the sentence "not used". The D/RH equivalence is not invoked. This does not forbid
    computing the Hadamard partial fractions. Using them is legitimate and is exactly what classifies the obstruction.

## NT_010: σ-derivative at σ = 1
- **Oddness ⇒ G″(1) = 0: CONFIRMED.** Even-order derivatives of an odd real-analytic function vanish.
- **V₁: CONFIRMED.**
  (1/(2ε) + γ)(1/ζ(2) − 2εζ′(2)/ζ(2)²)(G′ε + O(ε³)) = G′/(2ζ(2)) + ε(G′/ζ(2))(γ − ζ′/ζ(2)) + O(ε²).
  With G′ = −2X this gives V = Reℛ₁ − X/ζ(2) and V₁ = −(2/ζ(2))(γ − ζ′/ζ(2))X + Re∂_σℛ.
  Constants: ζ′(2) = −0.93755, ζ(2) = 1.64493, so ζ′/ζ(2) = −0.56996 ✓ and γ − ζ′/ζ(2) = 1.14718 ✓.
- **∂_σℛ bound: CONFIRMED as ARGUED.**
  - d/dσ[−2Re(−ζ′/ζ)(σ+½+iτ₀)] = 2Re(ζ′/ζ)′(3/2+iτ₀), and (ζ′/ζ)′(s) = ΣΛ(n)log n·n^{−s}, so the bound |·| ≤ 2κ holds ✓.
  - k^{−s̄} = k^{−σ}k^{iτ₀} is entire in complex σ for fixed real τ₀, so the Cauchy-disc argument is legitimate.
  - It still depends on the uniform-σ clause of NT_008, which needs the FIX above. Only o(1) is needed.
- **Cor 10.2: CONFIRMED as an implication. FIX the label to CONDITIONAL (on D, plus the ARGUED bound).**
  - The V < 0 case is excluded by continuity alone. The V = 0 case is excluded by V₁ ≤ −2.294(a₀−3.02) + 2κ + o(1) < 0 for a₀ large ✓.
  - Point-dependence: O_{τ₀}(ε²) is enough because the argument is pointwise.
- **Prop 10.3: FIX.**
  - The first-order inequality X(1 + 2.294ε) ≤ ζ(2)(Reℛ₁ + ε∂ℛ) is correct.
  - The comparison clause is wrong. The admissible X-threshold at 1+ε is ζ(2)(Reℛ₁ + ε∂ℛ)/(1 + 2.294ε). It is lower than the threshold at
    σ = 1 iff ∂ℛ < 2.294·Reℛ₁. That condition does not involve X, and it holds on the whole spectral range for a₀ large.
  - What depends on X is the sign of ∂_σΦ: V₁ < 0 iff X > ζ(2)Re∂ℛ/2.294. Restate it this way.
  - "Hardest inside (1, σ₁)" is DOWNGRADE to heuristic, because the ε² term is non-uniform in τ₀.
- **Prop 10.4: CONFIRMED.** Approximate identity on 𝕋^∞ ✓, and (iii) ⟹ (ii) by uniform continuity on a compact group ✓. The target is OPEN.

## Novelty
- NT_008: routine Euler–Maclaurin and sparse splitting. The identification "remainder = a₀ − 2Re(−ζ′/ζ)(3/2+iτ₀)" is new to the corpus but
  mathematically elementary.
- NT_009 Thm 9.1: new to the corpus, standard in technique (Titchmarsh §9.6 mean values plus archimedean dominance). It is low-value: the
  regularised pairing hides exactly the zero-geometric content.
- NT_010: the Laurent bookkeeping is elementary. The useful new content is Cor 10.2 (strictness under D) and the corrected Prop 10.3.

## Summary
The core identities are CONFIRMED. There are 5 FIXes: the A off-diagonal log factor, the uniform-σ clause, the citation source and the
finite-part reading, the Cor 10.2 label, and the Prop 10.3 comparison. There is 1 DOWNGRADE: NT_009 §3's framing, because pointwise (𝒱) is a
local zero-exclusion statement (𝒞_zeros), and the identity/mean-value class is NO-GO. No sign contact.
