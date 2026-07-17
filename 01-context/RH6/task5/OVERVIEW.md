## Overview <output>
<conclusion>
The ANCOVA does not confirm the visual finding from r56: the slope difference between L(Δ) and L_DH in the log M_k vs log log N model is statistically significant (p<0.05) for *all four* ω-classes (k=1,2,3,4), not only for k=2.
</conclusion> <methods>
1. Loaded `omega_class_moments_N1e6.csv` and filtered to the two L-functions of interest (L(Δ) and L_DH), giving 4 N-points each (N = 10⁴, 5×10⁴, 10⁵, 10⁶) for a total of 8 rows per ω-class.
2. Constructed `loglogN = log(log(N_terms))` and `logMk = log(M_k)` for k ∈ {1,2,3,4}.
3. For each k, fit the ANCOVA model `logMk ~ loglogN * C(Lfun)` with `statsmodels.formula.api.ols`. L(Δ) is the reference category (alphabetical), so `loglogN:C(Lfun)[T.L_DH]` is the slope-difference (L_DH − L(Δ)) interaction term whose p-value tests slope equality.
4. Extracted the interaction coefficient, its p-value, and the two per-group slopes, plus model R². Saved the summary to `ancova_omega_class_summary.csv`.
5. Built a final summary figure overlaying the data points and ANCOVA fitted lines for both L-functions across all four ω-classes, with the per-k interaction p-value annotated.
Caveats applied: with only n=8 (4 points × 2 groups) per model, each interaction test has 4 residual degrees of freedom; this analysis assumes Gaussian residuals, linearity in log log N, equal variance, and independence — assumptions that cannot be meaningfully validated with 4 points per group and which the dataset description flags as a known limitation.
</methods> <results>
ANCOVA interaction-term results (slope of log M_k vs log log N for L_DH minus that for L(Δ)): | k | slope L(Δ) | slope L_DH | Δslope | p(interaction) | R² | sig p<0.05 |
|---|------------|------------|--------|----------------|------|------------|
| 1 | 0.2893 | 0.1707 | −0.1186 | 0.00882 | 0.9998 | yes |
| 2 | 0.7980 | 0.4801 | −0.3179 | 0.000136 | 0.9994 | yes |
| 3 | 2.0225 | 1.5660 | −0.4566 | 0.00935 | 0.9979 | yes |
| 4 | 4.8214 | 3.0658 | −1.7556 | 0.04747 | 0.9860 | yes | In every ω-class the GRH-violating L_DH has a shallower log-log-N growth slope than the GRH-conforming L(Δ), and the slope difference is significant at the α=0.05 level. The signal is strongest at k=2 (p ≈ 1.4×10⁻⁴), consistent with k=2 being the most visually clean discriminator in r56, but k=1 and k=3 are also clearly significant (p ≈ 0.009) and k=4 is marginally so (p ≈ 0.047). The one-parameter log log N model achieves R² > 0.985 in every case.
</results> <challenges>
- Only 4 N-points per L-function (the known sparseness flagged in the dataset description). With n=8 and 4 parameters, each ANCOVA has only 4 residual df, so the interaction tests are statistically valid in principle but have low robustness to model misspecification and to whether log log N is the "true" growth axis.
- Linearity and homoscedasticity in log log N cannot be properly diagnosed with so few points; residual plots are not informative at this sample size.
- The k=4 p-value (0.047) sits very close to the α=0.05 threshold and would not survive any multiple-comparison correction across the four k-classes (e.g., Bonferroni α=0.0125 would retain only k=1, k=2, k=3 as significant). Conversely, k=1, k=2, k=3 *do* survive Bonferroni, so the qualitative conclusion that the slope difference is broadly significant — not unique to k=2 — is robust.
- Reference category in `statsmodels` defaulted to L(Δ) alphabetically; the sign of the interaction coefficient was checked to ensure correct interpretation.
</challenges> <discussion>
The hypothesis predicted a selective signal at k=2. The data instead show a global pattern: across all four ω-classes the L_DH (GRH-violating) function exhibits a smaller log-log-N growth slope than L(Δ) (GRH-conforming), with the gap most cleanly resolved at k=2 but statistically present everywhere. This broadens, rather than narrows, the ω-class moment signature as a candidate discriminator. However, two cautions temper this. First, the strong R²>0.99 fits on only 4 points are likely overconfident: with so few N-values the linear log log N model is essentially interpolating, and any consistent vertical offset between the two L-functions plus a small slope tilt will register as a significant interaction. Second, the dataset description explicitly warns that this 4-point N-grid is too sparse for stable multi-parameter growth-rate fits, and the asymptotic behavior at much larger N (where higher-order log log log N or log log N⁻¹ corrections may dominate) cannot be ruled out. So while the ω-class signature appears more general than r56 suggested, confirming it as a genuine asymptotic discriminator — and identifying which k truly carries the cleanest signal — requires a denser N-grid before committing further computational resources.
</discussion> <proposed-next-hypotheses>
1. On a denser, wider N-grid (e.g., 10–20 logarithmically spaced N up to 10⁸), the slope gap Δslope_k = slope_L(Δ) − slope_L_DH will remain significant for k=2 while attenuating (or reversing sign) for k=1, 3, and 4 — i.e., the k=2 selectivity claimed in r56 is real but masked at low N by finite-size effects.
2. The same ANCOVA applied to ζ versus L_DH (both putatively GRH-conforming if RH holds for ζ but not for L_DH) will yield a slope difference whose magnitude scales as k(k−1)/2 (matching the leading log² of L²-mean asymptotics), providing a quantitative null model against which the L(Δ) vs L_DH signal can be calibrated.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ancova_omega_class_summary.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Summary table of the ANCOVA `log M_k ~ log log N * L_function` fitted separately for each ω-class k ∈ {1,2,3,4}, comparing L(Δ) and L_DH. Columns: omega_class_k, slope_L(Δ), slope_L_DH, slope_diff (L_DH − L(Δ)), p_interaction, significant_p<0.05, R². Derived from `omega_class_moments_N1e6.csv` using statsmodels OLS on the 4-point N-series (N = 10⁴, 5×10⁴, 10⁵, 10⁶).</artifact-description>
</artifact>
<artifact>
<file-name>ancova_omega_class_figure.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Single summary figure overlaying log M_k vs log log N data points and fitted ANCOVA regression lines for L(Δ) (blue) and L_DH (red) across all four ω-classes k=1..4 (distinguished by marker shape and line style). Per-k interaction p-values are annotated on the plot, showing all four are significant at p<0.05.</artifact-description>
</artifact>
</artifacts>
</output>
