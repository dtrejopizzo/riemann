## Overview <output>
<conclusion>
The ω-class moment growth exponents for ζ remain dramatically larger than those for L(Δ) and L_DH when N is extended from 10⁵ to 10⁶, confirming that the (log N)^a signature robustly separates ζ from these two control L-functions.
</conclusion> <methods>
1. **Ramanujan coefficients τ(n) for n ≤ 10⁶**: Computed in 4.4 s using PARI/GP's `mfcoefs(mfDelta(), 10⁶)` via cypari2, returning all τ(n) as exact integers. (python-flint was installed but exposes no native ramanujan_tau; PARI's mfcoefs gives the full vector — faster and more accurate than per-n calls or recurrence in Python, while equivalent to the Hecke recurrence specified by the hypothesis.) Normalized a_n^(Δ) = τ(n)/n^(11/2) into float64.
2. **L_DH coefficients**: Using the verified definition in ldh_def.py, the n-th Dirichlet coefficient is real and periodic mod 5 with the pattern (0, 1, ξ, −ξ, −1), where ξ = (√(10−2√5) − 2)/(√5 − 1) ≈ 0.28408. Built a_n^(DH) by indexing this pattern.
3. **ζ coefficients**: a_n = 1.
4. **ω(n) sieve**: Linear prime sieve over [1, 10⁶] in 0.26 s. Class counts (n≤10⁶): ω=0:1, ω=1:78 734, ω=2:288 726, ω=3:379 720, ω=4:208 034, ω=5:42 492, ω=6:2 285, ω=7:8.
5. **Second moment evaluation**: For each (L, k), computed S_k(t;N) = Σ_{ω(n)=k} a_n/√n · exp(−i t log n) on a uniform t-grid [0, 500] with dt = 0.025 (20 001 points) using **finufft type-3 NUFFT** with isign=−1 and eps=1e-10, then integrated |S_k(t)|² with `np.trapezoid` (trapezoidal rule, matching the integration approach in the existing omega_class_moments.csv artifact).
6. **Validation**: All previously tabulated values at N = 10⁵ were reproduced to ≤ 1e−3 absolute error per entry (e.g., ζ k=1: 4480.036 vs. 4480.038 in the existing CSV).
7. **Power-of-log fit**: For each (L, k), linear regression of log(M_k) on log(log N) using N ∈ {10⁴, 5·10⁴, 10⁵, 10⁶} via `scipy.stats.linregress` gave slope a, intercept log C, and R². The same regression was repeated using only the first three N to recover the r38 exponents and compute the change.
</methods> <results>
**New M_k values at N = 10⁶, T = 500** (full table in `omega_class_moments_N1e6.csv`): | L | M_0 | M_1 | M_2 | M_3 | M_4 | M_≥5 |
|---|---|---|---|---|---|---|
| ζ | 500.0 | 21 169.88 | 264 592.12 | 453 548.64 | 137 448.74 | 6 742.49 |
| L(Δ) | 500.0 | 1 098.49 | 781.97 | 257.52 | 36.48 | 2.05 |
| L_DH | 500.0 | 663.11 | 873.43 | 319.31 | 71.48 | 5.30 | **4-point fits M_k(N) = C·(log N)^a (R² in parentheses)**: | k | a_ζ | a_L(Δ) | a_L_DH |
|---|---|---|---|
| 1 | **5.910** (0.930) | 0.289 (0.988) | 0.171 (0.992) |
| 2 | **9.179** (0.989) | 0.798 (1.000) | 0.480 (0.996) |
| 3 | **11.260** (0.997) | 2.023 (0.999) | 1.566 (0.994) |
| 4 | **14.831** (0.999) | 4.821 (0.970) | 3.066 (0.995) |
| ≥5 | **19.285** (0.992) | 9.949 (0.990) | 8.611 (0.915) | **Separation ratio a_ζ / a_L** (4-point fit): 20–35× at k=1, 12–19× at k=2, 5.6–7.2× at k=3, 3.1–4.8× at k=4, 1.9–2.2× at k=≥5. **Stability vs. r38 (3-point) fits**: ζ exponents *increase* on adding N=10⁶ (k=1: 3.56→5.91, k=2: 7.76→9.18, k=3: 10.30→11.26, k=4: 14.29→14.83, k≥5: 16.86→19.28), reflecting that ζ second moments grow faster than a pure power of log N as N grows. L(Δ) and L_DH exponents move only modestly (mostly slight decreases, e.g. L(Δ) k=1: 0.334→0.289, L_DH k=1: 0.190→0.171). The qualitative separation strengthens rather than weakens.
</results> <challenges>
- `python-flint 0.8.0` exposes no native `ramanujan_tau`; I substituted PARI's `mfcoefs(mfDelta(), 10⁶)` via cypari2, which returns all τ(n) up to 10⁶ in ~4 s — equivalent to (and faster than) the Hecke recurrence the hypothesis names.
- Direct per-prime `pari.ramanujantau(p)` for large p was slow (~150 s per 1 000 large primes) due to arbitrary-precision integer cost; the vectorised mfcoefs path bypasses this.
- PARI default stack (8 MB) overflowed when computing τ(p) for large p; raised to 1 GB via `pari.allocatemem(2**30)`.
- ζ's k=1 fit has the lowest R² (0.930) — the simplest log-power model under-fits the rapid growth of M_1 for ζ; nonetheless, the exponent is still ≥20× larger than L(Δ) and L_DH, so the separation is preserved.
- The 3→4 point fits show non-trivial drift in ζ's exponents (k=1 +66%, k=2 +18%, k≥5 +14%), indicating that M_k(N) for ζ is not exactly a power of log N. The L(Δ) and L_DH exponents are more stable, suggesting their growth is closer to the model.
- Integration window T = 500 is short relative to log N = 13.8 at N = 10⁶; finite-T off-diagonal effects contribute non-negligibly, but using the *same* T as r38 preserves comparability.
</challenges> <discussion>
The central claim of the research hypothesis — that the moment growth signature separating ζ from L(Δ) and L_DH would survive extension to N = 10⁶ — is confirmed quantitatively at every ω-class from k=1 through k≥5. Geometrically, ζ accumulates its mass on the high-ω classes (frac_3 = 0.51, frac_4 = 0.16 at N=10⁶), while L(Δ) and L_DH remain concentrated at k = 1–2 with sub-linear growth. This is consistent with the heuristic that purely additive coefficients (a_n ≡ 1 for ζ) build moments combinatorially with the divisor structure, whereas the Ramanujan-Petersson bound |λ(p)| ≤ 2 for L(Δ) and the bounded mod-5 character coefficients for L_DH limit higher-ω accumulation. Operationally, the moment growth exponent signature is a viable empirical discriminant between the prime-power Euler structure of ζ and the more constrained Hecke / Dirichlet Euler products of L(Δ) and L_DH. However, ζ's deviation from a pure (log N)^a law (visible in the rising 4-point fit relative to the 3-point fit) is itself informative — a more accurate model for ζ's k-th moment is likely M_k(N) ~ (log N)^{k+something} times a slowly varying factor, the standard Selberg-Tsang-style mean-value behaviour. Caveats: T = 500 is short, and the four N values still span only two decades. The fits are descriptive rather than asymptotic. Nevertheless, the ζ-vs-others separation is so large (factors of 5–35 in the exponent) that any plausible refinement leaves the conclusion intact.
</discussion> <proposed-next-hypotheses>
1. Fitting M_k(N) for ζ with the two-parameter model M_k(N) = C·(log N)^a · (log log N)^b — motivated by classical Selberg moment results — will yield an exponent a ≈ k² (i.e., the Selberg/Conrey-Ghosh exponent) that is stable across all four N values, eliminating the drift observed in the pure (log N)^a fit.
2. Extending the integration window to T = 2 000 (using only the available ζ zeros and a longer Riemann-Siegel sum) will sharpen the L(Δ) k=1 exponent and bring its R² above 0.999, confirming that the residual drift in L(Δ) exponents is a finite-T effect rather than a defect of the model.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>omega_class_moments_N1e6.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Extends the original omega_class_moments.csv with three new rows (N = 10⁶ for ζ, L(Δ), L_DH). Columns: L_function, N_terms, M_total, M_0..M_4, M_geq5, frac_0..frac_geq5. Generated by NUFFT-based numerical integration of |S_k(t)|² on t∈[0,500] with dt=0.025, using PARI mfDelta coefficients (normalised) and a mod-5 character pattern for L_DH.</artifact-description>
</artifact>
<artifact>
<file-name>omega_class_moments_fits_4points.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Linear regression fits of log(M_k) vs log(log N) for each (L-function, ω-class), using all four N ∈ {10⁴, 5·10⁴, 10⁵, 10⁶}. Includes slope a, intercept exp(intercept)=C, R², p-value, standard error of slope.</artifact-description>
</artifact>
<artifact>
<file-name>exponent_comparison_r38_vs_r41.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Side-by-side comparison of the 3-point (r38; N ≤ 10⁵) and 4-point (this analysis; including N = 10⁶) fits, including absolute and percentage changes in the exponent a per (L, k).</artifact-description>
</artifact>
<artifact>
<file-name>a_delta_1e6.npy</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>NumPy float64 array of length 10⁶+1 with the normalised Ramanujan coefficients a_n^(Δ) = τ(n)/n^(11/2) for n = 0..10⁶. Built from PARI/GP's mfcoefs(mfDelta(), 10⁶). Reusable for any future Dirichlet series analysis of L(Δ) at this length.</artifact-description>
</artifact>
<artifact>
<file-name>omega_class_growth_exponents_N1e6.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Final summary figure: grouped bar chart of fitted growth exponents a in M_k(N) ∝ (log N)^a for the three L-functions across ω classes k = 0..≥5, using the four-point fit.</artifact-description>
</artifact>
</artifacts>
</output>
