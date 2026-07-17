## Overview <output>
<conclusion>
The degree-stratified One-Class SVM detector with the prescribed max-combiner does NOT support the hypothesis: while F12 detection improves marginally to AUC=0.972, F4-family detection collapses to AUC=0.526, far below both the baseline (0.844) and the 0.90 target.
</conclusion> <methods>
Loaded `peaks_features_F1_F12_normalized_full.csv` (2200 rows × 31 cols, 11 classes × 200 peaks). Used the six normalized log-magnitude features `log_abs_S{1..6}_norm` (k≥7 excluded due to the documented mod-5 zero-leak at N=10⁶). Split GRH-true peaks by L-function degree:
- Train_D1 (degree 1): F1, F2, F6, F7 — 800 peaks
- Train_D2+ (degree ≥ 2): F9 (d=2), F10 (d=2), F11 (d=3) — 600 peaks
Each set was z-scored with its own `StandardScaler`, then a `OneClassSVM(kernel='rbf', gamma='scale', nu=0.1)` was fit. For every peak, anomaly score was defined as `-decision_function` (higher ⇒ more anomalous). The combined score, per the spec, is `max(s_D1, s_D2)` (peak flagged anomalous if either model flags it). AUCs were computed for two binary tasks: F4-family (F4∪F5p∪F5m, n=600) vs GRH-true (n=1400), and F12 (n=200) vs GRH-true. As a sensitivity analysis, an alternative `min`-combiner (peak normal if either manifold accepts it) was also evaluated. Implementation: scikit-learn 1.8.0.
</methods> <results>
Per-class mean anomaly scores reveal the failure mode (panel B): the D2 OCSVM assigns very high anomaly to ALL degree-1 classes regardless of GRH status — F1=5.80, F2=4.77, F6=5.84, F7=3.81 (true), F12=6.27, F4=2.68, F5p=2.63, F5m=2.73 (false). The D1 OCSVM correctly separates degree-1 violators from degree-1 GRH-true (F4≈1.28, F5p≈1.22, F5m≈1.34, F12≈1.55 vs F1=−1.09, F2=−1.00, F6=−0.52, F7=−0.88), but assigns small (≤0) anomaly to degree-≥2 GRH-true classes. Under the prescribed max-combiner, the score is dominated by D2 for every degree-1 peak, so F4/F5p/F5m violators (max≈2.7) are RANKED LOWER in anomaly than degree-1 GRH-true peaks (F1/F2/F6 max≈4.8–5.8), inverting the discrimination:
| Detector | F4-family AUC | F12 AUC |
|---|---|---|
| Baseline single OCSVM (r52) | 0.844 | 0.953 |
| Stratified, max-combiner (prescribed) | **0.526** | **0.972** |
| D1 model alone | 0.828 | 0.940 |
| D2 model alone | 0.536 | 0.972 |
| Stratified, min-combiner (sensitivity) | 0.853 | 0.958 | Hypothesis target (>0.90 for both families): F4-family False (0.526), F12 True (0.972) ⇒ **rejected** under the prescribed protocol. Even the most favorable combiner tested (min) only reaches F4-family AUC=0.853 (slight gain over 0.844), still below 0.90.
</results> <challenges>
The semantic ambiguity of "max" vs "min" combiner is a critical issue: anomaly detection by max(score) means a peak must satisfy BOTH degree manifolds to be considered normal — but a degree-1 GRH-true peak is, by construction, NOT in the degree-≥2 manifold, and vice versa, so the max-combiner labels nearly every peak as anomalous via whichever model is "wrong" for its degree, inverting the F4-family ranking. The proper combination for stratified anomaly detection is min(anomaly) = "normal if any manifold accepts it", but the spec explicitly mandates max. Both were therefore reported. No data quality issues; the OCSVM training was deterministic and stable.
</challenges> <discussion>
The result reveals a fundamental flaw in the stratification hypothesis as operationalized: degree is so strong a structural signal that an OCSVM trained on degree-2/3 coefficients treats ALL degree-1 inputs as anomalous, and vice versa. Under the prescribed max-combiner, this destroys signal because GRH-true degree-1 peaks (F1/F2/F6/F7) get LARGER cross-manifold anomaly than the (degree-1) GRH-violator F4 family. The min-combiner, which is the theoretically correct choice for "two-component normal manifold" anomaly detection, yields only a marginal F4-family improvement (0.853 vs 0.844) and a slight F12 regression (0.958 vs 0.953), and still fails to clear the 0.90 bar for F4. Thus the proposition that degree alone defines the "normal" manifold strata — and that two RBF OCSVMs with default ν=0.1 capture this stratification well enough to drive both AUCs above 0.90 — is not supported. The F6/F7 false-positive issue noted in r52 is real, but degree-stratification does not remove it; F6/F7 are degree-1 like F4, so they fall in the same D1 manifold. A more nuanced stratification (e.g., by conductor, by symmetry type, or by motivic family) or a different anomaly architecture (mixture-of-OCSVMs with a probabilistic combiner, or contamination-aware One-Class methods) is likely required.
</discussion> <proposed-next-hypotheses>
1. Stratifying the "normal" manifold by symmetry type (orthogonal/symplectic/unitary) rather than by degree will yield tighter OCSVM boundaries, with the symmetry-stratified detector using a min-combiner achieving F4-family AUC > 0.90 while preserving F12 AUC > 0.95.
2. The dominant source of F4/F5p/F5m mis-detection is structural similarity to the Davenport–Heilbronn-class tail behavior of F6 (Liouville) and F7 (Möbius); excluding F6 and F7 from the GRH-true training set will increase F4-family AUC of the original single OCSVM to > 0.90 without harming F12 AUC.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>stratified_ocsvm_results.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: AUC bars comparing the r52 baseline single OCSVM, the prescribed max-combined stratified detector, and a sensitivity min-combiner, for F4-family and F12 violator detection, with the 0.90 target line. Panel B: per-class mean anomaly scores from the D1- and D2-trained OCSVMs (x-tick labels colored by GRH status), illustrating that the D2 model pathologically inflates the anomaly of all degree-1 classes (true and false), which collapses the F4-family AUC under the max-combiner.</artifact-description>
</artifact>
</artifacts>
</output>
