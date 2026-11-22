# Phase 187 — Campaign of 100 non-contiguous windows: data to extract the λ_A(T) pattern

Objective: "let's try 100 non-contiguous windows, extract the pattern and extrapolate it taking
all the constraints into account." This folder is the **DATA** part; the pattern is extracted separately. Global label
for everything here: **NUMERICAL**.

## What is computed (definitions = r034_det.py / r040_head_mp.py from phase-186-toolbox; Paper 46 eq:symbol, eq:form, thm:A, prop:negtrace)

- Symbol: σ_T(τ) = m(τ) − Σ_{n∈S(T)} v_n cos(τ log n), m(τ) = Re ψ(¼ + iτ/2) − log π, v_n = 2 log p/√n,
  S(T) = {n = p^k : log n < 2T} (strict inequality: at T = ½log p the prime p is **not** present; the pair T ± 0.01 captures the jump).
- Form in x-space: 𝔞_T(F) = C₀‖F‖² + ∫₀^∞(‖F‖² − C_F(u))K(u)du − Σ v_n C_F(log n), K(u) = 2e^{−u/2}/(1 − e^{−2u}).
- Carrier: 𝒫_T = {F ∈ L²(I_T) : ∫F e^{±t/2} = 0}. λ_A(T) = inf 𝔞_T over 𝒫_T, ‖F‖ = 1.
- Decomposition: Neg_T = R_T σ₋(D) R_T, Pos_T = 𝔞_T + Neg_T; pencil Neg u = β Pos u on 𝒫_T; 1 − β₁ = λ_A/Pos(h*).
- Galerkin: orthonormal Legendre of degree < M on I_T. **λ_A^{(M)} is a variational UPPER bound of λ_A and decreases in M.**
  The blocks M′ < M are principal minors of the same matrix (a single construction per window).
- Arithmetic: python-flint (arb) at `prec_bits` per window, chosen so that dps ≥ 15 digits below the estimated
  −log₁₀ λ_A; checked a posteriori (`precision_margin_digits`) and redone with more digits if it fails. The
  Legendre/Bessel recurrences are rounded to the midpoint at each step (floating point at prec bits); the matrix products and the
  diagonalization (QR of acb_mat) are ball arithmetic: the radius attached to `lamA` bounds the round-off error of the
  linear algebra, **not** the truncation error of the quadratures (see "Quadrature control").
- Quadrature: y-integral of C(u) with M+2 Gauss nodes (exact for polynomials of degree ≤ 2M+3); u ∈ (0, 2T) in 16
  panels × n_u Gauss nodes (n_u chosen by the π-distance of K's poles from the real line to reach the requested
  digits; `n_u_total` = 16·n_u); Tate with M+80 nodes; Neg_T by Gauss nodes per component of {σ_T < 0}
  (16 + 6·width·T nodes, ≤ 120), spherical Bessel functions by recurrence (descending Miller if τT ≤ M+10, ascending otherwise),
  at precision min(prec, 256) bits (Neg affects only β_j, whose required relative precision is ~10⁻⁴).
- Negative set: double-precision scan of σ_T with step 2·10⁻³ up to τ_scan = min(1.1·2πe^{Σv_n} + 10, 2·10⁵),
  zeros refined with brentq; `scan_complete = YES` if the last crossing is toward σ > 0 and σ(τ_scan) > 0 (i.e. τ_last
  was reached). For Neg_T the components used are those starting at < τ_Neg = min(τ_scan, 3·10⁴) (`n_comps_Neg`); the distant
  ones are rare alignments with |û|² = O(τ⁻²) for the head (R186_040 §1.2(b)).
- N(T*) with T* = 2πe^{2T} and the first 150 zeros (zeros150.npy; γ₁₅₀ = 318.85 > T*(log 7) = 307.9).
- N_Sh = 2T·|{σ_T < 0}|/π (R186_034 definition), with the measure found in [0, τ_scan]; also the part within [0, T*].

## Grid (100 windows, non-contiguous)

- 25 low in [½log2, ½log5]: boundaries ½log2, ½log3, log2, ½log5 with ±0.01, plus 0.36…0.78 irregular.
- 40 mid in (½log5, 1.3]: boundaries ½log7, ½log8, ½log9, ½log11, ½log13 with ±0.01, plus 25 irregular points.
- 35 high in (1.3, 1.75]: boundaries ½log16, ½log17, ½log19, ½log23, log5, ½log27, ½log29, ½log31, ½log32 with ±0.01,
  plus 1.32, 1.34, 1.36, 1.45, 1.50, 1.53, 1.60, 1.75. (log 7 = 1.946 only if time allows, outside the 100.)
`python3 r187_campaign.py --stage low|mid|high|all --workers N` (resumable: skips T values already present in the CSV; one row per
window written on completion, with a lock). Environment: venv with python-flint 0.9 + gmpy2 (see the script header).

## Columns of DATA_100_WINDOWS.csv

