# Phase 102 execution plan

## Target

Prove Omega7:

[
  \lambda_n=\lambda_n^{arch}+\lambda_n^{prime}\ge0
  \qquad(n\ge1).
]

The finite exceptional range is already closed by a rational interval
certificate. The only mathematical target still capable of closing the
problem is the infinite signed inequality

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}\qquad(n\ge8).
]

## Closed trunk

| Item | Status | Phase 102 reference |
|---|---|---|
| Exact one-sided target | Closed | Snapshot restart plan |
| Paired arithmetic continuation | Closed | Snapshot restart plan |
| Laguerre integration by parts with boundary term | Closed | Snapshot restart plan |
| Finite range `1 <= n <= 7` | Closed | Snapshot finite certificate |

## Open trunk

| Item | Required closure |
|---|---|
| Global signed inequality | A proof of the lower bound for all `n>=8`. |
| Boundary limit | Uniform passage `epsilon downarrow 0` without separating divergent terms. |
| All scales in `n` | A theorem covering transition, oscillatory and tail ranges. |
| Sign preservation | A decomposition that estimates only after global signed pairing. |
| Discriminant mechanism | An arithmetic mechanism that distinguishes off-line controls without assuming the conclusion. |
| Li assembly | Combine finite and infinite ranges and apply Li. |

## Direct route

The direct route is split into two targets.

### A0

Prove an unconditional uniform tail theorem:

