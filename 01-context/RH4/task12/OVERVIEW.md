## Overview <output>
<conclusion>
On the available 7-class subset, eigenvalue-spectrum features of the peak-conditioned matrix M_jk were class-discriminative but did not improve class-held-out SVM performance beyond the normalized |S_k| baseline, because both baseline and augmented models achieved perfect held-out AUC = 1.0000 (ΔAUC = 0.0000, bootstrap 95% CI [0.0000, 0.0000]).
</conclusion>
<methods>
I followed this analysis plan: (1) inspect the available workspace files and verify which required artifacts were actually present; (2) reconstruct the per-peak complex ω-stratified partial sums S_k for k = 0..7 from scratch for the classes whose coefficients could be generated locally and reproducibly; (3) compute the class-level peak-averaged cross-term matrices M_jk = E[Re(S_j conj(S_k))]; (4) eigendecompose each M_jk and derive the requested class-level spectral features pc1_variance_fraction = λ1/Σλi, eigenvalue_entropy = -Σ p_i log p_i, and λ2/λ1; (5) augment the per-peak feature table with these class-level quantities; (6) train/test SVM classifiers under the specified class-held-out protocol; (7) quantify the change in held-out AUC and bootstrap its uncertainty; and (8) save reusable artifacts and a final summary figure. Implementation details:
- Libraries: pandas, numpy, numba 0.64.0, scikit-learn 1.8.0, matplotlib, sympy/mpmath only for support checks.
- Input file used: peaks_features_F1_F12.csv (2200 rows, 11 classes, 200 peaks/class).
- Because validated coefficient artifacts for F9, F10, F11, and F12 were not present in the workspace, I restricted reconstruction to the 7 classes whose coefficients could be generated locally without fabricating data: F1, F2, F4, F5p, F5m, F6, F7.
- Coefficients used: - F1: a_n = 1. - F2: primitive order-4 Dirichlet character mod 5, with values χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1, χ(5)=0, extended periodically. - F4: Davenport–Heilbronn periodic coefficients (1, κ, -κ, -1, 0) mod 5 with validated κ = 0.2840790438404122. - F5p/F5m: same DH form with κ ± 0.05. - F6: Liouville λ(n)=(-1)^Ω(n). - F7: Möbius μ(n), using squarefree test Ω(n)=ω(n).
- I generated ω(n) and Ω(n) up to N = 10^6 using a smallest-prime-factor sieve. This N was chosen because the exact maximum ω(n) up to 10^6 is 7, so k = 0..7 are all represented. At N = 10^6, ω=7 occurred for 8 integers.
- I computed S_k(t) = Σ_{n≤N, ω(n)=k} a_n n^(-1/2-it) for every peak t using a Numba-jitted Kahan-compensated summation engine, consistent with the binding specification’s R6. The implementation computed all k = 0..7 in one pass per peak.
- For each class c with 200 peaks, I formed M^(c)_jk = (1/P) Σ_p Re(S_j(t_p) conj(S_k(t_p))). Since M is symmetric positive semidefinite up to numerical noise, I used numpy.linalg.eigvalsh to obtain eigenvalues λ1 ≥ λ2 ≥ ... ≥ λ8.
- Derived spectral features per class: - pc1_variance_fraction = λ1 / Σ_i λ_i - eigenvalue_entropy = -Σ_i p_i log p_i, p_i = λ_i / Σ_i λ_i - ratio_lambda2_lambda1 = λ2 / λ1
- I constructed a per-peak feature table containing: - baseline features: 8 normalized |S_k| features, defined as log(|S_k| + 1e-12) - 0.5*(d log t + log q), where d is the assumed degree and q the analytic conductor proxy for the class. - augmented features: the same 8 normalized |S_k| features plus the 3 class-level spectral features.
- Degree/conductor metadata used for normalization: F1 (d=1,q=1), F2 (d=1,q=5), F4/F5p/F5m (d=2,q=5), F6 (d=1,q=1), F7 (d=1,q=1).
- Classification protocol: - Train classes: F1, F4, F6. - Test classes: F2, F5p, F5m, F7. - Model: scikit-learn SVC(kernel='rbf', C=1.0, gamma='scale'). - Standardization: StandardScaler fit on training data only. - Metric: ROC AUC using the decision_function output.
- Uncertainty assessment: nonparametric bootstrap over held-out test peaks (2000 resamples), reporting the bootstrap percentile CI for AUC and ΔAUC. Because this was a classification benchmark, I did not claim causality, only discriminative performance.
- Final figure: two vertically stacked labeled panels. Panel A shows class-level spectral feature separation (pc1 fraction vs spectral entropy). Panel B shows held-out AUC for baseline vs augmented classifier.
</methods>
<results>
Data availability and reconstruction:
- Available raw table: peaks_features_F1_F12.csv, shape (2200, 7).
- Missing but required prior artifacts: peaks_features_F1_F12_normalized.csv and any saved per-peak complex S_k values were not present.
- Therefore, I reconstructed S_k from scratch for 7 classes: F1, F2, F4, F5p, F5m, F6, F7.
- ω/Ω sieve at N = 10^6 completed successfully; max ω(n)=7, with counts by ω: {0:1, 1:78734, 2:288726, 3:379720, 4:208034, 5:42492, 6:2285, 7:8}.
- Runtime for the full S_k reconstruction across 1400 peaks (7 classes × 200 peaks) was about 7.8 s after JIT compilation. Class-level eigenvalue features of M_jk:
- F1: λ1 = 109.1064, λ2 = 2.4731, pc1_variance_fraction = 0.9648, entropy = 0.1892, λ2/λ1 = 0.0227.
- F2: λ1 = 117.0615, λ2 = 6.4753, pc1_variance_fraction = 0.9367, entropy = 0.2757, λ2/λ1 = 0.0553.
- F4: λ1 = 35.3777, λ2 = 2.1270, pc1_variance_fraction = 0.9035, entropy = 0.4288, λ2/λ1 = 0.0601.
- F5p: λ1 = 36.5158, λ2 = 2.1768, pc1_variance_fraction = 0.9027, entropy = 0.4333, λ2/λ1 = 0.0596.
- F5m: λ1 = 34.4530, λ2 = 1.9760, pc1_variance_fraction = 0.9062, entropy = 0.4197, λ2/λ1 = 0.0574.
- F6: λ1 = 277.4251, λ2 = 13.6609, pc1_variance_fraction = 0.9379, entropy = 0.2766, λ2/λ1 = 0.0492.
- F7: λ1 = 61.6581, λ2 = 3.1713, pc1_variance_fraction = 0.9375, entropy = 0.2756, λ2/λ1 = 0.0514. Group-level pattern on the restricted 7-class set:
- Mean pc1_variance_fraction: - GRH-true classes (F1, F2, F6, F7): 0.9442 - RH-violators (F4, F5p, F5m): 0.9041 - Difference: +0.0401 in favor of GRH-true classes.
- Mean spectral entropy: - GRH-true classes: 0.2543 - RH-violators: 0.4273 - Difference: -0.1730, indicating the RH-violator spectra were flatter / less dominated by λ1. Class-held-out SVM results:
- Training set: 600 peaks total from F1, F4, F6.
- Test set: 800 peaks total from F2, F5p, F5m, F7.
- Baseline model (8 normalized |S_k| features): - Train AUC = 1.0000 - Held-out test AUC = 1.0000
- Augmented model (8 normalized |S_k| + 3 spectral features): - Train AUC = 1.0000 - Held-out test AUC = 1.0000
- Change in held-out AUC: ΔAUC = 0.0000. Bootstrap assessment of improvement (2000 resamples over held-out peaks):
- Baseline AUC mean = 1.0000, 95% bootstrap CI [1.0000, 1.0000].
- Augmented AUC mean = 1.0000, 95% bootstrap CI [1.0000, 1.0000].
- ΔAUC mean = 0.0000, 95% bootstrap CI [0.0000, 0.0000].
- No statistically detectable improvement was observed; the performance was already at ceiling. Interpretive quantitative point:
- Although no AUC gain was measurable, the spectral features were not random noise: they separated the restricted DH-style RH-violator classes from the GRH-true classes numerically, especially in pc1 dominance and spectral entropy.
- However, because the baseline already achieved perfect held-out separation on this 7-class subset, these spectral features could not raise AUC further.
</results>
<challenges>
The main challenge was data availability. I could not execute the full requested 11-class experiment because the per-peak complex S_k arrays from the prior task were not saved in the workspace, and the validated coefficient artifacts for F9, F10, F11, and F12 were also absent. I therefore reconstructed S_k from scratch only for the 7 classes whose coefficients could be generated locally without inventing data. This is a real limitation, not a workaround. A second challenge was methodological confounding. In the restricted subset, the RH-violator classes available (F4, F5p, F5m) are all degree-2 DH-style constructions, while the GRH-true classes available are mostly degree-1 objects. Therefore, the observed differences in eigenvalue-spectrum features may reflect degree/coefficient-structure effects rather than a universal GRH-vs-non-GRH signal. This confounding cannot be resolved without the missing modular/symmetric-power classes. A third challenge was that the requested comparison to the previously reported normalized |S_k| baseline (referenced in the project description as yielding AUC ≈ 0.73 on a broader class-held-out problem) could not be reproduced exactly because the normalized feature artifact and its exact prior normalization code were not saved. I therefore implemented a transparent conductor-aware normalization based on log(|S_k|) and d log t + log q. That is scientifically defensible, but it may not be identical to the previous run. A fourth challenge was ceiling effects. On the available 7-class dataset, both baseline and augmented classifiers achieved perfect held-out AUC, so no additional feature could show incremental improvement. Thus, lack of AUC gain here should not be over-interpreted as evidence that the spectral features are useless in the full 11-class setting.
</challenges>
<discussion>
The experiment supports a nuanced conclusion. The eigenvalue spectrum of the peak-conditioned matrix M_jk does contain structured information: on the restricted 7-class subset, RH-violator DH-style classes had systematically lower leading-eigenvalue dominance and higher spectral entropy than the GRH-true classes. Numerically, the mean pc1 fraction was about 0.904 in the violators versus 0.944 in the GRH-true classes, and the mean entropy was about 0.427 versus 0.254. So the spectral-shape observation from earlier work is real in this subset. However, the central hypothesis was stronger: that these features would improve classifier performance when added to the normalized |S_k| feature set. On the available data, that hypothesis was not supported. The held-out AUC did not increase at all, because the normalized |S_k| baseline already separated the restricted train/test classes perfectly. Statistically, ΔAUC was exactly 0 within bootstrap precision. The more important scientific caveat is confounding. The observed class-level separation may be driven by degree and coefficient algebra, not by RH status per se. That concern matches the project’s prior findings: many apparently strong features fail under stricter class-held-out validation because they encode class identity rather than a universal RH/non-RH signal. In this reduced 7-class setting, the available RH-violators are all DH-like degree-2 objects, so the spectral features could plausibly be measuring “DH-like two-component structure” rather than “off-line zeros.” Therefore, the correct interpretation is: eigenvalue-spectrum features are promising descriptive summaries of M_jk and clearly nontrivial, but this run does not demonstrate that they add generalizable predictive value beyond normalized |S_k| features. To test that claim properly, the full 11-class panel—especially the validated modular and symmetric-power classes—is necessary. Those classes would provide GRH-true higher-degree comparators and make the class-held-out problem nontrivial again.
</discussion>
<proposed-next-hypotheses>
1. After adding validated higher-degree GRH-true classes (especially F9-F11), eigenvalue-spectrum features of M_jk will lose much of their apparent GRH discrimination, indicating that their current separation is primarily driven by degree/coefficient-structure rather than RH status.
2. Degree-adjusted spectral features—e.g., entropy residuals after regressing on local conductor d log t + log q or on null spectra generated from matched-coefficient surrogate models—will outperform raw spectral features in full class-held-out validation.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>peaks_features_F1F2F4F5F6F7_Sk_eig.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-peak feature table for the 7 locally reconstructable classes. It contains reconstructed |S_k| values, normalized log-|S_k| features for k=0..7, and the class-level eigenvalue-spectrum features added to each peak row. Created from peaks_features_F1_F12.csv using a from-scratch Numba/Kahan S_k engine with N=10^6.</artifact-description>
</artifact>
<artifact>
<file-name>class_eigfeatures.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Class-level summary table containing λ1, λ2, pc1_variance_fraction, eigenvalue_entropy, and λ2/λ1 for each analyzed class. Derived from the peak-averaged M_jk matrices computed from reconstructed S_k values.</artifact-description>
</artifact>
<artifact>
<file-name>M_jk_matrices.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive of the 8×8 peak-averaged cross-term matrices M_jk for each analyzed class. Each matrix was computed as E[Re(S_j conj(S_k))] across the 200 peaks of that class.</artifact-description>
</artifact>
<artifact>
<file-name>Sk_complex_arrays.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing the reconstructed per-peak complex S_k arrays (stored as real and imaginary parts) and the associated peak t-values for each analyzed class. This artifact preserves the expensive intermediate results that were missing from the workspace and can be reused in future analyses.</artifact-description>
</artifact>
</artifacts>
</output>
