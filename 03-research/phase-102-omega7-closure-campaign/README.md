# Phase 102 - Omega7 closure campaign

## Purpose

This phase is the single working container for the renewed attack on
`Omega7`, the Li--Keiper positivity statement

[
  \lambda_n\ge0\qquad(n\ge1).
]

The phase inherits the corrected restart plan and the full master context
snapshot stored in

[
  RH-MASTER-CONTEXT-SNAPSHOT/
]

The working rule is simple: a statement is not avoided because it has
force-RH. If it is true and necessary, it is a target. False statements are
corrected; RH-strength statements are proved or isolated as the exact load
still missing.

## Current status

The trunk has four closed entries:

1. Exact target:
   [
     \Omega_7
     \Longleftrightarrow
     \lambda_n^{prime}\ge-\lambda_n^{arch}
     \qquad(n\ge1).
   ]

2. Paired arithmetic continuation of the prime side.

3. Correct Laguerre integration by parts with the boundary term.

4. Finite exceptional range:
   [
     \lambda_n>0,\qquad 1\le n\le7.
   ]

The remaining central target is the infinite range:

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}\qquad(n\ge8).
]

## Working documents

- `PHASE_102_EXECUTION_PLAN.md`: ordered plan and ownership of each open point.
- `PHASE_102_OBLIGATION_LEDGER.md`: live ledger of closed, reduced and open items.
- `102_A0_UNIFORM_TAIL_TARGET.md`: first technical target for the direct Li route.
- `102_A0_UNIFORM_TAIL_THEOREM.md`: proved tail theorem conditional on an
  explicit PNT input; the archimedean lower bound is supplied internally by
  `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`.
- `102_A1_SIGNED_CORE_TARGET.md`: force-RH signed core target.
- `102_BOUNDARY_LIMIT_AND_LIMIT_ORDER.md`: admissible order of limits and the compact-core passage.
- `102_SCALE_DECOMPOSITION_AND_TRUNCATION.md`: scale bookkeeping and truncation rules.
- `102_A1_ZERO_SIDE_DISCRIMINANT.md`: off-line sensitivity requirement.
- `102_A1_SIGNED_COMPENSATION_MECHANISMS.md`: mechanisms and eliminated classes for A1.
- `102_BIBLIOGRAPHIC_GATE.md`: nonduplication check for the Li--Laguerre mechanism.
- `113_MELLIN_COBORDER_NORMAL_FORM.md`: exact Mellin normal form for the A1 core.
- `114_BORDERED_EULER_CURRENT_AUDIT.md`: bordered-current audit and Schur-complement obstruction.
- `115_WEIL_HERGLOTZ_REDUCTION.md`: reduction of Herglotz/Weil positivity to the A1 boundary measure.
- `116_POSITIVE_BOUNDARY_MEASURE_TARGET.md`: single positive-measure theorem that would close A1.
- `117_EULER_PRODUCT_POSITIVE_WEIGHT_AUDIT.md`: audit of the direct positive-coefficient route.
- `118_STIELTJES_INVERSION_SUPPORT_OBSTRUCTION.md`: positive Riesz measure and missing support collapse.
- `119_A1_TRUNCATION_OPTIMIZATION_AUDIT.md`: no-go for closing A1 by cutoff optimization alone.
- `119_BORDERED_EULER_CURRENT_NO_GO_AND_TARGET.md`: sharp bordered-current no-go and exact target.
- `119_DE_BRANGES_GATE_FOR_A1.md`: de Branges/Hermite--Biehler gate for A1.
- `120_TOTAL_POSITIVITY_AND_LI_SEQUENCE_AUDIT.md`: total positivity and Li coefficient audit.
- `121_A1_MARGIN_OR_ONE_SIDED_TAIL_GATE.md`: strong-margin and one-sided-tail gates for A1.
- `121_LI_TEST_FAMILY_SCOPE.md`: scope of the countable Li test family.
- `122_STRONG_MARGIN_REDUCTION.md`: exact prime-side form of the strong-margin gate.
- `123_ONE_SIDED_TAIL_GATE.md`: exact one-sided tail theorem needed beyond A0.
- `124_A1_GATE_IMPLICATION_GRAPH.md`: implication graph and false implications
  for the current A1 gates.
- `125_A1_FIXED_CUTOFF_GENERATING_FUNCTION.md`: fixed-cutoff coefficient
  normal form and moving-cutoff obstruction.
- `126_UNIVERSAL_CUTOFF_GATE_AUDIT.md`: audit showing A0 cannot supply a
  universal finite cutoff for the coefficient route.
- `127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md`: exact cutoff-flow formula and the
  one-sided boundary-current gate.
- `128_TAIL_AND_STRONG_MARGIN_GENERATORS.md`: coefficient generators for the
  strong-margin and tail gates, including the tail domain obstruction.
- `129_ABEL_LAPLACE_TAIL_DOMAIN_AUDIT.md`: tail as a signed Laplace transform
  in \(w=z/(1-z)\), with positivity not supplied by A0.
- `130_FOURIER_BOCHNER_GATE_AUDIT.md`: Fourier-kernel positivity audit and
  reduction to the stronger total-positivity/de Branges gate.
- `131_JENSEN_COFINAL_GATE_AUDIT.md`: Jensen hyperbolicity route, requiring
  cofinal Laguerre--Pólya convergence rather than finite/asymptotic checks.
- `132_HEAT_FLOW_NEWMAN_GATE_AUDIT.md`: heat-flow threshold route; A1 needs
  the threshold at or below zero, not only future real-rootedness.
- `133_LI_DISK_SCHUR_GATE_AUDIT.md`: disk-coordinate Li transform and the
  Schur/Carathéodory boundary-support gate.
- `134_OFFLINE_GEOMETRIC_MODE_LEMMA.md`: elementary proof that exterior Li
  multipliers force negative geometric subsequences.
- `135_ARCHIMEDEAN_GROWTH_BOUND.md`: elementary proof that
  \(\lambda_n^{\rm arch}=O(n\log n)\).
- `136_FINITE_EXTERIOR_SHELL_DOMINANCE.md`: finite maximal exterior shell
  dominance and the remaining infinite-divisor caveat.
- `137_ISOLATED_EXTERIOR_RADIUS_REDUCTION.md`: isolated exterior radius
  reduction and the remaining support-accumulation obstruction.
- `138_ZETA_EXTERIOR_RADIUS_MAXIMUM.md`: zero-side proof that any off-line
  zeta zero gives a finite maximal exterior Li-disk shell.
- `139_ZERO_SIDE_LI_CRITERION_CLOSURE.md`: consolidated zero-side Li
  criterion; arithmetic A1 remains the open sign theorem.
- `140_EULER_GAMMA_LI_GENERATOR.md`: exact Euler--Gamma Li generating
  function with archimedean and pole-paired prime generators.
- `141_PRIME_POLE_INTEGRAL_GENERATOR.md`: exact prime-pole integral
  generator; identifies the generator coefficient problem with the same
  signed Laguerre/A1 core.
- `142_A1_VARIATIONAL_ENERGY_FORM.md`: finite Schur--Friedrichs
  variational normal form for A1 and the missing Euler--Gamma coercive Schur
  lemma.
- `143_PRIME_POLE_PICK_STIELTJES_GATE.md`: Pick/Stieltjes audit for the
  prime-pole generator; local positivity is eliminated and the completed
  boundary-support theorem is isolated.
