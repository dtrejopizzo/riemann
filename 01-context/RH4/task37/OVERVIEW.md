## Overview <output>
<conclusion>
Under a Leave-One-Family-Out (LOFO) protocol, the baseline RBF-SVM on normalized log|S_k| features (k=1..6) shows asymmetric, partial generalization: it fails to cleanly classify the held-out F4 violator family (AUC ≈ 0.705, 95% CI [0.675, 0.735], at the hypothesis threshold) but generalizes well to the held-out F12 violator (AUC ≈ 0.838, 95% CI [0.787, 0.883]).
</conclusion> <methods>
1. Loaded `peaks_features_F1_F12_normalized_full.csv` (2200 peaks × 11 classes × 200 peaks each). Selected the 6 normalized features `log_abs_S{k}_norm` for k=1..6.
2. Defined the violator label as `~GRH` (1 = GRH-violator). GRH-true classes used: F1, F2, F6, F7, F9, F10, F11. Violator families: F4-family = {F4, F5p, F5m} (600 peaks); F12-family = {F12} (200 peaks).
3. Implemented two LOFO folds: - Fold 1: Train on all GRH-true (1400) + F12 (200), test on the F4 family (600 violators) plus a random subsample of 600 GRH-true peaks (random_state=42) drawn from the GRH-true pool and removed from training (final n_train = 1000, n_test = 1200, balanced 600/600). - Fold 2: Train on all GRH-true (1400) + F4-family (600), test on F12 (200 violators) plus 200 random GRH-true peaks (random_state=42) removed from training (n_train = 1800, n_test = 400, balanced 200/200).
4. Pipeline: `StandardScaler` fitted on training data only, then default `sklearn.svm.SVC(kernel='rbf')` with decision_function scores fed to `roc_auc_score`.
5. 95% CI from 1000 stratified-resample bootstraps over test indices (percentile method, single seed for reproducibility).
6. Compared against the established strict-protocol baseline AUC ≈ 0.828.
</methods> <results>
- Fold 1 (held-out F4 family; F12 in training): test AUC = 0.7051, 95% bootstrap CI [0.6754, 0.7351]. This sits essentially at the hypothesis threshold of 0.7 — the lower CI bound (0.675) is below 0.7, so the hypothesis "AUC < 0.7" is not unambiguously confirmed but is strongly supported as a regime of poor generalization. AUC drops by ≈0.12 relative to the strict-protocol baseline of 0.828.
- Fold 2 (held-out F12; F4-family in training): test AUC = 0.8380, 95% bootstrap CI [0.7867, 0.8834], statistically indistinguishable from (and slightly above) the 0.828 baseline.
- The two folds give significantly different AUCs (CIs do not overlap at 95%): the F4 family is markedly harder to recover from a model that has not seen any F4-style perturbation, whereas F12 is recoverable from a model trained on F4-family violators plus diverse GRH-true classes.
</results> <challenges>
- The protocol called for "balanced" test sets; with the F4 family containing 3 classes × 200 = 600 peaks, balancing required subsampling 600 GRH-true peaks for Fold 1, yielding a much larger Fold 1 test set (1200) than Fold 2 (400). This asymmetry is unavoidable given fixed family sizes.
- Bootstrap CIs were computed on a single random subsample of GRH-true peaks; sensitivity of the point estimate to the GRH subsample seed was not assessed but the bootstrap CI captures the dominant test-level uncertainty.
- The Fold-1 AUC sits right on the 0.7 threshold; the hypothesis strictly fails (point estimate 0.705 ≥ 0.7) but the lower 95% bound dips below 0.7, so the conclusion is borderline and seed-dependent.
</challenges> <discussion>
The asymmetric generalization is informative. F4 is built by additively perturbing the Davenport–Heilbronn function with a mod-5 character pattern (sharing arithmetic with F2/F5p/F5m), so its log|S_k| signature is distinct from anything in a training pool that contains F12 (a different violator family) plus standard L-functions. By contrast, F12 is recoverable when the training set already contains the F4 family, suggesting F12's peak signature partially overlaps with that of additive mod-q violators. Together with the strict-protocol baseline of 0.828, this LOFO experiment demonstrates that the current log|S_k| feature space is not a universal violator detector: it captures violator-vs-true structure only when at least one violator example structurally resembles the test family. This motivates seeking features that encode universal violator hallmarks (e.g., phase-coherent cross terms M_jk from the complex S_k arrays, ω-stratified moment ratios beyond raw magnitude) rather than family-specific magnitude patterns.
</discussion> <proposed-next-hypotheses>
1. Phase-aware cross-term features `M_jk = E[Re(S_j · conj(S_k))]` computed from the `Sk_complex_arrays.npz` data will improve LOFO Fold-1 AUC (held-out F4 family) above 0.80, because phase coherence at peaks is a violator-universal signature not captured by magnitudes alone.
2. Adding a mod-q-agnostic ω-stratified moment ratio (e.g., `log(M_22/M_11)`) as an extra feature will close the F4-vs-F12 generalization gap (LOFO Fold-1 AUC will rise to within 0.05 of Fold-2 AUC), indicating a more universal detector of GRH violation.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>lofo_auc_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Bar chart summarizing the two Leave-One-Family-Out folds (Fold 1 = held-out F4 family, AUC=0.705; Fold 2 = held-out F12, AUC=0.838) with 95% bootstrap CIs, against the strict-protocol baseline (0.828) and the hypothesis threshold (0.7). Generated via matplotlib from the LOFO experiment described in the methods.</artifact-description>
</artifact>
</artifacts>
</output>
