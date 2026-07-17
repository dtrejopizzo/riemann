## Overview <output>
<conclusion>
The simple one-parameter model log M_k = log C + a·log log N yields disjoint 95% CIs for the slope a between L(Δ) and L_DH only for the ω-class k=2 (1 of 4 classes), so the hypothesis as stated — that at least two of the four classes show disjoint CIs — is not supported.
</conclusion> <methods>
1. Loaded `omega_class_moments_N1e6.csv` and selected rows for L(Δ) and L_DH at N ∈ {10⁴, 5·10⁴, 10⁵, 10⁶} (4 N-points per L-function).
2. For each L-function and each k ∈ {1,2,3,4}, performed an ordinary least squares regression of y = log(M_k) on x = log(log(N)) using scipy.stats.linregress.
3. Recorded slope a, intercept, R², standard error of slope, and computed the 95% CI for a using t-critical with df = n − 2 = 2 (t₀.₉₇₅,₂ ≈ 4.303).
4. Built a side-by-side comparison table and tested whether the two 95% CIs are disjoint for each k.
5. Produced a single summary figure plotting a ± 95% CI for both L-functions across k.
Outputs saved to `omega_slope_fits_LDelta_vs_LDH.csv` and `omega_slope_comparison_table.csv`; figure saved as `omega_slope_comparison.png`.
</methods> <results>
Fitted slopes a (with 95% CI, R²) per ω-class: k=1:
- L(Δ): a = 0.289, 95% CI [0.193, 0.386], R² = 0.988
- L_DH: a = 0.171, 95% CI [0.125, 0.216], R² = 0.992
- CIs overlap (L_DH upper 0.216 > L(Δ) lower 0.193). NOT disjoint. k=2:
- L(Δ): a = 0.798, 95% CI [0.765, 0.831], R² = 0.99981
- L_DH: a = 0.480, 95% CI [0.391, 0.569], R² = 0.996
- CIs are disjoint (L(Δ) lower 0.765 > L_DH upper 0.569). DISJOINT. k=3:
- L(Δ): a = 2.023, 95% CI [1.858, 2.187], R² = 0.9993
- L_DH: a = 1.566, 95% CI [1.181, 1.951], R² = 0.994
- CIs overlap (L_DH upper 1.951 > L(Δ) lower 1.858). NOT disjoint. k=4:
- L(Δ): a = 4.821, 95% CI [2.241, 7.402], R² = 0.970
- L_DH: a = 3.066, 95% CI [2.375, 3.756], R² = 0.995
- CIs overlap broadly. NOT disjoint. Only 1 of 4 ω-classes (k=2) yields disjoint 95% CIs; the hypothesis requires ≥ 2.
</results> <challenges>
With only 4 N-points per fit, df = 2 and the t₀.₉₇₅ critical value is ≈4.303, producing wide CIs especially for the high-variance k=4 class (where L(Δ)'s CI spans [2.24, 7.40]). Tied behaviour of L(Δ) and L_DH at k=1, 3, 4 likely reflects shared leading-order growth scaling, with only finite-N corrections (better captured by log log log N terms) separating them — but as the primary-dataset notes record, two-parameter fits with the current 4-point grid are unstable. No data-quality issues otherwise.
</challenges> <discussion>
The k=2 ω-class is the most discriminating between GRH-conforming L(Δ) (a ≈ 0.80) and GRH-violating L_DH (a ≈ 0.48); this is consistent with squarefree-with-two-prime-factor terms carrying the bulk of the second-moment mass and being most sensitive to the off-critical-line zeros that contaminate L_DH. However, with only one disjoint pair of CIs, the simple single-parameter (log log N) model does not yet provide a robust multi-class signature distinguishing the two L-functions. A statistically convincing separation would benefit from (i) more N-points to shrink the CIs, or (ii) more degrees of freedom from a larger N-grid before attempting the two-parameter model that was previously found unstable. The k=2 separation is suggestive and warrants follow-up at intermediate N values.
</discussion> <proposed-next-hypotheses>
1. At k=2, the fitted slope a remains statistically distinct between L(Δ) and L_DH when the model is refit on a denser N-grid (adding N ∈ {2·10⁵, 5·10⁵, 2·10⁶}), and the gap |a_L(Δ) − a_L_DH| at k=2 is at least 5σ.
2. The relative discrepancy in fitted slopes between L(Δ) and L_DH peaks at the ω-class k* = ⌊log log N⌋ + 1 (so currently k*=2 for N ≤ 10⁶), reflecting the "typical" prime-factor count dominating the second moment.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>omega_slope_fits_LDelta_vs_LDH.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>OLS fit results for log M_k vs log log N, one row per (L-function, k) combination for L(Δ) and L_DH at k=1..4. Columns include slope, intercept, R², stderr, 95% CI bounds, n, p-value.</artifact-description>
</artifact>
<artifact>
<file-name>omega_slope_comparison_table.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Side-by-side comparison of fitted slope a, 95% CI string, and R² for L(Δ) vs L_DH for each ω-class k=1..4, plus a boolean column `disjoint_95CI` indicating whether the two CIs are disjoint.</artifact-description>
</artifact>
</artifacts>
</output>
