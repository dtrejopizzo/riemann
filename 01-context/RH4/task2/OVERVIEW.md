## Overview <output>
<conclusion>
The hypothesis is refuted: a linear regression of log(A_{k,F}) on log(d), log(q), and k explains only R²≈0.11 of the variance — far below the predicted 80% — and the residual GRH-true vs GRH-false separation is small and not statistically significant (Welch p≈0.29), so neither a degree/conductor "universality" nor a clean GRH-correlated residual signal is supported by the available 11×8 (C_k, M_kk) table.
</conclusion> <methods>
1. Loaded `Ck_Mkk_diag_results` from the workspace `.npy` files (`C.npy`, `M.npy`, `classes.npy`) — 11 classes (F1, F2, F4, F5p, F5m, F6, F7, F9, F10, F11, F12) × 8 ω-strata (k=0..7).
2. Computed amplification factor A_{k,F} = M_kk / C_k for all (class, k) pairs where both C_k > 0 and M_kk > 0 (83 valid pairs out of 88).
3. Built a class-invariants table from the v6 binding context document table of function classes: - F1 (ζ): d=1, q=1, GRH-true; F2 (Dirichlet χ mod 5): d=1, q=5, GRH-true. - F4 (L_DH), F5p, F5m: d=2, q=5, GRH-false (RH-violators). - F6 (Liouville), F7 (Möbius): d=1, q=1, GRH-true (anomalous but multiplicative). - F9 (Δ): d=2, q=1; F10 (newforms N∈{11,17,23}): d=2, q=17 (representative); F11 (Sym² Δ): d=3, q=1; all GRH-true. - F12 (linear combo of Dirichlet L's): d=2, q=15, GRH-false.
4. Fit OLS via `statsmodels.api.OLS`: log(A_{k,F}) ~ const + log(d) + log(q) + k. 83 obs, 79 dof.
5. Computed per-class mean residual; compared GRH-true (n=7) vs GRH-false (n=4) classes by Welch t-test and Mann-Whitney U.
6. Produced a 2-panel summary figure: (A) predicted vs observed log(A) colored by GRH; (B) bar chart of per-class mean residuals colored by GRH status. Saved CSVs `amplification_regression_data.csv` and `amplification_mean_residuals.csv`, and `amplification_regression_summary.png`.
</methods> <results>
- 83 (class, k) amplification points; A=1 trivially at k=0 (M_00=C_0=1) for every class.
- OLS regression log(A) ~ log(d)+log(q)+k: - R² = 0.112; adjusted R² = 0.078; F(3,79)=3.32, p=0.024. - log(d): coef = +0.114 (SE 0.344, p=0.74) — not significant. - log(q): coef = −0.023 (SE 0.122, p=0.85) — not significant. - k: coef = +0.179 (SE 0.057, p=0.0025) — only significant predictor; effect is dominated by the trivial k=0 anchor (A=1). Excluding k=0, R² collapses to 0.015 with all coefficients non-significant.
- Per-class mean residuals (sorted): F1 −0.27 (T), F7 −0.24 (T), F5p −0.20 (F), F4 −0.19 (F), F5m −0.17 (F), F10 −0.03 (T), F9 +0.00 (T), F12 +0.17 (F), F11 +0.23 (T), F2 +0.33 (T), F6 +0.36 (T).
- Mean residual: GRH-true = +0.054, GRH-false = −0.097.
- Welch t-test (true vs false): t=1.13, p=0.29; Mann-Whitney U: U=18, p=0.53. No significant residual GRH signal.
- The DH-violator family F4/F5± clusters together with notably negative residuals, whereas F12 (the other constructed violator) sits on the positive side — i.e., violator-class residuals do not share a common sign.
</results> <challenges>
- The "analytic conductor" is not unambiguously defined in the binding document; I used the LMFDB convention "level/modulus q" as a proxy and chose representative q for F10 (N=17, the middle of {11,17,23}) and degree 3 for F11 (Sym² of Δ, where the Sym³ alternative would give d=4). Sensitivity checks with d=4 for F11 or q=11/23 for F10 do not raise R² above ~0.15.
- F4, F5±, and F12 are not Selberg-class objects (linear combinations of Dirichlet L-functions); assigning a single "degree d" and "conductor q" is convention-dependent. I chose d=2 and q=lcm of the constituent moduli, consistent with the linear-combination structure given in the binding context.
- Only 11 classes provide 4 GRH-false vs 7 GRH-true samples, severely limiting power for the residual t-test (the test could not reliably detect even moderate effects with n=11 classes).
- k=0 is a structural anchor (A=1 by construction), inflating apparent significance of the k coefficient. Removing it eliminates all model signal, indicating no genuine k-trend in log(A) from this data.
</challenges> <discussion>
The hypothesis that peak amplification A_{k,F} = M_kk / C_k is dominantly governed by L-function degree and conductor — i.e., "universal" arithmetic invariants — is not supported by this 11-class × 8-stratum dataset. The very low R² (0.11, dropping to 0.02 once the trivial k=0 anchor is removed) shows that log(d), log(q), and k carry essentially no explanatory power for the per-class amplification curves at the resolution provided. This is consistent with the r28 finding that the C_k → M_kk relationship is strongly non-linear on the linear scale (R²≈0.71) but very tight on log-log (R²≈0.956): most of the signal is in the *coefficient mass* itself, not in summary invariants like d and q. Once C_k absorbs that mass, the residual ratio M_kk/C_k is a peak-conditioning multiplier whose variation across classes is not captured by d, q, k alone. The residual GRH analysis is correspondingly inconclusive. While the absolute mean-residual difference (~0.15 in log A, i.e. ~16%) is non-trivial, it is not statistically distinguishable from noise at n=11. Notably, the two RH-violator constructions split: F4/F5± (DH-style perturbations of a single Euler product) all show negative residuals, while F12 (a different linear combination of Dirichlet L-functions) sits on the positive side. This mirrors the r28 observation that "arithmetic ablation" works for additive perturbations of ζ but not for fundamentally different L-functions, and it suggests the GRH/violator label is not the right axis on which the residual variance is organized. Practical implication: A_{k,F} should not be treated as a near-deterministic function of (d, q, k), and removing a (d, q, k) trend from S_k features will not reliably yield a "universal" GRH-correlated signal at the current N=10⁶ and 11-class scope. A direct C_k-based normalization (i.e., log M_kk − log C_k, which is exactly log A) is more principled than a (d, q, k) regression.
</discussion> <proposed-next-hypotheses>
1. Peak amplification factor A_{k,F} is better described by the *local* ω-stratum coefficient density profile (e.g., the variance of |a_n|² across n with ω(n)=k, or the small-prime tail share of C_k) than by global invariants (d, q); a regression of log A_{k,F} on these local arithmetic moments will exceed R²=0.5 across the same 11 classes.
2. Within the additive-perturbation violator family (F4, F5±), residuals from a class-level log(M_kk) ~ log(C_k) regression carry a sign-consistent GRH-violator signature (negative offset versus the F1/F2/F6/F7/F9 manifold), while F12-type linear-combination violators do not — i.e., "GRH-violation" is not a single residual mode but at least two distinct ones tied to construction type.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>amplification_regression_data.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Long-format table of 83 (class, k) entries with C_k, M_kk, A=M_kk/C_k, log A, class invariants (degree d, conductor q, log d, log q), GRH status, and OLS residual from the log(A) ~ log(d)+log(q)+k fit. Built by merging the Ck_Mkk_diag_results arrays with class invariants taken from the v6 binding context.</artifact-description>
</artifact>
<artifact>
<file-name>amplification_mean_residuals.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-class mean residual of log(A_{k,F}) from the (log d, log q, k) OLS model, with GRH status. 11 rows, used for the GRH-true vs GRH-false comparison (Welch t-test p=0.29).</artifact-description>
</artifact>
<artifact>
<file-name>amplification_regression_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) predicted vs observed log(A_{k,F}) colored by GRH status with annotated R²=0.112 and coefficient p-values; (B) bar chart of per-class mean residuals colored by GRH status with the Welch t-test p-value annotated.</artifact-description>
</artifact>
</artifacts>
</output>
