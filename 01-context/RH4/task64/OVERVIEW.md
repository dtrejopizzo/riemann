## Overview <output>
<conclusion>
Eigenvector‑projection features substantially beat the instantaneous‑spectral baseline (AUC≈0.59) but only modestly improve on the log|S_k| baseline (best AUC=0.851 vs 0.828) — they do not provide a markedly superior peak‑level classifier under the Strict Protocol.
</conclusion> <methods>
1. Loaded complex S_k(t) arrays (k=0..7) for 200 peaks/class for the 11 function classes (F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) from the per‑class .npy files in the working directory and verified row‑wise t alignment with `peaks_features_F1_F12_normalized_full.csv`. Used k=1..6 throughout to avoid the documented N=10⁶ S_7 leak (and excluded the trivially constant k=0).
2. For each class, computed the cross‑term matrix M_jk = E_t[Re(S_j(t) conj(S_k(t)))] = Re((Sᵀ conj(S))/N) on its 200 peaks. Built `M_true_avg = ½(M_F1 + M_F9)` (training GRH‑true classes) and `M_false_avg = M_F4` (training GRH‑false class).
3. Eigendecomposed both 6×6 symmetric matrices with `np.linalg.eigh`. Top eigenvalues: M_true=[87.45, 2.53, 1.09] (95.5% / 2.8% / 1.2%); M_false=[35.23, 1.51, 0.88] (92.3% / 4.0% / 2.3%). Took top 2 and top 3 eigenvectors as bases.
4. For each of the 2200 peaks, projected its complex 6‑vector S(t) onto each real basis vector v and computed |v·S|² (squared projection magnitude).
5. Augmented the main feature table with 6 new columns (`proj_true_v{1..3}_sq`, `proj_false_v{1..3}_sq`) and saved as `peaks_features_F1_F12_with_projection_features.csv`.
6. Trained an RBF SVM (`SVC(kernel='rbf', probability=True)` in a `StandardScaler` pipeline) on Strict Protocol: train F1+F4+F9 (n=600), test F2+F6+F7+F10+F11+F12 (n=1200). Positive class = GRH‑violating. Tested three projection variants (raw and log of |·|² with 3 eigenvectors per matrix; log with 2 eigenvectors per matrix) and the published baseline (`log_abs_S{1..6}_norm`). Computed 95% bootstrap CIs (n=2000 resamples on the 1200 test points) and paired bootstrap p‑values for the AUC differences vs baseline (n=4000).
</methods> <results>
Strict Protocol held‑out AUCs (positive class = GRH‑violating):
- Instantaneous spectral, reported r38: AUC ≈ 0.59
- Baseline log|S_k|_norm, k=1..6 (6 features): AUC = 0.828, 95% CI [0.805, 0.850]
- Projection, 3 evec(true)+3 evec(false), raw |·|² (6 feat): AUC = 0.822, 95% CI [0.799, 0.844]
- Projection, 3 evec+3 evec, log |·|² (6 feat): AUC = 0.840, 95% CI [0.818, 0.862]
- Projection, 2 evec+2 evec, log |·|² (4 feat): AUC = 0.851, 95% CI [0.830, 0.872] ← best Paired bootstrap differences vs baseline:
- 3‑evec log projection: ΔAUC = +0.012, 95% CI [−0.012, +0.037], p ≈ 0.31 (not significant)
- 2‑evec log projection: ΔAUC = +0.023, 95% CI [+0.001, +0.046], p ≈ 0.04 (marginally significant) All projection variants vastly exceed the 0.59 instantaneous‑spectral baseline; none reach the perfect AUC=1.0 obtained from class‑level spectral features (which is expected since those depend on class‑averaged statistics rather than per‑peak data).
</results> <challenges>
- The dataset on disk consisted of per‑class .npy files (rather than a single Sk_complex_all_2200peaks.npz) — required reconstruction by stacking and verifying alignment against the master CSV.
- S_7 is identically zero at N=10⁶ for mod‑5 coefficient classes (F2, F4, F5±) — a known feature leak (r25); restricted analysis to k=1..6.
- Projection features are highly skewed (squared magnitudes spanning orders of magnitude); a log transform was needed for SVM kernel scaling and provided a meaningful AUC improvement over raw values.
- The leading eigenvector dominates each M_jk (>92% of the variance), so 1‑D and 2‑D projection bases capture nearly all spectral content — adding the 3rd eigenvector slightly hurt held‑out AUC, consistent with overfitting to training‑class‑specific subleading directions.
- Statistical comparison vs the baseline is underpowered: even the best variant has only a ~0.02 AUC margin and 95% CI overlap, so claims of significant superiority should be cautious.
</challenges> <discussion>
The hypothesis is only partially supported. Projecting per‑peak complex S_k onto eigenvectors of class‑averaged M_jk does dramatically outperform the instantaneous‑spectral approach (r38), confirming that geometry learned from the class‑level success transfers something useful to the peak level. However, against the established log|S_k| baseline (~0.83), the gain is at best marginal (+0.02 AUC for the 4‑feature 2‑evec variant; not significant for the 6‑feature variant). Mechanistically this is unsurprising: the leading eigenvector of M_true (and of M_false) is dominated by mid‑k components and is tightly correlated with the overall log|S_k| profile that the baseline already captures. The subleading eigenvectors carry phase‑sensitive structure that does not generalize cleanly to held‑out families — paralleling the r34 caveat that the perfect AUC of class‑level spectral features is a centroid‑separation effect rather than evidence that individual peaks from unseen families are linearly separable. Bottom line: the projection construction is a useful feature‑engineering idea — it cleanly beats naive instantaneous spectra and nearly matches the magnitude baseline with fewer features (4 vs 6) — but it does not unlock a qualitatively superior peak‑level classifier under Strict Protocol. Genuine improvement likely requires either more eigenvectors estimated from many GRH‑false training classes (we only had F4) or genuinely peak‑level (non‑centroid) structure such as cross‑peak phase correlations.
</discussion> <proposed-next-hypotheses>
1. Building the GRH‑false template from multiple training violators (e.g., F4 plus a held‑in subset of F5p/F5m or F12) rather than F4 alone will yield projection features whose Strict‑Protocol AUC exceeds 0.88, by mitigating the single‑class bias of M_false.
2. Replacing the squared projection magnitude |v·S|² with phase‑aware features (Re(v·S), Im(v·S), and the relative phase between top‑1 GRH‑true and top‑1 GRH‑false projections) will produce a peak‑level classifier whose AUC (a) significantly exceeds the log|S_k| baseline and (b) does not collapse under Leave‑One‑Family‑Out evaluation, evidencing genuinely peak‑level (non‑centroid) discrimination.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>peaks_features_F1_F12_with_projection_features.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>The 2200×37 main feature table (`peaks_features_F1_F12_normalized_full.csv`) augmented with six new per‑peak features: proj_true_v{1,2,3}_sq (squared magnitudes of complex S_k(t) projected onto the top‑3 eigenvectors of M_true_avg = ½(M_F1+M_F9)) and proj_false_v{1,2,3}_sq (analogous projections onto eigenvectors of M_false_avg = M_F4). Computed using k=1..6 of the complex S_k arrays loaded from the per‑class .npy files. Eigendecomposition via numpy.linalg.eigh on the 6×6 symmetric M_jk = Re((SᵀS̄)/N) matrices.</artifact-description>
</artifact>
<artifact>
<file-name>projection_features_strict_protocol.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two‑panel summary figure: (A) ROC curves on the 1200‑peak Strict‑Protocol test set for baseline log|S_k|_norm vs 2‑evec and 3‑evec log‑projection feature sets; (B) bar chart of held‑out AUCs with 95% bootstrap confidence intervals, including the reported instantaneous‑spectral baseline (0.59) for comparison.</artifact-description>
</artifact>
</artifacts>
</output>
