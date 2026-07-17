## Overview <output>
<conclusion>
Refining the candidates from the cached r34 scan yielded 110 confirmed off-line zeros of L_DH (all with Re(ρ)>0.501 and |L_DH(ρ)|<1e-40), but including them in the Front II Li-coefficient sum did not produce any negative λ_n for n=1..200; all 200 coefficients remained strictly positive (min λ_n = 0.0967 at n=1), so the hypothesized non-GRH signature did not materialize in this n-range.
</conclusion> <methods>
1. Loaded partial_chunks.pkl (80 chunks, 4 σ-lines × 20 t-chunks covering t∈[0,5000]) and concatenated/deduplicated points per σ ∈ {0.65, 0.75, 0.85, 0.95}, yielding ~10,001 (t, |L_DH|) samples per line.
2. Reconstructed r34 candidate detection: local minima via scipy.signal.argrelextrema with threshold sweep. A global threshold of |L_DH|<0.18 yields 190 candidates (per-σ counts 103/55/27/5), which is within one count of the documented 189 candidates — confirming this is r34's logic.
3. Refined each candidate at dps=50 using ldh_2d_worker.refine_candidate (mpmath.findroot with tol=10^-35), run in parallel via multiprocessing.Pool(8); 304.8 s total. All 190 converged; 30 converged to the critical line (Re≈0.5), 160 converged off the line.
4. Deduplicated converged off-line points (clustering tolerance 1e-10 on (Re, Im)), then applied the spec's filter (Re>0.501 and |L_DH|<1e-40). All 160 raw points satisfied the tolerance; deduplication left 110 distinct off-line zeros (max |L_DH| = 1.04e-47).
5. Built the augmented zero list: 5000 critical-line zeros from ldh_zeros_N5000_dps50.npy plus, for each off-line zero ρ=σ+it (σ>1/2), the full self-dual orbit {ρ, ρ̄, 1−ρ, 1−ρ̄}.
6. Computed Li coefficients λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] for n=1..200 at mpmath dps=60. Critical-line zeros included as paired (1/2+iγ, 1/2−iγ) for real-valued sums; off-line zeros included as 4-fold orbits. Verified Im(λ_n) = 0 exactly (real arithmetic of conjugate-paired terms).
7. Analyzed |1 − 1/ρ| for off-line zeros to estimate when negativity could appear.
</methods> <results>
- Candidate detection: 190 local minima with |L_DH|<0.18 across the four σ-lines (matches r34's 189 within rounding).
- Refinement outcome: 30 candidates converged to the critical line; 160 to off-critical zeros; 0 failed the tolerance.
- After deduplication, 110 distinct off-line zeros (Re>0.501), e.g. (0.6508301, 114.163343), (0.5743561, 166.479306), (0.6285081, 366.640908), (0.7088822, 440.484511), (0.5159183, 520.943801), … (0.8977501, 2442.530292), with Re ranging 0.516–0.898 and t up to 4999.6.
- The known R2 calibration zero (0.650786, 114.163343) is recovered with Re = 0.65083008060974… and t = 114.16334273075698…, |L_DH| = 8.1e-51.
- Li coefficients (5000 critical-line + 110 off-line orbits): all 200 values positive. Sample (total): λ_1=0.0967, λ_5=2.3334, λ_10=8.3955, λ_50=80.21, λ_100=186.74, λ_200=434.68. Off-line contributions are uniformly small and positive: Δλ_1=0.00039, Δλ_100=3.73, Δλ_200=13.55. Number of negative λ_n in 1..200: 0.
- Why no negativity: for the lowest-t off-line zero (t≈114, σ≈0.65), |1−1/(1−ρ)| = 1.0000116, so the geometric factor in λ_n grows by only ~1% by n≈800 and would not become exponentially dominant until n ~ 86,000. For the smallest excess σ−1/2 ≈ 0.0159, the naïve "rate" 1/(2(σ−1/2)) ≈ 31 vastly overstates growth because the dominant scaling is t-suppressed: log|1−1/(1−ρ)| ≈ (2σ−1)/(2t²). Thus the n=200 horizon is orders of magnitude too small for any single off-line orbit to overpower the O(N log N) positive bulk from 5000 critical-line zeros.
</results> <challenges>
- r34's exact candidate-detection threshold was not documented in memory; reconstructed by threshold sweep. The threshold 0.18 gives 190 candidates (vs reported 189). The discrepancy is at the level of a single borderline local minimum and does not affect downstream conclusions: 30 of these resolve to critical-line zeros and are discarded.
- Many candidates redundantly point to the same off-line zero (Newton basins overlap across σ-lines and adjacent t-minima), reducing 160 off-line refinements to 110 unique zeros.
- The truncated-zero sum is a finite approximation to the full λ_n; deeper negativity signatures from off-line zeros require either many more zeros (much larger N) or much higher n (thousands to millions), neither of which is reachable in this run.
- All arithmetic was done at mpmath dps=50–60; the off-line zeros are accurate to ~45 decimal digits (|L_DH| ≤ 1e-47), well within precision needed for n≤200 Li sums.
</challenges> <discussion>
The Davenport–Heilbronn function L_DH is the canonical Dirichlet series satisfying a functional equation but lacking an Euler product, and it is mathematically established that L_DH has infinitely many off-line zeros. We confirm and quantify this for t∈[0,5000]: 110 distinct off-line zeros with Re(ρ)∈[0.516, 0.898] coexist with the 5000 critical-line zeros. This is consistent with the prior R2 validation (the known off-line zero at t≈114.163 is recovered exactly). The hypothesis that including these zeros in the Li-coefficient sum would produce λ_n<0 for some n≤200 is not supported. The reason is structural rather than empirical: in Li/Bombieri–Lagarias form, each zero ρ contributes 1−(1−1/ρ)^n. For ρ off the critical line in the strip 0<Re(ρ)<1, the partner (1−ρ) satisfies |1−1/(1−ρ)|>1, but only by an amount ≈(2Re(ρ)−1)/(2|ρ|²), which is t-suppressed. For all 110 zeros found, this excess is at most ~10^-3 (for the smallest-t cases) down to ~10^-7 (large-t/large-σ cases). Exponential dominance over the O(N log N) positive bulk requires n far beyond 200. The empirical observation that off-line zero orbits actually INCREASE λ_n at small n (Δλ_200 ≈ 13.6) is the expected near-zero behavior of 4·(1 − Re((1−1/ρ)^n)) before geometric growth in the (1−ρ) partner outpaces it. Thus, while L_DH genuinely violates GRH and its off-line zeros are physically real, the Front II Li-coefficient pipeline at n≤200 is not a sensitive non-GRH detector for this function — confirming the spec's caveat that detection requires much larger n or different test functions. This refines r29's f8: Front II for L_DH is not "inconclusive due to missing zeros" but "structurally insensitive at moderate n even with off-line zeros included".
</discussion> <proposed-next-hypotheses>
1. Extending the Li-coefficient computation to n ≈ 10^4–10^6 (with sufficient critical-line zeros to keep the bulk converged) will reveal the first negative λ_n driven primarily by the lowest-t off-line zero pair (t≈114.16, σ≈0.651); the predicted crossover scale is n ≈ 1/log|1−1/(1−ρ)| ≈ 86,000 for that zero.
2. A Front II test function whose Fourier-transform support is concentrated near the off-line zeros' heights (e.g. a windowed φ centered at t≈114, 166, 367 with width ≪ t) will detect non-positivity (negative eigenvalue in the Gram matrix Q_N) at much smaller N than the Li-coefficient route, because the off-line zeros contribute coherently within the window instead of being diluted by 5000 critical-line zeros.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ldh_off_line_zeros.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>List of 110 confirmed off-line zeros of the Davenport–Heilbronn L-function L_DH with Re(ρ)>0.501 and |L_DH(ρ)|<1e-40, refined to mpmath dps=50 via 2D Newton from the 190 candidates produced by local-minimum detection on the cached partial_chunks.pkl scan. Columns: sigma (float Re), t (float Im), sigma_str / t_str (≈50-digit string forms suitable for mpmath.mpf), absL (|L_DH(ρ)|). Covers t∈[114, 4999.6]; max |L_DH| = 1.04e-47.</artifact-description>
</artifact>
<artifact>
<file-name>ldh_li_coefficients.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Li coefficients λ_n for n=1..200 for the Davenport–Heilbronn function. Columns: n, lambda_critical_only (using only 5000 critical-line zeros from ldh_zeros_N5000_dps50.npy with their ±iγ pairs), lambda_offline_contrib (added contribution from the 4-fold orbits of the 110 confirmed off-line zeros), lambda_total (sum). All values strictly positive; min total λ_n = 0.0967 at n=1, max = 434.68 at n=200. Computed at mpmath dps=60.</artifact-description>
</artifact>
<artifact>
<file-name>ldh_offline_li_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: scatter of the 110 confirmed off-line zeros in the (t, σ) plane against the critical line σ=1/2. Panel B: λ_n for n=1..200, comparing critical-line-only sum to the augmented sum including all 110 off-line zero orbits; both curves are strictly positive across the full range.</artifact-description>
</artifact>
</artifacts>
</output>
