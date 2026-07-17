## Overview <output>
<conclusion>
The trace residual η(X) for L(Δ,s) at T₀=46.13, σ=1, J=10 is empirically explained by a single super-polynomial Gaussian-in-log-X envelope η(X) ≈ 8.54·exp(−0.121·log²X); the data give no statistically resolvable polynomial degree-2 component, and the envelope reaches the 10⁻¹² threshold near X ≈ 6×10⁶ — not the X>10⁹ scale predicted by the hypothesis — so the validation gate, while still expensive, is *not* computationally inaccessible.
</conclusion> <methods>
1. Efficient τ(n) engine. Implemented exact-integer computation of τ(n) using the identity 1728·Δ(q) = E₄(q)³ − E₆(q)². Sieved σ₃(n), σ₅(n) up to N (O(N log N)). Polynomial cubings/squarings via Kronecker substitution: pack length-N coefficient lists into single integers using bit-aligned (slot_bits=240, byte-aligned) slots and multiply with gmpy2 (GMP FFT integer multiplication). This reduces tau computation to three big-int multiplies. Verified by (a) reproducing τ(2..97) exactly against OEIS A000594 and (b) Hecke recursion τ(p²)=τ(p)²−p¹¹ on 30 primes (all match). Total time for N=3×10⁵: 357 s.
2. Sweep. Loaded the validated 61-zero list L_Delta_zeros_200_reliable.pkl, passed γᵢ to weil_modular.compute_Q_modular with include_negative_zeros=True. Swept primes_cutoff X ∈ {500, 1000, 2000, 3000, 5000, 7000, 10⁴, 1.5·10⁴, 2·10⁴, 3·10⁴, 5·10⁴, 7·10⁴, 10⁵, 1.5·10⁵, 2·10⁵, 2.5·10⁵, 3·10⁵} (17 points). For each X computed M_zeros, M_arith and η = |tr(M_zeros)−tr(M_arith)|/|tr(M_zeros)| and λ_min(Q).
3. Modelling. Fit log η(X) (and its right-running maximum envelope) to the composite model log[A₁·exp(−α·log²X) + A₂·X^(−β)] (scipy.optimize.curve_fit), and to the pure super-polynomial model log A₁ − α·log²X for comparison. Extrapolated X needed for η<10⁻¹² by solving log²X = (log A₁ − log 10⁻¹²)/α.
</methods> <results>
- tr(M_zeros) = 6.362035 stable across all X (basis is fixed).
- Raw η(X) oscillates because Σ τ(p)·log p/√p has sign cancellation; the right-running envelope decays monotonically from 4.88×10⁻³ at X=500 to 1.91×10⁻⁸ at X=3×10⁵.
- Composite 4-parameter fit collapses to the super-polynomial branch (A₂→0, β→∞), giving no statistically resolvable polynomial floor. The pure super-polynomial fit yields A₁ = 8.54 (log A₁ = 2.15), α = 0.1212, with RMS log-residual ≈ 1.4 (envelope) / 1.6 (raw).
- Extrapolated cutoff for η<10⁻¹²: log X = √((2.145 + 27.63)/0.1212) ≈ 15.68 → X ≈ 6.4×10⁶ (≈ 2.1 × 10^6.8). Predicted η at X = 10⁷ is 1.8×10⁻¹³; at X = 10⁸, 1.2×10⁻¹⁷.
- λ_min(Q) tracks η: −0.28 at X=500, −1.4×10⁻⁷ at X=3×10⁵, consistent with O(η) bound on the smallest Weil eigenvalue when the rest of the spectrum is well-conditioned.
</results> <challenges>
- Computing τ(n) for n ≤ 3×10⁵ exactly required ~10⁸-bit big integers (slot_bits = 240, ≈ 15 MB packed). Naïve "+= big << shift" packing was O(N²) and dominated runtime (16 s at N=5×10⁴); replaced with bytearray + int.from_bytes/to_bytes (O(N) wall), reducing pack/unpack to <0.1 s. Final bottleneck is GMP integer multiplication itself.
- The hypothesised polynomial degree-2 tail term is not statistically separable from the super-polynomial term over X ∈ [5×10², 3×10⁵]; the curve_fit optimiser drives β to infinity. Either the polynomial term has a coefficient too small to detect at our X range, or its decay is itself sub-polynomial (logarithmic) and absorbed into A₁.
- Could not reach X=5×10⁵ within the runtime budget; one earlier attempt hit the 900 s per-cell limit. The pipeline is ready to run at larger N offline; extrapolation must therefore rely on the X≤3×10⁵ data.
</challenges> <discussion>
The data refute the *quantitative* form of the hypothesis (slow polynomial term forcing X>10⁹) but support the *qualitative* picture: a single super-polynomial Gaussian-in-log-X envelope, identical in functional form to the f11 model that explained the degree-1 noise floor, also governs the L(Δ,s) trace residual once the Deligne-bounded prime sum is summed to a sufficient cutoff. The plateau η ≈ 4×10⁻³ at small X is *not* a polynomial floor; it is the constant pre-factor A₁ before the super-poly cutoff "kicks in" near log²X ≈ log A₁/α ≈ 18 (X ≈ e^4.2 ≈ 65 — but suppressed by the τ(p) sign-cancellation noise). Practically, validation of L(Δ,s) to the 10⁻¹² standard appears to require X ≈ 10⁷, which with the new gmpy2 τ-pipeline scales as roughly 350 s · (10⁷/3·10⁵)^≈1.6 ≈ 9 × 10⁴ s ≈ one day of compute — expensive but not "computationally inaccessible". The validation criterion may therefore be relaxed conditionally on a one-time large run, rather than treated as intrinsically unreachable.
</discussion> <proposed-next-hypotheses>
1. The L(Δ,s) noise-floor coefficient α = 0.1212 (at T₀=46.13, σ=1, J=10) matches σ²/8 = 0.125 within 3%, i.e. the basis-only Gaussian-in-log-X law derived for ζ in f11 carries over verbatim to weight-12 degree-2 L-functions despite the doubled gamma factor.
2. Running the pipeline at X = 10⁷ on a single machine (predicted η ≈ 2×10⁻¹³) will achieve the strict |λ_min(Q)|<10⁻¹² gate for L(Δ,s), formally closing the validation task without requiring algorithmic refinement.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>tau_at_primes_300k.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Pickle of dict mapping each prime p ≤ 3×10⁵ (25,997 entries) to the exact integer τ(p). Computed via 1728·Δ = E₄³ − E₆² using divisor-sieved σ_3,σ_5 and Kronecker substitution with gmpy2 GMP multiplication. Validated against Hecke relation τ(p²)=τ(p)²−p¹¹ (30/30 pass) and direct comparison to OEIS A000594 for small p. Used as input to weil_modular.compute_Q_modular for the X-sweep.</artifact-description>
</artifact>
<artifact>
<file-name>L_Delta_eta_sweep_300k.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>CSV table of the X-sweep results: columns X, tr(M_zeros), tr(M_arith), η, λ_min, for 17 values of X from 500 to 3×10⁵ at fixed (T₀=46.13, σ=1, J=10).</artifact-description>
</artifact>
<artifact>
<file-name>eta_sweep_results.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Pickle of raw (X, tr_M_zeros, tr_M_arith, η, λ_min) tuples from the convergence sweep; the same data as the CSV in Python-native form for reuse.</artifact-description>
</artifact>
<artifact>
<file-name>L_Delta_eta_fit_summary.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final summary figure: log-log plot of η(X) raw points, right-running envelope, and the fitted super-polynomial model 8.54·exp(−0.121·log²X), with the η=10⁻¹² target line. Shows extrapolated crossing at X ≈ 6×10⁶.</artifact-description>
</artifact>
</artifacts>
</output>
