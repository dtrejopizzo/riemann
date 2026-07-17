## Overview <output>
<conclusion>
A One-Class SVM trained only on log|S_k|_norm features (k=1..6) of GRH-true peaks identifies unseen GRH-violator families as anomalies with AUC = 0.844 for the F4/F5p/F5m family and AUC = 0.953 for F12, satisfying the >0.80 threshold in both LOFO folds and demonstrating substantially better cross-family generalization than the binary classifiers reported in r48.
</conclusion> <methods>
1. Loaded `peaks_features_F1_F12_normalized_full.csv` (2200 peaks × 11 classes, 200 each).
2. Defined GRH-true classes = {F1, F2, F6, F7, F9, F10, F11} (1400 peaks) and violator families F4-fam = {F4, F5p, F5m} (600 peaks) and F12 (200 peaks).
3. Used the six normalized log-magnitude features `log_abs_S{1..6}_norm`, deliberately excluding S7 (known feature leak at N=10⁶ for mod-5 coefficient classes per r25) and S0 (trivially zero by normalization).
4. Standardized features with `StandardScaler` fit on GRH-true peaks. Trained an RBF One-Class SVM (`sklearn.svm.OneClassSVM`).
5. Tuned ν via 5-fold cross-validation on the GRH-true training set, selecting ν by calibration: matching the held-out outlier fraction to the nominal ν. With γ='scale', ν=0.1 was the best-calibrated reasonable choice (held-out outlier fraction 10.4% vs. nominal 10%). Final hyperparameters: ν=0.1, γ='scale', kernel='rbf'.
6. LOFO evaluation: in each fold, the model trained on GRH-true peaks scored all peaks. The anomaly score = −decision_function. AUC computed via `roc_auc_score` with violator family peaks labeled positive (anomaly) and GRH-true peaks labeled negative (normal).
7. Performed sensitivity analysis over ν ∈ {0.025, 0.05, 0.1, 0.15, 0.2}, per-class AUC breakdown, and an "all violators combined" evaluation.
</methods> <results>
- LOFO Fold A (violators = F4/F5p/F5m, GRH-true = F1,F2,F6,F7,F9,F10,F11): AUC = 0.844.
- LOFO Fold B (violator = F12): AUC = 0.953.
- Per-class AUC (vs. GRH-true): F4 = 0.844, F5p = 0.841, F5m = 0.848, F12 = 0.953.
- All violators pooled vs. GRH-true: AUC = 0.871.
- Per-class outlier fractions (decision_function < 0): GRH-true classes range 1.5–31.5% (F10 lowest, F6 highest); violators are flagged at 60–61% (F4/F5p/F5m) and 91% (F12). Mean decision scores are strongly negative for all four violator classes (−2.2 to −3.8) and positive for all seven GRH-true classes (0.4 to 3.2).
- Sensitivity over ν (γ='scale'): AUC_F4-fam ranges 0.66 (ν=0.025) → 0.83 (ν=0.05) → 0.84 (ν=0.1) → 0.83 (ν=0.2). AUC_F12 ranges 0.97 → 0.97 → 0.95 → 0.94. The hypothesis (>0.80 in both folds) holds for all ν ≥ 0.05.
- Cross-validated calibration (γ='scale'): nominal ν = 0.10 → observed held-out outlier fraction = 0.104, indicating well-calibrated boundary.
</results> <challenges>
- The objective frames this as "LOFO" but it is asymmetric: only the GRH-violator side is held out (the GRH-true training set is identical in both folds), since the OCSVM is trained on normal data only. This is the natural reading and was implemented as such.
- One-Class SVM AUC depends mainly on γ; ν primarily shifts the offset of the decision boundary. Reported AUCs are robust across reasonable ν but degrade at very small ν (ν=0.025) for F4-family.
- Within the GRH-true set, F6 and F7 produce notably lower decision scores than the other five classes, indicating heterogeneity inside the "normal" manifold; this is the main source of false positives and limits the F4-family AUC. A larger or more representative GRH-true training panel could likely raise that AUC further.
- Tuning ν purely by self-calibration avoids any peeking at violators, but means we cannot guarantee globally optimal AUC; we instead report sensitivity to ν.
</challenges> <discussion>
The one-class anomaly-detection paradigm meaningfully outperforms the binary discriminative approach used in r48, which exhibited asymmetric LOFO failure (a model trained on F12 violators could not recognize F4-family violators and vice versa). Here, a single anomaly model trained without ever seeing a violator achieves AUC ≥ 0.84 against both violator families. This supports the rationale that GRH-true peaks occupy a relatively coherent manifold in the log|S_k| feature space, and that GRH violation manifests as a generic departure from this manifold rather than as a particular alternative class structure. The asymmetry between F12 (AUC 0.95) and the F4/F5/F5m family (AUC 0.84) suggests that the F4-style mod-5 violators sit closer to the boundary of the GRH-true manifold than the F12 construction does — consistent with prior observations that mod-5 violators share substantial structure with mod-5 GRH-true forms (F2). The result also reinforces that the log|S_k| features, although crude bulk magnitudes, encode a robust geometric signature of GRH compliance that generalizes across constructions.
</discussion> <proposed-next-hypotheses>
1. Augmenting the OCSVM features with phase/cross-term information from the complex S_k(t) vectors (e.g., projections onto eigenvectors of the class-averaged M_jk matrix, available in `Sk_complex_all_2200peaks.npz`) will close the gap between F4-family AUC (0.84) and F12 AUC (0.95) by exploiting differences in the angular structure of GRH-true vs. violator peaks.
2. The remaining false-positive rate for GRH-true classes is concentrated in F6 and F7 (the higher-degree GRH-true L-functions), suggesting that the GRH-true "normal manifold" is degree-stratified; training separate one-class detectors per degree (or feeding degree as a covariate) will reduce GRH-true false positives and increase overall LOFO AUC.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ocsvm_grh_violator_detection.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: ROC curves for the two LOFO folds of the One-Class SVM (trained on GRH-true peaks with ν=0.1, γ='scale', features log|S_k|_norm for k=1..6). Panel B: Boxplots of OCSVM anomaly scores (= −decision_function) per class, with GRH-true classes (green) clearly below the decision boundary at 0 and GRH-violator classes (red) above it.</artifact-description>
</artifact>
</artifacts>
</output>
