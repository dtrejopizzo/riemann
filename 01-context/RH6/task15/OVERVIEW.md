## Overview <output>
<conclusion>
Increasing the basis dimension J sharply sharpens detection: |λ_min(Q)| for ζ_δ (δ=0.05 on the first 20 zeros) grows super-polynomially with J — by roughly 13 orders of magnitude from J=4 to J=20, with a global power-law exponent α≈17.9 — while |λ_min(Q)| for undeformed ζ remains at numerical-precision floor (≤8×10⁻¹¹ across all J), confirming the hypothesis.
</conclusion> <methods>
1. Re-implemented the Weil quadratic form Q = M_zeros − M_arith from `weil_sensitivity_map.json` (report r19) using the Gaussian-monomial basis h_i(t) = ((t−T0)/σ)^i · exp(−((t−T0)/σ)²/2), i=0…J−1, at the optimal point T0=46.1347, σ=1.0, with prime bound 1000 and half-window max(20, 6σ)=20.
2. M_arith = Σ_{p,k: p^k≤1000} (log p)/√(p^k) · [h(k log p)h(k log p)^T + h(−k log p)h(−k log p)^T].
3. M_zeros: for a zero at 1/2+β+iγ, the per-zero contribution is Re[v v^T] (no Hermitian conjugation in the outer product) with v = h(±γ − iβ), summing over the functional-equation pair (±γ). This formulation reproduces the published validation value λ_min(ζ_δ; J=10) = −0.5103 to ≈10⁻¹³ when β=0.05 and to machine precision when β=0.
4. Loaded `zeta_zeros_5000_dps50.npy`; restricted to zeros within 20 of T0 (12 zeros, indices 3–14, all within the "first 20" so all received the δ=0.05 real-part shift in ζ_δ).
5. Built ζ_δ by setting β_n = 0.05 for n=1..20 (β_n=0 otherwise); built ζ control with β_n=0.
6. Computed Q and its eigenvalues at J ∈ {4, 8, 12, 16, 20}. Used mpmath at dps=80 throughout (matrix construction and `mp.eig` based eigenvalue solve) because float64 lost λ_min for J≥16 due to lambda_max scaling like ((γ_max−T0)/σ)^(2J) (≈6.5×10¹⁵ at J=20) versus a target λ_min of order 10⁻⁸⁰ for the control.
7. Fit |λ_min(ζ_δ)| vs J using (a) power law log|λ_min|=α log J + c, (b) exponential log|λ_min|=aJ + b, (c) super-exponential log|λ_min|=a J log J + b. Reported local log-log slopes to capture the changing rate.
</methods> <results>
J-sweep of λ_min(Q) (mpmath dps=80; symmetric form): | J | λ_min(ζ) | λ_max(ζ) | λ_min(ζ_δ) | λ_max(ζ_δ) |
|----|---------------------|--------------|---------------------|--------------|
| 4 | +7.78×10⁻¹¹ | 1.90×10⁰ | −1.813×10⁻⁴ | 1.91×10⁰ |
| 8 | +1.12×10⁻⁷⁰ | 1.07×10³ | −1.138×10⁻² | 1.07×10³ |
| 12 | −9.26×10⁻⁸² | 6.75×10⁶ | −1.012×10¹ | 6.76×10⁶ |
| 16 | −8.74×10⁻⁸² | 1.42×10¹¹ | −5.546×10⁴ | 1.43×10¹¹ |
| 20 | −1.08×10⁻⁸⁰ | 6.56×10¹⁵ | −4.426×10⁹ | 6.51×10¹⁵ | - ζ_δ: |λ_min| grows by ≈2.4×10¹³ over the sweep (1.8×10⁻⁴ → 4.4×10⁹).
- Global log-log power-law fit: α ≈ 17.9, constant ≈ exp(−37.5). Fit is not uniform — local exponents are α≈6.0 (J=4→8), 16.8 (J=8→12), 29.9 (J=12→16), 50.6 (J=16→20), showing growth faster than any single power.
- Exponential fit log|λ_min|=1.93·J − 18.6 (local rate also grows from 1.04 to 2.82).
- Best simple model: super-exponential log|λ_min| ≈ 0.569·J·log J − 13.3.
- Control ζ: |λ_min| never exceeds 7.8×10⁻¹¹ and falls to ~10⁻⁸⁰ for J≥8 (limited by mpmath dps=80 floor). The separation between ζ_δ and ζ at J=20 is ≈89.6 orders of magnitude.
- Implementation validation: at J=10, our value λ_min(ζ_δ) = −0.510304260041… matches the JSON-recorded −0.510304260042 to ≈10⁻¹³.
</results> <challenges>
- The Weil-form construction in `weil_sensitivity_map.json` is not algebraically specified for off-line zeros. The naïve Hermitian construction v v^H (Re[h(γ−iβ) conj(h(γ−iβ))^T]) yields a PSD form even with δ≠0 and reproduces λ_min ≈ 10⁻¹² rather than the published −0.51. The correct construction is non-Hermitian, taking Re[v v^T] (no conjugation), which is precisely what subtracts an Im(v)·Im(v)^T positive contribution and admits negative eigenvalues. This convention was inferred by matching the published J=10 validation value to ~10⁻¹³.
- Float64 eigenvalue solves became unreliable for J≥16 because λ_max grows like ((γ_max−T0)/σ)^(2J)≈6×10¹⁵ at J=20; relative roundoff of ~10⁻¹⁶ then masks any true λ_min below ~1. Switching the matrix construction and eigenvalue computation to mpmath (dps=80) cured this for ζ_δ (real signal ≫ precision floor) and exposed that the ζ control λ_min was being limited by the mpmath precision floor, not by any genuine off-line structure.
- A clean closed-form power law does not describe the J-scaling; reporting requires either a wide-range power-law exponent (α≈17.9 with poor R²) or a super-exponential fit. We provide both for clarity.
- M_arith is essentially zero at T0=46.13 (prime support k·log p ≤ ~6.9 lies ~40σ from the test-function center, so h is exponentially small), so the form is dominated by the zero side; this is consistent with notes in `weil_sensitivity_map.json`.
</challenges> <discussion>
The result directly confirms the hypothesis posed for r19: at a fixed sensitive (T0,σ), enlarging the basis dimension J — i.e. enriching the local test-function space — provides a strictly more powerful detector of a real-part deformation while not generating spurious negativity on the GRH-conforming function. The growth is, empirically, faster than any single power law (locally α rises from ~6 to ~50 between J=4 and J=20) and is well captured by a super-exponential model log|λ_min|≈0.57·J log J. Interpreted in the explicit-formula picture, the basis dimension acts as a resolution proxy: each additional moment of the local test-function family adds a higher-order derivative of the deformation phase (e^{−iβ(t−T0)}) into Re[h(γ−iβ)h(γ−iβ)^T], producing rapidly larger violations of the Weil inequality. This shows that in this localized regime the Weil bound is, to numerical precision, saturated by ζ (no false positives even at J=20) but is decisively violated by ζ_δ. The same construction is therefore a sharp witness for the critical-line property in the small-window sense. Importantly, J cannot literally be sent to ∞ at fixed numerical precision: the rapidly growing λ_max (J=20 → 6.6×10¹⁵) imposes a finite precision budget; uniform control as J→∞ would require an a priori bound on the operator-norm-normalized λ_min, which our data does not provide.
</discussion> <proposed-next-hypotheses>
1. The super-exponential growth log|λ_min(ζ_δ)| ∝ J log J reflects a factorial-like saturation of moment matching against the perturbation phase e^{−iβ(t−T0)}; specifically, |λ_min| is controlled by the truncated Taylor expansion of the perturbation factor and should satisfy |λ_min(ζ_δ; J)| ≈ C · β^(2J) · (constant)^J · J! up to a normalization, testable by sweeping δ and checking that |λ_min(J)|^(1/J)/J approaches a δ-linear constant.
2. At the same (T0,σ) but with the L_DH off-critical Spira anomaly (T0≈85.7, σ=2, where the real-shift is ≈0.5), the J-sweep should also exhibit super-polynomial growth of |λ_min| with J, with a J-scaling exponent that quantitatively encodes the local off-line deviation magnitude — providing a non-parametric estimator of the Spira-zero real part from the spectrum of Q.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_J_sweep_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON record of the Weil-form J-sweep at (T0=46.13, σ=1.0, prime bound=1000). Contains parameters, the inferred M_zeros convention (Re[v v^T], non-Hermitian), the eigenvalue table (λ_min, λ_max) for ζ and ζ_δ at J∈{4,8,12,16,20}, three candidate fits (power-law α≈17.9, exponential a≈1.93, super-exponential a≈0.57 J log J), local log-log slopes, and a cross-check against the published J=10 validation value. Computed at mpmath dps=80 for stability.</artifact-description>
</artifact>
<artifact>
<file-name>weil_J_sweep.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Summary figure: semi-log plot of |λ_min(Q)| vs basis dimension J for ζ_δ (δ=0.05, first 20 zeros) and the GRH-conforming ζ control, with the global power-law fit overlaid (J^17.9). Annotated separation of ~90 orders of magnitude at J=20.</artifact-description>
</artifact>
</artifacts>
</output> 