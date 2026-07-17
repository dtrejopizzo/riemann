## Overview <output>
<conclusion>
For L(χ₄ mod 5), λ_min(Q(T0,σ,J)) converges uniformly in T0 to 0 for σ=2, while the apparent failure of convergence for σ≤1 is explained by systematic truncation error from the fixed prime cutoff X=10^5.
</conclusion>
<methods>
I analyzed the authoritative specification file engine-spec.md and loaded the two cached zero lists Lchi_zeros.pkl and Lchi_zeros_neg.pkl (130 positive- and 130 negative-imaginary zeros, respectively). I implemented the localized Weil explicit-formula quadratic form Q=M_zeros−M_arith for the primitive odd Dirichlet character χ mod 5 with χ(1)=1, χ(2)=i, χ(3)=−i, χ(4)=−1, conductor q=5, and parity a=1. The Hermite-Gauss basis was defined as φ_n(t)=((σ√π 2^n n!)^(−1/2)) H_n((t−T0)/σ) exp(−(t−T0)^2/(2σ^2)), and M_zeros was computed directly as Σ_γ φ_m(γ)φ_n(γ) over all cached zeros from both lists. For M_arith, I used the Weil explicit formula for primitive nontrivial Dirichlet L-functions. The archimedean term used the kernel R(t)=log(5/π)+Re ψ(3/4+it/2), integrated against φ_m(t)φ_n(t) via Gauss-Hermite quadrature (typically 80 nodes, increased with J). The prime-power term summed over all prime powers p^k≤10^5 (9,700 terms total), weighted by Λ(p^k)/√(p^k)=log(p)/√(p^k). I used the analytic Fourier transform of the Hermite-Gauss product basis, not numerical quadrature, for stability and speed. For ξ real and p=min(m,n), q=|m−n|, I used F_mn(ξ)=2^(q/2)·(p!/sqrt(m!n!))·(−iξ/2)^q·L_p^q(ξ^2/2)·exp(−ξ^2/4), verified numerically against mpmath quadrature before running the full grid. I computed Q(T0,σ,J) on the full requested grid: T0∈{30,46.13,60,85.7,120}, σ∈{0.5,1,2}, J∈{4,8,12,16,20,24,28}. For each grid point I cached Q, M_zeros, and M_arith to disk as .npz files in Q_cache/ and recorded λ_min, λ_max, the full eigenvalue list, tr(M_zeros), tr(M_arith), and the trace residual in results.json and lam_min_results.csv. I validated the implementation using the trace identity tr(M_zeros)=tr(M_arith), obtaining |Δtr|=3.55×10^−15 at T0=46.13, σ=2, J=10, which is consistent with the expected validated-control regime. For σ=2 only, I fit λ_min(J) separately for each T0 to both a+b·exp(−cJ) and a+b·J^(−c) using scipy.optimize.curve_fit, and recorded fitted parameters, RSS, R^2, and AIC in fits_sigma2.json. I then computed the uniformity statistic sup_T0 |λ_min(T0,2,J)−λ_∞(T0,2)| using the fitted asymptotic limits λ_∞. I generated a final summary figure with two vertically stacked panels: (A) λ_min versus J across all T0 and σ, and (B) the uniformity statistic for σ=2 with σ=1 and σ=0.5 shown for reference.
</methods>
<results>
The trace gate passed in the validated σ=2 regime. At T0=46.13, σ=2, J=10, tr(M_zeros)=5.729148741395164, tr(M_arith)=5.729148741395168, giving residual Δtr=−3.55×10^−15. Across the entire σ=2 grid, |Δtr| ranged from 0 to 2.23×10^−12. By contrast, for σ=1, |Δtr| ranged from 2.91×10^−12 to 7.75×10^−2, and for σ=0.5 it ranged from 2.83×10^−3 to 2.11×10^−1. For σ=2, λ_min remained at numerical floor for all T0 and J. Representative values were:
- T0=30: λ_min from −1.27×10^−15 (J=4) to −1.35×10^−14 (J=28)
- T0=46.13: −2.42×10^−15 to −1.93×10^−14
- T0=60: −2.63×10^−15 to −2.32×10^−14
- T0=85.7: −4.05×10^−15 to −2.52×10^−14
- T0=120: −6.47×10^−15 to −2.32×10^−12
Thus even the largest |λ_min| at σ=2 was only 2.32×10^−12, which is negligible relative to tr(M_zeros)=O(1–10). For σ=1, λ_min became substantially negative as J increased. At J=28, λ_min was:
- T0=30: −4.79×10^−1
- T0=46.13: −5.51×10^−1
- T0=60: −2.92×10^−1
- T0=85.7: −5.25×10^−1
- T0=120: −4.17×10^−1
At J=4, the same σ=1 values were only ~10^−11 in magnitude, showing strong J-dependent deterioration. For σ=0.5, the breakdown was stronger. λ_min was already negative at J=4, ranging from −8.39×10^−3 to −5.03×10^−2 depending on T0, and by J=28 it ranged from −1.77 to −1.97:
- T0=30: −1.77
- T0=46.13: −1.84
- T0=60: −1.87
- T0=85.7: −1.83
- T0=120: −1.97
These large negative values coincided with large trace residuals, indicating systematic rather than physical effects. For the σ=2 convergence fits, the estimated asymptotic limits λ_∞ were all numerically consistent with 0. Exponential fits outperformed power-law fits by AIC at every T0. The exponential-fit limits a were:
- T0=30: a=−5.84×10^−11, R^2=0.964, AIC=−481.0
- T0=46.13: a=−7.29×10^−11, R^2=0.952, AIC=−475.0
- T0=60: a=−3.66×10^−11, R^2=0.974, AIC=−475.5
- T0=85.7: a=−4.56×10^−14, R^2=0.983, AIC=−479.6
- T0=120: a=−8.59×10^−9, R^2=0.498, AIC=−389.1
These fitted limits are dominated by machine noise and are not meaningfully different from 0. The σ=2 uniformity statistic sup_T0 |λ_min(T0,2,J)−λ_∞(T0,2)| remained at machine-floor scale across all J:
- J=4: 6.47×10^−15
- J=8: 2.50×10^−14
- J=12: 5.44×10^−14
- J=16: 6.26×10^−14
- J=20: 1.21×10^−13
- J=24: 3.88×10^−13
- J=28: 2.32×10^−12
This mild increase with J is consistent with numerical roundoff accumulation, not loss of convergence.
</results>
<challenges>
A major methodological challenge was implementing the correct non-self-dual Dirichlet-L explicit formula with consistent Fourier-transform normalization and signs. I resolved this by validating against the trace identity tr(M_zeros)=tr(M_arith), which provided a stringent internal correctness check. Another challenge was ensuring numerical stability of the prime-power term; I avoided unstable direct quadrature by using the closed-form Laguerre-polynomial expression for the Hermite-Gauss Fourier transform and verified the formula numerically after discovering and correcting a missing exp(−ξ^2/4) factor. The fixed prime cutoff X=10^5 is a known limitation from the specification, and it clearly affected the σ≤1 calculations. Because the research objective explicitly required X=10^5, I did not alter it; instead, I quantified its consequences through trace residuals and λ_min behavior. The σ=2 fit models should also be interpreted cautiously: because the data are already at machine precision, the fitted asymptotic limits and rate parameters are noise-sensitive and not physically meaningful beyond establishing consistency with λ_∞=0.
</challenges>
<discussion>
The results strongly support the hypothesis. In the validated wide-window regime σ=2, the quadratic form for L(χ₄ mod 5) behaves exactly as expected for a GRH-satisfying control: Q is numerically indistinguishable from 0 across the entire T0-J grid, the trace identity closes at machine precision, and λ_min remains at numerical floor. The apparent convergence is uniform in T0 because the supremum deviation remains ~10^−15 to 10^−12 across J=4–28, which is negligible relative to the natural matrix scale. In contrast, the σ=1 and σ=0.5 regimes show substantial negative λ_min values accompanied by large trace mismatches. Because the same implementation is trace-validated at σ=2, these negative values should not be interpreted as genuine violations of GRH or genuine spectral signal. Instead, they are consistent with the specification’s prior finding that X=10^5 is too small for narrow localization windows, where the arithmetic-side truncation error dominates. This reproduces for L(χ₄ mod 5) the same pattern previously observed for the Riemann zeta control, suggesting that the phenomenon is structural to the fixed-cutoff engine rather than peculiar to one L-function. Scientifically, this means the localized Weil detector is stable under basis completion for this non-self-dual GRH control when the arithmetic side is computed accurately enough for the chosen localization width. The instability at small σ is therefore best understood as a controllable numerical artifact, reinforcing the need for a dynamic prime cutoff X that scales with localization width for rigorous narrow-window studies.
</discussion>
<proposed-next-hypotheses>
1. If the prime cutoff is increased dynamically according to X≈exp(c/σ^2), then for L(χ₄ mod 5) the σ=1 and σ=0.5 λ_min(J) curves will also converge to 0 uniformly in T0, with trace residuals returning to machine-floor scale.
2. For other validated GRH controls with correctly refined zeros and accurate gamma factors, the basis-completion limit λ_min(Q(T0,σ,J)) will likewise be 0 in the trace-validated regime, independent of self-duality, provided the arithmetic cutoff is matched to σ.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON record of all 105 grid computations, including T0, sigma, J, lambda_min, lambda_max, traces, trace residuals, and full eigenvalue lists. Created from the explicit-formula matrix computations performed in Python with numpy, scipy, and mpmath.</artifact-description>
</artifact>
<artifact>
<file-name>lam_min_results.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Tabular summary of the full grid of λ_min and trace statistics for L(χ₄ mod 5). Written from the aggregated pandas DataFrame used for downstream summaries and plotting.</artifact-description>
</artifact>
<artifact>
<file-name>fits_sigma2.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Fit results for the σ=2 convergence analysis, including exponential and power-law model parameters, RSS, R^2, and AIC for each T0. Generated using scipy.optimize.curve_fit on the computed λ_min(J) values.</artifact-description>
</artifact>
<artifact>
<file-name>Q_cache</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Directory containing 105 cached .npz files with Q, M_zeros, and M_arith matrices for every requested (T0, sigma, J) combination. Saved to avoid recomputation and preserve the full numerical outputs of the study.</artifact-description>
</artifact>
<artifact>
<file-name>REPORT.md</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Short written report summarizing the implementation, trace validation, σ=2 convergence, σ≤1 failure regime, and overall conclusion. Produced directly from the numerical results after completion of the grid search.</artifact-description>
</artifact>
</artifacts>
</output>
