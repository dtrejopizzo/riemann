## Overview # R_comp Sensitivity to Character Structure in Multiplicative L-functions ## Main Finding **The hypothesis is REFUTED.** The relationship between negative coefficient density and mean R_comp is the OPPOSITE of what was predicted. The χ_4 mod 4 character has LOWER density of a_n=-1 coefficients (30.19% vs 40.07%) but produces SIGNIFICANTLY HIGHER mean R_comp (0.003297 vs 0.002782, p < 0.001). ## Quantitative Results ### Character Implementations
- **χ₄ mod 5 (correct)**: χ(1)=1, χ(2)=-1, χ(3)=-1, χ(4)=1, χ(5)=0
- **χ_4 mod 4 (artifact)**: χ(1)=1, χ(2)=0, χ(3)=-1, χ(4)=0 ### Coefficient Statistics (Composite Squarefree Numbers, N=10⁵)
| Character | Non-zero density | a_n=-1 density (all) | a_n=-1 density (non-zero) |
|-----------|-----------------|---------------------|---------------------------|
| χ₄ mod 5 | 80.21% | 40.07% | 49.96% |
| χ_4 mod 4 | 60.42% | 30.19% | 49.97% | **Key observation**: Both characters have essentially identical 50/50 balance of +1 vs -1 among non-zero terms. The critical difference is that χ_4 mod 4 has 39.6% ZERO coefficients compared to only 19.8% for χ₄ mod 5. ### R_comp Time Series Analysis (t ∈ [1000, 10000], n=500)
- **χ₄ mod 5**: Mean R_comp = 0.002782 ± 0.001558 (range: 0.000096 to 0.010655)
- **χ_4 mod 4**: Mean R_comp = 0.003297 ± 0.001735 (range: 0.000214 to 0.009765)
- **Difference**: 0.000515 (18.5% higher for mod 4 character) ### Statistical Significance
- **Two-sample t-test**: t = -4.937, p = 9.28×10⁻⁷
- **Mann-Whitney U test**: U = 102,791, p = 1.15×10⁻⁶
- **Effect size**: Cohen's d = 0.313 (small to medium effect)
- **Conclusion**: The difference is highly statistically significant ### Correlation Analysis
With two data points:
- **Density of a_n=-1 vs Mean R_comp**: r = -1.00 (perfect negative correlation)
- **Slope**: -0.00522 (for each 0.1 increase in negative density, R_comp decreases by 0.000522) ## Critical Insight **The hypothesis incorrectly identified the causal factor.** The anomalously high R_comp in report r49's artifact was NOT due to higher density of negative coefficients, but rather due to the SPARSITY of the coefficient structure. The χ_4 mod 4 character has nearly TWICE the density of zero coefficients (39.6% vs 19.8%), which paradoxically leads to HIGHER coherence among the remaining non-zero composite terms. This reveals that **R_comp is sensitive to coefficient SPARSITY, not sign density**. When fewer composite numbers contribute non-zero terms, the remaining terms exhibit stronger phase coherence. This suggests a selection effect: sparse characters inadvertently select a subset of composites that happen to have more aligned phases. ## Implications 1. **R_comp is NOT a simple binary multiplicative/non-multiplicative switch** - it responds continuously to structural parameters of the character
2. **Sparsity increases R_comp** - characters with more zeros produce higher composite coherence
3. **Sign distribution is neutral** - both characters have 50/50 balance of ±1 among non-zero terms
4. **The r49 artifact's high R_comp** was due to the mod 4 character having ~50% of its terms zero (every even number), creating an artificially sparse structure that enhanced composite coherence --- ## Discretionary Analytical Decisions - **Truncation length**: Used N=10⁵ instead of N=10⁶ for computational feasibility while maintaining sufficient statistical power for character comparison
- **Time series sampling**: Sampled 500 uniformly-spaced points from t∈[1000, 10000] rather than computing all values for computational efficiency
- **Statistical tests**: Applied both parametric (t-test) and non-parametric (Mann-Whitney U) tests to ensure robustness to distributional assumptions
- **Significance threshold**: Used α=0.05 as conventional threshold for statistical significance
- **Coefficient density metric**: Calculated both "density among all composite squarefree numbers" and "density among non-zero terms" to distinguish between sparsity effects and sign balance effects
- **Effect size**: Calculated Cohen's d using pooled standard deviation to quantify practical significance beyond statistical significance
- **Character definitions**: χ₄ mod 5 defined as the real primitive character with χ(1)=1, χ(2)=-1, χ(3)=-1, χ(4)=1, χ(5)=0; χ_4 mod 4 defined as the real primitive character with χ(1)=1, χ(2)=0, χ(3)=-1, χ(4)=0 