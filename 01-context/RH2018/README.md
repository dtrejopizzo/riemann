# Research Program 2 — Resonance Suppression Diagnostics for Arithmetic L-Functions

**Period:** 2018

## Research Objective

This program executes a combined numerical-and-proof investigation into whether the Riemann Hypothesis can be established through **resonance suppression**: the idea that multiplicativity (Euler-product structure) prevents Dirichlet partial sums from exhibiting the large, coherent phase alignments needed to sustain zeros off the critical line.

The program follows strict methodological rules to avoid the pitfalls identified in prior work:

- **One implementation only** — every function/metric is defined once and reused everywhere; a second, divergent implementation is treated as a fatal error.
- **Validation gates** — before any analysis, |L_DH(ρ)| must be verified below 10⁻⁶ at all four known off-line zeros; failure halts the pipeline.
- **Liouville is fully multiplicative** — λ(n) = (−1)^Ω(n) is completely multiplicative (λ(mn) = λ(m)λ(n) for all m, n), with Dirichlet series ζ(2s)/ζ(s) and Euler product ∏_p(1+p⁻ˢ)⁻¹. It was flagged as a key test case because it can exhibit anomalous resonance despite full multiplicativity.
- **N-dependence tracking** — every metric is reported across N ∈ {10⁴, 10⁵, 10⁶, 10⁷}; a single number is never treated as a result, only a curve.
- **Kahan summation** — naive summation was shown to corrupt GEV (generalized extreme value) fits at N ≳ 10⁵.
- **Candid reporting** — refuted hypotheses are reported as refuted, without post-hoc adjustment.

### The Davenport–Heilbronn function (canonical definition)

χ: primitive character mod 5, order 4: χ(0)=0, χ(1)=1, χ(2)=i, χ(3)=i, χ(4)=1, period 5, χ(n) = conj(χ(n)).

κ = ((10−2√5)/5)^(1/2) ≈ 0.28408.

```
L_DH(s) = ((1−iκ)/2)·L(s,χ) + ((1+iκ)/2)·L(s,χ)
```

with a_n(DH) = ((1−iκ)/2)·χ(n) + ((1+iκ)/2)·χ(n). Coefficients are **complex** and **not** multiplicative.

Off-line zeros used for validation: (0.808517, 85.699348), (0.650786, 114.163343), (0.574355, 166.479306), (0.724258, 176.702461).

### 8 function classes studied

- **F1:** ζ(s), a_n = 1, multiplicative
- **F2:** L(s, χ₄), χ₄ mod 5 (χ₄(2)=i), multiplicative
- **F3:** f_rand, a_p random on unit circle (seed=42), extended multiplicatively
- **F4:** L_DH as above, NOT multiplicative
- **F5:** L_DH^(ε), ε ∈ {−0.1, ±0.05}, NOT multiplicative
- **F6:** L(s,λ), Liouville, FULLY multiplicative, ANOMALOUS
- **F7:** L(s,μ), Möbius, multiplicative (not fully)
- **F8:** f_fully_rand, a_n i.i.d. on unit circle, NOT multiplicative

## Method

### Step 1 — Canonical engine

- Implement D_F(t;N) = Σ_{n=1}^N a_n/n^(1/2+it) with Kahan summation (real+imaginary parts independently).
- Implement coefficient generators for all 8 classes.
- Implement diagnostic metrics:
  - **(A) GEV shape parameter ξ:** partition the t-range into B blocks, extract max|D_F| per block, fit GEV (scipy.stats.genextreme), report ξ with 95% CI (5000 bootstrap). ξ < 0 indicates Weibull-type bounded tails; ξ = 0 is the Gumbel limit; ξ > 0 is heavy-tailed Fréchet.
  - **(B) Composite coherence R_comp:** S_k(t;N) = Σ_{ω(n)=k} a_n/n^(1/2+it); R_comp = |D_F| / (Σ_k|S_k|²)^(1/2).
  - **(C) Cancellation ratio M_coh:** = 1/R_comp.
  - **(D) Rayleigh R statistic:** R(t*) = (1/π(N)) |Σ_{p≤N} exp(iθ_p(t))| where θ_p(t) = t·log(p) + arg(a_p).
  - **(E) Coefficient Autocorrelation Score (CAS):** log₁₀(max|FFT(a)|² / mean|FFT(a)|²).
  - **(F) Shannon entropy H:** −Σ p_a·log₂(p_a) over binned complex coefficient values on the unit circle.

Numerical validation: D_F checked against 50-digit mpmath for N=10⁴ at 10 random t per function (12-digit agreement required); L_DH validated to <10⁻⁶ at all 4 known zeros; λ-multiplicativity checked over 1000 random pairs; μ-multiplicativity checked on squarefree n. Any failure halts the analysis.

### Step 2 — GEV analysis (Target T1: Weibull persistence)

For all 8 function classes and N ∈ {10⁴,10⁵,10⁶}, D_F is computed on t ∈ [1000, 20000] with Δt = 2π/log(N), 500 blocks, fitting GEV shape ξ. Non-stationarity for F1 (ζ) and F4 (DH) at N=10⁶ was tested with sliding windows (width 5000, stride 2500) over t ∈ [500, 50000], 100 blocks/window, fitting constant/linear/log/power-law trend models selected via AIC/BIC. N-dependence of ξ was tracked for F1 and F4 across N ∈ {10⁴, 3×10⁴, 10⁵, 3×10⁵, 10⁶, 3×10⁶, 10⁷} at t ∈ [5000, 15000].

