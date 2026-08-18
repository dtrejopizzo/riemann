# Phase 103 — direct A1 closure

Working container for the phase defined by
`PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`.  Sole objective:
\[
  C_n(T_n)\ge0\qquad(n\ge8),
\]
starting from the narrowest direct form reached in phase 102.

## Result of the phase, in one paragraph

The direct route has been reduced to a single inequality with no bookkeeping
left in it,
\[
  \int_{\log2}^{T_n}\bigl(\psi(e^u)-e^u\bigr)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ \le\ {3\over4}A_n+1-L_n^{(1)}(\log2)
  \ =\ {3\over8}n\log n\,(1+o(1)),
\]
the reserve was computed exactly, and diagnostic computations suggest a
large margin for \(8\le n\le1200\).  Under RH the available estimates give
an eventual conditional closure.  `103_22` supplies explicit constants
for the two interior Laguerre budgets, and `103_58` sharpens them enough to
produce a fully explicit, though enormous, conditional threshold with
\(\log n_{\rm eff}<833334000\).  This does not validate the advertised
numerical threshold \(150\), and the finite interval from 150 to
\(n_{\rm eff}\) remains uncertified.  Likewise, the competitor
argument in `103_05` is presently an
outline, not a theorem: its conversion of lobe width into weighted mass and
its exponential lower bound still need uniform proofs.  The remaining
unconditional gate is a new cancellation or positivity theorem for the
actual weighted prime sum; proving it would prove RH.

## Documents

