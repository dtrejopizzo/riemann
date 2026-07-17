# Bottleneck Ledger — v6.6 Synthesis (R10) **Project goal.** Identify, for each numerical signature × control function, the
sharpest provable statement and the exact missing lemma / computational barrier
that prevents progress toward RH. **Panel.** ζ (positive control), L(χ₄ mod 5) (RH control), L_DH (non-RH control,
110 confirmed off-line zeros for t<5000), L(Δ,s) (Ramanujan Δ structural control,
partial), ζ_δ (deformation control). **Inputs.** N=5000 zero lists (dps=50 for ζ and L_DH, dps=80 for L(χ₅));
Jacobi (a_n,b_n) for both uniform and 1/|ρ|² weights; Li coefficients λ_n,
n=1..200; Step 0.5 power calibration table. --- | Function | Observable | Result | Interpretation | Bottleneck |
|:----------------------|:---------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| ζ | Jacobi b_n fit (uniform wt) | b_n ≈ 1407·n^-0.0108 (power-law wins; ΔAIC vs log = 698) | Slowly-decaying bulk on stable window c=0.1; no log-law signal | No theory forces a particular law; weight-dependence makes any asymptotic non-canonical |
| ζ_δ (strong) | Jacobi b_n fit (uniform AND 1/|ρ|² wt) | Coefficients literally identical to ζ to float64 precision | Front I is BLIND to real-part perturbations (γ unchanged) | Re(ρ) information enters only via |ρ|² in weight, dominated by γ² (r40 confirmed) |
| L_DH | Jacobi b_n fit (uniform wt) | b_n ≈ 1296·n^-0.0124 | Same functional form as ζ but different prefactor (≈ 1296 vs 1407) | Prefactor differences are weight-artifact; spectral-weight audit demands a discriminator stable to weight choice — none found |
| L(χ₄ mod 5) | Jacobi b_n fit (uniform wt) | b_n ≈ 1139·n^-0.0119 | Same shape, smaller prefactor (≈ 1139); zeros start higher → lower b_n | Same as ζ — descriptive only |
| L(Δ,s) | Jacobi b_n fit (partial N=129) | b_n ≈ 259·n^-0.0176 on n≤20 | Same functional family; small N | cypari2 cost scaling T^2.85: completing N=5000 dps=80 is ~10² over budget |
| ζ | Li λ_n (n ≤ 200) | λ_n > 0 (consistent with RH; positivity ⇔ RH per Bombieri–Lagarias) | Finite-n evidence; not a proof | Need a *uniform-in-n* lower bound; no known route (Lagarias 1999) |
| L_DH | Li λ_n (n ≤ 200) incl. 110 off-line zeros | λ_n > 0 for ALL n ≤ 200 even with 110 off-line zeros (r39 confirmed); λ_1≈0.097, off-line contribution +0.00039 | Li test is INSENSITIVE at this scale despite known RH violation | Predicted negativity onset n ≈ 86,000 — cost ~10⁵ × current |
| L(χ₄ mod 5) | Li λ_n | Not computed in this run | — | Same as ζ would be — insensitive test |
| L(Δ,s) | Li λ_n | Not computed (zero list incomplete) | — | Cost of generating N=5000 dps=80 list |
| ζ_δ | Li λ_n | Not computed (Step 0.5 already declared Li blind to real-part perturbations) | Expected blind based on L_DH evidence | Same crossover n needed |
| ζ | Gram form λ_min(Q_10) on Hermite test family | λ_min = 4.57e-09 (≥0 by construction; cond ≈ 2e16) | Numerical floor — not a discriminator | Need a Weil explicit-formula form Q(φ)=Σφ̂(γ)−boundary, not a Gram. R8 cloud budget OK; missing implementation. Uniform-in-N lower bound still open |
| ζ_δ | Gram form λ_min(Q_10) | Same as ζ (Re shift does not enter Hermite-of-γ form) | Confirms structural blindness | Need a form built on Re(ρ); explicit-formula form would do it |
| L_DH | Gram form λ_min(Q_10) | λ_min = 4.63e-09 | Effectively identical to ζ | Same as ζ |
| L_DH+offline | Gram form λ_min(Q_10) | λ_min = 1.95e-09 (lower!) | Adding 110 zeros perturbs eigenvalues but stays positive | Gram is always ≥0 — uninformative; need true Weil Q |
| L(χ₄ mod 5) | Gram form λ_min(Q_10) | λ_min = 2.90e-09 | Consistent with GRH expectation | Same — uninformative finite-N positivity (R7) |
| ζ vs ζ_δ (δ=1.0) | H0 bottleneck distance | d_B = 0.5 = δ/2 (Wasserstein-1 p<0.002, NP=500 perms) | Calibrated and exact: scales linearly with δ | None for detection; but no proof route from d_B to RH — pure phenomenology |
| ζ vs ζ_δ (δ=1e-3) | H0 bottleneck distance | d_B = 5.0e-4 = δ/2 (p<0.002) | Same linear law down to 10⁻³ | Limited by zero-list precision (~1e-15) below which detection saturates |
| L_DH vs ζ | H0 bottleneck (critical line only) | d_B = 0 (p = 1.0) | All on-line spectra indistinguishable in Re(ρ) | By construction — Re(ρ)≡½ is identical; this is a sanity check, not RH signal |
| L_DH+offline vs ζ | H0 bottleneck | d_B = 0.0141 (max off-line σ ≈ 0.514; p<0.002) | Off-line zeros of L_DH ARE detected; ~2× max σ−½ | TDA is sensitive but disconnected from a proof mechanism (R10 col. 4 = NO) |
| L(χ₄ mod 5) vs ζ | H0 bottleneck | d_B = 0 (p = 1.0) | GRH-consistent indistinguishability | Same as L_DH — sanity check |
| L(Δ,s) vs ζ | H0 bottleneck | Not run (zero list incomplete) | — | Zero-generation cost (T^2.85 scaling) |
| ζ | Moment ratio I_1/(T log T) | = 0.799 at T=5448 | Approaching 1 (Hardy–Littlewood); ~20% finite-T deficit | Need next-order Keating–Snaith correction & ω-class decomposition — not implemented in this run |
| ζ | Moment ratio I_2 / [T(log T)^4/(2π²)] | = 1.089 at T=5448 | Within 10% of Ingham; OK at this T | ω-class decomposition (Front II.7, 50% effort budget) NOT EXECUTED — primary open deliverable |
| L_DH, L(χ), L(Δ), ζ_δ | Moment ratios | Not computed | — | Same as ζ; need Dirichlet partial sum D_F(t;N) infrastructure | --- ## Per-observable summary statements (R9 sharpest statement) ### Front I — Jacobi b_n (descriptive only)
- For all five panel functions, the off-diagonal Jacobi b_n on the stable c=0.1 window is best modelled by a **power law** b_n ≈ c · n^δ with δ ∈ [−0.018, −0.011] (AIC selects power over log/constant by ~400–700 units).
- ζ and ζ_δ (strong) give Jacobi coefficients **identical to float64 precision** under both weighting choices — Front I is structurally blind to real-part perturbations.
- Verdict: descriptive phenomenology, no discriminator survives the spectral-weight audit. (Per R3/Front-I "Honest pivot clause": stop investing here.) ### Front II.5 — Li coefficients
- For L_DH, λ_n > 0 for **all** n ≤ 200, with the 110 off-line zeros contributing positively to λ_n (λ_1 contribution ≈ +0.00039, λ_200 contribution ≈ +0.02). The Li-positivity ⇔ RH equivalence (Bombieri–Lagarias) is therefore **uninformative at this scale**.
- The predicted crossover where λ_n turns negative is at **n ≈ 86,000**, beyond cloud-compute reach. ### Front II.6 — Weil/Gram positivity
- A Hermite-window Gram form Q_jk = Σ_ρ φ_j(γ)φ_k(γ) is **always PSD by construction** and yields λ_min(Q_10) ∈ [3e-9, 5e-9] across the panel — at the conditioning floor (cond ≈ 2e16).
- This is **not a true Weil quadratic form**; the explicit-formula form Q(φ)=Σ_ρ φ̂(γ) − boundary terms must be built. Until then, no informative finite-N positivity exists. ### Front III — H0 bottleneck distance on Re(ρ)
- **Calibration confirms d_B = δ/2 exactly:** ζ_δ(δ=1.0) ↦ d_B=0.500; ζ_δ(δ=1e-3) ↦ d_B=5e-4.
- L_DH+offline vs ζ: d_B = 0.01411, consistent with max(σ_off-line)−½ ≈ 0.014.
- Wasserstein-1 permutation tests give **p < 0.002 (500 perms)** for any off-line perturbation vs ζ, and p = 1.0 for any pair of on-line spectra.
- Verdict: sensitive, calibrated detector but **no proof route to RH** — labelled *numerical indicator only* per R10 col. 4 = NO. ### Front II.7 — Moment I_k(T)
- For ζ alone, computed I_1(T)/(T log T) = 0.799 and I_2(T)/[T(log T)^4/(2π²)] = 1.089 at T = 5447.86.
- These are consistent with the leading Hardy–Littlewood / Ingham asymptotics including expected ~10–20% next-order corrections.
- The ω-class decomposition (the 50%-effort highest-priority front per the spec) is **not executed**; it is the largest single open deliverable. --- ## Hierarchy of numerical signatures (in order of sensitivity to Re(ρ) shift) | Rank | Observable | Linear in δ? | Discriminates ζ vs L_DH+offline? | Connected to a proof route? |
|------|------------|--------------|----------------------------------|-----------------------------|
| 1 | H0 bottleneck distance on Re(ρ) | yes (= δ/2) | yes (d_B=0.014, p<0.002) | **no** — phenomenology |
| 2 | H1 persistence on Re(ρ) | only for contiguous perturbations | partial | no |
| 3 | Jacobi b_n (uniform wt) | no | no | no — descriptive |
| 4 | Jacobi b_n (1/|ρ|² wt) | no | no | no — descriptive |
| 5 | Li coefficients λ_n (n ≤ 200) | no | **no** (all λ_n > 0) | yes (Bombieri–Lagarias) but insensitive |
| 5 | Gram form λ_min(Q_N) (Hermite) | no | no | not a true Weil form | This establishes the **central methodological finding** of the program:
**sensitivity and relevance are anti-correlated** in this panel. TDA detects but
does not connect; Li/Weil connect (in principle) but do not detect at feasible N. --- ## Open bottlenecks (in priority order) 1. **ω-class moment decomposition (Front II.7)** — not executed. Requires implementing the Dirichlet partial sum S_k(t;N) over ω-class strata, then matching to Keating–Snaith C_k constants. Highest expected-value front; publishable independent of RH.
2. **True Weil explicit-formula quadratic form Q(φ)** — not implemented. Need to replace the structural-PSD Gram by the explicit-formula form, then bound λ_min(Q_N) and study its N-trend.
3. **L(Δ,s) zero list at N=5000, dps=80** — incomplete; cypari2 cost ~T^2.85 prevents single-machine completion. Could be parallelized via subprocess pattern (proven for L(χ₅)).
4. **Li-coefficient crossover at n ≈ 86,000 for L_DH** — out of reach by ~5 orders of magnitude in cost.
5. **Uniform-in-N lower bound for any finite positivity object** — the central missing theoretical lemma; no plausible route from cloud-scale numerics.
