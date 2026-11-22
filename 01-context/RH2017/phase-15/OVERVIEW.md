## Overview **ANSWER: Comparative GEV Analysis on R_comp Metric for Multiplicative Functions** The hypothesis that "all multiplicative functions exhibit GEV shape parameter ξ ≤ 0 for R_comp extremes" is **REJECTED**. **Quantitative Results:** 1. **Riemann ζ function**: - ξ = -0.140, 95% CI = [-0.253, -0.014] - CI entirely below 0: strong evidence for bounded tail distribution (Weibull-type) - **Consistent with hypothesis** ✓ 2. **L(χ₄) function** (mod 5 character): - ξ = 0.009, 95% CI = [-0.667, 0.200] - CI includes 0: consistent with ξ ≤ 0 but with high uncertainty (Gumbel-type) - Bootstrap instability observed (51.3% success rate) - Method of Moments fit required (AIC = 20.1 vs 135.9 for MLE) - **Consistent with hypothesis** ✓ (weakly) 3. **f_rand function** (random multiplicative, seed=42): - ξ = 0.213, 95% CI = [0.012, 0.379] - CI entirely above 0: strong evidence for heavy-tailed distribution (Fréchet-type) - **INCONSISTENT with hypothesis** ✗ 4. **L_DH reference** (non-multiplicative, from r47): - ξ ≈ 0.81 (heavy-tailed) **Key Finding:**
The random multiplicative function f_rand exhibits significant heavy-tailed behavior in R_comp extremes (ξ = 0.213), similar in character to (but weaker than) the non-multiplicative L_DH function (ξ ≈ 0.81). This demonstrates that heavy-tailed R_comp signatures are NOT unique to non-multiplicative functions. The critical distinction appears to be:
- **Structured multiplicative functions** (ζ, L(χ₄)): ξ ≤ 0 (bounded or Gumbel-type tails)
- **Random multiplicative functions** (f_rand): ξ > 0 (heavy tails)
- **Non-multiplicative functions** (L_DH): ξ > 0 (heavy tails, more extreme) This suggests that multiplicativity alone does not determine the tail behavior of R_comp extremes. The randomness in coefficient assignment may play a critical role in generating heavy-tailed resonances, independent of multiplicative structure. --- **DISCRETIONARY ANALYTICAL DECISIONS:** • Used N = 10⁵ truncation length (rather than 10⁶) for computational feasibility while maintaining adequate statistical power
• Set t range as [1000, 10000] with 9000 sampling points (Δt ≈ 1.0)
• Used 100 blocks for block maxima extraction (90 points per block)
• Applied 1000 bootstrap resamples for confidence interval estimation
• Set random seed = 42 for reproducibility of random multiplicative function
• Used Maximum Likelihood Estimation (MLE) for GEV fitting for Riemann ζ and f_rand
• Used Method of Moments for GEV fitting for L(χ₄) due to superior fit quality (AIC = 20.1 vs 135.9 for MLE, KS p-value = 0.071 vs 0.000)
• Set significance level α = 0.05 for 95% bootstrap confidence intervals
• Used Kahan compensated summation for numerical precision (target relative error < 10⁻¹⁵)
• Character χ₄ defined mod 5 (as specified): χ₄(n) = 0 if gcd(n,5)≠1, +1 if n≡±1(mod 5), -1 if n≡±2(mod 5)
• Composite squarefree numbers defined as: ω(n) ≥ 2 and μ(n) ≠ 0
• R_comp metric computed as: |Σ_{n comp, squarefree} a_n/n^(1/2+it)| / Σ_{n comp, squarefree} 1/n
• Percentile method used for bootstrap confidence intervals (2.5th and 97.5th percentiles) 