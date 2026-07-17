## Overview <output>
<conclusion>
Using the achievable five-control dataset generated within the runtime budget (common N=800 rather than the target N=5000 for all controls), Front I supports a shared degree-2 log-polynomial growth law for Jacobi coefficients a_n and b_n across ζ, L(χ₄ mod 5), L(Δ,s), and also L_DH, while L_DH is the only control showing a statistically significant deviation in spectral-measure spacing statistics, and standard height-based Front I is blind to the supplied ζ_δ perturbation.
</conclusion>
<methods>
I first audited the workspace and validated the binding specification in -PROMPT-v6-DATASET.md. I loaded the provided cached zero lists zeta_zeros_N5000_dps50.npy and zeta_delta_zeros_N5000_dps50.npy, confirmed their shapes/dtypes, and passed the R2 zeta gate by reproducing the first three nontrivial zeta zeros and checking |Z(γ)| with mpmath.siegelz. Because the three other required N=5000 control zero lists were not present on disk, I could not complete the exact requested N=5000 five-control analysis from existing data. To avoid fabrication, I generated the missing controls de novo within the 3600 s runtime budget. For L(Δ,s) (Ramanujan Δ, LMFDB 1.12.a.a), I installed/imported cypari2 and used PARI/GP lfunmf + lfunzeros to compute zeros up to height T=1000, yielding 1298 zeros, which I saved as delta_zeros_N1298_dps50.npy. For L(χ₄ mod 5), I used PARI/GP znstar(5,1), znconreychar(G,2), lfuncreate, lfuninit, and lfunzeros up to T=1000, yielding 902 zeros, saved as chi5_zeros_N902_dps50.npy. For the Davenport-Heilbronn control L_DH, I implemented the Hurwitz-zeta linear combination with coefficients determined by ξ=(sqrt(10-2sqrt(5))-2)/(sqrt(5)-1), verified the known off-line R2 test points (three below 10^-6 and the documented transcription-artifact point at ~4.03×10^-5), then defined a Hardy-style real-valued critical-line function Z_DH(t)=Re[e^{iθ(t)}L_DH(1/2+it)] with θ(t)=arg(Gamma((s+1)/2)(π/5)^(-it/2)). I scanned t∈[2,1000] on a 0.25 grid at dps=30, found 845 sign-change brackets, and refined them at dps=50 with mpmath.findroot, saving the resulting list as ldh_zeros_N845_dps50.npy. Because the limiting control had 845 zeros, I set a common comparison size N=800 across all five controls for the direct comparative Front I analysis. I reconstructed Jacobi coefficients from each discrete spectral measure using a normalized Lanczos/Stieltjes procedure on the zero-height spectrum γ_n with two admissible spectral weights: uniform and Gaussian. To avoid numerical overflow, I used normalized orthogonal-polynomial iterations with explicit reorthogonalization under the discrete weighted inner product. Per the specification’s stability guidance, I analyzed only the first cN coefficients with c=0.1, i.e. n=1,…,80. For model selection, I fit each a_n and b_n sequence on the stable window against five candidate laws: constant, linear in n, A log(n)+B, quadratic log-polynomial A log(n)+B log(n)^2+C, and power law A n^α (fit in log-log form but scored on the original scale). I computed Gaussian least-squares AIC and BIC, plus R^2. I repeated this for all controls and both spectral weights. For spectral-measure comparison, I computed smooth empirical unfolding maps N(γ) by least-squares fitting cumulative index against the basis {γ log γ, γ, log γ, 1}, formed unfolded nearest-neighbor spacings, and compared controls using two-sample KS statistics, p-values, and Wasserstein distances. I saved the analysis outputs to front1_model_selection.csv, front1_logpoly2_params.csv, and front1_ks_matrix.csv, and created the final summary figure front1_summary.png.
</methods>
<results>
Data availability and validation:
- Provided cached data: ζ N=5000 dps=50 and ζ_δ N=5000 dps=50.
- Generated within-budget controls: L(Δ,s) N=1298, L(χ₄ mod 5) N=902, L_DH N=845.
- Common comparison set: first N=800 zeros from each control.
- R2 zeta gate passed: γ1=14.134725141734..., γ2=21.022039638771..., γ3=25.010857580145..., with |Z(γ)|≈2.00×10^-49, 2.45×10^-49, and 2.37×10^-50.
- R2 L_DH validation points produced |L_DH(ρ)|≈6.51×10^-7, 4.03×10^-5, 6.82×10^-7, 4.71×10^-7; the second value matches the known transcription-artifact exception documented in the dataset description. Model-selection results on the stable Jacobi window n≤80:
- For every control (ζ, ζ_δ, L(χ₄ mod 5), L(Δ,s), L_DH), for both coefficient families (a_n and b_n), and for both spectral weights (uniform and Gaussian), the BIC-winning model was the quadratic log-polynomial A log(n)+B log(n)^2+C.
- Uniform-weight ΔBIC (winner over runner-up): - ζ: a_n 94.99, b_n 12.21 - ζ_δ: a_n 94.99, b_n 12.21 - L(χ₄ mod 5): a_n 86.28, b_n 29.06 - L(Δ,s): a_n 103.04, b_n 0.34 - L_DH: a_n 56.49, b_n 22.59
- Thus the fitted growth law was not unique to the GRH-satisfying controls; L_DH also selected the same family. Representative uniform-weight fitted log-polynomial parameters (A_log, B_log2, C, R^2):
- ζ a_n: (-30.8056, 5.5585, 639.4882), R^2=0.7322
- ζ b_n: (-8.8197, 0.8727, 310.1472), R^2=0.7787
- L(χ₄ mod 5) a_n: (-18.0007, 3.1863, 478.3598), R^2=0.6952
- L(χ₄ mod 5) b_n: (-8.9021, 1.1154, 240.3604), R^2=0.7231
- L(Δ,s) a_n: (-20.6522, 3.7988, 371.2038), R^2=0.7704
- L(Δ,s) b_n: (-3.8731, 0.2491, 176.4091), R^2=0.8202
- L_DH a_n: (-17.8159, 3.1263, 503.7835), R^2=0.5576
- L_DH b_n: (-9.7107, 1.2145, 254.8676), R^2=0.6709
These show quantitative parameter shifts and lower fit quality for L_DH, but not a qualitatively different best model family. Spectral-measure / spacing results:
- Mean and SD of unfolded nearest-neighbor spacings: - ζ: mean 0.9999, SD 0.3777 - ζ_δ: mean 0.9999, SD 0.3777 - L(χ₄ mod 5): mean 0.9979, SD 0.3593 - L(Δ,s): mean 1.0001, SD 0.3475 - L_DH: mean 0.9943, SD 0.4403
- Pairwise KS statistics on unfolded spacings: - ζ vs ζ_δ: 0.0000, p=1.000 - ζ vs L(χ₄ mod 5): 0.0338, p=0.752 - ζ vs L(Δ,s): 0.0501, p=0.269 - ζ vs L_DH: 0.0851, p=6.11×10^-3
- Pairwise Wasserstein distances from ζ: - to ζ_δ: 0.0000 - to L(χ₄ mod 5): 0.0230 - to L(Δ,s): 0.0345 - to L_DH: 0.0751
This identifies L_DH as the only statistically significant outlier in spectral spacing among the five controls at the analyzed N. ζ_δ sensitivity:
- Standard Front I based only on zero heights γ_n cannot distinguish ζ from the supplied ζ_δ artifact, because zeta_delta_zeros_N5000_dps50.npy keeps the imaginary parts identical to ζ and changes only Re(s) for indices 1000–1019.
- Therefore, at common N=800, ζ and ζ_δ are exactly identical under the standard height-spectrum Jacobi pipeline.
- An auxiliary off-line-aware weighted reconstruction using the real parts can produce large differences at higher Jacobi indices (e.g. max |Δa|≈199.0 and max |Δb|≈98.8 by N=1200), but those changes occur outside the cN stable window at that reduced N and therefore cannot be interpreted as robust Front I evidence here.
</results>
<challenges>
I cannot perform the exact requested full Front I analysis on five complete N=5000 zero lists because only the ζ and ζ_δ N=5000 lists were present in the workspace, while the L_DH, L(χ₄ mod 5), and L(Δ,s) N=5000 lists were absent and de novo generation to N=5000 is computationally too expensive for the 3600 s runtime budget. This was the primary limitation. Additional technical issues:
- cypari2 was not initially installed and had to be installed during the session.
- The first Lanczos implementation overflowed numerically because orthogonal polynomials on raw zero heights grow rapidly; I corrected this by editing the same analysis cell to use normalized recurrences with reorthogonalization.
- The supplied ζ_δ perturbation changes only the real parts, not the imaginary parts, so any standard Front I implementation based solely on the height spectrum is necessarily blind to that deformation; this is a methodological limitation of the observable, not a data-processing bug.
- The L_DH R2 validation set contains one documented transcription-artifact coordinate giving |L_DH|≈4×10^-5 instead of <10^-6; this matched the dataset description and therefore did not invalidate the implementation.
- Because the missing controls were generated only up to T≈1000, direct five-way comparison had to be restricted to N=800, reducing the stable Front I window to n≤80 rather than the target n≤500 for N=5000.
</challenges>
<discussion>
The main comparative Front I result is that the degree-2 log-polynomial phenomenology of Jacobi coefficients is not specific to the GRH-satisfying controls in the analyzed data. ζ, L(χ₄ mod 5), L(Δ,s), and L_DH all selected the same BIC-best growth family for both a_n and b_n under both tested spectral weights. This directly weakens the research hypothesis in its strongest form: the non-GRH control L_DH did not break the coefficient-law class. However, L_DH was not identical to the genuine L-functions. Its fitted Jacobi sequences had noticeably lower R^2, indicating more irregular residual structure, and its unfolded spacing distribution differed significantly from ζ (KS p=0.006), whereas L(χ₄ mod 5) and L(Δ,s) did not. So the data support a narrower conclusion: Front I coefficient-law class appears descriptive and broadly shared, while spectral-measure statistics still distinguish the non-Euler-product control. The ζ_δ result is scientifically important despite being negative. In the supplied artifact, the perturbation changes only Re(ρ) and not Im(ρ), so a Front I pipeline built on the real height spectrum γ_n is blind by construction. Under the project’s Step 0.5 logic, this means standard height-based Front I should be labeled blind to this deformation family unless the observable is reformulated to encode off-line displacement. Thus a null ζ vs ζ_δ comparison here is uninformative about RH sensitivity. Overall, this analysis supports the specification’s caution that Front I may be descriptive rather than discriminating. The strongest empirical separation in the current dataset comes from spacing-based spectral measures, not from a different best-fit asymptotic class for a_n and b_n. Because the full N=5000 five-control panel was unavailable, these findings should be treated as an honestly bounded intermediate result rather than the final project-level verdict.
</discussion>
<proposed-next-hypotheses>
1. At full matched N=5000, the Jacobi coefficients a_n and b_n for ζ, L(χ₄ mod 5), L(Δ,s), and L_DH will still share the same BIC-best log-polynomial model family, but L_DH will show significantly larger residual variance and poorer cross-weight stability than the genuine L-functions.
2. A Front I observable that explicitly incorporates off-line displacement (for example, a complex-spectrum or bivariate spectral reconstruction rather than using only imaginary parts) will detect the ζ_δ deformation monotonically with δ, whereas the standard height-only Jacobi reconstruction will remain blind.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>delta_zeros_N1298_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array of 1298 Ramanujan Δ L-function zero heights up to T=1000 generated with cypari2/PARI lfunmf and lfunzeros at 50-digit working precision. Saved as fixed-width Unicode strings for precision-preserving storage.</artifact-description>
</artifact>
<artifact>
<file-name>chi5_zeros_N902_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array of 902 zero heights for the Dirichlet L-function attached to the order-4 character mod 5, generated with cypari2/PARI using znconreychar, lfuncreate, lfuninit, and lfunzeros up to T=1000. Stored as fixed-width Unicode strings.</artifact-description>
</artifact>
<artifact>
<artifact>
<file-name>ldh_zeros_N845_dps50.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy array of 845 Davenport-Heilbronn critical-line zero heights up to T=1000. Generated by scanning a Hardy-style real-valued Z_DH(t) for sign changes and refining roots with mpmath.findroot at 50-digit precision after validating the L_DH implementation against the canonical off-line test points.</artifact-description>
</artifact>
<artifact>
<file-name>front1_model_selection.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Tabular model-selection report for Front I Jacobi coefficients across all analyzed controls, weights, coefficient types, and candidate models. Includes AIC, BIC, R^2, and indicators for the best AIC/BIC model.</artifact-description>
</artifact>
<artifact>
<file-name>front1_logpoly2_params.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Table of fitted quadratic log-polynomial parameters for a_n and b_n for each control and spectral weight, together with R^2 values. Created from the stable-window Front I fits.</artifact-description>
</artifact>
<artifact>
<file-name>front1_ks_matrix.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Pairwise KS-statistic matrix comparing unfolded nearest-neighbor spacing distributions across the five controls in the common N=800 analysis. Derived from smooth empirical unfolding and scipy.stats.ks_2samp.</artifact-description>
</artifact>
</artifacts>
</output>
