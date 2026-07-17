## Overview <output>
<conclusion>
At σ=1, the analysis shows that X=5×10^7 is sufficient only up to about J≤16; for J≥20 the trace gate fails increasingly badly (up to ~10^-5 relative for ζ at J=28), so the hypothesis that X=5×10^7 makes the λ_min(J) curves converge uniformly to 0 across the full requested J-grid is not supported by the current results.
</conclusion>
<methods>
I followed a direct implementation of the localized Weil quadratic form Q = M_zeros - M_arith using Python with numpy, scipy, mpmath, pandas, and matplotlib-ready code in the notebook. I first read the authoritative specification file engine-spec.md and loaded the cached zero lists Lchi_zeros.pkl and Lchi_zeros_neg.pkl. I generated a cached list of 49 Riemann zeta zeros up to imaginary part about 141 using mpmath.zetazero, which is sufficient for the tested T0 range because Hermite-Gauss localization at σ=1 decays rapidly away from T0. For the Hermite-Gauss basis, I used normalized Hermite functions ψ_n with the stable three-term recurrence
ψ_0(x)=π^(-1/4)e^(-x^2/2), ψ_1(x)=√2 x ψ_0(x), ψ_{n+1}(x)=√(2/(n+1)) x ψ_n(x)-√(n/(n+1)) ψ_{n-1}(x),
and φ_n(t)=σ^(-1/2) ψ_n((t-T0)/σ). Then M_zeros was assembled as M_zeros = (1/σ) Ψ Ψ^T over the relevant zero list. For the arithmetic side, I implemented the explicit-formula decomposition:
1. Prime-power term truncated at X, using all prime powers p^k≤X.
2. Archimedean term from the digamma factor, integrated numerically.
3. Polar term for ζ only (analytically negligible at these T0 values, but the explicit-formula sign convention was checked). The key acceleration was the analytic Fourier transform of the Hermite-Gauss product basis:
F0_{mn}(v) = exp(-v^2/4) · (-iv/√2)^{|n-m|} · sqrt(min(m,n)!/max(m,n)!) · L_min^{|n-m|}(v^2/2),
with generalized Laguerre polynomials L. I verified this identity numerically against direct quadrature for multiple (m,n,v) test cases, with absolute differences around 10^-16. The prime-power contribution was then computed as a vectorized sum over precomputed arrays of p, k, log p, and weights -(log p)/(π p^{k/2}), using the character values χ(p^k) for L(χ₄ mod 5). The archimedean term was evaluated by direct Simpson integration after changing variables r=T0+σx:
(1/(2π)) ∫ ψ_m(x) ψ_n(x) Φ_arch(T0+σx) dx,
where Φ_arch(r) = -log π + Re ψ(1/4+ir/2) for ζ and Φ_arch(r) = log(5/π) + Re ψ(3/4+ir/2) for L(χ₄ mod 5). I tested this implementation at the reference point T0=85.7, σ=2, J=10. Validation was performed before interpreting results. At the reference point T0=85.7, σ=2, J=10, the trace identity held to high precision for both controls: residual ≈ -1.61×10^-13 for ζ and ≈ -2.58×10^-13 for L(χ₄ mod 5). The resulting λ_min values were at the numerical floor: λ_min ≈ -2.62×10^-14 for ζ and ≈ -3.70×10^-14 for L(χ₄ mod 5), with |λ_min|/tr around 10^-15. I then computed the full requested σ=1 grid for X=5×10^7:
T0 ∈ {30, 46.13, 60, 85.7, 120},
J ∈ {4, 8, 12, 16, 20, 24, 28},
for both ζ and L(χ₄ mod 5). Results were saved to lambda_min_sigma1.csv. To diagnose the unexpectedly worsening residuals at high J, I performed a targeted truncation analysis on the ζ, T0=30, J=28 diagonal entry. I extended the prime sieve from 5×10^7 to 5×10^8 and computed the missing tail contribution from primes in (5×10^7, 5×10^8]. That tail contributed about 2.180315×10^-4 to M_arith[27,27], essentially exactly matching the previously observed diagonal discrepancy and the trace residual at J=28. This showed that the dominant failure at high J was not floating-point summation error, but truncation error from an insufficient prime cutoff X. I began recomputing the full prime grid at X=5×10^8 using a chunked caching strategy, but the notebook runtime expired before those recomputations completed. Therefore I cannot report validated full-grid X=5×10^8 results.
</methods>
<results>
Main validated results at X=5×10^7 and σ=1: Reference validation (T0=85.7, σ=2, J=10):
- ζ: tr(M_zeros)=3.8982947981, tr(M_arith)=3.8982947981, trace residual = -1.61×10^-13, λ_min = -2.6243×10^-14, |λ_min|/tr = 6.73×10^-15.
- L(χ₄ mod 5): tr(M_zeros)=6.6869909944, tr(M_arith)=6.6869909944, trace residual = -2.576×10^-13, λ_min = -3.6977×10^-14, |λ_min|/tr = 5.53×10^-15. σ=1, X=5×10^7, full grid summary:
- For both ζ and L(χ₄ mod 5), J=4, 8, 12, 16 gave trace residuals at about 10^-14 to 10^-13 relative and λ_min values at the numerical floor (~10^-14 to 10^-13).
- At J=20 and above, errors increased rapidly, especially for ζ. Selected ζ results:
- T0=30: λ_min = -1.33×10^-14 (J=4), -1.75×10^-14 (J=8), -2.81×10^-14 (J=12), -1.40×10^-13 (J=16), -3.85×10^-10 (J=20), -3.59×10^-7 (J=24), -1.15×10^-4 (J=28).
- T0=46.13: λ_min = -1.39×10^-14, -2.72×10^-14, -3.47×10^-14, -4.05×10^-13, -9.67×10^-10, -7.37×10^-7, -1.96×10^-4.
- T0=85.7: λ_min = -2.37×10^-14, -4.36×10^-14, -5.48×10^-14, -9.66×10^-14, -1.05×10^-10, -1.02×10^-7, -3.40×10^-5.
- Relative trace residuals for ζ were ~10^-14 through J=16, then ~10^-10 at J=20, ~10^-8 to 10^-7 at J=24, and ~2.0×10^-6 to 2.7×10^-5 at J=28 depending on T0. Selected L(χ₄ mod 5) results:
- T0=30: λ_min = -2.19×10^-14 (J=4), -2.64×10^-14 (J=8), -3.40×10^-14 (J=12), -4.75×10^-14 (J=16), -9.46×10^-13 (J=20), -8.34×10^-10 (J=24), -2.64×10^-7 (J=28).
- T0=46.13: λ_min = -2.69×10^-14, -3.66×10^-14, -4.28×10^-14, -5.61×10^-14, -1.79×10^-12, -1.63×10^-9, -5.18×10^-7.
- T0=85.7: λ_min = -3.92×10^-14, -4.26×10^-14, -5.59×10^-14, -6.31×10^-14, -7.40×10^-12, -5.60×10^-9, -1.49×10^-6.
- Relative trace residuals for L(χ₄ mod 5) were ~10^-14 through J=16, around 10^-13 to 10^-12 at J=20, around 10^-11 to 10^-10 at J=24, and around 6.5×10^-9 to 5.5×10^-8 at J=28. Critical truncation-diagnosis result:
- For ζ, T0=30, σ=1, J=28, the discrepancy in the highest diagonal mode was concentrated at n=27: M_zeros[27,27] - M_arith[27,27] ≈ 2.180×10^-4.
- Extending only the k=1 prime tail from p>5×10^7 up to p≤5×10^8 gave an added contribution of about +2.180315×10^-4 to the arithmetic term for that same entry, explaining the discrepancy almost exactly.
- This demonstrates that the apparent nonzero λ_min at high J for X=5×10^7 is a truncation artifact caused by insufficient prime cutoff, not evidence against the GRH controls. Saved artifact:
- lambda_min_sigma1.csv was written to disk with the computed X=5×10^7 grid.
</results>
<challenges>
The main challenge was that the project specification is an engine specification rather than a ready-made numerical table, so all objects had to be constructed from scratch from the explicit formula. The exact explicit-formula normalization and sign conventions had to be verified empirically against the trace identity, which fortunately succeeded at the reference point and several target points. A major computational issue emerged at σ=1 for large J. Initially, the growth of |λ_min| and trace residual with J suggested possible floating-point instability. I tested this possibility directly by comparing analytic Fourier-transform values against mpmath, checking compensated summation, and verifying Hermite-function recurrence accuracy. Those checks did not explain the growing error. The decisive diagnostic was extending the prime range for a single problematic high-J diagonal entry, which showed that the observed discrepancy was almost entirely due to prime-cutoff truncation, not arithmetic precision. The largest limitation is incomplete completion of the intended recomputation at larger cutoff. I started a chunked recomputation at X=5×10^8, which appears to be the right scale to repair the J=28 truncation problem, but the notebook hit the runtime limit before completion. Therefore I cannot provide validated λ_∞ fits, uniformity-curve plots, or final X=5×10^8 full-grid estimates without violating the no-fabrication requirement. A second limitation is that the final requested figure was not produced because runtime expired during the necessary recomputation phase. I also did not persist a final report.md or update MEMORY.md before timeout. The CSV artifact for the validated X=5×10^7 grid does exist, but the final higher-cutoff analysis remains unfinished.
</challenges>
<discussion>
The current evidence does not support the specific stated hypothesis that X=5×10^7 is sufficient to make the σ=1 λ_min(J) curves for both ζ and L(χ₄ mod 5) converge near zero uniformly in T0 across the full requested J-grid. What the data do support is a more nuanced conclusion: X=5×10^7 is already sufficient for low-to-moderate basis dimension (roughly J≤16), where both controls behave exactly as expected under the explicit formula, with trace residuals at ~10^-14 and λ_min values at the numerical floor. However, for higher Hermite modes (J≥20, especially J=24 and 28), the frequency-space support of the basis functions reaches far enough into the prime side that the truncation at X=5×10^7 becomes visible. This is scientifically important because it sharpens the earlier methodological warning from the dataset description. The problem is not simply “σ=1 requires a larger X” in a coarse sense; rather, the required X also depends strongly on J. High-order Hermite-Gauss modes probe larger Fourier frequencies u = log p, so even when σ is fixed, increasing J broadens the effective frequency window and raises the prime cutoff needed for trace agreement. The explicit tail calculation for the ζ J=28 diagonal mode is strong quantitative evidence for this interpretation. Thus, the present analysis strengthens the broader methodological claim that dynamic prime cutoffs are necessary in narrow localization regimes. It also suggests that hypothesis H1 may still be true in substance—namely, the GRH controls likely do have λ_min near zero at σ=1—but X=5×10^7 is not enough to demonstrate that uniformly over the full J range requested here. A larger cutoff, plausibly at least on the order of 5×10^8 for J=28 and perhaps higher for tighter tolerances, is needed for a definitive test.
</discussion>
<proposed-next-hypotheses>
1. At σ=1, the minimum prime cutoff required to keep the trace residual below 10^-10 grows materially with basis size J, and for J=28 it is substantially larger than 5×10^7, likely of order 10^8 to 10^9.
2. After increasing the cutoff to at least X≈5×10^8, the λ_min(J) curves for ζ and L(χ₄ mod 5) will remain near the numerical floor through J=28, restoring apparent convergence to 0 uniformly in T0.
</proposed-next-hypotheses>
<artifacts>
<artifact>
<file-name>lambda_min_sigma1.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>CSV table of the completed σ=1, X=5×10^7 grid for ζ and L(χ₄ mod 5), including λ_min, traces, relative trace residuals, zero counts, and per-configuration runtime. It was created from the explicit-formula engine implemented in the notebook using cached zero lists and a generated ζ zero list.</artifact-description>
</artifact>
<artifact>
<file-name>zeta_zeros.pkl</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Cached list of 49 Riemann zeta zeros generated with mpmath.zetazero up to imaginary part about 141, stored as strings in a pickle file. This file was produced during the analysis to support repeated localized computations without regenerating zeros.</artifact-description>
</artifact>
</artifacts>
</output>
