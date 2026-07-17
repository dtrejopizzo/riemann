## Overview ## Summary I successfully generated a controlled parametric dataset using a multiplicative function family F_α (where a_p = +1 with probability α at each prime) to model the relationship between S_k covariance structure and GEV shape parameter ξ. The analysis demonstrates systematic changes in both covariance structure and extreme value statistics as α varies from 0.5 (random multiplicative) to 1.0 (Riemann zeta function). ## Key Quantitative Results **1. GEV Shape Parameter ξ vs α:**
- ξ ranges from -0.4359 (α=0.99) to -0.1586 (α=0.7)
- α=0.5 (random): ξ = -0.1874 [-0.3547, -0.0549]
- α=1.0 (ζ function): ξ = -0.3733 [-0.4926, -0.2539]
- All ξ values are negative (Weibull domain), consistent with dataset description r42 for log|D(t;N)|
- Spearman ρ(α, ξ) = -0.683, p = 0.0424 (significant negative correlation) **2. Covariance Structure Evolution:**
- Mean off-diagonal real part: +0.0082 (α=0.5) → -0.0997 (α=1.0)
- Sum of negative off-diagonal real parts: -0.338 (α=0.5) → -3.128 (α=1.0), a 9.2× increase in anti-correlation magnitude
- Spearman ρ(sum_negative_real_offdiag, ξ) = +0.783, p = 0.0125 (significant: stronger anti-correlations → more negative ξ)
- Mean off-diagonal real part vs ξ: ρ = +0.767, p = 0.0159 (significant) **3. Regression Model Performance:**
- Ridge regression R² (LOOCV) = 0.483, RMSE = 0.066
- Key predictive features (by coefficient magnitude): - C_55 (high-ω variance): +0.223 - sum_negative_real_offdiag: +0.071 - mean_offdiag_real: +0.009
- Model performance is comparable to r40 (R² < 0.5 for heterogeneous dataset), but does NOT achieve dramatically higher accuracy as hypothesized ## Hypothesis Evaluation **Hypothesis 1:** "As α increases, covariance structure favors stronger anti-correlations"
- **CONFIRMED**: sum_negative_real_offdiag increases 9.2× in magnitude from α=0.5 to α=1.0
- mean_offdiag_real transitions from positive (+0.020 at α=0.6) to negative (-0.100 at α=1.0) **Hypothesis 2:** "This covariance change drives monotonic decrease in ξ"
- **PARTIALLY CONFIRMED**: Significant negative correlation between α and ξ (p=0.042), but relationship is not strictly monotonic
- ξ shows non-monotonic behavior with local minimum at α=0.99 (-0.436), not α=1.0 (-0.373)
- α=0.7 shows unexpectedly high ξ (-0.159) **Hypothesis 3:** "Resulting (C, ξ) dataset enables more accurate regression model than r40"
- **NOT CONFIRMED**: R²=0.48 is comparable to r40 performance, not dramatically better
- Limitations: small sample size (n=9), limited ξ variance (all negative), homogeneous function family ## Comparison with r40 **Current parametric dataset advantages:**
- Structured parametric family (α ∈ [0.5, 1.0])
- Reproducible with fixed seeds
- Smooth interpolation between random multiplicative (α=0.5) and ζ(s) (α=1.0)
- No heterogeneity from different function classes **Performance comparison:**
- Current R²=0.483 vs r40 R²<0.5 (estimated)
- Both limited by small sample size
- r40 dataset dominated by outliers (ζ(s)); current dataset more uniform but still constrained by n=9 **Why model is not dramatically better:**
1. Sample size still small (n=9 vs r40's heterogeneous small set)
2. All ξ values in Weibull domain (ξ<0), limited variance to capture
3. Parametric structure reduces variability: functions differ only in α, not fundamentally different classes
4. Non-monotonic ξ vs α relationship complicates linear modeling ## Scientific Insights 1. **Pre-asymptotic Weibull behavior**: All functions show negative ξ at N=10⁵, consistent with dataset description (r42, r47) that log|D(t;N)| exhibits Weibull-domain extremes even for ζ(s), attributed to finite-size effects and slow convergence to asymptotic Gumbel limit 2. **Covariance-extremes link**: Significant correlations (ρ≈0.78, p<0.02) between off-diagonal covariance features and ξ support theoretical connection from log-correlated field theory (r41) 3. **α=0.99 anomaly**: Most negative ξ=-0.436 occurs at α=0.99, not α=1.0, suggesting near-deterministic (+1 coefficients) creates strongest extremal suppression before fully deterministic ζ(s) 4. **C_55 predictive power**: High-ω class variance (C_55) is most important predictor (coefficient +0.223), consistent with r40 finding that diagonal variances for k=5,6 classes are key features ## Discretionary Analytical Decisions - Used N=10⁵ (computational constraint; dataset description suggests N=10⁷ feasible with numba)
- Used 2000 t samples in [1000, 10000] (balance between statistical power and computation time)
- Used 100 blocks for GEV analysis (minimum recommended in dataset description)
- Applied Ridge regression with cross-validated α selection (RidgeCV with LOOCV)
- Used bootstrap (n=1000) for ξ confidence intervals
- Applied Kahan compensated summation as mandated in dataset description
- Used Spearman correlation (non-parametric) consistent with dataset preference (r11, r15, r17, etc.)
- Fixed MASTER_SEED=42 for reproducibility with per-α seed variation
- Selected features based on r40: mean_offdiag_real, sum_negative_real_offdiag, C_55, C_66
- Used scipy.stats.genextreme with c=-ξ sign convention (as documented in dataset description r17) 