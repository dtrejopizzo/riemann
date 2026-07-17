## Overview <output>
<conclusion>
The hypothesis is rejected: a Ridge/Lasso regression on simple arithmetic statistics of the Dirichlet coefficients (|a_p| moments, low-lag autocorrelations, Σ|a_n|²/n) does NOT explain >75% of the variance in the PC1/PC2 amplification-space projections of the 11 function classes — leave-one-out cross-validated R² is negative for both PC1 (R²≈−0.29) and PC2 (R²≈−0.18), well below the 75% threshold.
</conclusion> <methods>
1. Loaded the 11×10 PCA projection matrix and class labels from `A_matrices.npy` / `projections.npy` / `classes.npy` (class order F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12). PC1 and PC2 capture 89.96% and 7.28% of variance, respectively.
2. Generated/loaded Hecke-normalized Dirichlet coefficients a_n up to N=10⁶ for each class: - F1: a_n=1; F6: Liouville λ(n) (sieve, smallest-prime-factor); F7: Möbius μ(n). - F2: order-4 complex primitive character χ mod 5 (χ(2)=i, χ(3)=−i, χ(4)=−1, period 5). - F4: a_n = χ(n)+κ·χ̄(n), κ=0.28408; F5p: κ+0.05; F5m: κ−0.05 (same complex χ mod 5). - F9: τ(n)/n^(11/2) from `coeffs_F9_a.npy`; F10: a_n/n^(1/2) from `coeffs_F10_a.npy`; F11: λ_n already-normalized from `lambda_n.npy`; F12: complex coefficients from `a.npy`.
3. For each class computed an 8-dimensional feature vector: mean, variance, skewness, kurtosis of |a_p| over the 168 primes p<1000; autocorrelations c_k = (1/(N−k)) Re Σ_{n=1}^{N−k} a_n · conj(a_{n+k}) for k=1,2,3; and the truncated second moment D = Σ_{n=1}^{N} |a_n|²/n.
4. Built an 11-row table (saved as `arithmetic_features_vs_PC.csv`) and trained scikit-learn Ridge (α∈{0.01…1000}) and LassoCV (with feature standardisation). Performance assessed by in-sample R², 5-fold CV, and Leave-One-Out CV using `sklearn.model_selection.LeaveOneOut`.
5. Final evaluation: best regularised in-sample fit at α=0.1 (Ridge) and best LOO at α=100; OLS reported separately to flag overfitting.
</methods> <results>
- Pearson correlations of features with targets: PC2 correlates strongly with var(|a_p|) (r=0.905) and weakly with skew, kurtosis, and Σ|a_n|²/n; PC1 has no |r|>0.21 single-feature correlation.
- In-sample fits (Ridge, α=0.1): R²(PC1)=0.555, R²(PC2)=0.896. OLS in-sample: R²(PC1)=0.990, R²(PC2)=1.000 — clear overfit (8 features for 11 samples).
- Cross-validated performance (the metric the hypothesis really demands): - LOO-CV best Ridge α=100: R²(PC1)=−0.294, R²(PC2)=−0.183. - 5-fold CV best Ridge α=100: R²(PC1)=−0.126, R²(PC2)=−0.232. - LassoCV LOO: R²(PC1)=−0.21, R²(PC2)≈−43.6 (highly unstable). All cross-validated R² are negative, meaning the model performs worse than predicting the mean of the held-out target.
- Diagnostic of the failure: F1 (ζ), F6 (Liouville), F7 (Möbius) all have mean(|a_p|)=1, var(|a_p|)=0, skew=kurt=0, and near-zero k=1,2,3 autocorrelations, yet their PC1 coordinates differ enormously (−14.3, +85.4, −2.6). No model on this feature set can separate them.
- Hypothesis target (>75% variance explained, properly cross-validated): NOT met for either PC1 or PC2.
</results> <challenges>
- Severe sample-size limitation: only 11 function classes vs. 8 predictors makes any cross-validation noisy and OLS guaranteed to overfit. The hypothesis is structurally hard to support with the available number of classes.
- Coefficient ambiguity: the PDF labels F2/F4 with "χ_4 mod 5" but does not give explicit a_n formulas. The classical Davenport–Heilbronn construction (used here) requires the order-4 complex primitive character mod 5, not the quadratic one — needed clarification via the PDF re-read and prior memory.
- Coefficient scaling: F9 (Δ) τ(n) grows like n^(11/2); had to normalize each modular form by its arithmetic factor n^((k−1)/2) to put |a_p| on a comparable O(1) scale across classes.
- LassoCV had repeated convergence warnings on this small dataset and produced highly unstable LOO predictions.
</challenges> <discussion>
The amplification-space coordinates encode information that is not captured by simple aggregate statistics of the Dirichlet coefficient sequence. Critically, classes that are arithmetically near-trivial in this feature set (ζ, λ, μ — all with |a_p|≡1 and zero low-lag autocorrelations) occupy widely separated PC1 positions, demonstrating that the peak-amplification matrix A_jk responds to structure (multiplicativity type, sign behaviour, conductor, gamma factors / functional equation) that |a_p|-distribution moments are blind to. PC2, which is dominated by var(|a_p|) — a proxy for "Sato–Tate-like" coefficient variance — does show some interpretable in-sample signal (modular forms F9, F10, F11 lie on the high-variance side; ζ/λ on the zero-variance side), but this trivially distinguishes "GL(1) vs higher rank" rather than predicting individual peak structure. This negative finding is consistent with r39's earlier observation that unconditional theoretical moments are poor predictors of high-peak statistics; the connection from a_n to amplification space is mediated by peak-conditioning effects that simple bulk statistics cannot reproduce.
</discussion> <proposed-next-hypotheses>
1. The PC1 amplification coordinate is driven by analytic/arithmetic invariants of the functional equation (degree d, gamma factors, log-conductor) rather than by bulk a_n statistics; a model using (d, log N, sum of Γ-shifts, root-number type) plus var(|a_p|) will achieve cross-validated R²>0.7 on PC2 and >0.5 on PC1.
2. Replacing global a_n-statistics with prime-power-weighted Sato–Tate residuals — i.e. moments of Λ(n)·a_n / √n in the explicit-formula sense — will yield arithmetic features that linearly predict A_jk eigen-projections, since these are the quantities that actually contribute to peak amplification through Weil's explicit formula.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>arithmetic_features_vs_PC.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table with 11 rows (classes F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) and 10 columns: 8 arithmetic features of the Dirichlet coefficient sequence a_n up to N=10⁶ (mean/variance/skewness/kurtosis of |a_p| over 168 primes p<1000, real-part autocorrelations Σ a_n conj(a_{n+k})/(N−k) for k=1,2,3, and second moment Σ|a_n|²/n), plus the target PC1 and PC2 amplification-space coordinates loaded from `A_jk_matrices_and_PCA.npz`/`projections.npy`. Intended as the inputs/targets for any future regression attempts on this dataset.</artifact-description>
</artifact>
<artifact>
<file-name>arithmetic_features_PC_prediction.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) PC1 predicted vs. actual; (B) PC2 predicted vs. actual. Blue circles are Ridge in-sample predictions (α=0.1, R²=0.555 and 0.896); red crosses are leave-one-out CV predictions (α=100, R²=−0.29 and −0.18). The contrast between in-sample fit and negative LOO R² visualises the over-fitting and lack of generalisation that lead us to reject the >75% explained-variance hypothesis.</artifact-description>
</artifact>
</artifacts>
</output>
