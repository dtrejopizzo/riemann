# Phase 102 obligation ledger

## Trunk

| Point | Status | Reference |
|---|---|---|
| 1. Exact target | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/LIVE_FRONTIER_AND_RESTART_PLAN.md` |
| 2. Paired arithmetic continuation | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/LIVE_FRONTIER_AND_RESTART_PLAN.md` |
| 3. Integration by parts with boundary term | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/LIVE_FRONTIER_AND_RESTART_PLAN.md` |
| 4. Finite exceptional range | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/fragments/OMEGA7_POINT4_FINITE_CERTIFICATE.md` |
| 5. Global signed inequality | Open | `103_POINT_05_GLOBAL_SIGNED_INEQUALITY.md` |
| 6. Boundary limit | Reduced | `105_POINT_06_BOUNDARY_LIMIT.md` |
| 7. All `n` scales | Reduced | `106_POINT_07_ALL_N_SCALES.md` |
| 8. Sign before estimate | Open | `107_POINT_08_SIGN_PRESERVATION.md` |
| 9. Arithmetic discriminant | Formulated | `108_POINT_09_ARITHMETIC_DISCRIMINANT.md` |
| 10. Typed off-line sensitivity | Formulated control | `109_POINT_10_TYPED_OFFLINE_SENSITIVITY.md` |
| 11. Li assembly | Conditional closed | `110_POINT_11_LI_ASSEMBLY.md` |

## Carril A

| Point | Status | Reference |
|---|---|---|
| 12. Signed unit | Reduced | The only current unit is global; see `102_A1_SIGNED_COMPENSATION_MECHANISMS.md` |
| 13. Global compensation | Open | A1 |
| 14. Signed truncation error | Closed for the far tail modulo explicit decaying PNT input | `102_A0_UNIFORM_TAIL_THEOREM.md`, `102_A0_UNIFORM_TAIL_AUDIT.md`, `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`, `152_EXPLICIT_PNT_INPUT_ADAPTER.md` |
| 15. Uniformity | Reduced | Tail audited; core remains A1 |
| 16. Literal Li inequality | Open | A0 plus A1 |

## Carril B

| Point | Status | Reference |
|---|---|---|
| 17. BTG-DIV | Open | `RH-MASTER-CONTEXT-SNAPSHOT/fragments/OMEGA7_CARRIL_B_TRIAGE.md` |
| 18. LP interface | Open | Same |
| 19. GAP-Z | Open | Same |
| 20. RDI-ANCHOR/core | Open | Same |
| 21. RDP-SHELL | Open | Same |
| 22. SAFE-PROLATE-BRIDGE | Open | Same |
| 23. SAFE-LIMIT-POINT | Conditional only | Same |
| 24. SR-SAFE | Open | Same |
| 25. RDI implies Li | Minimal theorem stated | `102_RDI_TO_LI_MINIMAL_BRIDGE.md` |

## Current reduced form

Omega7 is closed if the phase proves:

[
  \lambda_n>0\qquad(1\le n\le7),
]

and

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}\qquad(n\ge8).
]

The first statement is closed. A0 closes the far tail of the second statement.
The remaining live problem is A1, the signed finite core for `n>=8`.

## Current bottleneck

After the phase 102 reductions, every open obligation in the direct route is
concentrated in A1:

[
  -n+\int_1^{e^{T(n)}}(\psi(y)-y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

The surviving nonlocal mechanisms have now been normalized:

- `113_MELLIN_COBORDER_NORMAL_FORM.md` gives the exact contour normal form and
  isolates its missing sign theorem.
- `114_BORDERED_EULER_CURRENT_AUDIT.md` eliminates tautological Schur
  complements and isolates the required independent bordered positivity.
- `115_WEIL_HERGLOTZ_REDUCTION.md` reduces the Weil/Herglotz route to the
  construction of a positive Euler--Gamma boundary measure.
- `116_POSITIVE_BOUNDARY_MEASURE_TARGET.md` states the cleanest current
  force-RH target: construct that positive boundary measure from Euler--Gamma
  data.
- `117_EULER_PRODUCT_POSITIVE_WEIGHT_AUDIT.md` eliminates direct positivity
  of Euler-product weights as a closure route.
- `118_STIELTJES_INVERSION_SUPPORT_OBSTRUCTION.md` shows that ordinary
  inversion gives positivity of the divisor measure but leaves the support
  collapse, exactly the RH-strength content.
- `119_A1_TRUNCATION_OPTIMIZATION_AUDIT.md` eliminates cutoff optimization
  alone as a source of the A1 sign.
- `119_BORDERED_EULER_CURRENT_NO_GO_AND_TARGET.md` gives the sharp Schur
  complement no-go and the exact surviving bordered theorem.
- `119_DE_BRANGES_GATE_FOR_A1.md` reduces the de Branges route to an
  independent Hermite--Biehler construction from Euler--Gamma data.
- `120_TOTAL_POSITIVITY_AND_LI_SEQUENCE_AUDIT.md` eliminates finite total
  positivity and identifies infinite total positivity with the same boundary
  measure target.
- `121_A1_MARGIN_OR_ONE_SIDED_TAIL_GATE.md` records two exact gates that
  would close A1: a strong Li margin or a genuinely one-sided tail theorem.
- `121_LI_TEST_FAMILY_SCOPE.md` confirms that restricting to the Li test
  family is minimal but still RH-strength.
- `122_STRONG_MARGIN_REDUCTION.md` rewrites the strong-margin gate as the
  sharper signed prime lower bound
  \(\lambda_n^{prime}\ge-{1\over2}\lambda_n^{arch}\).
- `123_ONE_SIDED_TAIL_GATE.md` formulates the signed tail theorem that would
  improve A0 into an A1 closure and records why PNT tails do not provide it.
- `124_A1_GATE_IMPLICATION_GRAPH.md` consolidates the implication graph for
  all current A1 gates and lists the false implications that must not be used.
- `125_A1_FIXED_CUTOFF_GENERATING_FUNCTION.md` gives the exact holomorphic
  generating function for the fixed-cutoff compact core and isolates the
  moving-cutoff obstruction \(T_n\).
- `126_UNIVERSAL_CUTOFF_GATE_AUDIT.md` proves that the current A0 sufficient
  condition cannot provide a finite universal cutoff for all \(n\), so the
  fixed-cutoff coefficient route needs a new signed cutoff theorem.
- `127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md` gives the exact derivative of the
  compact core with respect to the cutoff and reduces the moving-cutoff route
  to a one-sided boundary-current inequality.
- `128_TAIL_AND_STRONG_MARGIN_GENERATORS.md` writes the strong-margin and
  tail gates as coefficient problems and records the half-domain obstruction
  for the tail transform under A0/PNT input.
- `129_ABEL_LAPLACE_TAIL_DOMAIN_AUDIT.md` changes to the variable
  \(w=z/(1-z)\), identifies the tail as a signed Laplace transform on
  \(\Re w\ge0\), and eliminates the inference from A0 convergence to
  Herglotz/Stieltjes positivity.
- `130_FOURIER_BOCHNER_GATE_AUDIT.md` eliminates ordinary Fourier-measure
  positivity as a route from \(\Xi\) to real zeros and isolates the stronger
  total-positivity/de Branges theorem that would be needed.
- `131_JENSEN_COFINAL_GATE_AUDIT.md` identifies the Jensen route as cofinal
  hyperbolicity plus Laguerre--Pólya convergence, and eliminates finite or
  fixed-degree asymptotic Jensen checks as closure.
- `132_HEAT_FLOW_NEWMAN_GATE_AUDIT.md` identifies the heat-flow route as the
  threshold theorem \(\Lambda\le0\), and eliminates eventual positive-time
  real-rootedness as a closure of A1.
- `133_LI_DISK_SCHUR_GATE_AUDIT.md` rewrites the Li transform in disk
  coordinates \(w_\rho=1-1/\rho\), identifies the Schur/Carathéodory support
  theorem needed, and eliminates divisor-defined boundary measures as
  circular.
- `134_OFFLINE_GEOMETRIC_MODE_LEMMA.md` proves the elementary fact that an
  exterior Li multiplier \(|w|>1\) forces a negative geometric subsequence,
  strengthening the off-line discriminator.
- `135_ARCHIMEDEAN_GROWTH_BOUND.md` proves
  \(\lambda_n^{\rm arch}=O(n\log n)\), so the archimedean budget cannot
  absorb an exterior geometric Li mode.
- `136_FINITE_EXTERIOR_SHELL_DOMINANCE.md` proves the finite maximal-shell
  version of the off-line discriminator and records the extra difficulties
  for an infinite divisor.
- `137_ISOLATED_EXTERIOR_RADIUS_REDUCTION.md` extends the discriminator to
  isolated exterior radii and isolates the remaining accumulation/support
  problem near the unit circle.
- `138_ZETA_EXTERIOR_RADIUS_MAXIMUM.md` proves that any off-line zeta zero
  produces a finite maximal exterior Li-disk shell, removing the infinite
  exterior-support caveat on the zero side.
- `139_ZERO_SIDE_LI_CRITERION_CLOSURE.md` consolidates the zero-side
  equivalence between Li positivity and critical-line support, and separates
  it from the still-open arithmetic A1 sign.
- `140_EULER_GAMMA_LI_GENERATOR.md` writes the exact Euler--Gamma generating
  function \(\mathcal L(z)=z\,d/dz\log\xi(1/(1-z))\), with the archimedean
  generator and the pole-paired prime generator separated.
- `141_PRIME_POLE_INTEGRAL_GENERATOR.md` rewrites the pole-paired prime
  generator as the exact integral against \(\psi(y)-y\), recovering the
  Laguerre coefficient formula and showing that the generator route lands
  on the same A1 compact sign theorem.
- `142_A1_VARIATIONAL_ENERGY_FORM.md` rewrites the compact A1 scalar as a
  finite Schur--Friedrichs variational minimum.  The exact remaining theorem
  is the Euler--Gamma coercive Schur lemma.
- `143_PRIME_POLE_PICK_STIELTJES_GATE.md` audits the Pick/Stieltjes route:
  the Euler-product half-plane has a positive measure, but the pole-paired
  Li-boundary object is signed.  A useful positive-measure proof must be the
  completed boundary-support theorem.
- `144_LAGUERRE_CORE_SIGN_PARTITION.md` proves the derivative-kernel
  collapse
  \(L'_{n-1}^{(1)}-L_{n-1}^{(1)}=-L_{n-1}^{(2)}\) and rewrites A1 as an
  alternating lobe-compensation inequality over the simple positive zeros
  of \(L_{n-1}^{(2)}\).
- `145_LAGUERRE_LOBE_DUAL_BALANCE.md` integrates the Chebyshev error once
  on each Laguerre lobe, giving the exact cumulative balance
  \(B(U)=\sum_{m\le e^U}\Lambda(m)(U-\log m)-e^U+1\) and the dual lobe
  theorem still required for A1.
- `146_RAISED_LAGUERRE_DUAL_HIERARCHY.md` iterates the dual balance: the
  \(r\)-fold balance
  \(B_r(U)=r!^{-1}\sum_{m\le e^U}\Lambda(m)(U-\log m)^r-e^U+
  \sum_{k<r}U^k/k!\) pairs with the raised kernel
  \(e^{-u}L_{n-1}^{(2+r)}\).  This is an equivalent A1 hierarchy, not a
  proof by smoothing.
- `147_BALANCE_LAPLACE_JET_FORM.md` takes the Laplace transform of the
  balances:
  \(\mathcal B_r(s)=-(H(s)+1)/s^{r+1}\) in the infinite half-plane and a
  finite arithmetic transform \(\mathcal B_{r,T}\) on the compact core.
  The raised A1 inequality becomes a finite signed jet at \(s=1\).
- `148_A1_FINITE_ARITHMETIC_CERTIFICATE_SCHEMA.md` expands the finite jet
  into explicit prime-power sums, endpoint values and elementary
  exponential-polynomial moments.  It is a pointwise certificate schema; the
  remaining theorem is a uniform signed bound for all \(n\ge8\).
- `149_MOVING_DIAGONAL_A1_GENERATOR.md` writes the fixed-cutoff compact A1
  generator \(\mathcal C_T(z)\) and isolates the actual moving-diagonal
  condition \([z^n]\mathcal C_{T_n}(z)\ge0\).  This prevents replacing A1
  by coefficient positivity for one fixed cutoff.
- `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md` proves the generator-level
  sign identity
  \(C_n(T)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T)\), aligning the A1
  diagonal generator with the strong-margin and one-sided-tail gates.
- `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md` supplies an explicit
  positive \(B_n\le\lambda_n^{\rm arch}\) for every \(n\ge8\).  This closes
  the archimedean lower-bound input in A0; only the explicit PNT remainder
  remains external to the A0 tail theorem.
- `152_EXPLICIT_PNT_INPUT_ADAPTER.md` states the exact external PNT shape
  still needed by A0: a decaying Vinogradov--Korobov-style relative error.
  It also records that constant relative Chebyshev bounds do not make the
  A0 tail integral converge.
- `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md` gives the exact
  comparison
  \(C_n(T)-C_n(S)=-\int_S^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du\).  It
  isolates the signed cutoff-transfer theorem and rules out formal
  monotonicity in \(T\).
- `154_CUTOFF_TRANSFER_DUAL_BALANCE.md` integrates the cutoff-transfer
  identity once.  The required transfer theorem becomes an accumulated
  balance inequality involving \(B_S(T)e^{-T}L_{n-1}^{(2)}(T)\) and the
  raised kernel \(L_{n-1}^{(3)}\).
- `155_A1_WEIL_SQUARE_ROOT_GATE.md` isolates the restricted Weil test
  underlying A1.  The missing theorem is a positive square-root or
  autocorrelation factorization of the completed compact test, not merely
  the linear explicit formula.
- `156_A1_LAGUERRE_N_RECURRENCE_GATE.md` derives the exact recurrence
  \(nC_{n+1}=(2n+1)C_n-(n+1)C_{n-1}+F_n\).  An induction route now reduces
  to a signed cumulative lower bound for the forcing \(F_n\), plus
  moving-cutoff transfer on the A0 diagonal.
- `157_ARCHIMEDEAN_FORCING_AUDIT.md` corrects the archimedean
  second-order piece of \(F_n\):
  \(D_n^{\rm arch}=\sum_{r\ {\rm odd}}[(1-1/r)^{n-1}(1/r+n/r^2)-1/r]\).
  It is explicit but not a free positive margin; the induction obstruction
  is the full signed forcing.
- `158_A1_GATE_TRIAGE_AND_PRIORITY.md` separates exact A1 rewritings from
  stronger sufficient theorems and eliminated shortcuts.  It sets the next
  priority as either local arithmetic signed balance/induction or global
  Euler--Gamma positivity.
- `159_INDUCTIVE_FORCING_CERTIFICATE_SCHEMA.md` expands the full recurrence
  forcing \(F_n(T)\) into finite prime-power sums, a pole polynomial and the
  explicit archimedean correction.  It supplies the pointwise certificate
  schema needed for the induction route.
- `160_INDUCTIVE_FORCING_GENERATOR.md` writes the same forcing as a
  fixed-cutoff generating function \(\mathcal F_T\).  The induction route is
  a coefficient-sum positivity theorem for \(\mathcal F_T\), plus
  moving-cutoff transfer.
- `161_LI_TOEPLITZ_MOMENT_GATE.md` reformulates the disk Schur route as an
  infinite Toeplitz moment problem.  Finite Toeplitz checks are not enough;
  a non-circular infinite moment theorem would imply the positive boundary
  measure gate.
- `162_LI_FEJER_TRIGONOMETRIC_MOMENT_GATE.md` rewrites the same infinite
  Toeplitz gate as positivity of the Euler--Gamma moment functional on every
  squared trigonometric polynomial, equivalently positivity of all translated
  Fejer means.  Untranslated or finite Fejer tests are only diagnostics.
- `163_PRIME_POLE_FEJER_TOEPLITZ_SUPPORT_GATE.md` applies the Fejer criterion
  to the prime-pole/Pick route.  It separates scalar Cesaro positivity, which
  cannot close A1, from full translated Fejer positivity, which is exactly
  the positive boundary-measure theorem in Cesaro form.
- `164_A1_TOEPLITZ_SCHUR_MARGIN.md` connects the Schur--Friedrichs energy
  form to Toeplitz prediction error.  It proves
  \(\lambda_n={1\over2}Q_n(1-z^n)\) under the moment normalization and
  isolates the sufficient margin \(Q_n(1-z^n)\ge A_n\), or the stronger
  innovation margin, needed to imply compact A1 after A0.
- `165_POISSON_CARATHEODORY_POSITIVITY_GATE.md` records the Abel/Poisson
  equivalent of the same moment problem:
  \(\Re H_{\rm EG}(z)\ge0\) in the disk.  This is the analytic form of the
  positive boundary-measure theorem.
- `166_POISSON_CARATHEODORY_SUPPORT_GATE.md` sharpens the same route with
  the no-interior-pole obstruction: if the exact singularities are the
  transformed nontrivial zeros, real-part positivity forces boundary
  support.  The non-circular Euler--Gamma construction and, for compact A1,
  the archimedean square margin remain open.
- `167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md` corrects the naive finite
  moment interpretation.  A finite Herglotz measure has bounded moments and
  cannot directly encode the unweighted infinite Li zero divisor.  The
  surviving global route must first construct a renormalized positive
  Euler--Gamma object, positive current, or vanishing-test Hilbert form.
- `168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md` isolates that
  vanishing-test form: on the critical-line model
  \(\sum_\rho |p(w_\rho)|^2\) converges for \(p(1)=0\), and
  \(p_n=1-z^n\) gives the Li square.  The open theorem is the non-circular
  Euler--Gamma construction of this positive kernel or its A1 margin.
- `169_LI_SCHOENBERG_VANISHING_KERNEL.md` writes the vanishing-test kernel
  in Li coefficients:
  \(K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}\).  Positivity of all such
  matrices is a stronger negative-type theorem; its diagonal gives Li, but
  the non-circular Euler--Gamma proof remains open.
- `170_VANISHING_KERNEL_PAIRING_NO_GO.md` proves the exact local obstruction
  for the direct functional-equation pairing: the orbit involution is
  \(w\mapsto1/\overline w\), and the Li cross-pairing has local matrix
  \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) on a non-fixed two-point orbit.
  Hence it is indefinite unless \(|w|=1\); the surviving route must use new
  positive Euler--Gamma terms, direct Schoenberg positivity, or an
  independent support theorem.
- `171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md` rules out orbitwise positive
  repairs that preserve every local Li-test value: on a non-fixed orbit the
  vectors \(1-z\) and \(1-z^2\) already span \(\mathbb C^2\), so a positive
  counterterm vanishing on all Li tests is identically zero.  Its global
  Cauchy--Schwarz form also rules out any positive counterterm on
  \((z-1)\mathbb C[z]\) that is invisible on every Li diagonal.
- `172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md` proves the exact equivalence
  between positivity of the anchored Schoenberg kernel
  \(K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}\) and Toeplitz positivity of
  the second-difference sequence
  \(g_0=2\lambda_1,\ g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\).  This is a
  full positive-definite sequence target, not coefficientwise convexity.
- `173_WEIGHTED_ZERO_DIVISOR_MEASURE_GATE.md` gives the zero-side meaning of
  those second differences: on the critical-line model they are moments of
  the transformed zero divisor weighted by \(|1-w_\rho|^2\).  The weight
  makes the divisor finite and supplies the correct renormalized
  finite-measure target, but its positivity still must be proved
  non-circularly from Euler--Gamma data.