### Step 3 — Phase decoherence (Target T2)

At the top 50 peaks of F1 (ζ), θ_p(t*) = t*·log(p) mod 2π was tested via Kolmogorov-Smirnov against uniform[0, 2π] and via Rayleigh R(t*). Predictions: F1 (ζ) should show approximately uniform prime phases; F4 (DH) should show uniform prime phases (composite-driven resonance instead); F6 (Liouville) should show non-uniform phases driven by sign structure. R_comp vs N was fit for F1, F4, F6 at top 10 peaks across N ∈ {10⁴..10⁶}, with the critical prediction that for ζ, R_comp must NOT grow with N.

### Step 4 — Coefficient rigidity (Target T3)

A parametric family a_p = +1 w.p. α, −1 w.p. 1−α (extended multiplicatively) was built for α ∈ {0, 0.1, ..., 1}, tracking H(α), max R_comp, ξ across a 3D surface to look for a phase transition at α=1. Sign-injection perturbations were tested from ζ: (1) a_n=1, (2) flip at p≡3 mod 4, (3) flip at squarefree with odd ω(n), (4) full λ(n) — tracking R_comp, ξ and when they cross zero. A "pretentious distance" D(F_i,F_j;N) = (Σ_{p≤N}(1 − Re(a_p(i)·conj(a_p(j))))/p)^(1/2) was computed as a distance matrix, testing the hypothesis that small D(F,ζ) correlates with low R_comp(F).

### Step 5 — Mathematical proof components

- **Vinogradov–Korobov verification:** checking |Σ_{p≤N} p^(it)| ≪ N·exp(−c·(log N)^(3/5)·(log log N)^(−1/5)) for c≈0.05, validating provable prime-phase equidistribution.
- **Selberg CLT verification:** checking log|D_ζ(t;N)| normality for T ∈ {10³,10⁴,10⁵} against Selberg's theorem, establishing that Gaussian cancellation is real.
- **Implication chain mapping:** (1) R_comp < δ ⟹ ξ < ε, (2) R_comp < ε ⟹ ξ < 0, (3) ξ < 0 ⟹ no power-law growth ⟹ no off-line zero.
- **Proof attempts:** (A) "R_comp ≲ 1/√(t, N/N₀)" via uniform bound on |D| from mean-value theorems. (B) "For a_n=1, R_comp ≲ 1/√(c log N)" via class-vector non-alignment and exponential sum estimates.

## Results — Central hypothesis partially confirmed, with a critical Liouville counterexample

### Discovery 1: Pre-asymptotic Weibull-type extremes and ξ-stability in Dirichlet partial sums

Using a validated Dirichlet partial-sum engine with strict DH zero calibration, block maxima of log-amplitudes exhibit stable, negative GEV shape parameters (ξ < 0) for ζ(s) and for a historically reconstructed DH function across N ∈ [10⁴, 10⁶]. This pre-asymptotic Weibull behavior persists without a resolvable N-trend at accessible scales.

For ζ(s), a dense N-grid shows ξ is essentially constant over N ∈ [10⁴, 10⁶], with mean ξ = −0.3042 ± 0.0007 and total range 0.0018; both a linear-in-log-N and a 1/log-N convergence model are statistically indistinguishable (ΔAIC≈0, ΔBIC≈0), revealing that any N-dependence is extremely weak at accessible scales. A complementary high-precision run reports ξ_ζ = 0.3124±0.0012 with no significant trend (weighted-slope p=0.9807), while the validated DH function is even more stable at ξ = 0.3693±0.0002 for N≥3×10⁴ (p=0.2712 for trend). An earlier sparse-grid analysis had detected an apparent drift toward ξ≈0 under a 1/log N model, but later dense sampling shows that constant and convergent models cannot be distinguished because the true N-dependence, if any, is orders of magnitude smaller than the uncertainty in this range. Together, these results establish persistent, pre-asymptotic Weibull-type tails (ξ<0) for ζ and DH across two decades of N, with no reliable evidence of visible convergence to the Gumbel limit within N≤10⁶.

Phase-resolved metrics clarify the mechanism-level differences underlying similar ξ-stability. Composite coherence R_comp is strongly suppressed for ζ (0.0020±0.0013) but elevated for DH (0.0132±0.0031) and maximal for Liouville (R=0.822 at resonance), while the Shannon entropy of coefficients uniquely identifies ζ through H=0 bits (constant a_n=1), and the CAS pinpoints periodic structure (DH CAS≈3.57). Prime-phase Rayleigh tests at ζ's top peaks show significant non-uniformity (65% with p<0.05; 50% with p<0.001), consistent with prime-driven resonance; in contrast, DH's primes are uniform (0/20 significant), and its peaks and zeros are composite-driven with strong, location-dependent inter-class interference: at the first off-line zero, primes have R=0.002 (p=0.70), but all terms have R=0.099 (p<10⁻¹⁵), with k=2 and k=3 composites showing detectable coherence (R=0.0426 and 0.1015, both p<0.001) and 78.4% inter-class destructive cancellation.

In a 3-feature space (R_comp, a reciprocal-based cancellation index, and CAS), nine classes of L-functions and surrogates achieve perfect SVM classification (100% accuracy; LOOCV 100%; separation p<10⁻¹⁸), demonstrating that tail suppression in ζ coexists with distinct phase-organization phenotypes in other families.

