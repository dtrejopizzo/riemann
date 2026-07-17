## Overview <output>
<conclusion>
The hypothesis is refuted: a multiple linear regression of the per-class peak-amplification tilt λ on the mean of |λ_p| for primes p<100 and log(conductor) achieves only an in-sample R²≈0.08 and a leave-one-out cross-validated R²≈−1.60, far below the predicted threshold of 0.7.
</conclusion> <methods>
1. Loaded `erdos_kac_tilt_fits.csv`, which provides the fitted Erdős–Kac/Poisson tilt parameter λ and family/GRH labels for the 11 classes F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12.
2. Assembled per-class normalized prime coefficients λ_p for the 25 primes 2 ≤ p < 100 from the following sources: - F1 (ζ): a_p = 1. - F2 (real primitive Dirichlet character mod 5, Legendre symbol): λ_p = (p/5). - F4 (Davenport–Heilbronn) with κ=0.28408 and the standard pattern a_n on residues (1,2,3,4,0) mod 5 = (1, κ, −κ, −1, 0); F5p, F5m use κ±0.05. - F6 (Liouville) and F7 (Möbius): λ(p) = μ(p) = −1. - F9 (Δ) from `coeffs_F9_lambda.npy`, F10 (11.2.a.a) from `coeffs_F10_lambda.npy`, F11 (Sym²Δ) from `lambda_n.npy`, F12 (χ₃ + cχ₅) from `a.npy`.
3. Computed the predictor mean(|λ_p|) over those 25 primes for each class and assigned the analytic conductor q (F1/F6/F7/F9/F11: 1; F2/F4/F5p/F5m: 5; F10: 11; F12: 15) with feature log(q).
4. Fit a multiple linear regression (`sklearn.linear_model.LinearRegression`) with target λ and predictors [mean(|λ_p|), log(q)]. Reported in-sample coefficients and R².
5. Evaluated generalization with leave-one-out cross-validation (`LeaveOneOut`, `cross_val_predict`) and computed CV R² as 1 − SS_res/SS_tot on concatenated out-of-fold predictions.
6. Computed Pearson and Spearman correlations of each predictor with λ as auxiliary diagnostics.
</methods> <results>
Per-class feature table (n = 11):
- F1 λ=0.451, mean|λ_p|=1.00, log q=0.00
- F2 λ=0.431, mean|λ_p|=0.96, log q=1.61
- F4 λ=0.445, mean|λ_p|=0.56, log q=1.61
- F5p λ=0.446, mean|λ_p|=0.59, log q=1.61
- F5m λ=0.444, mean|λ_p|=0.53, log q=1.61
- F6 λ=0.437, mean|λ_p|=1.00, log q=0.00
- F7 λ=0.462, mean|λ_p|=1.00, log q=0.00
- F9 λ=0.320, mean|λ_p|=0.75, log q=0.00
- F10 λ=0.297, mean|λ_p|=0.77, log q=2.40
- F11 λ=0.102, mean|λ_p|=0.65, log q=0.00
- F12 λ=0.439, mean|λ_p|=2.11, log q=2.71 Fitted regression: λ ≈ 0.326 + 0.050·mean(|λ_p|) + 0.017·log(q).
- In-sample R² = 0.084.
- Leave-one-out CV R² = −1.595 (predictions are worse than predicting the global mean of λ).
- Pearson correlations: r(mean|λ_p|, λ)=0.25 (p=0.47); r(log q, λ)=0.22 (p=0.52). Spearman: 0.12 and −0.10 respectively (both p>0.7).
- Visual inspection (Panel B) confirms no monotone relationship: the three modular forms F9/F10/F11 have low λ (0.10–0.32) yet have intermediate |λ_p| (0.65–0.77), while F12 has the highest mean|λ_p| (2.11) but a λ (0.44) statistically indistinguishable from the GRH-true F1/F6/F7 (1.00) and the DH violators F4/F5p/F5m (≈0.56). Conductor explains essentially nothing.
</results> <challenges>
- The dataset contains only 11 observations, so any leave-one-out estimate has very high variance; nevertheless the in-sample R² of 0.08 alone already rules out the hypothesized R²>0.7.
- Coefficients for F1, F2, F4, F5p, F5m, F6, F7 had to be reconstructed from first principles (using the documented κ=0.28408 and the standard DH residue pattern (1, κ, −κ, −1, 0) mod 5). These are unambiguous because a_p depends only on p mod 5, but the precise value of |a_p| at p=5 depends on the convention; we used a_5 = 0 consistent with the imprimitive Euler factor at the conductor prime.
- Conductors for F4/F5/F12 were taken from the conductor of the underlying Dirichlet characters (5 for F4/F5, 15 for F12); these are not standard "analytic conductors" of an L-function in the Selberg class but are the natural arithmetic conductors and are consistent with prior runs (r49). Using slight variants (e.g., q=25 for F4) does not materially change the result.
- The F11 lead-eigenvalue (5.0) and λ (0.10) are extreme outliers driven by the much larger Sym²Δ prime power growth — even before any modeling this point lies far off any potential trend with mean|λ_p|.
</challenges> <discussion>
This negative result is consistent with — and sharpens — the broader finding (r39, r44, r50) that unconditional bulk arithmetic statistics of the coefficients do not predict the conditional behavior at the largest peaks. The amplification tilt λ is a property of which terms S_k dominate at peaks, governed by the conditioning event |S(t)| large, not by the average size of |a_p| over small primes. In particular, F12 is built precisely so that its bulk |a_p| is large (because c is complex with |c|≈1.91, inflating |a_p|) yet its conditional peak structure is, by construction, indistinguishable at the family level from the small-coefficient DH violators F4/F5. Conversely, F1/F6/F7 share identical |a_p|=1 and identical conductor 1 yet have (slightly) different λ. The cross-validated negative R² shows the model is actively misled by F12's high mean|λ_p|. A predictive theory of λ must instead use peak-conditional features (e.g., the Erdős–Kac mean μ_eff = log log T at conditioned peaks, the leading eigenvector of the amplification matrix A_jk, or the principal components of M_jk in r39) rather than unconditional moments of a_p.
</discussion> <proposed-next-hypotheses>
1. The tilt parameter λ is governed by the peak-conditional Erdős–Kac mean μ_eff = ⟨ω(n)⟩_peaks rather than by unconditional coefficient statistics, and a regression of λ on μ_eff(class) and the leading eigenvalue of the amplification matrix A_jk will achieve cross-validated R² > 0.7.
2. Among modular forms (F9/F10/F11), λ scales with the degree d of the L-function (d=2 for F9/F10, d=3 for F11), with degree-3 functions exhibiting suppressed tilts; this can be tested by adding F13 (degree 2, Maass) at N=999 and a Sym³Δ control (degree 4) and fitting λ as a function of d alone.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>lambda_arithmetic_features.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-class table (11 rows: F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) used in this analysis. Columns: class, family, GRH status, fitted tilt λ from `erdos_kac_tilt_fits.csv`, the engineered predictor mean(|λ_p|) over the 25 primes 2≤p<100, the analytic conductor q and log(q), and the leave-one-out cross-validated prediction `lambda_pred_loo` from a multiple linear regression on [mean|λ_p|, log q].</artifact-description>
</artifact>
<artifact>
<file-name>lambda_regression_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: observed λ vs LOO-CV predicted λ (R²=−1.60), showing the model is worse than the mean baseline and that F12 in particular is grossly mis-predicted. Panel B: scatter of mean(|λ_p|) vs λ colored by GRH status, with class labels, illustrating the absence of a monotone relationship (Pearson r=0.25, p=0.47).</artifact-description>
</artifact>
</artifacts>
</output> 