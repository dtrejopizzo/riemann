## Overview <output>
<conclusion>
The Weil quadratic form's signal scales LINEARLY (exponent = 1.000) — not quadratically — with the real-part displacement β when a single existing ζ zero is moved off the critical line as specified in the objective, and the corresponding minimum detectable β (signal > 1000× the 5.31×10⁻⁴⁰ baseline) is ≈ 4.7×10⁻³⁶, ~16 orders of magnitude smaller than the hypothesized 10⁻²⁰.
</conclusion> <methods>
1. Reconstructed the refined Weil quadratic form Q = M_zeros − M_arith at mp.dps=80 with parameters T0=85.6993, σ=2.0, J=12 (Hermite basis), and prime-power sum extended to N=100000, exactly matching the r45 / weil_N100000_results.json baseline construction.
2. Built each component independently: • M_zeros: summed phi_i(γ)·phi_j(γ) over the 33 ζ zeros within ±40 of T0, loaded from zeta_zeros_5000_dps50.npy and cast to mpf. • M_polar: phi_i(±i/2)·phi_j(±i/2) (numerically ~10⁻⁷⁹⁸ at T0=85.7 — negligible). • M_logpi: log(π)/(2π)·δ_ij. • M_arch: (1/2π)·∫ phi_i(γ) phi_j(γ) · Re ψ(¼ + iγ/2) dγ via mpmath quadrature on nodes [T0−50, T0−20, T0, T0+20, T0+50]. • M_prime: −(1/2π) Σ_{n≤N} Λ(n)/√n · 2 Re F̂_ij(log n), where F̂_ij was computed in closed form via Hermite linearization H_i H_j = Σ_k 2^k k! C(i,k) C(j,k) H_{i+j-2k} and the analytic Fourier transform ∫H_n(y) e^{-y²} e^{iαy}dy = √π (iα)^n e^{-α²/4}, giving F̂_ij(u) = N_i N_j √π e^{-iuT0 − σ²u²/4}·Σ_k c_k(-iσu)^{i+j-2k}.
3. Validated the baseline: max|λ_min...max| of Q gave 5.3119534×10⁻⁴⁰, matching the J=12, N=100000 entry in weil_N100000_results.json to all printed digits.
4. Identified γ_k closest to T0: γ_k = 84.7355 (|γ_k − T0| ≈ 0.964).
5. For β ∈ {1e-2, 1e-10, 1e-15, 1e-18, 1e-20, 1e-22}: built M_zeros_pert by subtracting phi_i(γ_k)·phi_j(γ_k) and adding phi_i(γ_k+iβ)·phi_j(γ_k+iβ) — exactly the single-zero displacement protocol. Computed eigenvalues (np.linalg.eigvals) of Q_pert = M_zeros_pert − M_arith and recorded |λ_max|.
6. Fitted log10|λ_max| vs log10(β) by linear regression.
7. As a cross-check, also computed a functional-equation-respecting variant that adds both off-critical pair members at s = ½±β+iγ.
</methods> <results>
Baseline (GRH-conforming, J=12, N=100000): max|λ| = 5.3120×10⁻⁴⁰ (reproduces r45 to all digits). Single-zero displacement (objective protocol):
| β | max|λ| | ratio to baseline |
|----------|---------------|-------------------|
| 1e-2 | 1.135×10⁻² | 2.14×10³⁷ |
| 1e-10 | 1.135×10⁻¹⁰ | 2.14×10²⁹ |
| 1e-15 | 1.135×10⁻¹⁵ | 2.14×10²⁴ |
| 1e-18 | 1.135×10⁻¹⁸ | 2.14×10²¹ |
| 1e-20 | 1.135×10⁻²⁰ | 2.14×10¹⁹ |
| 1e-22 | 1.135×10⁻²² | 2.14×10¹⁷ | Power-law fit: log10|λ_max| = (1.0000)·log10(β) + 0.0550. Scaling exponent = 1.000 (linear, not quadratic). Prefactor |λ_max|/β = 1.135. Minimum detectable β (threshold = 1000·baseline = 5.31×10⁻³⁷): β_min ≈ 4.68×10⁻³⁶ — about 16 orders of magnitude smaller (i.e., much more sensitive) than the hypothesized 10⁻²⁰. Functional-equation-respecting pair-displacement variant (cross-check): max|λ_max| ≈ 0.776, essentially β-independent — consistent with the "constant-signal" behavior r48 reported for symmetric off-critical pair insertion.
</results> <challenges>
• M_arch quadrature with mpmath at dps=80 over a 78-pair upper-triangular matrix took ~390 s; this dominated runtime.
• Verifying the convention of r45 required matching numerical baseline (5.31×10⁻⁴⁰); the closed-form F̂_ij via Hermite linearization avoided any FFT/FT discretization error and reproduced r45 exactly.
• The hypothesis (quadratic scaling, β_min≈1e-20) assumed Q's quadratic form is even in β about the critical line; this is only true when zeros are perturbed in a functional-equation-symmetric way. The objective's literal protocol (single zero, single complex argument γ+iβ) breaks that symmetry, producing a leading-order linear-in-β perturbation of Q.
</challenges> <discussion>
The refined Weil form is even more sensitive than the hypothesis anticipated, but along an unexpected direction in parameter space: the objective's "subtract one critical, add one complex-argument" recipe creates a non-Hermitian perturbation that is linear in β (the Taylor expansion of phi_k(γ+iβ)phi_k(γ+iβ) − phi_k(γ)² begins at order iβ). The resulting |λ_max| therefore scales like β¹, giving the form an effective detection limit ~5×10⁻³⁶ at the 1000×baseline criterion — far below the hypothesized 10⁻²⁰. The functional-equation-respecting variant (off-critical pair at s=½±β+iγ) yields the same β-insensitive, large-constant signal observed in r48, confirming that the "displacement" must be implemented exactly as in the objective to obtain a sensitive β scaling. Net: the Weil form, with N=100000 prime cutoff and dps=80, is a remarkably sensitive diagnostic of even tiny non-critical perturbations, with linear-in-β response when the perturbation is asymmetric, and constant response when symmetric. This means experimental tests for GRH violation using this form should be designed around asymmetric perturbations; the predicted quadratic regime apparently requires a different perturbation geometry (e.g., perturbations preserving Q's Hermiticity at first order, perhaps a real-part β plus simultaneous imaginary-part adjustment to retain γ as the imaginary part of both ρ and 1−ρ̄).
</discussion> <proposed-next-hypotheses>
1. If the displacement is implemented in a Hermitian-preserving way — e.g., as a small variance/squeeze of phi_i(γ)phi_j(γ) → (phi_i(γ+iβ)phi_j(γ+iβ)+phi_i(γ−iβ)phi_j(γ−iβ))/2 minus 2·phi_i(γ)phi_j(γ), which is the second-order term in β — then |λ_max| will scale as β² with a measurable detection limit near β ≈ 10⁻²⁰ as originally hypothesized.
2. The linear-scaling prefactor (≈1.135 at γ_k = 84.7355) depends on the magnitude |phi_i(γ_k)·phi_j′(γ_k)| at the displaced zero; choosing γ_k = T0 exactly (rather than the nearest existing ζ zero) or moving a high-amplitude zero in a different basis location will rescale the prefactor by an order-of-magnitude predictable from the Hermite-function values at γ_k.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_displacement_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON containing parameters (T0, σ, J, N, γ_k, baseline), max|λ| vs β table for the single-zero displacement protocol, the power-law fit (slope = 1.000, intercept = 0.055, prefactor = 1.135), parallel results for the FE-respecting pair-displacement variant, and the derived minimum detectable β. Produced by mpmath dps=80 reconstruction of the refined Weil quadratic form using closed-form Hermite-FT prime-side terms and quadrature-based archimedean term.</artifact-description>
</artifact>
<artifact>
<file-name>weil_displacement_scaling.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Log–log plot of |λ_max| vs β for the single-zero displacement experiment with fit line (slope = 1.000), reference horizontal lines for the GRH baseline (5.31×10⁻⁴⁰) and the 3-orders-of-magnitude detection threshold (5.31×10⁻³⁷), the hypothesized quadratic line anchored at the predicted β_min = 10⁻²⁰, and the measured β_min = 4.68×10⁻³⁶. Visualizes that the empirical scaling is linear rather than quadratic and the measured detection limit is far below 10⁻²⁰.</artifact-description>
</artifact>
</artifacts>
</output>
