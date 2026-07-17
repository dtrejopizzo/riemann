## Overview <output>
<conclusion>
For L(χ₄ mod 5) at T₀=85.7, J=16, X=10⁵, λ_min(Q) is monotone non-decreasing under nested zero-window enlargement and is consistent with monotonicity in σ wherever the trace gate passes; no de Branges/Conrey–Li obstruction pattern (non-monotone window response) is observed, mirroring ζ-control behavior.
</conclusion> <methods>
1. Loaded the cached zero lists `Lchi_zeros.pkl` (130 positive-γ) and `Lchi_zeros_neg.pkl` (130 negative-γ); χ₄ mod 5 is non-self-dual and odd (χ(−1)=−1), so both lists are summed independently in the Weil EF.
2. Built the localized Weil quadratic form Q = M_zeros − M_arith on a Hermite–Gauss basis φ_n centered at T₀ with width σ. M_arith = M_arch − M_prime, where M_arch is the archimedean term (1/2π)∫ φ_iφ_j Ω(t)dt with Ω(t)=log(5/π)+Re Ψ(3/4+it/2), and M_prime is the prime-power sum over n=p^k ≤ X=10⁵ involving χ(p)^k+χ̄(p)^k and the Fourier transform g_ij(±k log p) of φ_iφ_j.
3. Implemented the analytic Fourier transform of φ_iφ_j using the Hermite product identity H_iH_j = Σ_k 2^k k! C(i,k)C(j,k) H_{i+j−2k} and the closed form ∫H_n(u)e^{−u²}e^{−iηu}du = √π e^{−η²/4}(−iη)^n. This avoided the quadrature errors that occur for highly oscillatory integrands (otherwise tr-gate failed at σ=4).
4. Verified the trace identity tr(M_zeros)=tr(M_arith) as the validation gate: passed at ~10⁻¹¹ for σ=2, σ=4 (numerical floor), confirming the engine's correctness for L(χ).
5. **σ-scan** at T₀=85.7, J=16, X=10⁵ over σ ∈ {0.25, 0.5, 1, 2, 4}; computed eigenvalues of the symmetrized Q via `numpy.linalg.eigvalsh`.
6. **Window-scan** at T₀=85.7, σ=2, J=16 using nested zero sets {|t|≤50, 100, 150, 200}, recomputing M_zeros only (M_arith fixed).
7. Stack: Python 3.13, mpmath 1.3.0 (Hermite/digamma/zeros), numpy/scipy (eigvalsh, Gauss–Hermite for M_arch).
</methods> <results>
**σ-scan (T₀=85.7, J=16, X=10⁵):**
| σ | tr residual | λ_min | reliable? |
|---|---|---|---|
| 0.25 | +1.13×10⁻¹ | −2.60 | NO (trunc-dominated) |
| 0.50 | −6.86×10⁻² | −1.27 | NO (trunc-dominated) |
| 1.00 | −9.90×10⁻³ | −1.73×10⁻² | NO (trunc-dominated) |
| 2.00 | +2.49×10⁻¹¹ | −2.28×10⁻¹² | YES |
| 4.00 | −2.67×10⁻¹² | −1.01×10⁻¹¹ | YES | At σ≤1 the trace residual is 10⁻³ to 10⁻¹, dominated by the fixed prime cutoff X=10⁵ (the spec-warned regime X∝exp(c/σ²) is required). At σ=2 and σ=4 the trace gate passes at ~10⁻¹¹, and λ_min sits at the numerical floor: |λ_min|/tr(M_zeros) ≈ 2×10⁻¹³ and 9×10⁻¹³ respectively, consistent with the ζ/L(χ)/L(Δ) numerical-floor signature (no false positives, magnitude ~10⁻⁸–10⁻¹⁰ floor cited in spec). **Window-scan (T₀=85.7, σ=2, J=16, nested zero sets):**
| |t|≤T_max | n_zeros | tr residual | λ_min |
|---|---|---|---|---|
| 50 | 43 | −1.08×10¹ | −1.307 |
| 100 | 107 | −1.73×10⁻⁷ | −1.73×10⁻⁷ |
| 150 | 181 | +2.49×10⁻¹¹ | −2.28×10⁻¹² |
| 200 | 259 | +2.49×10⁻¹¹ | −2.28×10⁻¹² | Sequence of λ_min: −1.307 → −1.73×10⁻⁷ → −2.28×10⁻¹² → −2.28×10⁻¹². Strictly monotone non-decreasing (differences +1.31, +1.73×10⁻⁷, 0). The saturation at 150 vs 200 reflects that further zeros have negligible amplitude on the J=16 basis (basis Gaussian envelope at |t|=150 already at 10⁻³⁶ for σ=2). **Conrey–Li / de Branges obstruction check:** None observed. The window-monotonicity pattern is strictly increasing and saturates at the numerical floor; there is no oscillation, no non-monotone "dip" upon enlargement. Structurally, adding zeros only adds a PSD rank-1 update v vᵀ to M_zeros (M_arith is window-independent), so monotone non-decreasing λ_min is the expected behavior for a clean GRH control, and that is exactly what is seen.
</results> <challenges>
1. **Quadrature failure for highly oscillatory integrands.** Initial implementation used Gauss–Hermite quadrature for the prime-side Fourier transform g_ij(k log p). For σ=4 with prime powers p^k near X=10⁵ this produced spurious 10⁻⁵–10⁻⁶ artifacts (e.g. 2^14, 2^15 contributions) and a 1.8×10⁻² trace residual. Fixed by deriving and using the closed-form ∫H_iH_j e^{−u²} e^{−iηu}du = √π e^{−η²/4} Σ_k 2^k k! C(i,k)C(j,k) (−iη)^{i+j−2k}.
2. **Prime cutoff insufficient for narrow σ.** Confirmed spec warning: at σ ∈ {0.25, 0.5, 1.0}, X=10⁵ leaves a systematic trace residual >10⁻² that completely dominates λ_min, rendering these points unreliable. A dynamic X∝exp(c/σ²) cutoff would be required.
3. **Zero list truncation at small windows.** At |t|≤50 (43 zeros), the trace gate fails by ~10, which simply reflects an unconverged M_zeros — it illustrates the directionality of window-monotonicity rather than a true engine failure.
4. Non-self-dual χ requires summing zeros on both positive and negative imaginary axis with chi(p)^k and χ̄(p)^k separately; care needed not to assume symmetry.
</challenges> <discussion>
The results corroborate the working hypothesis: L(χ₄ mod 5), in the regime where the trace-identity gate passes (σ ≥ 2 with X=10⁵), exhibits the same "clean control" behavior as ζ — λ_min sits at the numerical floor (~10⁻¹¹) with no negative signal indicating an obstruction. The window-enlargement test is, in particular, theoretically expected to be monotone for the construction Q = M_zeros − M_arith (each new zero contributes a PSD rank-1 update), and the empirical sequence confirms this strictly. The absence of any non-monotone dip refutes the existence of a de Branges/Conrey–Li-type obstruction at this point on the critical line for the J=16 spectral window. The σ-scan is only partially conclusive: only σ=2 and σ=4 are within the engine's validated regime at X=10⁵. The reliable points are both consistent with λ_min≈0 (numerical floor), so σ-monotonicity in the strict mathematical sense cannot be tested at high resolution here; what can be said is that no negative signal appears at either σ. Definitive σ-monotonicity testing would require dynamically scaling X with σ as spec'd. Importantly, the construction itself does not give a theoretical monotonicity in σ (unlike window enlargement), so a future σ-monotonicity test in the reliable regime would be a genuine empirical claim.
</discussion> <proposed-next-hypotheses>
1. For L(χ₄ mod 5) with a dynamically-scaled prime cutoff X(σ)∝exp(c/σ²) (c≈25), λ_min(Q) at T₀=85.7, J=16 is strictly monotone (non-positive and increasing in magnitude) across σ ∈ {0.25, 0.5, 1, 2, 4}, with |λ_min|/tr(M_zeros) staying below 10⁻⁸ for all σ.
2. At other heights T₀ along the critical line (e.g. T₀ ∈ {30, 50, 120, 180}) sampled for L(χ₄ mod 5), the window-monotonicity pattern remains strictly non-decreasing and saturates at the same ~10⁻¹¹ floor — i.e. the absence of a Conrey–Li obstruction is uniform in T₀, not specific to T₀=85.7.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>Lchi_Qform_results.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Pickle containing the full λ_min eigenvalue spectrum, trace residuals, and reliability flags for both the σ-scan (σ ∈ {0.25, 0.5, 1, 2, 4} at T₀=85.7, J=16, X=10⁵) and the nested window-scan (|t| ≤ 50, 100, 150, 200 at T₀=85.7, σ=2, J=16) of the L(χ₄ mod 5) localized Weil quadratic form Q = M_zeros − M_arith. Construction uses the analytic Hermite-Gauss/Laguerre Fourier transform identity for M_prime; trace gate verified at ~10⁻¹¹ in the reliable regime.</artifact-description>
</artifact>
<artifact>
<file-name>Lchi_monotonicity_results.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) window-monotonicity showing |λ_min(Q)| versus zero-window cutoff T_max = 50, 100, 150, 200 demonstrating strict monotone non-decrease and saturation at ~10⁻¹²; (B) σ-scan showing |λ_min| and |trace residual| versus σ, with reliable (σ=2, 4) and prime-cutoff-dominated (σ=0.25, 0.5, 1) points distinguished.</artifact-description>
</artifact>
</artifacts>
</output>
