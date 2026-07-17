# Research Programs 1–9 — The Empirical Base

These nine folders (`RH1` … `RH9`) are the **computational foundation** of the whole project:
nine large research programs. Together they produced the data, the calibrations, and the phenomenology that the
61-phase theoretical program (*Program 10*, [`../03-research/`](../03-research/)) was built on.

Each `RHk/` folder is a full local download of that program's run: one subfolder per
**task**, each containing an `OVERVIEW.md` (metadata + the full answer), the
executed notebook when available, and all input/output files.

## The nine programs

| # | Program | Tasks | Theme |
|---|---|---|---|
| RH1 | Resonance Detection and Class Separation in Arithmetic L-Functions | 89 | Resonance phenotype; ω-class separation (→ Arc A) |
| RH2 | Resonance Suppression for RH Proof | 95 | GEV / R_comp / CAS / Liouville parity |
| RH3 | Omega-Class Geometry of Dirichlet Polynomials at Large Values | 83 | ω-geometry at extreme peaks (large values) |
| RH4 | Omega-Stratified Conditional Covariance Reconstruction | 83 | Conditional cross-class covariance |
| RH5 | Inverse Spectral Positivity for Zeta Zeros | 60 | Inverse operator / Hilbert–Pólya angle |
| RH6 | Localized Weil Positivity and Omega-Class Moments | 68 | The localized Weil form + ω-moments |
| RH7 | Localized Weil Quadratic Form Detector | 43 | The detector Q = M_zeros − M_arith |
| RH8 | Localized Weil Form Stability and Monotonicity | 27 | Stability / monotonicity of the localized form |
| RH9 | Arithmetic Surface Lefschetz Structure for Zeta | 79 | Lefschetz / arithmetic-surface structure (mostly literature search) |

**Total:** 627 tasks across the nine programs across 10 years of work.

## Program summaries and key discoveries

### RH1 — Resonance Detection and Class Separation in Arithmetic L-Functions (2017)

Tests whether Euler-product (multiplicative) structure suppresses the coherent phase alignment ("resonance") needed for zeros off the critical line, using the Davenport–Heilbronn (DH) function — a non-multiplicative zeta-type function with **proven** off-line zeros — as calibration target.

- The predicted power-law growth |D_DH(γ;N)| ~ N^(β−1/2) at DH's known off-line zeros **failed decisively**: the fitted exponent was statistically indistinguishable from zero up to N=10⁹.
- A random multiplicative model — not DH — showed the heaviest tails and largest resonance scores, the opposite of the naive prediction.
- Phase decomposition resolved the mechanism: ζ's largest peaks are **prime-driven**, while DH's off-line-zero resonance is **composite-driven**, with universal inter-class destructive interference (M<1) shared by all tested classes.
- A metric-space classifier (composite coherence R_comp, cancellation ratio M, autocorrelation score CAS, coefficient entropy) achieved perfect separation of L-function archetypes across 350 peaks.
- The fully multiplicative Liouville function L(s,λ) showed the strongest resonance of any function tested, via intrinsic constructive interference — refuting "multiplicativity ⟹ suppression" outright.

### RH2 — Resonance Suppression for RH Proof (2018)

Extends the resonance-suppression program with strict methodological rules (single implementation, N-dependence tracking, honest reporting) across 8 function classes including Liouville and Möbius.

- Confirmed persistent, pre-asymptotic Weibull-type extreme-value tails (GEV shape ξ<0) for ζ and DH, stable across N∈[10⁴,10⁶].
- Discovered the **Liouville counterexample**: L(s,λ) is fully multiplicative yet exhibits large, N-stable, sign-organized resonance — a "multiplicativity illusion."
- Showed ζ's resonance suppression is driven by structured, fragile composite-class (especially semiprime) coupling, not by prime phases.
- Built a 3-feature classification geometry (R_comp, cancellation ratio, GEV shape) achieving perfect separation across nine L-function classes.

### RH3 — Omega-Class Geometry of Dirichlet Polynomials at Large Values (2019)

