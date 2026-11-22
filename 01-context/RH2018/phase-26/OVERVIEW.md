## Overview ## ANALYSIS COMPLETE: S_k Covariance Dynamics Do Not Predict GEV Shape Parameter ξ The regression modeling analysis **definitively rejects** the hypothesis that S_k covariance features predict the GEV shape parameter ξ with R² > 0.7. All tested models show poor predictive performance and negative leave-one-out cross-validation (LOOCV) R² values, indicating worse-than-baseline predictions. ### Primary Findings **Model Performance (All 8 functions):**
- Primary model (CS_N + CG_N): Training R² = 0.346, LOOCV R² = -1.971
- Extended model (5 features): Training R² = 0.961, LOOCV R² = -3.964 (severe overfitting)
- CS_N only: Training R² = 0.137, LOOCV R² = -1.242
- CG_N only: Training R² = 0.126, LOOCV R² = -1.542 **Best Model (CS_N only, excluding F8 outlier):**
- Training R² = 0.455, Adjusted R² = 0.346
- LOOCV R² = -0.255 (still negative, poor generalization)
- CS_N coefficient = 0.073 (p = 0.096, 95% CI: [-0.019, 0.164])
- Marginally significant but **opposite direction to hypothesis** **Direction of Association:**
The hypothesis predicted that stronger cancellation (more negative CS_N) would produce more negative ξ (heavier tails). However, the data show the **opposite trend**: more negative CS_N is weakly associated with LESS negative ξ (lighter tails), contradicting the proposed mechanism. **Comparison to Previous Model:**
- Previous model (f17) LOOCV R²: 0.3625
- Current best LOOCV R²: -0.255
- **Performance degradation:** -0.618 ### Statistical Evidence **Coefficient Details (CS_N + CG_N model, all 8 functions):**
- Intercept: -0.682 (SE=0.261, p=0.047)
- CS_N: -0.280 (SE=0.217, p=0.252) - NOT significant
- CG_N: 0.0014 (SE=0.001, p=0.262) - NOT significant **Most Predictive Feature:**
CS_N shows the strongest (though still weak) association with ξ, achieving marginal significance (p=0.096) when excluding F8. This partially supports the hypothesis that CS_N is more discriminative than CG_N, but the relationship is far weaker than predicted. **F8 (Fully Random) as Outlier:**
- CS_N = -0.284 (weakest cancellation)
- ξ = -1.370 (by far most negative, bounded Weibull tail)
- F8's extreme ξ value reflects its fundamentally different nature: complete absence of arithmetic structure produces minimal extreme values
- F8 completely breaks the hypothesized CS_N → ξ relationship ### Statistical Rigor **Inverse-Variance Weighting:**
Properly implemented using weights = 1/(ξ_SE)². For F8 (which had zero SE), used median SE = 0.031 from other functions. Weighting improved training R² by ~0.13 compared to unweighted regression. **Cross-Validation:**
Leave-one-out cross-validation (LOOCV) was performed on all models. All showed negative LOOCV R², indicating predictions worse than simply using the mean. This demonstrates fundamental lack of predictive power rather than random variation. **Multicollinearity Check:**
Discovered that CS_N ≡ Sum_Negative_N2 (perfect collinearity), requiring removal of redundant feature. Extended model still showed high condition number (4.9×10³), indicating numerical instability. ### Conclusion The hypothesis that S_k covariance metrics predict ξ with R² > 0.7 is **strongly rejected**. The best achievable LOOCV R² is -0.255, far below both the hypothesized threshold and the previous model's performance (0.3625). CS_N shows marginal predictive value but in the opposite direction to the hypothesis. The relationship between covariance dynamics and extreme value statistics is weaker and more complex than proposed, with the fully random function (F8) serving as a critical counterexample to the hypothesized mechanism. --- ## DISCRETIONARY DECISIONS - **Inverse-variance weighting scheme**: Used weights = 1/(ξ_SE)² as specified; for F8 with zero SE, assigned median SE (0.031) from other functions
- **F8 handling**: Reported results both including and excluding F8 to assess outlier influence
- **Model selection**: Tested multiple feature combinations (CS_N+CG_N, univariate, extended 5-feature model) to identify best predictor
- **Significance threshold**: Used α = 0.05 for statistical tests
- **Cross-validation method**: Applied leave-one-out (LOOCV) as appropriate for small sample (n=8)
- **Statistical framework**: Used weighted least squares (WLS) via statsmodels for proper inference with heteroscedastic errors
- **Correlation methods**: Reported both Pearson and Spearman correlations given non-Gaussian data
- **Extended dataset artifacts used**: sk_covariance_classification.csv and summary_bulk_and_gev.csv 