## Overview <output>
<conclusion>
The 67% negative off-diagonal claim for the covariance matrix Cov(Re S_j, Re S_k) of the Riemann zeta function is NOT confirmed: at N=10⁵ we observe exactly 50.0% (95% block-bootstrap CI [39.17%, 65.02%]) and at N≈5.24×10⁵ (truncated 10⁶) we observe 53.59% (95% CI [41.18%, 63.42%]); both lower bounds lie well below 50%, satisfying the v6 STOP CONDITION 0.3.
</conclusion> <methods>
1. Interpretation of S_k. The binding context document does not explicitly define S_k for this covariance claim; following the most computationally tractable interpretation consistent with R5/R6/R13, S_k is taken as the dyadic block partial sum S_k(t) = Σ_{n∈[2^k, min(2^(k+1), N+1))} n^(−1/2−it). This yields ⌈log₂N⌉ blocks (17 for N=10⁵, 20 intended for N=10⁶); the alternative "S_k = Σ_{n=1}^{k} ..." yields infeasible 10⁶×10⁶ matrices.
2. Numerical engine. Implemented from scratch (R1) using NumPy chunked outer products with float64 cos/sin via complex-exponential evaluation. Cross-validated against an independent Numba-jit Kahan compensated implementation (R6); agreement to 2.2×10⁻¹⁶ on all test cases at N=10⁵. NumPy uses pairwise reduction internally, giving accuracy comparable to Kahan for these sums.
3. Sampling. Uniform t-grid on [10⁴, 2·10⁴]: dt=0.2 (nT=50001) for N=10⁵ and dt=0.3 (nT=33334) for N=10⁶. The Selberg mean spacing 2π/log(T) at T=1.5×10⁴ is 0.6534, giving 3.27 and 2.18 samples per Selberg block respectively.
4. Covariance. Computed Cov(Re S_j, Re S_k) over the t-grid using np.cov. Block 0 (S_0 = 1, zero variance) was excluded — its inclusion makes correlations undefined; this leaves 16×16 (N=10⁵) and 18×18 (N=5.24×10⁵) matrices. Counted strictly negative off-diagonal entries.
5. Block bootstrap (B=200, seed=42). Block length L = round((2π/log(T))/dt) samples = 3 (N=10⁵) and 2 (N=5.24×10⁵), per R13. Each bootstrap replicate concatenates ⌊nT/L⌋ blocks sampled with replacement and recomputes the covariance and % negative. 95% CIs are percentile [2.5, 97.5].
6. Time-budget mitigation. The k=19 dyadic block at N=10⁶ (475 713 terms × 33 334 t-points) exceeded available wall time after ~600 s; results for "N=10⁶" therefore reflect a truncation to N=524 287 (blocks 0–18). This is reported transparently rather than fabricated.
</methods> <results>
- N=10⁵ (16×16 cov matrix, 240 off-diagonals): 120/240 = 50.00% negative; bootstrap mean 53.09%, 95% CI [39.17%, 65.02%], block length 3 samples.
- N=524 288 (18×18 cov matrix, 306 off-diagonals; truncation of N=10⁶): 164/306 = 53.59% negative; bootstrap mean 52.81%, 95% CI [41.18%, 63.42%], block length 2 samples.
- The claimed value 67% lies outside the upper bound of the N=524 288 CI (63.4%) and just inside the upper bound of the N=10⁵ CI (65.0%); the point estimates are essentially indistinguishable from the 50% null.
- Means of Re S_k for k≥1 are O(10⁻⁵), confirming MVT-style cancellation (R5), so unconditional cross-block covariances are dominated by sub-leading noise — consistent with the observed lack of robust signed bias.
- Decision rule (objective): "confirmed only if lower bound of 95% CI is significantly above 50%". Lower bounds at both N's are below 50% → claim NOT confirmed → STOP CONDITION 0.3 triggered → v6 prescribes reformulating Fronts 1 and 2 as exploratory.
</results> <challenges>
1. Definition ambiguity: the binding document does not specify whether S_k denotes truncated partial sums (S_k = Σ_{n=1}^{k}), dyadic block sums, or a different decomposition; the dyadic interpretation was adopted for computational tractability and because it is the only choice yielding a manageable covariance matrix at both N values. A different interpretation could in principle yield different percentages.
2. Compute budget: the k=19 dyadic block alone took ~600 s of vectorized NumPy time (roughly 2.4×10¹⁰ trigonometric evaluations); within the 3600 s budget it was not possible to complete the full N=10⁶ run. Reported "N=10⁶" results are therefore for N=524 287; the qualitative conclusion (no signal) is unaffected and consistent with the N=10⁵ result.
3. Block-bootstrap block size is small (L=2 or 3 samples) because dt is comparable to 2π/log(T); future runs should use dt ≤ 2π/(8 log T) to give ≥8 samples per Selberg block.
4. Block 0 of the dyadic decomposition (S_0 = 1) has identically zero variance and was excluded from off-diagonal statistics.
</challenges> <discussion>
The result is consistent with R5 and Anti-pattern #6 of the v6 Binding Context Document: under unconditional sampling of t in [10⁴, 2·10⁴], MVT-style cancellation drives the leading-order means and cross-covariances of Re S_k toward zero, leaving only sub-leading noise. In that regime the signs of off-diagonal covariance entries should be approximately Bernoulli(1/2), exactly as observed (50.00% at N=10⁵, 53.6% at N≈5.2×10⁵). The previously circulated 67% figure thus appears to be either (i) an artifact of a different (unstated) S_k definition, (ii) an artifact of conditional sampling (e.g. peaks |D|>λ√V) reported as unconditional, or (iii) an artifact of insufficiently rigorous error analysis in earlier RH1–3 runs. Per the document this should trigger reformulation of Fronts 1 and 2 from confirmatory to exploratory: "is there ANY signed structure in CONDITIONAL cross-covariances, and if so what is it?". The classical analogue (R9) is the Hardy–Littlewood / Goldston–Gonek–Heath-Brown picture in which leading-order mean-square contributions of partial sums of ζ(½+it) are Gaussian-like and unsigned to leading order; signed structure requires conditioning.
</discussion> <proposed-next-hypotheses>
1. CONDITIONAL covariance hypothesis: when t is restricted to peaks of |ζ(½+it)| in the top quartile (or with |D(t)| > λ√V(t) for a fixed λ ≈ 1), the percentage of negative off-diagonal entries of Cov(Re S_j, Re S_k) for the dyadic-block decomposition exceeds 60% with bootstrap CI lower bound > 50% — i.e. the 67% claim is a CONDITIONAL phenomenon and was misreported as unconditional in RH1–3.
2. S_k re-definition hypothesis: re-running Step 0.3 with S_k defined as truncated-at-k partial sums on a coarser k-grid (e.g. k ∈ {10², 10³, 10⁴, 10⁵, 10⁶}) yields a markedly higher fraction of negative off-diagonals because nested truncation introduces a Toeplitz-like negative-correlation structure absent in the dyadic decomposition.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>sums_N1e5.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Dyadic block partial sums S_k(t) for ζ(s) at N=10⁵, computed via cross-validated chunked NumPy with Kahan-reference verification. Stores Re and Im parts on a 50001-point t-grid spanning [10⁴, 2·10⁴] (dt=0.2) for K=17 dyadic blocks. Used for the primary covariance and block-bootstrap analysis.</artifact-description>
</artifact>
<artifact>
<file-name>sums_N1e6_partial.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Truncated dyadic block partial sums for ζ(s) at N=524 287 (blocks 0–18 of intended N=10⁶), on a 33334-point t-grid (dt=0.3) over [10⁴, 2·10⁴]. The k=19 block was not computed within the wall-clock budget; the 'done' index array records which blocks are populated.</artifact-description>
</artifact>
<artifact>
<file-name>cov_results.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final covariance matrices C5 (16×16) and C6 (18×18), bootstrap distributions boot5/boot6 (B=200), point estimates pct5/pct6 (50.00% and 53.59%) and 95% CIs [39.17,65.02] and [41.18,63.42]. Demonstrates non-confirmation of the 67% claim.</artifact-description>
</artifact>
<artifact>
<file-name>cov_negative_offdiag_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) bootstrap distributions of % negative off-diagonals for both N values with 50% null and 67% claim marked; (B) correlation heatmap of Corr(Re S_j, Re S_k) at N=10⁵ showing a near-tridiagonal sign structure rather than a globally negative one.</artifact-description>
</artifact>
</artifacts>
</output> 