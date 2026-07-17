## Overview <output>
<conclusion>
The proposed 6-D spectral feature vector does not lift the GRH-true centroid degeneracies: the 12-class macro-OvR AUC plateaus at ≈0.937 and never crosses the 0.95 target at any sample size, and the minimum inter-class distance among GRH-true centroids (d(F10,F11)=0.39 in standardized 6-D) is smaller than the bootstrap noise (≈0.7–0.9) at n=30.
</conclusion> <methods>
1. Loaded complex S_k arrays for 11 classes (F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) — supplied as per-class .npy files (200×8 complex128 each), unpacked from Sk_complex_all_2200peaks.npz — and the F14 array S_complex.npy. Total: 12 classes × 200 peaks × 8 k-modes.
2. For each class, computed the cross-term matrix M_jk = E[Re(S_j · conj(S_k))] over k=1..6 (6×6, symmetric), averaging over the 200 peaks of that class.
3. Built a 6-D feature vector per class: • Top-3 normalized eigenvalue magnitudes |λ_i|/Σ|λ| from M (using numpy.linalg.eigvalsh because M is symmetric). • Three signed off-diagonal entries of the correlation matrix C = M / sqrt(diag·diagᵀ) with the largest |·|.
4. Sample-size analysis (1-NN to class prototypes): • Split each class into a 100-peak prototype set and 100-peak test pool (random permutation, seed=1). • Prototypes computed once from prototype set; standardized via StandardScaler. • For n ∈ {3,5,10,…,200}, drew 200 bootstrap samples of n peaks per class from its test pool, recomputed M and the 6-D feature, classified by negative Euclidean distance to each prototype. • Macro one-vs-rest AUC computed manually (binary AUC per class then averaged) to avoid softmax probability-renormalization artifacts.
5. Computed pairwise standardized centroid distances and bootstrap noise distributions (mean and std of feature-to-centroid distance, n=30, 500 draws).
6. Repeated the protocol for the GRH-true subset {F1, F9, F10, F11}.
</methods> <results>
• Macro 12-class OvR AUC vs n (selected): n=10:0.821, n=20:0.892, n=30:0.914, n=50:0.931, n=80:0.937, n=100:0.932, n=150:0.936, n=200:0.937. The curve plateaus at ≈0.937 and never reaches 0.95.
• Per-class AUC at n=50 reveals the bottleneck: F10=0.750, F5m=0.860, F4=0.897, F5p=0.898, F6=0.932; F1, F2, F7, F12, F14 all ≥ 0.99.
• Centroid distances (standardized 6-D) show two strongly-degenerate clusters: – Mod-5 family (F4, F5p, F5m): pairwise distances 0.06–0.17 (essentially identical features). – GRH-true cluster (F9, F10, F11): d(F10,F11)=0.39, d(F9,F11)=0.45, d(F9,F10)=0.77; F1 stands ≈ 1.9–2.6 from this trio.
• Bootstrap noise at n=30 (Euclidean stdev ≈ mean): F1≈0.50, F9≈0.68, F11≈0.79, F10≈0.88, F4/5≈1.09. The minimum GRH-true centroid distance (0.39) is well below the noise scale (~0.7–0.9), confirming non-resolution at n=30.
• GRH-true 4-class subset AUC: n=30 gives only 0.65; n=50 gives 0.66, far from 0.95.
• Comparison to r41 baseline: the 2-D (pc1, H) space reportedly required n≈150 to reach AUC>0.95; the 6-D space does not reach 0.95 at any n tested up to 200.
</results> <challenges>
• sklearn's roc_auc_score with multi_class='ovr' rejected raw negative-distance scores because they are not row-normalized probabilities; using softmax to satisfy the API also distorts cross-column rankings. The robust fix was to compute binary OvR AUC manually per class and average.
• Leave-one-out re-computation of the in-class prototype on shrinking remainder caused asymmetric noise that artificially lowered AUC at large n; replaced with a fixed 100-peak prototype / 100-peak test split for clean scaling.
• F8 is missing from Sk_complex_all_2200peaks.npz (only 11 of 13 classes present); together with F14 we obtain 12 classes — matching the objective's "12-class" framing.
• The mod-5 family (F4, F5p, F5m) and the GRH-true (F9, F10, F11) both produce near-identical 6-D features. This is a genuine geometric limitation of the chosen feature, not a numerical artifact: their full M_jk diagonals also scale almost identically.
</challenges> <discussion>
The hypothesis fails on both criteria. (i) The 6-D feature vector compresses each class's M_jk to a near-rank-1 spectral fingerprint: λ_1/Σ|λ| sits in 0.89–0.96 for every class and the top-3 off-diagonal correlations all sit at 0.85–0.99. The dominant rank-1 structure of M_jk previously noted in r40 is exactly what makes top-3 eigenvalue magnitudes weakly informative — they encode essentially one number, the leading eigen-fraction. (ii) The GRH-true classes (F1, F9, F10, F11) lie on a thin manifold in this 6-D space; F9/F10/F11 form a tight cluster (pairwise distance 0.39–0.77) that is below the n=30 bootstrap noise. So degeneracy persists, and classification at n=30 remains impractical for these classes.
A practical implication is that further progress likely requires features that are (a) sensitive to higher-order structure (e.g., off-diagonal sign patterns, eigenvector angles, or off-diagonal entries beyond the leading three), or (b) peak-conditioned moments rather than class-averaged moments, since r39/r42 already showed that unconditional theory is a poor predictor of high-peak statistics.
</discussion> <proposed-next-hypotheses>
1. Including the leading eigenvector direction (the 6-vector in k-space, not just |λ_1|) — yielding ≈10 features after sign/phase normalization — will separate F9/F10/F11 because their leading directions tilt differently across k-modes despite similar λ_1 fractions.
2. Replacing class-averaged M_jk with peak-conditioned moments E[Re(S_j conj(S_k)) | |S_2| > τ] for an appropriate amplitude threshold τ will reveal class-specific structure that is invisible in unconditional averages, as predicted by the peak-conditioning discrepancy reported in r39.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>class_features_6D.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-class 6-D spectral feature table (12 classes × {lam1,lam2,lam3,off1,off2,off3}). lam_i are top-3 normalized eigenvalue magnitudes of the 6×6 M_jk (k=1..6) and off_i are the three signed off-diagonal entries of the correlation matrix M_jk/√(M_jj M_kk) with largest absolute value, computed from the full 200 peaks per class.</artifact-description>
</artifact>
<artifact>
<file-name>sample_size_analysis_6D.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy archive containing the sample-size sweep (ns, aucs_12 for n=5..200), the standardized 12×12 centroid distance matrix, the class label list, and the bootstrap-noise mean/std (n=30, 500 draws) per class. Generated by a fixed 100-peak prototype / 100-peak test-pool split with seed=1, 1-NN distance scoring, and manual macro OvR AUC.</artifact-description>
</artifact>
<artifact>
<file-name>final_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. (A) Macro OvR AUC vs sample size in 6-D feature space showing plateau at ≈0.937, never crossing the 0.95 target line; r41 reference (2-D, n≈150) marked. (B) 12×12 standardized centroid distance heatmap with per-class bootstrap noise (n=30) annotated on the diagonal in red, highlighting F9/F10/F11 and F4/F5p/F5m as residual degeneracy clusters.</artifact-description>
</artifact>
</artifacts>
</output>
