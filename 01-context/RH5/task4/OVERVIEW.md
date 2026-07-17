## Overview <output>
<conclusion>
The hypothesis is REFUTED in its specified form: a raw Vietoris–Rips H1 persistence pipeline on the 2D point cloud (Re(ρ), Im(ρ)) of zeros 900–1100 yields empty H1 diagrams for both ζ and ζ_δ, bottleneck distance 0, and a permutation p-value of 1.000 — identical to the standard imaginary-part-only TDA result reported in r25.
</conclusion> <methods>
1. Loaded `zeta_zeros_N5000_dps50.npy` (1-D `<U51` array) and `zeta_delta_zeros_N5000_dps50.npy` (structured array with `re` and `im` fields).
2. Constructed two (200×2) point clouds for indices 900–1100 (the perturbation region, which contains the indices 1000–1019 modified in ζ_δ). - ζ point cloud: Re=0.5 for all points; Im = float-cast of the high-precision strings. - ζ_δ point cloud: Re=0.6 for indices 1000–1019 (confirmed: exactly 20 contiguous points), Re=0.5 elsewhere; identical Im values.
3. Computed Vietoris–Rips persistence diagrams (H0, H1) using `ripser.ripser(pc, maxdim=1)` (installed `ripser` and `persim` at runtime).
4. Computed the observed H1 bottleneck distance using `persim.bottleneck`.
5. Ran a B=1000 label-permutation test (seed=42): combined the 400 points, randomly partitioned them into two groups of 200, recomputed H1 diagrams, and recorded bottleneck distances. The p-value was (#{d_perm ≥ d_obs}+1)/(B+1).
6. Produced a single 2-panel summary figure (`front_iii_2d_tda_calibration.png`).
</methods> <results>
- Observed H1 diagram for ζ point cloud: 0 features.
- Observed H1 diagram for ζ_δ point cloud: 0 features.
- Observed bottleneck distance d(H1_ζ, H1_ζδ) = 0.0000.
- Permutation test (B=1000): permutation bottleneck distances ranged 0–0.00407 (median 0.0032, 929/1000 nonzero); 1000/1000 permutation distances were ≥ observed (0).
- Empirical p-value = (1000+1)/(1000+1) = 1.000.
- Contrast with r25: the standard 1D unfolded-spacing TDA pipeline gave p=1.0 — identical here.
- Structural reason for the negative result: in ζ_δ the 20 perturbed indices (1000–1019) are contiguous, so the perturbation produces a shifted line segment (an "elbow"), not a closed loop. The 0.1 real-part offset is also much smaller than the typical Im-axis spacing (median ≈ 1.11, max ≈ 2.51 in the slice), so the perturbed slab is geometrically isolated and forms no Rips cycles. Indeed, persistent H1 features only appear in permuted (interleaved) configurations, where the offset points fall in between Re=0.5 points and triangulate small loops.
</results> <challenges>
- `ripser` and `persim` were not pre-installed and had to be pip-installed at runtime.
- High-precision Unicode-stored zeros required float-casting for `ripser`; this is acceptable because Rips persistence is scale-equivariant and only depends on inter-point distances, but the precision used by ripser is float32 internally.
- The contiguous nature of the perturbed indices (a known property from the dataset description) is what causes both pipelines to be blind; this is a structural — not numerical — limitation.
- The naive raw 2D pipeline (as literally specified) is dominated by the Im-axis scale, so the (Re,Im) anisotropy effectively reduces to a 1D problem; a re-scaled or unit-cell-normalised variant would likely be required to recover H1 sensitivity.
</challenges> <discussion>
The r25 conjecture that adding the real coordinate would render Front III sensitive to ζ_δ is not supported by the literal "real-part-aware" 2D point-cloud pipeline. Two intrinsic features of the ζ_δ artifact defeat raw Vietoris–Rips H1: (i) the 20 perturbed real parts are contiguous in index, so the perturbation appears as a translated line segment with no enclosed area; (ii) the anisotropic scale (ΔRe = 0.1 vs ΔIm ≈ 1) makes the Re axis effectively negligible at the Rips scale needed to bridge Im neighbours. To make Front III actually sensitive to this specific perturbation, the pipeline must either (a) rescale axes to make ΔRe comparable to ΔIm, (b) use a sliding-window / time-delay embedding so that the contiguous shifted block introduces a cycle in feature space, or (c) compute persistence on a higher-dimensional embedding (e.g., (Re, Im, ΔIm, ΔRe)) where the discontinuity at the boundary of the perturbed block creates a topological signature. This is an important calibration: even "more information" does not automatically translate to TDA sensitivity unless the topology is engineered to be perturbation-aware.
</discussion> <proposed-next-hypotheses>
1. A normalized 2D pipeline that rescales the Im axis to match the Re axis (e.g., divides Im by the median Im spacing) will produce a non-empty H1 diagram for ζ_δ whose H1 bottleneck distance from ζ is significant (permutation p<0.05).
2. A time-delay / sliding-window embedding of the sequence Re(ρ_n) (window size 5–25) will yield an H1 persistence diagram that is significantly different between ζ and ζ_δ (permutation p<0.05), because the discontinuities at indices 999→1000 and 1019→1020 create a closed loop in the delay embedding.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>front_iii_2d_tda_calibration.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure (vertical layout). Panel A shows the 2D (Re,Im) point clouds for ζ (Re=0.5, blue) and the ζ_δ perturbed slab (Re=0.6, red, indices 1000–1019) over the perturbation region (zeros 900–1100). Panel B reports the H1 persistence-diagram comparison: both H1 diagrams are empty, bottleneck distance = 0.0, and permutation test (B=1000) p = 1.000 — matching the r25 standard-pipeline blindness.</artifact-description>
</artifact>
</artifacts>
</output>
