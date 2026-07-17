## Overview <output>
<conclusion>
Across the tested high-t windows, the ω-class fourth-moment decomposition does not support the hypothesis that the zeta-function off-diagonal residual fraction approaches zero with increasing T₀; instead, it increases strongly, while L(Δ) decreases modestly at the highest window and L_DH appears to rise to a higher nonzero plateau.
</conclusion>
<methods>
I first inspected the available workspace artifacts and found the prior validated output `fourth_moment_omega_decomposition_T500_1000.json` and the canonical `ldh_def.py` implementation for the Davenport–Heilbronn L-function. The original r20 engine source code was not preserved on disk, so I reconstructed the decomposition engine directly from the stored artifact definition and then validated that reconstruction numerically against the `[500,1000]` reference window before extending it. The analysis used Python with `numpy`, `pandas`, `matplotlib`, `json`, and `mpmath`. I set `N_terms = 10000`, classes `ω(n) ∈ {0,1,2,3,4,5}`, and integration step `dt = 0.01`, matching the r20 configuration. For each function, I formed the Dirichlet polynomial
`D(t) = Σ_{n≤N} a_n / n^(1/2+it)`
and partitioned it into ω-classes
`S_k(t) = Σ_{ω(n)=k} a_n / n^(1/2+it)`.
I then computed, over each window, the total fourth moment `∫|D(t)|^4 dt`, the pure-class contribution `Σ_k ∫|S_k|^4 dt`, the diagonal cross contribution `4 Σ_{j<k} ∫|S_j|^2 |S_k|^2 dt`, and defined the off-diagonal residual as the remainder. For `ω(n)`, I used a sieve over `n ≤ 10000`. For ζ, coefficients were `a_n = 1`. For L_DH, coefficients were taken from the verified mod-5 character combination encoded in `ldh_def.py`, i.e. `a_n = Aχ(n) + Bχ̄(n)`. For L(Δ), I computed Ramanujan tau coefficients exactly up to `n=10000` using integer q-series convolution from `Δ(q)=q∏_{m≥1}(1-q^m)^24`, then normalized them to `a_n = τ(n)/n^(11/2)`. This avoided fabricating or approximating coefficients and preserved correctness of the arithmetic input. Because direct construction of the full phase matrix would be memory-intensive, I evaluated each `S_k(t)` in chunks over the t-grid using vectorized matrix multiplication with `exp(-it log n)`. Numerical integration used the composite trapezoid rule (`numpy.trapezoid`). As a validation step, the reconstructed engine reproduced the stored `[500,1000]` zeta result closely: my reconstruction gave pure 23.3104%, diag×4 85.3200%, off-diag -8.6304%, versus stored values 23.3105%, 85.3203%, -8.6308%. I then computed the requested windows `[5000,5500]` and `[20000,20500]` for ζ, L(Δ), and L_DH, and compared them with the stored `[500,1000]` baseline. I saved the new outputs as JSON files and generated a final summary figure with two vertically stacked subfigures: (A) off-diagonal residual versus `T₀` on a log x-axis, and (B) stacked pure plus diagonal-cross percentages by window and L-function.
</methods>
<results>
The validated `[500,1000]` baseline from the stored artifact was:
- ζ: pure 23.3105%, diag×4 85.3203%, off-diag -8.6308%, `∫|D|^4 dt = 85022.9267`
- L(Δ): pure 15.5658%, diag×4 46.9856%, off-diag 37.4485%, `∫|D|^4 dt = 45405.7577`
- L_DH: pure 18.7962%, diag×4 58.6437%, off-diag 22.5602%, `∫|D|^4 dt = 26507.4952` For `[5000,5500]`, I obtained:
- ζ: pure 15.0245%, diag×4 55.9059%, off-diag 29.0695%, `∫|D|^4 dt = 228633.0656`
- L(Δ): pure 16.2479%, diag×4 46.6915%, off-diag 37.0605%, `∫|D|^4 dt = 45220.9119`
- L_DH: pure 13.3317%, diag×4 42.8359%, off-diag 43.8324%, `∫|D|^4 dt = 48241.1574` For `[20000,20500]`, I obtained:
- ζ: pure 11.1861%, diag×4 40.9767%, off-diag 47.8372%, `∫|D|^4 dt = 375163.3749`
- L(Δ): pure 17.6144%, diag×4 53.5520%, off-diag 28.8336%, `∫|D|^4 dt = 52130.8731`
- L_DH: pure 14.6971%, diag×4 42.3035%, off-diag 42.9994%, `∫|D|^4 dt = 47595.0351` Comparison table:
- ζ off-diag residual: -8.6308% → 29.0695% → 47.8372%
- L(Δ) off-diag residual: 37.4485% → 37.0605% → 28.8336%
- L_DH off-diag residual: 22.5602% → 43.8324% → 42.9994% Thus, over the three tested windows, the off-diagonal residual does not trend toward zero for ζ. Instead, ζ shows the strongest positive increase among the three functions. L(Δ) remains high and nonzero but decreases by 8.61 percentage points between the first and last windows. L_DH increases by 20.44 percentage points from `[500,1000]` to `[5000,5500]` and then changes only slightly (-0.83 percentage points) between the two highest windows, consistent with a possible higher nonzero plateau over the tested range.
</results>
<challenges>
The main challenge was that the original r20 source code for the decomposition engine was not preserved in the workspace; only the output JSON artifact remained. I therefore had to reconstruct the engine from the artifact definitions and validate it numerically before using it. This introduces a modest reproducibility limitation, although the reconstruction matched the stored baseline closely. A second challenge was coefficient generation for L(Δ). Using ordinary `float64` q-series arithmetic would risk loss of integer accuracy in the Ramanujan tau coefficients at large n, so I replaced that with exact integer convolution up to `n=10000`, then normalized with `mpmath`. This was computationally heavier but methodologically safer. A third challenge was memory pressure in evaluating `S_k(t)` on a 50,000-point grid. I addressed this by chunking the t-grid during matrix construction; this kept the computation feasible without subsampling the dataset or changing the requested numerical resolution. Methodological limitations remain. The analysis uses only three windows, so convergence claims are necessarily provisional. I did not estimate numerical uncertainty from varying `dt`, quadrature rule, or window length, and the off-diagonal residual is defined as a difference of large quantities, which can amplify small numerical discrepancies. Therefore, the results are strong evidence against the specific “ζ off-diagonal → 0” trend over the tested range, but not a proof of asymptotic behavior.
</challenges>
<discussion>
Within the tested regime, the data contradict the motivating asymptotic picture for ζ. If the ω-class fourth-moment decomposition were becoming increasingly diagonal-dominant for the zeta function as `T₀` increased, one would expect the off-diagonal residual fraction to shrink, ideally toward zero. Instead, it flips sign relative to the `[500,1000]` window and then grows substantially positive by `[20000,20500]`. This indicates that, at least for `N=10^4` and these finite windows, the decomposition is not approaching a simple diagonal-dominant regime for ζ. For L(Δ), the behavior is different: the off-diagonal fraction is already large at `[500,1000]`, remains almost unchanged at `[5000,5500]`, and then drops at `[20000,20500]`. That pattern is compatible with slow drift toward a nonzero stable value, but the present three-window design is insufficient to identify the limit reliably. For L_DH, the increase from the first to the second window and near-stability thereafter is more suggestive of convergence to a higher positive residual, though again this remains tentative. Scientifically, these results support the broader methodological caution already noted in the dataset description: the ω-class decomposition behaves like a finite-N structural fingerprint rather than automatically collapsing to a universal diagonal signature simply by moving to higher t. The present computations strengthen that caution by showing that even for ζ, raising `T₀` from 500 to 20000 does not produce the anticipated decay of the residual at fixed `N=10^4`.
</discussion>
<proposed-next-hypotheses>
1. For the zeta function at fixed `N=10^4`, the ω-class off-diagonal residual fraction converges to a positive nonzero limit as `T₀` increases, rather than to zero.
2. For L_DH, the ω-class off-diagonal residual fraction stabilizes near approximately 43% for sufficiently high windows of length 500, while L(Δ) continues to drift downward toward a distinct nonzero limit.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>fourth_moment_omega_decomposition_T5000_5500.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON artifact containing the full ω-class fourth-moment decomposition for ζ, L(Δ), and L_DH on the window t∈[5000,5500] with N_terms=10000, dt=0.01, and classes 0–5. It was created by reconstructing the validated r20 decomposition engine and applying it to the requested high-t window.</artifact-description>
</artifact>
<artifact>
<file-name>fourth_moment_omega_decomposition_T20000_20500.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON artifact containing the full ω-class fourth-moment decomposition for ζ, L(Δ), and L_DH on the window t∈[20000,20500] with N_terms=10000, dt=0.01, and classes 0–5. It was produced with the same validated reconstruction used for the [5000,5500] window.</artifact-description>
</artifact>
<artifact>
<file-name>fourth_moment_omega_window_comparison.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compact comparison artifact summarizing pure, diagonal-cross, and off-diagonal fractions across the three windows [500,1000], [5000,5500], and [20000,20500] for all three L-functions. It was assembled from the stored r20 baseline and the two newly computed high-t decompositions.</artifact-description>
</artifact>
</artifacts>
</output>
