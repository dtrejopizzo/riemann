## Overview # Analysis of Inter-Class Energy Ratio r for f_canon_rand: N=10^6 Results and N=10^7 Computational Limits ## Summary I successfully completed the analysis for **N=10^6** with 5 peaks showing mean r = 3.090 ± 1.445 and 60.89% adjacent / 39.11% non-adjacent interference structure. However, the **N=10^7 analysis could not be completed** due to computational constraints exceeding available runtime limits. The Kahan summation required for ω-class decomposition takes >20 minutes per evaluation at N=10^7, making the full analysis infeasible within the 5400-second runtime limit. ## Detailed Results for N=10^6 ### Peak Identification and Refinement
Using sparse grid search (1000 points over t ∈ [10^6, 2×10^6]) with Numba-accelerated summation (35.8s), followed by Kahan-based refinement, I identified and analyzed 5 peaks: | Peak | t (refined) | |D| | r | Adjacent % | Non-adjacent % |
|------|-------------|-----|---|------------|----------------|
| 1 | 1,543,870.24 | 17.81 | 5.117 | 34.71 | 65.29 |
| 2 | 1,216,451.12 | 8.98 | 1.689 | 87.84 | 12.16 |
| 3 | 1,220,985.68 | 13.54 | 2.555 | 63.05 | 36.95 |
| 4 | 1,548,856.51 | 10.38 | 4.044 | 44.10 | 55.90 |
| 5 | 1,906,158.58 | 5.89 | 2.046 | 74.77 | 25.23 | ### N=10^6 Statistical Summary
- **Mean r**: 3.090088
- **Standard deviation**: 1.445232
- **Range**: [1.689, 5.117]
- **Mean adjacent contribution**: 60.89%
- **Mean non-adjacent contribution**: 39.11% The ω-class decomposition showed perfect reconstruction (error < 10^-6) at all peaks, with 20 ω-classes present at N=10^6. ## N=10^7 Computational Failure ### Progress Achieved
- Sparse grid search completed successfully (870.8s for 1000 evaluations)
- Top 5 peaks identified: t ∈ [11.5M, 18.4M], |D| ∈ [23.3, 36.0]
- Magnitude range: [0.024, 35.95] ### Computational Barrier
The analysis failed at the peak refinement stage. A single Kahan summation evaluation at N=10^7 requires >1200 seconds (20 minutes), making it impossible to:
1. Refine 5 peak locations (each requires ~10-15 minimization iterations)
2. Perform ω-class decomposition for 5 peaks (each requires a full N=10^7 Kahan pass) **Total estimated time for complete N=10^7 analysis**: >6 hours (far exceeding the 90-minute runtime limit) ## Interpretation of Available Results ### Cannot Address Primary Hypothesis
The research hypothesis requires comparing N=10^6 and N=10^7 statistics to assess monotonic evolution. With only N=10^6 data available, I **cannot determine whether r evolves monotonically** from N=10^6 to N=10^7. ### N=10^6 Characteristics
The f_canon_rand function at N=10^6 shows:
- **Moderate inter-class interference** (r ≈ 3.1, indicating numerator is ~3× the denominator)
- **Dominant adjacent-class interference** (60.89%), but substantial non-adjacent contribution (39.11%)
- **High peak-to-peak variability** (CV = 46.8%), suggesting stochastic variation in interference patterns ### Methodological Validation
- Numba acceleration provided 35× speedup but remains insufficient for N=10^7 decomposition
- ω-class decomposition achieved perfect reconstruction at N=10^6 (error < 10^-6)
- Two-phase approach (Numba grid + Kahan refinement) worked well for N=10^6 but hits computational cliff at N=10^7 ## Conclusion **The analysis partially failed.** I successfully computed r = 3.090 ± 1.445 with 60.89% adjacent interference for f_canon_rand at N=10^6 across 5 peaks, but the N=10^7 analysis could not be completed within computational limits. The fundamental computational barrier is that ω-class decomposition at N=10^7 requires Kahan summation (for precision), which takes >20 minutes per evaluation. This creates an insurmountable time constraint for analyzing multiple peaks. **Without N=10^7 data, the hypothesis of monotonic evolution cannot be tested.** The task requires either compiled code (C/Cython), pre-computed decompositions, or acceptance of lower precision (which may invalidate r calculations at N=10^7). --- ## DISCRETIONARY DECISIONS - **Statistical significance threshold**: Not applicable (no hypothesis test performed)
- **Number of peaks analyzed**: 5 peaks per N value (as specified in research objective)
- **Grid search density**: 1000 points over t ∈ [N, 2N] (as specified)
- **Peak refinement method**: Kahan-compensated summation with scipy.optimize.minimize_scalar, bounded method, xatol=1e-6
- **ω-class decomposition precision**: Kahan-compensated summation for all class sums (to minimize float64 precision errors)
- **r metric definition**: Canonical formula r = Σ_{j≠k} Re[S_j S̄_k] / Σ_k|S_k|² with symmetry factor of 2 for j<k pairs
- **Adjacent vs non-adjacent classification**: Adjacent defined as |j-k|=1, non-adjacent as |j-k|>1
- **Random seed**: 42 (for reproducibility, consistent with dataset generation)
- **Coefficient pre-computation method**: Sieve-based multiplicative algorithm (efficient but required validation against direct factorization)
- **N=10^7 computational strategy**: Attempted Kahan refinement, fell back to grid values when time limit exceeded (ultimately analysis could not complete)
- **External artifacts used**: - f_canon_rand_primes_N1e7.pkl (prime coefficients up to 10^7) - omega_values_N1e6.pkl (Ω(n) values for N=10^6) - omega_values_N1e7.pkl (Ω(n) values for N=10^7, prepared but not used due to timeout) 