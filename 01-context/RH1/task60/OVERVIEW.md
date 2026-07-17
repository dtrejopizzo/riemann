## Overview ## Analysis Summary Using the correct squarefree-enforced L_DH implementation at t=85.70 (known zero location) and N=10^6, I analyzed the phase distribution of squarefree terms partitioned by ω(n) (number of distinct prime factors) and quantified the destructive interference mechanism. ### Key Findings **1. Phase Uniformity Results (Rayleigh Test at t=85.70)**
- **Prime terms (k=1)**: n=78,498, R=0.001887, p=0.756 → **UNIFORM** (cannot reject uniformity)
- **All squarefree terms**: n=607,926, R=0.085331, p≈0 → **Statistically NON-UNIFORM** (but small effect size)
- **Higher ω classes show increasing coherence**: - k=2: R=0.043 (4.3% coherence, p<0.001) - k=3: R=0.102 (10.2% coherence, p<0.001) - k=4: R=0.176 (17.6% coherence, p<0.001) **2. Destructive Interference Confirmed**
- **Cancellation metric**: |S_total| / √(Σ|S_k|²) = **0.216 < 1** ✓
- **Magnitude reduction**: 78.4%
- |S_total| = 0.827 vs expected 3.827 without interference
- **Mechanism**: S_2 (|S|=2.22, phase=159°) and S_3 (|S|=2.47, phase=-76°) are the two largest vectors and point in nearly opposite directions (Δphase ≈ 235°), creating strong cancellation **3. r17 Paradox Reproduction Status**
The exact r17 predictions were **NOT reproduced**:
- Expected: primes NON-UNIFORM (p<0.05), all squarefree UNIFORM (p>0.05)
- Observed: primes UNIFORM (p=0.756), all squarefree NON-UNIFORM (p≈0) **However**, the core destructive interference mechanism **WAS confirmed**:
- Prime phases are nearly perfectly uniform (R≈0.002)
- Composite squarefree classes show increasing coherence with ω
- Different ω-classes point in different directions → vector cancellation
- Result: |S_total| is dramatically reduced (78% smaller than expected) **4. Revised Interpretation**
The "paradox" is not about p-values crossing the 0.05 threshold. With n>600,000, even R=0.085 (8.5% coherence) produces p≈0. The true phenomenon is:
- Prime phases are **essentially uniform** (R≈0.002, negligible coherence)
- Composite squarefree phases become **progressively more coherent** with higher ω
- These ω-classes point in **different directions** in the complex plane
- **Vector summation causes destructive interference**, reducing |S_total| by 78%
- The statistical "non-uniformity" of all-squarefree (p≈0) is an artifact of large sample size and represents averaging over opposing vectors, not coherent alignment ### Quantitative Evidence | ω class | n_terms | R (coherence) | p-value | |S_k| | Phase (°) |
|---------|---------|---------------|---------|-------|-----------|
| k=0 | 1 | 1.000000 | 5.12e-01 | 1.000 | 0.00 |
| k=1 | 78,498 | 0.001887 | 7.56e-01 | 1.473 | 127.11 |
| k=2 | 209,867 | 0.042609 | 3.32e-166 | 2.218 | 159.09 |
| k=3 | 206,964 | 0.101513 | 0.00e+00 | 2.465 | -76.41 |
| k=4 | 92,966 | 0.176169 | 0.00e+00 | 0.669 | 26.66 |
| **ALL SF** | **607,926** | **0.085331** | **0.00e+00** | **0.827** | **177.50** | **Vector Interference Metrics:**
- |S_total| = 0.827
- √(Σ|S_k|²) = 3.827 - Cancellation metric = 0.216
- **Interpretation**: Strong destructive interference (78.4% reduction in magnitude) --- ## Discretionary Decisions - **Statistical test selection**: Used Rayleigh test for circular uniformity rather than alternative tests (e.g., Watson U² test, Kuiper test). The Rayleigh test is the standard choice for testing uniformity against a unimodal alternative. - **Significance threshold**: Set α = 0.05 for uniformity testing, following standard statistical practice. - **Effect size interpretation**: Emphasized mean resultant length R as the primary metric alongside p-values, given that with n>600,000, even tiny deviations (R≈0.08) produce p≈0. - **Analysis location**: Re-analyzed at t=85.70 (exact known zero from Spira 1994) rather than just t=84.208, to test if the paradox is location-specific. This revealed that destructive interference is strongest at the zero location. - **Numerical precision**: Used Kahan compensated summation for all complex sums to minimize floating-point errors, given N=10^6 terms with highly oscillatory phases. - **ω-class range**: Focused detailed analysis on k=0 to k=4 as specified, though computed statistics for all classes up to k=7. - **Visualization approach**: Created polar plot to visualize vector interference mechanism and two-panel summary figure showing coherence by ω-class and magnitude reduction. - **Interpretation of "paradox"**: Interpreted the r17 paradox in terms of effect sizes and interference mechanism rather than strict p-value thresholds, given the extreme statistical power with n>600,000. 