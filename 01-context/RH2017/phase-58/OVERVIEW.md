## Overview ## Analysis Results: Vector Interference Pattern of L_DH at Non-Resonant Locations ### Main Conclusion
The hypothesis that "destructive interference (M≈0.2) is specific to L_DH resonances while random non-resonant locations show less cancellation" is **REJECTED**. The analysis reveals the opposite pattern: L_DH resonances exhibit **constructive interference** (M ≈ 1.76), while the strongest destructive interference (M ≈ 0.32) occurs at **quiet, low |D(t)| regions**. ### Key Quantitative Results **1. Cancellation Metric M by |D(t)| Region:**
- **Low |D(t)| locations** (<20th percentile): M = 0.321 ± 0.250 (strong destructive)
- **Random non-resonant** (<95th percentile): M = 0.939 ± 0.585 (moderate)
- **Top resonances** (≥95th percentile): M = 1.758 ± 0.211 (constructive) **2. Statistical Tests:** a) **Random non-resonant vs M = 0.2** (one-sample t-test): - t = 3.998, p = 0.00156 (one-sided) - Cohen's d = 1.264 (large effect) - **Result**: Random locations are significantly greater than M = 0.2 ✓ b) **Low |D(t)| vs M = 0.2** (one-sample t-test): - t = 1.532, p = 0.0799 (one-sided) - **Result**: Low |D(t)| locations are consistent with M ≈ 0.2 ✓ c) **Random vs Low |D(t)|** (two-sample t-test): - t = 3.075, p = 0.0095 - **Result**: Random locations have significantly higher M ✓ **3. Correlation Between |D(t)| and M:**
- **Pearson r = 0.655** (p = 7.35×10⁻²⁶)
- **Spearman ρ = 0.818** (p = 1.60×10⁻⁴⁹)
- Strong, highly significant positive correlation (n=200 samples) **4. Percentile Analysis:**
The cancellation metric M increases monotonically with |D(t)|:
- 10th percentile (|D| ≈ 3.6): M = 0.246 (destructive)
- 50th percentile (|D| ≈ 10.2): M = 1.019 (neutral)
- 95th percentile (|D| ≈ 31.9): M = 1.523 (constructive)
- 99th percentile (|D| ≈ 63.6): M = 1.862 (strong constructive) ### Interpretation The analysis demonstrates that for the Davenport-Heilbronn function L_DH: 1. **Resonances (high |D(t)|) arise from constructive interference**, not from reduced destructive interference. This is similar to the behavior of random multiplicative functions (f_rand), where large peaks show M > 1. 2. **The M ≈ 0.2 value** from previous analyses likely refers to **quiet, low-magnitude regions**, not resonant peaks. These locations exhibit strong destructive cancellation among terms partitioned by ω(n). 3. **Random non-resonant locations** (typical |D(t)|) show intermediate behavior (M ≈ 0.94), with moderate cancellation between ω(n) groups. 4. **The mechanism of L_DH resonances** appears fundamentally different from the hypothesis. Rather than being locations where destructive interference is reduced, resonances are locations where terms constructively align across different ω(n) groups, creating large |D(t)| values through additive reinforcement. This finding has important implications for understanding the extreme value behavior of L_DH: if resonances arise from constructive interference (M > 1), the distribution of |D(t)| maxima should reflect the statistics of constructive alignment events, not the statistics of reduced cancellation events. --- ## Discretionary Analytical Decisions - **Significance level**: Set α = 0.05 for all statistical tests
- **Sample size for random locations**: Selected n = 10 for primary analysis (matches research objective specification)
- **Non-resonant threshold**: Defined as below 95th percentile of |D(t)| (top 5% considered resonant)
- **Random seed**: Set to 42 for reproducible random sampling
- **t-range sampling**: Used dt = 1.0 (integer values) over [1000, 10000] for computational feasibility while maintaining fine resolution
- **Correlation sample size**: Used n = 200 samples for correlation analysis between |D(t)| and M
- **Percentile bins**: Analyzed 10th, 20th, 30th...99th percentiles with ±2 percentile sampling windows
- **One-sided vs two-sided tests**: Used one-sided test for directional hypothesis (M > 0.2), two-sided for comparison tests
- **Kahan summation**: Applied to all D(t) computations for numerical precision (per dataset specification)
- **Squarefree implementation**: Used corrected L_DH coefficients with a_n = 0 for all non-squarefree n (μ(n) = 0)
- **Statistical test selection**: Used parametric t-tests (Student's t) with Welch correction for unequal variances in two-sample comparisons, justified by n ≥ 10 and approximately normal distributions (verified via visual inspection)
- **Effect size metric**: Used Cohen's d for standardized effect size reporting
- **Correlation metrics**: Reported both Pearson (linear) and Spearman (monotonic) correlations to capture relationship robustness