[
  \sup_{0\le\varepsilon\le1}
  \left|
  \int_{e^{T(n)}}^\infty
  (\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
  \right|
  \le {1\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

This target is not expected to carry the full RH difficulty. It should use
only explicit PNT input and uniform Laguerre bounds.

### A1

Prove the signed core inequality:

[
  -n+
  \int_1^{e^{T(n)}}(\psi(y)-y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

This is the first isolated force-RH target in this phase.

## Alternative route

The LP+IDENT/RDI route is not the priority unless it produces one of the two
literal bridges:

[
  \mathrm{RDI}\Longrightarrow \lambda_n\ge0
]

or

[
  \mathrm{RDI}\Longrightarrow\text{all zeros of }\Xi\text{ are real}.
]

Without such a bridge, BTG and GAP-Z remain infrastructure, not closure of
Omega7.

## Work order

1. Lock the finite range in the phase ledger.
2. A0 is closed by `102_A0_UNIFORM_TAIL_THEOREM.md`, up to inserting the
   chosen explicit PNT constants.  The required archimedean lower bound is
   now supplied by `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`.
3. Attack A1 through one of the surviving signed gates recorded in
   `124_A1_GATE_IMPLICATION_GRAPH.md`: direct A1, strong margin, one-sided
   tail, positive boundary measure, Hermite--Biehler, infinite Pick/Stieltjes
   positivity, non-tautological bordered current, or symmetrized Mellin
   boundary positivity.
4. Keep the RDI route in triage unless a literal Li bridge appears.
5. Assemble Li only when no open hypothesis remains.

## Phase 102 reductions now available

| Block | Status | Reference |
|---|---|---|
| A0 tail | Proved modulo the chosen explicit decaying PNT constants; arch lower bound internal | `102_A0_UNIFORM_TAIL_THEOREM.md`, `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`, `152_EXPLICIT_PNT_INPUT_ADAPTER.md` |
| Boundary limit | Reduced to A0 plus A1 | `102_BOUNDARY_LIMIT_AND_LIMIT_ORDER.md` |
| Scale/truncation bookkeeping | Closed as bookkeeping | `102_SCALE_DECOMPOSITION_AND_TRUNCATION.md` |
| Off-line sensitivity | Formulated as required discriminator | `102_A1_ZERO_SIDE_DISCRIMINANT.md` |
| A1 mechanisms | Two local routes eliminated; two global routes survive | `102_A1_SIGNED_COMPENSATION_MECHANISMS.md` |
| Bibliographic gate | A1 identified as the unclaimed mechanism class | `102_BIBLIOGRAPHIC_GATE.md` |
| Mellin coborder | Exact normal form written; sign theorem open | `113_MELLIN_COBORDER_NORMAL_FORM.md` |
| Bordered Euler current | Tautological determinant class eliminated | `114_BORDERED_EULER_CURRENT_AUDIT.md` |
| Weil-Herglotz route | Reduced to positive boundary measure construction | `115_WEIL_HERGLOTZ_REDUCTION.md` |
| Positive boundary measure | Single target theorem stated | `116_POSITIVE_BOUNDARY_MEASURE_TARGET.md` |
| Euler product weights | Direct positivity route eliminated | `117_EULER_PRODUCT_POSITIVE_WEIGHT_AUDIT.md` |
| Stieltjes inversion | Positive measure exists; support collapse open | `118_STIELTJES_INVERSION_SUPPORT_OBSTRUCTION.md` |
| Truncation optimization | Cannot create the A1 sign | `119_A1_TRUNCATION_OPTIMIZATION_AUDIT.md` |
| Bordered current sharp no-go | Schur complement rigidity and exact target | `119_BORDERED_EULER_CURRENT_NO_GO_AND_TARGET.md` |
| de Branges gate | Reduced to independent Hermite--Biehler construction | `119_DE_BRANGES_GATE_FOR_A1.md` |
| Total positivity | Finite tests eliminated; infinite class equals boundary positivity | `120_TOTAL_POSITIVITY_AND_LI_SEQUENCE_AUDIT.md` |
| A1 margin gate | A0 plus strong margin or one-sided tail would close A1 | `121_A1_MARGIN_OR_ONE_SIDED_TAIL_GATE.md` |
| Li test family | Minimal countable target; still RH-strength | `121_LI_TEST_FAMILY_SCOPE.md` |
| Strong margin | Equivalent to sharper signed prime lower bound | `122_STRONG_MARGIN_REDUCTION.md` |
| One-sided tail | Exact signed tail gate stated; PNT tails insufficient | `123_ONE_SIDED_TAIL_GATE.md` |
| Gate graph | Current implications and forbidden shortcuts | `124_A1_GATE_IMPLICATION_GRAPH.md` |
| Fixed-cutoff generating function | Holomorphic coefficient normal form; moving cutoff open | `125_A1_FIXED_CUTOFF_GENERATING_FUNCTION.md` |
| Universal cutoff gate | A0 cannot provide a universal finite cutoff | `126_UNIVERSAL_CUTOFF_GATE_AUDIT.md` |
| Moving-cutoff flow | Exact boundary-current normal form; sign open | `127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md` |
| Tail and margin generators | Strong-margin and tail gates as coefficient problems | `128_TAIL_AND_STRONG_MARGIN_GENERATORS.md` |
| Abel-Laplace tail | Tail is a signed Laplace transform, not positive by A0 | `129_ABEL_LAPLACE_TAIL_DOMAIN_AUDIT.md` |
| Fourier-Bochner gate | Positive Fourier kernel is insufficient for real zeros | `130_FOURIER_BOCHNER_GATE_AUDIT.md` |
| Jensen cofinal gate | Finite/asymptotic checks insufficient; cofinal LP theorem needed | `131_JENSEN_COFINAL_GATE_AUDIT.md` |
| Heat-flow Newman gate | Threshold inequality required; future real-rootedness insufficient | `132_HEAT_FLOW_NEWMAN_GATE_AUDIT.md` |
| Li disk Schur gate | Disk support theorem needed; divisor boundary measure circular | `133_LI_DISK_SCHUR_GATE_AUDIT.md` |
| Off-line geometric mode | Exterior Li multiplier gives negative geometric subsequence | `134_OFFLINE_GEOMETRIC_MODE_LEMMA.md` |
| Archimedean growth | Archimedean term is \(O(n\log n)\) | `135_ARCHIMEDEAN_GROWTH_BOUND.md` |
| Finite exterior shell | Finite maximal exterior shell dominates lower terms | `136_FINITE_EXTERIOR_SHELL_DOMINANCE.md` |
| Isolated exterior radius | Isolated exterior shells reduce to finite dominance | `137_ISOLATED_EXTERIOR_RADIUS_REDUCTION.md` |
| Zeta exterior maximum | Off-line zeta zero gives finite maximal exterior shell | `138_ZETA_EXTERIOR_RADIUS_MAXIMUM.md` |
| Zero-side Li closure | Li positivity equivalent to critical-line support | `139_ZERO_SIDE_LI_CRITERION_CLOSURE.md` |
| Euler-Gamma Li generator | Exact arithmetic coefficient generator and paired prime split | `140_EULER_GAMMA_LI_GENERATOR.md` |
| Prime-pole integral generator | Generator coefficients equal the Laguerre prime-pole integral; A1 is the same compact sign problem | `141_PRIME_POLE_INTEGRAL_GENERATOR.md` |
| Variational energy form | A1 as a Schur--Friedrichs minimum; coercive Euler--Gamma Schur lemma still required | `142_A1_VARIATIONAL_ENERGY_FORM.md` |
| Prime-pole Pick/Stieltjes gate | Local positive-measure route eliminated; completed boundary support theorem isolated | `143_PRIME_POLE_PICK_STIELTJES_GATE.md` |
| Laguerre core sign partition | Kernel collapses to \(L_{n-1}^{(2)}\); A1 is an adjacent-lobe compensation theorem | `144_LAGUERRE_CORE_SIGN_PARTITION.md` |
| Laguerre lobe dual balance | Once-integrated prime-pole balance; A1 is a signed cumulative lobe theorem | `145_LAGUERRE_LOBE_DUAL_BALANCE.md` |
| Raised Laguerre dual hierarchy | Repeated cumulative balances \(B_r\) and raised kernels \(L_{n-1}^{(2+r)}\) give equivalent A1 targets | `146_RAISED_LAGUERRE_DUAL_HIERARCHY.md` |
| Balance Laplace jet form | Raised-balance A1 target as a finite signed jet of \(\mathcal B_{r,T}(s)\) at \(s=1\) | `147_BALANCE_LAPLACE_JET_FORM.md` |
| A1 finite arithmetic certificate schema | Each raised A1 instance reduced to explicit finite prime-power sums and endpoint blocks | `148_A1_FINITE_ARITHMETIC_CERTIFICATE_SCHEMA.md` |
| Moving diagonal A1 generator | Fixed-cutoff generator is explicit; actual A1 is coefficient positivity along \(T=T_n\) | `149_MOVING_DIAGONAL_A1_GENERATOR.md` |
| A1 tail remainder generator identity | Exact identity \(C_n(T)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T)\) fixes signs for margin/tail gates | `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md` |
| Archimedean positive lower bound | Explicit \(B_n>0\) with \(B_n\le\lambda_n^{\rm arch}\) for all \(n\ge8\) | `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md` |
| Explicit PNT adapter | A0 needs a decaying Vinogradov--Korobov remainder, not a constant relative Chebyshev bound | `152_EXPLICIT_PNT_INPUT_ADAPTER.md` |
| Cutoff comparison gate | Exact flow \(C_n(T)-C_n(S)\); cutoff transfer needs a signed lobe theorem | `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md` |
| Cutoff transfer dual balance | Cutoff transfer as accumulated prime-pole balance against \(L_{n-1}^{(3)}\) | `154_CUTOFF_TRANSFER_DUAL_BALANCE.md` |
| A1 Weil square-root gate | Mellin explicit formula needs a positive autocorrelation factorization to imply A1 | `155_A1_WEIL_SQUARE_ROOT_GATE.md` |
| A1 Laguerre n-recurrence gate | Three-term recurrence reduces induction to a signed forcing moment \(F_n(T)\) | `156_A1_LAGUERRE_N_RECURRENCE_GATE.md` |
| Archimedean forcing audit | Archimedean part of the recurrence forcing is explicit but not sign-free | `157_ARCHIMEDEAN_FORCING_AUDIT.md` |
| A1 gate triage | Separates equivalent normal forms from genuine stronger positivity targets | `158_A1_GATE_TRIAGE_AND_PRIORITY.md` |
| Inductive forcing certificate | Full forcing \(F_n(T)\) as finite prime-power sums plus explicit archimedean correction | `159_INDUCTIVE_FORCING_CERTIFICATE_SCHEMA.md` |
| Inductive forcing generator | Recurrence forcing as a fixed-cutoff coefficient-sum generator \(\mathcal F_T\) | `160_INDUCTIVE_FORCING_GENERATOR.md` |
| Li Toeplitz moment gate | Infinite disk Toeplitz positivity as a non-circular boundary-measure theorem | `161_LI_TOEPLITZ_MOMENT_GATE.md` |
| Li Fejer trigonometric gate | Toeplitz positivity as nonnegativity on every squared trigonometric polynomial, equivalently all translated Fejer means | `162_LI_FEJER_TRIGONOMETRIC_MOMENT_GATE.md` |
| Prime-pole Fejer support gate | Scalar Cesaro tests are insufficient; full translated Fejer positivity is the same support theorem | `163_PRIME_POLE_FEJER_TOEPLITZ_SUPPORT_GATE.md` |
| Toeplitz Schur margin | A1 after A0 would follow from a Toeplitz Li-test margin or stronger innovation margin | `164_A1_TOEPLITZ_SCHUR_MARGIN.md` |
| Poisson Carathéodory gate | Toeplitz/Fejer positivity as \(\Re H_{\rm EG}\ge0\) in the disk | `165_POISSON_CARATHEODORY_POSITIVITY_GATE.md` |
| Poisson support no-go | Exact transformed-zero singularities plus Carathéodory positivity force boundary support; compact A1 still needs the square margin | `166_POISSON_CARATHEODORY_SUPPORT_GATE.md` |
| Li moment renormalization obstruction | Finite Herglotz measures cannot naively represent the unweighted infinite Li divisor; a renormalized positive object is required | `167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md` |
| Renormalized vanishing-test kernel | Positive Euler--Gamma kernel on \((z-1)\mathbb C[z]\) would avoid finite-mass obstruction and contains all Li tests | `168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md` |
| Li Schoenberg vanishing kernel | Kernel \(K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}\) is the explicit negative-type normal form | `169_LI_SCHOENBERG_VANISHING_KERNEL.md` |
| Vanishing kernel pairing no-go | Functional-equation cross-pairing recovers Li but is locally indefinite off the unit circle | `170_VANISHING_KERNEL_PAIRING_NO_GO.md` |
| Local counterterm rigidity | Positive local counterterms, and any positive global counterterm invisible on all Li diagonals, cannot repair the cross-pairing after exact Li normalization | `171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md` |
| Schoenberg increment Toeplitz gate | Kernel positivity is equivalent to Toeplitz positivity of Li second differences \(g_m\) | `172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md` |
| Weighted zero-divisor measure gate | Second differences \(g_m\) are the finite weighted-divisor moments \(|1-w_\rho|^2\) on the critical-line model | `173_WEIGHTED_ZERO_DIVISOR_MEASURE_GATE.md` |
| Log-derivative half-plane positivity | Increment Toeplitz positivity is equivalent to \(\Re(\xi'/\xi)(s)\ge0\) in \(\Re s>1/2\) | `174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md` |
| Log-derivative RH equivalence | Half-plane positivity of \(\xi'/\xi\) is equivalent to RH, so it is a valid but RH-strength closure route | `175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` |
| Horizontal xi modulus monotonicity | Equivalent target \(\partial_\sigma\log|\xi(\sigma+it)|\ge0\), written as an explicit Euler--Gamma signed inequality | `176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md` |
| Sigma greater than one positivity | \(\Re(\xi'/\xi)>0\) is unconditional for \(\Re s>1\); only the strip \(1/2<\Re s\le1\) remains | `177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md` |
| Strip Poisson boundary no-go | Boundary signs in the strip are favorable, but Poisson needs zero-freeness inside the strip | `178_STRIP_POISSON_BOUNDARY_NO_GO.md` |
| Strip pole-defect decomposition | Interior zeros contribute sign-changing Green defects \(m\Re(s-\rho)^{-1}\) that boundary signs cannot ignore | `179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md` |
| Strip Poisson kernel formula | Explicit strip Poisson kernel gives positivity conditionally on the zero-free strip hypothesis | `180_STRIP_POISSON_KERNEL_FORMULA.md` |
| Global positivity versus compact A1 margin | Global RH/Li positivity closes Omega7 but compact A1 still needs strong margin, one-sided tail, or direct signed core | `181_GLOBAL_POSITIVITY_VS_COMPACT_A1_MARGIN.md` |
| Horizontal zero-barrier no-go | An off-line zero creates an infinite local downward wall for \(\log|\xi|\), so monotonicity cannot follow from bounded boundary/subharmonic corrections | `182_HORIZONTAL_ZERO_BARRIER_NO_GO.md` |
| Exact cumulative forcing representation | Fixed-cutoff recurrence solved exactly; A1 induction requires weighted cumulative forcing plus transfer | `183_EXACT_CUMULATIVE_FORCING_REPRESENTATION.md` |
| Moving diagonal recurrence defect | A1 diagonal recurrence has forcing \(F_n(T_n)\) plus two signed cutoff-transfer defects | `184_MOVING_DIAGONAL_RECURRENCE_DEFECT.md` |
| Diagonal forcing single-kernel form | \(F_n^{\rm diag}\) is one signed pairing against a piecewise Laguerre kernel plus archimedean correction | `185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md` |
| Cumulative diagonal forcing kernel | The full induction sum is one compact signed pairing against \(\mathcal H_n\) plus explicit base/archimedean terms | `186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md` |
| Cumulative diagonal balance form | Once-integrated induction sum equals a raised-kernel balance plus all signed cutoff jumps | `187_CUMULATIVE_DIAGONAL_BALANCE_FORM.md` |
| Diagonal cumulative coercivity audit | Two-sided envelopes for \(E\) collapse to the absolute-value bound; useful diagonal coercivity must be one-sided arithmetic | `188_DIAGONAL_CUMULATIVE_COERCIVITY_AUDIT.md` |
| Global log derivative to compact A1 audit | Half-plane positivity closes Omega7 through RH/Li but implies compact A1 only with a one-sided tail bridge, strong margin, or direct signed core | `189_GLOBAL_LOG_DERIVATIVE_TO_COMPACT_A1_AUDIT.md` |
| Diagonal balance finite certificate | The balance form with jumps is an explicit finite prime-power certificate \(\mathcal A_n+\Pi_n+\sum\Lambda(m)\Xi_n(m)\ge0\) | `190_DIAGONAL_BALANCE_FINITE_CERTIFICATE.md` |
| Absolute diagonal budget scale audit | The absolute route requires \(\mathcal B_n\) to dominate weighted \(L^1\) norms of \(\mathcal H_n\) for an explicit PNT envelope | `191_ABSOLUTE_DIAGONAL_BUDGET_SCALE_AUDIT.md` |
| One-sided tail from global positivity audit | Global Toeplitz/Schoenberg positivity does not order the moving tail \(R_n(T_n)\); the tail inequality is A1 in tail form unless a new margin/comparison theorem is added | `192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md` |
| Weighted L1 kernel certificate | The absolute load \(W_n(R)\) is a finite sign-partition certificate over zeros of the piecewise polynomial \(\mathcal H_n\) | `193_WEIGHTED_L1_KERNEL_CERTIFICATE.md` |
| Strong margin generator second pass | Strong margin is coefficient positivity of \(\mathcal L-\frac12\mathcal A\); bare Toeplitz/Schoenberg positivity lacks the archimedean diagonal margin | `194_STRONG_MARGIN_GENERATOR_SECOND_PASS.md` |
| Loewner--Schur tail comparison gate | A1 would follow from positivity of \(\mathfrak Q^{\mathcal L}-\frac14\mathfrak Q^{\mathcal A}-\mathfrak Q^{\mathcal R,T_n}\) on \(1-z^n\) or a containing subspace; global Toeplitz positivity alone does not give this order | `195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` |
| A1 remaining theorems canonical form | Consolidates the exact surviving theorem statements whose proof would close A1 or Omega7 | `196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md` |
| Cumulative kernel interval form | Gives the exact interval polynomials for \(\mathcal H_n\); the terminal load is \(|L_{n-1}^{(2)}|\), earlier loads are cumulative mixtures | `197_CUMULATIVE_KERNEL_INTERVAL_FORM.md` |
| Strong margin second-difference audit | Strong margin is a Dirichlet-energy lower bound for the increment Toeplitz sequence \(g_m\), not a consequence of Toeplitz positivity alone | `198_STRONG_MARGIN_SECOND_DIFFERENCE_AUDIT.md` |
| Comparative innovation margin gate | A Schur proof of A1 must prove comparative block positivity and nonnegative innovation before using the diagonal \(2C_n(T_n)\); otherwise it is circular | `199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` |
| Fejer mass strong-margin gate | Strong margin follows from a moving local mass lower bound for the increment measure near \(1\), stronger than positivity or total mass | `200_FEJER_MASS_STRONG_MARGIN_GATE.md` |
| Terminal Laguerre load gate | Any absolute diagonal proof must dominate the terminal load \(\int_{T_{n-1}}^{T_n}\varepsilon|L_{n-1}^{(2)}|\) before mixed intervals | `201_TERMINAL_LAGUERRE_LOAD_GATE.md` |
| Fejer density scale gate | Bounded increment-measure density gives only \(O(n)\) Fejer energy, below the \(n\log n\) archimedean margin; logarithmic/singular concentration is needed | `202_FEJER_DENSITY_SCALE_GATE.md` |
| Atom at one incompatibility audit | An atom of the increment measure at \(1\) would force \(\lambda_n\sim a n^2/2\) and a cubic pole in \(\mathcal L\), incompatible with the Euler--Gamma generator scale | `203_ATOM_AT_ONE_INCOMPATIBILITY_AUDIT.md` |
| Log-density increment generator gate | The increment generator has logarithmic boundary scale, matching log density near \(1\), but a positive lower-density theorem is still missing | `204_LOG_DENSITY_INCREMENT_GENERATOR_GATE.md` |
| Fejer log-constant audit | Exact constants are favorable for a pure log-density model: Abel coefficient \(1/2\) corresponds to density coefficient \(1\), while the exact Fejer margin needs leading coefficient \(1/2\); the missing input is still positivity plus a lower Fejer theorem | `205_FEJER_LOG_CONSTANT_AUDIT.md` |
| Fejer-Abel Tauberian gap | Abel logarithmic growth does not imply the Fejer margin without anti-concentration near moving Fejer zeros or a direct log-density/Fejer lower theorem | `206_FEJER_ABEL_TAUBERIAN_GAP.md` |
| A0 terminal-cutoff bridge audit | The A0 cutoff for \(n-1\) bounds the terminal Laguerre load for \(n\) only with a logarithmic cutoff-ratio loss, so the absolute route still needs a surplus or ratio theorem | `207_A0_TERMINAL_CUTOFF_BRIDGE_AUDIT.md` |
| VK cutoff-ratio terminal scale | For canonical Vinogradov--Korobov cutoffs, the terminal cutoff-ratio loss is \(O(1/n)\), giving terminal load \((5/72)\log n+O(1)\), but mixed intervals and \(\mathcal B_n\) remain open | `208_VK_CUTOFF_RATIO_TERMINAL_SCALE.md` |
| Archimedean budget sign audit | The recurrence archimedean forcing has \(D_n^{\rm arch}\sim-\frac12\log n\), so positive cumulative weights do not create a positive absolute-route budget | `209_ARCHIMEDEAN_BUDGET_SIGN_AUDIT.md` |
| Base-budget quadratic coefficient gate | The budget has \(\mathcal B_n=\Gamma_{\mathcal B}n^2+O(n\log n)\); terminal absorption for VK cutoffs depends on the sign of \(\Gamma_{\mathcal B}\) | `210_BASE_BUDGET_QUADRATIC_COEFFICIENT_GATE.md` |
| Mixed-interval off-diagonal load gate | Earlier intervals contain high-degree cumulative Laguerre mixtures; A0 cutoff decay at \(T_j\) does not automatically dominate the mixed \(L^1\) load | `211_MIXED_INTERVAL_OFFDIAGONAL_LOAD_GATE.md` |
| Base-budget telescoping reduction | The infinite archimedean series in \(\Gamma_{\mathcal B}\) telescopes, reducing positivity to a finite lower bound on \(\Delta_8^\ast\) | `212_BASE_BUDGET_TELESCOPING_REDUCTION.md` |
| Gamma_B compact base identity | The budget coefficient equals \((I_7(T_7)-I_8(T_8))/16\), so its sign is a finite compact arithmetic comparison | `213_GAMMA_B_COMPACT_BASE_IDENTITY.md` |
| Gamma_B base finite certificate | The sign of \(\Gamma_{\mathcal B}\) is an explicit finite prime-power inequality involving \(\Lambda(m)\) up to \(e^{\max(T_7,T_8)}\) and elementary Laguerre endpoint expressions | `214_GAMMA_B_BASE_FINITE_CERTIFICATE.md` |
| Base-cutoff Gamma positivity | With small auxiliary \(T_7\), the base condition \(C_8^\ast\ge0\) implies \(\Gamma_{\mathcal B}>0\), removing a separate terminal budget sign gate | `215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md` |
| Base C8 compact certificate | The base condition \(C_8^\ast\ge0\) is the finite inequality \(\Psi_8(T_8)-\sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)\ge8-\frac34A_8\), or follows from the finite strong margin \(\lambda_8\ge\frac12A_8\) | `216_BASE_C8_COMPACT_CERTIFICATE.md` |
| n=8 base margin certificate | A finite interval computation proves \(\lambda_8-\frac12\lambda_8^{\rm arch}>0\); A0 then gives \(C_8^\ast>0\) and hence the \(\Gamma_{\mathcal B}\) sign under the small-\(T_7\) normalization | `217_N8_BASE_MARGIN_CERTIFICATE.md` |
| Mixed A0 degree mismatch audit | A0 decay at \(T_j\) is calibrated to degree \(j\), while mixed intervals contain Laguerre degrees up to \(n-2\); the crude bound leaves \((1+u)^{k-j-2}\) | `218_MIXED_A0_DEGREE_MISMATCH_AUDIT.md` |
| Mixed Laguerre telescoping collapse | The cumulative off-diagonal mixture telescopes: \(\mathcal H_n=-L_{n-1}^{(2)}\) on \(T_8<u<T_n\), leaving only two low-cutoff degree-7 correction intervals | `219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md` |
| Terminal effective threshold reduction | The terminal interval is asymptotically absorbed after `217`, with \(\Gamma_{\mathcal B}>25/64\) versus VK terminal load \(O(\log n)\); the remaining terminal work is a finite rational threshold certificate | `220_TERMINAL_EFFECTIVE_THRESHOLD_REDUCTION.md` |
| Single Laguerre bulk L1 obstruction | In the collapsed absolute route, Plancherel--Rotach bulk growth \(e^{u/2}\) beats VK subexponential decay on \(u\asymp n\), so a VK absolute \(L^1\) proof cannot dominate by \(\mathcal B_n=O(n^2)\) | `221_SINGLE_LAGUERRE_BULK_L1_OBSTRUCTION.md` |
| Signed balance telescoped certificate | The telescoped kernel leaves only jumps at \(T_7,T_8\); the signed A1 route becomes a finite prime-power inequality with \(L_{n-1}^{(3)}\) plus degree-7 corrections | `222_SIGNED_BALANCE_TELESCOPED_CERTIFICATE.md` |
| Signed balance B-envelope no-go | A two-sided envelope for \(B(U)\) again becomes an absolute \(L^1\) problem, now for \(L_{n-1}^{(3)}\), and VK-scale decay fails by the same bulk growth | `223_SIGNED_BALANCE_B_ENVELOPE_NO_GO.md` |
| Strong margin RH-strength audit | The strong margin plus the finite \(1\le n\le7\) certificate implies all Li coefficients are nonnegative, hence RH; this route requires RH-strength sign information | `224_STRONG_MARGIN_RH_STRENGTH_AUDIT.md` |
| A1 post-absolute decision ledger | Consolidates that base, terminal asymptotic, and mixed structural gates are closed; VK absolute and symmetric \(B\)-envelope routes are discarded; remaining routes are signed/RH-strength | `225_A1_POST_ABSOLUTE_ROUTE_DECISION_LEDGER.md` |
| Direct telescoped prime-coefficient certificate | Expands the signed pairing directly; each prime-power coefficient is an endpoint formula in \(e^{-u}L_{n-1}^{(1)}\) plus fixed degree-7 corrections, avoiding the \(B\)-envelope layer | `226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md` |
| Small-T7 prime-block elimination | With \(0<T_7<\log2\), no prime powers lie in \(\log m<T_7\); the direct signed certificate has only the low block \(T_7\le\log m<T_8\) and high block \(T_8\le\log m\) | `227_SMALL_T7_PRIME_BLOCK_ELIMINATION.md` |
| High-block Laguerre correlation form | Rewrites the high block as \(e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}-\sum\Lambda(m)m^{-1}L_{n-1}^{(1)}(\log m)\), isolating the signed prime-power correlation | `228_HIGH_BLOCK_LAGUERRE_CORRELATION_FORM.md` |
| Small-T7 direct coefficient reduction | Combines `226`--`228`; all moving arithmetic content is one signed Chebyshev--Laguerre transform plus fixed base-window constants below \(T_8\) | `229_SMALL_T7_DIRECT_COEFFICIENT_REDUCTION.md` |
| Single-transform A1 frontier | Reconciles the telescoped route with the original compact core; A1 is one signed inequality for \(S_n(T_n)=\sum\Lambda(m)m^{-1}L_{n-1}^{(1)}(\log m)\) | `230_SINGLE_TRANSFORM_A1_FRONTIER.md` |
| High-block partial summation form | Converts the high correlation to \(A_8(T_n)L_{n-1}^{(1)}(T_n)+\int_{T_8}^{T_n}A_8(u)L_{n-2}^{(2)}(u)\,du\), isolating the weighted discrepancy \(E_8^\sharp\) | `231_HIGH_BLOCK_PARTIAL_SUMMATION_FORM.md` |
| Weighted Mertens envelope no-go | A two-sided bound for \(E_8^\sharp\) again yields an absolute \(L^1\) load for \(L_{n-2}^{(2)}\), whose bulk growth beats VK-subexponential decay | `232_WEIGHTED_MERTENS_ENVELOPE_NO_GO.md` |
| Single-transform fixed-cutoff generator | Packages \(S_n(T)\) as a finite Dirichlet-polynomial generating function; fixed-\(T\) positivity is explicit but A1 still needs moving-cutoff positivity | `233_SINGLE_TRANSFORM_FIXED_CUTOFF_GENERATOR.md` |
| Weighted Mertens--Chebyshev error identity | Expresses \(E_8^\sharp\) as boundary plus integral transforms of \(E(e^u)\), showing the weighted-Mertens frontier is the same signed Chebyshev--Laguerre core | `234_WEIGHTED_MERTENS_CHEBYSHEV_ERROR_IDENTITY.md` |
| Moving-cutoff derivative gate | Computes \(C_n'(T)=-(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)\) between prime-power jumps and shows jumps cancel; fixed-cutoff transfer requires a signed integral theorem | `235_MOVING_CUTOFF_DERIVATIVE_GATE.md` |
| Single-transform zero-side margin audit | Shows that Li/RH or a zero-side explicit formula does not by itself prove compact A1; the route still needs strong margin, one-sided tail, or equivalent compact margin | `236_SINGLE_TRANSFORM_ZERO_SIDE_MARGIN_AUDIT.md` |
| Cutoff-transfer tail equivalence | Shows that transferring positivity from fixed or infinite cutoff to \(T_n\) is exactly a signed tail/correlation theorem; symmetric estimates require strong margin | `237_CUTOFF_TRANSFER_TAIL_EQUIVALENCE.md` |
| Tail-margin compensation frontier | Writes \(C_n(T_n)=M_n+\delta_n\), where \(M_n=\lambda_n-\frac12A_n\) and \(\delta_n=\frac14A_n-R_n(T_n)\ge0\); A1 requires tail surplus to compensate any strong-margin deficit | `238_TAIL_MARGIN_COMPENSATION_FRONTIER.md` |
| Margin-tail threshold ladder | Calibrates partial Li margin \(\lambda_n\ge\kappa_n A_n\) against one-sided tail \(R_n(T_n)\le\rho_n A_n\); A1 is \(\kappa_n-\rho_n\ge1/4\) | `239_MARGIN_TAIL_THRESHOLD_LADDER.md` |
| Deficit-ratio tail-surplus gate | Normalizes the strong-margin deficit \(d_n=(-M_n)_+/A_n\) and tail surplus \(s_n=\delta_n/A_n\); A1 is exactly \(s_n\ge d_n\) | `240_DEFICIT_RATIO_TAIL_SURPLUS_GATE.md` |
| Tail-surplus generator diagonal no-go | Packages \(\delta_n\) as coefficients of \(\Delta_{T_n}\), with cutoff flow \(d[z^n]\Delta_T/dT=-E(e^T)e^{-T}L_{n-1}^{(2)}(T)\); isolated surplus positivity is insufficient | `241_TAIL_SURPLUS_GENERATOR_DIAGONAL_NO_GO.md` |
| Loewner cone margin-tail decomposition | Splits \(\mathfrak Q^{\mathcal C,T}\) into strong-margin and tail-surplus forms; a valid Loewner proof must dominate the negative margin cone or prove Schur innovation before using \(2C_n(T_n)\) | `242_LOEWNER_CONE_MARGIN_TAIL_DECOMPOSITION.md` |
| Loewner negative-part compensation reduction | Refines the cone target by decomposing \(\mathfrak Q^{\mathcal M}\) into positive/negative parts; domination of \(\mathfrak Q^{\mathcal M}_-\) by the surplus form is sufficient | `243_LOEWNER_NEGATIVE_PART_COMPENSATION_REDUCTION.md` |
| A0 tail-improvement requirement | Rewrites compact A1 as the sharp normalized improvement over A0: \(\eta_n=\frac14-R_n(T_n)/A_n\) must dominate the strong-margin deficit \(d_n=\max(0,\frac12-\lambda_n/A_n)\) | `244_A0_TAIL_IMPROVEMENT_REQUIREMENT.md` |
| Terminal threshold data dependence | Records the six fixed data items needed to turn the terminal asymptotic theorem into a rational finite threshold certificate | `245_TERMINAL_THRESHOLD_DATA_DEPENDENCE_CERTIFICATE.md` |
| Global half-plane / compact A1 separation | Shows that global half-plane positivity would close Omega7 through RH/Li, but gives only \(d_n\le1/2\); compact A1 still requires \(s_n\ge d_n\) | `246_GLOBAL_HALF_PLANE_COMPACT_A1_SEPARATION.md` |
| Quarter-margin plus nonpositive-tail gate | Shows A1 follows from \(\lambda_n\ge A_n/4\) and \(R_n(T_n)\le0\); this is a sufficient RH-strength special point of the margin-tail ladder | `247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md` |
| Quarter-margin generator RH-strength audit | Defines \(\mathcal Q_{1/4}=\mathcal L-\frac14\mathcal A\) and shows its coefficient positivity for \(n\ge8\) already implies Li/RH with the finite low-index certificate | `248_QUARTER_MARGIN_GENERATOR_RH_STRENGTH_AUDIT.md` |
| Tail-sign Laguerre zero partition gate | Converts \(R_n(T_n)\le0\) into a signed lobe inequality over zeros of \(L_{n-1}^{(2)}\) beyond \(T_n\); A0 gives only a weaker lower bound | `249_TAIL_SIGN_LAGUERRE_ZERO_PARTITION_GATE.md` |
| Nonpositive-tail symmetric-envelope no-go | Shows \(R_n(T_n)\le0\) cannot be inferred from any two-sided envelope \(|E(e^u)|\le W(u)\); the tail functional changes sign under \(E\mapsto-E\) | `250_NONPOSITIVE_TAIL_SYMMETRIC_ENVELOPE_NO_GO.md` |
| RDI Li-coefficient extraction gate | States the exact local-uniform coefficient bridge needed for RDI to imply \(\lambda_n\ge0\), or alternatively real-rooted convergence to \(\Xi\) | `251_RDI_LI_COEFFICIENT_EXTRACTION_GATE.md` |
| Real-ray convergence not Li-coefficient no-go | Shows pointwise real-axis convergence does not imply Li coefficient convergence; local uniform complex convergence is essential for the RDI bridge | `310_REAL_RAY_CONVERGENCE_NOT_LI_COEFFICIENT_NO_GO.md` |
| Schur zero-coupling diagonal collapse | Shows a comparative Schur block with \(b_n=0\) has innovation \(2C_n(T_n)\), so zero coupling is exactly A1 rather than a new margin | `252_SCHUR_ZERO_COUPLING_DIAGONAL_COLLAPSE.md` |
| Disk Herglotz half-plane gate | Reformulates \(\Re(\xi'/\xi)\ge0\) in \(\Re s>1/2\) as a positive boundary-measure representation for \(H_\xi(z)=2\xi'/\xi(1/(1-z))\) | `253_DISK_HERGLOTZ_MEASURE_HALF_PLANE_GATE.md` |
| Tail-sign explicit-formula phase gate | Rewrites the nonpositive-tail condition as a one-sided zero-phase inequality with incomplete Laguerre transforms \(\Phi_{n,T}(\rho)\) | `254_TAIL_SIGN_EXPLICIT_FORMULA_PHASE_GATE.md` |
| Tail-margin correlation slack form | Introduces \(h_n\) via \(R_n(T_n)\le A_n/4-h_n\) and shows compact A1 is exactly the pointwise slack condition \(h_n\ge(-M_n)_+\) | `255_TAIL_MARGIN_CORRELATION_SLACK_FORM.md` |
| Pointwise dual cone and average gate | Shows smoothed positivity is insufficient unless coordinate masses are positively reconstructible, or unless a coefficient-extraction theorem is proved | `256_POINTWISE_DUAL_CONE_AND_AVERAGE_GATE.md` |
| Averaged slack pointwise no-go | Shows averaged, density-one, cofinal, or purely asymptotic tail-margin slack does not imply compact A1 without pointwise conversion or finite exceptional certificates | `257_AVERAGED_SLACK_POINTWISE_NO_GO.md` |
| Critical-line support tail-phase no-go | Shows that critical-line support of the zero measure does not by itself imply the oriented incomplete-Laguerre phase inequality required for the compact tail sign or \(s_n\ge d_n\) | `258_CRITICAL_LINE_SUPPORT_TAIL_PHASE_NO_GO.md` |
| Tail phase and lobe duality gate | Shows the Laguerre lobe tail inequality and the explicit-formula zero-phase inequality are the same signed functional, so unsigned lobe/zero bounds cannot prove the tail sign | `274_TAIL_PHASE_LOBE_DUALITY_GATE.md` |
| Tail-phase lobe balance gate | Splits the critical-line phase kernel into \(q^+-q^-\) and identifies the exact required dominance \(P^-_{n,T_n}-P^+_{n,T_n}\) over the trivial-tail and deficit margin | `280_TAIL_PHASE_LOBE_BALANCE_GATE.md` |
| Phase completion criterion A1/global | Separates external Omega7 closure from compact A1 closure and records the exact routes that satisfy the explicit “including A1” completion target | `275_PHASE_COMPLETION_CRITERION_A1_AND_GLOBAL.md` |
| Loewner subspace cofinality gate | Shows Loewner positivity proves A1 only on spaces containing \(p_n=1-z^n\), or when \(p_np_n^*\) is positively reconstructible from tested rank-one forms | `276_LOEWNER_SUBSPACE_COFINALITY_GATE.md` |
| Finite certificate effective-threshold gate | Shows pointwise arithmetic certificates close only checked indices unless paired with a uniform theorem or explicit \(N_\infty\) plus rigorous finite verification below it | `277_FINITE_CERTIFICATE_EFFECTIVE_THRESHOLD_GATE.md` |
| Cofinal subsequence certificate no-go | Shows certificates on a cofinal or density-one subset still do not prove compact A1 unless propagation, positive reconstruction, or an effective-threshold theorem covers every omitted coordinate | `278_COFINAL_SUBSEQUENCE_CERTIFICATE_NO_GO.md` |
| Radial Abel positivity not Herglotz no-go | Shows positivity/logarithmic growth on the positive radius does not imply disk Carathéodory positivity or Toeplitz positivity; angular tests are still required | `290_RADIAL_ABEL_POSITIVITY_NOT_HERGLOTZ_NO_GO.md` |
| Centered Fejer tests not Toeplitz no-go | Gives a finite Hermitian sequence with all centered Fejer sums positive but a negative Toeplitz block, separating Li diagonal tests from full Herglotz positivity | `300_CENTERED_FEJER_TESTS_NOT_TOEPLITZ_NO_GO.md` |
| Finite Toeplitz blocks not Herglotz gate | Shows any fixed finite family of Toeplitz blocks can be positive while the next block is indefinite; Herglotz needs infinite Toeplitz positivity or a genuine limiting theorem | `324_FINITE_TOEPLITZ_BLOCKS_NOT_HERGLOTZ_GATE.md` |
| Fejer log-density closure theorem | Conditional strong-margin theorem: a positive increment measure plus an explicit Fejer lower bound, or log-density coefficient \(a>1/2\), closes the infinite range with a finite remainder | `259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` |
| Exact Fejer log-kernel constant | Proves \(\int F_nL\,dm=H_{n-1}-(n-1)/n\ge\log n-1\), fixing \(B_L=1\) for the conditional log-density closure route | `260_EXACT_FEJER_LOG_KERNEL_CONSTANT.md` |
| Fejer finite-remainder certificate schema | Specifies the pointwise interval certificates needed for \(8\le n<N_\infty\): either strong margin \(\lambda_n\ge A_n/2\) or direct compact \(C_n(T_n)\ge0\) | `261_FEJER_FINITE_REMAINDER_CERTIFICATE_SCHEMA.md` |
| Explicit archimedean upper Fejer input | Proves \(\lambda_n^{arch}\le\frac12 n\log n+3n\) for \(n\ge2\), fixing \(B_A=3\), \(N_A=2\) in the conditional Fejer threshold | `262_EXPLICIT_ARCHIMEDEAN_UPPER_FEJER_INPUT.md` |
| Local log-density to global Fejer patch | Shows a local logarithmic lower density near \(\zeta=1\), plus global nonnegativity, yields the required global Fejer lower bound with an explicit worsened constant | `263_LOCAL_LOG_DENSITY_TO_GLOBAL_FEJER_PATCH.md` |
| Fejer route explicit threshold ledger | Combines the Fejer constants into \(N_\infty=\max(2,\lceil\exp((3+a+B_h^\ast)/(a-1/2))\rceil)\), reducing the route to a positive measure, local density, and finite verification | `264_FEJER_ROUTE_EXPLICIT_THRESHOLD_LEDGER.md` |
| Fejer log-density Abel coefficient budget | Shows the actual Euler--Gamma Abel growth forces any logarithmic lower-density coefficient to satisfy \(a\le1\), while closure requires \(a>1/2\) | `265_FEJER_LOG_DENSITY_ABEL_COEFFICIENT_BUDGET.md` |
| Abel-to-Fejer defect gate | Reduces any Abel-transfer proof to bounding the positive defect \(D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+\); in the natural normalization \(c_P=1\), \(\alpha=1\), the defect coefficient must satisfy \(d<1/2\) | `266_ABEL_TO_FEJER_DEFECT_GATE.md` |
| Abel-defect constant threshold | Gives the explicit constant condition \(d_\alpha<1-\alpha/2\) and threshold \(N_\infty(\alpha)\) that would turn an Abel defect anti-concentration theorem into strong margin plus the finite certificate of `261` | `291_ABEL_DEFECT_CONSTANT_THRESHOLD_LEDGER.md` |
| Poisson-weighted bad-set anti-concentration | Reduces the defect estimate to bounding Poisson-weighted mass on \(B_{n,\tau}=\{F_n<\tau P_n\}\), with constant condition \(b_\tau+(1-\alpha\tau)_+<1-\alpha/2\) | `292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md` |
| Fejer--Poisson bad-set geometry | Shows \(B_{n,\tau}\) contains \(1/n\)-scale windows around every nontrivial \(n\)-th root, so the Abel-transfer route needs arithmetic anti-concentration for \(\nu_g\) | `293_FEJER_POISSON_BAD_SET_GEOMETRY_GATE.md` |
| Bad-set Carleson window condition | Gives a sufficient local-window theorem: if \(\nu_g(I_{n,k})\le(\rho_\tau\log n+B_\tau)/n\) on root windows and \(C_\tau'\rho_\tau<1-1/(2\tau)\), \(\tau>1/2\), then the `292` bad-set estimate feeds into the `291` Abel threshold | `311_BAD_SET_CARLESON_WINDOW_SUFFICIENT_CONDITION.md` |
| Weighted Carleson bad-set gate | Refines the root-window condition to the Poisson-weighted sum \(\sum_k n\nu_g(I_{n,k})/(1+\kappa(k)^2)\le\beta_\tau\log n+B_\tau\), with target \(C_\tau\beta_\tau<1-1/(2\tau)\) | `296_WEIGHTED_CARLESON_BAD_SET_GATE.md` |
| Central-floor weighted budget gate | Combines the central log-density floor with the weighted upper target, forcing \(aK(\tau)\le C_\tau\beta_\tau<1-1/(2\tau)\) for any viable Abel bad-set proof | `297_CENTRAL_FLOOR_WEIGHTED_BUDGET_GATE.md` |
| Central-floor compatibility window | Shows the central floor is not by itself contradictory: at \(\tau=3/2\), \(K(3/2)<2/3\), so \(aK(3/2)<1-1/(2\tau)\) for all \(a\le1\) | `316_CENTRAL_FLOOR_COMPATIBILITY_WINDOW.md` |
| Bad-set central-window log-mass floor | Shows every usable \(\tau>1/2\) makes \(B_{n,\tau}\) contain a central \(1/n\)-window, forcing a positive coefficient floor from any local lower log-density \(h\ge aL-B\) | `314_BAD_SET_CENTRAL_WINDOW_LOG_MASS_FLOOR.md` |
| Local density not bad-set anti-concentration | Shows local logarithmic density near \(1\) does not imply the Poisson-weighted bad-set bound; sparse positive spikes at moving Fejer zeros can force arbitrarily large bad-set coefficients | `294_LOCAL_DENSITY_NOT_BAD_SET_ANTI_CONCENTRATION_NO_GO.md` |
| Bounded density bad-set zero coefficient | Shows bounded absolutely continuous density contributes only \(O(1)\) to Poisson-weighted bad-set mass, so the logarithmic obstruction lies in the non-bounded remainder | `295_BOUNDED_DENSITY_BAD_SET_ZERO_COEFFICIENT_GATE.md` |
| Log-kernel Abel-defect model ledger | Computes the exact leading scaling constant \(\kappa_\alpha\) for \(\int(P_{1-1/n}-\alpha F_n)_+L\,dm=\kappa_\alpha\log n+o(\log n)\), isolating the residual Euler--Gamma anti-concentration still needed | `312_LOG_KERNEL_ABEL_DEFECT_MODEL_LEDGER.md` |
| Log-kernel defect optimization ledger | Shows the pure log-kernel defect leaves positive leading budget; near \(\alpha=3/4\), the model margin is about \(0.2729644367\), so only the remnant bad-set mass remains obstructive | `315_LOG_KERNEL_DEFECT_OPTIMIZATION_LEDGER.md` |
| Euler--Gamma remainder bad-set certificate | Gives the effective closure schema for \(d\nu_g=aL\,dm+d\rho\): certify the log-kernel defect and a direct or weighted bad-set bound for \(\rho\) so \(a\kappa_\alpha^+ + e_\alpha<1-\alpha/2\), then use `291` and `261` | `325_EG_REMAINDER_BAD_SET_CERTIFICATE_SCHEMA.md` |
| Poisson lower not log domination no-go | Shows logarithmic Poisson lower bounds at \(1\) do not imply measure domination \(\nu\ge aL\,dm\); the Fejer decomposition is a separate theorem or must be replaced by a direct defect bound | `328_POISSON_LOWER_NOT_LOG_DOMINATION_NO_GO.md` |
| Direct A1 termwise sign obstruction | Shows the direct prime-power certificate is not coefficientwise positive; high-block coefficients inherit Laguerre oscillation, so direct A1 requires signed global compensation | `313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md` |
| Laguerre lobe block-compensation gate | Partitions the direct high-block certificate into sign lobes and shows A1 requires the oriented block inequality \(H_n^+-H_n^-+B_n^{base}\ge0\), not absolute lobe control | `298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md` |
| Lobe-block partial summation gate | Converts each direct sign-lobe block into a main term plus signed Chebyshev-error integral, so the remaining theorem is the oriented discrepancy inequality over lobes | `299_LOBE_BLOCK_PARTIAL_SUMMATION_GATE.md` |
| Direct A1 oriented Chebyshev minimal theorem | States the exact remaining direct theorem \(\sum_jH_{n,j}^{err}\ge-B_n^{base}-\sum_jH_{n,j}^{main}\) and rules out the monotonicity shortcut for sign-changing Laguerre lobes | `329_DIRECT_A1_ORIENTED_CHEBYSHEV_MINIMAL_THEOREM.md` |
| Tail-lobe one-sided envelope criterion | Gives a sufficient pointwise tail theorem: lower envelopes on positive Laguerre tail lobes and upper envelopes on negative lobes certify \(I_n(T_n)\ge(d_n-1/4)A_n\) | `320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` |
| Tail-lobe interval certificate schema | Specifies the rigorous interval data needed to certify the `320` lobe criterion at each index or above an effective threshold | `322_TAIL_LOBE_INTERVAL_CERTIFICATE_SCHEMA.md` |
| Tail-lobe step-envelope effective reduction | Reduces bounded-lobe Chebyshev envelopes to finite prime-power endpoint extrema and isolates the final-ray one-sided weighted theorem as the remaining infinite input | `326_TAIL_LOBE_STEP_ENVELOPE_EFFECTIVE_REDUCTION.md` |
| Final-ray absolute cost gate | Allows a symmetric PNT/VK envelope only on the final tail ray as an explicit negative cost after bounded lobes have been certified arithmetically | `327_FINAL_RAY_ABSOLUTE_COST_GATE.md` |
| Direct/tail lobe transfer gate | Shows compact direct lobe dominance and tail lobe dominance are equivalent only through the full compact identity; \(\omega_n'=K_n\) is not a positive transfer | `321_DIRECT_TAIL_LOBE_TRANSFER_GATE.md` |
| Poisson-to-Fejer positive inverse no-go | Shows Abel/Poisson lower bounds cannot imply Fejer lower bounds through a positive inverse kernel, since \(F_N\) has moving zeros and Poisson kernels are strictly positive | `270_POISSON_TO_FEJER_POSITIVE_INVERSE_NO_GO.md` |
| Positive increment versus Fejer mass separation | Shows \(\nu_g\ge0\) gives global Li positivity through \(2\lambda_n=n\int F_n\,d\nu_g\), but compact A1 additionally requires the quantitative lower bound \(\int F_n\,d\nu_g\ge A_n/n\), i.e. local logarithmic mass with \(1/2<a\le1\) or an equivalent Fejer theorem | `271_POSITIVE_INCREMENT_FEJER_MASS_SEPARATION.md` |
| Fejer mass localization necessary gate | Uses \(F_n(e^{i\theta})\le\min(n,\pi^2/(n\theta^2))\) to show any compact Fejer lower bound requires logarithmic localized mass near \(\zeta=1\) | `272_FEJER_MASS_LOCALIZATION_NECESSARY_GATE.md` |
| Fejer layer-cake distribution gate | Rewrites the Fejer mass requirement as \(\int_0^n\nu_g\{F_n\ge t\}\,dt\ge A_n/n\), unifying local-density and Abel-defect routes as distribution lower bounds | `273_FEJER_LAYER_CAKE_DISTRIBUTION_GATE.md` |
| Abel spike versus Fejer zero model no-go | Constructs a finite positive measure with logarithmic Poisson spikes at \(r_{N_j}=1-1/N_j\) but bounded matching Fejer tests, proving radial \(\mathcal G_+\)-scale data do not force Fejer margin or local log-density | `281_ABEL_SPIKE_FEJER_ZERO_MODEL_NO_GO.md` |
| RDI bridge | Minimal theorem stated; not proved | `102_RDI_TO_LI_MINIMAL_BRIDGE.md` |
| Li assembly | Conditional theorem proved | `102_LI_ASSEMBLY_CONDITIONAL_THEOREM.md` |
