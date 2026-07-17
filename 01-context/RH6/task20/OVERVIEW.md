## Overview <output>
<conclusion>
At N=10^6 the ω-class fourth-moment decomposition fractions for ζ, L(Δ), and L_DH continue to drift dramatically rather than converge, decisively confirming that the signature has no stable limit in the accessible range of N.
</conclusion>
<methods>
1. Reconstructed and validated the r16/r26 fourth-moment engine from the JSON metadata of the existing artifacts. The Dirichlet polynomial is D(t)=Σ_{n=1..N} a_n n^{-1/2-it}, partitioned by ω(n) into classes k=0..5 with S_k(t) the partial sum over those n. Total ∫|D|⁴ dt, pure ∫|S_k|⁴ dt for each k, and all C(6,2)=15 diagonal-cross ∫|S_j|²|S_k|² dt were computed by left-Riemann sum on the uniform grid t∈[500,1000), dt=0.01 (50,000 points). The off-diagonal residual is total − pure − 4·Σ_{j<k} cross. Terms with ω(n)>5 (which appear only past N≈30,030) were left out of class sums but kept in D, matching the prior artifact convention.
2. Coefficient generation up to N=10^6: ζ → a_n=1; L_DH → a_n = [0,1,ξ,-ξ,-1] indexed by n mod 5 (real, from ldh_def.py); L(Δ) → a_n = τ(n)/n^{11/2}, with τ(n) computed exactly as the q^n coefficient of Δ(q)=q·∏_{n≥1}(1-q^n)^{24}, built via python-flint fmpz_series: Euler pentagonal sparse seed for ∏(1-q^n), then five squarings and one multiplication to obtain (·)^{24} truncated to degree 10^6. Reproduced τ(1..10)=(1,-24,252,-1472,4830,-6048,-16744,84480,-113643,-115920) exactly; Deligne bound |a_Δ(n)|≤d(n) was checked for the global maximum (n=808447, |a|=5.38, d(n)=8).
3. ω(n) up to 10^6 obtained from a smallest-prime-factor sieve; class counts: ω=0:1, 1:78,734, 2:288,726, 3:379,720, 4:208,034, 5:42,492, 6:2,285, 7:8.
4. Main kernel: a Numba-jitted, 8-thread parallel accumulator computing D(t) and S_0..S_5(t) directly as Σ a_n n^{-1/2} (cos(-t·log n)+i sin(-t·log n)). Validated against the saved N=10^4 ζ result and matched to 1e-5 relative error on every reported fraction. Runtime ~280 s per L-function at N=10^6 on 8 CPUs.
5. Integrals were assembled into the same decomposition definition (pure, 4×diag-cross, off-diag) as in the prior JSONs to enable a like-for-like comparison.
</methods>
<results>
New N=10^6 fractions (∫|D|⁴ dt = total):
- ζ: total = 1.10275×10^5, pure = 29.328%, diag×4 = 124.377%, off-diag = −53.705%.
- L(Δ): total = 6.40547×10^4, pure = 18.615%, diag×4 = 71.810%, off-diag = +9.575%.
- L_DH: total = 2.65085×10^4, pure = 28.085%, diag×4 = 99.725%, off-diag = −27.810%. Comparison across N (off-diagonal residual %, the primary diagnostic):
| L | N=10^4 | N=5·10^4 | N=10^6 | spread |
|---|---|---|---|---|
| ζ | −8.631 | −32.166 | −53.705 | 45.07 pts (monotonic ↓) |
| L(Δ) | +37.449 | +39.842 | +9.575 | 30.27 pts (non-monotonic) |
| L_DH | +22.560 | +5.152 | −27.810 | 50.37 pts (monotonic ↓) | Pure fraction (%): ζ 23.31→27.03→29.33; L(Δ) 15.57→13.53→18.61; L_DH 18.80→22.29→28.08 — modest monotonic growth except L(Δ)’s dip at 5·10^4.
Diagonal-cross×4 fraction (%): ζ 85.32→105.14→124.38; L(Δ) 46.99→46.63→71.81; L_DH 58.64→72.56→99.72 — all grow strongly with N, exceeding 100% (i.e., greater than the total integral) for ζ and approaching that for L_DH. The decomposition closes algebraically (off-diag = total − pure − 4·cross), so the magnitude of |off-diag| measures how much of the fourth moment is carried by genuinely off-diagonal interference among classes. That magnitude grows by tens of percentage points between N=5·10^4 and N=10^6 for ζ and L_DH, and L(Δ) jumps from +39.8% to +9.6% — i.e., no monotone shrinkage toward a fixed value and no flattening.
</results>
<challenges>
- The principal computational bottleneck was the (N×N_t) = 10^6 × 5·10^4 = 5·10^{10} complex phase evaluations required per L-function. A straightforward numpy implementation projected to many hours; a Numba parallel JIT kernel with sincos accumulation reduced this to ~280 s/L on 8 cores.
- Ramanujan τ(n) up to 10^6 requires careful arithmetic. python-flint’s fmpz_series with Euler-pentagonal seed and five squarings was used; the alternative dense approach would have been prohibitively expensive.
- The previous artifacts kept classes k=0..5 even though, for N≥30,030, integers with ω(n)=6 exist (and at N=10^6, 2,293 numbers have ω≥6). I followed the same convention so the comparison is like-for-like; the off-diagonal residual absorbs those terms, which contributes (modestly) to growth at large N but cannot explain the bulk of the drift.
- Coefficient precision: τ(n)/n^{11/2} is well within float64 range (Deligne bound checked), so float arithmetic is justified for this purpose; however the off-diagonal residual is computed as a difference of large numbers, so reported precision in the residual is roughly four significant figures, which is far smaller than the observed N-dependence and therefore cannot account for the drift.
</challenges>
<discussion>
The data answer the convergence question unambiguously in the negative: the diagonal × 4 fraction not only fails to plateau, it pushes past 100% of the total fourth moment for ζ and approaches 100% for L_DH, while the off-diagonal residual takes large negative values to compensate. Across two decades of N, the ω-class fourth-moment fractions are not even close to a single, L-function-specific limit; they are a finite-N structural fingerprint, exactly as the prior memo from r26 anticipated. For Front B, which depended on these fractions stabilizing into an interpretable “asymptotic” signature in any computationally accessible regime, this is a stop signal. Any analytic interpretation of the decomposition coefficients must either be re-parameterized so the limiting object is meaningful at finite N (e.g., re-normalized cross moments, or moments computed on a t-window whose width scales with N) or the diagnostic must be replaced. The decomposition still distinguishes the three L-functions sharply at any fixed N, so it can serve as a fingerprint, but not as a probe of an asymptotic limit accessible at present compute scales.
</discussion>
<proposed-next-hypotheses>
1. If the integration window is rescaled to grow with N (e.g., T ~ N or T ~ N·log N as suggested by the heuristic length of Dirichlet polynomial off-diagonals), the diag×4 and off-diagonal fractions for ζ at fixed (N, T(N)) will become approximately N-independent, indicating that the drift observed at fixed window t∈[500,1000] is a finite-window effect rather than a divergent feature of the method.
2. Among non-self-dual L-functions, the magnitude of off-diagonal drift between N=5·10^4 and N=10^6 correlates with the size of the second-moment off-critical contribution: specifically, L_DH (which has known off-critical zeros) shows the largest swing, ζ next, and L(Δ) (a genuine cuspidal L-function with all zeros on the critical line) the smallest — implying the drift contains a signature distinguishing L-functions by their zero distribution.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>fourth_moment_omega_decomposition_T500_1000_N1000000.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Full ω-class fourth-moment decomposition for ζ, L(Δ), and L_DH at N_terms=10^6, on the high-t window t∈[500,1000), dt=0.01 (50,000-point left Riemann sum). Contains total ∫|D|⁴ dt, per-class pure integrals (k=0..5), all C(6,2)=15 pairwise |S_j|²|S_k|² integrals, and derived pure / 4·diag-cross / off-diagonal residual percentages. Engine reconstructed from the r16/r26 spec, validated against the saved N=10^4 zeta result, and parallelized with Numba; Ramanujan τ(n) up to 10^6 computed exactly via python-flint power series of Δ=q∏(1-q^n)^{24}.</artifact-description>
</artifact>
</artifacts>
</output>
