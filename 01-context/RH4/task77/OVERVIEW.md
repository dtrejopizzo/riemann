## Overview <output>
<conclusion>
The Δ_jk matrices for the 7-member Davenport–Heilbronn family are strongly low-rank (mean λ₁²/‖Δ‖_F² ≈ 0.90, ≈0.94 excluding the κ=−1.09 outlier) and their leading eigenvectors are far more stable than scalar Δ-statistics (mean off-diagonal cosine similarity 0.994; ≥0.999 within the 6 inner members), partially supporting the "low-rank perturbation" hypothesis — but the residual variation in v₁ orientation tracks the construction parameter κ rather than the off-line-zero location β, so the eigenvector does not encode (β, γ).
</conclusion> <methods>
1. The bundled archive `DH_family_results.npz` was not present in the workspace; per the dataset description, equivalent component `.npy` files were loaded: `M_F1.npy` (8×8 ζ-baseline), `M_betas.npy` (7×8×8 family matrices), `betas.npy`, `kappas.npy`.
2. For each family member i ∈ {0,…,6} (β = 0.55, 0.60, …, 0.85), computed Δ⁽ⁱ⁾ = M_betas[i] − M_F1. All matrices are real symmetric (verified via `np.allclose(Δ, Δᵀ)`), so eigendecomposition was done with `np.linalg.eigh`.
3. Eigenvalues were sorted by |λ| descending. The rank-1 fraction was computed as λ₁²/‖Δ‖_F² with ‖Δ‖_F² = Σ λⱼ² (cross-checked against Σ Δ_jk²). An entropy-based effective rank exp(−Σ pⱼ log pⱼ) with pⱼ = λⱼ²/‖Δ‖_F² was also reported.
4. Leading eigenvectors v₁⁽ⁱ⁾ were sign-aligned to the central member (β=0.70) and the 7×7 cosine-similarity matrix v₁⁽ⁱ⁾·v₁⁽ʲ⁾ was computed.
5. Per-component Pearson correlations of v₁ with β and |κ| and a partial correlation with β controlling for |κ| (linear residualization) were computed using `scipy.stats.pearsonr`.
6. Coefficient of variation (std/|mean|) was computed for scalar Δ-statistics for benchmarking against eigenvector stability.
7. Final summary figure (PNG) and a derived archive `DH_delta_eigenstructure.npz` (eigenvalues, eigenvectors, similarity matrix, rank-1 fractions) were saved.
</methods> <results>
Per-member statistics: | β | κ | ‖Δ‖_F² | λ₁ | λ₁²/‖Δ‖_F² | eff. rank |
|------|--------|--------|--------|-----------|-----------|
| 0.55 | −1.094 | 691.7 | −21.44 | 0.664 | 2.49 |
| 0.60 | −0.489 | 876.0 | −28.32 | 0.915 | 1.43 |
| 0.65 | −0.185 | 952.9 | −29.98 | 0.943 | 1.30 |
| 0.70 | +0.011 | 968.0 | −30.27 | 0.947 | 1.28 |
| 0.75 | +0.153 | 954.6 | −30.06 | 0.947 | 1.28 |
| 0.80 | +0.267 | 932.9 | −29.67 | 0.944 | 1.30 |
| 0.85 | +0.364 | 907.5 | −29.17 | 0.938 | 1.33 | Mean λ₁²/‖Δ‖_F² = 0.900 ± 0.097 (all 7); 0.939 ± 0.012 (excluding the κ=−1.09 / β=0.55 extreme outlier). |λ₂|/‖Δ‖_F ≈ 0.20–0.26 for the 6 inner members and 0.48 for β=0.55, confirming a dominantly rank-1 structure for the inner family. Leading eigenvectors (sign-aligned to β=0.70) are nearly identical: cosine-similarity matrix off-diagonal mean = 0.9937 (min 0.9757, max 1.0000); restricted to β ∈ {0.60,…,0.85}, mean = 0.99975 (min 0.99927). By contrast, scalar Δ-statistics have CVs of 9.9% (‖Δ‖_F²), 10.3% (λ₁), 10.7% (λ₁²/‖Δ‖_F²), and 27.8% (effective rank). The leading eigenvector is therefore ~10²–10³× more stable across the family than scalar norms. The small residual variation in v₁ does not encode β. Per-component Pearson correlations |r(v₁[j], |κ|)| range 0.88–0.97 with p ≤ 0.008 for every component, while |r(v₁[j], β)| are 0.51–0.85 with mostly non-significant p-values. After residualizing v₁[j] on |κ|, only 1/8 components retains a significant residual correlation with β at α = 0.05 (j=4: r = 0.77, p = 0.045), which would not survive multiple-comparison correction. The cosine similarity to the central member also correlates more strongly with |κ| (r = −0.91, p = 0.011) than with β (r = +0.62, p = 0.14).
</results> <challenges>
- The bundled `DH_family_results.npz` was absent; component `.npy` files (`M_F1.npy`, `M_betas.npy`, `betas.npy`, `kappas.npy`, `Sk_peaks.npy`, etc.) were used as documented in the primary-dataset description.
- Sample size is small (n = 7 family members), so partial-correlation tests have low power; reported p-values should be interpreted cautiously and we did not apply multiple-comparison correction in the per-component test.
- The β=0.55 / κ=−1.094 member is a clear outlier (rank-1 fraction 0.66 vs ~0.94 for the others), driven by its much larger |κ|; its inclusion biases family-wide means downward and inflates the eigenvector-similarity off-diagonal range.
- We cannot independently verify the original `r63` baseline construction or the precise definition of M_jk from the available `.npy` files; we treated `M_F1.npy` as the ζ baseline as labeled.
</challenges> <discussion>
The hypothesis splits into two empirically separable claims. The structural claim — that Δ_jk is approximately rank-1 — is strongly supported: λ₁ alone captures ≈94% of the squared Frobenius norm for the six inner family members (and even at β=0.55, 66% concentrates in a single mode). This is consistent with resonance-theoretic predictions (f40) of a single dominant "scar" mode imprinted on the peak-conditioned cross-term matrix. The orientational claim — that v₁ encodes the off-line zero location (β, γ) — is not supported. The eigenvector is dramatically more stable than scalar norms (a genuine, useful finding), but the tiny residual rotation that does occur tracks |κ| almost perfectly and shows no robust β-dependence after κ is partialled out. This recapitulates, at the level of the eigenvector, the same κ-confound that r66 documented for scalar Δ-statistics: the spectral signature reflects how the function is built (the κ deformation), not where its non-trivial zero sits. Practically, this means v₁ functions as a near-universal "DH violator direction" — useful for anomaly detection of this construction class — but it is not an inverse-bridge feature for localizing zeros. Recovering (β, γ) from spectral data, if possible at all, will likely require a different observable (e.g., a γ-localized phase observable from the complex S_k(t) at peaks) rather than the time-averaged matrix Δ_jk.
</discussion> <proposed-next-hypotheses>
1. Within a fixed-κ slice of the DH construction (varying only γ, the imaginary part of the off-line zero), the leading eigenvector of Δ_jk will rotate measurably and its rotation angle will correlate linearly with γ — testing whether κ is the only confound and γ-dependence is recoverable when |κ| is held constant.
2. The complex S_k(t) values at peaks contain a γ-localized phase signature: the windowed cross-spectrum ⟨S_j(t)·S_k(t)*·e^(−iγt)⟩ over peaks will exhibit a resonance peak at the true off-line ordinate γ that is absent from the time-averaged real matrix M_jk, providing the inverse-bridge observable that v₁(Δ) fails to be.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>DH_delta_eigenstructure.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Compressed NumPy archive of the eigen-analysis of the Davenport–Heilbronn Δ_jk matrices. Contains: betas (7,), kappas (7,), M_F1 (8,8) baseline, M_betas (7,8,8), full sorted eigenvalues per member, sign-aligned leading eigenvectors (7,8), the 7×7 cosine-similarity matrix of v₁'s, λ₁²/‖Δ‖_F² rank-1 fractions, ‖Δ‖_F², λ₁, and entropy-based effective rank. Produced by symmetric eigendecomposition (`np.linalg.eigh`) of Δ⁽ⁱ⁾ = M_betas[i] − M_F1 with sign-alignment to the β=0.70 reference.</artifact-description>
</artifact>
<artifact>
<file-name>DH_delta_lowrank_eigenstructure.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: rank-1 variance fraction λ₁²/‖Δ‖_F² versus β, annotated with κ values; mean = 0.900 across all 7 members, 0.939 excluding the β=0.55/κ=−1.09 outlier. Panel B: 7×7 heatmap of cosine similarities between sign-aligned leading eigenvectors v₁ of Δ_jk; mean off-diagonal value 0.9937, demonstrating that the orientation of the dominant Δ mode is highly stable across the DH family.</artifact-description>
</artifact>
</artifacts>
</output>