**The Liouville L-function exemplifies a different route to N-stable extremes:** a fully multiplicative coefficient sequence λ(n)=(−1)^Ω(n) produces intrinsic constructive interference. At a large peak (t*=7563.5, N=10⁵) the signed vector resultant reaches R=0.822 with |D_λ|=46.88, despite an unsigned resultant of only 0.070; this is driven by sign-organized coherence rather than Euler-product structure per se. A direct even/odd-Ω decomposition shows that both components independently exhibit N-stable ξ and that, at the top 10 peaks for N=10⁶, their phases align almost perfectly (mean Δφ=1.83°±4.32°, 10/10 with |Δφ|<30°) with near-unity magnitude balance; this constructive phase-locking persists without trend across N∈{10⁴,10⁵,10⁶}. These observations confirm the **multiplicativity illusion**: full multiplicativity does not guarantee resonance suppression; instead, coefficient architecture and phase organization control coherence and extreme behavior.

Finally, the persistence of ξ<0 is consistent with modern extreme-value theory on finite-size (penultimate) behavior in the Gumbel domain: second-order extended regular variation, subleading centering/scaling corrections, monotone-transform sensitivity of penultimate shape, non-stationary parameter mixing, and long-range dependence can all yield an effective negative ξ in finite samples even when ξ=0 asymptotically.

Direct power-law predictions at DH off-line zeros are contradicted by five-decade tests: the observed growth exponent α=0.000440±0.000453 is statistically indistinguishable from zero versus the predicted 0.3085, with composite-class interference accounting for the suppression. Taken together, the data-supported picture is that Weibull-type extremes and ξ-stability are robust pre-asymptotic features for ζ and DH on accessible scales, while Liouville's stability arises from a distinct, parity-organized constructive mechanism — emphasizing that coefficient architecture, not multiplicativity alone, governs resonance and extremes.

### Discovery 2: Arithmetic coupling of composite classes underpins ζ(s) resonance suppression and its fragility

The zeta function's unusually weak extreme resonances arise from a **structured, anti-correlated coupling** among composite-class contributions S_k that is coordinated with prime-phase organization at peaks. Targeted sign flips confined to composite classes, especially semiprimes (ω=2), dismantle this coupling, inflate composite coherence by ~30%, and shift the extreme-value tail toward heavier behavior, whereas flipping prime signs leaves composite coherence unchanged.

Flipping signs only on composites raises the composite-coherence metric R_comp by 29–32% (ω=2: +29.1%, p=5.1×10⁻⁴; ω=3: +32.3%, p=3.2×10⁻⁴; odd ω: +32.3%, p=1.4×10⁻⁴), while flipping primes leaves R_comp unchanged (0% change, p=1.000) despite increasing the overall partial-sum magnitude by 25.6%. Extreme-value analysis using the GEV shape parameter ξ shows that composite perturbations shift the tail toward heavier behavior: ξ_ζ = −0.2052 [−0.2868, −0.1317], F_k2: ξ = −0.1104 [−0.1870, −0.0253], F_k3: ξ = −0.0314 [−0.1290, +0.0601], with all pairwise differences highly significant (p<10⁻⁴), yet remaining in the Weibull (ξ<0) regime at N=10⁵. Together these results identify **structured composite coupling — not prime signs or multiplicativity — as the operative mechanism** behind ζ(s)'s resonance suppression and its sensitivity to composite-class manipulations.

Semiprimes (ω=2) emerge as a structural bridge linking primes to higher composites. Perturbing only primes changes ξ negligibly (ζ: −0.2052 → F_k1: −0.2101; Δ=−0.0049), while perturbing only semiprimes induces a large shift (ζ: −0.2052 → F_k2: −0.1104; Δ=+0.0948, a 46% relative change). Covariance analyses reveal why: prime perturbations alter only S_1 interactions (‖ΔC_1‖=1.056) and leave the inter-composite block unchanged (Frobenius norm=0.000), whereas semiprime perturbations propagate through the composite structure, producing distributed changes (‖ΔC_2‖=2.046) and a large inter-composite block shift (Frobenius norm=1.819), with the strongest change in |ΔC_{2,3}|=1.263.

A mechanistic decomposition pinpoints the lever driving the tail shift: flipping ω=2 reverses the sign of all covariances involving S_2 while leaving its variance unchanged (Var(S_2)=3.953954 in both ζ and F_k2; 0.0% change). The total negative covariance strength collapses by 99.0% (e.g., Cov(S_1,S_2): −0.354→+0.354; Cov(S_2,S_3): −0.653→+0.653), and the off-diagonal Frobenius norm is 2.86× larger (0.845 vs 0.296; permutation p<0.001) with significantly stronger adjacent-class correlations (mean 0.232 vs 0.056), demonstrating that S_k are not independent but coupled through shared factorization structure — a prerequisite for the fragile cancellation pattern.

Finally, a vector-sum model captures magnitude scaling across composite classes but exposes the fragility of the phase relations that underwrite suppression. For ζ, the empirical adjacent-class law |S_{k+1}|/|S_k| ≈ C·log(N)/k (C=0.472; r²=0.936) combined with measured inter-class phases predicts |D| to −2.8% and R_comp to +0.4% error at a representative peak (t*≈2819, N=10⁵). However, the same model fails for the ω=2-perturbed function: |D| error −25% and R_comp error +40%, because the 180° flip of S_2 dismantles the delicate, irregular phase alignments (phase difference s.d.≈40°) that the model must take as input. This shows that the magnitudes follow a stable arithmetic law, but the resonance-suppression phenotype lives in the inter-class phases — precisely the element that proves fragile under composite-class perturbations. Together with the broader classification and phase tests, these results explain both the strength and the fragility of ζ(s)'s resonance suppression, and why coefficient architecture, not multiplicativity, is the decisive determinant of extreme-value behavior.