Maps how ω-classes (grouping integers by number of distinct prime factors) interact to produce peaks and troughs in Dirichlet partial sums, across three fronts: conditional anti-correlation, moment decomposition, and semiprime fragility.

- Found that inter-class energy at extreme peaks is **dominantly constructive**, not destructive as previously suggested — a prior "gold standard" negative value turned out to correspond to a trough, not a peak.
- Discovered a robust, non-monotonic structural anomaly in the fourth-moment ω-decomposition near N≈10⁵, present in ζ, Liouville, and DH but absent in i.i.d. null models.
- Identified a causal density rule for multiplicative functions (sparse systems are S₂-dominant, dense systems S₃-dominant) that DH decisively violates, remaining S₂-dominant despite 80% coefficient density.
- Built a Numba-accelerated evaluation engine (up to 37× speedup at N=10⁷) and invalidated a previously circulated list of DH off-line zero locations.

### RH4 — Omega-Stratified Conditional Covariance Reconstruction (2020)

A forensic re-validation program that re-checks tentative claims from RH2–RH3 before building an implication chain toward a publishable theorem about ω-class covariance.

- Resolved a normalization inconsistency in the DH coefficient phase (κ≈0.28408, not (1+i)/2), invalidating incorrect previously-circulated off-line zeros.
- Overturned the "67% negative off-diagonal covariance" claim via rigorous bootstrap re-analysis: peak-conditioned interference is dominantly **constructive**, and the ω=2 stratum is influential but not uniquely load-bearing.
- Discovered that class-averaged spectral entropy of the ω-stratified cross-term matrix is a near-perfect discriminator between GRH-true and GRH-false L-function families.
- Showed that differences in the cross-term matrix M_jk across L-functions are governed by **coefficient/conductor arithmetic**, not by off-line zero location — closing one inverse-spectral-reconstruction route.

### RH5 — Inverse Spectral Positivity for Zeta Zeros (2021)

Builds a single validated computational pipeline (zero generation, detection-power calibration, inverse-spectral reconstruction, positivity tests, topological data analysis) to search for rigorous RH-relevant numerical signatures.

- Established a sharp asymmetry: standard Li coefficients, Jacobi reconstructions, and Mercer-kernel positivity matrices are structurally **blind** to real-part (off-line) perturbations at feasible N, while real-part-aware topological data analysis and localized Weil quadratic forms are high-power detectors.
- Found two independent, high-power separators of the DH GRH violation: persistent H1 homology of spacing embeddings and the number-variance statistic Σ²(L).
- Delivered the program's central result: an **adaptively localized Weil quadratic form** (Hermite-Gauss basis, centered at the known off-line zero) produces a strictly negative minimum eigenvalue for DH while remaining non-negative for all GRH-consistent controls — the first proof-relevant, feasible-N detector of a GRH violation.

### RH6 — Localized Weil Positivity and Omega-Class Moments (2022)

Pushes the localized Weil detector from RH5 toward a rigorous statement, and executes the first ω-class moment decomposition of Dirichlet-polynomial moments against Keating-Snaith predictions.

- Established a geometry-tuned Weil quadratic form detector: with the arithmetic side correctly completed, it cleanly separates DH from GRH-conforming controls, shows δ² scaling in deformation magnitude, and gains super-polynomial sensitivity with basis dimension — while identifying the precise missing lemma (a uniform-in-basis truncation bound) needed for a proof.
- Executed the first ω-class decomposition of Dirichlet-polynomial moments: fractional second-moment allocations drift with N (Erdős-Kac redistribution) and never stabilize, but growth exponents and fourth-moment diagonal/off-diagonal structure give robust, sharply separating finite-N fingerprints.
- Showed that H0 topological persistence is only quadratically sensitive to real-part zero displacements (δ² scaling) and empirically fails to flag DH as an outlier — closing this TDA approach and redirecting attention to the Weil-form detector.

### RH7 — Localized Weil Quadratic Form Detector (2023)

Builds a canonical engine for the localized Weil quadratic form and drives toward the decisive question: is the uniform truncation lemma needed for a proof unconditional, conditional, or RH-equivalent?

