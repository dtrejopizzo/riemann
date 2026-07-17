## Overview <output>
<conclusion>
The hypothesis is rejected: conditioning on large |D(t;N)| does not increase the percentage of negative off-diagonal entries in Cov(Re S_j, Re S_k); on the contrary, both conditional point estimates (37.4% and 43.2%) and their 95% block-bootstrap upper bounds (42.6% and 45.3%) lie well below the 60% threshold and the 55% lower-bound criterion.
</conclusion> <methods>
1. Built a Numba-JIT, parallel, Kahan-compensated dyadic-block summation engine for the Riemann zeta partial sum D(t;N) = Σ_{n=1}^{N} n^{-1/2-it} decomposed into K=20 dyadic blocks S_k(t;N) = Σ_{n=2^(k-1)}^{min(2^k-1,N)} n^{-1/2-it}, with N=10⁶ (block 20 truncated at 10⁶). Validated against 50-digit mpmath at t=100, N=10⁴: relative agreement ≈13.5 digits, consistent with the r2 spec (~12.8 digits).
2. Evaluated S_k(t;10⁶) for 100,001 values of t on a dense uniform grid t∈[10⁴, 2·10⁴] with step Δt=0.1 (≈14 samples per mean zeta-zero gap 2π/log(T)≈0.68); total runtime ≈568 s on the available CPUs, parallelized over t with prange.
3. Computed |D(t;N)| = |Σ_k S_k|. Defined two conditioning subsets: • A: top 10% by |D| (n=10,000; |D|≥4.61). • B: |D| > 1.5·√(log log N) = 1.5·√(log log 10⁶) ≈ 2.4306 (n=25,366; 25.4% of grid).
4. Computed the 20×20 covariance matrix Cov(Re S_j, Re S_k) on each subset (np.cov, rowvar=False) and the percentage of the 380 strictly off-diagonal entries that are negative.
5. Block bootstrap (B=1000) on the full grid with moving-block length L=100 (≈10 t-units, > zero spacing). For each resample, the conditioning was reapplied (top-10% and threshold rules) to the resampled |D| values, the conditional covariance recomputed, and the off-diagonal % negative re-tabulated. 95% CIs were taken as the [2.5, 97.5] percentile of the bootstrap distribution.
6. As a methodological cross-check, the same procedure was applied unconditionally on this fresh grid.
</methods> <results>
• Subset A (top 10% |D|): pct_neg_off = 37.37%, 95% CI = [32.11%, 42.63%].
• Subset B (|D|>1.5·√loglogN): pct_neg_off = 43.16%, 95% CI = [37.37%, 45.26%].
• Unconditional (same fresh grid t∈[10⁴, 2·10⁴], dt=0.1, 20 blocks): pct_neg_off = 43.68%, 95% CI = [37.89%, 55.79%].
• Reference unconditional values from r3 (cov_results description): 50.0% and 53.6%. Hypothesis criteria: point estimate >60% AND CI lower-bound >55%.
• Subset A: point 37.37% < 60% (fails); CI lower 32.11% < 55% (fails). Upper bound 42.63% < 60%, so the data are inconsistent with even the 60% threshold.
• Subset B: point 43.16% < 60% (fails); CI lower 37.37% < 55% (fails). Upper bound 45.26% < 60%. Direction of the conditional effect: relative to the unconditional 43.68% on the same grid, conditioning on large |D| DECREASES the fraction of negative off-diagonal covariances (Subset A: −6.3 pp; Subset B: −0.5 pp). Inspecting Cov_A reveals strong positive correlations among small-n blocks (k≤11), consistent with the largest |D| events being driven by coherent constructive contributions from low-frequency dyadic blocks rather than by anti-correlated cancellation across blocks.
</results> <challenges>
• cov_results.npz from r3 was not present on disk; only its descriptive summary (50.0%, 53.6% off-diagonal negativity) was available, so the comparison uses those reported numbers and a freshly recomputed unconditional baseline on the same grid as the conditional analysis.
• "Dense grid" was unspecified; selected Δt=0.1 (≈14 samples per zeta-zero gap) as a balance between resolution and runtime — finer grids would barely change conditional sample sizes for this question.
• Block bootstrap on a conditioning rule has subtleties: resampling the underlying t-blocks and reapplying the rule (used here) is preferred over resampling the post-conditioned subset, which would underestimate variance.
• 100k evaluations of D and S_k at N=10⁶ required ~10 minutes — the analysis is engine-bound; the Kahan-compensated Numba implementation is essential at this N (naive summation would corrupt covariances per the R6 note).
• Pre-existing C5/C6/pct5/pct6/boot5/boot6 files in the workspace had shapes 16×16 and 18×18 (pct values 50.0% and 53.6%, identical to the r3 unconditional figures), so they appear to mirror r3 and not the conditional analysis required here; they were therefore not used.
</challenges> <discussion>
The result contradicts the conjectural mechanism behind the hypothesis. The proposal was that large excursions of |D| should be associated with strongly anti-correlated contributions from different dyadic blocks (i.e., a negative-off-diagonal-rich Cov(Re S_j, Re S_k)). What we observe instead — both for the strict top-10% conditioning and the soft threshold |D|>1.5·√loglogN — is the opposite: conditioning on large |D| selects t where many low-index blocks are positively co-aligned (visible as a red sub-block in the Cov_A heatmap among k≤11), which actually reduces the fraction of negative off-diagonal entries. This is statistically consistent with the heuristic that rare large peaks of partial sums are dominated by coherent constructive interference rather than by cancellation patterns. The unconditional baseline on this grid (43.7%) is itself below the r3-reported 50–54% range, suggesting that the precise off-diagonal-sign fraction is sensitive to t-range, grid density, and the choice of K=20 dyadic blocks; nonetheless the conditional values move further away from, not toward, the 60% target. Combined with the r3 stop-condition finding that even the unconditional 67% claim was not reproducible, the present analysis closes the conditional reformulation: the "negative off-diagonal dominance" phenomenon does not exist in the dyadic-block representation under either unconditional or large-|D|-conditional sampling for ζ(s) at N=10⁶ and T~10⁴.
</discussion> <proposed-next-hypotheses>
1. The off-diagonal-sign structure of Cov(Re S_j, Re S_k) is concentrated in the high-index dyadic blocks (k≥12 for N=10⁶): after restricting the covariance to blocks k≥12, the percentage of negative off-diagonal entries will exceed 60% both unconditionally and conditional on the top-10% of |D|.
2. The phenomenon hypothesized for ζ(s) does manifest in a different decomposition: when S_k is redefined using Selberg-class style smoothed or logarithmic blocks (e.g., n in [N^{(k-1)/K}, N^{k/K}]) rather than dyadic blocks, the conditional fraction of negative off-diagonal Cov(Re S_j, Re S_k) entries (top 10% by |D|) will exceed 55% for ζ(s) at N=10⁶, T∈[10⁴, 2·10⁴].
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>cov_conditional_results.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy archive containing the full computational outputs of this conditional covariance analysis for ζ(s), N=10⁶, K=20 dyadic blocks, t-grid [10⁴, 2·10⁴] with Δt=0.1 (100,001 points): t_grid, |D|, the (M,K) real and imaginary partial-sum block matrices Sre_blocks/Sim_blocks, conditioning indices idxA/idxB, 20×20 covariance matrices Cov_A/Cov_B/Cov_uncond, point-estimate percentages pct_A/pct_B/pct_uncond, B=1000 bootstrap distributions pct_A_boot/pct_B_boot/pct_U_boot, 95% bootstrap CIs ci_A/ci_B/ci_U, and the run parameters (block length L=100, threshB, dt_step). Created with a Numba-JIT Kahan-compensated dyadic engine validated against 50-digit mpmath.</artifact-description>
</artifact>
<artifact>
<file-name>conditional_cov_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final summary figure (two stacked panels). Panel A: bootstrap distributions of % negative off-diagonal Cov(Re S_j, Re S_k) entries for Subset A, Subset B, and unconditional, with the 60% hypothesis threshold and 55% CI-lower-bound threshold annotated. Panel B: heatmap of the 20×20 conditional covariance matrix for Subset A, showing dominance of positive correlations among low-index dyadic blocks.</artifact-description>
</artifact>
</artifacts>
</output> 