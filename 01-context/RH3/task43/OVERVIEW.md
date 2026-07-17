## Overview At N=10^5, NO function among zeta, L(s,χ₄), f_rand, L(s,μ), and L(s,λ) exhibits strong conditional anti-correlation at peaks. All functions show mean r values close to zero (range: -0.043 to +0.010), with approximately 50-57% of peaks having r<0, indicating essentially random distribution around r=0 rather than the strong anti-correlation patterns described in the original dataset at N=10^4. **CRITICAL DISCREPANCY**: My recomputation at N=10^4 yields drastically different results from the original dataset description. The original dataset claims zeta has mean r=+1.276 and Liouville has 100% r<0 with mean r=-0.903 at N=10^4. However, my recomputation yields zeta mean r=-0.023 (51% r<0) and Liouville mean r=-0.024 (49% r<0), suggesting either a different computational definition, an error in the original description, or substantial N-dependence in the phenomenon. **Results at N=10^5 (top 200 peaks, t∈[10^5, 2×10^5]):** 1. **Zeta (a_n=1)**: Mean r = -0.043, Median r = -0.036, Std = 0.315, 56.0% r<0
2. **L(s,χ₄) (Dirichlet character mod 4)**: Mean r = +0.010, Median r = -0.021, Std = 0.233, 52.5% r<0
3. **f_rand (multiplicative random)**: Mean r = -0.041, Median r = -0.042, Std = 0.475, 55.0% r<0
4. **L(s,μ) (Möbius function)**: Mean r = -0.002, Median r = -0.010, Std = 0.176, 56.5% r<0
5. **L(s,λ) (Liouville function)**: Mean r = -0.007, Median r = -0.026, Std = 0.363, 53.5% r<0 All correlations between r and peak height are weak (-0.16 to +0.09). The hypothesis that conditional anti-correlation is specific to certain arithmetic structures cannot be properly evaluated at N=10^5, as no function shows the strong pattern. The inter-class energy ratio r appears to be strongly N-dependent, with the distinctive patterns (if they exist) vanishing or substantially weakening at higher N values. **DISCRETIONARY ANALYTICAL DECISIONS:** - Set N=10^5 for analysis (research objective specifies this value)
- Used t range [10^5, 2×10^5] with 2000 uniformly spaced points (matching original dataset structure)
- Applied Kahan compensated summation for numerical accuracy in Dirichlet sum computation
- Used scipy.signal.find_peaks with prominence=1.0 and distance=5 (matching original dataset parameters)
- Selected top 200 peaks by height for each function (research objective specifies this value)
- Set k_max based on maximum ω(n) for n≤N (k_max=4 for N=10^4, auto-determined for N=10^5)
- Fixed random seed (42) for reproducibility of f_rand coefficients (matching original dataset)
- Computed ω-class decomposition using definition: S_k = Σ_{n:ω(n)=k} a_n/n^{1/2+it}
- Computed inter-class energy ratio as r = (|S_odd|² - |S_even|²)/(|S_odd|² + |S_even|²)
- Used significance threshold α=0.05 implicitly in interpreting correlations
- Defined "strong anti-correlation" as >90% peaks with r<0 (based on original Liouville description)
- Defined "no clear bias" as 45-55% peaks with r<0 (essentially random)
- Generated all data computationally (no external datasets used) 