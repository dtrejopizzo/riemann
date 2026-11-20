## Overview # RESEARCH HYPOTHESIS ASSESSMENT: CONFIRMED The hypothesis that a pre-computed dataset of Dirichlet partial sum magnitudes |D_F(t*;N)| at resonance peaks t* can be generated within a feasible timeframe is **CONFIRMED**. The dataset was successfully generated in 35.4 minutes, well within the 90-minute computational budget. ## QUANTITATIVE EVIDENCE **Dataset Specifications:**
- **Total records:** 600 (60 peaks × 10 N values)
- **Functions:** 3 (ζ(s), L_DH(s), L(s,λ))
- **Peaks per function:** 20 (identified from t ∈ [1000, 5000] at N=10⁵)
- **N values:** 10 logarithmically-spaced points from 10⁴ to 10⁷
- **Output:** Single CSV file (43.4 KB) with columns: function_class, peak_t, N, D_magnitude, R_comp
- **Computational time:** 35.4 minutes (peak finding: 2.5 min, D_magnitude: 17.0 min, R_comp: 14.7 min) **Data Quality Validation:**
- Zero missing values (600/600 complete records)
- All D_magnitude values positive and in range [5.496, 21.928]
- All R_comp values in valid range [0.000016, 0.062017]
- Expected N-dependence patterns observed: - D_magnitude increases with N for 90% of peaks (54/60) - R_comp decreases with N for 100% of peaks (60/60) **Key Findings:**
1. **L(s,λ) exhibits strongest resonance:** Maximum D_magnitude = 21.93 at t*=4337.26, N=10⁷, representing a 1.53× growth from N=10⁴
2. **L_DH shows flat scaling:** Typical growth factor ~1.00 from N=10⁴ to N=10⁷, consistent with prior literature findings of near-zero growth exponents at off-line zero locations
3. **ζ(s) shows moderate growth:** Typical growth factor ~1.07, consistent with log-correlated field behavior
4. **R_comp universally decays:** All functions show 50-150× reduction in composite coherence from N=10⁴ to N=10⁷, confirming phase randomization with increasing truncation length **Methodological Rigor:**
- Kahan compensated summation implemented for all partial sum computations (median relative error 2.95×10⁻¹⁴ from prior validation)
- L_DH coefficient structure validated: period-5 pattern confirmed, coefficients zero at multiples of 5
- Peak identification using scipy.signal.find_peaks with minimum separation constraint
- R_comp computed via circular statistics (mean resultant length) on composite squarefree terms (ω(n) ≥ 2) ## DOWNSTREAM UTILITY DEMONSTRATED The dataset enables rapid analysis of N-dependence without re-computing expensive partial sums:
- **GEV fitting** for extreme value distributions can now use 10 N-points per peak (vs. previous 3-point analyses)
- **Power-law vs log-correlated model selection** can be performed across all 60 peaks simultaneously
- **Multi-function classification** can leverage both D_magnitude and R_comp features across dense N-scales
- **Computational savings:** Each downstream analysis that would have required 600 partial sum evaluations (~35 minutes) can now be performed instantly via CSV lookup The dataset directly addresses the computational bottleneck identified in the research context, where "full-scale computations involving large N over wide t ranges are often infeasible" and "some tasks estimated to require 40+ hours of CPU time." --- ## DISCRETIONARY ANALYTICAL DECISIONS - **Peak identification t-range:** Set to t ∈ [1000, 5000] rather than wider ranges to balance resolution and computational cost within 90-minute budget
- **Grid spacing for peak finding:** Used Δt = 5 × (2π/log(N)) coarse grid (1466 points) rather than theoretical minimum Δt = 2π/log(N) (7330 points) to reduce peak-finding time from ~12 minutes to ~2.5 minutes; this provides sufficient resolution while maintaining 90% computational budget for dense N-scale evaluations
- **Peak count:** Set to top 20 peaks per function rather than all local maxima to focus on highest-amplitude resonances most relevant for downstream analyses
- **N value selection:** Logarithmic spacing chosen to capture both small-N and large-N behavior: {10⁴, 2×10⁴, 5×10⁴, 10⁵, 2×10⁵, 5×10⁵, 10⁶, 2×10⁶, 5×10⁶, 10⁷}
- **R_comp definition:** Implemented as mean resultant length of composite squarefree terms (ω(n) ≥ 2), following the research literature's focus on composite-driven resonance mechanisms
- **Minimum peak separation:** Set to 2 grid points (~5.5 in t-space) to avoid identifying closely-spaced oscillations as separate peaks
- **Function selection:** Analyzed ζ(s) [F1], L_DH(s) [F4], and L(s,λ) [F6] as specified in research objective; omitted other function classes (L(s,χ₄), random multiplicative) to meet computational constraints 