- `144_LAGUERRE_CORE_SIGN_PARTITION.md`: derivative-kernel collapse
  \(L'_{n-1}^{(1)}-L_{n-1}^{(1)}=-L_{n-1}^{(2)}\) and the canonical
  Laguerre-lobe compensation theorem equivalent to A1.
- `145_LAGUERRE_LOBE_DUAL_BALANCE.md`: once-integrated prime-pole balance
  and lobe duality; A1 becomes a signed bound for cumulative balances
  against Laguerre-lobe variation.
- `146_RAISED_LAGUERRE_DUAL_HIERARCHY.md`: repeated cumulative prime-pole
  balances and the exact raising hierarchy
  \((e^{-u}L_m^{(\alpha)})'=-e^{-u}L_m^{(\alpha+1)}\).
- `147_BALANCE_LAPLACE_JET_FORM.md`: Laplace-transform and finite-jet form
  of the raised balances; A1 becomes a signed jet inequality at \(s=1\).
- `148_A1_FINITE_ARITHMETIC_CERTIFICATE_SCHEMA.md`: explicit finite
  prime-power certificate formula for each raised A1 instance; uniform
  signed proof still required.
- `149_MOVING_DIAGONAL_A1_GENERATOR.md`: fixed-cutoff A1 generator and the
  moving-diagonal coefficient problem created by the A0 cutoffs \(T_n\).
- `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`: exact generator identity
  \(C_n(T)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T)\), linking A1 to
  the strong-margin and one-sided-tail gates.
- `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`: explicit positive
  lower bound \(0<B_n\le\lambda_n^{\rm arch}\) for all \(n\ge8\), closing
  the archimedean lower-bound input for A0.
- `152_EXPLICIT_PNT_INPUT_ADAPTER.md`: exact Vinogradov--Korobov-style PNT
  remainder shape needed by A0 and why constant relative Chebyshev bounds
  are insufficient for the tail.
- `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md`: exact comparison
  \(C_n(T)-C_n(S)\) and the signed cutoff-transfer theorem needed to move
  positivity to the A0 cutoff.
- `154_CUTOFF_TRANSFER_DUAL_BALANCE.md`: accumulated-balance version of
  cutoff transfer, with endpoint term and raised kernel \(L_{n-1}^{(3)}\).
- `155_A1_WEIL_SQUARE_ROOT_GATE.md`: restricted Weil/Mellin test for A1
  and the missing positive square-root/autocorrelation factorization.
- `156_A1_LAGUERRE_N_RECURRENCE_GATE.md`: exact three-term recurrence in
  the Li index \(n\) for \(C_n(T)\), reducing an induction route to a signed
  forcing moment.
- `157_ARCHIMEDEAN_FORCING_AUDIT.md`: corrected explicit formula for the
  archimedean second-order forcing in the \(n\)-recurrence; it is not a
  free positive margin.
- `158_A1_GATE_TRIAGE_AND_PRIORITY.md`: consolidation of A1 gates into
  equivalent normal forms, stronger sufficient routes, eliminated shortcuts,
  and next priority targets.
- `159_INDUCTIVE_FORCING_CERTIFICATE_SCHEMA.md`: finite prime-power and
  archimedean certificate schema for the full forcing in the Laguerre
  induction route.
- `160_INDUCTIVE_FORCING_GENERATOR.md`: fixed-cutoff generating function for
  the recurrence forcing; induction becomes coefficient-sum positivity plus
  moving-cutoff transfer.
- `161_LI_TOEPLITZ_MOMENT_GATE.md`: disk Carathéodory/Toeplitz moment
  formulation of the positive boundary-measure gate; finite checks are
  insufficient.
- `162_LI_FEJER_TRIGONOMETRIC_MOMENT_GATE.md`: equivalent
  trigonometric-polynomial form of the Toeplitz gate; Fejer/Dirichlet kernel
  subtests are separated from the full translated Fejer criterion, which is
  equivalent to Toeplitz positivity.
- `163_PRIME_POLE_FEJER_TOEPLITZ_SUPPORT_GATE.md`: prime-pole/Pick
  refinement of the Fejer criterion; scalar Cesaro tests are insufficient,
  while full translated Fejer positivity is the same boundary-measure gate.
- `164_A1_TOEPLITZ_SCHUR_MARGIN.md`: Schur--Friedrichs Toeplitz
  variational margin; \(Q_n(1-z^n)\ge A_n\), or the stronger innovation
  margin, would imply compact A1 after A0.
- `165_POISSON_CARATHEODORY_POSITIVITY_GATE.md`: Abel/Poisson equivalent of
  the Toeplitz and Fejer gates; the global route is
  \(\Re H_{\rm EG}(z)\ge0\) in the disk with non-circular singularities.
- `166_POISSON_CARATHEODORY_SUPPORT_GATE.md`: sharpened support/no-go form:
  Poisson positivity is exactly infinite Toeplitz positivity, and interior
  singularities are impossible for a true Carathéodory function.
- `167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md`: finite Herglotz measures
  cannot directly encode the unweighted infinite Li zero divisor; the
  Toeplitz/Fejer/Poisson route needs a renormalized Euler--Gamma positive
  object.
- `168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md`: replaces the naive
  finite-measure picture by a positive kernel on polynomials vanishing at
  \(1\), the natural class containing all Li tests \(1-z^n\).
- `169_LI_SCHOENBERG_VANISHING_KERNEL.md`: explicit renormalized kernel
  normal form \(K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}\); positivity is
  a stronger Schoenberg/negative-type route whose diagonal gives Li.
- `170_VANISHING_KERNEL_PAIRING_NO_GO.md`: local no-go for constructing the
  Li vanishing kernel by the functional-equation cross-pairing; off the unit
  circle the required two-point matrix is indefinite, so a positive
  Euler--Gamma form needs new terms or an independent support proof.
- `171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md`: diagonal and local positive
  counterterms that preserve all Li-test values orbitwise must vanish; the
  first two Li tests already span the non-fixed two-point orbit.  The same
  Cauchy--Schwarz rigidity rules out any positive global counterterm
  invisible on all Li diagonals.
- `172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md`: exact equivalence between
  Schoenberg kernel positivity and Toeplitz positivity of the Li
  second-difference sequence
  \(g_0=2\lambda_1,\ g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\).
- `173_WEIGHTED_ZERO_DIVISOR_MEASURE_GATE.md`: zero-side interpretation of
  \(g_m\) as moments of the transformed divisor weighted by
  \(|1-w_\rho|^2\), giving the finite-measure form of the renormalized route.
