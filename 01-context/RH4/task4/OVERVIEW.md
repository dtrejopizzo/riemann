## Overview <output>
<conclusion>
Spectral features of the class-averaged cross-term matrix yield a numerically higher held-out AUC than raw log|S_k| magnitudes under the strict protocol (logreg AUC 0.60 vs 0.08, RF 0.80 vs 0.18), but the wide class-bootstrap 95 % CIs ([0.20, 1.00] vs [0.02, 0.18]) and a small held-out class set (n = 6) make the improvement suggestive rather than statistically conclusive.
</conclusion> <methods>
1. Loaded peaks_features_F1_F12_normalized_full.csv (2200 rows × 31 cols, 11 classes × 200 peaks).
2. Important caveat: the CSV stores only magnitudes |S_k| (column abs_Sk), not complex S_k. The exact M_jk = E[Re(S_j · conj(S_k))] cannot be reconstructed; we therefore computed the closest available class-level proxy M_jk = E[|S_j| · |S_k|] (8×8 symmetric PSD) by averaging over the 200 peaks of each class.
3. For each of 11 classes diagonalised M_jk with numpy.linalg.eigvalsh; clipped tiny negative eigenvalues to 0; computed pc1_variance_fraction = λ₁/Σλᵢ and eigenvalue_entropy = −Σ pᵢ log pᵢ with pᵢ = λᵢ/Σλⱼ.
4. Joined the two scalar spectral features back to every row by class label and saved peaks_features_F1_F12_normalized_full_with_spectral.csv (2200 × 33).
5. Applied the r25 “Strict Protocol” split: train = {F1, F4, F9}; test = {F2, F6, F7, F10, F11, F12}; target = ¬GRH (predict GRH-false). Following the r25 memo, the S_7 column was excluded from the log|S_k| feature set (feature leak at N = 10⁶).
6. Fit StandardScaler + LogisticRegression (C = 1, max_iter = 2000) on three feature sets: (a) log_abs_S0..S6_norm, (b) {pc1_variance_fraction, eigenvalue_entropy}, (c) union. Repeated with RandomForest (300 trees) as a non-linear sanity check.
7. Reported held-out ROC-AUC and a class-stratified bootstrap 95 % CI (n = 2000) drawing 6-class samples with replacement from the test classes — the appropriate level of resampling because rows are nested within class.
</methods> <results>
Class-level spectral features (selected):
- F1 (GRH-T) pc1=0.984, H=0.097; F2 (T) 0.986/0.085; F9 (T) 0.986/0.085; F10 (T) 0.990/0.064; F11 (T) 0.988/0.076.
- F4 (F) 0.971/0.164; F5p (F) 0.971/0.165; F5m (F) 0.971/0.164; F12 (F) 0.973/0.151.
- F6 (T) 0.969/0.161; F7 (T) 0.972/0.148 ← intrude into the GRH-false region. Strict-protocol held-out AUC (logistic regression):
- log|S_k| only (S0..S6): AUC = 0.081, 95 % CI (class-boot) [0.018, 0.177].
- spectral only: AUC = 0.600, 95 % CI [0.200, 1.000].
- combined: AUC = 0.601, 95 % CI [0.203, 1.000]. Random-forest sanity check: AUC log|S_k| = 0.176, spectral = 0.800, combined = 0.726. Per-class mean P(GRH-false) for spectral-only logreg:
F12 0.967 (TP), F6 0.997 (FP), F7 0.970 (FP), F2 0.0008 (TN), F10 0.00004 (TN), F11 0.0002 (TN) → sensitivity 1/1, specificity 3/5. The log|S_k|-only AUC < 0.5 (anti-correlated) reproduces the r25 finding that magnitude features fail under class-held-out validation; spectral features are at least correctly oriented and concentrate GRH-false classes (F4, F5±, F12) toward low pc1 / high entropy, while most GRH-true L-functions (F1, F2, F9–F11) sit at high pc1 / low entropy.
</results> <challenges>
- Major data limitation: only |S_k| magnitudes are stored in peaks_features_F1_F12_normalized_full.csv, so the literal definition M_jk = E[Re(S_j·conj(S_k))] could not be evaluated; we used M_jk = E[|S_j||S_k|] as a proxy. The complex-valued S_k arrays would be required to compute the exact matrix and its (potentially signed) spectrum.
- Spectral features are class-level constants — within a class all 200 rows share identical values. The effective sample size for the spectral classifier is therefore the 6 held-out classes, which is why the class-stratified bootstrap CI spans [0.20, 1.00].
- Two GRH-true modular-symmetric-square-like classes (F6, F7) sit in the same spectral region as the constructed GRH violators, producing systematic false positives.
- S_7 column had to be excluded for log|S_k| features per the documented mod-5 feature leak at N = 10⁶.
- Training set of only 3 classes (one of which, F4, is the sole GRH-false training class) limits how much generalisable boundary the model can learn.
</challenges> <discussion>
Under strict class-held-out evaluation, raw log|S_k| magnitudes are not just uninformative — they are anti-aligned with GRH status (AUC ≈ 0.08), corroborating the r21–r25 conclusion that M_jk readouts mostly reflect coefficient arithmetic (conductor primes, coefficient magnitudes) rather than zero-distribution physics. Spectral features (pc1 fraction, entropy) flip the sign of the signal: they cleanly separate the additively perturbed zeta classes (F4, F5±, F12) from zeta-like / modular L-functions (F1, F2, F9–F11) and so correctly classify F12. They also resolve the f16 ambiguity in the right direction — spectral features generalise better than magnitudes — but at the same time they are confounded by L-function degree/conductor structure: GRH-true F6 and F7 (whose Sato–Tate measure differs from the U(1) case) project into the same low-pc1 / high-entropy region as the GRH violators. The result is that spectral features encode “distance from the unitary/zeta-like statistical regime,” which correlates with but is not identical to GRH status. The wide class-bootstrap CIs make a definitive ranking premature: spectral features are a strict improvement on magnitudes, but they do not yet provide a reliable GRH discriminator on this 11-class corpus.
</discussion> <proposed-next-hypotheses>
1. The spectral “distance-from-unitary” signal is degree- and Sato–Tate-driven: regressing pc1_variance_fraction and eigenvalue_entropy on (degree d, conductor q, symmetry type) will explain ≥ 80 % of inter-class variance, leaving negligible residual variance attributable to GRH status.
2. Recomputing M_jk from the complex-valued S_k arrays (preserving phase information) and restricting eigen-decomposition to off-diagonal-driven components will yield spectral features that distinguish F12 from F6/F7 — i.e. the phase, not the amplitude, of cross-terms is what carries the GRH-violation signature.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>peaks_features_F1_F12_normalized_full_with_spectral.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Augmented version of the r25 strict-protocol feature table (2200 rows × 33 columns) with two additional columns, pc1_variance_fraction and eigenvalue_entropy, computed per class from the eigenvalue spectrum of the class-averaged matrix M_jk = E[|S_j||S_k|] (a magnitude proxy for the canonical cross-term matrix, since complex S_k values were not available in the source CSV).</artifact-description>
</artifact>
<artifact>
<file-name>strict_protocol_spectral_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON summary of held-out ROC-AUC and class-stratified bootstrap 95 % CIs for the three logistic-regression feature sets (log|S_k| only, spectral only, combined) under the strict r25 protocol (Train: F1, F4, F9 → Test: F2, F6, F7, F10, F11, F12), plus random-forest sanity-check AUCs.</artifact-description>
</artifact>
<artifact>
<file-name>spectral_vs_logS_strict_protocol.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) per-class scatter of pc1_variance_fraction vs eigenvalue_entropy coloured by GRH status; (B) bar chart of held-out AUC with class-bootstrap 95 % CIs for the three feature sets.</artifact-description>
</artifact>
</artifacts>
</output>