| file | work-order step | content |
|---|---|---|
| `103_01_GLOBAL_TELESCOPING_AND_ENDPOINT_TABLE.md` | 1 | Stieltjes telescoping with exact endpoints; endpoint table; the moving cutoff is convention-free; \(\mathcal R_n\le Q_n\) is *identical* to the direct certificate; closed form of \(Q_n\) |
| `103_02_EXACT_RESERVE_THEOREM.md` | 2, 3 | exact reserve, uniform lower bound, true scale \(\frac38n\log n\), explicit threshold \(n_0(T_8)\); final one-line form of the target |
| `103_03_LAGUERRE_LOBE_GEOMETRY.md` | 4 | zero locations, bulk lobe width \(2\pi\sqrt{x/(4-x)}=\Theta(1)\), amplitude envelope, the three budgets \(n\), \(n^{3/4}\), \(e^{3n/2}\) |
| `103_04_ORIENTED_TRANSPORT_TARGET_AND_CONDITIONAL_CLOSURE.md` | 5–8 | conditional outline under RH; the qualitative eventual result survives, while the threshold \(150\) is diagnostic |
| `103_05_ADMISSIBLE_COMPETITOR_NO_GO.md` | 7 (negative) | candidate monotone competitor; quantitative mass comparison and support claims are not yet proved |
| `103_06_NUMERICAL_CERTIFICATE_REPORT.md` | 6 | pipeline validation against `217`; \(A_n\) asymptotics; strong margin to \(n=1200\); true \(\mathcal J_n=O(1)\); load tables; a numerical trap |
| `103_07_CLOSURE_LEDGER_AND_FINAL_DEDUCTION.md` | 9, 10 | the nine acceptance criteria; final deduction to RH; RH-equivalence of the target; recommendation |
| `103_08_RIGOR_AUDIT_AND_CLOSURE_BOUNDARY.md` | audit | distinguishes algebraic results, conditional arguments, and numerical diagnostics; records the remaining proof obligations |
| `103_09_RIGOROUS_OUTER_TAIL_LEMMA.md` | repair | a Cauchy--orthogonality bound covering the previously omitted interval \([4N,T_n]\) |
| `103_10_RIGOROUS_INTERIOR_LAGUERRE_BUDGETS.md` | repair | proof of the uniform interior bounds \(I_2\ll N^{3/4}\), \(I_3\ll N^{5/4}\) from a uniform hard-edge/bulk/Airy Laguerre estimate |
| `103_11_EFFECTIVITY_AND_ZERO_SUM_GATE.md` | audit/theorem | effectivity audit for the hidden Laguerre constants and proof that the proposed uniform zero-sum bound is equivalent to RH |
| `103_12_HARD_EDGE_CORRECTION_AND_FIXED_WINDOW_COLLAPSE.md` | repair | corrects the fixed-lower-endpoint lobe partition; exact finite-window collapse and the sharper \(O_{T_8}(n^{1/4})\) reserve term |
| `103_13_ADVERSARIAL_STATUS_CORRECTION.md` | controlling audit | withdraws the unproved threshold, certification, and competitor claims; states exactly what remains rigorous |
| `103_14_REGULARISED_EULER_GENERATING_IDENTITY.md` | exploratory theorem | absolutely convergent Euler--Laguerre generating identity with pole regulator; exact obstruction to factorwise positivity |
| `103_15_THETA_MEASURE_CUMULANT_OBSTRUCTION.md` | exploratory theorem/no-go | common positive theta-measure identity; low-order positivity; exact obstruction to generic measure and all-cumulants arguments |
| `103_16_EXPONENTIAL_COORDINATE_PRINGSHEIM_NO_GO.md` | exploratory no-go | Stirling-coordinate sufficient condition for Li positivity; elementary Pringsheim proof that the condition is false |
| `103_17_SELBERG_CONVOLUTION_KERNEL_NO_GO.md` | exploratory no-go | positive Selberg coefficients \(\Lambda\log+\Lambda*\Lambda\) and the exact signed Laguerre-kernel obstruction |
| `103_63_SELBERG_QUANTILE_COLLECTIVE_ATTEMPT.md` | exact collective audit | centered Selberg identity inserted before the quantile pullback; explicit inverse operator, noncoercive Hankel form, and exact positive-measure countermodels at Selberg scale |
| `103_18_TURAN_RICCATI_COUPLING_AUDIT.md` | exploratory no-go | positive theta variance coupled exactly to the Li logarithmic derivative; no induction beyond second-moment information |
| `103_19_EULER_TRUNCATION_RENORMALISATION_NO_GO.md` | exploratory no-go | Euler-product truncation with simultaneous continuous pole renormalisation; exact signed prime-jump obstruction |
| `103_20_LAGUERRE_INDEX_INDUCTION_NO_GO.md` | exploratory no-go | exact first and second index recurrences for the common-cutoff certificate; both preserve signed kernels |
| `103_21_REAL_RAY_STIELTJES_NO_GO.md` | exploratory no-go | real-ray positivity of the Li generator; fixed positive Stieltjes measures are incompatible with its divisor |
| `103_22_ODE_EFFECTIVITY_LOSS_AUDIT.md` | effective Laguerre bounds | explicit Bessel--Volterra and short energy transport proof of \(I_2=O(N^{3/4})\), \(I_3=O(N^{5/4})\) for \(N\ge149\), with deliberately huge constants |
| `103_24_EULER_GAMMA_CARATHEODORY_MARGIN_AUDIT.md` | Euler--Gamma audit | exact completed Carathéodory and Loewner-margin symbols; weak kernel positivity is RH-equivalent and full margin positivity is later eliminated |
| `103_25_ARCHIMEDEAN_BOUNDARY_OBSTRUCTION_TO_LOEWNER_MARGIN.md` | Euler--Gamma no-go | explicit digamma remainder proves the full Loewner margin is false even under RH; only Dirichlet/Fejer energies remain |
| `103_27_FEJER_ZERO_SAMPLING_AND_RECIPROCAL_PAIR_NO_GO.md` | spectral no-go | exact RH Fejer sampling for \(2\lambda_n\); off-line functional quartets have both signs, so pairing/Parseval cannot supply coercivity |
| `103_29_THETA_MLR_LOG_CONCAVITY_AND_SQUARE_NO_GO.md` | theta no-go | theta tilts have only generic MLR/TP2; a log-concave symmetric countermodel has off-line zeros, and cumulant-square positivity fails |
| `103_33_THETA_HEAT_FLOW_COLLISION_AUDIT.md` | theta heat audit | derives the heat equation, simple-zero motion, and (L^2) energy; an exact positive-kernel model shows backward real-zero collisions |
| `103_30_THETA_ROUTE_AND_CONVEXITY_BOUNDARY.md` | theta-convexity audit | exact theta formula for the strong-margin generator; a positive smooth Schwartz countermodel proves that real log-convexity and decay do not control the complex zeros |
| `103_26_INTEGRATED_STRONG_MARGIN_AUDIT.md` | integrated-margin audit | exact Abel--Fejer identity for \(2\lambda_n-\lambda_n^{\rm arch}\); rules out pointwise-symbol and coefficientwise Euler-factor positivity without ruling out the scalar averages |
| `103_28_ZERO_QUARTET_FEJER_NO_GO.md` | spectral-symmetry no-go | exact functional-equation quartet contribution; off-line quartets have negative Fejer energies infinitely often, so reflection symmetry alone cannot close A1 |
| `103_23_INDEPENDENT_ODE_EFFECTIVITY_AUDIT.md` | independent audit | verifies the ODE/Volterra/energy powers and records the repaired Cramer constant in `103_22` |
| `103_31_CENTRAL_XI_STABILITY_AND_STRONG_MARGIN_GATE.md` | stability/moment audit | central-theta Jensen target and exact strong-margin exponential; ratio and reciprocal criteria rationally falsified, while Stieltjes and misplaced Jensen strengthenings are excluded by the complex divisor |
| `103_34_FIRST_JENSEN_MINOR_FOR_THETA.md` | theta/Jensen theorem | proves strict log-concavity of the full theta kernel and all degree-two shifted Jensen polynomials; identifies why the covariance proof stops at PF2 |
| `103_36_CUBIC_JENSEN_DISCRIMINANT_GATE.md` | cubic Jensen audit | exact discriminant and ratio-drop factorization; proves PF2 cannot imply PF3 and isolates the third-difference estimate absent from Andreief/Wronskian squares |
| `103_40_EFFECTIVE_SADDLE_LOSS_FOR_CUBIC_GATE.md` | effective saddle audit | unique theta-moment saddle and negligible higher theta modes; Gaussian error is two orders too coarse for the cubic cancellation, requiring a correlated third-order Laplace expansion |
| `103_43_THETA_HAZARD_CONVEXITY_GATE.md` | theta curvature audit | proves hazard convexity for \(u\ge1/4\), isolates the modular compact interval, and derives the exact size-bias update showing why convexity alone does not order the cubic tilted covariances |
| `103_47_THETA_TRANSLATION_TAIL_PF3_CRITERION.md` | theta-specific cubic criterion | exact translate representation of all theta modes; decreasing relative tail moments and a quantitative first-mode-plus-tail sufficient condition; translation mixtures alone are rationally falsified as a PF3 mechanism |
| `103_48_CORRELATED_THETA_TAIL_DISCRIMINANT_AUDIT.md` | correlated theta-tail audit | exact four-factor discriminant expansion retaining all tail errors; rational no-go for deriving its sign from decreasing likelihood ratio or the \(1/300\) tail bound alone |
| `103_49_DIRECT_A1_NEW_MECHANISM.md` | direct A1 flow audit | exact divisor-theta square attempt fails termwise after the required differential operator; an absolutely convergent regulator flow yields a new scalar positive-part budget sufficient for the strong margin |
| `103_53_A1_REGULATOR_FLOW_BUDGET.md` | regulator-flow budget audit | exact prime--pole--Gamma flow increment; mandatory endpoint cancellation and an \(n^n\) loss rule out termwise positive-part bounds, leaving a completed sign/saddle partition |
| `103_57_COMPLETED_ENDPOINT_MATCHING.md` | completed endpoint matching | fixes a non-shrinking \(\delta=1/8\); normalized-Stieltjes Taylor endpoint plus Laguerre-lobe exterior yields a completed sufficient matching inequality, while shrinking split windows are scaled out |
| `103_58_EFFECTIVE_CONDITIONAL_THRESHOLD.md` | effective conditional threshold | replaces the enormous ODE Bessel constant by B=25000, proves an explicit Jensen zero count, and obtains RH-implies-A1 for every n at least n_eff with log(n_eff) below 833334000; the finite gap from 150 to n_eff remains |
| `103_62_INDEPENDENT_EFFECTIVE_THRESHOLD_AUDIT.md` | independent effectivity audit | independently checks the Bessel split, Volterra exponent, Laguerre constants, Jensen count, zero partial summation, transport factors, reserve, and closed threshold in 103_58; records the RH and finite-gap caveats |
| `103_54_A1_BINOMIAL_BARRIER_ATTEMPT.md` | Abel barrier audit | sums the binomial differences before the singular limit, derives the exact pole--prime collision, and quantifies why absolute or lobe bounds cannot control it |
| `103_55_CONVEXITY_BARRIER_FALSE.md` | certified mechanism correction | rigorous eta intervals prove \(\Delta^2D_{147}<0\), eliminating the convexity induction while retaining first-difference and cumulative-curvature targets |
| `103_56_FIRST_DIFFERENCE_A1_GATE.md` | first-difference gate | interval-safe monotonicity certificate through \(n=148\); exact Abel increment and an absolute VK-envelope scale no-go |
| `103_59_SIGNED_FIRST_DIFFERENCE_MECHANISM.md` | signed first-difference audit | proves that first-difference positivity is structurally stronger than RH, carries out exact primitive and prime-mass transports, falsifies generic total-positivity/sign mechanisms, and isolates the fixed-weight paired transport inequality still required |
| `103_60_A1_KERNEL_FACTORIZATION_ATTEMPT.md` | kernel-factorization audit | canonical trivial-zero factors have a convergent negative, not positive, binomial transform; an exact 101st-derivative certificate excludes positive logarithmic mixtures, and the Laguerre pullback destroys the genuine phase-averaged von Mangoldt square |
| `103_61_VON_MANGOLDT_QUANTILE_COST.md` | canonical quantile-cell audit | decomposes the completed cost into exact \(\log p\)-length prime-power cells and a signed Laguerre-lobe matrix; derives the local Chebyshev-deficit term and proves exact opposite signs for the \(p=2\) and \(p=101\) tower responses |
| `103_64_CELL_LOBE_MATRIX_FACTORIZATION.md` | exact cell--lobe collapse | proves \(\sum_qM_q(t)=t-1-\psi(t)\), derives the exact gap--lobe moment matrix, gives the rational minimal \(q=5,n=1\) obstruction to local PSD/total-positive closure, and rationally certifies opposite signs of the convex-order primitive at 2976 and 4000; the Monge cross difference vanishes identically |
| `103_65_STRONG_MARGIN_COLLECTIVE_ALTERNATIVE.md` | collective Gram audit | unconditional angular Gram decomposition of \(2\lambda_n\) plus the exact signed radial-quartet defect; proves that polarized prefix squares collapse to false Loewner positivity and removes the unnecessary RH qualifier from the boundary no-go |
| `103_66_EULER_TOWER_TELESCOPING.md` | exact Euler-tower compression | telescopes each \(p^k\) tower into multiplicative annuli, identifies their collective weight with \(\psi(x)=\log\operatorname{lcm}(1,\ldots,\lfloor x\rfloor)\), and collapses the paired Abel limit to the analytic germ \(-(d/dt)\log(t\zeta(1+t))\) |
| `103_67_COLLECTIVE_PRIME_TOWER_SQUARE_IDENTITY.md` | collective square identity | aggregates every prime-power cell remainder into the exact signed square \(-\frac12\int(\psi-x+1)^2\tau''\), and telescopes the first moments into a cumulative max-index kernel; this sharpens the remaining A1 target without assuming its sign |
| `103_68_COMPLETED_MELLIN_LAW_FACTORIZATION.md` | completed probabilistic factorization | factors the pole--eta--Gamma germ as an exact ratio of Laplace transforms of four explicit laws and rewrites the cumulative margin as coefficients of its logarithm; low derivatives and support exclude a positive independent deconvolution |
| `103_69_COMPLETED_WEIL_AUTOCORRELATION.md` | completed Weil autocorrelation | constructs the exact Laguerre test $f_n$ with $\mathcal W(f_n*f_n^\#)=2\lambda_n$ before the Euler pullback; audits the off-line reciprocal sign and shows divisor Möbius inversion already loses the square at $n=2$ |
| `103_70_VAUGHAN_HEATH_BROWN_LAGUERRE_AUDIT.md` | Type I/II viability audit | exact Vaughan decomposition and Laguerre addition formula; ordinary phase estimates fail by rank-one logarithmic geometry; its initial separate Hardy-norm continuation is retracted by 103_71 |
| `103_71_LAGUERRE_HARDY_NONDUPLICATION_AND_STOP_GATE.md` | nonduplication and stop gate | proves the Hardy generator is exactly Phase 102/233 and a classical Laguerre--Laplace coordinate; separate Cauchy norms lose the required Moebius--divisor cancellation and are discarded |
| `103_52_A1_DISCRETE_RECURRENCE_GATE.md` | direct A1 recurrence audit | exact all-order finite differences of the strong margin; isolates the missing arithmetic barrier as a binomial transform of \(\log(t\zeta(1+t))\) and rules out local-sign shortcuts |
| `103_45_ETA_SUM_INTERCHANGE_IMPLEMENTATION_STATUS.md` | finite-generator implementation | exact interchange reducing the finite Hasse computation to \(O(KM)\) transcendental interval work; later completed by the normalized verifier in `103_51` |
| `103_46_ETA_FIXEDPOINT_EXECUTION_AUDIT.md` | finite-generator execution audit | replaces Fraction logarithms by outward fixed-point `artanh`; its initial timeout is superseded by the completed dual-truncation certificate in `103_51` |
| `103_51_FINITE_STRONG_MARGIN_21_149_CERTIFICATE.md` | exact finite certificate | normalized Hasse/eta coefficient intervals and two independent truncations certify the strong margin for every \(21\le n\le149\) |
| `103_50_INDEPENDENT_ETA_MARGIN_AUDIT.md` | finite-generator algebra audit | verifies the quotient/tail ordering, logarithm recurrence, prime and archimedean reconstruction, and records the corrected audit of the constant coefficient |
| `103_41_HIGH_ORDER_EM_SCALING_BOUNDARY.md` | finite-certificate scaling audit | shows why the present coarse Euler--Maclaurin remainder with \(N=64\) cannot certify the high Stieltjes orders needed through \(n=149\) |
| `103_44_ETA_EULER_TAIL_BOUND.md` | high-order constant generator | Euler-transformed eta expansion with the geometric coefficient tail used by the completed finite certificate `103_51` |
| `103_37_INDEPENDENT_FIRST_JENSEN_AUDIT.md` | independent theta audit | verifies the modular origin matching, curvature constants, normalized-moment lemma, and even-subsequence proof in `103_34` |
| `103_39_CUBIC_GATE_COVARIANCE_AND_STRONG_CURVATURE_NO_GO.md` | cubic curvature audit | exact tilted-covariance form of the cubic gate; a smooth strongly log-concave counterfamily proves that even arbitrarily large curvature cannot imply PF3 generically |
| `103_42_CONVEX_HAZARD_CUBIC_JENSEN_NO_GO.md` | convex-hazard audit | falsifies the proposed increasing-convex-hazard lemma: a rationally certified limit and smooth (h',h''>0) approximants have a negative cubic gate |
| `103_32_FINITE_MARGIN_VERIFIER_INPUT_AUDIT.md` | finite-certificate audit | identifies the high-order Stieltjes and zeta interval inputs missing from the original \(n\le8\) verifier |
| `103_35_RATIONAL_STIELTJES_GENERATOR_PILOT.md` | exact finite certificate | rational Euler--Maclaurin generator plus outward fixed-point propagation; certifies the strong margin for \(9\le n\le20\) without floating point |

## Tools

All in `tools/`, pure Python + numpy, no external dependencies.

* `zeta_tools.py` — complex \(\zeta,\zeta',\psi_{\rm digamma},\xi'/\xi\);
  \(\lambda_n\) by Cauchy integral of the Li generating function.
  Validation: \(\lambda_8=1.46575567714706\), matching the certified
  rational interval of `217` to 14 digits.
* `arch_and_margin.py` — \(A_n=\lambda_n^{\rm arch}\) in its numerically
  stable odd-\(r\) form; strong-margin table; asymptotic fit.
* `laguerre_geometry.py` — rescaled Laguerre recurrence, PR constants, zero
  spacing, the three budgets.
* `raised_kernel.py` — the \(\alpha=3\) kernel used by the summation-by-parts
  estimate.
* `budget_vs_load.py` — budget \(q(n)\) versus absolute loads for the
  envelope family \(W=e^{u/2}u^a\); also recovers the true correlation
  \(\mathcal J_n\) from \(\lambda_n\).
* `conditional_bound_check.py` — evaluates the three diagnostic terms of
  `103_04`; its apparent crossing at \(n=150\) is not a certified threshold.
* `bd_ratio_interval_verify.py` — fraction-only certificates falsifying the
  proposed \(B_D\) ratio condition at \(n=3\) and reciprocal positivity at
  \(n=7\).
* `stieltjes_em_interval_pilot.py` — exact-rational Euler--Maclaurin
  generation of Stieltjes constants and finite strong-margin pilots.
* `fixed_margin_9_20.py` — common-scale integer interval propagation proving
  the strong margin for every \(9\le n\le20\).
* `eta_fixed_generator.py` — exact Hasse weights, outward fixed-point
  logarithms, quotient coefficients, and the proved geometric tail.
* `fixed_margin_eta_21_149.py` — normalized-coefficient propagation proving
  the strong margin for every \(21\le n\le149\).

Reproduce with `cd tools && python3 <file>`.

## Status

* Criteria 1, 2, 4, 7, 8, 9 of the guide: closed.
* Criterion 5: closed on the reserve side.
* Criterion 6: rigorously certified through \(n=149\) (and independently
  numerically checked farther); the requested finite range is closed.  This
  does not by itself make the separate conditional threshold \(150\)
  effective.
* Criterion 3: eventual closure under RH at the qualitative level;
  unconditional closure and an effective threshold remain open.

A1 remains open unconditionally.  Together with the inherited A0 and finite
certificates, its uniform proof would imply RH; no such proof is contained
in the phase at present.