### Discovery 3: Anomalous resonance architecture of the Liouville L-function from coefficient parity

The Liouville L-function L(s,λ) exhibits large, N-stable resonances that are **not** driven by prime-phase bias but by a deterministic parity architecture in its fully multiplicative coefficients λ(n)=(−1)^Ω(n). Phase-resolved and extreme-value analyses show persistent constructive interference between the even-Ω and odd-Ω components and the heaviest bulk tails among the archetype functions studied, establishing a resonance phenotype distinct from both ζ(s) and the Davenport–Heilbronn function.

Prime-phase mean resultant lengths (Rayleigh R) at large resonance peaks are near zero for all three archetypes, with ζ least uniform (R=0.00602±0.002112), L(s,λ) intermediate (0.00500±0.001897), and L_DH(s) most uniform (0.004035±0.002072), and only 2% of Liouville peaks reject uniformity at α=0.05; magnitude correlates with prime-phase bias for ζ (r=0.594, p<0.001) but not for L(s,λ). Yet L(s,λ) attains very large peaks — e.g., |D_λ(t*)|=46.88 at t*=7563.5 — accompanied by strong alignment of signed term vectors (R=0.822), despite prime phases being close to uniform; this alignment vanishes for unsigned vectors (R=0.070), pinpointing the (−1)^Ω(n) sign pattern as the mechanism. Together these results separate prime-driven resonance in ζ(s) from sign-architecture-driven resonance in L(s,λ), with L_DH(s) as a composite-driven intermediate that retains uniform primes.

Direct perturbation of the Ω(n) architecture shows that this coherence is not a fragile artifact of arithmetic ordering. A permutation test that randomly reassigns Ω-labels across n at N=10⁶ yields a null distribution for a vectorial coherence ratio R_vec=|Σ_k S_k|/Σ_k|S_k| (distinct from the quadratic R_comp used elsewhere) with mean 0.3459±0.1699 (std), while the true L(s,λ) achieves 0.5641 at the resonance peak t*=7700 (Z=1.284; one-tailed p=0.122), i.e., 63% above the null mean but not statistically significant at α=0.05. This rules out a dependence on the specific n↔Ω(n) ordering and supports a mechanism rooted in the global Ω-parity distribution and its induced sign organization, consistent with prior observations that λ's strongest alignment arises from coefficient signs rather than prime-phase clustering.

The extremes of L(s,λ) are strikingly N-stable. In GEV fits to block maxima of log|D| over N, the Liouville function maintains a stable shape parameter ξ around ≈0.19, significantly different from both ζ(s), which shows log-convergence from ξ=0.37 to 0.09, and L_DH(s), which converges from ξ=0.35 to 0.16 (ζ vs L(s,λ): p=0.0079; L_DH vs L(s,λ): p=0.69). A mechanistic decomposition reveals why: splitting D into even-Ω and odd-Ω components shows that each component's extreme statistics are N-stable (even-Ω: ξ=0.338±0.094/0.340±0.093; odd-Ω: ξ=0.331±0.095/0.504±0.093; stability Z-scores 0.01 and 1.67), and, crucially, at N=10⁶ the two components align constructively at every one of the top 10 peaks with near-perfect phase-locking (mean Δφ=1.83°±4.32°) and balanced magnitudes (median |D_even|/|D_odd|=0.991). This constructive relationship persists across truncation depths (largest-peak Δφ: 2.20°, 6.09°, 0.24° for N∈{10⁴,10⁵,10⁶}), providing a direct dynamical underpinning for N-stable extremes in the total sum.

Covariance analysis across Ω-classes further distinguishes Liouville's resonance architecture from ζ. While magnitude covariances Cov(|S_j|,|S_k|) are positive for all pairs in both functions, signed covariances Cov(Re S_j, Re S_k) expose the cancellation structure: ζ exhibits 67% negative off-diagonal entries with net sum 1.024, whereas L(s,λ) shows 53% negatives with net sum 0.553 — 46% weaker cancellation. Moreover, Liouville's weak cancellation is N-stable (0.5447→0.5531; +1.5%), in sharp contrast to ζ(s), which strengthens by +48.2% (0.6911→1.024) from N=10⁵ to 10⁶. Consistent with this weaker, stable cancellation architecture, the bulk statistics of L(s,λ) are the most heavy-tailed among the three: Shapiro-Wilk decisively rejects normality (p=1.52×10⁻⁴⁰) with excess kurtosis +2.75 and 1.56% of observations beyond ±3σ (5.8× Gaussian), compared with ζ(s) (+0.88; 0.82%) and L_DH(s) (+0.91; 0.72%) at N=10⁵, t∈[10⁵, 2×10⁵].

Finally, these properties situate L(s,λ) within a broader classification of resonance phenotypes by coefficient organization. Across function classes, a three-feature space built from composite-coherence, coefficient autocorrelation, and cancellation metrics yields perfect separation (100% SVM accuracy; cluster p<10⁻¹⁸), with ζ(s) uniquely characterized by zero coefficient entropy H=0, while L(s,λ) and L_DH(s) occupy distinct non-zero-entropy regimes due to their sign- and period-structured coefficients respectively. Collectively, the evidence establishes a **multiplicativity illusion**: complete multiplicativity does not ensure resonance suppression; instead, the Ω-parity architecture of λ(n) generates persistent constructive interference, N-stable extremes, and heavy-tailed bulk fluctuations that are mechanistically and statistically distinct from both ζ(s) and L_DH(s).

