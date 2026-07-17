## Overview <output>
<conclusion>
The hypothesis is refuted: a regression of PC1/PC2 of the amplification matrix A_jk on the fundamental functional-equation invariants (degree d, log conductor, Σ Re(μ_j), number of gamma factors) explains far less than 60% of the cross-validated variance — leave-one-out R² is negative for both components (PC1: −0.80, PC2: −0.38 under RidgeCV).
</conclusion> <methods>
1. Loaded `projections.npy` (11×10) and `classes.npy` from `A_jk_matrices_and_PCA.npz`-derived files at `/workspace/.../`. Targets are PC1 and PC2 from these projections. The dataset contains 11 of the 12 requested classes; F14 is not present in the artifact and could not be added without redoing the upstream PCA, so analysis was performed on n=11.
2. Compiled per-class fundamental invariants from the Selberg-class definitions in the v6 PDF and standard references: - F1 ζ: d=1, q=1, Σμ=0, nΓ=1; Γ_R(s/2). - F2 L(s,χ_4 mod 5) (odd Dirichlet character): d=1, q=5, Σμ=1, nΓ=1. - F4, F5p, F5m (Davenport–Heilbronn family): d=1, q=5, Σμ=1, nΓ=1. - F6 Liouville, F7 Möbius (≈ζ(2s)/ζ(s), 1/ζ(s)): d=1, q=1, Σμ=0, nΓ=1. - F9 Δ (weight 12, level 1): d=2, q=1, Γ_R(s+11/2)Γ_R(s+13/2) → Σμ=12, nΓ=2. - F10 (weight 2, level 11): d=2, q=11, Γ_R(s+1/2)Γ_R(s+3/2) → Σμ=2, nΓ=2. - F11 Sym²Δ: d=3, q=1, Γ_R(s)Γ_R(s+11)Γ_R(s+12) → Σμ=23, nΓ=3. - F12 (L(s,χ_3)+L(s,χ_5) DH-style): d=2, q=15, Σμ=1+1=2, nΓ=2.
3. Built the 11×4 design matrix [d, log q, Σμ, nΓ] and noted that d and nΓ are perfectly collinear (r=1.000); kept both for completeness, results unchanged after dropping nΓ.
4. Trained two regressors per PC: standardized `RidgeCV` (α∈logspace(−3,3,25)) and OLS, evaluated by leave-one-out CV (predictive R² = 1 − SS_res/SS_tot from out-of-fold predictions). Also fitted a degree-2 polynomial Ridge for sanity.
5. Reported in-sample R², LOO R², and per-feature marginal Pearson correlations with PC1/PC2.
</methods> <results>
- LOO R² (RidgeCV): PC1 = −0.80, PC2 = −0.38.
- LOO R² (OLS): PC1 = −0.99, PC2 = −2.12.
- LOO R² (Ridge + degree-2 polynomial of d, log q, Σμ): PC1 = −0.52, PC2 = −2.63.
- In-sample R² (OLS, the most generous): PC1 = 0.35, PC2 = 0.35 — already below the 0.60 threshold even before cross-validation.
- Marginal Pearson correlations with PC1: degree −0.14, log q −0.12, Σμ −0.28, nΓ −0.14. With PC2: degree +0.57, log q +0.14, Σμ +0.45, nΓ +0.57. The strongest single signal (degree↔PC2, r≈0.57, R²≈0.33) is well below 60%.
- All four mod-5 degree-1 violators/character objects (F2, F4, F5p, F5m) share the same invariant vector, yet their PC1 values differ wildly (F2: +22.7 vs F4/F5p/F5m: ≈ −35.6), so the invariants cannot in principle distinguish a major axis of the amplification space.
</results> <challenges>
- The artifact contains 11 classes (no F14), so the analysis was n=11 instead of the requested 12; this further limits LOO statistical power but does not change the qualitative conclusion (in-sample R² already <0.4).
- nΓ and degree are perfectly collinear on this set, so they encode the same information.
- Several invariants (e.g., Davenport–Heilbronn objects F4/F5p/F5m, and arguably F12) are not strictly Selberg-class; a "degree", "conductor" and gamma factor must be assigned by convention. I used the gamma factor of the underlying Dirichlet L-function(s); plausible alternative conventions (e.g., counting F12 as a sum of two degree-1 objects giving d_eff=2 with combined log q=log 15) were used and do not lift R² near 60%.
- Mapping "Σ Re(μ_j) of Π Γ((s+μ_j)/2)" vs Π Γ_R(s+μ_j) (which differ by a factor of 2 in shifts) is a convention; both choices are linear rescalings of the same column under standardization, so this does not alter the regression.
</challenges> <discussion>
Combined with prior findings (r39, r44) that simple bulk a_n statistics fail to predict peak amplification, this result shows that the *coarsest* analytic invariants of the functional equation — degree, conductor, and gamma-factor shifts — likewise do not pin down a class's location in PC1/PC2 of A_jk. The clearest demonstration is that the four objects sharing the (d=1, q=5) Dirichlet-character / DH-family invariant vector occupy two completely different PC1 regimes (F2 in the GRH-true cluster vs F4/F5p/F5m in the violator cluster). PC2 carries some degree-related signal (modular/symmetric-square classes are pushed positive) but not enough to predict held-out classes. The amplification PC structure therefore appears to depend on properties beyond the global functional-equation data — plausibly on the *peak-conditioned* second-moment structure of the coefficients (consistent with rule R5 that conditional cross-covariances are not captured by unconditional invariants). This is a useful negative result: it directs the search toward conditioned/local invariants (e.g., low-lying-zero one-level density, conditional small-prime moments, symmetry type) rather than global Selberg-class data.
</discussion> <proposed-next-hypotheses>
1. The PC1 coordinate of A_jk is predicted (CV R²>0.6) by the *symmetry type* of the L-function (unitary vs orthogonal vs symplectic, and GRH vs violator) together with the one-level density of low-lying zeros, rather than by (d, log q, Σμ).
2. Replacing global gamma-factor shifts with a peak-conditioned moment statistic — specifically E[|a_p|²/p | peak event] aggregated over small primes p≤100 — yields LOO R²>0.6 for both PC1 and PC2 across the same 11 classes.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>invariants_to_PC_regression.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel figure summarizing the LOO regression of PC1/PC2 (from A_jk PCA projections) on the four functional-equation invariants. Panel A: scatter of true vs LOO-predicted PC coordinates per class, showing predictions collapse near zero with no alignment to y=x. Panel B: bar chart of in-sample and LOO R² for RidgeCV and OLS, with the hypothesis threshold R²=0.6 marked; all LOO bars are negative, refuting the hypothesis.</artifact-description>
</artifact>
</artifacts>
</output>
