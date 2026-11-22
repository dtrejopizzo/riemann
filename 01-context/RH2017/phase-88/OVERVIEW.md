## Overview # GEV Analysis of L(χ₄) and L_DH^(ε=0.01): Complete Classification ## Summary The hypothesis was **partially confirmed**. L(χ₄) exhibits bounded-tail behavior similar to ζ (ξ = -0.2150, 95% CI: [-0.3719, -0.1139]), with no significant statistical difference (p = 0.3220). However, L_DH^(ε=0.01) shows intermediate behavior (ξ = -0.0827, 95% CI: [-0.3240, 0.0511]), not the heavy-tailed behavior predicted. The perturbed L_DH function is statistically indistinguishable from the baseline L_DH (p = 0.6100), indicating that small perturbations (ε = 0.01) do not alter extreme value behavior. ## Key Findings ### 1. L(χ₄) Classification
- **ξ = -0.2150** with 95% CI [-0.3719, -0.1139]
- **Bounded-tail behavior** (Weibull domain): entire CI is negative
- **KS test p-value = 0.8675**: excellent fit to GEV distribution
- **No significant difference from ζ** (p = 0.3220): both structured multiplicative functions show similar extreme value behavior
- **Highly significant difference from f_rand** (p < 0.0001): random multiplicative functions behave differently ### 2. L_DH and L_DH^(ε=0.01) Classification
- **L_DH**: ξ = -0.0834, 95% CI [-0.3259, 0.0507]
- **L_DH^(ε=0.01)**: ξ = -0.0827, 95% CI [-0.3240, 0.0511]
- **No significant difference** between perturbed and baseline (p = 0.6100)
- **Intermediate behavior**: CIs span from bounded to light-tailed regimes
- **No significant difference from ζ or L(χ₄)**: wide CIs result in overlap ### 3. Complete Function Classification | Function | Type | ξ | 95% CI | Tail Behavior |
|----------|------|---|--------|---------------|
| ζ | Multiplicative | -0.1365 | [-0.2635, 0.0153] | Bounded/Gumbel |
| L(χ₄) | Multiplicative | -0.2150 | [-0.3719, -0.1139] | Bounded |
| f_rand | Multiplicative | 0.2087 | [0.0274, 0.3559] | Heavy-tailed |
| L_DH | Non-multiplicative | -0.0834 | [-0.3259, 0.0507] | Intermediate |
| L_DH^(ε=0.01) | Non-multiplicative | -0.0827 | [-0.3240, 0.0511] | Intermediate | ## Critical Insights 1. **Multiplicativity does not determine tail behavior**: The multiplicative functions span from bounded-tail (ζ, L(χ₄)) to heavy-tailed (f_rand), demonstrating that arithmetic structure matters more than multiplicative structure alone. 2. **Structured vs random multiplicative functions diverge**: ζ and L(χ₄) (Dirichlet L-functions with specific arithmetic properties) cluster together with ξ ≤ 0, while f_rand (random multiplicative coefficients) has ξ > 0. 3. **Non-multiplicative functions show uncertainty**: Both L_DH variants have wide confidence intervals spanning negative to positive ξ values, occupying an intermediate regime that overlaps with both bounded and light-tailed distributions. 4. **Perturbations preserve extreme value behavior**: The ε = 0.01 perturbation to L_DH produces virtually identical GEV parameters (Δξ = 0.0007, p = 0.61), indicating that small coefficient changes do not fundamentally alter tail behavior. 5. **No simple multiplicative/non-multiplicative dichotomy**: The hypothesis that multiplicative and non-multiplicative functions form distinct GEV classes is not supported. Instead, we observe three regimes: - **Bounded/Gumbel** (ξ ≤ 0): ζ, L(χ₄), L_DH variants - **Intermediate** (CI spans 0): L_DH variants - **Heavy-tailed** (ξ > 0): f_rand ## Statistical Robustness All GEV fits passed goodness-of-fit tests (KS p-values > 0.47), indicating excellent model fit. Bootstrap confidence intervals (1000 samples) provide robust uncertainty quantification. The computational implementation used corrected squarefree constraints for L_DH variants, ensuring validity of non-multiplicative structure. ## Discretionary Decisions - **Statistical test selection**: Used bootstrap permutation tests rather than parametric tests due to unknown distribution of Δξ under the null hypothesis
- **Significance threshold**: Set α = 0.05 for hypothesis testing
- **GEV fitting method**: Used scipy.stats.genextreme MLE implementation after initial custom implementation showed convergence issues
- **Bootstrap sample size**: n = 1000 (sufficient for stable 95% CI estimation)
- **Block maxima extraction**: Used 100 blocks matching existing analysis parameters
- **Perturbation magnitude**: ε = 0.01 as specified in research objective
- **Squarefree implementation**: Applied corrected constraint (μ(n) ≠ 0) for L_DH and perturbed variant
- **Random seeds**: seed=42 for L_DH base coefficients, seed=1042 for perturbations (to ensure independence)
- **CI estimation method**: Percentile bootstrap method (2.5th and 97.5th percentiles) 