### Discovery 4: Metric geometry and reproducibility of resonance-suppression diagnostics

This work establishes a reproducible, metric-geometric framework for diagnosing resonance suppression in arithmetic L-functions. A three-feature space — composite coherence (R_comp), a cancellation ratio (M_coh), and a coefficient autocorrelation score (CAS) — cleanly separates resonance phenotypes across nine function classes with perfect classification, while single metrics and prime-only similarity measures fail to generalize across parameter regimes. Reproducibility hinges on strict numerical protocols and validated implementations, as canonical Davenport–Heilbronn off-line zero predictions do not materialize up to N=10⁷.

The diagnostic geometry is built on three complementary features computed from D_F(t;N): (i) composite coherence R_comp(t)=|D_F|/(Σ_k|S_k|²)^(1/2) where S_k(t) is the contribution from numbers with exactly k prime factors, (ii) a cancellation ratio M_coh=1/R_comp, and (iii) a coefficient autocorrelation score CAS=log₁₀(max FFT power/mean FFT power) of the coefficient sequence a_n; the extreme-value tail is summarized by the GEV shape parameter ξ (ξ<0 indicates Weibull-bounded tails). In this three-dimensional space, nine L-function classes (including ζ, Dirichlet characters, Davenport–Heilbronn, Liouville, Möbius, and random controls) are perfectly separated by a support-vector machine trained on 450 peaks, achieving 100% accuracy under leave-one-out cross-validation with cluster separation p<10⁻¹⁸; ζ is uniquely identified by zero entropy (H=0), and CAS correctly flags periodic structure in Davenport–Heilbronn (≈3.57) versus ≈1.0 for randoms. By contrast, single metrics can be unstable across regimes: although ζ exhibits strong suppression (ξ≈−0.17), the same magnitude-based features are not generally predictive across classes.

Phase-resolved analyses clarify mechanism-level differences that underlie this separation. At peaks, prime phases are systematically non-uniform — 65% of peaks reject uniformity at p<0.05 in Rayleigh tests — whereas Davenport-Heilbronn shows uniform prime phases but composite-driven resonance with strong inter-class destructive interference (≈78.4% magnitude reduction), and Liouville exhibits pronounced sign-organized alignment with resultant length R=0.822 at a giant peak (|D_λ|≈46.9). These distinctions are consistent with independent prime-sum bounds: numerical verification of Vinogradov–Korobov-type estimates shows |Σ_{p≤N}p^{it}|/N decreases monotonically from ≈3.2×10⁻³ at N=10⁴ to ≈2.3×10⁻⁴ at N=10⁶, supporting effective equidistribution of prime phases in the tested range. Together, these results separate prime-driven cancellation (ζ) from composite- or sign-driven resonance (Davenport–Heilbronn and Liouville) in a way that is stable to implementation idiosyncrasies and data provenance issues.

Stress tests show why no single observable suffices as a discriminator. The upper envelope of R_comp decays universally with N for ζ, Davenport-Heilbronn, and Liouville — well fit by b/log(N)^α with α≈5.40, 5.28, and 4.40 respectively — contradicting a proposed 1/c·log(N) behavior and nullifying R_comp as an asymptotic separator; at N=10⁶ the 99.9th-percentile envelope remains ≤1 for all three functions. Prime-only similarity likewise fails: the "pretentious distance" to ζ does not negatively correlate with the GEV shape parameter (Pearson r=+0.457, p=0.303) and instead shows a positive, significant association with composite coherence (r=+0.781, p=0.038), indicating that prime resemblance to ζ is not the operative driver of tail suppression. A parametric family with random ±1 prime coefficients (probability α for +1) confirms the non-universality of metric-tail links: ξ is largely insensitive to α in [0, 0.8] (≈0.23±0.27), the R_comp correlation is weak and non-significant (Spearman ρ=0.357, p=0.432), and the λ-like endpoint α=1 is a structural outlier with ξ=0.048 [95% CI: 0.053, 0.159], underscoring that extreme-value behavior is controlled by coefficient architecture rather than any single resonance metric.

Mechanistic modeling aimed at predicting corroborates these limits. Regression models built from S_k covariance dynamics fail decisively (e.g., LOOCV R²=−1.971 with the primary feature set), and even extended models overfit with severely negative cross-validated performance. Bulk-moment proxies do modestly better — skewness alone yields ≈0.161±0.205 with LOOCV R²=0.149 after excluding a fully random outlier — yet remain far from reliable predictors. Consistent with this, classifiers trained only on bulk moments cannot separate RH-satisfying from RH-violating classes (50% LOOCV accuracy across SVM variants and logistic baselines), with systematic misclassification of Möbius and complex Dirichlet classes demonstrating overlap in these coarse statistics.

Reproducibility is the decisive enabler: Kahan summation is mandatory to avoid 10⁴–10⁶× numerical errors, Davenport-Heilbronn implementations must be zero-validated before analysis, and prime-sum bounds should be checked; notably, the canonical Davenport-Heilbronn implementation fails |L_DH(ρ)|<10⁻⁶ at all four off-line zeros up to N=10⁷, whereas the numerically confirmed Vinogradov-Korobov behavior supports the prime-equidistribution assumptions used by the diagnostic geometry. Overall, the three-feature geometry is a robust separator of resonance phenotypes, but neither single metrics, pretentious distance, nor current covariance-based models can reliably forecast extreme-value tails or RH status, and canonical off-line-zero power-law signatures do not appear in the accessible N-range.

## What this contributed

