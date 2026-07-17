## Overview <output>
<conclusion>
The hypothesis is supported in the signal-only (off-critical pair contribution) sense — α grows monotonically from ≈0 to ≈17.5 as β/σ increases from 0.15 to 2.47, crossing the super-polynomial threshold (α>10) at σ≤0.125 — but the prescribed full-Q pipeline (Q = M_zeros − M_arith) does NOT reveal this monotonic relationship because its |λ_min| is dominated by an M_arith truncation/missing-archimedean baseline that itself scales as J^≈21 across all σ.
</conclusion> <methods>
Implementation in mpmath at dps=80, following the research-objective prescription literally and then complementing with a signal-isolation analysis. 1. Test functions: h_j(u) = ((u−T0)/σ)^j · exp(−(u−T0)²/(2σ²)), J = 4,8,12,16,20. Evaluated at complex u when needed.
2. Parameters: T0 = γ = 85.6993; off-critical pair (β, γ) = (±0.3085, 85.6993); window T0±40; prime_bound=1000.
3. M_zeros: built from 33 ζ-zeros (from `zeta_zeros_5000_dps50.npy`) within T0±40 as Σ_k v(γ_k) v(γ_k)^T, plus the off-critical contribution Σ_{u∈{γ−iβ, γ+iβ}} Re[v(u) v(u)^T] (the "non-Hermitian Re[v v^T]" construction).
4. M_arith built from the standard explicit-formula form (M_arith)_{ij} = Σ_{n=p^k ≤ 1000} (Λ(n)/√n) · 2·Re[ ĥ_i(log n) · conj(ĥ_j(log n)) ], using the analytically derived Fourier transform of h_j: ĥ_j(ξ) = σ · e^{−iξT0} · √(2π) · e^{−(ξσ)²/2} · Σ_{k even ≤ j} C(j,k) · (−iξσ)^{j−k} · (k−1)!! The closed form was verified against numerical quadrature for j=0..3 (agreement to ~14 digits).
5. Sweeps over σ ∈ {2.0, 1.0, 0.5, 0.25, 0.125} and J ∈ {4, 8, 12, 16, 20}.
6. Computed eigenvalues of Q = M_zeros − M_arith with mpmath.eigsy; α from scipy.stats.linregress of log|λ_min| vs log J.
7. To isolate the off-critical contribution from the dominant baseline, also computed eigenvalues of the off-critical-only matrix M_off = Re[v(γ−iβ)v(γ−iβ)^T] + Re[v(γ+iβ)v(γ+iβ)^T] alone and fit its |λ_min|–J power law.
</methods> <results>
Full Q = M_zeros − M_arith (as prescribed):
σ=2.0, β/σ=0.15: α=21.08, R²=0.91
σ=1.0, β/σ=0.31: α=21.55, R²=0.89
σ=0.5, β/σ=0.62: α=21.69, R²=0.89
σ=0.25, β/σ=1.23: α=21.28, R²=0.88
σ=0.125, β/σ=2.47: α=17.54, R²=0.95
→ α is essentially flat (∼21) at σ ≥ 0.25 and even decreases at σ=0.125. The hypothesized monotonic increase is NOT observed in the full Q. Baseline diagnostic (Q without the off-critical pair) reproduces the same α≈21 scaling, demonstrating that the J^≈21 growth is a property of the M_arith truncation/missing archimedean (gamma-factor / polar) terms, NOT of any zero anomaly. With β=0.3085 and σ≥0.25, the off-critical contribution to |λ_min| is < 10⁻³ relative to this baseline at J≥8 and is therefore invisible. Signal-only (off-critical pair contribution alone, M_off):
σ=2.0: |λ_min|=4.88e−2 (essentially J-independent), α≈0.0
σ=1.0: |λ_min|=0.211 (essentially J-independent), α≈0.0
σ=0.5: |λ_min|=1.28→1.30, α≈0.013
σ=0.25: |λ_min|=46→4.76e4, α=4.20, R²=0.96
σ=0.125: |λ_min|=2.05e5→7.37e17, α=17.50, R²=0.95
→ α grows monotonically with β/σ, and super-polynomial growth (α>10) is recovered for β/σ ≳ 2.5 (σ=0.125), exactly as hypothesized. For σ=0.125 (β/σ=2.47) the off-critical contribution finally exceeds the M_arith baseline (full Q |λ_min| ≈ 8.0e17 vs baseline ≈ 6.7e16), and the full-Q α (17.5) coincides with the signal-only α (17.5), confirming that the signal is being detected.
</results> <challenges>
1. The prescribed M_arith (Λ(n)/√n prime-power sum truncated at N=1000, with no gamma-factor / polar / continuous-spectrum contributions) is not a tight enough representation of the spectral side of the explicit formula for ζ. As a result Q is not approximately PSD in the absence of off-critical zeros, and |λ_min| of Q is dominated by a J^≈21 truncation baseline for σ ≥ 0.25.
2. With β=0.3085, the off-critical contribution at σ=2.0 yields |λ_min| of order 0.05 — many orders of magnitude below the baseline. The signal is therefore invisible in the full pipeline until σ is small enough (β/σ ≳ 2.5).
3. The prior r36 report of α≈1.06 for L_DH and an artificial-ζ analog at T0=85.7, σ=2.0 could not be reproduced in the full-Q pipeline here (we get α≈21); this strongly suggests r36 was working with a more complete arithmetic side (gamma-factor + polar terms) and/or normalised so that the baseline was sub-leading. The current results should be interpreted in light of this discrepancy: the *signal* analysis is unambiguous, but the *full-pipeline* numbers are baseline-dominated.
4. mpmath.eigsy of dense 20×20 matrices at dps=80 is fast (~3.6 s per σ for the whole J sweep), so compute was not a limiter.
</challenges> <discussion>
The geometric-signature hypothesis is best stated as a property of how the chosen Gaussian-monomial basis projects an off-critical pair into the J-dimensional test space: when β/σ is small the off-critical u = γ ± iβ lies well inside the basis support and contributes a bounded, J-independent rank-2 perturbation; when β/σ is large, the imaginary-shift y → y ± i(β/σ) excites the high-order monomials and the Gaussian damping no longer suppresses them, producing super-polynomial growth dictated entirely by the basis geometry. Our M_off-only sweep gives a clean numerical demonstration: α(β/σ) increases monotonically and crosses 10 near β/σ ≈ 2. This has a direct methodological consequence for any Weil-form search for off-critical zeros: at a fixed candidate (β, γ), the detector amplification can be tuned by choosing σ such that β/σ is large (≳2). Conversely, an observation of α≈O(1) at large σ tells you nothing about the absence of an off-critical pair — it is the expected null response of the geometry. The fact that the full Q pipeline as literally specified is baseline-dominated also indicates an important caveat for r36-style analyses: the M_arith side as constructed from only the Λ(n)/√n sum to N=1000 is incomplete, and conclusions about "α as an intrinsic signature" must control for this baseline (e.g., by subtracting the no-off-critical Q, as we did).
</discussion> <proposed-next-hypotheses>
1. The geometric scaling exponent α(β/σ) of the signal-only off-critical pair matrix follows a universal function α ≈ c·log( (β/σ)·(J/J0) ) (or a power law in β/σ) that depends only on the ratio β/σ, not on γ or T0 — testable by repeating the M_off-only sweep at several distinct (β, γ) pairs and checking collapse onto a single curve when plotted vs β/σ.
2. Augmenting M_arith with the standard archimedean gamma-factor contribution and the trivial-zero / polar terms of ζ will reduce the no-off-critical baseline α from ≈21 to O(1), at which point the full Q = M_zeros − M_arith pipeline will exhibit the same monotonic α(β/σ) behaviour as the signal-only analysis, even at σ=2.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>weil_sigma_sweep_results.json</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>JSON containing all parameters and numerical results of the σ-sweep: per-σ |λ_min|(J) arrays for the full Q = M_zeros − M_arith pipeline and for the signal-only M_off-pair matrix, plus log-log regression outputs (α, R², intercept) and β/σ values. Generated by the analysis notebook with mpmath at dps=80 using 33 ζ-zeros within T0±40, 193 prime powers up to N=1000, and an analytically derived Fourier transform of the Gaussian-monomial basis.</artifact-description>
</artifact>
<artifact>
<file-name>weil_sigma_sweep.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure: (A) α vs β/σ for the full Q pipeline (essentially flat at α≈21 because of baseline dominance) and for the signal-only M_off matrix (monotonically rising from ≈0 to ≈17.5 and crossing the α=10 super-polynomial threshold near β/σ≈2); (B) log–log plot of |λ_min| of M_off vs J for each σ, showing the dramatic emergence of super-polynomial growth at σ=0.125.</artifact-description>
</artifact>
</artifacts>
</output> 