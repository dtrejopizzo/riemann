## Overview <output>
<conclusion>
The 1-Wasserstein distance W₁ between the H0 persistence diagrams of the baseline ζ-zero point cloud and the deformed clouds P_δ scales quadratically with δ (fitted log–log slope ≈ 1.99), refuting the hypothesis of linear scaling.
</conclusion> <methods>
1. Installed gudhi, ripser, persim, and POT (gudhi's Wasserstein backend).
2. Loaded the first 2,000 ζ zeros from `zeta_zeros_5000_dps50.npy` (50-dp decimal strings) and cast to float64 — sufficient because the smallest shift tested (10⁻³) is far above float64 ε.
3. Built baseline P₀ = {(0.5, γₙ) : n=1..2000} and deformed P_δ for δ ∈ {10⁻³, 10⁻², 10⁻¹} by shifting only the first 20 points to (0.5+δ, γₙ).
4. Computed the H0 persistence diagram of each cloud via `ripser` (maxdim=0). Equivalent results were obtained passing a float64 pairwise-Euclidean distance matrix explicitly, ruling out float32 precision artifacts.
5. Computed W₁ with `gudhi.wasserstein.wasserstein_distance(order=1.0, internal_p=2.0, keep_essential_parts=False)` after dropping the single essential (infinite-death) H0 class in each diagram. `persim.wasserstein` (its default 1-Wasserstein with Euclidean ground metric) gave identical values.
6. Performed a least-squares fit of log₁₀(W₁) vs log₁₀(δ) to estimate the scaling exponent and produced a final log–log plot with slope=1 and slope=2 reference lines.
</methods> <results>
W₁(P₀, P_δ) values:
- δ = 1×10⁻³: W₁ = 2.384×10⁻⁷
- δ = 1×10⁻²: W₁ = 2.289×10⁻⁵
- δ = 1×10⁻¹: W₁ = 2.279×10⁻³ Successive ratios when δ increases by 10×: 96.0 and 99.6 (≈ 100 = 10²), consistent with quadratic growth. Log–log linear fit: slope = 1.990, intercept = −0.655 (W₁ ≈ 0.222·δ¹·⁹⁹). The optimal-transport cost between H0 diagrams is therefore governed by the same O(δ²/gap) leading correction that dominates pairwise Euclidean distance changes when only the x-coordinates of a subset of points shift: for cross pairs (one shifted, one not), Δd ≈ δ²/(2·gap), verified directly (e.g. for points γ₁ and γ₁₀₁ at δ=0.1: Δd = 2.236×10⁻⁵, exactly matching the prediction δ²/(2·gap)). Within-shifted and within-unshifted pairs are unchanged. Because every entry of the distance matrix shifts by at most O(δ²), the resulting changes in H0 birth/death values — and thus W₁ — inherit the same O(δ²) scaling.
</results> <challenges>
- `persim.wasserstein` does not accept an `order` parameter; used `gudhi.wasserstein.wasserstein_distance(order=1.0)` instead (also required installing POT). persim's default value matched gudhi's order=1 result exactly, confirming both are valid W₁ implementations with Euclidean ground metric.
- Initial concern that the ~10⁻⁷ value at δ=10⁻³ was a float32-precision artifact (ripser uses float32 internally); recomputing via an explicitly float64 distance matrix gave identical W₁ values, confirming the result is real, not numerical noise.
- H0 diagrams contain one essential (infinite-death) class per cloud; these were excluded from the Wasserstein computation (`keep_essential_parts=False`), which is appropriate since both diagrams have exactly one essential class that would be matched trivially.
</challenges> <discussion>
The proposed W₁-based detector does not improve on the bottleneck-distance result of r17 in this geometric setting. The reason is structural rather than metric-specific: the H0 persistence diagram of a 2-D point cloud aligned along a vertical line is determined by inter-point Euclidean distances. Shifting a subset of the x-coordinates by δ perturbs each cross-pair distance only by δ²/(2·gap) (second-order in δ), while same-side pair distances are unchanged. Any p-Wasserstein distance (including the bottleneck distance, p=∞) is therefore at most O(δ²) for this perturbation, regardless of the choice of p. To obtain a linear-in-δ TDA signal one would need either (i) a higher-dimensional ambient embedding that exposes the x-shift at first order, (ii) features sensitive to H1 cycles whose birth/death scales with x rather than distance, or (iii) a non-isotropic ground metric on the diagram (e.g. with a horizontal weight). The negative result strengthens the conclusion of r17 that the (Re, Im) point-cloud geometry is intrinsically a quadratically weak GRH-violation detector.
</discussion> <proposed-next-hypotheses>
1. Using an anisotropic embedding that amplifies the real part (e.g., mapping zeros to (κ·Re(s), Im(s)) with κ ≫ 1, or to (Re(s), Im(s), |L'(s)|)) will restore first-order (linear-in-δ) sensitivity of TDA Wasserstein distances to off-critical-line shifts.
2. Replacing H0-on-points with H1 persistence of the sublevel-set filtration of |ζ(σ+it)| over a 2-D rectangle will yield a TDA signal whose Wasserstein distance from the σ=½ baseline scales linearly with δ, because zero locations enter the function value at first order.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>w1_vs_delta_loglog.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Log–log plot of the 1-Wasserstein distance W₁ between the H0 persistence diagram of the baseline 2000-point ζ-zero cloud P₀ = {(0.5, γₙ)} and deformed clouds P_δ (first 20 points shifted to (0.5+δ, γₙ)) for δ ∈ {10⁻³, 10⁻², 10⁻¹}. Includes the fitted line (slope 1.990) and slope-1 / slope-2 reference lines, showing W₁ scales quadratically with δ, refuting the linear-scaling hypothesis.</artifact-description>
</artifact>
</artifacts>
</output>
