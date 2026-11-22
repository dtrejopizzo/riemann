# R186_119 — Audit of the numerical references for λ_A (log 2, ½log3, ½log5)

**Status: COMPLETE, NUMERICAL.** Sweeps finished: Legendre M = 40…240 and Fourier J = 40…640 in arb balls (220 bits), sampled
Nyquist Jb = 50…800 (double precision). Scripts `leg_audit.py`, `fourier_audit.py` (session scratchpad, venv with python-flint 0.9). Still pending
only the 24×96 quadrature control (irrelevant: M = 120 reproduces r187's value with a different quadrature to 9.87775·10⁻⁸).

## 0. Question and short answer
R186_053 §3.4: the Fourier–Nyquist Galerkin gives upper bounds of λ_A **below** the corpus's Legendre references
(1.042·10⁻⁷, 9.486·10⁻⁴, 3.84·10⁻¹²). **Verified explanation: (a) Legendre M = 40 is not converged.** The corpus's references are
exactly the M = 40 value (reproduced here in 220-bit ball arithmetic: 1.04212784192·10⁻⁷ at log 2, identical to r187's and r117's).
The phase-187 ball campaign is the same Legendre method with larger M (M = 140 at log 2: 9.8634·10⁻⁸; M = 72 at ½log3: 9.4615·10⁻⁴;
M = 90 at ½log5: 3.176·10⁻¹²) and shows the monotone decrease in M; it does not "match Nyquist": both methods converge slowly from above
toward the same limit, and at equal J or M the Fourier one lands lower. There is no bias in the Nyquist matrix: (b), (c), (d) ruled out
(§2). No sign changes; Paper 46 is not touched (its lower bounds 8.8577·10⁻⁵ at ½log3 and 2.5·10⁻¹² at ½log5 stay below
all upper bounds: 9.456·10⁻⁴ and 3.09·10⁻¹²).

## 1. Methods (all in 220-bit arb balls except the third)
1. **Legendre** (`leg_audit.py`, own; x-form of Paper 46 thm:A/eq:Aform as in r024/r034/r043/r187): orthonormal Legendre basis of degree
 < M on I_T, exact C(u) via Gauss M+2, Lévy in 16 panels × 72 Gauss nodes, closed-form tail ∫_{2T}^∞K, Tate via Gauss M+60, principal
 minors for every M. Certificate: arb Rayleigh quotient of the inverse-iteration vector (rigorous upper bound).
2. **Fourier** (`fourier_audit.py`, own, assembled in closed form, no matrix quadrature): e_j = e^{ijπt/T}/√2T; the matrix only
 needs the scalar integrals Λ_m = ∫(1−cos ω_m u)K, S_m = ∫ sin(ω_m u)K, U_m = ∫ u cos(ω_m u)K (analytic integrands, panels
 ≤ ½ period). Checked against `r052_nyquist.fourier_matrix` (quadrature, double precision): |ΔM|_max = 9·10⁻¹⁵ at J = 12; reproduces
 λ_J = 1.76433·10⁻⁷ / 1.30581·10⁻⁷ (J = 12/24, log 2) from R186_118.
3. Sampled Nyquist ½(D_e + HᵀD_oH) with L = 2·10⁵ odd modes and analytic odd tail (r052/r053, double precision).

## 2. Final table (upper bounds; Legendre and Fourier in 220-bit arb, certified by Rayleigh quotient; n₋ = 0 in all)
| window | method | M or J | λ (·10⁻⁸ at log 2, ·10⁻⁴ at ½log3, ·10⁻¹² at ½log5) | status |
|---|---|---|---|---|
| log 2 | Legendre | 40/60/80/100/120/140/160/180/200/220/240 | 10.4213/10.1075/9.9591/9.9067/9.8777/9.8634/9.8549/9.8487/9.8451/9.8422/9.8401 | not converged; diff. ~M^{−3.5}, tail ≈ 0.01 → **9.83** |
| log 2 | Fourier | 40/80/160/320/640 | 10.8783/10.0519/9.8796/9.8421/9.8326 | ratio ≈ 0.25 per doubling, tail ≈ 0.003 → **9.830** |
| log 2 | sampled Nyquist + odd tail | 50/100/200/400/800 | 10.467/9.965/9.861/9.838/9.831 (R186_053: 9.831) | = Fourier to 4 digits |
| ½log3 | Legendre | 40/…/240 | 9.4858/9.4670/9.4582/9.4550/9.4533/9.4518/9.4510/9.4505/9.4500/9.4497/9.4495 | tail ≈ 0.001 → **9.448** |
| ½log3 | Fourier | 40/80/160/320/640 | 9.5617/9.4764/9.4558/9.4502/9.4484 | tail ≈ 0.0008 → **9.448** |
| ½log3 | Nyquist + tail | 50/…/800 | 9.5201/9.4665/9.4532/9.4494/9.4481 | = Fourier to 4 digits |
| ½log5 | Legendre | 40/…/240 | 3.8858/3.2678/3.1797/3.1685/3.1457/3.1308/3.1263/3.1207/3.1156/3.1132/3.1116 | tail ≈ 0.007 → **3.105** |
| ½log5 | Fourier | 40/80/160/320/640 | 4.1633/3.4059/3.1619/3.1111/3.1029 | tail ≈ 0.002 → **3.101** |
| ½log5 | Nyquist + tail (R186_053) | 100/400 | 3.28/3.09 | double precision, ±0.01 |

**Extrapolated values (Richardson on the successive differences, two independent bases in agreement):**
λ_A(log 2) = 9.83·10⁻⁸ (±0.01), λ_A(½log3) = 9.448·10⁻⁴ (±0.001), λ_A(½log5) = 3.10·10⁻¹² (±0.01). Rigorous upper bounds (Rayleigh in
balls): 9.83263704·10⁻⁸, 9.44839739·10⁻⁴, 3.10294772·10⁻¹² (Fourier J = 640).

### 2b. Earlier working table (historical)
| window | method | M or J | λ (upper bound) | status |
|---|---|---|---|---|
| log 2 | Legendre | 40 | 1.04212784192·10⁻⁷ (±5·10⁻¹⁹) | = corpus reference; NOT converged |
| log 2 | Legendre (r187, balls) | 60/80/100/120/140 | 1.01075/0.99591/0.99067/0.98778/0.98634·10⁻⁷ | NOT converged (relvar 1.5·10⁻³) |
| log 2 | Legendre | 160…240 | — | in progress |
| log 2 | Fourier | 12/24 | 1.76433·10⁻⁷ / 1.30581·10⁻⁷ | reproduces R186_118 |
| log 2 | Fourier | 160 | 9.87959521·10⁻⁸ (28 nodes/panel; matches 16 nodes/panel pending) | NOT converged |
| log 2 | Nyquist (R186_053 §3.2) | 50…800 | 10.47/9.964/9.861/9.837/9.831·10⁻⁸ | differences 5.6/1.4/0.45/0.19·10⁻⁹ |
| ½log3 | Legendre | 40 | 9.4858·10⁻⁴ | = reference; NOT converged |
| ½log3 | Legendre (r187) | 52/72 | 9.4713/9.4615·10⁻⁴ | NOT converged |
| ½log3 | Fourier | 40/80/160 | 9.56171/9.47638/9.45580·10⁻⁴ | NOT converged; 320, 640 in progress |
| ½log3 | Nyquist (double, own) | 50/100/200 | 9.5198/9.4662/9.4530·10⁻⁴ (odd tail +3·10⁻⁸) | matches R186_053 to 4 digits |
| ½log5 | Legendre | 40 | 3.84·10⁻¹² (double) | = reference; NOT converged |
| ½log5 | Legendre (r187) | 50/70/90 | 3.469/3.2008/3.176·10⁻¹² | NOT converged |
| ½log5 | Fourier | 40/80 | 4.16331/3.40585·10⁻¹² | NOT converged; 160…640 in progress |
| ½log5 | Nyquist (R186_053) | 100/400 (with tail) | 3.28/3.09·10⁻¹² | NOT converged |

Reading: both bases converge algebraically (Legendre ~M^{−2.5…3.5}, Fourier ~J^{−2}) and from above to the same limit; at equal dimension
Fourier lands lower. Consistent with a minimizer h* not smooth at ±T (domain of the form = log-Sobolev space). The final figures
are in §2.

## 3. Ruling out hypotheses (b)–(d) of the request
- (b) Bias of the Nyquist matrix: the Fourier matrix assembled in closed form (no symbol sampling, no L, no odd tail,
 no boundary convention for n = 4) matches r052's quadrature one to 10⁻¹⁴ and its λ_J match those of R186_053/R186_118;
 the odd tail equals +3·10⁻⁸ at ½log3 and +10⁻¹¹ at log 2 (alternating direction ≈ nullified by h*). The ½ convention for n = 4 (R186_118
 MAJOR-2) only affects the sampling of the symbol on the grid, not the form of Paper 46 (strict N_T: n = 4 excluded at log 2, included
 at ½log5 with v₄ = 2 log 2/2), which is what both codes assemble.
- (c) σ_T vs s_T: the x-form (eq:Aform) with Lévy truncated to [0, 2T] plus the tail ∫_{2T}^∞K is identical across the three methods; there is no aliasing.
- (d) Tate: a_j = (−1)^j 2 sinh(T/2)/((½ + iω_j)√2T), b_j = conj(a_j); constraints Re a·x = Im a·x = 0 ⇔ A = B = 0 on the complex span;
 minimum over complex numbers = minimum over reals because M is real symmetric. The Tate vectors match r052 to 3·10⁻¹⁷.

## 4. Verdict and what to cite
- The references 1.042·10⁻⁷ / 9.486·10⁻⁴ / 3.84·10⁻¹² are **Legendre M = 40 values, unconverged upper bounds** (6% / 0.4% /
 ≥ 20% above the limit). They must not be cited as "λ_A".
- Cite: **λ_A(log 2) = 9.83·10⁻⁸** (3 digits), **λ_A(½log3) = 9.448·10⁻⁴** (4 digits), **λ_A(½log5) = 3.10·10⁻¹²** (3 digits); as rigorous
 upper bounds, the Fourier J = 640 values of §2. Always with method and J/M when a specific Galerkin value is cited. Paper 46's lower bounds (thm:C 8.8577·10⁻⁵; thm:log5A 2.5·10⁻¹²)
 remain below all the upper bounds.
- Memos citing the wrong value as λ_A (correct to "Legendre upper bound M = 40" or to the new value): R186_034 (table §, 9.486e-4),
 R186_040 (table, 1.042e-7), R186_043 (λ_A M = 40), R186_044 (§1.1, 1.3, table: 9.4858e-4, 1.0421e-7, 3.8409e-12), R186_045 (table
 1.04e-7), R186_046 (1.03e-7, 3.65e-12), R186_047 (9.49e-4, 1.04e-7, 3.8e-12), R186_048 (9.4858e-4, 1.0421e-7), R186_051 (l. 194, 239),
 R186_052 (l. 100), R186_053 (§0, §3.4, final table: as "reference"), R186_115 (1.04e-7), R186_117 (l. 19, 50: 3.887e-12), R186_118
 (l. 61, 148, 202). In phase-187: PATTERN_REPORT.md (9.86e-8, 3.176e-12 as "λ_A": these are Legendre M = 140/90, not converged to the 3rd
 digit), R186_114 (9.48028e-4, 3.162e-12), R186_106 (9.467e-4), R186_041 (9.46e-4). The phase-187 law's constant changes in the
 third digit, as R186_053 anticipated.

## 5. Falsifiers of this memo
A Galerkin on any subspace of 𝒫_T with a value < 9.82·10⁻⁸ (log 2), < 9.447·10⁻⁴ (½log3) or < 3.09·10⁻¹² (½log5) would refute the
extrapolation; a Legendre or Fourier value below Paper 46's lower bounds (8.8577·10⁻⁵, 2.5·10⁻¹²) would refute the paper
(does not occur: margin ×10.7 and ×1.24).
