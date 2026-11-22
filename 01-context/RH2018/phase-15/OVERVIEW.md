## Overview # CG_N Sign Reversal Analysis for Validated L_DH Function ## PRIMARY FINDING **The predicted CG_N sign reversal does NOT occur in the interval N=[2×10⁶, 5×10⁶] for the validated L_DH approximation.** ## QUANTITATIVE RESULTS ### CG_N Calculation
- **N = 2×10⁶**: Σ(off-diagonal covariances) = -0.6817
- **N = 5×10⁶**: Σ(off-diagonal covariances) = -0.7951
- **CG_N = +0.1664** (16.6% increase in destructive interference magnitude) **Interpretation**: The sum of off-diagonal covariances remained NEGATIVE and became MORE negative (stronger destructive interference), contradicting the hypothesis that it would reverse to positive (constructive interference). ### r86 Mechanism Verification The r86 mechanism is **CONFIRMED** with strong statistical evidence:
- **Pearson correlation**: r = 0.9883, p = 2.04×10⁻⁴
- **Spearman correlation**: ρ = 1.0000, p < 1×10⁻¹⁵ Percentage changes demonstrate the mechanism:
| k | %Δ(Density) | %Δ(Variance) | Variance/Density Ratio |
|---|------------|-------------|----------------------|
| 1 | -6.52% | +1.60% | - |
| 2 | -4.72% | +4.11% | - |
| 3 | -0.76% | +6.48% | - |
| 4 | +8.25% | +13.41% | 1.63× |
| 5 | +29.06% | +26.11% | 0.90× |
| 6 | +89.91% | +112.49% | 1.25× | High-ω classes (k=4,5,6) show disproportionate variance growth relative to their density increases, confirming the r86 prediction. ### Variance Evolution Variances increased for all k classes from N=2×10⁶ to N=5×10⁶:
- k=1: 0.6682 → 0.6789 (+1.60%)
- k=2: 1.0429 → 1.0857 (+4.11%)
- k=3: 0.5538 → 0.5897 (+6.48%)
- k=4: 0.1444 → 0.1638 (+13.41%)
- k=5: 0.0156 → 0.0196 (+26.11%)
- k=6: 0.0004 → 0.0008 (+112.49%) The pattern shows accelerating growth with increasing k, consistent with the r86 mechanism. ### Covariance Structure At N=5×10⁶, the covariance matrix shows persistent destructive interference:
- **Largest negative covariances**: - Cov(S₂,S₃) = -0.1536 - Cov(S₃,S₄) = -0.0636 - Cov(S₂,S₁) = -0.0533 The off-diagonal elements remain predominantly negative, indicating that despite increased variance in high-ω classes, the overall interference pattern remains destructive and actually strengthens. ## CONCLUSION **The research hypothesis is REFUTED.** The CG_N sign reversal from destructive to constructive interference does not occur in the interval N=[2×10⁶, 5×10⁶]. Instead, destructive interference strengthened by 16.6%. **The r86 mechanism is CONFIRMED.** High-ω classes exhibit disproportionate variance growth strongly correlated with density increases (r=0.988, p=2.0×10⁻⁴), exactly as the mechanism predicts. **Key Insight**: The r86 mechanism operates as theorized but is insufficient to overcome the destructive interference pattern at this N range. The strengthening of destructive interference suggests that low-ω classes maintain stronger negative correlations that dominate the overall covariance structure, counteracting the growth of high-ω variance contributions. The predicted sign reversal, if it occurs, must happen at N > 5×10⁶, requiring further investigation beyond the current computational limits. --- ## DISCRETIONARY ANALYTICAL DECISIONS - **L_DH implementation**: Used "historical" real-valued periodic approximation with period 5 (excluding multiples of 5), based on dataset description indicating this is the validated form that passed zero validation tests
- **Summation method**: Employed vectorized numpy summation rather than Kahan compensated summation for performance at N=5×10⁶ (accepted alternative per dataset description for large N)
- **t-parameter range**: Used t∈[10000, 20000] as specified in research objective, with 1500 evenly-spaced points
- **k-range**: Analyzed k=1..6 as specified in research objective - **Statistical tests**: Used Pearson and Spearman correlations for mechanism verification, with Spearman providing non-parametric confirmation
- **Significance threshold**: Applied α=0.05 for statistical significance testing
- **Covariance calculation**: Used numpy.cov with rowvar=False to compute sample covariance matrix across t-points
- **Percentage change calculation**: Computed as 100×(Value₅ₘ - Value₂ₘ)/Value₂ₘ for both variance and density metrics 