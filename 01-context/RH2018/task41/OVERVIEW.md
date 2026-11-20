## Overview **CONCLUSION:** An SVM classifier trained on bulk statistical moments (variance, skewness, excess kurtosis) does NOT effectively separate RH-satisfying from RH-violating functions. All tested SVM variants (RBF kernel, linear kernel, balanced class weights) achieve only 50% accuracy with leave-one-out cross-validation, equivalent to random chance. The classifier fails to improve upon simpler approaches and cannot correctly identify L_DH(s) and L(s,λ) as distinct from ζ(s) and other RH-satisfying functions. --- **DETAILED RESULTS:** **Model Performance (LOOCV):**
- SVM (RBF, default): Accuracy=50%, Precision=0%, Recall=0%, F1=0.0
- SVM (Linear): Accuracy=50%, Precision=0%, Recall=0%, F1=0.0 - SVM (RBF, Balanced): Accuracy=50%, Precision=40%, Recall=66.7%, F1=0.5
- Logistic Regression (Skewness only): Accuracy=50%, Precision=0%, Recall=0%, F1=0.0 The balanced SVM shows marginally better performance metrics (recall=66.7%, precision=40%) but still achieves only 50% overall accuracy, correctly classifying 4 out of 8 functions. **Systematic Misclassifications:**
- **F7 (Möbius L(s,μ), RH-True)**: Misclassified by ALL models (4/4), consistently predicted as RH-violating. F7 has lower variance (0.93), less negative skewness (-0.39), and lower excess kurtosis (0.19) compared to F1 and F2, positioning it closer to the RH-violating cluster. - **F3 (L(χ) complex mod 5, RH-False)**: Misclassified by 3/4 models, frequently predicted as RH-satisfying. F3 has high variance (1.69), strongly negative skewness (-0.81), and high excess kurtosis (1.29), making it nearly indistinguishable from F1 and F2. - **F1 (Riemann ζ) and F2 (L(χ₄) real mod 5)**: Both RH-satisfying functions were misclassified by 3/4 models. **Feature Space Analysis:**
- **Separability Ratio**: 0.47 (Euclidean distance between class centroids / average within-class distance), indicating poor class separation. - **Class Overlap**: Mann-Whitney U tests show no significant differences between RH-True and RH-False groups for any feature (p>0.39 for all). - **Most Confusable Pair**: F2 (RH-True) and F3 (RH-False) have an inter-point distance of only 0.46 in standardized feature space, far smaller than typical within-class distances. - **Centroid Distance**: Only 1.10 in standardized 3D feature space, with substantial overlap in all pairwise projections. **Comparison to Reference Task (r84):**
The rationale stated that the simple linear model using skewness from task r84 was "surprisingly effective." However, logistic regression using skewness alone achieves only 50% accuracy in this analysis, identical to all SVM variants. This suggests either:
1. The r84 finding may have evaluated a different metric or subset of functions, or
2. The "effectiveness" was relative to other approaches tested in that context rather than absolute predictive power. The current analysis conclusively demonstrates that neither simple linear models nor sophisticated non-linear SVM classifiers can reliably distinguish RH-satisfying from RH-violating functions using bulk statistical moments at N=10⁵. **Key Statistical Evidence:**
- Between-class distance (mean): 2.22 ± 1.11
- Within RH-True distance (mean): 2.00 ± 0.65 - Within RH-False distance (mean): 2.66 ± 1.26
- Minimum between-class distance: 0.46 (F2-F3 pair)
- PCA analysis: First two components capture 97.4% of variance (PC1=63.6%, PC2=33.8%), yet classes remain inseparable in this projection. --- **DISCRETIONARY DECISIONS:** - Used variance, skewness, and excess kurtosis as features (excluded mean, as it primarily reflects function normalization rather than distributional shape)
- Applied StandardScaler for feature normalization prior to SVM training
- Selected RBF kernel as primary non-linear kernel; also tested linear, polynomial (degree=2), and sigmoid kernels for comparison
- Set SVM gamma parameter to 'scale' (default: 1/(n_features × X.var()))
- Used leave-one-out cross-validation (LOOCV) due to small sample size (n=8)
- Tested balanced class weights to address 3:5 class imbalance between RH-True and RH-False
- Set random_state=42 for reproducibility
- Applied significance threshold α=0.05 for Mann-Whitney U tests
- Used two-sided alternative hypothesis for Mann-Whitney tests
- Classified RH status based on established knowledge: RH-satisfying={F1: Riemann ζ, F2: L(χ₄) real mod 5, F7: Möbius L(s,μ)}; RH-violating={F3, F4, F5, F6, F8}
- Used PCA with 2 components for decision boundary visualization (captures 97.4% of variance)
- Defined precision, recall, and F1-score with zero_division=0 to handle undefined metrics when no positive predictions are made
- Evaluated all kernel types with consistent cross-validation approach for fair comparison
