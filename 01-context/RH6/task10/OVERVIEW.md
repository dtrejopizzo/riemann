## Overview <output>
<conclusion>
At J=12 with the refined Weil form (N=10⁵), the signal from an artificial off-critical ζ-zero pair exceeds the GRH baseline (5.31×10⁻⁴⁰) by ~39 orders of magnitude for every tested β; the smallest β in the requested set, β=10⁻⁶, is therefore unambiguously detectable (and the form remains sensitive far below this).
</conclusion> <methods>
1. Reconstructed the Riemann–Weil quadratic form Q = M_zeros − M_arith at mp.dps=80 using mpmath, centered at T₀=85.6993 with σ=2 on an orthonormal Hermite basis φ_k(t)=(1/√σ)·ψ_k((t−T₀)/σ), where ψ_k is the normalized Hermite function (1/√(2ᵏk!√π)·H_k(x)·e^(−x²/2)). Loaded the 33 ζ-zeros from `zeta_zeros_5000_dps50.npy` lying in [T₀−40, T₀+40]. 2. Fixed J=12. 3. For β ∈ {10⁻², 10⁻³, 10⁻⁴, 10⁻⁵, 10⁻⁶}, formed the rank-2 anomaly matrix A_ij(β) = φ_i(T₀+iβ)·φ_j(T₀+iβ) + φ_i(T₀−iβ)·φ_j(T₀−iβ) (real symmetric since φ is real on ℝ). 4. Because |λ_max(Q_baseline)| = 5.31×10⁻⁴⁰ from `weil_N100000_results.json` (independently produced reference) is enormously smaller than |λ_max(A)| (~1.5), λ_max(Q_modified) ≈ λ_max(A) to machine precision; computed eigenvalues of A with `mpmath.eig`. 5. Validated the reconstruction by reproducing r45's documented anomaly value at β=0.3085 (J=12, N=10⁵): we obtain 1.8379186464 vs. reported 1.8379186463045816 — agreement to ~10 significant figures.
</methods> <results>
| β | max|λ(Q)| | ratio to baseline (5.31e-40) | log₁₀(ratio) |
|---------|-----------|------------------------------|--------------|
| 10⁻² | 1.52757 | 2.876×10³⁹ | 39.459 |
| 10⁻³ | 1.52728 | 2.875×10³⁹ | 39.459 |
| 10⁻⁴ | 1.52728 | 2.875×10³⁹ | 39.459 |
| 10⁻⁵ | 1.52728 | 2.875×10³⁹ | 39.459 |
| 10⁻⁶ | 1.52728 | 2.875×10³⁹ | 39.459 | Every requested β yields a signal ≥39 orders of magnitude above the GRH-conforming baseline — vastly exceeding the 3-order detection threshold. The smallest β in the requested set that is unambiguously detectable is therefore **β = 10⁻⁶** (and probing β as small as 10⁻⁵⁰ still gives the same ≈1.5272788336 limit, equal to the J=12 trace of φ(T₀)φ(T₀)ᵀ for a critical-line added pair).
</results> <challenges>
The principal subtlety is that as β→0 the anomaly does NOT vanish: an "artificial off-critical pair" is an ADDED zero pair in the explicit-formula sum, so even at β=0 it contributes 2·φ(T₀)φ(T₀)ᵀ — a finite nonzero rank-1 perturbation. This means the Weil form's "sensitivity to β" is dominated by the existence of the spurious pair itself rather than by its real-part offset; the β-dependence (visible only in the 4th–5th significant digit between β=10⁻² and 10⁻⁶) is the genuine displacement signature but is dwarfed by the always-present "added-zero" contribution. No computational issues; mpmath dps=80 is more than adequate.
</challenges> <discussion>
Within the framework of r45, the refined Weil form (N=10⁵) at J=12 is overwhelmingly sensitive: an artificial off-critical pair near T₀ produces signals 39 orders of magnitude above noise for any β down to 10⁻⁶ (and effectively down to numerical zero). However, this reflects the fact that the Weil quadratic form is fundamentally a detector of spectral *mismatches* between the zero sum and the arithmetic side — any spurious zero (critical or not) yields a large signal. The β-displacement itself produces only a perturbative shift (<0.02%) on top of this dominant "extra-zero" contribution at the heights tested here (β·log|T₀| ≪ 1). To convert this experiment into a strict GRH stress test, the protocol should compare *moving* a zero off the critical line (subtract critical contribution, add off-critical contribution) rather than *adding* an off-critical pair to an already-complete spectrum; that gives a signal genuinely O(β²) for small β.
</discussion> <proposed-next-hypotheses>
1. When the artificial perturbation is implemented as a *displacement* of an existing ζ zero (subtract its critical-line contribution, add an off-critical one) rather than an additive pair, the Weil-form signal at J=12, N=10⁵ scales as |λ_max| ∝ β² for small β, and the minimal detectable β (3-orders-of-magnitude criterion above the 5.31×10⁻⁴⁰ baseline) lies near β ≈ 10⁻²⁰.
2. The trace identity tr(A(β)) = 2·Σ_k|φ_k(T₀+iβ)|² grows as e^(β²/σ²) for small β, so increasing σ (window width) at fixed J should sharpen the β-dependence and recover a genuine power-law sensitivity curve.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_sensitivity_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON containing per-β maximum |eigenvalue|, ratio to the r45 GRH baseline (5.31e-40), log₁₀(ratio), and a 3-order-of-magnitude detectability flag for J=12, N=10⁵, T₀=85.6993, σ=2, mp.dps=80. Includes a validation entry showing our reconstruction reproduces r45's anomaly value at β=0.3085 (1.8379186464 vs. 1.8379186463). Computed via mpmath using the closed-form rank-2 anomaly matrix A_ij(β)=φ_i(T₀+iβ)φ_j(T₀+iβ)+φ_i(T₀−iβ)φ_j(T₀−iβ) and mpmath.eig.</artifact-description>
</artifact>
<artifact>
<file-name>weil_sensitivity_figure.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Log-log plot of |λ_max(Q)| versus β ∈ {10⁻²,…,10⁻⁶} at J=12, N=10⁵, showing the signal (~1.527) sitting ~39 orders of magnitude above the GRH baseline (5.31×10⁻⁴⁰) and the 3-order detectability threshold.</artifact-description>
</artifact>
</artifacts>
</output>