- `174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md`: the increment
  Toeplitz gate is equivalent to
  \(\Re(\xi'/\xi)(s)\ge0\) for \(\Re s>1/2\), a compact global
  Carathéodory target.
- `175_LOG_DERIVATIVE_RH_EQUIVALENCE.md`: proves that
  \(\Re(\xi'/\xi)(s)\ge0\) in \(\Re s>1/2\) is equivalent to RH via the
  no-interior-pole direction and the Hadamard product under RH.
- `176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md`: equivalent horizontal
  monotonicity form
  \(\partial_\sigma\log|\xi(\sigma+it)|\ge0\), with the explicit
  Euler--Gamma signed inequality.
- `177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md`: proves the half-plane
  positivity unconditionally for \(\Re s>1\); the missing RH-strength
  extension is the strip \(1/2<\Re s\le1\).
- `178_STRIP_POISSON_BOUNDARY_NO_GO.md`: strip Poisson boundary signs are
  favorable, but the argument requires zero-freeness in the strip, which is
  exactly the missing RH-strength input.
- `179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md`: interior off-line zeros
  create explicit sign-changing pole defects
  \(m\Re(s-\rho)^{-1}\), so strip Green/Poisson proofs must account for
  these negative local terms.
- `180_STRIP_POISSON_KERNEL_FORMULA.md`: explicit Poisson kernel formula in
  the strip; positivity follows from boundary data only after the zero-free
  strip hypothesis is supplied.
- `181_GLOBAL_POSITIVITY_VS_COMPACT_A1_MARGIN.md`: separates the global
  RH/Li closure route from the stronger quantitative margin needed to close
  compact A1 after the A0 tail budget.
- `182_HORIZONTAL_ZERO_BARRIER_NO_GO.md`: local zero-barrier theorem for
  horizontal modulus monotonicity; an off-line zero forces
  \(\partial_\sigma\log|\xi|\to-\infty\) from the left, so bounded boundary
  or subharmonic arguments cannot close the strip target.
- `183_EXACT_CUMULATIVE_FORCING_REPRESENTATION.md`: solves the fixed-cutoff
  A1 recurrence exactly; Target E is a weighted cumulative forcing
  inequality plus moving-cutoff transfer.
- `184_MOVING_DIAGONAL_RECURRENCE_DEFECT.md`: exact recurrence on the A0
  diagonal \(T_n\), with the two explicit cutoff-transfer defects added to
  the forcing.
- `185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md`: rewrites the diagonal
  forcing \(F_n^{\rm diag}\) as one signed integral against a piecewise
  Laguerre kernel plus the explicit archimedean correction.
- `186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md`: inserts the diagonal forcing
  kernel into the cumulative induction weights, producing one compact signed
  kernel \(\mathcal H_n\) on \([0,T_n]\).
- `187_CUMULATIVE_DIAGONAL_BALANCE_FORM.md`: integrates the cumulative
  diagonal pairing once and shows that the exact balance contains a raised
  piecewise Laguerre kernel plus signed cutoff jumps.
- `188_DIAGONAL_CUMULATIVE_COERCIVITY_AUDIT.md`: proves that symmetric
  envelope bounds for \(E\) give only the absolute-value lower bound for
  the \(\mathcal H_n\) pairing; diagonal coercivity needs a one-sided
  arithmetic theorem or the explicit absolute sufficient inequality.
- `189_GLOBAL_LOG_DERIVATIVE_TO_COMPACT_A1_AUDIT.md`: exact audit of the
  implication from global log-derivative positivity to compact A1.  The
  global theorem closes Omega7 through RH/Li, but compact A1 additionally
  needs the bridge
  \(R_n(T_n)\le\lambda_n-\frac14\lambda_n^{\rm arch}\), the strong margin
  \(\lambda_n\ge\frac12\lambda_n^{\rm arch}\), or a direct signed-core
  proof.
- `190_DIAGONAL_BALANCE_FINITE_CERTIFICATE.md`: expands the balance form
  with jumps into the exact finite certificate
  \(\mathcal A_n+\Pi_n+\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)\ge0\).
- `191_ABSOLUTE_DIAGONAL_BUDGET_SCALE_AUDIT.md`: audits the absolute
  sufficient route from `188`; an envelope \(R\) closes only if
  \(\mathcal B_n\ge\int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du\), with
  explicit scale forms for constant-relative, log-power and
  Vinogradov--Korobov profiles.
- `192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md`: refines the
  global-to-compact bridge.  Global Toeplitz/Schoenberg positivity gives
  \(\lambda_n\ge0\), but the one-sided tail inequality is exactly A1 in
  tail form and still needs a margin, tail--margin correlation,
  Loewner/Schur comparison, or direct compact proof.
- `193_WEIGHTED_L1_KERNEL_CERTIFICATE.md`: turns the absolute diagonal load
  \(W_n(R)\) into a finite sign-partition certificate over the zeros of the
  piecewise polynomial cumulative kernel \(\mathcal H_n\).
- `194_STRONG_MARGIN_GENERATOR_SECOND_PASS.md`: exact generator
  \(\mathcal M_{\rm SM}=\mathcal L-\frac12\mathcal A\) for the strong
  margin; global Toeplitz/Schoenberg positivity gives only
  \(Q_n(1-z^n)\ge0\), while compact A1 via A0 needs
  \(Q_n(1-z^n)\ge\lambda_n^{\rm arch}\).
- `195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md`: states the exact comparative
  form
  \(\mathfrak Q^{\mathcal L}-\frac14\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T_n}\) whose positivity on \(1-z^n\), or on a
  containing finite subspace, would imply the moving-diagonal A1
  inequality.  Bare global Toeplitz positivity does not imply this Loewner
  order.
- `196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md`: canonical list of the
  remaining exact theorem statements that would close A1: direct compact
  core, absolute \(L^1\) domination, strong margin, one-sided tail,
  comparative Loewner--Schur order, or the global half-plane theorem.
- `197_CUMULATIVE_KERNEL_INTERVAL_FORM.md`: exact interval formula for
  \(\mathcal H_n\); the terminal interval is
  \(-L_{n-1}^{(2)}\), while earlier intervals are cumulative Laguerre
  mixtures not controlled by standard interlacing alone.
- `198_STRONG_MARGIN_SECOND_DIFFERENCE_AUDIT.md`: rewrites the strong margin
  in increment Toeplitz coordinates:
  \(n g_0+2\sum_{m<n}(n-m)g_m\ge\lambda_n^{\rm arch}\); positivity of the
  \(g\)-Toeplitz matrices gives only nonnegativity of this Dirichlet energy.
- `199_COMPARATIVE_INNOVATION_MARGIN_GATE.md`: Schur/innovation refinement
  of the comparative form.  A1 follows if the comparative block is positive
  on a chosen space \(U_n\) and the innovation
  \(\inf_{u\in U_n}\mathfrak Q^{\mathcal C,T_n}(1-z^n-u,1-z^n-u)\) is
  nonnegative; computing this after assuming the A1 diagonal is circular.
- `200_FEJER_MASS_STRONG_MARGIN_GATE.md`: quantitative Fejer-mass gate for
  the strong margin; a sufficient condition is local increment-measure mass
  \(\nu_g(|\theta|\le1/n)\ge(\pi^2/4)\lambda_n^{\rm arch}/n^2\).
- `202_FEJER_DENSITY_SCALE_GATE.md`: density-scale audit for the Fejer
  strong-margin route; bounded absolutely continuous density is too small,
  so a successful route needs logarithmic or stronger concentration near
  \(\zeta=1\), or another signed proof.
- `203_ATOM_AT_ONE_INCOMPATIBILITY_AUDIT.md`: eliminates the atom-at-one
  shortcut for the actual Euler--Gamma Li generator; such an atom would
  force quadratic Li growth and a cubic pole in \(\mathcal L(z)\).
- `204_LOG_DENSITY_INCREMENT_GENERATOR_GATE.md`: log-density normal form for
  the Fejer route; \(\mathcal G_+(z)=\lambda_1+\xi'/\xi(1/(1-z))\) has the
  logarithmic boundary scale compatible with logarithmic density, but this
  gives only scale compatibility, not the needed lower bound.
- `205_FEJER_LOG_CONSTANT_AUDIT.md`: constant audit for the Fejer/log-density
  route; \(\lambda_n^{\rm arch}\sim\frac12n\log n\), a density
  \(a\log(e/|\theta|)\) gives Abel coefficient \(a/2\) and Fejer coefficient
  \(a\), so constants are favorable in the ideal \(a=1\) model, but the
  positive-measure and lower-Fejer theorem remain open.
- `206_FEJER_ABEL_TAUBERIAN_GAP.md`: Tauberian-gap audit for the same route.
  Abel kernels are smooth, while Fejer kernels have moving zeros; mass near
  \(2\pi k/n\) can be visible to Abel and nearly invisible to the \(n\)-th
  Fejer test, so Abel logarithmic growth alone cannot supply the margin.
- `207_A0_TERMINAL_CUTOFF_BRIDGE_AUDIT.md`: audits whether A0 cutoffs
  automatically control the terminal Laguerre load.  The previous cutoff
  gives
  \(\mathcal T_n\le c_nB_{n-1}\log((1+T_n)/(1+T_{n-1}))\), so this step
  still needs a cutoff-ratio/surplus condition; the earlier non-terminal
  intervals are isolated later and collapsed in `219`.
- `208_VK_CUTOFF_RATIO_TERMINAL_SCALE.md`: evaluates that ratio for
  canonical Vinogradov--Korobov cutoffs.  It gives
  \(\log((1+T_n)/(1+T_{n-1}))={5\over3n}+O(1/(n\log n))\), hence terminal
  load \((5/72)\log n+O(1)\); \(\mathcal B_n\) and non-terminal kernel
  control remain at this point in the chronology.
- `209_ARCHIMEDEAN_BUDGET_SIGN_AUDIT.md`: shows that the recurrence
  archimedean forcing satisfies
  \(D_n^{\rm arch}=-\frac12\log n+O(1)\), so
  \(1+\frac34D_n^{\rm arch}\) is eventually negative.  The absolute route
  therefore needs a full lower bound for \(\mathcal B_n\), not just
  positivity of the weights.
- `210_BASE_BUDGET_QUADRATIC_COEFFICIENT_GATE.md`: isolates the coefficient
  \(\Gamma_{\mathcal B}\) with
  \(\mathcal B_n=\Gamma_{\mathcal B}n^2+O(n\log n)\).  If positive, it
  absorbs the terminal \(O(\log n)\) VK load for large \(n\); if not, the
  terminal absolute route needs another reserve.
- `211_MIXED_INTERVAL_OFFDIAGONAL_LOAD_GATE.md`: isolates the remaining
  nonterminal absolute-route obstruction.  On \((T_j,T_{j+1})\),
  \(\mathcal H_n\) contains Laguerre degrees up to \(n-2\), so A0 decay
  calibrated at \(T_j\) does not automatically control the mixed \(L^1\)
  load.
- `212_BASE_BUDGET_TELESCOPING_REDUCTION.md`: telescopes the infinite
  archimedean series in \(\Gamma_{\mathcal B}\), giving
  \(\Gamma_{\mathcal B}=(1+\Delta_8^\ast)/16
  -3(\lambda_8^{\rm arch}-\lambda_7^{\rm arch})/64\).  Positivity reduces
  to the finite threshold
  \(\Delta_8^\ast>-0.7175270082\ldots\).
- `213_GAMMA_B_COMPACT_BASE_IDENTITY.md`: substitutes the compact definition
  of \(\Delta_8^\ast\) and shows
  \(\Gamma_{\mathcal B}=(I_7(T_7)-I_8(T_8))/16\).  The terminal budget sign
  is exactly the finite base comparison \(I_7(T_7)>I_8(T_8)\), not an
  infinite archimedean question.
- `214_GAMMA_B_BASE_FINITE_CERTIFICATE.md`: expands
  \(I_7(T_7)-I_8(T_8)\) as a finite prime-power certificate with elementary
  endpoint functions \(\Phi_7,\Phi_8,\Psi_7,\Psi_8\).  It makes
  \(\Gamma_{\mathcal B}>0\) directly checkable once \(T_7,T_8\) are fixed.
- `215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md`: shows that choosing
  the auxiliary cutoff \(0<T_7\le\min(\log2,1/130)\) makes
  \(I_7(T_7)>-1\).  Then the already-required base condition
  \(C_8^\ast\ge0\) forces \(I_8(T_8)<-29/4\), so
  \(\Gamma_{\mathcal B}>0\) follows without a separate sign certificate.
- `216_BASE_C8_COMPACT_CERTIFICATE.md`: expands the base condition
  \(C_8^\ast\ge0\) as the finite inequality
  \(\Psi_8(T_8)-\sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  \ge 8-\frac34A_8\).  It also records the finite strong-margin shortcut
  \(\lambda_8\ge\frac12A_8\).
- `217_N8_BASE_MARGIN_CERTIFICATE.md`: executes that finite strong-margin
  shortcut by extending the rational Stieltjes verifier to \(n=8\).  It
  proves \(\lambda_8-\frac12\lambda_8^{\rm arch}>1.4553\), so A0 gives
  \(C_8^\ast>0\) and, with `215`, \(\Gamma_{\mathcal B}>0\).
- `218_MIXED_A0_DEGREE_MISMATCH_AUDIT.md`: shows that the crude mixed
  estimate using only A0 decay at \(T_j\) and the elementary Laguerre bound
  leaves a factor \((1+u)^{k-j-2}\) for \(k>j\).  Thus the mixed route needs
  an off-diagonal Laguerre theorem, mixture cancellation, or a signed proof.
- `220_TERMINAL_EFFECTIVE_THRESHOLD_REDUCTION.md`: records the exact
  terminal defect \(\mathfrak D_n=\mathcal B_n-\Theta_n\).  After `217`,
  the terminal interval is absorbed for all sufficiently large \(n\) because
  \(\Gamma_{\mathcal B}>25/64\) while the canonical VK terminal load is
  \(O(\log n)\); the remaining terminal work is a finite rational threshold
  certificate.
- `219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md`: performs the cumulative
  mixture cancellation missing from `218`.  The weights telescope, giving
  \(\mathcal H_n=-L_{n-1}^{(2)}\) on \(T_8<u<T_n\).  The mixed off-diagonal
  obstruction is replaced by a single-Laguerre weighted \(L^1\) problem plus
  two low-cutoff degree-7 correction intervals.
- `221_SINGLE_LAGUERRE_BULK_L1_OBSTRUCTION.md`: shows that this collapsed
  absolute \(L^1\) route fails for VK envelopes.  In the bulk \(u\asymp n\),
  Laguerre Plancherel--Rotach growth contributes \(e^{u/2}\), while VK
  relative decay is only subexponential; the load is exponential and cannot
  be bounded by \(\mathcal B_n=O(n^2)\).
- `222_SIGNED_BALANCE_TELESCOPED_CERTIFICATE.md`: pushes the telescoping
  collapse through the signed balance identity.  All jumps after \(T_8\)
  vanish; only \(T_7,T_8\) remain.  The viable signed route is reduced to a
  finite prime-power inequality with \(L_{n-1}^{(3)}\) and fixed degree-7
  corrections.
- `223_SIGNED_BALANCE_B_ENVELOPE_NO_GO.md`: shows that the signed balance
  cannot be closed by a two-sided envelope for \(B(U)\).  Such a bound again
  becomes an absolute \(L^1\) estimate, now for \(L_{n-1}^{(3)}\), and VK
  decay fails in the Laguerre bulk.
- `224_STRONG_MARGIN_RH_STRENGTH_AUDIT.md`: records that the strong-margin
  route is RH-strength.  Together with the finite \(1\le n\le7\)
  certificate, it implies all Li coefficients are nonnegative and therefore
  RH by Li's criterion.
- `225_A1_POST_ABSOLUTE_ROUTE_DECISION_LEDGER.md`: consolidates the current
  decision state.  Base, terminal asymptotic, and mixed structural gates are
  closed; VK absolute and symmetric \(B\)-envelope routes are discarded; the
  remaining routes require signed arithmetic or RH-strength input.
- `226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md`: removes the
  integrated \(B\)-layer from `222`.  The signed pairing is expanded
  directly, and each prime-power coefficient is an endpoint expression in
  \(e^{-u}L_{n-1}^{(1)}\) plus fixed degree-7 corrections.
- `227_SMALL_T7_PRIME_BLOCK_ELIMINATION.md`: uses the strict auxiliary
  normalization \(0<T_7<\log2\) to remove the \(\log m<T_7\) prime block.
  The direct signed certificate now has only two arithmetic regimes:
  \(T_7\le\log m<T_8\) and \(T_8\le\log m\).
- `228_HIGH_BLOCK_LAGUERRE_CORRELATION_FORM.md`: rewrites the high block as
  a Chebyshev mass term minus the signed correlation
  \(\sum\Lambda(m)m^{-1}L_{n-1}^{(1)}(\log m)\).  This isolates the
  remaining high-block arithmetic theorem.
- `229_SMALL_T7_DIRECT_COEFFICIENT_REDUCTION.md`: combines `226`--`228`
  into one direct signed target.  The only moving arithmetic object left is
  \(\sum_{m\le e^{T_n}}\Lambda(m)m^{-1}L_{n-1}^{(1)}(\log m)\), plus fixed
  base-window constants below \(T_8\).
- `230_SINGLE_TRANSFORM_A1_FRONTIER.md`: reconciles the telescoped route
  with the original compact core.  A1 is exactly a one-transform inequality
  for \(S_n(T_n)=\sum_{m\le e^{T_n}}\Lambda(m)m^{-1}
  L_{n-1}^{(1)}(\log m)\).
- `231_HIGH_BLOCK_PARTIAL_SUMMATION_FORM.md`: applies partial summation to
  the high correlation.  It becomes
  \(A_8(T_n)L_{n-1}^{(1)}(T_n)+\int A_8(u)L_{n-2}^{(2)}(u)\,du\), so the
  remaining theorem is a signed weighted-discrepancy integral.
- `232_WEIGHTED_MERTENS_ENVELOPE_NO_GO.md`: shows that a two-sided bound
  for the weighted Mertens discrepancy \(E_8^\sharp\) is still insufficient:
  it creates an absolute \(L^1\) load for \(L_{n-2}^{(2)}\), and the
  Laguerre bulk beats VK-subexponential decay.
- `233_SINGLE_TRANSFORM_FIXED_CUTOFF_GENERATOR.md`: packages
  \(S_n(T)\) into a fixed-cutoff generating function.  It shows exactly
  what fixed-\(T\) coefficient positivity would prove and why A1 still
  needs moving-cutoff positivity along \(T=T_n\).
- `235_MOVING_CUTOFF_DERIVATIVE_GATE.md`: computes the exact cutoff
  derivative.  \(C_n(T)\) is continuous at prime-power jumps, and between
  jumps
  \(C_n'(T)=-(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)\).  Moving a fixed-cutoff
  proof to \(T_n\) therefore needs a signed integral theorem.
- `236_SINGLE_TRANSFORM_ZERO_SIDE_MARGIN_AUDIT.md`: records why a
  zero-side explicit formula or Li/RH positivity does not by itself prove
  compact A1.  The explicit-formula route still needs strong margin,
  one-sided tail placement, or an equivalent compact margin theorem.
- `237_CUTOFF_TRANSFER_TAIL_EQUIVALENCE.md`: shows that moving positivity
  from a fixed or infinite cutoff to \(T_n\) is exactly a signed
  tail/correlation theorem.  Symmetric A0-style estimates close A1 only
  with strong margin.
- `238_TAIL_MARGIN_COMPENSATION_FRONTIER.md`: writes
  \(C_n(T_n)=M_n+\delta_n\), where
  \(M_n=\lambda_n-\frac12\lambda_n^{\rm arch}\) and
  \(\delta_n=\frac14\lambda_n^{\rm arch}-R_n(T_n)\ge0\).  A1 requires the
  tail surplus to compensate any strong-margin deficit.
- `239_MARGIN_TAIL_THRESHOLD_LADDER.md`: quantifies the tradeoff.  If
  \(\lambda_n\ge\kappa_n A_n\) and \(R_n(T_n)\le\rho_nA_n\), then A1 follows
  exactly when \(\kappa_n-\rho_n\ge1/4\).  A0 corresponds to
  \(\rho_n=1/4\), hence requires strong margin \(\kappa_n\ge1/2\).
- `240_DEFICIT_RATIO_TAIL_SURPLUS_GATE.md`: normalizes that tradeoff.
  With \(d_n=(-M_n)_+/A_n\) and \(s_n=\delta_n/A_n\), compact A1 is exactly
  \(s_n\ge d_n\).
- `241_TAIL_SURPLUS_GENERATOR_DIAGONAL_NO_GO.md`: defines the surplus
  generator \(\Delta_T=\frac14\mathcal A-\mathcal R_T\) with
  \([z^n]\Delta_{T_n}=\delta_n\), and proves
  \(\mathcal M+\Delta_T=\mathcal C_T\).  Its cutoff flow is
  \(d[z^n]\Delta_T/dT=-E(e^T)e^{-T}L_{n-1}^{(2)}(T)\).  Thus isolated
  surplus positivity does not close A1; the missing statement is the
  comparative diagonal
  bound \([z^n]\Delta_{T_n}\ge-[z^n]\mathcal M\).
- `242_LOEWNER_CONE_MARGIN_TAIL_DECOMPOSITION.md`: decomposes the
  comparative form as
  \(\mathfrak Q^{\mathcal C,T}
  =\mathfrak Q^{\mathcal M}+\mathfrak Q^{\Delta,T}\).  On \(1-z^n\) this is
  \(2(M_n+\delta_n)=2C_n(T_n)\), so a non-circular Loewner proof must prove
  domination of the negative margin cone by the tail-surplus cone on a
  larger space.
- `243_LOEWNER_NEGATIVE_PART_COMPENSATION_REDUCTION.md`: refines the cone
  target by splitting \(\mathfrak Q^{\mathcal M}\) into positive and
  negative spectral parts on a finite comparison space.  A sufficient
  theorem is
  \(\mathfrak Q^{\Delta,T_n}\succeq\mathfrak Q^{\mathcal M}_-\), which
  reduces on \(1-z^n\) to \(\delta_n\ge-M_n\).
- `244_A0_TAIL_IMPROVEMENT_REQUIREMENT.md`: normalizes the precise extra
  strength needed beyond A0.  With
  \[
    \eta_n=\frac14-{R_n(T_n)\over A_n},\qquad
    d_n=\max\left(0,\frac12-{\lambda_n\over A_n}\right),
  \]
  A0 is \(\eta_n\ge0\), while compact A1 is exactly
  \(\eta_n\ge d_n\).  Equivalently, the signed Chebyshev--Laguerre tail
  integral must exceed \((d_n-\frac14)A_n\).
- `245_TERMINAL_THRESHOLD_DATA_DEPENDENCE_CERTIFICATE.md`: separates the
  terminal finite task from A1.  The asymptotic sign
  \(\mathfrak D_n>0\) is closed for sufficiently large \(n\), but an
  executable threshold requires a fixed cutoff policy, ratio bounds,
  \(B_{n-1}\) bounds, base intervals, archimedean summand intervals, and a
  finite check.
- `246_GLOBAL_HALF_PLANE_COMPACT_A1_SEPARATION.md`: records that the global
  half-plane theorem would close Omega7 through RH/Li, but contributes only
  \(d_n\le1/2\) to compact A1.  Together with A0's \(s_n\ge0\), this still
  does not imply the compact gate \(s_n\ge d_n\).
- `247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md`: isolates a weaker
  RH-strength sufficient route than strong margin:
  \(\lambda_n\ge A_n/4\) plus \(R_n(T_n)\le0\).  It is exactly the
  \(d_n\le1/4,\ s_n\ge1/4\) point of the margin-tail ladder.
- `248_QUARTER_MARGIN_GENERATOR_RH_STRENGTH_AUDIT.md`: defines
  \(\mathcal Q_{1/4}=\mathcal L-\frac14\mathcal A\), so
  \([z^n]\mathcal Q_{1/4}=\lambda_n-\frac14A_n\).  Positivity for
  \(n\ge8\), together with the finite low-index certificate, already implies
  Li positivity/RH.
- `249_TAIL_SIGN_LAGUERRE_ZERO_PARTITION_GATE.md`: writes the condition
  \(R_n(T_n)\le0\) as a signed lobe inequality over the zeros of
  \(L_{n-1}^{(2)}\) lying beyond \(T_n\), plus the final ray.  A0 gives only
  a lower bound by \(-A_n/4\), not the required nonnegative sign.
- `250_NONPOSITIVE_TAIL_SYMMETRIC_ENVELOPE_NO_GO.md`: proves that the
  tail sign \(R_n(T_n)\le0\) cannot follow from a symmetric envelope
  \(|E(e^u)|\le W(u)\) alone, because the tail functional is odd under
  \(E\mapsto-E\).
- `251_RDI_LI_COEFFICIENT_EXTRACTION_GATE.md`: fixes the exact bridge
  needed for RDI to imply Li: local uniform convergence in the coordinate
  \(s=1/(1-z)\) to
  \(z(1-z)^{-2}\xi'/\xi(1/(1-z))\), with nonnegative approximating
  coefficients, or locally uniform real-rooted convergence to \(\Xi\).
- `310_REAL_RAY_CONVERGENCE_NOT_LI_COEFFICIENT_NO_GO.md`: gives the model
  \(F_N(z)=z/(1+N^2z^2)\), which converges pointwise to \(0\) on the real
  axis but has fixed linear coefficient \(1\).  Real-ray convergence cannot
  replace local uniform complex convergence for RDI coefficient extraction.
- `252_SCHUR_ZERO_COUPLING_DIAGONAL_COLLAPSE.md`: shows that if the
  comparative Schur coupling \(b_n\) vanishes, the Schur innovation equals
  \(2C_n(T_n)\).  Zero coupling therefore collapses to the A1 diagonal and
  is not a separate proof mechanism.
- `253_DISK_HERGLOTZ_MEASURE_HALF_PLANE_GATE.md`: rewrites the global
  semiplane theorem as a disk Herglotz representation for
  \(H_\xi(z)=2\xi'/\xi(1/(1-z))\).  A positive boundary measure constructed
  before using zero support would imply RH/Omega7; defining it from
  critical-line zeros would be circular.
- `290_RADIAL_ABEL_POSITIVITY_NOT_HERGLOTZ_NO_GO.md`: shows that positive
  radial Abel values or logarithmic radial growth of \(H_\xi(r)\) do not
  imply disk Herglotz positivity.  The missing global theorem is angular
  Carathéodory/Toeplitz positivity, not merely positivity on \(0<r<1\).
- `300_CENTERED_FEJER_TESTS_NOT_TOEPLITZ_NO_GO.md`: gives an explicit
  Hermitian sequence whose centered Fejer sums are all positive but whose
  \(3\times3\) Toeplitz block is not positive.  Centered Li/Fejer diagonal
  tests are therefore not a construction of the Herglotz measure.
- `324_FINITE_TOEPLITZ_BLOCKS_NOT_HERGLOTZ_GATE.md`: shows that, for every
  fixed \(N\), the blocks \(T_L\) for \(L\le N\) can all be positive while
  \(T_{N+1}\) is indefinite.  Finite Toeplitz checks are evidence only, not
  a Herglotz-measure construction.
- `254_TAIL_SIGN_EXPLICIT_FORMULA_PHASE_GATE.md`: expresses the signed tail
  \(I_n(T)=\int_T^\infty E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du\) through the
  explicit formula as a one-sided phase inequality over the zeros with
  weights \(\Phi_{n,T}(\rho)/\rho\).
- `255_TAIL_MARGIN_CORRELATION_SLACK_FORM.md`: introduces the correlation
  slack \(h_n\) by \(R_n(T_n)\le A_n/4-h_n\), and shows A1 follows exactly
  when \(h_n\ge(-M_n)_+\).  Normalized, this is the already isolated gate
  \(s_n\ge d_n\).
- `256_POINTWISE_DUAL_CONE_AND_AVERAGE_GATE.md`: proves the dual form of
  compact A1: every finitely supported nonnegative average of
  \(C_n(T_n)\) must be nonnegative, and smoothed positivity closes A1 only
  if each coordinate mass is positively reconstructible or if a genuine
  coefficient-extraction theorem is supplied.
- `257_AVERAGED_SLACK_POINTWISE_NO_GO.md`: shows that averaged,
  density-one, cofinal, or purely asymptotic slack information does not
  imply the pointwise gate \(h_n\ge(-M_n)_+\) unless it is made effective at
  every index, with finite certificates for exceptions.
- `258_CRITICAL_LINE_SUPPORT_TAIL_PHASE_NO_GO.md`: separates RH-location
  data from compact A1 tail-phase data.  Support of the zero measure on the
  critical line does not by itself imply the one-sided incomplete-Laguerre
  phase inequality needed for \(R_n(T_n)\le0\) or \(s_n\ge d_n\).
- `274_TAIL_PHASE_LOBE_DUALITY_GATE.md`: identifies the Laguerre lobe
  tail inequality of `249` and the zero-phase inequality of `254` as the
  same signed functional.  Unsigned lobe bounds and zero-modulus bounds
  cannot combine into the one-sided tail sign.
- `280_TAIL_PHASE_LOBE_BALANCE_GATE.md`: decomposes the critical-line
  phase kernel into positive and negative parts and shows that the tail
  route is exactly the lobe dominance condition
  \(P_{n,T_n}^- - P_{n,T_n}^+\) above the explicit trivial-tail/deficit
  margin.
- `275_PHASE_COMPLETION_CRITERION_A1_AND_GLOBAL.md`: separates external
  Omega7 closure from compact A1 closure.  Since the requested goal
  includes A1, a global RH/Li proof alone is not enough unless the compact
  A1 certificate \(C_n(T_n)\ge0\), or an equivalent bridge, is also proved.
- `276_LOEWNER_SUBSPACE_COFINALITY_GATE.md`: states the cofinality
  requirement for Loewner--Schur tests.  Positivity on a subspace proves A1
  only if the subspace contains \(p_n=1-z^n\), or if \(p_np_n^*\) is
  positively reconstructed from the tested rank-one directions.
- `277_FINITE_CERTIFICATE_EFFECTIVE_THRESHOLD_GATE.md`: records the exact
  limitation of pointwise arithmetic certificates.  Finite verification
  closes only checked indices unless paired with either a uniform theorem
  for all \(n\ge8\) or an explicit effective threshold \(N_\infty\) plus
  rigorous interval verification below it.
- `278_COFINAL_SUBSEQUENCE_CERTIFICATE_NO_GO.md`: rules out the
  infinite-but-subsequential shortcut.  Certificates on a cofinal or
  density-one set still omit coordinates, and therefore do not prove A1
  unless a propagation, positive-reconstruction, or effective-threshold
  theorem covers every missing index.
- `259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md`: gives a conditional strong
  margin closure theorem: a positive increment measure plus an explicit
  lower Fejer bound, or logarithmic boundary density coefficient \(a>1/2\),
  implies \(\lambda_n\ge A_n/2\) beyond an effective threshold and reduces
  the rest to finite interval verification.
- `260_EXACT_FEJER_LOG_KERNEL_CONSTANT.md`: proves the exact Fejer/log
  kernel identity
  \(\int F_nL\,dm=H_{n-1}-(n-1)/n\), hence the uniform lower bound
  \(\int F_nL\,dm\ge\log n-1\).  This fixes \(B_L=1\) in the conditional
  log-density route.
- `261_FEJER_FINITE_REMAINDER_CERTIFICATE_SCHEMA.md`: records the exact
  finite certificate left after the Fejer/log-density threshold.  For
  \(8\le n<N_\infty\), one must verify either the strong margin
  \(\lambda_n\ge A_n/2\) by rigorous intervals or the compact coefficient
  \(C_n(T_n)\ge0\) directly.
- `262_EXPLICIT_ARCHIMEDEAN_UPPER_FEJER_INPUT.md`: proves the explicit
  archimedean upper input
  \(\lambda_n^{arch}\le \frac12 n\log n+3n\) for \(n\ge2\).  This fixes
  \(B_A=3\), \(N_A=2\) in the Fejer/log-density closure threshold.
- `263_LOCAL_LOG_DENSITY_TO_GLOBAL_FEJER_PATCH.md`: repairs the
  local-to-global step in the Fejer route.  A local lower density
  \(h\ge aL-B_h\) near \(\zeta=1\), with \(h\ge0\) globally, implies the
  global Fejer lower bound with
  \(B_h^\ast=\max\{B_h,a(-\log(2\sin(\theta_0/2)))_+\}\).
- `264_FEJER_ROUTE_EXPLICIT_THRESHOLD_LEDGER.md`: combines `260`, `262`,
  and `263` into the explicit strong-margin threshold
  \(N_\infty=\max(2,\lceil\exp((3+a+B_h^\ast)/(a-1/2))\rceil)\), leaving
  only the positive increment measure, local density theorem, and finite
  interval certificate.
- `265_FEJER_LOG_DENSITY_ABEL_COEFFICIENT_BUDGET.md`: compares the
  logarithmic density model with the actual Abel growth of
  \(\mathcal G_+\).  A lower density coefficient \(a\) must satisfy
  \(a\le1\), while the Fejer margin requires \(a>1/2\); the live window is
  \(1/2<a\le1\).
- `266_ABEL_TO_FEJER_DEFECT_GATE.md`: isolates the exact loss term in any
  Abel-to-Fejer transfer.  With
  \(D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+\), a Fejer lower bound follows
  from Abel logarithmic mass only if the defect integral is
  anti-concentrated strongly enough, e.g. \(d<1/2\) in the natural
  Euler--Gamma normalization with \(\alpha=1\).
- `291_ABEL_DEFECT_CONSTANT_THRESHOLD_LEDGER.md`: turns the Abel-defect
  route into an explicit constant ledger.  If
  \(\int P_{1-1/n}\,d\nu_g\ge\log n-B_P\) and
  \(\int(P_{1-1/n}-\alpha F_n)_+\,d\nu_g\le d_\alpha\log n+B_D\) with
  \(d_\alpha<1-\alpha/2\), then strong margin holds for
  \(n\ge N_\infty(\alpha)\), with
  \(N_\infty(\alpha)=\max(N_0,2,\lceil\exp((3+B_\alpha)/(q_\alpha-1/2))\rceil)\).
  The finite remainder is exactly the certificate of `261`.
- `292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md`: rewrites the
  defect theorem as a geometric bad-set condition.  For
  \(B_{n,\tau}=\{F_n<\tau P_{1-1/n}\}\),
  \[
    D_{n,\alpha}\le
    P_n{\bf1}_{B_{n,\tau}}+(1-\alpha\tau)_+P_n{\bf1}_{B_{n,\tau}^c}.
  \]
  Hence a Poisson-weighted bound
  \(\int_{B_{n,\tau}}P_n\,d\nu_g\le b_\tau\log n+B_B\), with
  \(b_\tau+(1-\alpha\tau)_+<1-\alpha/2\), feeds directly into `291`.
- `293_FEJER_POISSON_BAD_SET_GEOMETRY_GATE.md`: proves that the bad sets
  contain \(1/n\)-scale windows around every nontrivial \(n\)-th root of
  unity.  Thus the `292` estimate is a genuine arithmetic
  anti-concentration theorem for \(\nu_g\), not a trivial geometric
  small-set bound.
- `311_BAD_SET_CARLESON_WINDOW_SUFFICIENT_CONDITION.md`: gives the
  complementary sufficient direction.  The bad set is contained in
  \(1/n\)-scale windows around all \(n\)-th roots, and a Carleson bound
  \(\nu_g(I_{n,k})\le(\rho_\tau\log n+B_\tau)/n\) on those moving windows
  implies the `292` estimate with \(b_\tau=C_\tau'\rho_\tau\).  Optimizing
  the Abel constants leaves the target
  \(C_\tau'\rho_\tau<1-1/(2\tau)\), \(\tau>1/2\).
- `296_WEIGHTED_CARLESON_BAD_SET_GATE.md`: sharpens `311` by replacing
  uniform root-window control with the weighted condition
  \(\sum_k n\nu_g(I_{n,k})/(1+\kappa(k)^2)\le\beta_\tau\log n+B_\tau\).
  This matches the Poisson weight and leaves the target
  \(C_\tau\beta_\tau<1-1/(2\tau)\).
- `297_CENTRAL_FLOOR_WEIGHTED_BUDGET_GATE.md`: combines the central
  lower floor from `314` with the upper target of `292`/`296`.  For local
  log-density coefficient \(a\), the Abel bad-set route at \(\tau\) needs
  \(aK(\tau)<1-1/(2\tau)\), and any weighted proof must fit
  \(aK(\tau)\le C_\tau\beta_\tau<1-1/(2\tau)\).
- `316_CENTRAL_FLOOR_COMPATIBILITY_WINDOW.md`: proves that this central
  floor does not by itself make the Abel bad-set route impossible in the
  live range \(a\le1\).  At \(\tau=3/2\), \(c=3/2\) is admissible, while
  \(R(17/10)>3/2\) forces \(K(3/2)\le(2/\pi)\arctan(17/10)<2/3\), leaving
  strict budget before the target \(1-1/(2\tau)=2/3\).
- `314_BAD_SET_CENTRAL_WINDOW_LOG_MASS_FLOOR.md`: records the necessary
  central-window cost in the same route.  Since
  \(F_n(1)/P_{1-1/n}(1)\to1/2\), every \(\tau>1/2\) makes
  \(B_{n,\tau}\) contain a \(1/n\)-scale window around \(1\).  A local
  lower density \(h\ge aL-B\) then forces
  \(b_\tau\ge a(2/\pi)\arctan c_\tau\) for any central scale
  \(c_\tau\) with \(R(u)<\tau\) on \(|u|\le c_\tau\).
- `294_LOCAL_DENSITY_NOT_BAD_SET_ANTI_CONCENTRATION_NO_GO.md`: separates
  the local log-density route from the Abel-defect route.  A positive
  measure may satisfy the local lower-density hypothesis near \(1\) while
  sparse positive spikes at moving Fejer zeros force arbitrarily large
  Poisson-weighted bad-set coefficients.
- `295_BOUNDED_DENSITY_BAD_SET_ZERO_COEFFICIENT_GATE.md`: removes bounded
  absolutely continuous density from the bad-set obstruction.  If
  \(d\nu=h\,dm\) with \(0\le h\le H\), then
  \(\int_{B_{n,\tau}}P_{1-1/n}\,d\nu\le H\), so its logarithmic bad-set
  coefficient is zero.
- `312_LOG_KERNEL_ABEL_DEFECT_MODEL_LEDGER.md`: computes the canonical
  logarithmic-density model for the Abel defect.  For
  \(L=-\log|2\sin(\theta/2)|\),
  \[
    \int(P_{1-1/n}-\alpha F_n)_+L\,dm
    =
    \kappa_\alpha\log n+o_\alpha(\log n),
  \]
  where \(\kappa_\alpha\) is an explicit one-dimensional scaling
  integral.  This separates the harmless model log-kernel defect from the
  still-open Euler--Gamma remnant anti-concentration problem.
- `315_LOG_KERNEL_DEFECT_OPTIMIZATION_LEDGER.md`: compares
  \(\kappa_\alpha\) with the Abel-defect budget \(1-\alpha/2\).  The pure
  log-kernel model has positive leading margin, with a coarse optimum near
  \(\alpha=3/4\), so the live obstruction is the residual bad-set mass, not
  the logarithmic model itself.
- `325_EG_REMAINDER_BAD_SET_CERTIFICATE_SCHEMA.md`: combines `291`,
  `296`, and `312`--`315` into one effective certificate for the
  Euler--Gamma remnant.  If
  \(d\nu_g=aL\,dm+d\rho\), it is enough to certify the log-kernel defect
  upper coefficient and a direct or weighted bad-set defect bound for
  \(\rho\) with
  \(a\kappa_\alpha^+ + e_\alpha < 1-\alpha/2\), then apply the explicit
  threshold and finite remainder.
- `328_POISSON_LOWER_NOT_LOG_DOMINATION_NO_GO.md`: shows that a Poisson
  lower bound at \(1\) does not imply measure domination \(\nu\ge aL\,dm\).
  The model \(\delta_1\) has Poisson values \(2n-1\ge\log n\) but gives no
  mass to arcs away from \(1\) where \(L>0\).  The Fejer decomposition must
  be proved separately or replaced by a direct defect estimate.
- `313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md`: shows that the direct A1
  prime-power certificate cannot close by termwise coefficient positivity.
  The high-block coefficients are
  \(e^{-T_n}L_{n-1}^{(1)}(T_n)-e^{-\log m}L_{n-1}^{(1)}(\log m)\), and they
  inherit the oscillations of \(e^{-u}L_{n-1}^{(1)}(u)\).  Direct A1 must
  therefore use signed global compensation.
- `298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md`: exposes the minimal
  block unit for that compensation.  Partitioning by the sign lobes of
  \(G_{n-1}(T_n)-G_{n-1}(u)\), direct A1 is exactly
  \(H_n^+-H_n^-+B_n^{\rm base}\ge0\); absolute lobe load bounds are
  insufficient without oriented dominance.
- `299_LOBE_BLOCK_PARTIAL_SUMMATION_GATE.md`: applies exact partial
  summation on each direct lobe block.  The direct route becomes an
  oriented Chebyshev-error inequality over the Laguerre lobes, not a
  two-sided Chebyshev-envelope estimate.
- `329_DIRECT_A1_ORIENTED_CHEBYSHEV_MINIMAL_THEOREM.md`: records the
  exact direct theorem left after the lobe reductions:
  \(\sum_jH_{n,j}^{err}\ge-B_n^{base}-\sum_jH_{n,j}^{main}\).  It also
  rules out the monotonicity shortcut: nonnegative prime-power mass must be
  placed with the correct Laguerre orientation, not merely counted.
- `320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md`: gives the tail-side
  sufficient criterion matching the lobe balance.  Lower envelopes for
  \(E(e^u)\) on positive \(e^{-u}L_{n-1}^{(2)}\)-lobes and upper envelopes
  on negative lobes certify \(I_n(T_n)\ge(d_n-1/4)A_n\) when their oriented
  lobe lower bound has enough margin.
- `322_TAIL_LOBE_INTERVAL_CERTIFICATE_SCHEMA.md`: turns the `320` criterion
  into an auditable interval certificate.  Each index needs isolated tail
  zeros of \(L_{n-1}^{(2)}\), lobe-weight enclosures, oriented one-sided
  bounds for \(E(e^u)\), and a rigorous comparison with
  \((d_n-1/4)A_n\).
- `326_TAIL_LOBE_STEP_ENVELOPE_EFFECTIVE_REDUCTION.md`: shows that on
  every bounded tail lobe the required constant one-sided envelope for
  \(E(e^u)=\psi(e^u)-e^u\) is exactly a finite prime-power endpoint
  computation.  The remaining genuinely infinite input is the final-ray
  one-sided weighted theorem, plus all-index or effective-threshold
  coverage.
- `327_FINAL_RAY_ABSOLUTE_COST_GATE.md`: gives a valid hybrid use of a
  two-sided PNT/VK envelope on the final ray only.  After bounded lobes are
  certified arithmetically, the final ray contributes the explicit cost
  \(\int_{\xi_{n,*}}^\infty W(u)e^{-u}|L_{n-1}^{(2)}(u)|\,du\), which must
  be absorbed in the pointwise A1 margin.
- `321_DIRECT_TAIL_LOBE_TRANSFER_GATE.md`: records that the compact direct
  lobe route and the tail lobe route transfer only through the full compact
  identity.  The derivative relation \(\omega_n'=e^{-u}L_{n-1}^{(2)}\) is
  not positivity-preserving and cannot replace the missing signed theorem.
- `270_POISSON_TO_FEJER_POSITIVE_INVERSE_NO_GO.md`: proves that no nonzero
  positive combination of radial Poisson kernels is dominated by a Fejer
  kernel \(F_N\), because \(F_N\) vanishes at nontrivial \(N\)-th roots.
  Abel/Poisson lower data therefore cannot yield the Fejer lower bound by a
  positive inverse kernel.
- `271_POSITIVE_INCREMENT_FEJER_MASS_SEPARATION.md`: proves the logical
  separation between a positive increment measure and compact A1.  Such a
  measure gives \(\lambda_n\ge0\) through
  \(2\lambda_n=n\int F_n\,d\nu_g\), hence global Omega7 if constructed
  non-circularly, but A1 still needs the quantitative Fejer lower bound
  \(\int F_n\,d\nu_g\ge A_n/n\), equivalently the lower log-density theorem
  with \(1/2<a\le1\) plus finite verification.
- `272_FEJER_MASS_LOCALIZATION_NECESSARY_GATE.md`: proves a necessary
  localization condition for any Fejer lower bound of size \(\log n\):
  \(F_n\) is bounded by \(\min(n,\pi^2/(n\theta^2))\), so the compact route
  needs logarithmic mass in the corresponding localized near-one quantity.
- `273_FEJER_LAYER_CAKE_DISTRIBUTION_GATE.md`: rewrites the Fejer mass
  theorem as
  \(\int_0^n\nu_g\{F_n\ge t\}\,dt\ge A_n/n\), the exact distribution
  condition behind the local-density and Abel-defect routes.
- `281_ABEL_SPIKE_FEJER_ZERO_MODEL_NO_GO.md`: gives an explicit finite
  positive measure
  \(\nu=\sum_j(\log N_j/N_j)\delta_{e^{2\pi i/N_j}}\) with
  superexponential \(N_j\).  At \(r_{N_j}=1-1/N_j\), the Poisson integral is
  \(\gg\log N_j\), while \(F_{N_j}\) vanishes on the main atom and the other
  atoms contribute only \(O(1)\).  Thus radial Abel/\(\mathcal G_+\)-scale
  information does not imply the Fejer margin or a local log-density
  theorem; anti-concentration or direct Fejer density remains necessary.
- `234_WEIGHTED_MERTENS_CHEBYSHEV_ERROR_IDENTITY.md`: expresses
  \(E_8^\sharp\) exactly through the ordinary Chebyshev error \(E(e^u)\).
  The weighted-Mertens frontier is therefore another coordinate form of
  the same signed Chebyshev--Laguerre core.
- `201_TERMINAL_LAGUERRE_LOAD_GATE.md`: terminal necessary gate for the
  absolute route; any such proof must first dominate
  \(\int_{T_{n-1}}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du\), with an
  exact sign-partition formula using zeros of \(L_{n-1}^{(2)}\).
- `102_RDI_BRIDGE_TRIAGE.md`: carril B bridge status.
- `102_RDI_TO_LI_MINIMAL_BRIDGE.md`: minimal theorem needed for RDI to re-enter.
- `102_LI_ASSEMBLY_CONDITIONAL_THEOREM.md`: final Li assembly once the infinite range is proved.
- `103_POINT_05_GLOBAL_SIGNED_INEQUALITY.md` through `112_CARRIL_B_POINTS_17_25.md`: pointwise execution notes for the remaining Omega7 obligations.

## Closing criterion

This phase closes Omega7 only if it contains a complete proof of

[
  \lambda_n\ge0\qquad(n\ge1),
]

with the finite range and the infinite range both proved, all limits declared,
and Li's theorem applied without an open intermediate hypothesis.