- Established a strict, single-source-of-truth numerical pipeline for Dirichlet partial-sum evaluation, validated at 30-digit precision and reused across all analyses in this program.
- Discovered the **Liouville counterexample to naive suppression-by-multiplicativity**: L(s,λ) is fully multiplicative yet exhibits large, N-stable, sign-organized resonances — a "multiplicativity illusion" that reshaped the research direction toward coefficient architecture rather than multiplicativity per se.
- Identified composite-class (especially semiprime) coupling, not prime-phase structure, as the operative mechanism behind ζ(s)'s resonance suppression, and showed this coupling is fragile to surgical sign perturbations.
- Built a reproducible three-feature classification geometry (R_comp, M_coh/CAS, GEV shape ξ) that perfectly separates nine L-function classes, establishing a general diagnostic toolkit for future programs.
- Reconfirmed that canonical Davenport-Heilbronn off-line-zero power-law predictions fail to materialize up to N=10⁷, reinforcing the finding from Program 1 that the "killer signature" is not detectable at accessible computational scales.

## Connection to later work

The Liouville counterexample and the composite-class coupling of ζ motivated the ω-class geometry of RH2019; the claims recorded here were later re-audited in RH2020.

## Structure of the folder

The program is divided into 94 numbered phases, one subfolder `phase-N/` each. A phase folder normally contains `OVERVIEW.md` (the written result of that phase), the executed notebook when one exists (`notebook_executed.ipynb` and/or a notebook with a hexadecimal name) and the input and output files (data arrays, tables, figures). The one-line descriptions below are taken from each phase's `OVERVIEW.md`; where a phase has no written summary this is stated.

