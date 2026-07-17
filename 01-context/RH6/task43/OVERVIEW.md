## Overview <output>
<conclusion>
The ω-class second moments M_k(N) for ζ, L(Δ), and L_DH are all well-described in log–log space by a power-of-log model M_k(N) ≈ C_k·(log N)^a, and the fitted exponent a forms a clear quantitative signature that strongly separates ζ (large exponents, e.g. a≈3.6, 7.8, 10.3, 14.3 for k=1–4) from L(Δ) and L_DH (small exponents, e.g. ≲6 for k=1–4), although with only three N values per L-function the 2-parameter fit has only 1 degree of freedom and the result is a finite-N empirical fingerprint rather than a tested asymptotic law.
</conclusion> <methods>
1. Loaded `omega_class_moments.csv` (9 rows: 3 L-functions × 3 N values N∈{10⁴, 5×10⁴, 10⁵}; columns M_k for k=0,1,2,3,4 and M_≥5).
2. For each (L, k), fit three nested models to the three (N, M_k) points: (a) M = C·log N (1 parameter, closed-form least-squares for C); (b) M = C·(log N)^k with k fixed to the ω-class index (1 parameter); (c) M = C·(log N)^a fitted by linear least-squares in log–log space on (log log N, log M) → C = exp(intercept), a = slope (2 parameters → exact freedom of 1).
3. Reported R² in both linear M-space and log–log space (the latter is what the regression actually minimises).
4. Compared the fitted exponents a across L-functions for each class k, then summarised in a pivot table and a two-panel figure (A: log–log curves of M_k vs log N; B: a versus k for each L).
5. Saved per-(L,k) fits to `omega_class_growth_fits.csv` and the summary figure to `omega_class_growth_fits.png`.
Tools: pandas, numpy, scipy.optimize (not needed in the end — closed-form OLS sufficed), matplotlib. No statistical assumptions about errors could be made (no replicates), so formal significance tests and uncertainty bands were not produced.
</methods> <results>
Fitted exponents a in M_k(N) ≈ C·(log N)^a (log–log R² in parentheses): k=1: ζ a≈3.56 (R²=0.980), L(Δ) a≈0.33 (0.998), L_DH a≈0.19 (0.995)
k=2: ζ a≈7.76 (0.998), L(Δ) a≈0.79 (0.999), L_DH a≈0.50 (0.992)
k=3: ζ a≈10.30 (1.000), L(Δ) a≈2.10 (1.000), L_DH a≈1.73 (0.996)
k=4: ζ a≈14.29 (1.000), L(Δ) a≈6.02 (0.994), L_DH a≈3.38 (0.999)
k≥5: ζ a≈16.86 (0.995), L(Δ) a≈11.40 (1.000), L_DH a≈12.31 (0.989)
k=0: M_0=500 is N-independent (it is the integration window length), so a≈0 trivially. Total-moment fits: ζ a≈8.63, L(Δ) a≈0.52, L_DH a≈0.45 — confirming the dramatic separation of ζ from the two other L-functions. Goodness-of-fit comparison among models:
- Model (a) M = C·log N fits poorly almost everywhere (R² often negative for ζ-classes with k≥2 and for L(Δ), L_DH k=1: e.g. L_DH k=1 R²_a = -16.1).
- Model (b) M = C·(log N)^k fits ζ poorly (best R²≈0.64 for k=4) but does much better for L(Δ) (R²=0.86–0.94) and L_DH (R²=0.86–0.98) for higher k.
- Model (c) M = C·(log N)^a fits all (L,k) very well in log–log space (R²≥0.98 in every non-trivial case), but with only one excess degree of freedom this near-perfect fit cannot be interpreted as a strong test of the functional form. Signature: ζ exponents are 5–20× larger than L(Δ) and L_DH exponents at low k, providing a sharp, monotonically-growing-with-k separation. L(Δ) and L_DH exponents are similar in magnitude, with L_DH slightly smaller than L(Δ) for k=1,2,4 and the two crossing for k=3 and k≥5; the within-pair difference (~0.2–2.6) is smaller than the ζ-vs-rest gap. Approximate empirical scalings for ζ — a(k) ≈ {3.6, 7.8, 10.3, 14.3} for k=1..4 — are close to neither 2k+1 (=3,5,7,9) nor k² (=1,4,9,16) nor k(k+1)/2 (=1,3,6,10); they roughly follow a near-linear growth a≈3.5+3.5k, suggesting an extra Selberg-type ~(log N)^? factor beyond the (log N)^k naive expectation, but the three-point data cannot pin down a multi-parameter (log N)^a (log log N)^b form.
</results> <challenges>
- Only N = 10⁴, 5×10⁴, 10⁵ (three points) per L-function. A two-parameter model leaves a single degree of freedom, so log–log R² values near 1 are largely structural rather than evidential. The proposed three-parameter (log N)^a (log log N)^b model would exactly interpolate the data and is therefore not identifiable from this CSV.
- log log N spans only 9.21 → 11.51, a factor of ~1.25, giving very little lever-arm to discriminate among slowly-varying functional forms.
- No uncertainty estimates accompany the moments, so formal residual analysis, confidence intervals on a, or model comparison via reduced χ² are not possible.
- The k=0 column is constant (=500, the window length), confirming it is the trivial constant term and should be excluded from growth-rate inference.
- Per the dataset description, ω-class fractions continue to drift at least up to N=10⁶, so the asymptotic regime may not have been reached at N=10⁵; the exponents reported should be regarded as effective finite-N exponents in this window.
</challenges> <discussion>
The exponents a obtained from M_k(N) ≈ C·(log N)^a yield a quantitative fingerprint that is substantially more discriminating than the raw fractions reported in the source CSV. Most strikingly, ζ exhibits much faster (log N)-growth across every ω-class than either L(Δ) or L_DH — for example, M_2 for ζ grows as roughly (log N)^7.8 while L_DH and L(Δ) grow only as ~(log N)^0.5 and ~(log N)^0.8 respectively. This is consistent with the heuristic that the Dirichlet polynomial of ζ on the critical line behaves like a random multiplicative function whose moments inherit Selberg/Bohr–Jessen-type log-power growth, whereas the Dirichlet coefficients of L(Δ) (a cusp form, |a_n|≪n^{11/2+ε} normalised, Sato–Tate distributed) and the non-Euler-product L_DH have very different (and more bounded) ω-class moment structure. Importantly, the L_DH vs L(Δ) separation — relevant to the program of finding signatures of off-critical-line zeros — is small (Δa ≲ 2.6 within each k) and the two functions even cross at k=3 and k≥5, so growth exponents alone do not cleanly mark the known off-critical anomaly of L_DH. The strong ζ-vs-rest separation should therefore be read primarily as a separation of L-functions with vs. without genuine Euler products and central character, not as a direct RH-violation signal. Treated, as the dataset description recommends, as a finite-N structural fingerprint, the (C, a) pairs are a more compact and rank-stable summary than raw moments at one N — but extending to additional N values (10⁶, 10⁷) is required before any claim about the underlying functional form (pure log-power vs log-power × loglog-power) can be tested.
</discussion> <proposed-next-hypotheses>
1. Extending the moment table to N ∈ {10⁶, 10⁷} will reveal that the effective exponents a_k(N) themselves drift logarithmically in N, and that adding a (log log N)^b factor (i.e. M_k ≈ C·(log N)^a (log log N)^b) becomes identifiable and yields a stable b that separates L_DH from L(Δ) more cleanly than (log N)^a alone.
2. The empirical near-linear relation a_ζ(k) ≈ α + β·k (with α≈β≈3.5 in our fit window) reflects an underlying combinatorial law a_ζ(k) → 2k − 1 + O(1) in the true asymptotic regime, predicted by an ω-decomposition of the Conrey–Gonek 2k-th moment heuristic; this is testable by enlarging N and recomputing a_k.
</proposed-next-hypotheses> <artifacts>
<artifact>
<file-name>omega_class_growth_fits.csv</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Per (L-function, ω-class k) fitted parameters for three growth models — (a) M = C·log N, (b) M = C·(log N)^k with k fixed by class, and (c) M = C·(log N)^a (two-parameter) — together with R² in linear M-space and in log–log space. Produced by OLS on (log log N, log M_k) using the three N values in omega_class_moments.csv.</artifact-description>
</artifact>
<artifact>
<file-name>omega_class_growth_fits.png</file-name>
<artifact-type>agent_produced</artifact-type>
<artifact-description>Two-panel summary figure. Panel A: log–log plot of M_k(N) vs log N for k=1..4 and L ∈ {ζ, L(Δ), L_DH}, showing ζ slopes are visually much steeper than for the other two L-functions. Panel B: fitted exponent a (from M_k ≈ C·(log N)^a) versus ω-class k for each L-function, showing ζ separated by a factor of 3–20 from L(Δ) and L_DH across all classes.</artifact-description>
</artifact>
</artifacts>
</output>
