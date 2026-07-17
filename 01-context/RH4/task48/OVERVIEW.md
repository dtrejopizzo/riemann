## Overview <output>
<conclusion>
The hypothesis is refuted: replacing the ad-hoc block size 2π/log(N) with the theoretically justified 2π/log(T) significantly lowers the GEV shape parameter ξ for |ζ(½+it)| on t∈[10⁴,10⁵], with the new estimate (ξ≈0.4676) lying clearly outside the 95 % bootstrap CI of the old estimate (ξ≈0.4800, CI=[0.4751, 0.4831]).
</conclusion> <methods>
1. Generation of |ζ(½+it)|. Per R1/R6 we re-implemented from scratch a vectorized Riemann–Siegel evaluator: Z(t)=2·Σ_{n=1..m} cos(θ(t)−t·ln n)/√n + (−1)^{m−1}(t/2π)^{−1/4}·Ψ(p), with m=⌊√(t/2π)⌋, p=√(t/2π)−m, and θ(t) from a 5-term asymptotic expansion. The asymptotic θ matched mpmath.siegeltheta to ≤3×10⁻¹¹ at t∈{10⁴,5×10⁴,10⁵}; sample Z values matched mpmath.siegelz to ~10⁻⁵ — sufficient for GEV fitting since |ζ| values being binned are O(1)–O(10).
2. Sampling. We computed |ζ(½+it)| at N=10⁶ uniformly spaced points on t∈[10⁴,10⁵] (Δt=0.09), in numpy chunks of 10⁴ t-values, total runtime ≈4 s.
3. Block maxima. Two block sizes were applied on the t-axis: - A (ad hoc): b_A = 2π/ln(10⁶) ≈ 0.4548 (≈5.05 samples per block, n_blocks=197 892). - B (theoretical, R13): b_B = 2π/ln(T) using the geometric-mean height T=√(10⁴·10⁵)≈31 623, giving b_B ≈ 0.6064 (≈6.74 samples per block, n_blocks=148 419). Sensitivity also reported with T=10⁴ and T=10⁵. For each block the maximum was taken via numpy.maximum.reduceat; the trailing partial block was discarded.
4. GEV fit. We fit the three-parameter GEV via MLE using scipy.stats.genextreme.fit (loc, scale, shape c) and report ξ=−c. 95 % uncertainty is from a non-parametric bootstrap (n_boot=100 per approach, fixed seeds); CI is the 2.5/97.5 percentile of bootstrapped ξ.
5. Decision rule. The hypothesis is refuted iff the point estimate of approach B lies outside the 95 % CI of approach A.
</methods> <results>
- Approach A (b = 2π/log N): ξ_A = 0.47999, loc = 1.4811, scale = 1.1522, 95 % bootstrap CI = [0.47513, 0.48314], n_blocks = 197 892.
- Approach B (b = 2π/log T, T = T_geom ≈ 3.16×10⁴): ξ_B = 0.46758, loc = 1.6670, scale = 1.2393, 95 % bootstrap CI = [0.46286, 0.47189], n_blocks = 148 419.
- Δξ = ξ_B − ξ_A = −0.01242. The new ξ lies clearly below the lower edge of the old CI (0.46758 < 0.47513), and conversely ξ_A lies above the upper edge of the new CI (0.47999 > 0.47189). The two confidence intervals do not overlap.
- Sensitivity to choice of T inside the window: ξ(b=2π/ln 10⁴)=0.45918 and ξ(b=2π/ln 10⁵)=0.47171; both remain below ξ_A and below the lower endpoint of the A-CI, so the qualitative conclusion is robust to the exact "representative" T used.
- All three estimates are consistent with a heavy-tailed (Fréchet, ξ>0) extreme-value regime for block maxima of |ζ(½+it)| in this height window. The estimated ξ is, however, substantially larger than the asymptotically expected Gumbel limit (ξ=0) implied by Selberg-type CLTs at very large height — a known finite-T pre-asymptotic bias.
</results> <challenges>
- Direct mpmath.siegelz evaluation at 10⁶ points was prohibitive (>10 h); we therefore implemented a vectorized Riemann–Siegel formula and validated it against mpmath at sampled t. This kept evaluation under 5 seconds while remaining well within the precision needed for ξ estimation.
- scipy.stats.genextreme.fit is slow (~2 s on 200 k samples); 200 bootstraps timed out the cell. We reduced n_boot to 100 per approach. CIs are therefore Monte-Carlo noisy at the 4th decimal place but the gap between A and B (Δξ ≈ 1.2×10⁻²) is far larger than that noise.
- The block sizes prescribed by the protocol correspond to only ≈5–7 samples per block; the GEV asymptotics are pre-asymptotic in this regime, which is exactly the issue R13 highlights. Both estimates should therefore be interpreted as block-size-dependent finite-T characterizations rather than as a converged ξ.
- "T" in 2π/log T is not unique within a window; we report the geometric-mean choice as primary and the endpoint choices as sensitivity, all of which preserve the conclusion.
</challenges> <discussion>
This audit confirms the rationale for rule R13: the ad-hoc block size 2π/log N (N being the number of samples drawn from the t-axis) and the theoretically motivated Selberg block size 2π/log T (mean spacing of large-value events at height T) produce GEV shape estimates that differ by roughly 0.012 — small in absolute terms but well outside either 95 % CI given the very large block counts. Per the document's STOP CONDITION 0.5, this magnitude qualifies as "ξ changes significantly (>prior CI)", which means downstream Front-3 cluster centers and any classifier trained on ξ as a feature must be recomputed with the corrected block size. Substantively, the corrected (smaller) ξ_B brings the empirical extremal index of |ζ| at moderate T closer to the expected slow drift toward the Gumbel (ξ→0) asymptotic regime, but does not eliminate the strong finite-T heavy-tail signature. The result also reinforces the broader Anti-Pattern 18 in the document: ξ measured under a misspecified block scaling is a biased summary of the local extremal behavior of L-functions and should not be used to discriminate function classes without first standardizing on 2π/log T.
</discussion> <proposed-next-hypotheses>
1. The shape parameter ξ obtained with the Selberg block size 2π/log T decreases monotonically toward the Gumbel limit ξ=0 as T increases through {10³, 10⁴, 10⁵, 10⁶, 10⁷}, consistent with Selberg's CLT for log|ζ|; a log-T regression of ξ̂ should give a non-trivial negative slope with bootstrap CI excluding zero.
2. For non-RH-violating Selberg-class members (F2, F6, F7, F9, F11, F13), GEV ξ̂ at fixed N and matched T-window converges to a common value (universality), whereas the constructed RH violators F4, F5, F12 show a significantly higher ξ̂ at the same height — yielding an extreme-value-based discriminator whose held-out AUC ≥ 0.85 satisfies STOP CONDITION 0.6.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>gev_block_size_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON summary of the Step 0.5 GEV block-size audit on |ζ(½+it)| over t∈[10⁴,10⁵] with N=10⁶ Riemann–Siegel samples. Contains for each approach (A: b=2π/log N; B: b=2π/log T at T_geom, T_lower, T_upper) the block size, samples-per-block, number of blocks, MLE GEV (loc, scale, ξ), and 95 % non-parametric bootstrap CIs for ξ (n_boot=100). Also records the decision flags showing that ξ_B lies outside ξ_A's CI and Δξ ≈ −0.0124.</artifact-description>
</artifact>
<artifact>
<file-name>gev_block_size_comparison.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Single-panel summary figure showing the GEV shape parameter ξ with 95 % bootstrap error bars for the two block-size choices, with the A-band shaded; the B point clearly falls below A's CI band, visually confirming the refutation of the hypothesis.</artifact-description>
</artifact>
</artifacts>
</output> 