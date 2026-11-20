## Overview ## Answer The hypothesis that positive inter-class energy ratio r at N=10,000 is a small-N artifact has been **strongly validated** for the zeta function. For the Liouville function, the hypothesis of persistent negativity across all N has been **partially refuted**. ### Key Quantitative Results **Zeta Function (Q4 - Highest Peaks):**
- N=10⁴: mean(r) = +1.778 ± 0.920 (n=50 peaks)
- N=10⁵: mean(r) = -0.208 ± 0.098 (n=50 peaks) - N=10⁶: mean(r) = -0.203 ± 0.092 (n=35 peaks)
- Change: Δr = -1.98 (111% reduction with sign flip from positive to negative)
- At N=10⁶, 94.3% of Q4 peaks have r < 0
- Pearson correlation with peak height: +0.344 at N=10⁴ → -0.343 at N=10⁶ (sign flip)
- 95% CI at N=10⁶: [-0.235, -0.171] (significantly negative) **Liouville Function (Q4 - Highest Peaks):**
- N=10⁴: mean(r) = -0.948 ± 0.072 (n=50 peaks)
- N=10⁵: mean(r) = -0.217 ± 0.121 (n=50 peaks)
- N=10⁶: mean(r) = -0.213 ± 0.109 (n=33 peaks)
- Change: Δr = +0.736 (78% reduction in magnitude, no sign flip)
- At N=10⁶, 97.0% of Q4 peaks still have r < 0
- Pearson correlation with peak height: -0.216 at N=10⁴ → -0.453 at N=10⁶ (strengthening)
- 95% CI at N=10⁶: [-0.252, -0.173] (significantly negative) ### Convergence Analysis Both functions show rapid convergence with minimal change between N=10⁵ and N=10⁶:
- Zeta Q4: |Δr| from 10⁵→10⁶ = 0.005 (vs. 1.99 from 10⁴→10⁵)
- Liouville Q4: |Δr| from 10⁵→10⁶ = 0.005 (vs. 0.73 from 10⁴→10⁵) All quartiles (Q1-Q4) for both functions show this pattern: large transitions from N=10⁴ to N=10⁵, then stabilization at N=10⁶. ### Unexpected Discovery At large N, both zeta and Liouville functions converge to remarkably similar r values at high peaks (Q4: r ≈ -0.20), suggesting a universal asymptotic behavior independent of coefficient structure. The strong differentiation observed at N=10⁴ (zeta: +1.78 vs. Liouville: -0.95) was entirely an artifact of insufficient truncation. ### Tables of Mean r by Quartile **Zeta Function:**
| Quartile | N=10⁴ | N=10⁵ | N=10⁶ |
|----------|-------|-------|-------|
| Q1 (lowest) | +0.819 | +0.054 | +0.071 |
| Q2 | +1.236 | +0.024 | +0.033 |
| Q3 | +1.270 | -0.062 | -0.044 |
| Q4 (highest) | +1.778 | -0.208 | -0.203 | **Liouville Function:**
| Quartile | N=10⁴ | N=10⁵ | N=10⁶ |
|----------|-------|-------|-------|
| Q1 (lowest) | -0.844 | +0.166 | +0.156 |
| Q2 | -0.885 | +0.040 | +0.092 |
| Q3 | -0.933 | -0.099 | -0.003 |
| Q4 (highest) | -0.948 | -0.217 | -0.213 | --- ## Discretionary Decisions - **Truncation values**: Analyzed N ∈ {10⁴, 10⁵, 10⁶} as specified in research objective
- **t-range setting**: Set T=N for each truncation (e.g., t ∈ [10⁵, 2×10⁵] for N=10⁵)
- **Number of t-points**: Used 2,000 points for N=10⁴ and N=10⁵; reduced to 1,000 for N=10⁶ to ensure completion within 5,400s runtime limit
- **Peak detection parameters**: prominence=1.0, distance=5 (matching original dataset methodology)
- **Number of peaks analyzed**: Requested top 200 peaks; obtained fewer for N=10⁶ (139 zeta, 132 Liouville) due to reduced t-sampling
- **ω-class range**: k_max=4 (matching original dataset)
- **Quartile binning**: Used numpy.percentile with boundaries at 25%, 50%, 75% of peak heights
- **Numerical method**: Kahan compensated summation for all Dirichlet polynomial evaluations
- **Significance level**: α=0.05 for confidence intervals
- **Correlation method**: Reported both Pearson (parametric) and Spearman (rank-based) correlations
- **External data**: Used existing N=10,000 data from `omega_decomposition_peaks_N10000.pkl` as baseline 