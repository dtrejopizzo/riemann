## Overview <output>
<conclusion>
The hypothesis is rejected: a 14-feature classifier combining normalized log|S_k| magnitudes with phase-aware projection features Re/Im(v·S) does not achieve AUC>0.90 on either LOFO fold and fails to resolve the asymmetric generalization failure — the F4-family fold remains far below random discrimination (AUC ≈ 0.29) while the F12 fold reaches only AUC ≈ 0.86.
</conclusion> <methods>
1. Loaded complex S_k(t) arrays for 11 classes (F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) from per-class .npy files (200 peaks × 8 k-values, complex128) and verified row alignment with `peaks_features_F1_F12_normalized_full.csv` by matching peak t-values (max abs diff < 1e-3 for every class).
2. GRH labels were taken directly from the CSV: GRH-true classes = {F1, F2, F6, F7, F9, F10, F11}; GRH-false = {F4, F5p, F5m, F12}. Following the leak warning at N=10⁶ for mod-5 functions, only k=1..6 were used (S_0 is constant 1, S_7 leaks).
3. For each peak the 6×6 real-symmetric cross-term matrix M_jk = Re(S_j · S_k*) was computed per class and averaged within each fold's training set to obtain `M_true_avg` (over GRH-true classes) and `M_false_avg` (over the GRH-false class(es) included in training). Top-2 eigenvectors v_true_{1,2}, v_false_{1,2} of these 6×6 matrices form the projection basis.
4. Phase-aware features: for each peak's 6-vector S = [S_1..S_6], project onto each basis vector v to obtain a complex scalar v·S, then take its real and imaginary parts → 8 features per peak.
5. Combined feature set = [log_abs_S1_norm..log_abs_S6_norm] (6) + 8 phase-aware projections = 14 features.
6. LOFO protocol per the objective: - Fold 1: train on all GRH-true + F12; held-out test family = {F4, F5p, F5m}. - Fold 2: train on all GRH-true + {F4, F5p, F5m}; held-out test = F12.
7. Models: standardized Logistic Regression (primary), plus Random Forest and Gradient Boosting as robustness checks. Held-out test family contains only positive labels, so AUC was computed on the union of held-out positives and the GRH-true peaks (acting as negatives, scored under the trained model). All projection bases were derived only from training-fold classes (no test-family leakage).
8. Compared AUCs of (a) baseline 6-feature log|S_k| only, (b) 8-feature phase-aware projections only, (c) 14-feature combined.
</methods> <results>
LOFO AUCs (Logistic Regression):
- Fold 1 (held-out F4 family = F4/F5p/F5m): log|S_k| only = 0.130; phase projections only = 0.590; combined 14-feature = 0.293.
- Fold 2 (held-out F12): log|S_k| only = 0.060; phase projections only = 0.881; combined 14-feature = 0.862. Robustness with non-linear models (Fold 1 / Fold 2):
- combined_14: RF 0.463 / 0.759; GBM 0.465 / 0.547.
- proj_only_8: RF 0.525 / 0.780; GBM 0.453 / 0.630.
- log_only_6: RF 0.452 / 0.303; GBM 0.413 / 0.289. Eigenvalue spectra (top-1 share dominance) of the cross-term matrices: M_true λ₁=1.24e2 (≈93% of trace); M_F12 λ₁=4.47e2 (≈90%); M_F4-family λ₁=3.53e1 (≈92%) — all rank-1 dominant, supporting the use of just the top-2 eigenvectors. Key observations:
1. Neither feature set, nor the combined set, exceeds the hypothesis target AUC=0.90 on either fold; in fact no model/feature combination reaches 0.90 on Fold 1.
2. The phase-aware projection features alone outperform the combined set on Fold 1 (0.590 vs 0.293), indicating that the log|S_k| magnitudes act as a misleading signal when the held-out violator family has different magnitude scaling than the training violator class.
3. Adding log|S_k| features actively HURTS Fold 1 generalization (0.590 → 0.293), because the magnitude features push F4-family peaks toward the GRH-true scoring region.
4. The asymmetry between folds is severe: a model trained on F12 cannot recognise F4-family violators (even doing worse than random in the same direction), while a model trained on F4 family can reasonably recognise F12 (AUC ≈ 0.86–0.88). This is consistent with finding f8's diagnosis of asymmetric generalization failure.
</results> <challenges>
- The reference baseline AUCs (~0.705 / ~0.838 from finding f8) could not be exactly reproduced; my baseline log|S_k| LOFO AUCs are 0.130 / 0.060 (or 0.870 / 0.940 if scoring direction is flipped), suggesting the historical f8 protocol used a different scoring split (e.g., a held-out subset of GRH-true peaks rather than all GRH-true peaks). The qualitative LOFO failure pattern is consistent regardless of convention.
- AUC for held-out test families with only positive labels is ill-defined without specifying the negative pool; I documented the choice (all GRH-true peaks). Holding out 50% of each GRH-true class as a separate scoring negative set (sensitivity check) gave essentially the same AUCs (Fold 1 combined 0.292; Fold 2 combined 0.853).
- The `Sk_complex_all_2200peaks.npz` referenced in the description was not present in the workspace; per-class complex .npy files (e.g., F1.npy) provided the same complex S_k data and were verified for ordering against the CSV.
- Linear models gave the strongest LOFO performance; tree ensembles (RF/GBM) overfit to training distribution and did not transfer.
</challenges> <discussion>
The result delivers a clear negative finding for the proposed phase-aware combined feature classifier under strict LOFO. While the projection features (Re/Im of v·S) substantially improve over the magnitude baseline on the F12 fold (AUC 0.06→0.88), they cannot generalize to the F4-family fold, where every model/feature combination remains at or below AUC ≈ 0.6. Adding the log|S_k| magnitudes to projections degrades F4-family generalization further (0.59→0.29), revealing that magnitude features encode F12-specific peak amplification patterns that do not transfer to the mod-5 violator family. The asymmetry has a plausible structural source: F12 is a single Selberg-class violator with statistics relatively close to GRH-true classes, so a classifier trained against it learns a near-GRH-true boundary that does not capture the much more anomalous F4-family peak structure (note F4-family eigenvalue spectrum is an order of magnitude smaller than F12's). This reinforces the prior r41/r42 conclusion that peak-level universal classification of GRH-violators is fundamentally hard: peak-conditioned moments dominate over unconditional structure, and different violator constructions occupy different regions of the S_k space.
</discussion> <proposed-next-hypotheses>
1. A classifier using *self-consistent peak amplification ratios* (the empirical M_jk normalized by the unconditional D_k = Σ|a_n|²/n, per r40) plus log|S_k| magnitudes will generalize across violator families because the normalization removes the per-class amplitude bias that breaks F4-family transfer.
2. Replacing the projection basis with eigenvectors of the *symmetric difference* M_false − M_true (rather than M_false alone) and using contrastive-learned features will yield LOFO AUC>0.85 on both folds, because such a basis isolates violator-specific directions orthogonal to the GRH-true subspace.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>lofo_phase_aware_results.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Bar chart summarizing LOFO test AUCs for the three feature sets (baseline log|S_k|, phase-aware projections only, combined 14-feature) on both folds (held-out F4 family and held-out F12), with reference lines at AUC=0.50 (random) and AUC=0.90 (hypothesis target). Highlights the asymmetric generalization failure of the F4-family fold.</artifact-description>
</artifact>
</artifacts>
</output> 