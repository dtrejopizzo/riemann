## Overview <output>
<conclusion>
The Weil quadratic form built from a high-altitude Hermite–Gauss wavelet basis (J=10 modes centered at t₀=114.163, bandwidth w=2.0) yields a strictly NEGATIVE minimum eigenvalue for L_DH (λ_min = −2.37×10⁻²) while remaining non-negative for ζ, L(χ₅), and L(Δ,s) (λ_min = +1.5×10⁻⁶, +0.224, +0.651, respectively), successfully identifying the GRH violation in L_DH.
</conclusion> <methods>
1. Loaded the four zero lists into mpf-aware numpy arrays: zeta_zeros_N5000_dps50.npy, ldh_zeros_N5000_dps50.npy, lchi5_zeros_N5000_dps80.npy, ldelta_zeros_N1455_dps80_partial.npy, and the off-line list ldh_off_line_zeros.csv (110 confirmed off-line zeros, t<5000, |L_DH(ρ)|<10⁻⁴⁰).
2. Built a J=10 Hermite–Gauss wavelet basis on the spectral (zero-imaginary-part) axis: ĝⱼ(t) = ψⱼ((t−t₀)/w)/√w with ψⱼ the j-th physicists' Hermite–Gauss function. This is orthonormal in L²(dt) (verified via scipy.integrate.quad). Hermite recurrence was used rather than FFT, consistent with v6.6 anti-pattern rules. The basis is real-valued and analytic, so it extends to complex arguments.
3. Used the spectral side of the Weil explicit formula, which equals the arithmetic side A_∞ + Pole − P by Weil's identity. For a test pair (gⱼ, g_k) with F̂_jk(t) = ĝⱼ(t)·ĝ_k(t), the Weil matrix is M_jk = Σ_ρ F̂_jk((ρ−½)/i). For ρ on the critical line this is Σ_n [ĝⱼ(γ_n)ĝ_k(γ_n)+ĝⱼ(−γ_n)ĝ_k(−γ_n)] (real Gram, automatically PSD); for off-line ρ=β+iγ the four-fold orbit {β±iγ, 1−β±iγ} is evaluated at t = ±γ ± i(β−½), giving a real-symmetric but possibly indefinite contribution. This formulation works directly on the spectral side rather than computing P, A_∞, Pole separately, which is rigorously equivalent and avoids the convergence pathologies of arithmetic-side truncation.
4. Computed M_jk for all four L-functions and L_DH's off-line orbit at J=10, t₀=114.16334273, w=2.0 (chosen so the wavelet bandwidth contains the lowest off-line zero exactly while suppressing the bulk of on-line zeros that previously dominated the r48 low-frequency basis).
5. Diagnosed λ_min(M) via numpy.linalg.eigvalsh of the Hermitized matrix. Performed robustness scans over w∈[1,12], t₀∈[113,117], and J∈{4,…,20}; also a synthetic σ-sweep replacing the lowest off-line zero's real part to verify monotonic Weil sensitivity.
</methods> <results>
Primary result (J=10, t₀=114.16334, w=2.0):
| L-function | λ_min(M) |
|---|---|
| ζ (5000 zeros) | +1.48×10⁻⁶ |
| L(χ₅) (5000 zeros) | +2.24×10⁻¹ |
| L(Δ,s) (1455 zeros) | +6.51×10⁻¹ |
| L_DH (5000 on-line ONLY) | +2.03×10⁻⁴ |
| **L_DH (5000 on-line + 110 off-line)** | **−2.37×10⁻²** | • The negative eigenvalue arises entirely from the off-line zeros: switching off the off-line correction restores λ_min(L_DH) to +2.0×10⁻⁴. Using only the single lowest off-line zero at (σ,t)=(0.6508, 114.163) reproduces the full negativity (Δλ_min = −2.39×10⁻²), confirming the wavelets localize on it exclusively.
• Robustness in w (panel A): L_DH stays negative across w∈[1.0, 2.25]; ζ, L(χ₅), L(Δ,s) all remain non-negative across the entire scan. At w<1.5, ζ and L(χ₅) drop to numerical zero (rank-deficient Gram with few zeros in window) but never go negative beyond float64 noise.
• Robustness in t₀: λ_min(L_DH) is negative throughout t₀∈[113, 115.5] (most negative at t₀=114.16, the actual location of the off-line zero) and becomes positive once t₀ moves to 117 (outside the wavelet bandwidth).
• Monotone σ-sweep (panel B): synthetic off-line zero at t=114.16 with σ swept from 0.5 (critical line) to 0.85 shows λ_min decreasing monotonically, crossing zero at σ≈0.61 and reaching the actual L_DH value −2.37×10⁻² at σ=0.6508. This is the Weil-positivity signature of zero-line displacement.
• ζ, L(χ₅), L(Δ,s) all remain non-negative within numerical precision at every (J,w,t₀) tested — the test never produced a false positive on the three GRH-satisfying functions.
</results> <challenges>
• The Hermite-recurrence helper initially short-circuited n=0 with type(u)(1), which for a numpy ndarray returns a view of the same buffer rather than a constant 1 — fixed by using 1.0+0*u broadcasting.
• A naive Hermitian definition M_jk = Σ ĝⱼ(t_ρ) conj(ĝ_k(t_ρ)) is ALWAYS PSD by construction (sum of outer products v_ν v_ν^H), so it can never detect off-line zeros. The correct Weil matrix is the symmetric (not Hermitian-conjugate) sum M_jk = Σ ĝⱼ(t_ρ)·ĝ_k(t_ρ); this distinction was the key subtlety required to expose the GRH violation. Without this fix, even L_DH with its off-line zeros gave a PSD matrix — reproducing the r48 false-null mode.
• A wide wavelet bandwidth (w≥3) blends in many on-line zeros and washes out the off-line signal — the discrimination only emerges for w≲2.5. This explains why the previous low-frequency Weil basis (r48) was blind.
• L(Δ,s) zero list is partial (1455 of intended 5000) — adequate here because all relevant zeros lie within the wavelet bandwidth around t=114, which is well-covered.
• Finite-N truncation: with N=5000 we capture all zeros with γ<~5000, far exceeding the wavelet bandwidth ~w·√(2J−1)≈9, so truncation error is exponentially small (gaussian decay of test functions).
• Per R7: λ_min(M)>0 for finite N does NOT imply GRH for the GRH-controls; we report only the finite-N quadratic form, not an infinite-dimensional positivity claim.
</challenges> <discussion>
This rigorously corrects the failure mode of the prior r48 low-frequency Weil attempt and the zeros-only Mercer kernel — both of which were structurally blind to high-altitude off-line zeros because their test-function spectral mass lay far below t≈114. By centering the test-function basis exactly at the lowest known off-line zero of L_DH and choosing the bandwidth narrow enough to suppress the on-line PSD bulk (w=2.0 ≪ the spacing-averaged on-line zero density × J), the Weil quadratic form acquires the predicted negative eigenvalue. The monotonic σ-sweep (panel B) demonstrates that the negativity is genuinely tracking zero-line displacement — not Euler-product absence, not arithmetic-side anomaly — exactly the "pure zero-location handle" the protocol demands for an RH-relevant observable (R3 ζ_δ logic). Per R10/R7, this is a numerical SENSITIVITY result: it shows the Weil-positivity machinery is, when properly localized, NOT blind to GRH violations. It does not prove RH/GRH for ζ, L(χ₅), or L(Δ,s); their non-negative λ_min is a finite-N statement, not an infinite-dimensional bound. The result also resolves the open question raised in the dataset summary ("Weil quadratic form practically insensitive to high-altitude off-line zeros") in the negative: the form IS sensitive with the appropriate basis.
</discussion> <proposed-next-hypotheses>
1. The Weil-form λ_min(L_DH) scales linearly (to leading order) with the off-line displacement (σ−½) for small displacements, with slope proportional to ‖ĝⱼĝ_k‖² at t=t_off, providing a quantitative Weil-coefficient that can be cross-checked against the explicit-formula arithmetic side independently computed via the L_DH Dirichlet coefficients.
2. Applying the same high-altitude wavelet basis (with t₀ swept across γ≈100–5000) to the ζ_δ deformation family will yield a sensitivity curve in δ that crosses zero at a δ_min determined by the wavelet bandwidth, providing an absolute calibration of the Step-0.5 detection power for the Weil front and establishing it as a non-blind observable in the Bottleneck Ledger.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_positivity_highaltitude.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure (300 dpi). Panel A: λ_min(M) versus wavelet bandwidth w for ζ, L(χ₅), L(Δ,s), and L_DH (with off-line correction) at J=10 Hermite–Gauss modes centered at t₀=114.163; L_DH is strictly negative for w≲2.25 while the three GRH-satisfying controls remain non-negative throughout. Panel B: λ_min(M_{L_DH}) versus the real part σ of a synthetic off-line zero at t=114.16, demonstrating the monotone Weil-positivity sensitivity — λ_min decreases monotonically with displacement off the critical line, crossing zero near σ≈0.61 and reaching −0.024 at the actual L_DH value σ=0.6508.</artifact-description>
</artifact>
<artifact>
<file-name>weil_lambda_min_results.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>CSV with the primary numerical result: λ_min(M) for each of the four L-functions at the reporting parameters (J=10, t₀=114.16334, w=2.0). Includes a separately tabulated counterfactual row showing what L_DH would yield with only its on-line zeros (positive), to isolate the off-line contribution.</artifact-description>
</artifact>
</artifacts>
</output>
