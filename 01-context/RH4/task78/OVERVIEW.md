## Overview <output>
<conclusion>
On the unified, range-matched dataset, the One-Class SVM trained on core GRH-true peaks (F1,F2,F9,F10) shows a clear, quantifiable generalization gap — held-out GRH-true AUC=0.894 vs. in-sample AUC=0.983 — partially supporting the hypothesis: the gap is real and family-driven (F6 is the offender), but the failure is much milder than reported in r73 once data inconsistency is removed.
</conclusion> <methods>
1. Loaded the 11 per-function `Sk_*.npy` arrays (each shape (200, 8) complex128) and metadata (N=10⁶, n_peaks=200, t∈[10⁴,2·10⁴], k_range=0–7) that constitute the unified range-matched peaks artifact described as `unified_range_matched_peaks_F1-F12.npz`.
2. Verified known data leaks: S₀ is class-constant (no zeros) and S₇ is identically zero for mod-5-conductor functions (F2, F4, F12, plus F5±). Excluded both.
3. Built leak-controlled feature matrix X = log(|S_k| + 1e-300) for k ∈ {1,2,3,4,5,6}, giving a 6-dim feature per peak.
4. Defined splits per the r73 protocol: - Train (core GRH-true): F1, F2, F9, F10 → 800 peaks. - Test violators: F4, F12 → 400 peaks. - Test held-out GRH-true: F6, F7 → 400 peaks.
5. Standardized features with `StandardScaler` fit on the training set and applied to all test sets.
6. Fit `sklearn.svm.OneClassSVM(nu=0.1, gamma='scale')` on the standardized training peaks.
7. Computed anomaly scores as −decision_function(X). Computed ROC AUC for (a) violators vs held-out GRH-true and (b) violators vs in-sample GRH-true (control).
8. Performed per-pair AUC breakdown (each violator vs each held-out family) to localize the generalization failure.
9. Produced a 2-panel summary figure (ROC curves + per-family anomaly-score boxplots).
</methods> <results>
- AUC, violators (F4,F12) vs held-out GRH-true (F6,F7): **0.894**.
- AUC, violators vs in-sample GRH-true (F1,F2,F9,F10) (control): **0.983**.
- Generalization gap: ΔAUC = 0.089 (in-sample minus held-out). Per-pair breakdown (the gap is dominated by F6):
- F4 vs F6: AUC = 0.735
- F12 vs F6: AUC = 0.883
- F4 vs F7: AUC = 0.963
- F12 vs F7: AUC = 0.994 Per-family mean anomaly scores and outlier rates (decision boundary at 0):
- F1: −1.28 (15.5% flagged), F2: −1.60 (7.0%), F9: −1.77 (8.0%), F10: −1.81 (9.0%) — training fits ν=0.1 closely.
- F7 (held-out GRH-true): −1.89 (10.0% flagged) — indistinguishable from training.
- F6 (held-out GRH-true): +2.01 (66.5% flagged) — almost entirely classified as anomaly.
- F4 (violator): +4.60 (93.0% flagged); F12 (violator): +6.72 (99.5% flagged) — strongly detected. Comparison to r73: r73 reported a near-complete failure of the held-out generalization (AUC near chance), driven in part by data inconsistency (heterogeneous N, t-range, peak rules). On the unified, range-matched dataset:
- The held-out AUC rises from ~chance to 0.894, a substantial improvement attributable to data consistency.
- However, the in-sample/held-out gap (0.983 → 0.894) and the F6-specific failure (best AUC 0.735) persist, even with consistent data.
</results> <challenges>
- The single `.npz` artifact was not present on disk; the data existed as separate `.npy` files in the workspace root (per-function `Sk_*.npy`, `amp_peaks_*.npy`, `t_peaks_*.npy`, plus metadata). I reconstructed the dataset by loading the individual files.
- The dataset includes F5p and F5m (not requested in the protocol) and lacks F3, F8, F13. Only the 11 named files were used; the protocol's 11 listed functions map cleanly onto the available files.
- Verified the S₀/S₇ leak structure empirically: S₇ is identically zero exactly for the mod-5-conductor functions (F2, F4, F5p, F5m, F12), confirming that excluding S₇ is essential to avoid trivial separation.
- One-Class SVM AUC has no standard error from a single fit; the per-family AUCs (n=200 per side) and tight boxplots indicate the result is not driven by a few outliers.
- No randomness in OC-SVM with `gamma='scale'`; result is deterministic.
</challenges> <discussion>
The hypothesis is supported in direction but tempered in magnitude. Cleaning up data inconsistency dramatically improves held-out generalization (from near-chance in r73 to AUC ≈ 0.89), confirming that a substantial fraction of the previously reported failure was a methodological artifact. Yet a clear, family-specific generalization gap remains, almost entirely localized to F6: F6's peaks systematically receive high anomaly scores (mean +2.0; 66.5% beyond the learned boundary) despite being GRH-true, while F7 is statistically indistinguishable from the core training families. This is consistent with the broader finding (r48, r63, r67, r73) that leak-controlled spectral features encode *how* an L-function is constructed (its arithmetic family, conductor, weight, twist structure), not just whether GRH holds. The residual ΔAUC ≈ 0.09 thus represents a genuine, structural limit on the universality of OC-SVM-based anomaly detection in this feature space, not a data-quality artifact. Practically: the OC-SVM remains a strong family-conditional detector and even retains useful (but no longer near-perfect) cross-family detection power on the unified data, with F6 being the family whose log|S_k| geometry most diverges from the F1/F2/F9/F10 manifold.
</discussion> <proposed-next-hypotheses>
1. F6's deviation from the core GRH-true manifold in log|S_k| feature space is driven by a specific structural property (e.g., its weight, level, or root-number sign); peak-conditioned ω-stratified statistics for F6 will differ from F1/F2/F9/F10 in a way predictable from its functional-equation parameters, and including a second F6-like family in training will close the held-out AUC gap to within in-sample noise.
2. Augmenting the feature set with phase or argument features of S_k(t) (e.g., arg(S_k) or Re/Im decompositions) at peak locations will increase held-out AUC for violators-vs-held-out-GRH-true above 0.95 without re-introducing leakage, indicating that violator detectability lives in spectral phase coherence rather than in amplitude alone.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ocsvm_lofo_unified.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: ROC curves for the One-Class SVM (trained on F1,F2,F9,F10 leak-controlled log|S_k| features for k=1..6) discriminating violators (F4,F12) from in-sample GRH-true (AUC=0.983) and from held-out GRH-true F6,F7 (AUC=0.894). Panel B: per-family anomaly-score boxplots showing F6 is the source of the held-out gap (mean +2.0, 66.5% flagged), while F7 is indistinguishable from the training distribution.</artifact-description>
</artifact>
</artifacts>
</output>
