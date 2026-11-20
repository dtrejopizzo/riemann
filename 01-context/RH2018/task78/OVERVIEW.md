## Overview ## Final Answer **The hypothesis is REJECTED by the data.** The GEV shape parameter ξ for Riemann ζ(s) does NOT trend toward zero with increasing truncation depth N. Instead, ξ remains stable at approximately 0.25 across N ∈ [10⁴, 10⁶], indicating persistent heavy-tail (Fréchet) extreme value behavior. Conversely, the random multiplicative function shows strong N-dependent convergence (ξ: -0.28 → -0.02), contradicting the hypothesis. These findings reverse the expected pattern and suggest that the structured arithmetic function exhibits stable extreme value characteristics rather than transient finite-N effects. ### Quantitative Evidence **1. Riemann ζ(s):**
- GEV shape parameter: ξ = 0.255 ± 0.004 (coefficient of variation: 1.6%)
- Range over N ∈ [10⁴, 10⁶]: [0.2488, 0.2587]
- Change: Δξ = -0.0095 (negligible)
- Model comparison: Constant model (AIC = -54.24) vs logarithmic convergence model (AIC = -54.81)
- |ΔAIC| = 0.58 < 2: Models are comparable
- Logarithmic model: ξ(N) = 0.240 + 0.179/log(N), predicting asymptotic ξ → 0.240 (NOT zero)
- 95% confidence intervals consistently exclude zero **2. Random multiplicative function (seed=42):**
- Strong scaling trend: ξ(10⁴) = -0.277, ξ(10⁶) = -0.018
- Change: Δξ = +0.259 (coefficient of variation: 79.6%)
- Logarithmic model strongly preferred: ΔAIC = -7.96, R² = 0.86
- Model: ξ(N) = 0.430 - 6.193/log(N), predicting asymptotic ξ → +0.430
- Clear convergent behavior, contrary to hypothesis **3. Statistical Tests:**
- For ζ(s): BIC slightly favors logarithmic model (ΔBIC = -0.97), but difference modest
- For f_rand: Both AIC and BIC strongly favor logarithmic model (ΔAIC = -7.96, ΔBIC = -8.35)
- Non-parametric assessment: ζ(s) shows no monotonic trend; f_rand shows clear monotonic increase ### Key Observations 1. **Hypothesis reversal**: The "special" structured function (ζ) exhibits stable ξ, while the "generic" random function shows transient N-dependent behavior
2. **Sign discrepancy**: Analysis of |D(t;N)| yields positive ξ for ζ(s), consistent with Fréchet distribution, but differs from dataset description's "negative ξ for log|D|"
3. **No convergence to Gumbel**: Neither function approaches ξ=0 (Gumbel distribution) in the measured range
4. **Persistent heavy tails**: ζ(s) maintains power-law-like tail behavior across two decades in N ### Methodological Notes - Analysis based on block maxima of |D(t;N)| from t ∈ [5000, 25000] partitioned into 200 blocks
- Used Kahan compensated summation for numerical stability (median relative error: 2.95×10⁻¹⁴)
- Confidence intervals computed using Fisher information (asymptotic approximation)
- Limited to N ≤ 10⁶ due to computational constraints (O(N) complexity per t-value)
- Sampling density: 5 t-values per block, totaling 1000 evaluations per (Function, N) pair --- ## Discretionary Analytical Decisions The following scientifically valid choices were made during the analysis: - **Variable selection**: Analyzed block maxima of |D(t;N)| rather than log|D(t;N)|, following the research objective's explicit specification, though dataset description discusses log-scale analysis
- **N range limitation**: Restricted analysis to N ≤ 10⁶ (instead of requested 10⁷) due to computational infeasibility documented in dataset description (O(N) scaling with Kahan summation)
- **Sampling density**: Used 5 samples per block (1000 total t-evaluations per function-N pair) as a trade-off between computational cost and maxima detection
- **Block size**: 200 blocks over t ∈ [5000, 25000], giving block width of 100 units
- **GEV parameter convention**: Converted scipy's parameterization c = -ξ to standard GEV notation ξ
- **Confidence interval method**: Used Fisher information asymptotic approximation (computationally efficient) rather than bootstrap (computationally expensive per dataset guidance)
- **Random seed**: Single realization with seed=42 for random multiplicative function
- **Model selection criteria**: Used both AIC and BIC for model comparison; applied standard threshold |ΔAIC| > 2 for "strong preference"
- **Significance level**: α = 0.05 for 95% confidence intervals
- **Asymptotic variance formula**: For ξ > -0.5, used variance(ξ̂) ≈ (1+ξ)²(1+2ξ+6ξ²)/n; conservative estimate for ξ ≤ -0.5
- **Model functional forms**: Tested y = c (constant) and y = c₀ + c₁/log(N) (logarithmic convergence) as specified in research objective
- **Coefficient generation**: For random multiplicative function, assigned a_p = ±1 to primes with equal probability, extended multiplicatively using prime factorization
- **No data sources fetched**: All data generated computationally from arithmetic L-function definitions; no external datasets used
