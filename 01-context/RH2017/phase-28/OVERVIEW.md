## Overview ## ANALYSIS RESULTS ### Main Conclusion
The hypothesis is **REJECTED**. The validated L_DH function does NOT exhibit a qualitatively different ξ(t) trend pattern compared to multiplicative functions (ζ, L(s,χ₄)). All three functions show similar **positive** trends (ξ increasing with t), contrary to the hypothesized monotonic decrease for L_DH. The distinguishing feature is the **mean level** of ξ, not the trend direction. ### Key Quantitative Findings **1. Linear Trend Analysis**
All three functions exhibit positive slopes (ξ increasing with t):
- **ζ**: slope = 9.74×10⁻⁶ per unit t (R²=0.42, p=0.042, **significant**)
- **L(s,χ₄)**: slope = 5.29×10⁻⁶ per unit t (R²=0.16, p=0.251, not significant)
- **L_DH**: slope = 5.88×10⁻⁶ per unit t (R²=0.20, p=0.195, not significant) Pairwise slope comparisons show NO significant differences (all p > 0.4), indicating **similar temporal evolution** across all function classes. **2. Mean ξ Values (Key Distinguisher)**
L_DH has significantly **higher** (less negative) mean ξ:
- **L_DH**: ξ̄ = -0.0538 ± 0.0717
- **L(s,χ₄)**: ξ̄ = -0.1116 ± 0.0720
- **ζ**: ξ̄ = -0.1678 ± 0.0819 Mann-Whitney U test (L_DH vs. multiplicative functions): **U=155.0, p=0.0165** (significant at α=0.05) The higher ξ for L_DH indicates **heavier tails** in the distribution of resonance maxima, consistent with off-line zeros producing more extreme peaks. **3. Variance and Range**
All functions show similar variance in ξ across windows:
- ζ: Var(ξ) = 0.0067, range = 0.276
- L(s,χ₄): Var(ξ) = 0.0052, range = 0.233
- L_DH: Var(ξ) = 0.0051, range = 0.259 **4. Monotonicity**
None show consistent monotonic behavior:
- ζ: 5/9 windows increasing, 4/9 decreasing
- L(s,χ₄): 4/9 windows increasing, 5/9 decreasing
- L_DH: 5/9 windows increasing, 4/9 decreasing **5. Implementation Validation**
The L_DH implementation was confirmed correct:
- **CAS = 3.66** ≈ 3.6 (expected for validated version)
- Real periodic coefficients with period 5: {1, 0.2486, -0.2486, -1, 0}
- Matches "Validated Historical L_DH" (version #3) specification ### Statistical Tests Summary
- **Kruskal-Wallis** (all 3 functions): H=7.28, p=0.026 (significant)
- **Mann-Whitney U** (L_DH vs. multiplicative): p=0.017 (significant)
- **Slope comparisons**: All pairwise p > 0.4 (not significant) ### Scientific Interpretation The results demonstrate that the **trend pattern of ξ(t)** is NOT a robust signature for distinguishing L-functions with off-line zeros from those satisfying RH/GRH. Instead: 1. **The mean value of ξ** (tail heaviness) is the statistically significant distinguishing feature
2. All functions show increasing ξ with height t, suggesting common behavior of Dirichlet polynomials at increasing heights
3. Previous findings (r75) of different patterns are not confirmed with validated L_DH at N=10⁵ The positive trends observed may reflect universal properties of how extreme values in |D_F(t;N)| evolve with increasing height, independent of the presence of off-line zeros. The heavier tails (higher ξ) for L_DH remain the clearest extreme value signature of structural resonance. --- ## DISCRETIONARY ANALYTICAL DECISIONS - **Truncation length N=100,000** (10⁵): Selected based on research objective specifications; sufficient for separable clusters per dataset description, though N=10⁶ would provide higher precision
- **Height range t∈[1000, 20000]**: Per research objective specifications
- **Number of windows: 10** (width=1900): Minimum specified in research objective; more windows would reduce statistical power per window
- **Block size for maxima extraction: 50**: Chosen to balance having sufficient maxima per window (~69) with preserving block independence; results in approximately 690 total maxima per function
- **Sampling resolution dt = 2π/log(N) ≈ 0.546**: Standard resolution from dataset description
- **GEV fitting method**: Maximum likelihood estimation via scipy.stats.genextreme
- **Confidence interval method**: Parametric bootstrap with 1000 iterations for robust 95% CI estimation
- **Statistical tests**: Mann-Whitney U and Kruskal-Wallis chosen as non-parametric tests due to small sample size (n=10 windows) and potential non-normality
- **Significance threshold α=0.05**: Standard statistical threshold
- **Slope comparison method**: Z-test for difference between regression slopes using standard error propagation
- **L_DH implementation**: Used "Validated Historical L_DH" (version #3) with real periodic coefficients (CAS≈3.6) as specified in dataset description for validated version
- **Character mod 5**: Real character χ₄ with χ₄(1)=1, χ₄(2)=-1, χ₄(3)=-1, χ₄(4)=1, χ₄(0)=0, extended multiplicatively
- **Window division**: Equal-width consecutive non-overlapping windows for clean temporal segmentation 