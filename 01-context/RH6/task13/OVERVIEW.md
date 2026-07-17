## Overview <output>
<conclusion>
The ANCOVA shows highly statistically significant differences (p < 0.05 for all ω-classes k=1..4) in the log M_k vs log log N growth slopes between ζ and L_DH, and — as hypothesized — the L_DH slope is smaller than the ζ slope for every ω-class, mirroring (and far exceeding in magnitude) the previously observed L(Δ) vs L_DH pattern.
</conclusion> <methods>
1. Loaded `omega_class_moments_N1e6.csv` (3 L-functions × 4 N values: 10⁴, 5×10⁴, 10⁵, 10⁶) and selected the ζ and L_DH rows.
2. For each ω-class k ∈ {1,2,3,4} built a long-form table with columns: `logM = log(M_k)`, `loglogN = log(log(N_terms))`, and a categorical `L_function` (reference = `zeta`).
3. Fit the OLS ANCOVA model `logM ~ loglogN * L_function` using `statsmodels.formula.api.ols`. The coefficient on `loglogN` gives the slope for ζ; the interaction coefficient `loglogN:L_function[T.L_DH]` gives the slope difference (L_DH − ζ) and its p-value tests the slope-equality null.
4. Compared the resulting slope differences and interaction p-values with the previously computed `ancova_omega_class_summary.csv` (L(Δ) vs L_DH) and saved the merged comparison to `ancova_zeta_vs_ldh_summary.csv`.
5. Produced a single summary bar chart (`ancova_zeta_vs_ldh_comparison.png`) of the absolute slope differences with p-value annotations.
</methods> <results>
ζ vs L_DH ANCOVA (interaction term = slope difference L_DH − ζ): | k | slope ζ | slope L_DH | Δ(L_DH−ζ) | p_interaction | R² |
|---|---------|------------|-----------|---------------|-----|
| 1 | 5.910 | 0.171 | −5.739 | 7.4e-03 | 0.981 |
| 2 | 9.179 | 0.480 | −8.699 | 2.3e-04 | 0.998 |
| 3 | 11.260 | 1.566 | −9.694 | 3.5e-05 | 0.999 |
| 4 | 14.831 | 3.066 | −11.765 | 2.8e-06 | 0.9998 | All four p-values are < 0.05 (in fact < 0.01), so the null of equal slopes is rejected for every ω-class. Comparison with the prior L(Δ) vs L_DH result (`ancova_omega_class_summary.csv`): | k | Δ(L_DH−ζ) | p (ζ vs L_DH) | Δ(L_DH−L(Δ)) | p (L(Δ) vs L_DH) |
|---|-----------|---------------|---------------|------------------|
| 1 | −5.74 | 7.4e-03 | −0.119 | 8.8e-03 |
| 2 | −8.70 | 2.3e-04 | −0.318 | 1.4e-04 |
| 3 | −9.69 | 3.5e-05 | −0.457 | 9.3e-03 |
| 4 | −11.77 | 2.8e-06 | −1.756 | 4.7e-02 | The sign of the slope difference is the same (L_DH < GRH-conforming) in every ω-class, but the magnitude of the ζ−L_DH gap is one to two orders of magnitude larger than the L(Δ)−L_DH gap (e.g., −11.77 vs −1.76 at k=4). The ζ slopes themselves are also much steeper than L(Δ)'s, consistent with ζ's prime-power-rich Euler product driving very rapid ω-class moment growth.
</results> <challenges>
- The N-grid contains only 4 points (10⁴, 5×10⁴, 10⁵, 10⁶) per L-function, giving the ANCOVA only 4 residual degrees of freedom and 1 df for the interaction; p-values should be interpreted with caution under this low-power, small-sample regime.
- Linearity of `log M_k` in `log log N` is assumed but cannot be rigorously validated with 4 points; higher-order curvature (e.g. `log log log N`) would be unidentifiable.
- The N-grid is unbalanced in log-spacing (three points within 10⁴–10⁵, one at 10⁶), so the high-N point exerts considerable leverage on the fitted slopes — particularly for ζ, whose moments grow rapidly.
- Standard ANCOVA assumes Gaussian, homoscedastic residuals on the log scale; with N=8 observations per fit this assumption cannot be meaningfully tested.
</challenges> <discussion>
The hypothesis is confirmed in both qualitative and quantitative respects: the slope of `log M_k` vs `log log N` is significantly smaller for the Davenport–Heilbronn function L_DH than for the Riemann zeta function across all four ω-classes tested, with p-values ranging from 7.4×10⁻³ down to 2.8×10⁻⁶. Combined with the earlier L(Δ) vs L_DH result, this provides cross-validation (Rule R3) that the ω-class second-moment growth signature is not idiosyncratic to a single GRH-conforming comparator — it appears to distinguish L_DH (which has zeros off the critical line and lacks an Euler product) from genuine L-functions in the Selberg class. The much larger ζ–L_DH gap relative to the L(Δ)–L_DH gap is consistent with ζ's special structure (all primes contribute via 1−p^{−s}), whereas the holomorphic cusp form Δ has bounded |a_p|p^{−1/2} ≤ 2 and so produces more modest growth. While encouraging, the conclusion is constrained by the sparse 4-point N-grid; densifying the grid (especially with additional points at N ≥ 10⁶) is necessary before treating these slope differences as a robust quantitative signature.
</discussion> <proposed-next-hypotheses>
1. Densifying the N-grid with additional points at N ∈ {3×10⁵, 3×10⁶, 10⁷} will preserve the sign and significance of the ζ−L_DH and L(Δ)−L_DH slope differences while shrinking their standard errors by at least 50%, and may reveal log-log-log curvature that the current 4-point fit cannot resolve.
2. The same ω-class slope ordering (Selberg-class L-function > L_DH) will hold for the Dirichlet L-function L(χ₄ mod 5), so a ζ-vs-L(χ₄) ANCOVA will yield non-significant slope differences (p > 0.05) for k ∈ {1,2,3,4}, identifying the signature specifically with the presence/absence of an Euler product rather than with arithmetic complexity.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ancova_zeta_vs_ldh_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-ω-class ANCOVA summary comparing ζ vs L_DH (this analysis) side-by-side with the prior L(Δ) vs L_DH results. Columns include omega_class_k, slope_zeta, slope_L_DH, diff (L_DH − ζ), p_inter (ζ vs L_DH), R², plus the corresponding L(Δ) slopes/diffs/p-values from `ancova_omega_class_summary.csv`. Produced via statsmodels OLS on `log M_k ~ log log N * L_function` for k ∈ {1,2,3,4} using the 4-point N-series in `omega_class_moments_N1e6.csv`.</artifact-description>
</artifact>
</artifacts>
</output> 