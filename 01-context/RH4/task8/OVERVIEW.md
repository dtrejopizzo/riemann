## Overview <output>
<conclusion>
The exponential-tilt-of-Poisson model captures the qualitative shape of the leading eigenvector of the peak amplification matrix A_jk but does NOT meet the hypothesized R² > 0.95 criterion (mean R²≈0.72), and the fitted tilt λ does not separate GRH-true from GRH-violator classes — instead it primarily separates non-modular (λ ≈ 0.43–0.46) from modular (λ ≈ 0.10–0.32) families.
</conclusion> <methods>
1. Loaded the previously-computed per-class amplification matrices `A_matrices.npy` (shape 11×8×8), corresponding M_jk matrices, baseline diagonals, family/GRH labels, and PCA outputs from the workspace artifact set derived from `A_jk_matrices_and_PCA.npz`.
2. Computed the class-averaged amplification matrix Ā = mean_c A^(c) and obtained its leading symmetric eigenvector v_avg via `numpy.linalg.eigh` (using the symmetrized (A+Aᵀ)/2). Sign was fixed so that the dominant component is positive.
3. Defined the theoretical baseline P(k|μ) = `scipy.stats.poisson.pmf(k, μ)` with μ fixed at log(log(10⁶)) ≈ 2.6258, and the parametric model f(k) = C · exp(λk) · P(k|μ) for k = 0..7.
4. Fit (C, λ) via `scipy.optimize.curve_fit` (least-squares) on k=0..7 for both the class-averaged eigenvector and the per-class leading eigenvectors of each A^(c). Goodness of fit reported as R² = 1 − SS_res/SS_tot.
5. Repeated fits restricted to k=0..6 to control for the documented S_7 leak in mod-5 classes; assessed sensitivity to fixing μ vs. letting μ vary.
6. Tested whether the fitted λ discriminates GRH-true vs. GRH-violator classes via Mann–Whitney U.
7. Produced a 2-panel summary figure (`erdos_kac_tilt_fit.png`) and a per-class fit table (`erdos_kac_tilt_fits.csv`).
</methods> <results>
- Class-averaged leading eigenvector v_avg (k=0..7): [0.100, 0.209, 0.343, 0.472, 0.573, 0.484, 0.207, 0.017]; leading eigenvalue ≈ 59.4 (for the mean A_jk).
- Class-averaged fit: C = 0.708, λ = 0.401, R² = 0.861 (k=0..7); with μ free, μ = 2.88, λ = 0.310, R² = 0.861. Both well below the hypothesized 0.95 threshold.
- Per-class fits with μ fixed at log log 10⁶: | class | family | GRH | λ | R² | |-------|--------|-----|------|------| | F1 | zeta | GRH | 0.451 | 0.568 | | F2 | character | GRH | 0.431 | 0.759 | | F4 | DH | violator | 0.445 | 0.687 | | F5p | DH | violator | 0.446 | 0.690 | | F5m | DH | violator | 0.444 | 0.685 | | F6 | Liouville/Möbius | GRH | 0.437 | 0.877 | | F7 | Liouville/Möbius | GRH | 0.462 | 0.900 | | F9 | modular | GRH | 0.320 | 0.853 | | F10 | modular | GRH | 0.297 | 0.881 | | F11 | modular | GRH | 0.102 | 0.277 | | F12 | DH | violator | 0.439 | 0.728 | Mean R² = 0.719; median = 0.728. No class achieves R² > 0.95.
- λ does not separate GRH from violators: violators cluster tightly at λ ≈ 0.443±0.003, but GRH-true classes span 0.10–0.46, overlapping the violator range. Mann–Whitney U on λ ~ GRH status: U = 8, p = 0.32 (n.s.).
- λ DOES separate families: modular forms (F9, F10, F11) have λ = 0.10–0.32 (mean 0.24, std 0.12), while all non-modular classes (zeta, character, Liouville/Möbius, Davenport–Heilbronn) lie in λ = 0.43–0.46 (between-family separation is essentially complete).
- Residual structure (e.g. for v_avg): model under-predicts at k=0 (residual +0.05), over-predicts at k=2,3 and at k=7 (residual −0.13). The empirical eigenvector is more peaked at k=4 and falls faster at the right tail than C·exp(λk)·Poisson(μ) can accommodate, indicating sub-Poisson tail behavior.
- Restricting the fit to k=0..6 changes λ moderately (≈+0.05 for non-modular classes) but does not raise R² above 0.95 (mean R² = 0.56, with one class going negative).
</results> <challenges>
- The `A_jk_matrices_and_PCA.npz` archive itself was not present, but its constituent arrays were available as separate `.npy` files; these were loaded and used directly.
- Notably, `pca_components.npy` is shape (10, 64): each row is a flattened 8×8 matrix (a PCA over per-class A matrices), not a length-8 vector. The objective's "pc1_vector of shape 8" therefore had to be interpreted as the leading eigenvector of the (class-averaged or per-class) A_jk matrix itself, which is consistent with the rationale (r45) about exponential tilting acting on ω-strata.
- The 8-point grid (k=0..7) provides only 6 degrees of freedom after a 2-parameter fit; R² is sensitive to single-point residuals (especially k=7), and the boundary behavior of the eigenvector at the leak-affected k=7 stratum perturbs fits.
- F11 has a noticeably flatter/lower leading eigenvector (lead eigenvalue only 5.0, vs ≥25 for other classes), causing its tilt fit to be poor (R²=0.28) and λ to collapse near 0.1.
</challenges> <discussion>
The empirical leading eigenvector of A_jk is unambiguously concentrated at higher ω-strata than the Poisson(log log N) baseline — a clear signature of "exponential tilting toward many-prime integers" predicted by the resonance method. However, the exact functional form C·exp(λk)·Poisson(k|μ) is only an approximate description: it cannot simultaneously match the small k=0 weight and the rapid decay above k=4. Modular L-functions (F9–F11) exhibit a markedly weaker tilt, consistent with their multiplicative-but-bounded coefficients (Deligne |a_p| ≤ 2 p^{(k-1)/2} normalized) damping the contribution of highly composite n compared with completely multiplicative ±1 coefficients (Liouville, character). Davenport–Heilbronn violators (F4, F5p, F5m, F12) and Liouville/Möbius/zeta GRH classes share nearly identical tilts (λ ≈ 0.44), reaffirming the prior finding (r39, r46) that simple coefficient/eigenvector statistics fail to distinguish GRH-true from GRH-violator families. Thus λ is informative as a family descriptor but is not a GRH discriminant. The hypothesis is rejected on both stated criteria (R² > 0.95 fails, λ does not correlate with GRH status); the residual pattern points instead toward a heavier-tailed (e.g. negative-binomial or shifted-Poisson) baseline rather than a pure Poisson, plus possible higher-order tilts.
</discussion> <proposed-next-hypotheses>
1. The leading eigenvector of A_jk is more accurately modeled by a tilted negative-binomial baseline P_NB(k | r, p) — reflecting the over-dispersion of ω(n) at peak-conditioned events — and a two-parameter fit (tilt λ, dispersion r) will achieve R² > 0.95 across all non-modular classes while preserving the family-level separation seen in λ.
2. Within the modular family, the fitted tilt λ correlates linearly with the Sato–Tate second moment ⟨a_p²⟩/p^{k-1} (≈1 for holomorphic forms after normalization vs. the value 2 for completely multiplicative ±1 coefficients), providing a quantitative bridge between the empirical amplification structure and the analytic conductor / coefficient-distribution of the L-function.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>erdos_kac_tilt_fits.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per-class non-linear least-squares fits of the leading eigenvector of the peak amplification matrix A_jk to the model C·exp(λk)·Poisson(k|μ=log log 10⁶) for k=0..7, including fitted C, λ, R², family, GRH status, and the leading eigenvalue. Generated via numpy.linalg.eigh on each (A+Aᵀ)/2 followed by scipy.optimize.curve_fit.</artifact-description>
</artifact>
<artifact>
<file-name>erdos_kac_tilt_fit.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final two-panel summary figure: (A) class-averaged leading eigenvector vs. Poisson baseline and exp-tilted Poisson fit (λ=0.401, R²=0.861); (B) per-class fitted tilt λ colored by family with GRH violators hatched, showing modular forms with λ≈0.10–0.32 vs. non-modular classes at λ≈0.43–0.46.</artifact-description>
</artifact>
</artifacts>
</output> 