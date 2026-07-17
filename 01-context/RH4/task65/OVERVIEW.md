## Overview <output>
<conclusion>
The hypothesis is rejected: adding log|S_j|/log|S_k| ratio features (j,k ∈ {1..4}) to the baseline log|S_k| feature set degrades, rather than improves, class-held-out generalization, with a strict-protocol test AUC of 0.705 (95% CI [0.678, 0.733])—well below both the 0.85 target and the 0.828 baseline.
</conclusion> <methods>
1. Loaded `peaks_features_F1_F12_normalized_full.csv` (2200 rows × 31 cols; 200 peaks for each of 11 classes F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12).
2. Baseline pipeline replication: SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42) preceded by StandardScaler. Trained on F1+F4+F9 (n=600), tested on the main and strict held-out class sets, with positive class = GRH-false (violator). This faithfully reproduced r25's reported numbers (train AUC 0.9809; main 0.9143; strict 0.8278), confirming the model specification.
3. Constructed 12 log-ratio features `logS{j}_div_logS{k}` = log|S_j| / log|S_k| for j,k ∈ {1,2,3,4}, j≠k, computed from raw (un-normalized) log-magnitudes consistent with the hypothesis text. No NaN/inf values arose because no log|S_k| in [1..4] equals zero in this table.
4. Ran three feature configurations under both protocols: - Baseline: 6 normalized log|S_k| features (k=1..6). - Augmented: baseline + 12 log-ratio features. - Ratios-only: 12 log-ratio features.
5. Computed test AUC and 1000-iteration percentile bootstrap (seed=42) 95% CIs over the test set, matching r25's CI methodology.
6. Saved JSON summary `hypothesis_AUC_ratio_features.json` and a final comparison figure `ratio_features_AUC_comparison.png`.
</methods> <results>
Baseline reproduction (sanity check):
- Train AUC = 0.9809; Main test AUC = 0.9143 (CI [0.901, 0.927]); Strict AUC = 0.8278 (CI [0.806, 0.850]) — all within rounding of r25. Baseline + log-ratio features (the hypothesis's proposed model):
- Train AUC = 0.9895 (slightly higher → mild overfitting).
- Main test AUC = 0.8780 (95% CI [0.862, 0.893]); Δ = −0.036 vs baseline.
- Strict test AUC = 0.7049 (95% CI [0.678, 0.733]); Δ = −0.123 vs baseline.
- The strict 95% CI lies entirely below 0.85 (margin of ≥0.117), so the hypothesis is rejected with strong statistical confidence. Ratios-only (ablation):
- Main test AUC = 0.7346 (CI [0.709, 0.758]); Strict AUC = 0.5712 (CI [0.533, 0.604]) — barely above chance, indicating the ratio features alone do not encode a generalizable GRH signature. Direction of effect: ratio features increased train AUC slightly but lowered held-out AUC, characteristic of features that fit training-class peculiarities (F1/F4/F9) but fail to transfer to novel classes—the same generalization failure mode the hypothesis sought to remedy.
</results> <challenges>
- The exact r25 model specification (kernel, hyperparameters, scaling) was not recorded in any saved artifact; I reconstructed it as RBF SVC with default C/gamma plus StandardScaler. This was validated by exact reproduction of r25's reported AUCs (train 0.9809; main 0.9143; strict 0.8278), giving high confidence the comparison is apples-to-apples.
- The hypothesis text specified ratios of log magnitudes (log|S_j|/log|S_k|); since log|S_k| values can be negative, these ratios mix sign information that is not naturally bounded. No undefined values arose for k∈{1..4}, but this representation is part of why the ratios may not behave as cleanly as intended.
- No grid search over SVM hyperparameters was performed; with the augmented feature space, a different (C, γ) might mitigate but is unlikely to overcome a 12-point AUC gap or close the 14-point distance to the 0.85 threshold.
</challenges> <discussion>
The proposed remedy—ratios designed to be scale-invariant and capture internal stratum structure—does not improve, and in fact substantially harms, class-held-out generalization in this setting. Several non-mutually-exclusive explanations are plausible: (i) the existing `_norm` features are already degree-/conductor-corrected per the r14 normalization scheme, so ratios add redundancy plus noise rather than new structure; (ii) ratios of log magnitudes amplify variance when one log|S_k| is small (near zero crossing) and thereby inject high-leverage features that the SVM keys on for training-class idiosyncrasies; (iii) consistent with the project's recurring finding (r21–r25), the M_jk-derived S_k strata reflect the function's coefficient arithmetic (conductor primes, mod structure) rather than its zero locations, so any nonlinear combination of S_k features inherits this confound. Together, these results reinforce the documented conclusion that GRH violation (zero off-axis behavior) is not detectable from coefficient-arithmetic features alone, and that simple algebraic feature engineering on top of S_k is unlikely to bridge the gap. The strict protocol with F12 as the sole novel violator remains the discriminating benchmark, and on it the hypothesis cleanly fails.
</discussion> <proposed-next-hypotheses>
1. Zero-statistic features (e.g., nearest-neighbor zero-spacing distributions, or low-lying zero residuals after subtracting GUE expectations on an interval [T, T+H]) computed directly from each function's L-values—rather than coefficient-driven S_k strata—will yield strict-protocol AUC > 0.85 with F12 held out, because they probe the actual zero geometry GRH constrains.
2. Replacing log|S_k| with peak-localized phase or argument coherence statistics (e.g., circular variance of arg(S_k) across the top-200 peaks at fixed k) will be more robust to family-specific scaling than the current magnitude-based features and will narrow the train-vs-strict-test AUC gap by at least 0.05 absolute.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>hypothesis_AUC_ratio_features.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON record of the ratio-feature held-out experiment: lists the 6 baseline normalized log|S_k| features, the 12 added log|S_j|/log|S_k| ratio features (j,k ∈ {1..4}, j≠k), train/test class splits, the SVC model specification, and the train/main/strict test AUCs with 1000-iter percentile-bootstrap 95% CIs for three feature configurations (baseline reproduced, baseline+ratios, ratios-only). Also records the verdict (hypothesis rejected) with the negative effect size (ΔAUC = −0.123 on the strict protocol).</artifact-description>
</artifact>
<artifact>
<file-name>ratio_features_AUC_comparison.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Bar chart comparing held-out test AUC (with bootstrap 95% CIs) under the main and strict protocols across three feature configurations: baseline log|S_k|, baseline + log-ratio features, and ratios-only. Includes the 0.85 hypothesis-threshold reference line, visually demonstrating that the ratio-augmented model falls below baseline on both protocols and that its strict-protocol CI lies entirely below the 0.85 target.</artifact-description>
</artifact>
</artifacts>
</output>