- `174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md` cancels the Li
  Jacobian in the increment generator and shows that the same gate is
  precisely
  \(\Re(\xi'/\xi)(s)\ge0\) for \(\Re s>1/2\).  This would exclude all
  right-half critical-strip zeros by the no-interior-pole argument and close
  Omega7 by Li, but the inequality itself remains open.
- `175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` proves the converse as well:
  under RH, the paired Hadamard product gives
  \(\xi'/\xi(s)=\sum_\rho (s-\rho)^{-1}\), whose real part is nonnegative
  for \(\Re s>1/2\).  Thus the half-plane positivity theorem is exactly
  RH-strength.
- `176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md` rewrites the same theorem
  as horizontal monotonicity
  \(\partial_\sigma\log|\xi(\sigma+it)|\ge0\), and expands it into the
  exact Euler--Gamma signed inequality involving pole, Gamma and prime
  terms.  Symmetry of \(\xi\) and subharmonicity do not supply this
  monotonicity.
- `177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md` proves the unconditional
  part of the log-derivative positivity theorem:
  \(\Re(\xi'/\xi)(s)>0\) for \(\Re s>1\), by the zero-side Hadamard product
  and the fact that all nontrivial zeros lie in \(0<\Re\rho<1\).  The open
  part is exactly the strip \(1/2<\Re s\le1\).
- `178_STRIP_POISSON_BOUNDARY_NO_GO.md` audits the strip Dirichlet method:
  \(\Re(\xi'/\xi)=0\) on the critical-line boundary away from zeros and is
  nonnegative on \(\Re s=1\), but applying Poisson in the strip requires
  holomorphy there.  That holomorphy is the missing zero-free theorem.
- `179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md` records the missing Green
  terms when interior zeros are removed from the strip.  A zero
  \(\rho=\beta+i\gamma\), \(\beta>1/2\), contributes
  \(m\Re(s-\rho)^{-1}\), which is negative on the left of \(\rho\) and
  blows up negatively near the pole.
- `180_STRIP_POISSON_KERNEL_FORMULA.md` writes the explicit strip Poisson
  kernel
  \[
    P_L(x,y)={1\over2L}{\sin(\pi x/L)\over
    \cosh(\pi y/L)-\cos(\pi x/L)}
  \]
  and shows that the boundary signs imply interior positivity only under the
  zero-free strip hypothesis.
- `181_GLOBAL_POSITIVITY_VS_COMPACT_A1_MARGIN.md` separates closure routes:
  global half-plane positivity would close Omega7 through RH and Li, but the
  compact A1 decomposition still needs the strong margin
  \(\lambda_n\ge {1\over2}\lambda_n^{\rm arch}\), a one-sided tail theorem,
  or a direct signed-core proof.
- `182_HORIZONTAL_ZERO_BARRIER_NO_GO.md` records the local barrier version
  of the strip obstruction: if \(\rho=\beta+i\gamma\), \(\beta>1/2\), is a
  zero of multiplicity \(m\), then on \(t=\gamma\)
  \(\partial_\sigma\log|\xi(\sigma+i\gamma)|=m/(\sigma-\beta)+O(1)\),
  which tends to \(-\infty\) from the left.  Thus bounded boundary,
  Poisson, or subharmonic corrections cannot prove the horizontal
  monotonicity theorem without excluding or singularly neutralizing the
  zero.
- `183_EXACT_CUMULATIVE_FORCING_REPRESENTATION.md` solves the fixed-cutoff
  Laguerre recurrence exactly:
  \(C_n(T)\) is \(C_8(T)\), \(\Delta_8(T)\), and a weighted cumulative sum
  of \(F_k(T)=M_k(T)+1+\frac34D_k^{\rm arch}\).  Termwise forcing positivity
  is not necessary; the exact target is the cumulative inequality plus
  moving-cutoff transfer.
- `184_MOVING_DIAGONAL_RECURRENCE_DEFECT.md` writes the recurrence directly
  on the A0 diagonal \(C_n^\ast=C_n(T_n)\).  The diagonal forcing is
  \(F_n(T_n)\) plus the explicit transfer defect
  \(n\Phi_{n+1}(T_n,T_{n+1})-(n+1)\Phi_{n-1}(T_{n-1},T_n)\).  This is the
  exact local induction target for A1.
- `185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md` compresses that diagonal
  forcing into
  \[
    F_n^{\rm diag}=1+\frac34D_n^{\rm arch}
    +\int_0^\infty E(e^u)e^{-u}\mathcal K_n(u)\,du,
  \]
  where \(\mathcal K_n\) is an explicit piecewise Laguerre kernel.  The
  kernel is signed, so this is a normal form rather than a positivity proof.
- `186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md` inserts \(\mathcal K_k\) into
  the exact cumulative weights from `183`, giving a single compact kernel
  \(\mathcal H_n=\sum_{k=8}^{n-1}w_{n,k}\mathcal K_k\).  The resulting A1
  induction target is one finite signed inequality on \([0,T_n]\); the
  cumulative kernel is still oscillatory.
- `187_CUMULATIVE_DIAGONAL_BALANCE_FORM.md` integrates that cumulative
  pairing once.  The resulting target contains the cumulative balance
  \(B\), a raised piecewise Laguerre kernel and every signed cutoff jump;
  omitting those jumps is an invalid shortcut.
- `188_DIAGONAL_CUMULATIVE_COERCIVITY_AUDIT.md` proves the symmetric-envelope
  no-go for that pairing.  If \(|E(e^u)|\le R(u)\), then the best lower
  bound available from this information alone is
  \[
    -\int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
  \]
  Hence no hidden coercive gain comes from the cumulative weights; a proof
  must supply one-sided arithmetic information or prove this explicit
  absolute bound is already inside the base-archimedean budget.
- `189_GLOBAL_LOG_DERIVATIVE_TO_COMPACT_A1_AUDIT.md` gives the exact
  bridge audit between the global half-plane theorem and compact A1:
  \[
    C_n(T_n)=\lambda_n-R_n(T_n)-{1\over4}\lambda_n^{\rm arch}.
  \]
  Hence global Li positivity plus A0 gives only
  \(C_n(T_n)\ge-\frac12\lambda_n^{\rm arch}\).  Compact A1 still needs a
  one-sided tail theorem, the strong margin, or a direct signed-core proof.
- `190_DIAGONAL_BALANCE_FINITE_CERTIFICATE.md` expands the balance formula
  with jumps into the finite certificate
  \[
    \mathcal A_n+\Pi_n+
    \sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)\ge0.
  \]
  The coefficients are explicit but signed, so the remaining theorem is
  uniform positivity of that certificate.
- `191_ABSOLUTE_DIAGONAL_BUDGET_SCALE_AUDIT.md` gives the exact scale
  condition for the absolute route left by `188`.  For an envelope
  \(|E(e^u)|\le R(u)\), define
  \[
    W_n(R)=\int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
  \]
  The absolute route closes only if \(\mathcal B_n\ge W_n(R)\) uniformly.
  For relative PNT profiles \(R(u)=e^u\varepsilon(u)\), this becomes
  \(\mathcal B_n\ge\int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du\).
- `192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md` refines the
  global-to-compact bridge: the desired tail inequality
  \(R_n(T_n)\le\lambda_n-\frac14\lambda_n^{\rm arch}\) is equivalent to
  \(C_n(T_n)\ge0\).  Global Toeplitz/Schoenberg positivity gives
  \(\lambda_n\ge0\), but does not compare \(\mathcal L\) with the moving
  tail generators \(\mathcal R_{T_n}\).  A margin, tail--margin
  correlation, Loewner/Schur comparison, or direct compact proof is still
  required.
- `193_WEIGHTED_L1_KERNEL_CERTIFICATE.md` turns the absolute diagonal load
  \(W_n(R)\) into a finite sign-partition certificate over the zeros of the
  piecewise polynomial cumulative kernel \(\mathcal H_n\).  The remaining
  theorem is uniform domination of this weighted \(L^1\) load by
  \(\mathcal B_n\).
- `194_STRONG_MARGIN_GENERATOR_SECOND_PASS.md` writes the strong-margin
  generator
  \[
    \mathcal M_{\rm SM}=\mathcal L-\frac12\mathcal A.
  \]
  Its coefficient positivity is equivalent to
  \(\lambda_n\ge\frac12\lambda_n^{\rm arch}\).  Toeplitz/Schoenberg
  positivity gives only \(Q_n(1-z^n)\ge0\); compact A1 through A0 requires
  the quantitative margin \(Q_n(1-z^n)\ge\lambda_n^{\rm arch}\).
- `195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` formulates the needed tail
  comparison as a precise form/order theorem:
  \[
    \mathfrak Q^{\mathcal L}
    -{1\over4}\mathfrak Q^{\mathcal A}
    -\mathfrak Q^{\mathcal R,T_n}
    \succeq0
  \]
  on \(1-z^n\), or more strongly on a finite subspace containing it.  This
  is not implied by \(\mathfrak Q^{\mathcal L}\succeq0\); it is the missing
  comparative tail theorem.
- `196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md` consolidates the exact
  surviving closure theorems: direct compact core, absolute \(L^1\)
  domination, strong margin, one-sided tail, comparative Loewner--Schur
  order, or the global half-plane theorem.
- `197_CUMULATIVE_KERNEL_INTERVAL_FORM.md` writes the interval polynomials
  for \(\mathcal H_n\).  In particular,
  \(\mathcal H_n=-L_{n-1}^{(2)}\) on \((T_{n-1},T_n)\), so every absolute
  route must dominate the terminal Laguerre \(L^1\) load and also the
  earlier cumulative mixtures.
- `198_STRONG_MARGIN_SECOND_DIFFERENCE_AUDIT.md` translates the strong
  margin into the increment Toeplitz sequence:
  \[
    2\lambda_n=n g_0+2\sum_{m=1}^{n-1}(n-m)g_m.
  \]
  Hence strong margin requires
  \(n g_0+2\sum_{m=1}^{n-1}(n-m)g_m\ge\lambda_n^{\rm arch}\).  If
  \(g_m\) has a positive Herglotz measure \(\nu_g\), this is
  \(\int|1+\cdots+\zeta^{n-1}|^2d\nu_g\ge\lambda_n^{\rm arch}\).  Positivity
  alone gives only the nonnegative left side.
- `199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` refines the comparative
  Loewner route into a Schur/innovation theorem.  For
  \(p_n=1-z^n\), A1 follows if the comparative form is nonnegative on a
  chosen block \(U_n\) and
  \[
    \inf_{u\in U_n}
    \mathfrak Q^{\mathcal C,T_n}(p_n-u,p_n-u)\ge0.
  \]
  This must be proved before using the diagonal identity
  \(\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)=2C_n(T_n)\); otherwise the Schur
  complement argument is circular.
- `200_FEJER_MASS_STRONG_MARGIN_GATE.md` turns the strong margin into a
  quantitative Fejer-mass theorem.  A sufficient local condition is
  \[
    \nu_g(|\theta|\le1/n)\ge{\pi^2\over4}
    {\lambda_n^{\rm arch}\over n^2},
  \]
  while the exact condition remains
  \(n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}\).
- `202_FEJER_DENSITY_SCALE_GATE.md` audits the density scale in that Fejer
  theorem.  If \(d\nu_g=h\,dm\) with \(h\le M\), then
  \(n\int F_n\,d\nu_g\le Mn\), which is below the archimedean
  \(n\log n\) scale for large \(n\).  A successful Fejer route needs
  logarithmic or stronger concentration near \(\zeta=1\), an atom/singular
  component, or a different signed proof.
- `203_ATOM_AT_ONE_INCOMPATIBILITY_AUDIT.md` removes the atom-at-one
  shortcut from the actual Euler--Gamma normalization.  An atom
  \(\nu_g\{1\}=a_0>0\) would contribute \(\lambda_n^{\rm atom}=a_0n^2/2\)
  and a cubic pole \(a_0z/(1-z)^3\) in \(\mathcal L(z)\), incompatible
  with \(\mathcal L(z)=O((1-z)^{-2}\log(1/(1-z)))\) along \(z\to1^-\).
- `204_LOG_DENSITY_INCREMENT_GENERATOR_GATE.md` identifies the compatible
  boundary scale for the Fejer route:
  \[
    \mathcal G_+(z)=\lambda_1+{\xi'\over\xi}\!\left({1\over1-z}\right).
  \]
  Thus \(\mathcal G_+(r)=O(\log(1/(1-r)))\), matching logarithmic density
  near \(\zeta=1\).  The missing theorem is a positive lower logarithmic
  density or the exact Fejer lower bound.
- `205_FEJER_LOG_CONSTANT_AUDIT.md` fixes the constants in that route:
  \(\lambda_n^{\rm arch}\sim\frac12n\log n\), a density
  \(a\log(e/|\theta|)\) gives radial Abel coefficient \(a/2\) but Fejer
  coefficient \(a\).  Hence the ideal Euler--Gamma log-density model
  \(a=1\) would have enough leading constant; the obstacle is not constants
  but the still-open positive-measure and lower-Fejer theorem.
- `206_FEJER_ABEL_TAUBERIAN_GAP.md` records the remaining transfer gap:
  at \(\theta=2\pi k/n\), the Fejer kernel vanishes while the matching Abel
  kernel is still of size \(n\).  Hence Abel logarithmic growth cannot imply
  the Fejer margin without an anti-concentration, lower-density, or direct
  Fejer theorem.
- `207_A0_TERMINAL_CUTOFF_BRIDGE_AUDIT.md` checks whether the A0 cutoffs
  automatically pass the terminal Laguerre load from `201`.  For the PNT
  profile \(A\exp(-\eta(u))\), the cutoff \(T_{n-1}\) gives
  \[
    \mathcal T_n
    \le
    {n^2\over12(n-1)^2}B_{n-1}
    \log {1+T_n\over1+T_{n-1}},
  \]
  so terminal control still needs a cutoff-ratio theorem or one extra
  decay surplus; it does not close the absolute route automatically.
- `208_VK_CUTOFF_RATIO_TERMINAL_SCALE.md` proves the canonical VK
  cutoff-ratio scale:
  \[
    T_n={25\over9a^{5/3}}n^{5/3}(\log n)^2(1+o(1)),
    \qquad
    \log {1+T_n\over1+T_{n-1}}
    ={5\over3n}+{2\over n\log n}+o(1/n).
  \]
  Therefore the terminal load from `207` is only
  \((5/72)\log n+O(1)\) for canonical VK cutoffs.  This helps the terminal
  absolute route but still leaves \(\mathcal B_n\), finite checks and
  earlier mixed-interval loads open.
- `209_ARCHIMEDEAN_BUDGET_SIGN_AUDIT.md` removes another shortcut in the
  absolute route.  The recurrence forcing satisfies
  \[
    D_n^{\rm arch}=-{1\over2}\log n+O(1),
  \]
  so \(1+\frac34D_n^{\rm arch}\) is eventually negative.  Hence positivity
  of the weights \(w_{n,k}\) does not make \(\mathcal B_n\) a positive
  reserve; the full budget domination theorem remains open.
- `210_BASE_BUDGET_QUADRATIC_COEFFICIENT_GATE.md` isolates the exact
  large-\(n\) budget coefficient
  \[
    \Gamma_{\mathcal B}
    =
    {\Delta_8^\ast\over16}
    +{1\over2}\sum_{k=8}^{\infty}
    {1+\frac34D_k^{\rm arch}\over k(k+1)}
  \]
  and proves \(\mathcal B_n=\Gamma_{\mathcal B}n^2+O(n\log n)\).  Its sign
  decides whether the terminal \(O(\log n)\) VK load can be absorbed for
  large \(n\).
- `211_MIXED_INTERVAL_OFFDIAGONAL_LOAD_GATE.md` isolates the nonterminal
  part of Theorem B.  On each \((T_j,T_{j+1})\), the cumulative kernel
  contains
  \[
    u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)
  \]
  with degrees up to \(n-2\).  Thus A0 decay at \(T_j\) is not enough by
  itself; a separate mixed \(L^1\), off-diagonal Laguerre, or signed theorem
  is required.
- `212_BASE_BUDGET_TELESCOPING_REDUCTION.md` evaluates the infinite
  archimedean part of \(\Gamma_{\mathcal B}\) exactly:
  \[
    \Gamma_{\mathcal B}
    =
    {1+\Delta_8^\ast\over16}
    -{3\over64}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch}).
  \]
  Therefore \(\Gamma_{\mathcal B}>0\) is equivalent to
  \(\Delta_8^\ast>-0.7175270082\ldots\).  The remaining budget question is
  finite/base, not an infinite archimedean series.
- `213_GAMMA_B_COMPACT_BASE_IDENTITY.md` substitutes
  \(\Delta_8^\ast=C_8(T_8)-C_7(T_7)\) and obtains the sharper identity
  \[
    \Gamma_{\mathcal B}={I_7(T_7)-I_8(T_8)\over16}.
  \]
  Thus positive terminal budget is exactly the finite signed base
  comparison \(I_7(T_7)>I_8(T_8)\); the finite Li certificate does not
  automatically prove it because it is a compact cutoff comparison.
- `214_GAMMA_B_BASE_FINITE_CERTIFICATE.md` expands that comparison as a
  finite prime-power certificate.  For \(T_8\ge T_7\),
  \[
  \begin{aligned}
    16\Gamma_{\mathcal B}
    &=
    \sum_{m\le e^{T_7}}\Lambda(m)
    [\Phi_7(\log m,T_7)-\Phi_8(\log m,T_8)]\\
    &\quad
    -
    \sum_{e^{T_7}<m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
    -\Psi_7(T_7)+\Psi_8(T_8).
  \end{aligned}
  \]
  All \(\Phi,\Psi\) are elementary endpoint expressions, so the positive
  terminal-budget case is finite once \(T_7,T_8\) are fixed.
- `215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md` shows that this
  finite sign gate is absorbed by the usual base case if the auxiliary
  \(T_7\) is chosen small.  For
  \(0<T_7\le\min(\log2,1/130)\), \(I_7(T_7)>-1\); if
  \(C_8^\ast\ge0\), then \(I_8(T_8)<-29/4\), so
  \(\Gamma_{\mathcal B}>0\).  The remaining base issue is therefore the
  actual compact certificate \(C_8^\ast\ge0\).
- `216_BASE_C8_COMPACT_CERTIFICATE.md` expands that base issue as
  \[
    \Psi_8(T_8)
    -
    \sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
    \ge
    8-{3\over4}A_8.
  \]
  This is finite once \(T_8\) is fixed.  It also records the finite
  sufficient alternative \(\lambda_8\ge\frac12A_8\), since A0 then gives
  \(C_8^\ast\ge0\).
- `217_N8_BASE_MARGIN_CERTIFICATE.md` closes that finite alternative.  The
  extended rational verifier proves
  \[
    \lambda_8-{1\over2}\lambda_8^{\rm arch}
    >
    1.455305710633246144455217.
  \]
  Since A0 gives \(|R_8(T_8)|\le\frac14\lambda_8^{\rm arch}\), the identity
  \(C_8(T_8)=\lambda_8-\frac14\lambda_8^{\rm arch}-R_8(T_8)\) gives
  \(C_8^\ast>0\).  With `215`, this also gives \(\Gamma_{\mathcal B}>0\).
- `218_MIXED_A0_DEGREE_MISMATCH_AUDIT.md` shows that the crude mixed
  absolute estimate cannot be obtained by combining local A0 decay with the
  elementary Laguerre bound.  On \((T_j,T_{j+1})\), A0 gives
  \((1+u)^{-(j+1)}\), while \(L_{k-1}^{(2)}\) costs
  \((1+u)^{k-1}\), leaving \((1+u)^{k-j-2}\) for \(k>j\).
- `220_TERMINAL_EFFECTIVE_THRESHOLD_REDUCTION.md` closes the terminal
  asymptotic obstruction after `217`: under the small-\(T_7\)
  normalization, \(\Gamma_{\mathcal B}>25/64\), while canonical VK terminal
  load is \(O(\log n)\).  The remaining terminal task is the finite rational
  certificate \(\mathfrak D_n=\mathcal B_n-\Theta_n\ge0\) over the explicit
  threshold range.
- `219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md` closes the raw mixed
  off-diagonal kernel obstruction by telescoping the cumulative weights.
  It proves
  \[
    \mathcal H_n(u)=-L_{n-1}^{(2)}(u)\qquad(T_8<u<T_n),
  \]
  with only fixed degree-7 corrections on \((0,T_7)\) and \((T_7,T_8)\).
  The remaining absolute-route theorem is a weighted \(L^1\) domination for
  this collapsed single-Laguerre load.
- `221_SINGLE_LAGUERRE_BULK_L1_OBSTRUCTION.md` rules out that remaining
  absolute theorem for VK envelopes: the collapsed Laguerre bulk has
  exponential \(e^{u/2}\) absolute mass on \(u\asymp n\), while VK relative
  decay is subexponential, so the absolute load eventually exceeds the
  quadratic budget \(\mathcal B_n\).
- `222_SIGNED_BALANCE_TELESCOPED_CERTIFICATE.md` gives the corresponding
  signed target after the absolute route fails.  The integrated balance now
  has only two cutoff jumps, at \(T_7,T_8\), and the finite certificate is
  \[
    \mathcal A_n+\Pi_n^{\rm tel}
    +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m)\ge0.
  \]
- `223_SIGNED_BALANCE_B_ENVELOPE_NO_GO.md` proves that a symmetric
  envelope for \(B(U)\) cannot close that signed target: it reduces to an
  absolute \(L^1\) bound for \(L_{n-1}^{(3)}\), whose bulk growth again
  overwhelms VK-scale decay.
- `224_STRONG_MARGIN_RH_STRENGTH_AUDIT.md` records that the strong-margin
  theorem is not an elementary surplus estimate: together with the finite
  \(1\le n\le7\) certificate it implies the Li criterion, hence RH.
- `225_A1_POST_ABSOLUTE_ROUTE_DECISION_LEDGER.md` consolidates the decision
  after the absolute-route audits: symmetric VK-size estimates are
  discarded, and the active targets are the signed finite inequality of
  `222` or one of the RH-strength routes.
- `226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md` simplifies the
  signed target further: direct expansion of \(\psi(e^u)\) gives
  \[
    \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0,
  \]
  where \(\Omega_n(m)\) is an explicit endpoint expression in
  \(e^{-u}L_{n-1}^{(1)}\) plus fixed degree-7 corrections.
- `227_SMALL_T7_PRIME_BLOCK_ELIMINATION.md` uses
  \(0<T_7<\log2\) to show that the \(\log m<T_7\) prime-power block in
  `226` is empty.  The arithmetic sum has only a finite low block below
  \(T_8\) and the high oscillatory block above \(T_8\).
- `228_HIGH_BLOCK_LAGUERRE_CORRELATION_FORM.md` rewrites the high block as
  \[
    e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}
    -
    \sum_{e^{T_8}\le m\le e^{T_n}}
    {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
  \]
  The remaining theorem is a signed prime-power correlation estimate.
- `229_SMALL_T7_DIRECT_COEFFICIENT_REDUCTION.md` combines the direct
  coefficient reductions into a single moving arithmetic transform
  \[
    \sum_{m\le e^{T_n}}{\Lambda(m)\over m}
    L_{n-1}^{(1)}(\log m),
  \]
  plus fixed base-window constants below \(T_8\).
- `230_SINGLE_TRANSFORM_A1_FRONTIER.md` identifies the equivalent final
  compact A1 inequality as a one-transform bound for
  \(S_n(T_n)=\sum_{m\le e^{T_n}}\Lambda(m)m^{-1}
  L_{n-1}^{(1)}(\log m)\), with the continuous counterpart
  \(1-L_n^{(0)}(T_n)\).
- `231_HIGH_BLOCK_PARTIAL_SUMMATION_FORM.md` gives the equivalent
  weighted-discrepancy form of the high block:
  \[
    A_8(T_n)L_{n-1}^{(1)}(T_n)
    +\int_{T_8}^{T_n}A_8(u)L_{n-2}^{(2)}(u)\,du,
  \]
  isolating \(E_8^\sharp(u)=A_8(u)-(u-T_8)\).
- `232_WEIGHTED_MERTENS_ENVELOPE_NO_GO.md` shows that a symmetric bound for
  \(E_8^\sharp\) cannot close the partial-summation frontier: it again
  creates an absolute \(L^1\) load for \(L_{n-2}^{(2)}\), whose bulk beats
  VK-scale decay.
- `233_SINGLE_TRANSFORM_FIXED_CUTOFF_GENERATOR.md` packages
  \(S_n(T)\) into a fixed-\(T\) coefficient generator.  It is exact for a
  fixed cutoff, but A1 still requires positivity along the moving cutoffs
  \(T=T_n\).
- `235_MOVING_CUTOFF_DERIVATIVE_GATE.md` computes the exact cutoff
  derivative:
  \[
    C_n'(T)=-(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)
  \]
  between prime-power jumps, while the jumps cancel.  Thus fixed-cutoff
  positivity transfers only with a signed integral theorem.
- `236_SINGLE_TRANSFORM_ZERO_SIDE_MARGIN_AUDIT.md` records the exact
  zero-side margin requirement:
  \[
    C_n(T_n)=\lambda_n-{1\over4}\lambda_n^{\rm arch}-R_n(T_n).
  \]
  Li positivity alone gives \(\lambda_n\ge0\), while compact A1 still
  needs strong margin, a one-sided tail theorem, or equivalent compact
  margin data.
- `237_CUTOFF_TRANSFER_TAIL_EQUIVALENCE.md` shows that fixed-cutoff or
  infinite-cutoff transfer to \(T_n\) is precisely the one-sided tail/sign
  correlation problem.  There is no separate monotonicity principle unless
  one proves the sign of the Laguerre--Chebyshev transfer integral.
- `238_TAIL_MARGIN_COMPENSATION_FRONTIER.md` rewrites the compact target as
  \[
    C_n(T_n)=M_n+\delta_n,\qquad
    M_n=\lambda_n-\frac12A_n,\quad
    \delta_n=\frac14A_n-R_n(T_n)\ge0.
  \]
  Thus A1 requires exactly enough tail surplus \(\delta_n\) to cover any
  negative strong-margin excess \(M_n\).
- `239_MARGIN_TAIL_THRESHOLD_LADDER.md` gives the sharp quantitative
  tradeoff: if \(\lambda_n\ge\kappa_n A_n\) and
  \(R_n(T_n)\le\rho_nA_n\), then A1 is exactly
  \(\kappa_n-\rho_n\ge1/4\).  Li positivity alone would require
  \(R_n(T_n)\le-A_n/4\), while A0 requires strong margin.
- `240_DEFICIT_RATIO_TAIL_SURPLUS_GATE.md` rewrites the same condition as
  \(s_n\ge d_n\), where \(d_n=(-M_n)_+/A_n\) is the normalized
  strong-margin deficit and \(s_n=\delta_n/A_n\) is the normalized tail
  surplus.
- `241_TAIL_SURPLUS_GENERATOR_DIAGONAL_NO_GO.md` packages the surplus into
  \[
    \Delta_T={1\over4}\mathcal A-\mathcal R_T,
  \]
  and shows that isolated coefficient positivity of \(\Delta_{T_n}\) is
  insufficient.  The exact cutoff flow is
  \[
    {d\over dT}[z^n]\Delta_T
    =
    -E(e^T)e^{-T}L_{n-1}^{(2)}(T).
  \]
  The needed comparison is
  \([z^n]\Delta_{T_n}\ge-[z^n]\mathcal M\), where
  \(\mathcal M=\mathcal L-\frac12\mathcal A\).
- `242_LOEWNER_CONE_MARGIN_TAIL_DECOMPOSITION.md` decomposes the comparative
  form as
  \[
    \mathfrak Q^{\mathcal C,T}
    =
    \mathfrak Q^{\mathcal M}
    +
    \mathfrak Q^{\Delta,T},
  \]
  where \(\mathfrak Q^{\mathcal M}\) is the strong-margin form and
  \(\mathfrak Q^{\Delta,T}\) is the tail-surplus form.  On
  \(p_n=1-z^n\), this gives
  \[
    {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)
    =
    M_n+\delta_n
    =
    C_n(T_n).
  \]
  Therefore a Loewner proof checked only on \(\mathbb Cp_n\) is just A1;
  a non-circular proof must establish cone domination or Schur innovation
  on a larger canonical space.
- `243_LOEWNER_NEGATIVE_PART_COMPENSATION_REDUCTION.md` refines that target
  on a finite comparison space by writing
  \[
    \mathfrak Q^{\mathcal M}
    =
    \mathfrak Q^{\mathcal M}_+
    -
    \mathfrak Q^{\mathcal M}_-.
  \]
  A sufficient theorem is
  \[
    \mathfrak Q^{\Delta,T_n}
    -
    \mathfrak Q^{\mathcal M}_-
    \succeq0,
  \]
  which reduces on \(p_n\) to the same sharp condition
  \(\delta_n\ge-M_n\).
- `244_A0_TAIL_IMPROVEMENT_REQUIREMENT.md` records the exact normalized
  upgrade from A0 to A1.  If
  \[
    \eta_n=\frac14-{R_n(T_n)\over A_n},
    \qquad
    d_n=\max\left(0,\frac12-{\lambda_n\over A_n}\right),
  \]
  then A0 gives only \(\eta_n\ge0\), while compact A1 is exactly
  \[
    \eta_n\ge d_n.
  \]
  In signed-tail form this is
  \[
    \int_{T_n}^{\infty}
      E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
    \ge
    \left(d_n-\frac14\right)A_n.
  \]
- `245_TERMINAL_THRESHOLD_DATA_DEPENDENCE_CERTIFICATE.md` records that the
  terminal asymptotic sign is closed, but an executable \(N_0\) requires
  six fixed data items: cutoff policy, cutoff-ratio bounds, \(B_{n-1}\)
  bounds, base intervals, finite archimedean summand intervals, and the
  finite interval check of \(\mathfrak D_n\ge0\).  This is subordinate to
  A1 and does not address the signed/comparative compact obstruction.
- `246_GLOBAL_HALF_PLANE_COMPACT_A1_SEPARATION.md` separates the global
  RH-strength route from the compact A1 obligation.  The half-plane theorem
  would give \(\lambda_n\ge0\), hence \(d_n\le1/2\), while A0 gives
  \(s_n\ge0\).  Compact A1 still requires \(s_n\ge d_n\).  Thus a global
  proof can close Omega7 externally, but compact A1 still needs the
  margin-tail bridge unless A1 is bypassed by that global closure route.
- `247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md` records the sufficient
  special point
  \[
    \lambda_n\ge {1\over4}A_n,\qquad R_n(T_n)\le0.
  \]
  In normalized coordinates this is \(d_n\le1/4\) and \(s_n\ge1/4\), hence
  \(s_n\ge d_n\).  The route is weaker than strong margin but still
  RH-strength, and the nonpositive tail is a genuinely signed condition not
  supplied by A0.
- `248_QUARTER_MARGIN_GENERATOR_RH_STRENGTH_AUDIT.md` defines
  \[
    \mathcal Q_{1/4}=\mathcal L-{1\over4}\mathcal A
  \]
  with coefficients \(\lambda_n-\frac14A_n\).  Its Euler--Gamma form is
  \[
    {3\over4}\mathcal A
    -{z\over(1-z)^2}
    -{z\over(1-z)^3}\int_0^\infty
      E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
  \]
  Positivity of these coefficients for \(n\ge8\), together with the finite
  low-index certificate, already implies Li positivity and RH.
- `249_TAIL_SIGN_LAGUERRE_ZERO_PARTITION_GATE.md` writes the nonpositive-tail
  condition \(R_n(T_n)\le0\) as the signed lobe theorem
  \[
    \sum_j\sigma_{n,j}\mathcal E_{n,j}\ge0
  \]
  over the zeros of \(L_{n-1}^{(2)}\) beyond \(T_n\), including the final
  infinite ray.  A0 supplies only the weaker bound
  \(\sum_j\sigma_{n,j}\mathcal E_{n,j}\ge-A_n/4\).
- `250_NONPOSITIVE_TAIL_SYMMETRIC_ENVELOPE_NO_GO.md` proves that the
  nonpositive-tail sign cannot be obtained from any symmetric envelope
  \(|E(e^u)|\le W(u)\) alone.  The functional
  \[
    \int_{T_n}^{\infty}E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \]
  is odd under \(E\mapsto-E\), while the envelope is invariant, so a
  one-sided sign needs genuinely signed arithmetic information.
- `251_RDI_LI_COEFFICIENT_EXTRACTION_GATE.md` fixes the exact coefficient
  bridge required for RDI to imply Li.  The acceptable direct theorem is
  local uniform convergence near \(z=0\) of
  \[
    zF_N'(z)
    \to
    {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
  \]
  with nonnegative approximating coefficients, so Cauchy's formula passes
  to \(\lambda_n\).  The alternative is locally uniform real-rooted
  convergence to the true \(\Xi\).  Both are RH-strength bridges.
- `310_REAL_RAY_CONVERGENCE_NOT_LI_COEFFICIENT_NO_GO.md` gives the explicit
  failure mode behind the local-uniform requirement.  The functions
  \[
    F_N(z)={z\over1+N^2z^2}
  \]
  converge pointwise to \(0\) on the real axis, but \([z]F_N=1\) for all
  \(N\).  Their poles collapse to \(0\), so no complex local uniform
  convergence is available.  Therefore real-ray RDI convergence cannot
  imply Li coefficient convergence.
- `252_SCHUR_ZERO_COUPLING_DIAGONAL_COLLAPSE.md` records the degenerate
  Schur case \(b_n=0\).  Then the Schur innovation is
  \[
    d_n=2C_n(T_n),
  \]
  so proving nonnegative innovation is exactly proving A1.  Zero coupling
  does not create a separate Loewner margin.
- `253_DISK_HERGLOTZ_MEASURE_HALF_PLANE_GATE.md` rewrites the global
  semiplane theorem as
  \[
    H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right)
    =
    \int_{\partial\mathbb D}{\zeta+z\over\zeta-z}\,d\nu_\xi(\zeta)
  \]
  for a positive finite boundary measure.  Such a measure implies
  holomorphy in the disk and therefore excludes off-line zeros.  The
  measure must be constructed before using zero support; defining it from
  critical-line zeros is circular.
- `290_RADIAL_ABEL_POSITIVITY_NOT_HERGLOTZ_NO_GO.md` eliminates the radial
  Abel shortcut.  A function can satisfy \(H(r)>0\) for every \(0<r<1\)
  and still fail \(\Re H(z)\ge0\) in the disk; for example
  \(H(z)=1+3z^2\) is positive on the positive radius but has negative real
  part on the imaginary radius and a non-positive Toeplitz block.  Thus the
  global measure route needs angular Herglotz/Toeplitz positivity, not just
  radial logarithmic growth.
- `300_CENTERED_FEJER_TESTS_NOT_TOEPLITZ_NO_GO.md` eliminates the centered
  Fejer shortcut.  The sequence \(g_0=1\), \(g_1=0\), \(g_2=3/2\),
  \(g_m=0\) for \(m\ge3\), has all centered Fejer sums positive:
  \[
    \mathcal F_1=1,\quad \mathcal F_2=1,\quad
    \mathcal F_n=4-6/n>0\quad(n\ge3),
  \]
  but its \(3\times3\) Toeplitz block is negative on \((1,0,-1)\).
  Therefore Li/Fejer diagonal positivity is not a Herglotz-measure
  construction; full translated Fejer/Toeplitz positivity is still needed.
- `324_FINITE_TOEPLITZ_BLOCKS_NOT_HERGLOTZ_GATE.md` eliminates finite
  Toeplitz checking as a global shortcut.  For any fixed \(N\), the sequence
  \(g_0=1\), \(g_{\pm(N+1)}=M>1\), and all other nonzero modes absent has
  \(T_L=I_{L+1}\) for every \(L\le N\), but \(T_{N+1}\) is negative on
  \(e_0-e_{N+1}\).  Hence the Herglotz route needs positivity for every
  block, a positive boundary measure, or a valid limiting theorem with
  coefficient convergence.
- `254_TAIL_SIGN_EXPLICIT_FORMULA_PHASE_GATE.md` rewrites the signed tail
  functional as
  \[
    I_n(T)
    =
    -2\Re\sum_{\Im\rho>0}{\Phi_{n,T}(\rho)\over\rho}
    -\mathcal T_{n,T},
  \]
  where \(\Phi_{n,T}\) is an incomplete Laguerre transform.  The
  nonpositive-tail route is therefore the one-sided phase inequality
  \[
    2\Re\sum_{\Im\rho>0}{\Phi_{n,T_n}(\rho)\over\rho}
    \le -\mathcal T_{n,T_n}.
  \]
- `255_TAIL_MARGIN_CORRELATION_SLACK_FORM.md` introduces a separate slack
  \(h_n\) by
  \[
    R_n(T_n)\le {1\over4}A_n-h_n.
  \]
  Compact A1 follows exactly when
  \[
    h_n\ge(-M_n)_+.
  \]
  In normalized variables this is \(s_n\ge d_n\), so the slack formulation
  is a clean bookkeeping version of the main margin-tail bridge.
- `275_PHASE_COMPLETION_CRITERION_A1_AND_GLOBAL.md` records the phase-level
  completion criterion.  External routes such as global half-plane
  positivity, disk Herglotz positivity, or the RDI bridges close Omega7
  through RH/Li, but they do not by themselves prove compact A1.  Since A1
  is explicitly part of the requested goal, completion requires either a
  direct compact A1 proof or one of the equivalent margin-tail, strong
  margin, signed-tail, or Loewner/Schur conditions.
- `276_LOEWNER_SUBSPACE_COFINALITY_GATE.md` records the cofinality condition
  for comparative Loewner tests.  Positivity on a family of test vectors
  implies the A1 diagonal only if
  \[
    p_np_n^*\in
    \overline{\operatorname{cone}}\{v_\alpha v_\alpha^*\},
    \qquad p_n=1-z^n,
  \]
  or if the tested subspace directly contains \(p_n\).  Otherwise finite
  separation gives Hermitian forms positive on all tested directions but
  negative on \(p_n\).
- `277_FINITE_CERTIFICATE_EFFECTIVE_THRESHOLD_GATE.md` records the
  effective-threshold rule for finite arithmetic certificates.  A pointwise
  certificate from `148`, `190`, `230`, or the finite remainder form `261`
  proves A1 only on its checked indices unless it is paired with a uniform
  theorem for all \(n\ge8\), or with an explicit threshold \(N_\infty\)
  and rigorous verification of every \(8\le n<N_\infty\).
- `278_COFINAL_SUBSEQUENCE_CERTIFICATE_NO_GO.md` extends the same rule to
  infinite subsequential checks.  Positivity on a cofinal, density-one, or
  otherwise natural subset does not imply the missing coordinates of A1;
  every omitted index must be covered by propagation, positive
  reconstruction, or an effective-threshold theorem.
- `256_POINTWISE_DUAL_CONE_AND_AVERAGE_GATE.md` records the dual form of
  compact A1.  Pointwise positivity of \(C_n(T_n)\) is equivalent to
  nonnegativity of every finitely supported nonnegative average
  \[
    \sum_{n\ge8}\mu_nC_n(T_n)\ge0.
  \]
  Therefore a smoothed route closes A1 only if it positively reconstructs
  each coordinate mass, or if it supplies an independent
  coefficient-extraction theorem.  Bare Abel, Laplace, Fejer, heat, or
  averaged positivity is not a coefficientwise proof.
- `257_AVERAGED_SLACK_POINTWISE_NO_GO.md` applies the same pointwise rule to
  tail--margin slack.  An averaged, cofinal, density-one, or asymptotic
  lower bound for \(h_n-(-M_n)_+\) does not prove compact A1 unless it is
  converted into
  \[
    h_n\ge(-M_n)_+
  \]
  for every \(n\ge8\), or into an effective large-\(n\) theorem plus a
  finite exceptional-index certificate.
- `258_CRITICAL_LINE_SUPPORT_TAIL_PHASE_NO_GO.md` records the corresponding
  zero-side separation for the explicit-formula tail phase.  Even after
  restricting a positive model measure to the critical line, the functional
  \[
    2\Re\int_{\gamma>0}
    {\Phi_{n,T_n}(1/2+i\gamma)\over1/2+i\gamma}\,d\mu(\gamma)
  \]
  is an oriented weighted moment.  Support on the line gives the domain of
  integration, but not the required one-sided bound; compact A1 still needs
  a genuine tail-phase theorem or the equivalent gate \(s_n\ge d_n\).
- `274_TAIL_PHASE_LOBE_DUALITY_GATE.md` records that the lobe partition of
  `249` and the explicit-formula phase inequality of `254` are the same
  signed functional.  If \(\Phi_{n,j}\) denotes the transform of one
  absolute Laguerre lobe, then
  \[
    \Phi_{n,T}(\rho)=\sum_j\sigma_{n,j}\Phi_{n,j}(\rho),
  \]
  and summing the lobe explicit formula gives exactly the phase inequality.
  Thus unsigned lobe bounds and zero-modulus bounds cannot produce the
  one-sided tail sign; a signed correlation/phase theorem is still needed.
- `280_TAIL_PHASE_LOBE_BALANCE_GATE.md` gives the signed positive/negative
  phase decomposition.  With
  \(q_{n,T}=\Re(\Phi_{n,T}(1/2+i\gamma)/(1/2+i\gamma))=q^+-q^-\), define
  \(P^\pm_{n,T}=\int q^\pm\,d\mu_\zeta\).  Then
  \[
    I_n(T)=2(P^-_{n,T}-P^+_{n,T})-\mathcal T_{n,T}.
  \]
  Thus the full deficit-compensating tail gate is exactly
  \[
    P^-_{n,T_n}-P^+_{n,T_n}
    \ge {1\over2}\left(\mathcal T_{n,T_n}
    +(d_n-1/4)A_n\right).
  \]
  This is the precise signed lobe-balance theorem still missing.
- `259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` turns the Fejer/log-density
  audits into a conditional strong-margin closure theorem.  If a positive
  increment measure \(\nu_g\) exists and either
  \[
    \int F_n\,d\nu_g\ge\left({1\over2}+\eta\right)\log n-B_F
  \]
  or a logarithmic boundary density lower bound with coefficient
  \(a>1/2\) is proved with explicit constants, then
  \(\lambda_n\ge A_n/2\) for all sufficiently large \(n\), and the remaining
  finite interval can be checked directly.  The construction of such a
  positive measure and lower-density theorem remains open.
- `260_EXACT_FEJER_LOG_KERNEL_CONSTANT.md` closes the analytic constant in
  the log-density alternative.  It proves
  \[
    \int_{\partial\mathbb D}F_nL\,dm
    =
    H_{n-1}-{n-1\over n}
    \ge \log n-1,
  \]
  so `259` may use \(B_L=1\) and \(N_L=1\).  The remaining Fejer route
  obstruction is therefore the positive increment measure and the actual
  lower log-density theorem, not the kernel constant.
- `261_FEJER_FINITE_REMAINDER_CERTIFICATE_SCHEMA.md` closes the bookkeeping
  for the finite interval left by the Fejer threshold.  Once `264` supplies
  \(N_\infty\), every \(8\le n<N_\infty\) must be certified pointwise by
  rigorous intervals proving either
  \[
    \lambda_n^- - {1\over2}A_n^+\ge0
  \]
  or directly
  \[
    C_n(T_n)^-\ge0.
  \]
  This is the exact finite remainder; averaged or asymptotic information
  cannot replace it by `256` and `257`.
- `262_EXPLICIT_ARCHIMEDEAN_UPPER_FEJER_INPUT.md` closes the archimedean
  upper input in the same threshold calculation:
  \[
    \lambda_n^{arch}\le {1\over2}n\log n+3n
    \qquad(n\ge2).
  \]
  Thus `259` may take \(B_A=3\) and \(N_A=2\).
- `263_LOCAL_LOG_DENSITY_TO_GLOBAL_FEJER_PATCH.md` closes the
  local-to-global bookkeeping gap in that route.  If
  \(h(\theta)\ge aL(\theta)-B_h\) holds on \(|\theta|\le\theta_0\),
  \(h\ge0\) globally, and the remainder measure is positive, then the same
  Fejer lower bound holds globally with
  \[
    B_h^\ast=\max\{B_h,\ a(-\log(2\sin(\theta_0/2)))_+\}.
  \]
  Thus local logarithmic density coefficient \(a>1/2\) is enough once the
  positive measure decomposition exists.
- `264_FEJER_ROUTE_EXPLICIT_THRESHOLD_LEDGER.md` combines these constants.
  With
  \[
    B_h^\ast=\max\{B_h,\ a(-\log(2\sin(\theta_0/2)))_+\},
  \]
  the Fejer strong-margin route holds for
  \[
    n\ge
    \max\left(
      2,
      \left\lceil
      \exp\left({3+a+B_h^\ast\over a-1/2}\right)
      \right\rceil
    \right),
  \]
  assuming the positive increment measure and local lower-density theorem.
  Compact A1 is then reduced to the finite interval below that threshold.
- `265_FEJER_LOG_DENSITY_ABEL_COEFFICIENT_BUDGET.md` adds the opposite
  coefficient constraint from the actual generator.  Since
  \[
    \mathcal G_+(r)
    =
    \lambda_1+{\xi'\over\xi}\!\left({1\over1-r}\right)
    =
    {1\over2}\log {1\over1-r}+O(1),
  \]
  a positive local density lower bound \(h\ge aL-B_h\) would force
  \(a\le1\).  The Fejer route is therefore narrowed to the sharp possible
  window \(1/2<a\le1\).
- `266_ABEL_TO_FEJER_DEFECT_GATE.md` records the exact quantitative loss in
  any route that tries to transfer Abel/Poisson logarithmic mass into Fejer
  mass.  With
  \[
    D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+,
  \]
  one has
  \[
    \int F_n\,d\nu
    \ge {1\over\alpha}
    \left(
      \int P_{1-1/n}\,d\nu-\int D_{n,\alpha}\,d\nu
    \right).
  \]
  For the Euler--Gamma normalization \(\int P_{1-1/n}\,d\nu_g=\log n+O(1)\);
  with \(\alpha=1\), a defect coefficient \(d<1/2\) would be enough to
  re-enter the Fejer closure theorem.  This is an anti-concentration gate,
  not a proof.
- `291_ABEL_DEFECT_CONSTANT_THRESHOLD_LEDGER.md` makes the same route
  constant-executable.  If
  \[
    \int(P_{1-1/n}-\alpha F_n)_+\,d\nu_g
    \le d_\alpha\log n+B_D,
    \qquad d_\alpha<1-\alpha/2,
  \]
  together with an effective Abel lower bound
  \(\int P_{1-1/n}\,d\nu_g\ge\log n-B_P\), then the Fejer lower coefficient
  is \(q_\alpha=(1-d_\alpha)/\alpha>1/2\).  Using the archimedean upper
  input of `262`, strong margin follows above the explicit threshold
  \[
    N_\infty(\alpha)=
    \max\left(N_0,2,\left\lceil
    \exp\left({3+B_\alpha\over q_\alpha-1/2}\right)\right\rceil\right),
  \]
  and `261` supplies the finite-remainder format below that threshold.
- `292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md` turns the
  defect estimate into a geometric distribution problem.  For
  \[
    B_{n,\tau}=\{F_n<\tau P_{1-1/n}\},
  \]
  the pointwise bound
  \[
    D_{n,\alpha}
    \le
    P_n{\bf1}_{B_{n,\tau}}
    +(1-\alpha\tau)_+P_n{\bf1}_{B_{n,\tau}^c}
  \]
  shows that it is enough to prove
  \[
    \int_{B_{n,\tau}}P_n\,d\nu_g\le b_\tau\log n+B_B
  \]
  with \(b_\tau+(1-\alpha\tau)_+<1-\alpha/2\), assuming the two-sided Abel
  scale of the actual increment measure.  This isolates the arithmetic
  anti-concentration needed near the moving Fejer-zero bad sets.
- `293_FEJER_POISSON_BAD_SET_GEOMETRY_GATE.md` computes the deterministic
  geometry behind those bad sets.  For \(0<\tau\le1\), \(B_{n,\tau}\)
  contains windows of radius \(\sqrt{\tau}/(2n)\) around every nontrivial
  \(n\)-th root of unity.  Hence the missing bound in `292` cannot be
  replaced by bare geometric smallness; it must use arithmetic distribution
  of the actual increment measure.
- `311_BAD_SET_CARLESON_WINDOW_SUFFICIENT_CONDITION.md` records the
  complementary sufficient window condition.  A root-window estimate
  \[
    \nu_g(I_{n,k}(\tau))
    \le { \rho_\tau\log n+B_\tau\over n}
  \]
  implies
  \[
    \int_{B_{n,\tau}}P_n\,d\nu_g
    \le C_\tau'(\rho_\tau\log n+B_\tau).
  \]
  Optimizing the `292` constants reduces this local-window route to
  \(C_\tau'\rho_\tau<1-1/(2\tau)\) for some \(\tau>1/2\).
- `296_WEIGHTED_CARLESON_BAD_SET_GATE.md` refines that sufficient
  condition to the natural Poisson-weighted window sum
  \[
    \sum_{k=0}^{n-1}
    {n\,\nu_g(I_{n,k}(\tau))\over1+\kappa(k)^2}
    \le \beta_\tau\log n+B_\tau.
  \]
  This still implies the bad-set estimate of `292`, with coefficient
  \(b_\tau=C_\tau\beta_\tau\), but does not require uniform unweighted
  control of windows far from \(\zeta=1\).
- `297_CENTRAL_FLOOR_WEIGHTED_BUDGET_GATE.md` combines the weighted upper
  condition with the central lower floor.  If the local logarithmic density
  coefficient is \(a\), then any Abel bad-set proof at a fixed \(\tau\)
  must satisfy
  \[
    aK(\tau)\le C_\tau\beta_\tau<1-{1\over2\tau}.
  \]
  If the left floor already exceeds the right target, that \(\tau\) cannot
  close the Abel-defect route.
- `316_CENTRAL_FLOOR_COMPATIBILITY_WINDOW.md` proves that this two-sided
  budget is not automatically empty in the live range \(a\le1\).  The bound
  \(R(u)<3/2\) on \(|u|\le3/2\) shows the central window is nonempty at
  \(\tau=3/2\), while \(R(17/10)>3/2\) forces
  \[
    K(3/2)\le {2\over\pi}\arctan(17/10)<{2\over3}.
  \]
  Hence \(aK(3/2)<1-1/(2(3/2))\) for every \(a\le1\): the central floor is
  a real budget cost, not a standalone contradiction.
- `314_BAD_SET_CENTRAL_WINDOW_LOG_MASS_FLOOR.md` records the necessary
  central cost created by the same condition \(\tau>1/2\).  Since
  \(F_n(1)/P_{1-1/n}(1)\to1/2\), the bad set contains a central
  \(1/n\)-window.  If \(h\ge aL-B\) locally, then
  \[
    \liminf_{n\to\infty}{1\over\log n}
    \int_{B_{n,\tau}}P_n\,d\nu
    \ge a\,{2\over\pi}\arctan c_\tau
  \]
  for any \(c_\tau\) with the central scaling ratio \(R(u)<\tau\) on
  \(|u|\le c_\tau\).  Thus the bad-set coefficient has a required floor as
  well as the `292` upper target.
- `294_LOCAL_DENSITY_NOT_BAD_SET_ANTI_CONCENTRATION_NO_GO.md` separates the
  local-density closure input from the Abel-defect anti-concentration
  input.  Adding sparse positive spikes at moving Fejer zeros preserves a
  local logarithmic lower-density bound near \(1\), but can force
  arbitrarily large Poisson-weighted bad-set coefficients along a
  subsequence.  Thus `292` needs independent arithmetic distribution
  information.
- `295_BOUNDED_DENSITY_BAD_SET_ZERO_COEFFICIENT_GATE.md` identifies a
  harmless component for the same route.  If \(d\nu=h\,dm\) with
  \(0\le h\le H\), then
  \[
    \int_{B_{n,\tau}}P_{1-1/n}\,d\nu\le H
  \]
  for every \(n,\tau\).  Hence bounded absolutely continuous mass has zero
  logarithmic bad-set coefficient, and the obstruction is confined to the
  singular or unbounded-density remainder.
- `312_LOG_KERNEL_ABEL_DEFECT_MODEL_LEDGER.md` calibrates the opposite
  model case.  For the canonical logarithmic density
  \(L=-\log|2\sin(\theta/2)|\),
  \[
    \int(P_{1-1/n}-\alpha F_n)_+L\,dm
    =
    \kappa_\alpha\log n+o_\alpha(\log n),
  \]
  where
  \[
    \kappa_\alpha={1\over2\pi}\int_{\mathbb R}
    \left({2\over1+u^2}
      -\alpha\left({2\sin(u/2)\over u}\right)^2\right)_+du .
  \]
  Therefore the pure log-kernel defect is explicit; the remaining Abel
  route must control any additional Euler--Gamma remnant near moving
  Fejer zeros.
- `315_LOG_KERNEL_DEFECT_OPTIMIZATION_LEDGER.md` compares this model
  coefficient with the Abel-defect budget \(1-\alpha/2\).  The pure
  log-kernel model has positive leading margin; on a coarse grid,
  \[
    \alpha={3\over4},\qquad
    \kappa_\alpha\approx0.3520355633,\qquad
    1-{\alpha\over2}-\kappa_\alpha\approx0.2729644367.
  \]
  Thus the remaining quantitative obstruction is the residual bad-set mass,
  not the canonical logarithmic component itself.
- `325_EG_REMAINDER_BAD_SET_CERTIFICATE_SCHEMA.md` packages the remaining
  Abel--Fejer route as an effective certificate.  Given
  \(d\nu_g=aL\,dm+d\rho\) and the full Abel lower bound, one must certify
  \[
    \int D_{n,\alpha}L\,dm\le\kappa_\alpha^+\log n+B_L
  \]
  and either a direct remnant defect bound
  \(\int D_{n,\alpha}\,d\rho\le e_\alpha\log n+B_\rho\), or a weighted
  bad-set/Poisson bound implying such an \(e_\alpha\).  The closure
  condition is
  \[
    a\kappa_\alpha^+ + e_\alpha<1-\alpha/2.
  \]
  Then `291` gives an explicit \(N_\infty(\alpha)\), and `261` gives the
  finite remainder format.
- `328_POISSON_LOWER_NOT_LOG_DOMINATION_NO_GO.md` separates Abel lower
  growth from log-kernel domination.  The point mass \(\delta_1\) has
  \(\int P_{1-1/n}\,d\delta_1=2n-1\ge\log n\), but it cannot dominate
  \(aL\,dm\) on any arc away from \(1\) where \(L>0\).  Hence the
  decomposition \(d\nu_g=aL\,dm+d\rho\), \(\rho\ge0\), must be proved as a
  separate measure-order theorem or replaced by a direct full-defect bound.
- `313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md` records the direct-route
  termwise audit.  In the high prime-power block,
  \[
    \Omega_n(m)=
    e^{-T_n}L_{n-1}^{(1)}(T_n)
    -
    e^{-\log m}L_{n-1}^{(1)}(\log m).
  \]
  Since \(e^{-u}L_{n-1}^{(1)}(u)\) has alternating Laguerre lobes, these
  coefficients are not of one sign.  Direct A1 must therefore prove a
  signed global compensation theorem, not coefficientwise positivity.
- `298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md` turns that compensation
  into the exact lobe-block criterion.  After partitioning
  \([T_8,T_n]\) by the sign of
  \(G_{n-1}(T_n)-G_{n-1}(u)\), the high block splits into
  \(H_n^+-H_n^-\), and the direct certificate is exactly
  \[
    H_n^+-H_n^-+B_n^{\rm base}\ge0.
  \]
  Therefore absolute lobe-load estimates are insufficient unless they are
  supplemented by oriented dominance.
- `299_LOBE_BLOCK_PARTIAL_SUMMATION_GATE.md` applies exact partial
  summation on each direct lobe block.  With
  \(\mathcal E_a(u)=\psi(e^u)-e^u-(\psi(e^a-)-e^a)\), the arithmetic
  contribution on each block becomes a boundary term plus
  \[
    -\int_a^b\mathcal E_a(u)e^{-u}L_{n-1}^{(2)}(u)\,du.
  \]
  Thus the remaining direct theorem is an oriented Chebyshev-error
  inequality over the Laguerre lobes, not an absolute envelope.
- `329_DIRECT_A1_ORIENTED_CHEBYSHEV_MINIMAL_THEOREM.md` sharpens the direct
  target to the exact remaining theorem
  \[
    \sum_jH_{n,j}^{\rm err}
    \ge
    -B_n^{\rm base}-\sum_jH_{n,j}^{\rm main}.
  \]
  It also records the monotonicity no-go: positivity of \(\Lambda\) and
  monotonicity of \(\psi\) do not control placement of prime-power mass
  among positive and negative Laguerre lobes.  The missing input is
  oriented arithmetic placement, not unsigned mass.
- `320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` gives the analogous
  tail-side sufficient theorem.  If \(E(e^u)=\psi(e^u)-e^u\) has lower
  envelopes on the positive lobes of \(K_n=e^{-u}L_{n-1}^{(2)}\) and upper
  envelopes on the negative lobes, then the oriented envelope lower bound
  \(\mathcal L_n\) certifies compact A1 at \(n\) whenever
  \[
    \mathcal L_n\ge\left(d_n-\frac14\right)A_n.
  \]
  Symmetric envelopes reduce to the absolute worst-case bound and therefore
  to the already discarded absolute route.
- `322_TAIL_LOBE_INTERVAL_CERTIFICATE_SCHEMA.md` converts that sufficient
  theorem into a rigorous pointwise certificate format.  For each \(n\) it
  requires isolated tail zeros of \(L_{n-1}^{(2)}\), interval enclosures for
  lobe weights, oriented one-sided Chebyshev-error bounds on each lobe, and
  an interval-safe comparison with \((d_n-1/4)A_n\).  Infinite closure still
  needs either all indices or an effective threshold plus finite remainder.
- `326_TAIL_LOBE_STEP_ENVELOPE_EFFECTIVE_REDUCTION.md` strengthens the
  effective part of that format.  On any bounded tail lobe,
  \(\psi(e^u)-e^u\) decreases between prime-power logarithms and jumps
  upward by \(\Lambda(m)\).  Hence the lower and upper constants required
  by `320` are exactly finite endpoint extrema over the prime powers in
  the lobe.  The remaining non-finite input is the final-ray one-sided
  weighted theorem, together with all-index or effective-threshold
  coverage.
- `327_FINAL_RAY_ABSOLUTE_COST_GATE.md` records a safe hybrid use of
  symmetric PNT/VK envelopes.  They may be applied only on the final ray as
  the explicit negative cost
  \[
    \mathcal R_{n,\infty}(W)=
    \int_{\xi_{n,*}}^\infty W(u)e^{-u}|L_{n-1}^{(2)}(u)|\,du,
  \]
  after the bounded lobes have been handled by oriented arithmetic.  This
  does not revive the global symmetric-envelope route; it is a pointwise
  final-ray cost that must be absorbed by the bounded-lobe surplus.
- `321_DIRECT_TAIL_LOBE_TRANSFER_GATE.md` records the transfer rule between
  the compact direct lobe system and the tail lobe system.  Although
  \(\omega_n'(u)=e^{-u}L_{n-1}^{(2)}(u)\), this derivative relation changes
  sign and produces boundary terms; it is not a positive map from direct
  lobe dominance to tail lobe dominance.  The two forms are equivalent only
  after the full identity \(C_n(T_n)=\lambda_n-A_n/4-R_n(T_n)\) is assembled,
  so using one to prove the other without an independent signed theorem is
  circular.
- `270_POISSON_TO_FEJER_POSITIVE_INVERSE_NO_GO.md` proves that radial Abel
  lower bounds cannot be positively inverted into Fejer lower bounds.  For
  \(N\ge2\), \(F_N\) vanishes at nontrivial \(N\)-th roots of unity, while
  every radial Poisson kernel \(P_r\) is strictly positive there.  Hence no
  nonzero positive combination or positive integral of \(P_r\)'s can be
  pointwise dominated by \(F_N\).  The Fejer route therefore needs a direct
  Fejer lower bound, a local density theorem, or anti-concentration against
  the moving Fejer zeros.
- `271_POSITIVE_INCREMENT_FEJER_MASS_SEPARATION.md` closes the remaining
  logical shortcut in the Fejer route.  A positive increment measure gives
  \[
    2\lambda_n=n\int F_n\,d\nu_g
  \]
  and hence global Li positivity, but compact A1 needs the stronger
  quantitative condition
  \[
    \int F_n\,d\nu_g\ge {A_n\over n}.
  \]
  Positivity, finite total mass, and support away from \(\zeta=1\) cannot
  supply that \(O(\log n)\) Fejer mass.  The remaining compact route is
  exactly a lower log-density theorem with \(1/2<a\le1\), or an equivalent
  direct Fejer lower bound, plus finite verification.
- `272_FEJER_MASS_LOCALIZATION_NECESSARY_GATE.md` gives a necessary
  localization shadow of the Fejer lower theorem.  From
  \[
    F_n(e^{i\theta})\le \min\left(n,{\pi^2\over n\theta^2}\right),
  \]
  any bound \(\int F_n\,d\nu_g\ge\frac12\log n-O(1)\) forces
  \[
    n\nu_g(|\theta|\le1/n)
    +{\pi^2\over n}\int_{|\theta|>1/n}{d\nu_g\over\theta^2}
    \ge {1\over2}\log n-O(1).
  \]
  Thus the required Fejer mass must be localized near \(\zeta=1\) in a
  logarithmic sense.
- `273_FEJER_LAYER_CAKE_DISTRIBUTION_GATE.md` gives the exact distribution
  form of that Fejer mass theorem:
  \[
    \int_{\partial\mathbb D}F_n\,d\nu_g
    =
    \int_0^n\nu_g\{F_n\ge t\}\,dt.
  \]
  Hence compact strong margin is equivalent to
  \[
    \int_0^n\nu_g\{F_n\ge t\}\,dt\ge {A_n\over n}
    \qquad(n\ge8).
  \]
  Local density and Abel-defect anti-concentration are two sufficient
  mechanisms for this same distribution lower bound.
- `281_ABEL_SPIKE_FEJER_ZERO_MODEL_NO_GO.md` supplies an explicit positive
  finite measure model showing why radial generator data do not replace
  those mechanisms.  With
  \[
    \nu=\sum_j{\log N_j\over N_j}\delta_{e^{2\pi i/N_j}}
  \]
  and \(N_j\) superexponential, one has
  \[
    \int P_{1-1/N_j}\,d\nu\gg\log N_j,
    \qquad
    \int F_{N_j}\,d\nu=O(1).
  \]
  The logarithmic Abel spike sits on the moving zero of \(F_{N_j}\).  Hence
  Abel/\(\mathcal G_+\)-scale lower data, even with positivity, do not force
  compact Fejer margin or an absolutely continuous local log-density.
- `234_WEIGHTED_MERTENS_CHEBYSHEV_ERROR_IDENTITY.md` gives the exact
  identity
  \[
    E_8^\sharp(u)
    =
    e^{-u}E(e^u)-e^{-T_8}E(e^{T_8})
    +\int_{T_8}^{u}e^{-t}E(e^t)\,dt,
  \]
  so the weighted-Mertens frontier is another signed Chebyshev-error
  coordinate, not a new positivity source.
- `201_TERMINAL_LAGUERRE_LOAD_GATE.md` isolates the terminal necessary
  condition for the absolute diagonal route:
  \[
    \mathcal B_n\ge
    \int_{T_{n-1}}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
  \]
  The load has an exact sign-partition formula using the zeros of
  \(L_{n-1}^{(2)}\), and constant envelopes reduce to endpoint values of
  \(L_n^{(1)}\).

The bibliographic gate in `102_BIBLIOGRAPHIC_GATE.md` identifies this A1
mechanism, not the known Li criterion or the known explicit formulae, as the
place where new mathematics must enter.
