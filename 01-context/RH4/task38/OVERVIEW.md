## Overview <output>
<conclusion>
The hypothesis is partially refuted: the F4 (DH) and F12 violator families do show massive systematic differences in individual normalized log|S_k| features (k=1..4 are essentially disjoint, KS=1.0), but contrary to the specific prediction the s2/s3 ratio is nearly identical between the two families (KS=0.14), and an RBF SVM trained on F1+F4 generalizes perfectly to F12 (and vice-versa, AUC=1.0 in both directions).
</conclusion>
<methods>
1. Loaded `peaks_features_F1_F12_normalized_full.csv` (2200 rows × 31 cols, 11 classes × 200 peaks).
2. Defined feature set: normalized log|S_k| for k=1..6 (S_0 is trivially 0 by construction, S_7 excluded due to the documented mod-5 leak at N=10^6).
3. Cross-family generalization test (binary GRH-violator vs F1 zeta): - Pipeline = StandardScaler → SVC(kernel='rbf', gamma='scale'). - (a) Trained on F1+F4 (label 1=F4), evaluated AUC on F12 vs F1 using SVM decision_function scores. - (b) Trained on F1+F12, evaluated AUC on F4 vs F1.
4. Distribution comparison: built two pools — DH family = {F4, F5p, F5m} (n=600) and F12 (n=200). Ran two-sample Kolmogorov–Smirnov tests (`scipy.stats.ks_2samp`) on each normalized log|S_k| (k=1..6).
5. Computed `s2_s3_ratio = log|S_2| / log|S_3|` (raw log values; identical to ratio of normalized values because the dataset's normalization is multiplicative on log|S_k|, verified empirically) and ran the same KS test.
6. Saved KS summary table (`r26_DH_vs_F12_KS_summary.csv`) and final 2-panel figure (`r26_DH_vs_F12_summary.png`).
</methods>
<results>
Cross-family AUCs (binary violator vs F1 zeta on the 6 normalized log|S_k|):
- Train F1+F4 → test F12 vs F1: **AUC = 1.000**
- Train F1+F12 → test F4 vs F1: **AUC = 1.000** KS test, DH family (n=600) vs F12 (n=200), normalized log|S_k|:
| feature | KS | p-value | DH mean | F12 mean |
|---|---|---|---|---|
| log|S_1|_norm | 1.000 | 2.6e-194 | 0.280 | 0.826 |
| log|S_2|_norm | 1.000 | 2.6e-194 | 0.529 | 1.007 |
| log|S_3|_norm | 1.000 | 2.6e-194 | 0.478 | 0.929 |
| log|S_4|_norm | 0.965 | 4.7e-165 | 0.309 | 0.747 |
| log|S_5|_norm | 0.792 | 2.3e-95 | -0.218 | 0.232 |
| log|S_6|_norm | 0.690 | 2.6e-69 | -1.342 | -0.870 |
| **s2/s3 ratio** | **0.140** | **5.3e-3** | **1.128** | **1.089** | The S_1, S_2, S_3 distributions are completely disjoint between DH and F12 (KS=1.0). F12 has uniformly larger normalized log|S_k| than the DH family for k=1..5. The s2/s3 ratio, by contrast, is statistically distinguishable but only weakly so (KS=0.14): means 1.128 (DH) vs 1.089 (F12), differing by ~3.5% with heavily overlapping distributions.
</results>
<challenges>
- The "generalization failure" framing in the hypothesis was not reproduced in this minimal binary setting: an RBF-SVM with k=1..6 normalized features separates each violator family from zeta perfectly, and the two violator families lie on the same side of the F1 boundary, so cross-family AUC is 1.0 in both directions. The previously observed failure in r25 likely came from a richer multi-class setup or class-held-out protocol that is not reconstructed here.
- The dataset's `log_abs_Sk_norm` column is a (per-peak, multiplicative) rescaling of `log_abs_Sk`, so ratios `S_2/S_3` are invariant under normalization (verified numerically).
- S_7 features were excluded due to the known feature leak at N=10^6 (always zero for mod-5 functions).
</challenges>
<discussion>
The data show two distinct things. (1) At the level of individual ω-strata magnitudes, F12 and the DH family are dramatically different: F12 produces systematically larger normalized log|S_k| values across k=1..5, with the lower-ω strata (S_1–S_3) being completely separated. This is consistent with the r21–r25 view that M_jk / S_k features encode coefficient arithmetic (conductor primes, coefficient magnitudes), and F4/F5 (mod-5 DH-type perturbations of zeta) and F12 (an explicit GRH-violator built differently) have fundamentally different coefficient arithmetic.
(2) Despite this, the *shape* of the S_k spectrum, captured by the s2/s3 ratio, is nearly the same in both families — a signature of the common underlying "main sum dominated by low-ω terms" structure. So the specific feature proposed in the hypothesis (s2/s3 ratio) is *not* the discriminator between violator families; rather, the absolute levels are.
The cross-family AUC=1.0 result indicates that, *for the simple task of distinguishing a violator from zeta*, F4 and F12 are not actually antagonistic — both sit far from F1 in the same direction. The r25 generalization failure must therefore reside elsewhere (e.g., distinguishing violators from non-zeta GRH-true L-functions like F9–F11, or in a more constrained held-out protocol).
</discussion>
<proposed-next-hypotheses>
1. The r25 generalization failure is driven not by F4-vs-F12 differences but by overlap between violator families and the modular L-functions F9/F10/F11: an RBF SVM trained on {F1, F4} will misclassify F9/F10/F11 peaks as violators, while training on {F1, F4, ..., F11} (all GRH-true) will recover discrimination.
2. A degree/conductor-aware re-normalization that subtracts the family mean of log|S_k| (per (d,q)) will collapse the DH-family and F12 distributions onto a common manifold while preserving separation from GRH-true classes — effectively turning the s2/s3-style ratio into a robust, family-invariant violator signature.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>r26_DH_vs_F12_KS_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Summary table of two-sample Kolmogorov–Smirnov tests comparing the DH-family (F4, F5p, F5m; n=600) vs F12 (n=200) on the normalized log|S_k| features (k=1..6) plus the engineered s2_s3_ratio feature. Columns: feature, KS_stat, p_value, DH_mean, F12_mean. Generated in this analysis from peaks_features_F1_F12_normalized_full.csv using scipy.stats.ks_2samp.</artifact-description>
</artifact>
<artifact>
<file-name>r26_DH_vs_F12_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel figure summarizing the cross-family analysis. Panel A: bar chart of KS statistics for DH family vs F12 across S_1..S_6 normalized features and the s2/s3 ratio, annotated with p-values. Panel B: histograms of s2_s3_ratio for the two families with the cross-family SVM AUCs in the title. Confirms that S_1–S_4 magnitudes are completely separated (KS=1.0) while the s2/s3 ratio is nearly identical (KS=0.14).</artifact-description>
</artifact>
</artifacts>
</output>
