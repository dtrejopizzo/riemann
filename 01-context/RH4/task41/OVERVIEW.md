## Overview <output>
<conclusion>
The scale-invariant amplification-ratio features (a_k(t)=|S_k(t)|²/C_k) substantially repair Fold 1 of the LOFO protocol (AUC 0.29 → 0.75) but degrade Fold 2 (AUC 0.86 → 0.72), so the hypothesis that they yield AUC > 0.85 on both folds is NOT supported.
</conclusion>
<methods>
1. Loaded complex ω-stratified sums S_k(t) (k=0..7) for the 200 highest peaks of each of 11 classes (F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) from per-class .npy files derived from Sk_complex_all_2200peaks.npz, plus the 11×8 matrix of theoretical second moments C_k from Ck_Mkk_diag_results.npz.
2. For each peak, computed the rank-1 instantaneous diagonal m_kk(t)=|S_k(t)|² and the scale-invariant amplification ratios a_k(t)=m_kk(t)/C_k. Following the documented S_7-leak (mod-5 classes have C_7≈0 and S_7=0 at N=10⁶), restricted features to k=0..6 (7 features per peak; a_0≡1 retained as a no-op constant for transparency).
3. Implemented two LOFO folds exactly as in r48: Fold 1 trains on GRH-true classes (F1, F2, F6, F7, F9, F10, F11) plus F12 (positives = F12) and tests on GRH-true ∪ F4-family (F4, F5p, F5m) with positives = F4-family; Fold 2 trains on GRH-true plus F4-family (positives = F4-family) and tests on GRH-true ∪ F12 (positives = F12).
4. Classifier: scikit-learn 1.8.0 Pipeline of StandardScaler + LogisticRegression (max_iter=5000, C=1.0). Sensitivity sweep over C∈{0.01,0.1,1,10}, class_weight∈{None, balanced}, and {raw, log1p, log-clip} feature transforms confirmed best-case AUCs are unchanged in conclusion.
5. AUC computed via sklearn.metrics.roc_auc_score on decision-function scores.
</methods>
<results>
- Fold 1 (train F12, test F4-family): AUC = 0.748 (best across hyperparameter sweep = 0.771 with C=10, class_weight=balanced, raw).
- Fold 2 (train F4-family, test F12): AUC = 0.716 (best across sweep = 0.721).
- Comparison vs r48 magnitude baseline (log|S_k|): Fold 1 0.29 → 0.75 (+0.46, large gain, classifier no longer anti-correlated); Fold 2 0.86 → 0.72 (−0.14, regression).
- Both folds are below the hypothesis threshold AUC>0.85.
- Class-wise mean profiles (figure panel B) show why: F4/F5p/F5m have nearly identical, low amplification at k=3,4 (a_3≈8.9, a_4≈16.4), whereas F12 sits at a_3≈13, a_4≈23 — close to F2 and intermediate between GRH-true and F4-family. The two violator families therefore have systematically different amplification scales even after C_k normalization, so a binary boundary fit on one violator family does not transfer cleanly to the other.
- Sample sizes: Fold 1 train n=1600 (200 positive), test n=2000 (600 positive); Fold 2 train n=2000 (600 positive), test n=1600 (200 positive).
</results>
<challenges>
- Direct division by C_k for k=7 is undefined for mod-5 classes (C_7=0 due to the documented S_7 feature-leak at N=10⁶); restricted features to k=0..6, leaving 7 (rather than the planned 8) features per peak.
- a_0 ≡ 1 by construction (C_0 = 1 = |S_0|² for all classes), so it carries no information; kept for transparency but contributes nothing.
- Features are highly right-skewed (max≈386, mean≈14), but log/log1p transforms did not improve test AUC.
- Only 200 peaks per class limits statistical power for very rare positives (F12: 200 train or test instances).
</challenges>
<discussion>
The amplification-ratio normalization successfully removes the catastrophic anti-correlation seen in Fold 1 of r48 (AUC 0.29 → 0.75), confirming the qualitative intuition that dividing by C_k brings violator families onto a more comparable footing. However, the residual class-conditional structure of a_k still differs systematically between the F4-family and F12: F12's amplification profile most closely resembles F2 (a GRH-true class) at k=1,2 and is distinctly larger than F4-family at k=3,4. A linear classifier trained on F4-family thus learns a boundary near GRH/F4-family separation that misses F12, and conversely. The hypothesis that scale-invariant amplification ratios alone solve the asymmetric LOFO failure is therefore refuted: they reduce, but do not eliminate, the family-specific amplification structure. A peak-level classifier robust to held-out violator families likely requires features that capture the *shape* of the a_k spectrum (e.g., ratios a_k/a_{k-1}, spectral entropy, or peak-of-peak indices) rather than its absolute level, or features derived from the full complex S_k including phase information.
</discussion>
<proposed-next-hypotheses>
1. A classifier built on the *shape* of the amplification spectrum — specifically log-ratios r_k = log(a_{k+1}/a_k) for k=1..5 — will achieve AUC > 0.85 on both LOFO folds because these ratios are invariant under a multiplicative class-specific scale.
2. Concatenating amplification-ratio features with spectral-entropy and argmax-stratum statistics of the a_k vector will close the asymmetric LOFO gap, because F12 and the F4-family differ in which ω-stratum carries peak amplification (k=4 for F12 vs k=4 with shallower curvature for F4-family).
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>lofo_amplification_ratio_results.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: bar chart comparing r48 baseline AUCs (0.29, 0.86) against amplification-ratio AUCs (0.75, 0.72) on the two LOFO folds, with the 0.85 hypothesis target marked. Panel B: heatmap of class-wise mean amplification ratios a_k=⟨|S_k|²⟩/C_k for k=0..6 across the 11 classes, showing the residual systematic differences between the F4 and F12 violator families that explain why the hypothesis is not met.</artifact-description>
</artifact>
</artifacts>
</output>
