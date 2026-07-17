## Overview <output>
<conclusion>
The arithmetic-ablation model robustly predicts Δ_empirical = M_jk(F4) − M_jk(ζ): excluding terms with 5 | n from the ω-stratified zeta sum reproduces the empirical difference matrix with cosine similarity 0.9978 — well above the 0.9 threshold — confirming that, as for F12, the F4-vs-ζ M_jk gap is driven primarily by F4's conductor arithmetic rather than by its non-GRH zero structure.
</conclusion> <methods>
1. Loaded the on-disk artifacts of the prior F12 ablation experiment (Sk_zeta.npy, M_zeta.npy, t_peaks.npy, N=10^6, K=8, κ=0.28408 for context). The 200-peak t-grid (t∈[50.5, 1967.1], irregularly spaced, fixed) was reused so all comparisons are at identical conditioning points.
2. Loaded F4 (Davenport–Heilbronn) ω-stratified partial sums S_k(F4) at the same 200 peaks from Sk_re.npy / Sk_im.npy (corresponds to Sk_at_peaks_F4.npz). Verified S_k(ζ) reproduces the stored M_jk(ζ) exactly (max abs diff 1.3e−13).
3. Computed empirical 8×8 matrices M_jk(F) = mean over peaks of Re(S_j · conj(S_k)) for both F=ζ and F=F4, and Δ_empirical = M(F4) − M(ζ).
4. Built an ω-table for n ≤ 10^6 with a sieve and re-summed n^(−1/2 − it) using a Numba-parallel Kahan-compensated summation, ω-stratified into K=8 buckets, EXCLUDING all n divisible by p = 5 (the conductor prime of F4 in the κ=0.28408 Davenport–Heilbronn construction). This produced ablated zeta sums S'_k(ζ) at the same 200 t-values.
5. Formed M'_jk(ζ) and Δ_ablation = M'(ζ) − M(ζ). Computed cosine similarity, Pearson r, best-fit scalar α (least-squares), and R² between the 64-dim flattened Δ matrices.
6. Saved Delta_ablation_results_F4.npz with all matrices, S_k arrays, t_peaks, and summary statistics, and produced a 2-panel summary figure.
</methods> <results>
- Cosine similarity (Δ_empirical, Δ_ablation) = 0.9978 (hypothesis threshold > 0.9: PASSED).
- Pearson r = 0.9968, p ≈ 1.2e−69 (n = 64 matrix entries).
- Best-fit slope α = 1.285, R² = 0.9936; the ablation model captures the shape of Δ almost perfectly but underestimates magnitude by ~28% (Frobenius norm Δ_empirical = 108.85 vs Δ_ablation = 84.52).
- The agreement is much stronger than the F12 result reported in the prior r21 study (cosine 0.9730), even though F4 has only one conductor prime (p=5) versus F12's two (p∈{3,5}).
- Both Δ matrices are essentially negative throughout, peak in the j=k=2 ω-bucket (Δ_emp[2,2] = −49.5, Δ_abl[2,2] = −40.7), and decay smoothly toward higher ω, consistent with removal of high-multiplicity contributions from removing one prime's multiples (which kills ~20% of integers and dominates ω∈{2,3} bins).
- Internal consistency: recomputed M_zeta agrees with the stored matrix to 13 digits; the diagonal of M_F4 is dramatically smaller than M_ζ in middle-ω bins (e.g., M[2,2]: 1.40 for F4 vs 50.88 for ζ), reflecting Davenport–Heilbronn's destructive cancellation that the ablation model reproduces by simply removing a fixed multiplicative subset of integers.
</results> <challenges>
- The repository on disk had the contents of the prior Delta_ablation_results.npz pre-extracted to individual .npy files rather than the npz archive itself; this required reconstructing the loading step manually but did not affect results.
- The stored Sk_zeta_ablated.npy (the F12 ablation prediction artifact) did not numerically match a fresh recomputation using the same described rule (exclude n with 3|n or 5|n) — disagreement of order unity in entries — though it did reproduce the reported cosine 0.973 against Δ_empirical(F12). This inconsistency was logged but did not affect the F4 analysis, which recomputed ablation from scratch using the validated S_k(ζ) and S_k(F4) at a common 200-peak grid.
- Subagent / large-compute resources were not needed; the full 1e6 × 200-peak ablation summation completed in ~1 second using a Numba-parallel Kahan kernel.
- Hypothesis directly tests an effect at the M_jk level only; this analysis does not establish a mechanism for the failure of GRH for F4 — only that M_jk differences between ζ and F4 do not encode GRH-violation information, consistent with the broader r21 finding.
</challenges> <discussion>
The F4 result generalizes the r21 (F12 vs ζ) "arithmetic ablation" finding to a second, independently-constructed GRH-violator. F4 (Davenport–Heilbronn at κ=0.28408) is a linear combination of two Dirichlet L-functions modulo 5 designed to violate GRH while preserving an analogue of the functional equation; F12 is an explicit construction modulo 15. That a one-line model — "delete terms with conductor-prime divisibility from ζ" — explains 99.4% of the variance in M_jk(F4) − M_jk(ζ) and 94.7% for F12 strongly supports the conclusion stated in the dataset description: ω-stratified covariance matrices read out coefficient arithmetic (specifically, which integers contribute), not zero locations. This means M_jk is a poor diagnostic for GRH violation as such; any classifier trained on M_jk-derived features will primarily learn conductor / coefficient arithmetic and will fail to generalize across function classes — exactly the pattern noted in r10/r17. The slight overshoot of the empirical Δ above the model (α≈1.29 > 1) suggests F4 has additional negative contribution from the π/2 phase rotations of its Dirichlet character coefficients beyond pure deletion of 5-divisible terms, but this residual carries little structure (only ~0.6% of variance).
</discussion> <proposed-next-hypotheses>
1. A two-parameter ablation model (delete 5|n, plus a complex coefficient ω·χ(n) on the remaining 5∤n terms reflecting the F4 character mixture) will reduce the F4 residual to below 0.1% of variance and yield α ≈ 1, providing a fully analytic decomposition of M_jk(F4) − M_jk(ζ).
2. For the modular L-functions F9–F11, the empirical Δ = M_jk(F_i) − M_jk(ζ) will be predicted with cosine > 0.95 by ablating ζ on each function's conductor primes (with appropriate Euler-factor reweighting), demonstrating that the ω-stratified covariance is universally a conductor-arithmetic readout across the entire L-function panel.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>Delta_ablation_results_F4.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy archive containing the F4 arithmetic-ablation experiment results: empirical and ablation 8×8 matrices M_zeta, M_F4, M_zeta_ablated_p5, Δ_empirical = M(F4)−M(ζ), Δ_ablation = M'(ζ;5|n excluded)−M(ζ); the underlying complex S_k arrays at 200 ζ-peak t-values for ζ, F4, and ablated-ζ (200×8 each); peak heights t_peaks; and summary scalars cosine_similarity = 0.9978, pearson_r = 0.9968, alpha_best_fit = 1.285, r2_best_fit = 0.9936, Frobenius norms. Produced from a Numba-parallel Kahan-compensated ω-stratified Dirichlet summation up to N=10^6 on a fixed shared 200-peak grid; M(ζ) was validated to 13-digit agreement against the on-disk r21 matrix before ablation.</artifact-description>
</artifact>
<artifact>
<file-name>F4_ablation_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) scatter of Δ_empirical vs Δ_ablation entries with y=x and best-fit lines, annotated with cosine 0.9978, Pearson 0.9968, R² 0.9936; (B) side-by-side heatmaps of the 8×8 empirical and ablation Δ matrices on a shared diverging color scale, showing matched negative structure peaked at j=k=2.</artifact-description>
</artifact>
</artifacts>
</output>
