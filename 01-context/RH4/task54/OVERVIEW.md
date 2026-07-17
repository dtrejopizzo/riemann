## Overview <output>
<conclusion>
In this controlled Davenport–Heilbronn family, the difference-matrix statistics did not show a statistically significant monotonic relationship with the off-line zero location β, and the leading eigenvalue λ_1(Δ) did not increase with β as hypothesized.
</conclusion>
<methods>
I first defined the Davenport–Heilbronn family as L(s;κ)=((1−iκ)/2)L(s,χ)+((1+iκ)/2)L(s,χ̄), where χ is the order-4 Dirichlet character modulo 5. Using mpmath (v1.3.0) with the Hurwitz-zeta representation L(s,χ)=5^(−s)∑_{a=1}^4 χ(a)ζ(s,a/5), I tracked the known off-line zero near 0.8085+85.6993i at κ≈0.28408 and numerically inverted the β(κ) relationship to select 7 family members with target β values 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, and 0.85. The resulting κ values were approximately −1.09418, −0.48935, −0.18471, 0.01073, 0.15292, 0.26654, and 0.36447, respectively. For the coefficient generation at N=10^6, I used the exact identity a_n(κ)=Re(χ(n))+κ·Im(χ(n)), so coefficients were generated from scratch without simulation and depend only on n mod 5. I sieved Ω(n) (number of prime factors with multiplicity) up to 10^6, then grouped integers into ω-strata k=0,…,7 to match the available 8×8 baseline matrix format. I precomputed log n and n^(−1/2), then evaluated the stratum-resolved sums S_k(t)=∑_{Ω(n)=k} a_n n^(−1/2−it) over the full interval t∈[10^4,2×10^4] on a grid with spacing 0.05 using Numba-accelerated kernels. Exploiting linearity, I decomposed S_k(t;κ)=A_k(t)+κB_k(t), where A_k uses Re(χ) and B_k uses Im(χ), allowing one expensive coarse-grid pass for all κ values. These coarse-grid arrays were saved in A_B_grid_DH_N1e6.npz. For each κ, I formed D(t)=∑_{k=0}^7 S_k(t), identified local maxima of |D(1/2+it)| on the coarse grid, selected the 200 largest peaks, and refined each peak by iterative batch re-evaluation in narrow windows around the coarse maxima. At the refined peaks, I computed the 8-dimensional complex vectors S_k(t_peak). I then formed M_jk(β)=mean_p Re(S_j(t_p)·conj(S_k(t_p))) over the 200 peaks. The baseline F1 matrix was loaded from M.npy in the workspace, and I computed Δ(β)=M(β)−M(F1). For each Δ matrix, I computed the Frobenius norm, trace, largest eigenvalue λ_1(Δ) (largest algebraic eigenvalue of the symmetrized matrix), smallest eigenvalue, and a trace-normalized variant Δ_norm=M(β)/tr(M(β))−M(F1)/tr(M(F1)). I then evaluated Pearson correlation coefficients and two-sided p-values, and Spearman rank correlations with p-values, between β and each candidate statistic. Because multiple statistics were examined, I interpreted isolated marginal p-values cautiously and did not claim significance without consistent evidence. The final result figure was saved as DH_family_discriminator.png, and the full numerical results were saved as DH_family_results.npz.
</methods>
<results>
The selected DH family members and their recovered first off-line zeros were:
β=0.55 (κ=−1.09418, t≈85.5755), β=0.60 (κ=−0.48935, t≈85.5915), β=0.65 (κ=−0.18471, t≈85.6155), β=0.70 (κ=0.01073, t≈85.6434), β=0.75 (κ=0.15292, t≈85.6709), β=0.80 (κ=0.26654, t≈85.6955), and β=0.85 (κ=0.36447, t≈85.7167). Using the 200 largest peaks in t∈[10^4,2×10^4], the unnormalized Δ statistics were:
- β=0.55: ||Δ||_F=26.3009, tr(Δ)=−0.0902, λ_1(Δ)=12.7281, λ_min(Δ)=−21.4370
- β=0.60: ||Δ||_F=29.5977, tr(Δ)=−19.9248, λ_1(Δ)=7.6078, λ_min(Δ)=−28.3166
- β=0.65: ||Δ||_F=30.8683, tr(Δ)=−24.6291, λ_1(Δ)=6.4990, λ_min(Δ)=−29.9803
- β=0.70: ||Δ||_F=31.1123, tr(Δ)=−25.4047, λ_1(Δ)=6.3253, λ_min(Δ)=−30.2740
- β=0.75: ||Δ||_F=30.8974, tr(Δ)=−25.1575, λ_1(Δ)=6.2601, λ_min(Δ)=−30.0621
- β=0.80: ||Δ||_F=30.5439, tr(Δ)=−24.3849, λ_1(Δ)=6.3464, λ_min(Δ)=−29.6691
- β=0.85: ||Δ||_F=30.1249, tr(Δ)=−23.2497, λ_1(Δ)=6.5542, λ_min(Δ)=−29.1729 These values were not monotonic in β. In particular, λ_1(Δ) decreased sharply from 12.73 at β=0.55 to about 6.3–6.6 for β≥0.65, contradicting the hypothesized increase with β. Correlation results versus β were:
- λ_1(Δ): Pearson r=−0.6951, p=0.0830; Spearman ρ=−0.5357, p=0.2152
- ||Δ||_F: Pearson r=0.6155, p=0.1412; Spearman ρ=0.3929, p=0.3833
- tr(Δ): Pearson r=−0.6655, p=0.1027; Spearman ρ=−0.3929, p=0.3833
- λ_min(Δ): Pearson r=−0.6370, p=0.1239; Spearman ρ=−0.3929, p=0.3833 For trace-normalized matrices, the normalized leading eigenvalue also remained non-monotonic:
- β=0.55: λ_1(Δ_norm)=0.29611
- β=0.60: 0.36274
- β=0.65: 0.41746
- β=0.70: 0.42987
- β=0.75: 0.41828
- β=0.80: 0.40162
- β=0.85: 0.38418
with Pearson r=0.5722, p=0.1794 and Spearman ρ=0.3929, p=0.3833 versus β. A notable secondary result was that several statistics were strongly monotonic in |κ| rather than β:
- λ_1(Δ) vs |κ|: Pearson r=0.9515, p=0.0010; Spearman ρ=0.9286, p=0.0025
- ||Δ||_F vs |κ|: Pearson r=−0.9879, p<1e-4; Spearman ρ=−1.0000, p<1e-4
- λ_1(Δ_norm) vs |κ|: Pearson r=−0.9936, p<1e-4; Spearman ρ=−1.0000, p<1e-4 Thus, within this family, the Δ-based discriminator tracked the construction parameter magnitude much more strongly than the off-line zero’s real part.
</results>
<challenges>
The primary challenge was that the requested analysis required generating all coefficients and peak-conditioned spectral data from scratch rather than reading a ready-made feature table. Direct evaluation of Dirichlet polynomials over a dense t-grid at N=10^6 is computationally expensive, so I exploited the DH family structure a_n(κ)=Re(χ(n))+κIm(χ(n)) to compute reusable A_k and B_k components once and then combine them for all κ values. Even with this optimization, the coarse t-grid evaluation over [10^4,2×10^4] required a large Numba computation, and the peak refinements for all seven family members remained expensive. A second challenge is inferential: only 7 β values were sampled, so correlation tests have limited power and wide uncertainty. The p-values should therefore be interpreted cautiously. Also, I matched the existing 8×8 baseline by using ω-strata k=0,…,7 only; terms with Ω(n)≥8 were excluded from M_jk. This preserves comparability to the baseline matrix provided in the workspace, but it is still a modeling choice that could affect the absolute scale of statistics. Another important limitation is conceptual: peak-conditioned matrices M_jk depend both on the coefficients and on the peak set, and the peak set itself changes with κ. Therefore, M_jk(β) is not a simple function of β alone. This makes monotonicity biologically or mathematically nontrivial and likely explains why naive inverse-bridge expectations can fail even within one construction family.
</challenges>
<discussion>
The hypothesis is not supported by the computed data. The leading eigenvalue λ_1(Δ) does not increase monotonically as the off-line zero moves away from the critical line; instead, it drops from the β=0.55 case and then flattens, while normalized variants peak near β≈0.70 and decline on either side. Statistically, none of the tested β-correlations reached conventional significance, and the rank-based evidence for monotonicity was weak. The more informative result is that Δ-based spectral statistics appear to be much more sensitive to the underlying construction parameter κ than to the zero location β itself. This is scientifically important because it suggests that even within a fixed violator family, the peak-conditioned cross-structure may encode aspects of how the function is built, not just where its first off-line zero lies. That observation aligns with the broader programmatic warning from prior analyses: peak conditioning introduces structure that is not captured by unconditional bulk coefficient summaries, and family-specific mechanisms can dominate cross-family generalization. In practical terms, this means the hoped-for “inverse bridge” from Δ_jk to β is not established here. A positive monotone bridge may still exist after a different normalization, a different baseline, or a different statistic that suppresses κ-amplitude effects, but the present experiment indicates that λ_1(Δ) itself is not a robust proxy for β in this DH family. The data instead support the more cautious interpretation that Δ_jk captures a mixture of violation geometry and construction amplitude, with the latter dominating in this parameterization.
</discussion>
<proposed-next-hypotheses>
1. After removing κ-amplitude effects by regressing or orthogonalizing Δ_jk statistics against |κ|, the residualized leading eigenvalue or another spectral component will show a stronger monotonic relationship with β.
2. A subspace-based statistic derived from the full eigenvalue spectrum or eigenvector alignment of Δ_jk, rather than the single largest eigenvalue, will correlate more strongly with the off-line zero location β within the Davenport–Heilbronn family.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>selected_kappas.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON file containing the targeted β values, corresponding numerically recovered κ parameters, and the tracked first off-line zero locations used to define the Davenport–Heilbronn family members.</artifact-description>
</artifact>
<artifact>
<file-name>A_B_grid_DH_N1e6.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing the reusable coarse-grid decomposition S_k(t;κ)=A_k(t)+κB_k(t) for ω-strata k=0..7 on t∈[10^4,2×10^4] at N=10^6. This was generated with Numba-accelerated evaluation of Dirichlet polynomials from scratch.</artifact-description>
</artifact>
<artifact>
<file-name>DH_family_results.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive containing the final family-level results: β values, κ values, Δ statistics, baseline matrix, family-specific M matrices, refined peak locations, and complex S_k values at peaks. It was created from the full peak-conditioned analysis of the seven Davenport–Heilbronn family members.</artifact-description>
</artifact>
</artifacts>
</output>