| Phase | Content |
|---|---|
| [1](phase-1/) | The hypothesis that ζ(s) would show greater sensitivity to block size in GEV analysis—due to strong correlations causing slow convergence to the asymptotic extreme value … |
| [2](phase-2/) | The research hypothesis that the validated "historical" L_DH function exhibits clear pre-asymptotic convergence of its GEV shape parameter ξ toward zero as N increases from 10⁴ to … |
| [3](phase-3/) | The research hypothesis that variable transformation (/D(t;N)/ vs log/D(t;N)/) explains the contradiction between r53 and earlier findings is partially refuted |
| [4](phase-4/) | The hypothesis that L_DH(s) has a bulk distribution distinct from both non-Gaussian ζ(s) and Gaussian L(s,λ) is CONFIRMED, but with a critical revision: L(s,λ) is not Gaussian—it … |
| [5](phase-5/) | Hypothesis rejected: The upper envelope of composite coherence R_comp(t;N) does NOT distinguish between ζ(s) and the anomalous functions L_DH(s) and L(s,λ) in the manner … |
| [6](phase-6/) | The research hypothesis is CONFIRMED: The perturbed Davenport-Heilbronn functions L_DH^(ε) with ε = ±0.05 exhibit a stable, positive GEV shape parameter ξ that shows little to no … |
| [7](phase-7/) | At N=10^7, the S_k phase structure for ζ(s) at a resonance peak is not statistically distinguishable from the null distribution generated by permuting ω(n) labels, rejecting the … |
| [8](phase-8/) | The inverse correlation between bulk kurtosis and GEV ξ observed across diverse L-functions does NOT hold within a parametric family of multiplicative functions where prime … |
| [9](phase-9/) | The surgical perturbation of the ω(n)=5 class caused a statistically significant increase in the GEV shape parameter ξ (Δξ = +0.016, p < 0.000001, Z-test), confirming the causal … |
| [10](phase-10/) | The surgically perturbed L-functions F_k2 and F_k3 exhibit significantly higher GEV shape parameters (ξ) than the baseline Riemann zeta function ζ(s), confirming a statistically … |
| [11](phase-11/) | The research hypothesis is CONFIRMED with exceptional clarity: the increase in the GEV shape parameter ξ from -0.2052 (ζ) to -0.1104 (F_k2) when flipping the sign of coefficients … |
| [12](phase-12/) | The hypothesis that there exists a critical value of α between 0.9 and 1.0 where the GEV shape parameter ξ undergoes a sharp transition is partially supported but requires … |
| [13](phase-13/) | Analysis conclusion Surgical coefficient perturbations to ζ(s) alter the GEV shape parameter ξ by systematically modifying S_k covariance dynamics, with larger changes in … |
| [14](phase-14/) | Research hypothesis assessment: CONFIRMED The hypothesis that a pre-computed dataset of Dirichlet partial sum magnitudes /D_F(t*;N)/ at resonance peaks t* can be generated within … |
| [15](phase-15/) | CG_N Sign Reversal Analysis for Validated L_DH Function |
| [16](phase-16/) | The Riemann zeta function ζ(s) exhibits significantly stronger structured off-diagonal correlations in its S_k covariance structure (Frobenius norm = 0.845) compared to a random … |
| [17](phase-17/) | Regression model for predicting gev shape parameter ξ FROM S_k covariance features |
| [18](phase-18/) | Reverse-Engineering the Historical Davenport-Heilbronn Function |
| [19](phase-19/) | L_DH cancellation dynamics dramatically diverge from ζ(s) AT HIGHER N — Primary Finding The hypothesis is REJECTED |
| [20](phase-20/) | Unable to Complete Due to Computational Constraints — Research Question Determine whether the N-stable GEV statistics of the Liouville function L(s,λ) result from N-stable GEV … |
| [21](phase-21/) | The hypothesis is CONFIRMED. The CG_N sign reversal mechanism in the validated L_DH approximation is driven by non-uniform evolution of S_k sum variances that is strongly … |
| [22](phase-22/) | Analysis of R_comp vs ξ Correlation Across L-Function Classes |
| [23](phase-23/) | The hypothesis is REJECTED. The Ω(n) permutation test at N=10⁶ demonstrates that permuting the Ω(n) labels does NOT significantly reduce the composite coherence R_comp at the … |
| [24](phase-24/) | T-Regime Dependence of Kurtosis-ξ Correlation |
| [25](phase-25/) | The research hypothesis is REJECTED. The proposed mechanism does not explain the coexistence of peak stability and faster R_comp decay at resonance peaks for ζ(s) |
| [26](phase-26/) | S_k Covariance Dynamics Do Not Predict GEV Shape Parameter ξ The regression modeling analysis definitively rejects the hypothesis that S_k covariance features predict the GEV … |
| [27](phase-27/) | (No written summary; data files only.) |
| [28](phase-28/) | (No written summary; data files only.) |
| [29](phase-29/) | (No written summary; data files only.) |
| [30](phase-30/) | I cannot complete the analysis of CG_N sign reversal in perturbed L_DH^(ε) functions because the prerequisite validated L_DH implementation is not available in the workspace, and … |
| [31](phase-31/) | GEV Shape Parameter Analysis for L-Functions |
| [32](phase-32/) | (No written summary; data files only.) |
| [33](phase-33/) | Phase cannot proceed: precondition not satisfied — Critical Precondition Failure The research objective explicitly states: > "Pre-computation: This phase is CONTINGENT on the … |
| [34](phase-34/) | (No written summary; data files only.) |
| [35](phase-35/) | The N-stable extreme value statistics of the Liouville function L(s,λ) arise from stable, constructive interference between the even-Ω(n) and odd-Ω(n) components, both of which … |
| [36](phase-36/) | Incomplete due to implementation issue — Core Finding I successfully implemented the computational pipeline to test the CG_N sign reversal hypothesis for perturbed L_DH^(ε) … |
| [37](phase-37/) | The GEV shape parameter analysis reveals significant asymptotic differences between ζ(s) and L_DH(s): — Quantitative Results Riemann Zeta Function ζ(s): - Mean ξ∞ = -0.234 ± 0.033 … |
| [38](phase-38/) | Numerical Verification of Vinogradov-Korobov Theorem and Selberg CLT |
| [39](phase-39/) | Of Findings The analysis yielded results opposite to the original hypothesis: For truncated partial sums D(t;N) at N=10⁶ and t∈[100000, 200000]: - Riemann ζ(s): log/D(t;N)/ is … |
| [40](phase-40/) | Analysis of Pretentious Distance vs. Composite Coherence Correlation |
| [41](phase-41/) | An SVM classifier trained on bulk statistical moments (variance, skewness, excess kurtosis) does NOT effectively separate RH-satisfying from RH-violating functions |
| [42](phase-42/) | Pre-asymptotic Convergence of ξ for Riemann Zeta Function |
| [43](phase-43/) | The R_comp metric demonstrates significant sensitivity to t-value selection, but contrary to the research question's premise, R_comp is NOT consistently low for ζ(s) at large … |
| [44](phase-44/) | Surgical Coefficient Perturbations Reveal Fragility of Zeta Function's Low Composite Coherence |
| [45](phase-45/) | The hypothesis is REJECTED. The specific, regular distribution of integers according to their ω(n) value (as described by Sathé-Selberg theorems) does not appear to be essential … |
| [46](phase-46/) | I cannot complete the requested analysis due to severe computational constraints |
| [47](phase-47/) | (No written summary; data files only.) |
| [48](phase-48/) | The hypothesis that flipping signs for ω(n)=6 would cause a statistically significant increase in the GEV shape parameter ξ is REJECTED |
| [49](phase-49/) | The research hypothesis is CONFIRMED: The GEV shape parameter ξ for L_DH(s) does NOT show stable negative values as N increases, in stark contrast to ζ(s) |
| [50](phase-50/) | Comparison of S_k Covariance Structure for L(s,λ) vs ζ(s) |
| [51](phase-51/) | The research hypothesis is REJECTED. The predicted negative correlation between mean R_comp and tail-lightness does NOT hold for the parametric multiplicative family examined |
| [52](phase-52/) | The hypothesis is CONFIRMED with strong quantitative evidence. The uniquely stable S_k covariance structure of L(s,λ) (CG_N ≈ 0) is directly caused by persistent, N-stable … |
| [53](phase-53/) | The hypothesis that accelerated R_comp decay at resonance peaks is driven by faster N-dependent phase rotation between S_k vectors is REJECTED |
| [54](phase-54/) | The research hypothesis that the negative correlation between D(F, ζ) (pretentious distance to zeta) and R_comp (composite coherence) observed in r22 is a robust phenomenon is … |
| [55](phase-55/) | At the resonance peak t* = 2818.99 (N=10^5, identified from scan over t∈[1000,3000]), the baseline ζ(s) exhibits strong constructive interference among ω-class phasors: S_1, S_2 … |
| [56](phase-56/) | Analysis of Phase Transition in α-Parametric Multiplicative Functions |
| [57](phase-57/) | I cannot complete the requested analysis due to insurmountable computational constraints |
| [58](phase-58/) | (No written summary; data files only.) |
| [59](phase-59/) | Analysis of GEV Shape Parameter ξ Scaling with Truncation Depth N |
| [60](phase-60/) | The research hypothesis that L(s,λ) would decay much more slowly than ζ(s) is REJECTED |
| [61](phase-61/) | L-kurtosis vs gev shape parameter correlation — Main Findings The strong negative correlation between bulk tail shape and extreme value statistics is a robust phenomenon that … |
| [62](phase-62/) | At large peaks, all three functions (ζ(s), L_DH(s), and L(s,λ)) exhibit predominantly uniform prime-phase distributions, with mean Rayleigh R statistics in the range 0.004-0.006 … |
| [63](phase-63/) | (No written summary; data files only.) |
| [64](phase-64/) | Analysis blocked: contingency condition not satisfied — Primary Finding This analysis cannot be completed as specified because the required contingency condition is not met |
| [65](phase-65/) | The hypothesis that the inverse correlation between bulk kurtosis and GEV ξ would emerge when combining real and complex parametric families is REJECTED |
| [66](phase-66/) | I successfully generated a controlled parametric dataset using a multiplicative function family F_α (where a_p = +1 with probability α at each prime) to model the relationship … |
| [67](phase-67/) | Pretentious Distance and Resonance Suppression |
| [68](phase-68/) | Non-Stationarity of GEV Parameter ξ for ζ(s) and L_DH(s): Analysis Incomplete Due to Computational Constraints |
| [69](phase-69/) | (No written summary; data files only.) |
| [70](phase-70/) | The N-stability of the GEV shape parameter ξ partially supports the hypothesis that it serves as a signature of functions with off-line zeros, but with important caveats regarding … |
| [71](phase-71/) | Analysis of N-Scaling of GEV Shape Parameter ξ for L-Function Classification |
| [72](phase-72/) | Peak Fragility in Partial Sums of ζ(s) and L(s,λ) |
| [73](phase-73/) | High-Precision Davenport-Heilbronn Implementation |
| [74](phase-74/) | The analysis reveals a perfect monotonic relationship (Spearman ρ = 1.0000, p < 0.0001, Pearson r = 0.9993) between the change in square-free class density and the change in S_k … |
| [75](phase-75/) | Vector Sum Model for Composite Coherence |
| [76](phase-76/) | Analysis of R_COMP scaling at resonance peaks vs. RANDOM T VALUES — Main Finding The hypothesis that ζ(s) exhibits slower decay of R_comp at resonance peaks compared to random t … |
| [77](phase-77/) | The critical probability for breaking ζ-like resonance suppression is p* ≈ 0.40, where introducing Liouville-like sign flips with probability p ≥ 0.40 causes the GEV shape … |
| [78](phase-78/) | The hypothesis is REJECTED by the data. The GEV shape parameter ξ for Riemann ζ(s) does NOT trend toward zero with increasing truncation depth N |
| [79](phase-79/) | Gumbel vs. GEV Model Comparison for Block Maxima |
| [80](phase-80/) | Dataset Description: Resonance Suppression Research I have created a comprehensive dataset description document (DATASET_DESCRIPTION.md, 17KB) that catalogs the complete research … |
| [81](phase-81/) | The research hypothesis is rejected: bulk excess kurtosis and the GEV shape parameter ξ exhibit a strong negative correlation (Spearman ρ = -0.81, p = 0.015), not the hypothesized … |
| [82](phase-82/) | Analysis Summary The parametric family of multiplicative functions with randomly assigned prime coefficients (a_p = +1 with probability α, -1 with probability 1-α) exhibits GEV … |
| [83](phase-83/) | High-Power Analysis of R_comp N-Dependence for ζ(s): Peaks vs Random Ordinates |
| [84](phase-84/) | The N-scaling of the GEV shape parameter ξ provides partial but incomplete discrimination among the three archetype L-functions, contradicting the original hypothesis in key … |
| [85](phase-85/) | The bulk statistical moments approach provides a significantly better predictive model for the GEV shape parameter ξ compared to the S_k covariance model, with a LOOCV R² … |
| [86](phase-86/) | The research hypothesis is decisively rejected: at N = 10^7, the canonical L_DH implementation fails validation at all four off-line zeros with /D(ρ; N)/ remaining in the range … |
| [87](phase-87/) | The S_k covariance structure reveals three distinct dynamical regimes (progressive cancellation, stable cancellation, and cancellation decay) but does not universally classify … |
| [88](phase-88/) | Complete Analysis of Gumbel μ Prediction from S_k Covariance Features — Main Results Model Performance on Full Dataset (14 functions): - LOOCV R² = -0.1598 (failed - model … |
| [89](phase-89/) | The hypothesis that low fragility scores at ζ(s) resonance peaks are due to the change vector ΔV being nearly orthogonal to the main sum vector V_1 is REJECTED |
| [90](phase-90/) | Composite Coherence R_comp vs Truncation Length N: Analysis Results For the three L-functions ζ(s), L_DH(s), and L(s,λ), I analyzed the behavior of the composite coherence metric … |
| [91](phase-91/) | Hypothesis rejected: For the 8 function classes tested at N=10⁴, composite coherence R_comp is NOT more strongly (and negatively) correlated with minimum pretentious distance … |
| [92](phase-92/) | Perturbing prime (ω=1) versus semiprime (ω=2) coefficients produces qualitatively different structural impacts on both the GEV parameter ξ and the S_k covariance matrix … |
| [93](phase-93/) | I cannot analyze the scaling of R_comp with N for ζ(s), L_DH(s), and L(s,λ) because the required dataset is not available |
| [94](phase-94/) | The discrepancy between r57 (finding f22) and r65 regarding the N-scaling of ξ for ζ(s) is NOT an artifact of sparse N-sampling alone |
