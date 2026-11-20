## Overview # ANSWER TO RESEARCH HYPOTHESIS The hypothesis that low fragility scores at ζ(s) resonance peaks are due to the change vector ΔV being nearly orthogonal to the main sum vector V_1 is **REJECTED**. ## Quantitative Evidence **1. Relative Magnitude (M_rel = |ΔV| / |V_1|):**
- Peak ordinates: median = 0.009014 (IQR: 0.004705-0.014051)
- Random ordinates: median = 0.085040 (IQR: 0.051646-0.310334)
- Mann-Whitney U test: p < 0.001, rank-biserial r = 0.94 (highly significant, ~9-fold difference) **2. Alignment Angle (θ between ΔV and V_1):**
- Peak ordinates: median = 93.24° (IQR: 51.38°-133.87°)
- Random ordinates: median = 113.86° (IQR: 69.42°-143.41°)
- Mann-Whitney U test: p = 0.351, rank-biserial r = 0.18 (NOT significant)
- Reference: 90° indicates orthogonality **3. Absolute Change Magnitude (|ΔV|):**
- Peak ordinates: median = 0.097850
- Random ordinates: median = 0.116494
- Mann-Whitney U test: p = 0.365, rank-biserial r = 0.17 (NOT significant) **4. Initial Sum Magnitude (|V_1|):**
- Peak ordinates: median = 10.5294 (IQR: 8.89-11.67)
- Random ordinates: median = 1.0577 (IQR: 0.62-2.04)
- Mann-Whitney U test: p < 0.001, rank-biserial r = -0.94 (highly significant, ~10-fold difference) **5. Angle Distribution:**
- Kolmogorov-Smirnov test for uniformity [0, π]: Peak angles p = 0.921, Random angles p = 0.346
- Both groups consistent with uniform (random) orientation ## Key Finding The low fragility score at resonance peaks is **NOT** due to orthogonality of ΔV to V_1. Instead: 1. The **absolute change magnitude |ΔV| is statistically indistinguishable** between peaks and random ordinates (p = 0.365)
2. The **alignment angles θ show no significant difference** between groups (p = 0.351) and both are consistent with random orientation
3. The **initial sum magnitude |V_1| is ~10× larger** at peaks by construction (p < 0.001) Therefore, **M_rel = |ΔV| / |V_1| is small at peaks primarily because of the large denominator |V_1|**, not because of any special geometric relationship (orthogonality) between the sum and its increments. The "stability" at peaks is a straightforward consequence of the large resonance amplitude itself—the same absolute perturbation |ΔV| represents a much smaller relative change when divided by a large |V_1|. --- ## DISCRETIONARY DECISIONS - **Statistical test selection**: Mann-Whitney U test (non-parametric) chosen over t-test due to potential non-normality of distributions and small sample sizes (n=20 per group), consistent with dataset methodological standards
- **Significance threshold**: α = 0.05 for all hypothesis tests
- **Peak detection parameters**: Prominence threshold = 2.0 and minimum distance = 5 points (50 units in t) for scipy.signal.find_peaks
- **Effect size metric**: Rank-biserial correlation coefficient computed as r = 1 - 2U/(n₁n₂) for Mann-Whitney U tests
- **Coarse scan resolution**: dt = 10.0 for initial peak identification in t ∈ [5000, 15000]
- **Truncation parameters**: N = 10⁶, ΔN = 1000 (as specified in research objective)
- **Random seed**: seed = 42 for random ordinate selection (as specified)
- **Angle metric**: Alignment angle computed as θ = arccos(Re(V₁ · conj(ΔV)) / (|V₁| · |ΔV|)), where · denotes complex conjugation
- **JIT compilation**: numba @jit(nopython=True) used for Kahan summation to meet computational efficiency requirements
- **Circular statistics**: scipy.stats.circmean and circstd used for circular angle analysis
- **Visualization scale**: Linear scale for both M_rel and θ in final figure to show full distributions including outliers 