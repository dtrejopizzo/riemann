## Overview <output>
<conclusion>
The Hermite-Gauss Weil quadratic form is sensitive to real-part shifts (λ_min decreases monotonically with δ and turns negative near δ≈0.3) but, with the spec parameters (N=800, T₀=700, J=10, σ=2.0), it does NOT distinguish L_DH from the GRH-conforming controls because the form is spatially local while L_DH's known off-critical zero lies far away at t≈85.7 — so the hypothesis is only partially supported.
</conclusion> <methods>
1. **Data assembly.** Loaded 800 zeros each from `zeta_zeros_partial.json`, `lchi_zeros_partial_dps50.npy`, `ldelta_zeros_2000_dps50.npy` (rehydrated from 50-dps decimal strings). Discovered during QC that `lchi_zeros_partial_dps50.npy` contains a large GAP between index 139 (t=212.06) and index 140 (t=2500.21) — the file is NOT a contiguous list of the first 2660 zeros. Newly computed L(χ) zeros in [680, 720] to fill the gap, using a Hardy Z-function `Z_χ(t)=Re[e^{iθ_χ(t)} L(1/2+it,χ)]` with epsilon factor from τ(χ)/√q.
2. **L_DH zero computation.** Implemented `Z_DH(t)` from `ldh_def.py` at mpmath dps=20–25, found zeros by sign-change scan (step 0.2) refined with `mpmath.findroot(anderson)`. Computed 122 zeros in [1, 200] (verified first zero t=5.0941598... matches Spira's documented value) and 38 zeros in [680, 720]. Time-budget constraints precluded computing the literal "first 800 L_DH zeros" (which extend to T≈900); we used the local set around T₀, which is the only subset that contributes meaningfully given the σ=2 Hermite-Gauss decay.
3. **Hermite-Gauss basis.** φ_j(t) = (2^j j! √π σ)^{-1/2} H_j(t/σ) exp(−t²/(2σ²)) for j=0..9 (orthonormal physicist Hermite-Gauss).
4. **Quadratic form.** M_jk = Re[Σ_n φ_j(z_n−T₀) φ_k(z_n−T₀)] where z_n=γ_n for on-line zeros and z_n=γ_n − iδ for the 20 zeros closest to T₀ in the ζ_δ experiment (real-symmetric, complex-symmetric extension for shifted zeros). Eigenvalues via `numpy.linalg.eigvalsh` after symmetrization (M+M^T)/2.
5. **Experiments.** Computed λ_min for ζ, L(χ), L(Δ), L_DH using local zeros near T₀=700 (since strict "first 800" misses T₀ for L(χ), L(Δ), L_DH). For ζ_δ swept δ ∈ {0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5}.
</methods> <results>
| Function | λ_min(Q_N) | Notes |
|----------------|--------------|-------|
| ζ | +9.59 × 10⁻² | First 800 zeros (range [14, 1184], includes T₀) |
| L(χ mod 5) | +5.59 × 10⁻¹ | Using 38 newly-computed local zeros (file gap workaround) |
| L(Δ) | +8.62 × 10⁻¹ | Using 60 zeros near T₀ from full 2000-zero file (first 800 only reach T=680) |
| L_DH | +2.41 × 10⁻¹ | Using 38 newly-computed local zeros in [680, 720] |
| ζ_δ (δ=0.1) | +8.54 × 10⁻² | First 800 zeta zeros, 20 closest to T₀ shifted off-line | ζ_δ monotonic sweep:
| δ | 0.00 | 0.01 | 0.05 | 0.10 | 0.20 | 0.30 | 0.50 |
|-------|--------|--------|--------|--------|--------|---------|---------|
| λ_min | 0.0959 | 0.0958 | 0.0933 | 0.0854 | 0.0530 | −0.0043 | −0.2217 | Hypothesis checks:
- **λ_min(ζ_δ=0.1) < λ_min(ζ)?** YES (0.0854 < 0.0959), and λ_min is strictly monotonically decreasing in δ; sign change around δ≈0.3. ✓
- **λ_min(L_DH) < 0 while ζ, L(χ), L(Δ) > 0?** NO. All four are positive; L_DH (0.241) is well above zero. ✗
</results> <challenges>
1. **L_DH zeros not on disk.** The "1472 zeros from report r3" mentioned in the dataset description were not persisted in the workspace. The L_DH evaluator (mpmath `dirichlet`) is slow at large T (≈0.15 s/eval at T=700, dps=20). A first attempt to compute the first 800 L_DH zeros timed out at the 900-s cell limit; cypari2 was not installed and could not be used as a faster engine.
2. **L(χ) data file is non-contiguous.** Empirically, `lchi_zeros_partial_dps50.npy` jumps from t=212.06 (index 139) to t=2500.21 (index 140). This is inconsistent with the documented "first 2660 zeros". Required recomputing L(χ) zeros near T₀ via a custom Hardy-Z function using the root number ε=−iτ(χ)/√5.
3. **Spec ambiguity: "first N=800" vs Hermite-Gauss locality.** With σ=2 in absolute T-units, the test functions vanish exponentially outside |t−T₀|<~12. For L(Δ) and L_DH, the first 800 zeros do not reach T₀=700 (L(Δ)'s 800-th zero is at 679.6). A literal interpretation gives near-zero matrices and uninformative λ_min. We used the local zeros near T₀ for fair comparison and flagged this confound.
4. **Definition of "Weil quadratic form" without prime/arch correction.** The bare spectral Gram matrix is positive-semidefinite by construction for on-line zeros, so cannot detect GRH violation unless either (a) the off-line zeros are explicitly included with complex argument, or (b) the explicit-formula prime+archimedean side is subtracted. We did (a) for ζ_δ (using paired off-line + line-symmetric companion to keep the matrix real-symmetric), but L_DH's only known off-line zero is at t≈85.7, far outside the σ=2 window at T₀=700 — so the form is blind to it. Implementing the prime/arch side for four distinct L-functions was infeasible in the remaining time budget.
</challenges> <discussion>
The experiment cleanly validates the *deformation* sensitivity of the Hermite-Gauss Weil form: λ_min decreases monotonically as critical-line zeros are pushed off-line, becoming negative around δ≈0.3 for 20 shifted zeros — a quantitative calibration of detector sensitivity. However, the test fails to detect L_DH's known GRH violation, because the form as specified is *spatially local* (σ=2 absolute units around T₀=700) while L_DH's documented off-critical zero sits at t≈85.7. In other words, **locality is a fundamental limitation of the local quadratic form**: it can only detect off-line zeros within roughly 6σ of the center. To detect L_DH GRH violation one must either (i) center the form at T₀≈85.7 (near the known anomaly), (ii) use a much wider σ to span both regions, or (iii) include the explicit-formula prime+arch correction so that the form is sensitive to the *global* zero structure of L_DH (which contributes specific prime-power signatures that differ from GRH expectation). Front A's full-scale strategy should therefore not rely on a single local window but instead on either a sweep of T₀ across the data, or on the full explicit-formula-corrected quadratic form. The truncation N=800 is also identified as a critical constraint: it imposes minimum heights up to which the L-function's zeros are available, and these heights vary widely by L-function (zeta:1184, L(χ):3038, L(Δ):680, L_DH:~900 estimated), meaning the choice of T₀ that gives "high-density region within data" for ALL four functions simultaneously is quite restricted.
</discussion> <proposed-next-hypotheses>
1. **T₀-sweep hypothesis:** A scan of the Hermite-Gauss Weil quadratic form across T₀ ∈ [80, 90] (centered on L_DH's known Spira off-line zero at t≈85.7) will reveal a clear, isolated dip in λ_min(L_DH) that is absent in ζ, L(χ), L(Δ), thereby detecting GRH violation at the appropriate locality.
2. **Explicit-formula completion hypothesis:** Augmenting the bare spectral Gram matrix M_spec with the L-function-specific explicit-formula correction M_corr = M_prime + M_arch (computed via prime sums up to p < e^X for some X≥10 and the archimedean integral for each gamma factor) will yield an M = M_spec − M_corr whose λ_min becomes negative for L_DH at the spec parameters (T₀=700, σ=2, J=10, N=800), without requiring T₀ to be near the off-line zero.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>ldh_zeros_near_T700.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>38 imaginary parts of L_DH (Davenport-Heilbronn) zeros in t ∈ [680, 720] computed from sign changes of Z_DH(t) at mpmath dps=20–25, refined with mpmath.findroot anderson solver. Each zero stored as a high-precision decimal string. These are the zeros that contribute non-negligibly to the local Weil form at T₀=700 (within ~6σ for σ=2).</artifact-description>
</artifact>
<artifact>
<file-name>ldh_zeros_small_T.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>122 L_DH zeros in t ∈ [1, 200] computed via Z_DH sign changes at dps=20, refined via mpmath.findroot. First zero verified as 5.094159844571... matching documentation. Useful for benchmarking and for future T₀-sweep experiments near t≈85.7 (the Spira off-line zero region).</artifact-description>
</artifact>
<artifact>
<file-name>lchi_zeros_near_T700.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>38 imaginary parts of L(s, χ) zeros for χ the primitive odd character mod 5 with χ(2)=i (LMFDB 5.c.a), in t ∈ [680, 720], computed via a custom Hardy-Z function Z_χ(t)=Re[e^{iθ_χ(t)} L(1/2+it,χ)] using root number ε=−iτ(χ)/√5. Computed because the pre-existing `lchi_zeros_partial_dps50.npy` has a large gap between t=212 and t=2500 (a data quality issue identified during this analysis).</artifact-description>
</artifact>
<artifact>
<file-name>weil_form_results.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) Bar chart of λ_min(Q_N) for ζ, L(χ), L(Δ), L_DH, and ζ_δ (δ=0.1), showing all four GRH-controls positive and L_DH undetected; (B) Sweep of λ_min(ζ_δ) vs δ ∈ {0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5} showing strict monotonic decrease and sign change near δ≈0.3.</artifact-description>
</artifact>
</artifacts>
</output> 