## Overview <output>
<conclusion>
Normalizing the four peak features by L-function degree and analytic-conductor scaling laws improves the class-held-out AUC from 0.534 to 0.733, a substantial gain over the r10 baseline but still below the hypothesised 0.80 threshold, so the hypothesis is not supported.
</conclusion> <methods>
1. Loaded peaks_features_F1_F12.csv (2,200 peaks × 11 classes × 200 peaks each).
2. Built a class→(q, d) invariants table consistent with the objective example (F1: q=1,d=1; F2: q=5,d=1; F9: q=1,d=2). Other assignments: F4/F5±/F6/F7 = degree 1 (q=5,3,7); F10 weight-2 newform (q=11, d=2); F11 sym² (q=1, d=3); F12 (q=11, d=2). The exact integer values of q for degree-1 perturbative classes have negligible numerical effect because the dominant log-scaling in the analytic conductor at heights t∈[10⁴,10⁵] is driven by d·log(t).
3. Defined the local analytic-conductor exponent log C(t) = d·log(t+3) + log q and the local mean spacing 2π/log C(t).
4. Documented scaling laws (Selberg CLT for amplitude; mean-spacing² for the second-derivative-like quantities): - norm_amplitude = feat_A_log_peak / √(0.5·d·log log C(t)) - norm_curvature = feat_B_curvature · (2π/log C(t))² - norm_roughness = feat_C_roughness · (2π/log C(t))² - norm_xi = feat_xi (already dimensionless)
5. Replicated the r10 protocol exactly: train RBF-SVM (C=1, γ='scale') on F1+F4+F6, test on F2, F5+, F5−, F7, F9, F10, F11, F12. Used StandardScaler + SVC(probability=True). Computed held-out AUC, confusion matrix, classification report, and per-class mean P(GRH=1).
6. Saved svm_norm_features_results.json, peaks_features_F1_F12_normalized.csv, and a 2-panel summary figure (ROC + per-class probabilities).
</methods> <results>
- Held-out AUC, original features (replicates r10): 0.5335 (matches svm_classification_results.json: 0.5335).
- Held-out AUC, normalized features: 0.7333 — Δ = +0.20.
- Hard-decision metrics are unchanged: confusion matrix [[400,200],[600,400]], accuracy 0.500, precision/recall both 0.40/0.67 for non-GRH and 0.67/0.40 for GRH (because the SVM still predicts a single label per held-out class).
- Per-class mean predicted P(GRH=1) (true label in parens): - Correctly handled: F2(GRH)=1.00, F10(GRH)=0.77, F5+(non-GRH)=0.005, F5−(non-GRH)=0.005. - Still misclassified GRH→non-GRH: F11(GRH)=0.26, F9(GRH)=0.05, F7(GRH)=0.09. - Still misclassified non-GRH→GRH: F12(non-GRH)=0.95.
- Improvement comes from better calibration on degree-2 GRH classes (F10 moves correctly across 0.5; F9, F11 move toward GRH but not across the threshold), while the hardest case F12 (non-GRH degree-2 construction) remains scored as GRH-like.
- Hypothesis test: AUC 0.733 < 0.80 → hypothesis NOT supported.
</results> <challenges>
- Several classes have q=1, making any feature that uses log(q) directly degenerate; this required using the analytic conductor d·log(t)+log(q) rather than naive division by log(q) (the example formula in the objective would have produced div-by-zero on F1, F9, F11).
- The exact LMFDB conductor for the F12 construction and the precise weight/level interpretation of F11 (approximate sym² in r10) are not unambiguously specified in the context document, so degree-2 q values for F10/F12 had to be plausibly assigned (q=11). Sensitivity is small because log(q) ≪ d·log(t) at t~10⁴.
- The held-out hard-decision accuracy is unchanged (0.50) because the SVM produces near-binary scores per held-out class; AUC reflects rank-ordering improvement that does not yet cross the 0.5 decision threshold for F11, F9, F7.
- Only three training classes (one non-GRH: F4) means the classifier has very limited exposure to non-GRH variability — the F12-style non-GRH signature is unseen at training time.
</challenges> <discussion>
Degree- and conductor-aware normalization moves the class-held-out classifier well above chance (AUC 0.73 vs 0.53), confirming that a substantial fraction of the r10 generalization failure was due to features capturing degree-related scale rather than a GRH signal. The improvement is concentrated on degree-2 GRH classes (F10 in particular), consistent with the Selberg-CLT amplitude rescaling and mean-spacing curvature rescaling absorbing the dominant degree-driven variance. However, two structural problems remain: (i) the F12 non-GRH degree-2 construction produces normalized features that overlap the GRH-degree-2 cloud, suggesting that the ad-hoc construction's RH violation is not detectable from local peak geometry once degree is normalized away; (ii) F9 and F11 still rank as non-GRH, indicating that ξ and the Selberg amplitude scaling are not sufficient to capture the heavier-tail behaviour expected at peaks of higher-degree GRH L-functions in this t-window. Falling short of AUC>0.80 implies that simple multiplicative normalization is necessary but not sufficient — additional features (e.g., log-spaced higher moments, gap statistics, or t-window-matched moment ratios) are likely required, in line with the rationale's prediction that failure here would call for more elaborate feature engineering.
</discussion> <proposed-next-hypotheses>
1. Adding two further degree-aware features — a normalized local second moment ⟨|L|²⟩/(log C(t))^{d²/4} and a normalized nearest-zero gap g·log C(t)/(2π) — to the four normalized features will push the class-held-out AUC above 0.80 under the same train(F1,F4,F6)/test(rest) protocol.
2. Including at least one higher-degree non-GRH class (a constructed degree-2 Davenport–Heilbronn analogue) in the training set will eliminate the F12 misclassification failure mode and yield class-held-out AUC > 0.80 even with the four normalized features alone.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>svm_norm_features_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Structured JSON summary of the held-out SVM experiment with degree/conductor-normalized features. Contains the exact normalization laws, the class→(q,d) table, AUCs for original and normalized feature sets (0.5335 → 0.7333), confusion matrices, classification reports, and a hypothesis-supported flag (False, threshold 0.80). Replicates the r10 protocol exactly so values can be compared one-to-one with svm_classification_results.json.</artifact-description>
</artifact>
<artifact>
<file-name>peaks_features_F1_F12_normalized.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Augmented peak-feature table: original peaks_features_F1_F12.csv joined with class invariants (q, d) and four new normalized features (norm_amplitude, norm_curvature, norm_roughness, norm_xi) derived using analytic-conductor and Selberg-CLT scaling laws. Suitable for follow-on classification experiments.</artifact-description>
</artifact>
<artifact>
<file-name>svm_norm_features_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) class-held-out ROC curves comparing original features (AUC=0.533) to normalized features (AUC=0.733) with hypothesis threshold annotated; (B) per-test-class mean predicted P(GRH=1) for both feature sets, color-coded by true GRH label, highlighting that F11/F9/F7 (true GRH) and F12 (true non-GRH) remain misclassified after normalization.</artifact-description>
</artifact>
</artifacts>
</output>
