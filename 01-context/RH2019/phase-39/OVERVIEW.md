## Overview ## Analysis of f_canon_rand at N=10^6: r metric and ω-class structure Due to computational limitations at N=10^7 (each Dirichlet sum evaluation taking >30 seconds with vectorized summation, making grid searches infeasible within the time budget), I successfully completed the full analysis for N=10^6 only. ### Results for N=10^6 (Top 5 Peaks) **Peak Identification:**
I performed a coarse grid search over t ∈ [10^6, 2×10^6] with spacing 100 (10,000 points, completed in 10.1 minutes), followed by fine refinement. The top 5 peaks are: 1. t = 1420300.0, |D| = 49.09987
2. t = 1266500.0, |D| = 47.90401
3. t = 1719300.0, |D| = 44.87156
4. t = 1108900.0, |D| = 33.25699
5. t = 1467600.0, |D| = 31.54360 **Canonical r Metric Values:** Peak 1: r = 5.9121, r_adj = 1.8485 (31.3%), r_nonadj = 4.0637
Peak 2: r = 1.7067, r_adj = 1.6486 (96.6%), r_nonadj = 0.0582
Peak 3: r = 5.6365, r_adj = 1.8312 (32.5%), r_nonadj = 3.8053
Peak 4: r = 6.1523, r_adj = 1.8625 (30.3%), r_nonadj = 4.2897
Peak 5: r = 5.3692, r_adj = 1.8222 (33.9%), r_nonadj = 3.5470 **Mean Statistics (N=10^6, top 5 peaks):**
- Mean r = 4.9554
- Mean r_adjacent = 1.8026 (36.4% of total)
- Mean r_non_adjacent = 3.1528 (63.6% of total) **ω-Class Power Distribution:**
All five peaks show broad power distributions across ω-classes 0-19, with peak power typically at ω=3 or ω=4 (25-30% of total power). The distributions are approximately bell-shaped, centered around ω=3-5. ### Computational Constraints Encountered **N=10^7 Analysis:** The analysis could not be completed at N=10^7 due to severe computational limitations:
- Each Dirichlet sum evaluation at N=10^7 takes 30-60 seconds even with vectorized (fast) summation
- A minimal coarse grid search with 1,000 points would require ~8-17 hours
- The available time budget (90 minutes total) and per-cell timeout (20 minutes) made this infeasible
- Coefficient generation for N=10^7 took 6.0 minutes (successfully completed) ### Comparison Impossible **Critical Limitation:** Without N=10^7 results, I cannot determine whether f_canon_rand exhibits "simple, monotonic evolution" or "complex, non-monotonic behavior" as hypothesized. The comparison between N=10^6 and N=10^7 cannot be performed. ### Technical Observations 1. **Computational Bottleneck:** The primary bottleneck is the Dirichlet sum evaluation itself, not coefficient generation or ω-decomposition. At N=10^7, even highly optimized vectorized NumPy code is too slow for grid searches. 2. **Method Validation:** At N=10^6, fast vectorized summation and Kahan summation produce identical results to machine precision (differences ~10^-16), confirming numerical stability at this scale. 3. **Peak Structure:** The coarse grid spacing of 100 at N=10^6 was sufficient to capture peaks accurately - fine grid refinement (spacing=1) yielded no improvement, suggesting peaks have width >> 100. 4. **One Anomalous Peak:** Peak 2 (t=1266500) shows strikingly different r structure with 96.6% adjacent contribution, compared to 30-34% for the other four peaks. This suggests heterogeneity in peak structure even for non-arithmetic functions. ### Conclusions **Partial Hypothesis Test:** I can report baseline r metric behavior for f_canon_rand at N=10^6 (mean r = 4.96), but cannot assess evolution to N=10^7. The hypothesis regarding "simple, monotonic evolution" versus "complex, non-monotonic behavior" **remains untested** due to computational infeasibility. **Methodological Insight:** For N=10^7 analysis of this function, alternative approaches are required:
- Compiled implementations (Cython, Numba, C++)
- Random sampling rather than grid searches
- Pre-selection of specific t values based on theory
- More powerful computational resources **Baseline Established:** This analysis provides the first rigorous characterization of f_canon_rand's r metric at N=10^6, establishing a baseline for future large-N studies with adequate computational resources. --- ## DISCRETIONARY DECISIONS - **Grid spacing for N=10^6 coarse search:** Used spacing of 100, resulting in 10,000 evaluation points over t ∈ [10^6, 2×10^6]
- **Number of peak candidates:** Selected top 20 candidates from coarse search for refinement, ultimately analyzing top 10 refined peaks
- **Fine grid spacing:** Used spacing of 1.0 for fine grid search within ±100 window around coarse peaks
- **Number of peaks for final analysis:** Analyzed top 5 peaks for full ω-decomposition and r metric computation
- **Summation method for grid searches:** Used vectorized fast summation for coarse/fine grid searches; reserved Kahan summation only for final peak evaluation
- **Random seed:** Used seed=42 for f_canon_rand coefficient generation (inherited from pre-computed prime data artifact)
- **N=10^7 grid sampling strategy:** Attempted 1,000 point linear spacing (spacing ~10,000) before timeout - this proved computationally infeasible
- **External artifact used:** f_canon_rand_primes_N1e7.pkl (prime coefficients up to 10^7), omega_values_N1e6.pkl and omega_values_N1e7.pkl (pre-computed Ω values) 