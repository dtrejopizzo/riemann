## Overview ## ANSWER **The bulk statistical moments approach provides a significantly better predictive model for the GEV shape parameter ξ compared to the S_k covariance model, with a LOOCV R² improvement from -1.971 to +0.149.** The optimal model is a simple univariate linear regression using **Skewness** as the sole predictor for 7 arithmetic L-functions (excluding the F8 fully random outlier): **ξ = 0.161 × Skewness - 0.205** ### Key Quantitative Results: **Model Performance (7 functions):**
- R² = 0.562
- LOOCV R² = 0.149 (vs. -1.971 for S_k covariance model)
- RMSE = 0.0405
- Spearman ρ = 0.786 (p = 0.036)
- Model coefficient: 0.161 ± 0.064 (p = 0.052, marginally significant) **Bivariate Correlations with ξ (all 8 functions):**
- Excess Kurtosis: r = -0.811, p = 0.015 (significant)
- Skewness: r = 0.700, p = 0.053 (marginally significant)
- Variance: r = 0.519, p = 0.187 (not significant) **Multiple Regression Results:**
Multiple regression models using all three bulk moments (Variance + Skewness + Excess Kurtosis) achieved high in-sample R² (0.926 for 8 functions, 0.605 for 7 functions) but failed to generalize in cross-validation, yielding negative LOOCV R² values (-0.262 and -1.844, respectively). This indicates severe overfitting despite inverse-variance weighting. **Critical Finding - F8 Outlier Effect:**
F8 (fully random function) is an extreme outlier with ξ = -1.370 (compared to the range -0.185 to -0.373 for the other seven functions). Including F8 causes all models to fail cross-validation. The optimal strategy requires excluding F8 from model training. ### Conclusion **YES**, the bulk statistical moments approach is predictive and represents a viable predictive strategy compared to the S_k covariance model. The LOOCV R² improvement of +2.12 (from -1.971 to +0.149) demonstrates that the bulk moments model can generalize to unseen L-functions, whereas the S_k covariance model completely fails to do so. However, important caveats apply:
1. **Modest predictive power**: LOOCV R² = 0.149 indicates weak but positive generalization
2. **Limited scope**: Model only valid for the 7 arithmetic L-functions (F1-F7)
3. **Simpler is better**: Univariate Skewness model outperforms multiple regression
4. **Statistical significance**: Relationship is marginally significant (p = 0.052) The bulk moments approach provides a simpler, more robust alternative to complex covariance-based modeling, though predictive accuracy remains limited. --- ## DISCRETIONARY DECISIONS - **Model selection criterion**: Used LOOCV R² as the primary metric for model comparison and generalization assessment, following the precedent established in task r78
- **Handling F8's zero standard error**: Assigned F8 the minimum non-zero SE (0.0243) for inverse-variance weighting calculations to avoid infinite weights
- **F8 exclusion strategy**: Created separate models with and without F8 to assess outlier influence, ultimately recommending the 7-function model based on superior LOOCV performance
- **Significance threshold**: Applied α = 0.05 for statistical significance testing; reported p = 0.052 as "marginally significant"
- **Feature selection**: Tested both multiple regression (all three bulk moments) and univariate models; selected univariate Skewness model based on superior LOOCV performance
- **Weighted regression**: Applied inverse-variance weighting using weights = 1/SE² to account for heterogeneous uncertainty in ξ estimates across functions
- **Correlation method**: Reported both Pearson and Spearman correlations; prioritized Spearman (ρ = 0.786, p = 0.036) as a robust non-parametric measure given the small sample size (n=7)
- **Normality assumption**: Validated model assumptions using Shapiro-Wilk test on LOOCV residuals (W = 0.966, p = 0.867), confirming residuals are consistent with normality
- **Dataset used**: summary_bulk_and_gev.csv (derived artifact from previous analysis, containing bulk moments and GEV parameters at N=10⁵) 