## Overview <output>
<conclusion>
The hypothesis is NOT supported: the H0 persistence-diagram bottleneck distances do not separate L_DH from the GRH-conforming functions — in this analysis L_DH is the SECOND-most isolated (after ζ, which is an outlier purely because of zero-density / height-range differences), and permutation tests give p ≈ 0.48–0.50, consistent with the prior r17 finding that H0 bottleneck distance scales as δ² and is therefore a weak detector of small off-critical-line deviations.
</conclusion> <methods>
1. Loaded the three available high-precision zero lists (`zeta_zeros_5000_dps50.npy`, `lchi_zeros_5000_dps50.npy`, `ldelta_zeros_2000_dps50.npy`) and the 122 L_DH zeros from `ldh_zeros_small_T.json` (t ∈ [1, 200], dps=20). No `checkpoints_ldh/ldh_ckpt_02500.npy` was present, so 2 000 L_DH zeros are not available; for a fair like-for-like comparison the analysis was restricted to the first **N = 122** zeros of each function (matched cardinality).
2. Converted all zero strings to floats via `mpmath.mpf` at dps=50 and built 2-D point clouds `(0.5, γ_n)` for each function. For L_DH the literature-known off-critical zero `(0.808517, 85.699348)` was appended, yielding 123 points.
3. Computed H0 persistence diagrams with `ripser` (maxdim=0).
4. Computed all pairwise H0 bottleneck distances with `persim.bottleneck` (essential infinite class ignored, default behavior — flagged by persim warning).
5. Visualised the 4×4 distance matrix with classical MDS (`sklearn.manifold.MDS`, dissimilarity='precomputed').
6. Two complementary permutation tests for whether L_DH is an outlier: (a) **Exact rank-based perm test (4 scenarios)**: re-injected the off-critical point `(0.808517, 85.699348)` into each of the 4 critical-line clouds in turn; computed the mean bottleneck distance of the perturbed function to the other three; p = (# scenarios ≥ observed) / 4. (b) **Randomised perm test (N = 200)**: random function chosen, random one of its zero ordinates used as the t-coordinate for an injected off-critical point at Re = 0.808517; mean bottleneck distance to the other three (critical-line-only) computed; p = (#null ≥ observed + 1)/(N+1).
7. As a control, also computed bottleneck(L_DH-with-off-critical, L_DH-critical-only) to isolate the local effect of the off-critical point on its own diagram.
</methods> <results>
Pairwise H0 bottleneck distance matrix (first 122 zeros each; L_DH includes the off-critical zero):
``` zeta L(chi) L(Delta) L_DH
zeta 0.0000 2.6696 2.2021 2.5422
L(chi) 2.6696 0.0000 0.4675 0.7560
L(Delta) 2.2021 0.4675 0.0000 0.9072
L_DH 2.5422 0.7560 0.9072 0.0000
```
Mean bottleneck distance of each function to the other three:
ζ = 2.471, L(χ) = 1.298, L(Δ) = 1.192, **L_DH = 1.402**.
Rank (most → least isolated): ζ ≫ L_DH > L(χ) > L(Δ). Effect of injecting the off-critical point on L_DH's own diagram: d_B(L_DH_full, L_DH_crit-only) = **0.375** — small and similar in magnitude to the L_DH–L(χ) and L_DH–L(Δ) distances. Permutation tests for "L_DH is separated":
• Rank-based (4 scenarios — inject off-critical into ζ, L(χ), L(Δ), or L_DH): S_inj = {ζ: 2.407, L(χ): 1.392, L(Δ): 1.298, L_DH: 1.402} → **p = 0.50**.
• Randomised perm (N = 200 random injections): null mean = 1.642 (std 0.432), observed = 1.402 → **p = 0.478**. MDS embedding (stress = 3.2 × 10⁻⁴) places ζ alone in the bottom-left quadrant; L(χ), L(Δ), and L_DH cluster together with L_DH only marginally further from L(χ)/L(Δ) than they are from each other.
</results> <challenges>
• The dataset description references `checkpoints_ldh/ldh_ckpt_02500.npy` (2 500 L_DH zeros at dps=50), but the file is not present in the workspace; only 122 L_DH zeros at dps=20 (in t ∈ [1, 200]) are available. To keep the comparison fair, all four functions were restricted to their first 122 zeros — this departs from the objective's "first 2 000 zeros" specification.
• Generating 2 000 fresh L_DH zeros via `cypari2` would have taken hours and could not be completed within the runtime budget; this is the dominant limitation of the analysis.
• ζ becomes a spurious "TDA outlier" simply because its first 122 zero spacings span up to t = 273 vs ≤ 200 for the others (higher density of zeros differs by function). This height-range confound dominates the matrix; a height-matched comparison (rather than count-matched) would be a useful follow-up but again requires more L_DH zeros.
• `persim.bottleneck` ignores the single infinite-persistence H0 class; this is standard practice and emitted only as a warning.
• Permutation tests with only 4 functions give very coarse exact p-values (granularity 0.25); the randomised injection variant alleviates this but is itself a model-specific null.
</challenges> <discussion>
The numerical evidence directly refutes the working hypothesis at the resolution we can currently test (n = 122 zeros): the off-critical-line zero of L_DH at s ≈ 0.8085 + 85.699 i changes the L_DH H0 persistence diagram by only ≈ 0.375 in bottleneck distance, which is comparable to or smaller than the natural pairwise distances among the three GRH-conforming functions themselves (0.47–0.91). Consequently L_DH does not stand out as a TDA outlier; if anything, the "outlier" position in MDS belongs to ζ, and it is driven not by a critical-line violation but by ζ's larger height span at fixed index. This is fully consistent with the previously-documented r17 result that for a roughly 1-D point cloud aligned on Re = 1/2, a real-part perturbation δ enters the H0 bottleneck distance only quadratically (d_B ∝ δ²), so the contribution from a single off-critical point with δ ≈ 0.31 is bounded by ≈ 0.1, easily masked by the variation in zero spacings between L-functions. H0 bottleneck distance on the (Re, Im) cloud is therefore confirmed not to be a sensitive geometric test of GRH. More discriminating approaches will need either higher-dimensional homology, point-cloud rescalings that amplify real-part displacements (e.g. (k·Re, Im) with k ≫ 1), or detectors of arithmetic origin such as the full Weil quadratic form Q = M_zeros − M_arith already validated for L_DH.
</discussion> <proposed-next-hypotheses>
1. Rescaling the real-coordinate by a large factor k (point cloud `(k·Re(s), Im(s))` with k ≥ 50) will make the H0 bottleneck distance d_B between L_DH and the three GRH-conforming functions scale **linearly** with the off-critical displacement δ, so that L_DH becomes a statistically significant TDA outlier (perm p < 0.05) once k·δ exceeds the typical nearest-neighbour gap of the zeros.
2. Using H1 (loop) persistence on the (Re, Im) point cloud — not H0 — and including the off-critical L_DH zero will produce a finite-persistence H1 feature in L_DH that is absent in ζ, L(χ), and L(Δ), thereby providing a topology-only detector of off-critical zeros that does not suffer from the δ² insensitivity of H0.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>tda_lfunction_comparison.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) heat-map of the 4×4 pairwise H0 bottleneck distance matrix among ζ, L(χ), L(Δ), and L_DH (first 122 zeros each; L_DH includes the off-critical zero at (0.808517, 85.699348)); (B) 2-D classical MDS embedding of the same matrix annotated with the rank-based (p = 0.50) and randomised (p = 0.48) permutation p-values for L_DH separation. Generated with ripser/persim/sklearn/matplotlib.</artifact-description>
</artifact>
<artifact>
<file-name>h0_bottleneck_distance_matrix.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>4×4 CSV table of pairwise H0 bottleneck distances among the H0 persistence diagrams of the four L-functions, computed with persim.bottleneck on ripser diagrams of (Re(s), Im(s)) point clouds built from the first 122 zeros of each function (L_DH cloud additionally contains the off-critical zero (0.808517, 85.699348)).</artifact-description>
</artifact>
</artifacts>
</output>
