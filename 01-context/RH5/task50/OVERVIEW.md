## Overview <output>
<conclusion>
Injecting m=10 off-line zeros (Re=½+0.1) into the N=5000 ζ-zero list produces a small but nonzero bottleneck distance of 5.76×10⁻³ between the H1 persistence diagrams, but creates NO new long-lived features — the perturbation only induces low-lifetime shifts consistent with the persistence stability theorem.
</conclusion> <methods>
1. **Zero list acquisition (R2 gate).** Downloaded Odlyzko's `zeros1` table (10⁵ zeros, ~9-dp precision). R2 validation: γ₁=14.134725142 (diff 1×10⁻⁹), γ₂=21.022039639 (diff 0), γ₃=25.010857580 (diff 0). Passed to the precision of the table; cached the first N=5000 values as `zeta_zeros_N5000.npy`. (Note: the dataset spec explicitly permits Odlyzko tables with ~9-dp precision in lieu of mpmath dps=50, which would be computationally prohibitive.)
2. **One-sided deformation (R3/r3).** Selected m=10 indices evenly spaced in [100, N−100] (deterministic, reproducible). Encoded zeros as complex points ρ_n = ½ + iγ_n; for the perturbed list, replaced the chosen ρ_k by (½+δ) + iγ_k with δ=0.1, leaving the rest on the line (no mirror across ½, avoiding artificial cancellations).
3. **Unfolding and point cloud.** Riemann–von Mangoldt smooth unfolding u_n = (γ_n/2π) log(γ_n/2π) − γ_n/2π + 7/8 (mean spacing ≈ 1). Built 3-D delay-embedding point cloud P_n = (s_n, s_{n+1}, r_n) where s_n = u_{n+1}−u_n and r_n = Re(ρ_n)−½. Original lives in the plane r=0; perturbed has 10 points lifted to r=0.1.
4. **Persistence.** Vietoris–Rips via `ripser` (maxdim=1, thresh=2.0) on both clouds (~26 s each). Bottleneck distance via `persim.bottleneck` (~62 s).
5. **Comparison.** Tabulated top-10 lifetimes, median lifetimes, and per-feature nearest-neighbour L∞ distances between the two diagrams.
</methods> <results>
- N=5000 points per cloud; H1 generators: 1381 (original) vs 1379 (perturbed).
- Maximum H1 lifetime is **identical** between diagrams: 0.05525. The 10 longest lifetimes agree to ≤10⁻⁵ for the first 9 (e.g., 0.05130, 0.04956, 0.04721, 0.04670, 0.04509, 0.04398, 0.04171, 0.04086 in both); differ only at the 10th feature (0.04046 vs 0.04025).
- Median lifetimes: 4.147×10⁻³ (orig) vs 4.153×10⁻³ (pert) — indistinguishable.
- **Bottleneck distance d_B(H1_orig, H1_pert) = 5.759×10⁻³.**
- Per-feature nearest-neighbour L∞ distances: max(orig→pert)=5.12×10⁻³, max(pert→orig)=3.93×10⁻³. The most-shifted features have low lifetime (≤0.04), well below the high-persistence regime.
- Stability bound: by the persistence stability theorem, d_B ≤ d_H(point clouds) ≤ δ = 0.1; the observed 5.8×10⁻³ ≪ 0.1, consistent with theory.
- **No new high-persistence feature** is present in the perturbed diagram. The top features in the two diagrams coincide point-for-point.
</results> <challenges>
- Generating N=5000 zeros at dps=50 *de novo* via `mpmath.zetazero` would have taken many hours; per Rule R8 of the spec, using a validated Odlyzko table is the sanctioned alternative. Its ~9-dp precision is lower than the dps=50 target but more than sufficient for TDA at δ=0.1.
- No prior pipeline existed in the workspace, so the "unfolding + point cloud" had to be specified canonically: smooth-unfolded spacings as a 2-step delay embedding plus a real-part-deviation axis. Other natural choices (e.g., higher-dim delay, pure (Re, Im_unf) embedding) might give different absolute bottleneck values, but the *qualitative* conclusion (no new long-lived features under m=10 off-line zeros) follows from a simple counting argument: 10 isolated points lifted by 0.1 in an otherwise-flat r=0 cloud cannot form a 1-cycle with high persistence in 3-D.
- `ripser` memory/time scales steeply with N; thresh=2.0 (twice mean spacing) keeps the H1 computation tractable while capturing the long-lived regime.
</challenges> <discussion>
The hypothesis has two parts: (i) **new long-lived H1 features appear** in the perturbed diagram, and (ii) **bottleneck distance is significantly greater than zero**. Part (ii) is technically supported (d_B = 5.76×10⁻³ > 0), but part (i) is **not** supported: the top-10 long-lived features are essentially identical between the two diagrams, and the most-displaced features in the bottleneck matching are low-lifetime (close-to-diagonal) points. The bottleneck distance is driven by diffuse, near-diagonal noise — exactly what the persistence stability theorem predicts for a 10-point, δ=0.1 perturbation of a 5000-point cloud. This is consistent with the prompt's prior expectation (Front III: "H1 typically vanishes after unfolding [and] is expected to be negative — cap it hard") and with Step 0.5's framing: the H1 invariant has **low detection power** against a small, sparse off-line injection. By R10 ("sensitivity vs relevance"), this observable should be flagged a **blind/uninformative** indicator for m=10, δ=0.1; any null result of an L_DH-vs-ζ comparison using H1 at these scales must not be interpreted as evidence for RH. The result is a clean negative Front III finding: ten off-line zeros at δ=0.1 perturb H1 only at the noise floor (sub-percent of the longest-lived feature), and do not generate any new persistent loops.
</discussion> <proposed-next-hypotheses>
1. **Threshold hypothesis.** Increasing the injected fraction (m ∈ {50, 200, 500} at δ=0.1) and/or the displacement (δ ∈ {0.1, 0.2, 0.3} at m=10) will eventually create at least one new H1 feature with lifetime above the bulk distribution, defining a minimum-detectable (m, δ) curve for H1 sensitivity.
2. **Discriminating-power hypothesis.** Replacing the H1 invariant by a *weighted persistence functional* of H0 (which directly measures point density) will yield bottleneck distances scaling linearly with mδ — i.e., H0 is non-blind to off-line injection where H1 is blind — providing a usable Step-0.5 power table for Front III.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>odlyzko_zeros1.txt</file-name>
<artifact-type>external_source</artifact-type>
<artifact-description>Odlyzko's precomputed list of the first 10⁵ non-trivial ζ zeros' imaginary parts to ~9 decimal places (https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1). Downloaded directly; passed the R2 validation gate to the precision of the table (|γ₁ − ref| = 1×10⁻⁹).</artifact-description>
</artifact>
<artifact>
<file-name>zeta_zeros_N5000.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>First N=5000 ζ-zero imaginary parts extracted from the Odlyzko table, cached as a NumPy array (float64). Used as the canonical input for both the original and the off-line-injected analyses.</artifact-description>
</artifact>
<artifact>
<file-name>H1_diagrams_zeta_injection.npz</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy archive containing the H1 persistence diagrams for the original and perturbed (m=10, δ=0.1) zero lists, the injection indices, and the computed bottleneck distance (5.759×10⁻³). Generated by Vietoris–Rips persistence (`ripser`, maxdim=1, thresh=2.0) on a 3-D delay embedding of unfolded spacings augmented with Re(ρ)−½.</artifact-description>
</artifact>
<artifact>
<file-name>H1_persistence_zeta_offline_injection.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>300-dpi summary figure: overlaid H1 persistence diagrams for the original ζ zeros (N=5000) and the m=10/δ=0.1 off-line-perturbed list, with the bottleneck distance and maximum lifetimes annotated. Top-persistence features coincide; bottleneck displacement is small and confined to low-lifetime, near-diagonal points.</artifact-description>
</artifact>
</artifacts>
</output>