| column | content |
|---|---|
| T, T_label, stage | window; label if it is a boundary (½log p, log p); stage low/mid/high |
| S_size, S_max_n | #S(T) and the largest n ∈ S(T) |
| prec_bits, dps, n_u_total | working precision (bits, digits) and total nodes of the u-quadrature |
| M, M_list, lamA_list | final M and the sequence λ_A^{(M′)} at the blocks M′ (step 20), with ball radius |
| lamA, lamA_float, lamA_prev, relvar_lastM | λ_A^{(M)} (ball), as float, the value at M − 20, and the relative variation |λ_A^{(M)}/λ_A^{(M−20)} − 1| |
| converged | YES if relvar_lastM < 10⁻² (two stable digits over +20 in M); if not, NOT CONVERGED and λ_A is an upper bound |
| log10_lamA, lam2 | log₁₀ λ_A; second eigenvalue of 𝔞_T|𝒫_T (degeneracy of h*) |
| nneg, nneg_flag | n₋(𝔞_T|𝒫_T) in the final Galerkin; warning if > 0 (possible contact vs noise) |
| precision_margin_digits | dps − (−log₁₀ λ_A): must be ≥ 15 |
| beta_top10, one_minus_beta_top10, ladder_top10 | β₁ ≥ … ≥ β₁₀ of the pencil, 1 − β_j, ladder −log(1 − β_j) (natural log) |
| K_1em2, K_1em3, K_1em4, K_e | #{j : 1 − β_j < 10⁻², 10⁻³, 10⁻⁴, e⁻¹} (nearly balanced directions) |
| n_beta_gt_1 | #β_j > 1 (= n₋; must be 0) |
| hstar_even_mass, hstar_parity, hstar2_even_mass | even mass of the minimizer h*_T (even Legendre coefficients) and of the second eigenvector; parity (even/odd/mixed) |
| hstar_peak, hstar_centroid, centroid_cut | argmax of |ĥ*(τ)|² and centroid ∫τ|ĥ*|²/∫|ĥ*|² on [0, centroid_cut], centroid_cut = min(τ_last, 4T*), grid 0.01 |
| hstar_mass_inner_T2 | ∫_{|t|<T/2}|h*|² / ‖h*‖² |
| Pos_h, Neg_h | Pos_T(h*), Neg_T(h*) (Pos − Neg = λ_A) |
| arch_term_h, prime_term_h | ⟨h*, A₀h*⟩ (archimedean, includes C₀ and the tail) and ⟨h*, Pr h*⟩ = −Σ v_n C_{h*}(log n); sum = λ_A |
| lamA_inf | λ_A^∞(T) = min of the archimedean form A₀ on 𝒫_T (no primes; can be < 0 because m < 0 near τ = 0) |
| Tstar, N_Tstar | T* = 2πe^{2T}, N(T*) = #{γ ≤ T*} |
| tau_scan, tau_last, scan_complete | reach of the scan, last zero of σ_T found, whether τ_last was reached |
| n_comps, n_comps_Neg, tau_Neg_cut | components of {σ_T<0} found, used in Neg, cutoff |
| neg_measure, N_Sh, N_Sh_below_Tstar | measure of {σ_T<0} on [0, τ_scan], Shannon number, and the part below T* |
| time_build_s, time_neg_s, time_total_s | CPU seconds (single process) |
| notes | warnings (precision redone, contact, N(T*) outside the 150 zeros) |

`windows/T_<T>.json`: per window, Legendre coefficients (float) of h* and of the second eigenvector, negative components,
1 − β_j (first 40), the 20 lowest eigenvalues of 𝔞_T|𝒫_T, and the history in M.

## Quadrature control and reproduction
(completed at the end of the campaign: see "Results")

## Phase result (editor)

* 46 converged windows with balls, T ∈ [0.337, 1.075]: λ_A > 0 and index 0 in all of them (NUMERICAL certified by balls in Galerkin; upper bounds on λ_A).
* **Descriptive law (PATTERN_REPORT.md, CONJECTURE):** −ln λ_A ≈ 13.0·e^{2T} − 24.6·T − 18.7; fitted on [0.55, 0.85] predicts 17 held-out windows (0.87–1.075) to within +0.24 ± 0.12 digits; smooth across the prime entries; Zhu's 2π²N/ln N overestimates by 10–12 digits in this range (pre-asymptotic); "2π per zero" excluded out of sample. K_{1e-3} = N(T*) + c, c ∈ {−1,0,1} in 40/40. CONDITIONAL[(REG)] folds not observed (0 ± 3 vs +6…+18 predicted), except at ½log8.
* **M₁ falsifier test (DATA_MM_FALSIFIER.csv): the perturbation with a pair of off-line zeros reproduces ζ's λ_A to within 0.2–3% (small δ) with the same K, parity, peak and ladder; with δ = 0.1/0.3 it gives λ_A < 0, n₋ = 2 at log2 and ½log5 WHILE PRESERVING K = N(T*) ± 1 and even parity. The whole pattern is a class property: it does not imply positivity.** f_t shares the fit over any finite range.
* Extrapolation admissible but of indeterminate form beyond T ≈ 1.3 (−log₁₀ λ_A ≈ 41 at 1.2, 89–101 at 1.5, 278–371 at 2).
* Preregistered test (PREREG_LAW_TEST.md) on 4 random windows T = 1.128, 1.236, 1.316, 1.447: in progress.
* — **Campaign and preregistered test INTERRUPTED** (no more resources to be consumed). Final state: 48 rows in DATA_100_WINDOWS.csv (47 converged up to T = 1.075; T = 1.135 NOT CONVERGED, −ln λ_A ≥ 78.9); DATA_PREREG_4.csv with one row (T = 1.128, M = 120, −ln λ_A ≥ 77.05, not converged, at the upper edge of the exponential-law band and inside that of "2π per zero"); verdict §7 of PREREG_LAW_TEST.md not completed. Standing conclusion: the per-window observable pattern is a class property (M₁ falsifier); the sign lives in the extreme eigenvalue of the truncated Wiener–Hopf W_T(σ₊ − σ₋/β) at the inertia crossing (R186_042), with no literature.

## Other files in this folder

- `CONSTRAINTS_FOR_PATTERN.md` — Corpus constraints on any pattern T ↦ λ_A(T) and on the per-window observables.
- `windows_mm/` — subfolder (8 files).
- `r187_mm.py`, `r187_pattern.py`, `r187_prereg_verdict.py` — scripts.