- Validated a single canonical engine to machine precision across ζ, Dirichlet L(χ₄ mod 5), and the modular L(Δ,s); diagnosed the exact reason the DH benchmark can't be reproduced from public arithmetic-side definitions.
- Proved a finite-dimensional perturbation theorem: an off-critical zero at displacement δ forces λ_min(Q)<0 via a universal **δ² scaling law**, with an explicit low-rank operator predicting the numerical prefactor to better than 0.001% error — the program's central mathematical result.
- Derived a closed-form, unconditional (PNT-only) truncation-noise bound from Hermite-Gauss Fourier decay, validated across three L-function families.
- Delivered the headline verdict: **detecting** a fixed off-critical zero requires only unconditional PNT-level input, but **uniform convergence** of finite truncations to the true infinite Weil functional is **RH-equivalent** — precisely separating what's provable now from what would constitute a proof of RH.

### RH8 — Localized Weil Form Stability and Monotonicity (2024)

Empirically tests two structural hypotheses for the localized Weil form's minimum eigenvalue λ_min(Q): basis-completion stability as J→∞, and monotonicity in localization width σ and nested spectral windows.

- Built a canonical, specification-driven engine validating the explicit-formula trace identity to machine precision for ζ, L(χ₄ mod 5), and L(Δ,s), resolving prior L(Δ,s) difficulties as zero-refinement errors.
- Confirmed basis-completion stability (λ_min(Q) converges to the numerical floor) for all three GRH-respecting controls, provided the prime cutoff scales with 1/σ.
- Confirmed localization monotonicity (λ_min rises toward zero with wider σ and larger spectral windows), with no instance of a de Branges/Conrey-Li obstruction pattern.
- Discovered and fixed a critical bias for non-self-dual L-functions: the unsymmetrized explicit formula for L(χ₄ mod 5) produces a spurious trace defect; pairing χ with χ̄ eliminates it by 78 orders of magnitude.

### RH9 — Arithmetic Surface Lefschetz Structure for Zeta (2025)

A literature-and-proof program that reframes RH as equivalent to the existence of an independent hard-Lefschetz sl₂-structure with Hodge-Riemann positivity on an "arithmetic surface" S = Spec ℤ ×_{Spec F₁} Spec ℤ (Grothendieck's Standard Conjectures for that absolute product), and tests three candidate routes to build it.

- Proved a structural obstruction ruling out the Connes-Consani noncommutative/adèle-class route: its positivity is provably equivalent to RH (not independent), and no compatible Lefschetz operator can be built from the spectral operator given the expected ℚ-linear independence of zero ordinates.
- Identified Arakelov geometry as the most promising partial blueprint: it supplies a non-circular Lefschetz class and Hodge-Riemann-type positivity via the arithmetic Hodge Index theorem, but the absolute surface and a geometric lowering operator remain unconstructed.
- Showed absolute prismatic cohomology offers a plausible cohomological scaffold but no global spectral (Frobenius/Sen-type) generator whose spectrum could equal the Riemann zeros.
- Established a precise, quantitative target for any future construction: reproducing the long-range spectral-rigidity plateau of the Riemann zeros (Δ₃^∞≈0.1908) via an explicit prime-power series — directly motivating the geometric obstruction studied in Program 10.

## How to read a task

Inside each `RHk/task-XXXXXXXX/`:
- **`OVERVIEW.md`** — A written result of that step.
- **`notebook_executed.ipynb`** — the executed analysis notebook, when the underlying run produced one.
- **output / input files** — datasets, figures, and other generated things.

## Relationship to the rest of the program

The bottom line of this empirical base is recorded in the program summary
([`../COMPLETE-PROGRAM-SUMMARY.md`](../COMPLETE-PROGRAM-SUMMARY.md)): the ω-class work is
**descriptively rich but did not beat convexity**, and the localized-Weil detector (RH6–RH8)
became the object the theoretical program pivoted to. The published distillations are in
[`../04-papers/`](../04-papers/).
