# A1 gate implication graph

## Purpose

This document records the exact implication relations between the current A1
gates.  Its role is bookkeeping: it prevents the proof search from counting
the same missing sign theorem several times under different coordinates.

## Central objects

For \(n\ge8\), put
\[
  A_n=\lambda_n^{\rm arch}>0
\]
and
\[
  K_n(T)
  =
  -n+\int_1^{e^T}(\psi(y)-y)f'_{n,0}(y)\,dy.
\]

The present compact target is
\[
  K_n(T_n)+{3\over4}A_n\ge0.
\tag{A1}
\]

The full Li target is
\[
  \lambda_n= A_n+\lambda_n^{\rm prime}\ge0
  \qquad(n\ge1).
\tag{Li}
\]

The positive boundary measure target is the construction of a positive
symmetric measure in the line coordinate for
\[
  {\xi'\over\xi}\left({1\over2}+z\right),
\]
with support on the imaginary axis in that coordinate.

## Proven implication chain

The documents in this phase establish the following formal chain.

\[
\begin{array}{c}
\hbox{positive boundary measure}\\
\Downarrow\\
\hbox{critical-line support of the divisor}\\
\Downarrow\\
\lambda_n\ge0\quad(n\ge1)\\
\Downarrow\\
\Omega_7.
\end{array}
\]

The first implication is proved by the singularity support of the Cauchy
transform: a representation with singularities only on the imaginary axis
forces every pole of \(\xi'/\xi\) in the line coordinate to lie there.

The second implication is the paired Li sum-of-squares formula on the
critical line.

The third implication is only terminology: \(\Omega_7\) is the Li positivity
statement.

## A0 plus A1 chain

The direct compact route has a separate chain.

\[
\begin{array}{c}
\hbox{finite certificate for }1\le n\le7\\
+\hbox{ A0 tail estimate}\\
+\hbox{ A1 compact sign}\\
\Downarrow\\
\lambda_n\ge0\quad(n\ge1)\\
\Downarrow\\
\Omega_7.
\end{array}
\]

This is the assembly theorem already recorded in the phase.  The only open
item in this chain is A1.

## Strong margin gate

The strong margin theorem
\[
  \lambda_n\ge {1\over2}A_n\qquad(n\ge8)
\tag{SM}
\]
implies A1 together with the A0 budget
\[
  |R_n(T_n)|\le {1\over4}A_n.
\]

Indeed,
\[
  K_n(T_n)+{3\over4}A_n
  =
  \lambda_n-R_n(T_n)-{1\over4}A_n
  \ge
  {1\over2}A_n-{1\over4}A_n-{1\over4}A_n
  =
  0.
\]

Thus
\[
  \hbox{SM}+\hbox{A0}\Longrightarrow\hbox{A1}.
\]

But SM is strictly stronger than the Li lower bound in the prime split:
\[
  \lambda_n^{\rm prime}\ge -{1\over2}A_n
\]
instead of merely
\[
  \lambda_n^{\rm prime}\ge -A_n.
\]

Therefore SM is a valid route but not a simplification already justified by
the existing phase.

## One-sided tail gate

A one-sided tail theorem would prove
\[
  R_n(T_n)\le \lambda_n-{1\over4}A_n.
\]

Substituting this into
\[
  K_n(T_n)+{3\over4}A_n
  =
  \lambda_n-R_n(T_n)-{1\over4}A_n
\]
gives A1 immediately.

However, unless the right side is bounded without using \(\lambda_n\), this
is a restatement.  A useful one-sided tail theorem must give a signed
Euler--Gamma upper bound for \(R_n(T_n)\) that survives the paired boundary
limit.

## Coordinate routes

The following routes all imply the positive boundary measure target if their
non-tautological core is proved:

- Hermite--Biehler or de Branges construction from Euler--Gamma data;
- infinite total positivity or Pick/Stieltjes positivity of the transformed
  Li generating function;
- fixed-cutoff compact coefficient positivity together with a uniform
  admissible cutoff, a positive moving-cutoff transform, or a separate
  one-sided tail theorem;
- non-tautological bordered current with positivity proved before the Schur
  complement is identified with \(C_n\);
- Mellin coborder identity whose symmetrized boundary form is positive
  before the zero-side interpretation is used.

In each case, the algebraic identity part is already normalized in phase 102.
The missing part is the same kind of positivity-preserving continuation from
the Euler-product region to the Li boundary.

## Non-implications

The following implications are not proved and must not be used:

1. A0 alone implies A1.
2. A finite positive matrix model implies A1 without an independent
   cofinal identification.
3. Finite total positivity of initial Li coefficients implies Omega7.
4. Riesz positivity of \(\log|\xi|\) implies support on the critical line.
5. A contour shift of the Mellin normal form implies positivity merely from
   the functional equation.
6. A Schur complement identity implies nonnegativity of the complement.
7. Positivity of coefficients for one fixed compact cutoff implies A1 with
   the moving A0 cutoffs \(T_n\).
8. The A0 sufficient condition supplies a finite universal cutoff for all
   \(n\).

Each false implication is an eliminated proof class, not a reason to abandon
the corresponding non-tautological theorem.

## Current exact load

After all reductions, the remaining proof load can be stated in any one of
the following equivalent-or-stronger forms:

1. prove A1 directly;
2. prove the strong margin SM;
3. prove a useful one-sided tail theorem;
4. construct the positive boundary measure;
5. construct an Euler--Gamma Hermite--Biehler function;
6. prove infinite Pick/Stieltjes positivity for the Li generating transform;
7. prove a non-tautological positive bordered current;
8. prove positivity of the symmetrized Mellin boundary form.
9. prove a coefficient-positive fixed-cutoff or moving-cutoff compact
   transform that also accounts for the A0 dependence \(T_n\).
10. prove a coefficient-positive theorem for the exact prime-pole generator
    after the pole-prime pairing, which by `141_PRIME_POLE_INTEGRAL_GENERATOR.md`
    is precisely the same signed Laguerre/A1 coefficient problem.
11. prove the adjacent Laguerre-lobe compensation theorem in
    `144_LAGUERRE_CORE_SIGN_PARTITION.md`, after the derivative kernel is
    collapsed to \(L_{n-1}^{(2)}\).
12. prove the Euler--Gamma coercive Schur lemma in
    `142_A1_VARIATIONAL_ENERGY_FORM.md`, so that A1 is the minimum of a
    nonnegative affine quadratic energy.
13. prove the completed Pick/Stieltjes boundary-support theorem isolated in
    `143_PRIME_POLE_PICK_STIELTJES_GATE.md`.
14. prove the signed dual lobe balance theorem in
    `145_LAGUERRE_LOBE_DUAL_BALANCE.md`, controlling the cumulative
    prime-pole balance against Laguerre-lobe variation.
15. prove one of the raised-balance inequalities in
    `146_RAISED_LAGUERRE_DUAL_HIERARCHY.md`, where \(B_r\) is controlled
    one-sidedly against \(L_{n-1}^{(2+r)}\) including all endpoint terms.
16. prove the finite signed Laplace-jet inequality in
    `147_BALANCE_LAPLACE_JET_FORM.md` for \(\mathcal B_{r,T_n}\) at
    \(s=1\).
17. prove a uniform signed estimate for the explicit finite arithmetic
    certificate in `148_A1_FINITE_ARITHMETIC_CERTIFICATE_SCHEMA.md`.
18. prove moving-diagonal coefficient positivity for the family
    \(\mathcal C_T(z)\) in `149_MOVING_DIAGONAL_A1_GENERATOR.md`.
19. prove either the strong-margin theorem or a genuinely one-sided tail
    theorem in the exact sign convention of
    `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`.
20. prove the signed cutoff-transfer inequality in
    `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md`, allowing positivity at
    an auxiliary cutoff to move to the A0 cutoff \(T_n\).
21. prove the dual accumulated cutoff-transfer inequality in
    `154_CUTOFF_TRANSFER_DUAL_BALANCE.md`.
22. construct the positive Weil square-root/autocorrelation factorization
    isolated in `155_A1_WEIL_SQUARE_ROOT_GATE.md`.
23. prove the signed forcing bounds required by the Laguerre \(n\)-recurrence
    in `156_A1_LAGUERRE_N_RECURRENCE_GATE.md`.
24. prove the full signed forcing bound left by the corrected archimedean
    audit in `157_ARCHIMEDEAN_FORCING_AUDIT.md`.
25. prove the Euler--Gamma trigonometric moment theorem in
    `162_LI_FEJER_TRIGONOMETRIC_MOMENT_GATE.md`: nonnegativity on every
    squared trigonometric polynomial, equivalently on all translated Fejer
    means, not merely on scalar Cesaro tests or finite subfamilies.
26. prove the completed prime-pole Fejer support theorem in
    `163_PRIME_POLE_FEJER_TOEPLITZ_SUPPORT_GATE.md`, with moments constructed
    from completed Euler--Gamma data and singularities identified
    non-circularly.
27. prove the Toeplitz Schur margin theorem in
    `164_A1_TOEPLITZ_SCHUR_MARGIN.md`: the Li-test margin
    \(Q_n(1-z^n)\ge A_n\), or the stronger innovation margin
    \(\sigma_n\ge A_n\), for all \(n\ge8\).
28. prove the completed Poisson/Carathéodory theorem in
    `165_POISSON_CARATHEODORY_POSITIVITY_GATE.md`:
    \(\Re H_{\rm EG}(z)\ge0\) for \(|z|<1\), with non-circular singularity
    identification.
29. prove the sharpened Poisson support theorem in
    `166_POISSON_CARATHEODORY_SUPPORT_GATE.md`: the same real-part
    positivity plus exact transformed-zero singularities, and, for compact
    A1 after A0, the square margin \(Q_n(1-z^n)\ge A_n\).
30. construct the renormalized positive Euler--Gamma moment object required
    by `167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md`, since a finite
    Herglotz measure cannot naively represent the unweighted infinite Li
    zero divisor.
31. construct the positive vanishing-test kernel of
    `168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md` on
    \((z-1)\mathbb C[z]\), with
    \(\mathfrak Q(1-z^n,1-z^n)=2\lambda_n\) or the stronger A1 margin.
32. prove the Li Schoenberg kernel positivity of
    `169_LI_SCHOENBERG_VANISHING_KERNEL.md`:
    \[
      [\lambda_j+\lambda_k-\lambda_{|j-k|}]_{1\le j,k\le N}\ge0
    \]
    for every \(N\), from Euler--Gamma data rather than boundary support.
33. avoid the direct functional-equation cross-pairing eliminated by
    `170_VANISHING_KERNEL_PAIRING_NO_GO.md`: it recovers the Li square, but
    on a non-fixed orbit \(w\mapsto1/\overline w\) its local matrix is
    indefinite, so positivity requires new Euler--Gamma terms, direct
    Schoenberg positivity, or an independent support theorem.
34. avoid orbitwise positive counterterms eliminated by
    `171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md`: if such a counterterm
    preserves all local Li-test values, it must vanish, so any repair must be
    genuinely new.  The same file rules out every positive global
    counterterm invisible on all Li diagonals; a viable construction cannot
    be the old cross-pairing plus a nonzero positive invisible patch.
35. prove the increment Toeplitz theorem of
    `172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md`:
    \[
      [g_{|j-k|}]_{1\le j,k\le N}\ge0,\qquad
      g_0=2\lambda_1,\quad
      g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
    \]
36. prove the completed weighted-divisor theorem of
    `173_WEIGHTED_ZERO_DIVISOR_MEASURE_GATE.md`: the \(g_m\) are positive
    finite boundary moments with exact transformed-zero singularities,
    without assuming \(|w_\rho|=1\).
37. prove the half-plane log-derivative positivity theorem of
    `174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md`:
    \[
      \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
    \]
38. use `175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` as the exact logical status
    of that gate: it is equivalent to RH, so it is a closure route but not a
    simplification.
39. prove the horizontal modulus monotonicity theorem in
    `176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md`:
    \[
      \partial_\sigma\log|\xi(\sigma+it)|\ge0
      \qquad(\sigma>1/2).
    \]
40. extend the unconditional positivity region of
    `177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md` from \(\Re s>1\) to the
    full strip \(1/2<\Re s\le1\).
41. avoid the circular strip-Poisson inference eliminated by
    `178_STRIP_POISSON_BOUNDARY_NO_GO.md`: favorable vertical boundary
    signs imply interior positivity only after zero-freeness in the strip is
    already known.
42. account for the pole defects isolated in
    `179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md`: every off-line zero in
    the right half strip contributes \(m\Re(s-\rho)^{-1}\), with a negative
    lobe that cannot be dropped from Green's formula.
43. use the explicit strip Poisson kernel of
    `180_STRIP_POISSON_KERNEL_FORMULA.md` only conditionally: it proves
    positivity from boundary signs after zero-freeness in the strip has
    already been established.
44. keep the load separation of
    `181_GLOBAL_POSITIVITY_VS_COMPACT_A1_MARGIN.md`: global RH/Li positivity
    closes Omega7, but compact A1 needs an additional margin, one-sided
    tail, or direct signed-core proof.
45. use `189_GLOBAL_LOG_DERIVATIVE_TO_COMPACT_A1_AUDIT.md` as the exact
    bridge audit: global log-derivative positivity gives
    \(\lambda_n\ge0\), while compact A1 is equivalent to
    \(\lambda_n\ge R_n(T_n)+\frac14\lambda_n^{\rm arch}\).  With A0 alone,
    the missing extra input is a one-sided tail theorem, the strong margin
    \(\lambda_n\ge\frac12\lambda_n^{\rm arch}\), or direct A1.
46. use `192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md` to avoid a
    false tail inference: global Toeplitz/Schoenberg positivity gives
    \(\lambda_n\ge0\), but it does not imply
    \(R_n(T_n)\le\lambda_n-\frac14\lambda_n^{\rm arch}\).  That inequality
    is A1 itself in tail coordinates unless a new margin/comparison theorem
    is proved.
47. use `195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` as the exact
    comparison target: prove
    \(\mathfrak Q^{\mathcal L}-\frac14\mathfrak Q^{\mathcal A}
    -\mathfrak Q^{\mathcal R,T_n}\ge0\) on \(1-z^n\), or a stronger
    finite-subspace Loewner inequality.  Positivity of the global Li form
    alone is not such an order comparison.
48. use `199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` only in the
    non-circular direction: first prove comparative block positivity and a
    nonnegative innovation margin, then infer \(C_n(T_n)\ge0\).  Computing a
    Schur complement after assuming the A1 diagonal sign is only a
    restatement.
49. avoid the horizontal-modulus shortcut eliminated by
    `182_HORIZONTAL_ZERO_BARRIER_NO_GO.md`: symmetry, subharmonicity, bounded
    boundary averages or bounded correction terms cannot overcome the local
    barrier \(m\log|\sigma-\beta|\) created by an off-line zero.  A proof of
    monotonicity must exclude the zero or neutralize it by a genuinely
    singular Euler--Gamma mechanism.
50. prove the exact cumulative forcing inequalities of
    `183_EXACT_CUMULATIVE_FORCING_REPRESENTATION.md`, plus moving-cutoff
    transfer, if using the Laguerre induction route.
51. or prove directly the diagonal forcing inequality of
    `184_MOVING_DIAGONAL_RECURRENCE_DEFECT.md`, where the forcing includes
    the two cutoff-transfer defects on the A0 diagonal.
51. prove the one-kernel diagonal forcing lower bound of
    `185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md`, including the cumulative
    weights from `183`.
51. prove the cumulative-kernel inequality of
    `186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md`, where the full diagonal
    induction load is one signed pairing against \(\mathcal H_n\).
52. after `188_DIAGONAL_CUMULATIVE_COERCIVITY_AUDIT.md`, do not count a
    two-sided envelope for \(E\) as a coercive diagonal theorem: the exact
    variational infimum is the absolute-value bound.  A viable diagonal
    proof must give one-sided arithmetic alignment or show that the explicit
    absolute bound is small enough.
53. if using the absolute route audited in
    `191_ABSOLUTE_DIAGONAL_BUDGET_SCALE_AUDIT.md`, prove the uniform scale
    inequality
    \[
      \mathcal B_n\ge
      \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du
      \qquad(n\ge9)
    \]
    for a declared PNT envelope \(R\).  Otherwise return to the signed
    finite arithmetic certificate.
54. `193_WEIGHTED_L1_KERNEL_CERTIFICATE.md` refines that absolute route to
    a finite sign-partition problem over the zeros of the piecewise
    polynomial cumulative kernel \(\mathcal H_n\).  A proof still needs
    uniform domination of the resulting weighted \(L^1\) load by
    \(\mathcal B_n\).
55. `197_CUMULATIVE_KERNEL_INTERVAL_FORM.md` gives the exact interval
    polynomials for \(\mathcal H_n\).  The terminal interval is
    \(\mathcal H_n=-L_{n-1}^{(2)}\), while earlier intervals are cumulative
    Laguerre mixtures.  Thus standard interlacing for a single Laguerre
    sequence is not a substitute for the weighted \(L^1\) theorem.
56. for the strong-margin route, use
    `194_STRONG_MARGIN_GENERATOR_SECOND_PASS.md`: prove
    \[
      [z^n]\left(\mathcal L-\frac12\mathcal A\right)\ge0
      \qquad(n\ge8),
    \]
    equivalently \(Q_n(1-z^n)\ge\lambda_n^{\rm arch}\).  Bare
    Toeplitz/Schoenberg positivity supplies only \(Q_n(1-z^n)\ge0\).
57. in second-difference coordinates, `198_STRONG_MARGIN_SECOND_DIFFERENCE_AUDIT.md`
    shows that the same margin is
    \[
      n g_0+2\sum_{m=1}^{n-1}(n-m)g_m
      \ge\lambda_n^{\rm arch}.
    \]
    A positive \(g\)-Toeplitz measure must therefore satisfy a quantitative
    Dirichlet/Fejer lower bound, not merely Herglotz positivity.
58. `199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` refines the Loewner--Schur
    comparison into a non-circular innovation condition: prove comparative
    block positivity and a nonnegative innovation before using the diagonal
    identity \(2C_n(T_n)\).
59. `200_FEJER_MASS_STRONG_MARGIN_GATE.md` turns the strong-margin
    second-difference theorem into a quantitative mass requirement near
    \(\zeta=1\).  It is enough to prove
    \[
      \nu_g(|\theta|\le1/n)\ge{\pi^2\over4}
      {\lambda_n^{\rm arch}\over n^2},
    \]
    or the exact bound \(n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}\).
60. `202_FEJER_DENSITY_SCALE_GATE.md` shows that bounded absolutely
    continuous density cannot supply this scale: it gives at most \(O(n)\)
    Fejer energy, while the archimedean margin is \(n\log n\).  A Fejer
    route needs logarithmic or stronger concentration near \(\zeta=1\), or
    a singular component.
61. `203_ATOM_AT_ONE_INCOMPATIBILITY_AUDIT.md` removes the atom at
    \(\zeta=1\) as a compatible shortcut: it would force
    \(\lambda_n\) to have a quadratic component and \(\mathcal L(z)\) to
    have a cubic pole, contrary to the Euler--Gamma generator scale.
62. `204_LOG_DENSITY_INCREMENT_GENERATOR_GATE.md` identifies the remaining
    compatible Fejer scale: the increment generator
    \(\mathcal G_+(z)=\lambda_1+\xi'/\xi(1/(1-z))\) has logarithmic
    boundary growth.  A lower logarithmic boundary-density theorem is still
    required; the upper scale alone does not prove the margin.
63. `201_TERMINAL_LAGUERRE_LOAD_GATE.md` isolates a necessary terminal
    condition for the absolute diagonal route:
    \[
      \mathcal B_n\ge
      \int_{T_{n-1}}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
    \]
    If this fails for a proposed envelope/cutoff system, the absolute route
    fails before the earlier mixed intervals are considered.

The universal-cutoff subgate is audited separately: the current A0 theorem
cannot provide such a cutoff.  Any universal-cutoff proof must therefore be
signed and independent of the absolute A0 estimate.  The moving-cutoff
subgate is also normalized: the cutoff dependence is exactly a
boundary-current integral, and its missing input is a one-sided lower bound
for that current.

The strong-margin and tail gates also have coefficient forms.  The
strong-margin generator is a direct modification of the Li generating
function.  The tail generator is only coefficientwise or Abel-side under the
current A0/PNT input; it cannot be used as a full-disk holomorphic function
without an additional signed continuation theorem.

`196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md` is now the canonical list of
the surviving exact closure theorems.  Any route not proving one of those
statements, or the global half-plane theorem, remains an equivalent normal
form or a sufficient condition still missing its main inequality.

The full pole-paired prime generator has now been identified exactly with
the Laguerre integral against \(\psi(y)-y\).  Thus coefficient positivity of
that generator is not a separate shortcut: after splitting at \(e^{T_n}\),
it is A1 plus the already budgeted A0 tail.

The compact Laguerre kernel has also been reduced to a single polynomial:
\[
  {d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)=-L_{n-1}^{(2)}(u).
\]
Therefore every local compact proof must prove an alternating compensation
law across the canonical lobes cut out by the zeros of \(L_{n-1}^{(2)}\), or
else use one of the global gates above.

The variational route is normalized in Schur--Friedrichs form: the Schur
complement identity is automatic, and only coercivity of the completed
Euler--Gamma energy has proof force.  Likewise, the Pick/Stieltjes route is
not supplied by the raw prime measure; after pole pairing it requires a
completed positive boundary-support theorem.

The lobe route also has a dual form: once the kernel is collapsed, integrating
the Chebyshev error once gives an exact cumulative balance.  A proof must
show one-sided alignment of this balance with the variation of each Laguerre
lobe, not merely apply an absolute PNT bound to the balance.

The same dual form can be iterated.  Each integration raises the Laguerre
parameter and replaces the Chebyshev error by a smoother cumulative
prime-pole balance \(B_r\).  This creates a hierarchy of equivalent A1
targets; it is not a smoothing proof unless one of the raised balances is
shown to have the required one-sided alignment.

The raised hierarchy also has a finite Laplace-jet form.  Because the raised
Laguerre kernel is a polynomial times \(e^{-u}\), the compact integral is a
finite signed combination of derivatives of the truncated balance transform
\(\mathcal B_{r,T}\) at \(s=1\).  This supplies a coefficient target, not an
automatic positivity theorem.

The jet target can be expanded completely into finite prime-power sums and
endpoint polynomial-exponential blocks.  This gives exact pointwise
certificates for fixed \(n,T,r\), but it closes the phase only after a
uniform signed proof of those finite expressions for every \(n\ge8\).

The same data have a fixed-cutoff generating function.  For fixed \(T\),
ordinary coefficient positivity of \(\mathcal C_T\) is well-defined, but A1
requires the moving diagonal \([z^n]\mathcal C_{T_n}\ge0\).  Any proof using
fixed-cutoff coefficient positivity must therefore supply a universal cutoff,
a one-sided cutoff-flow theorem, or a direct moving-diagonal argument.

The moving diagonal is also exactly
\[
  C_n(T_n)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T_n).
\]
This identity does not prove A1, but it fixes the signs of the two surviving
tail routes: strong Li margin or a one-sided estimate for \(R_n(T_n)\).

For any proof that changes cutoffs, the exact transfer identity is
\[
  C_n(T)-C_n(S)
  =
  -\int_S^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\]
Since both factors change sign, monotonicity in \(T\) is not formal; it is a
new signed lobe theorem.

The cutoff-transfer theorem also has a dual form obtained by integrating the
Chebyshev error once on \([S,T]\).  The resulting inequality uses the local
balance \(B_S\), an endpoint term, and the raised kernel \(L_{n-1}^{(3)}\).
This is equivalent to the transfer gate but gives a sharper target for
one-sided accumulated-balance arguments.

The Mellin/Weil route has the same structure: the linear explicit formula
for the compact A1 test is already known, but positivity requires a
square-root or autocorrelation factorization of the completed test before
any zero-side support statement is invoked.

There is also an induction route in \(n\).  The Laguerre three-term
recurrence gives an exact recurrence for \(C_n(T)\), but the recurrence is
not positivity-preserving unless a signed cumulative lower bound is proved
for its forcing moment.

On the A0 diagonal, the cumulative induction sum can be integrated once
against the accumulated balance \(B(U)=\int_0^U E(e^v)\,dv\).  The exact
formula is not a positivity theorem: it contains a raised piecewise Laguerre
kernel and a finite sum of signed jumps at the cutoffs \(T_j\).  Therefore
the diagonal balance route closes A1 only if the full inequality with those
jump terms is proved.

Expanding that accumulated balance gives the finite certificate
\[
  \mathcal A_n+\Pi_n+
  \sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)\ge0.
\]
This is exactly the diagonal balance condition, not a relaxation.  Its
coefficients are signed, so exposing the prime powers does not by itself
create positivity.

The archimedean part of that forcing is explicit but not sign-free.  Thus
the inductive obstruction is the full forcing
\[
  M_n(T)+1+\frac34D_n^{\rm arch},
\]
not only the prime moment.

`158_A1_GATE_TRIAGE_AND_PRIORITY.md` records the current priority split:
equivalent normal forms should feed either a local arithmetic signed-balance
proof or a global Euler--Gamma positivity theorem.  They are not independent
closures by themselves.

For the local induction target, `159_INDUCTIVE_FORCING_CERTIFICATE_SCHEMA.md`
turns the full forcing into explicit finite prime-power data.  A proof still
needs a uniform signed lower bound for those certificates and moving-cutoff
transfer.

`160_INDUCTIVE_FORCING_GENERATOR.md` packages the same forcing in a
fixed-cutoff generating function.  This converts induction into a weighted
coefficient-sum positivity problem, but it remains fixed-cutoff and therefore
still needs signed transfer to the A0 diagonal.

On the global positivity side, `161_LI_TOEPLITZ_MOMENT_GATE.md` expresses
the disk Schur route as infinite Toeplitz moment positivity.  This is a true
positive-boundary theorem only when all matrix sizes and the non-circular
identification with completed Euler--Gamma data are proved.

In Abel coordinates \(w=z/(1-z)\), the tail is a signed Laplace transform on
\(\Re w\ge0\).  A0 gives convergence of that transform, not positivity of
the underlying signed density.  Therefore Herglotz, Stieltjes or complete
monotonicity conclusions require an additional positivity theorem.

The Fourier-cosine representation of \(\Xi\) gives an ordinary positive
Fourier measure and hence Bochner positive definiteness on the real line.
That is weaker than A1: positive-definite entire functions may have non-real
zeros.  The Fourier route becomes viable only after upgrading Bochner
positivity to infinite total positivity, a Pólya-frequency property, or an
Euler--Gamma Hermite--Biehler theorem.

The Jensen-polynomial route is a concrete version of the same upgrade.  It
closes A1 only at the cofinal level: all required Jensen polynomials must be
hyperbolic with convergence into the Laguerre--Pólya class.  Finite Jensen
checks and fixed-degree asymptotic hyperbolicity do not imply A1.

The heat-flow route is another version of the Laguerre--Pólya gate.  It
closes A1 only if the real-rootedness threshold is proved to be at or below
the original time.  Eventual real-rootedness at later heat times leaves the
same A1 gap open.

The disk Schur route maps zeros by \(w_\rho=1-1/\rho\).  Critical-line zeros
map to the unit circle, while an off-line quartet contributes an exterior
point.  A Schur or Carathéodory proof must construct boundary support on
\(\partial\mathbb D\) from Euler--Gamma data; defining the measure from the
zero divisor assumes the support statement.

The exterior-point obstruction is quantitative: if \(|w|>1\), then
\(\operatorname{Re}(w^n)\) is positive with geometric size along an infinite
subsequence.  The paired Li contribution is therefore negative with
geometric size along that subsequence.  This supplies the common off-line
discriminator for all gates, but it does not prove that zeta has no exterior
point.

The archimedean split cannot absorb such a mode: its contribution is
\(O(n\log n)\), whereas the exterior contribution has size \(c|w|^n\) along
an infinite subsequence.  Hence every successful gate must exclude exterior
points structurally.

For typed finite controls this can be sharpened: a nonzero finite maximal
exterior shell dominates lower-radius shells and the archimedean term along
an infinite subsequence.  For the full zeta divisor, the remaining difficulty
is the infinite support problem: possible infinitely many exterior radii,
limiting shells, and paired summation must be controlled by a support theorem.

The same dominance applies to an isolated exterior radius separated from all
lower exterior radii by a gap.  Therefore any surviving counter-scenario must
involve non-isolated exterior support, accumulation toward the unit circle,
or infinite paired cancellation.

For zeta zeros in the critical strip, the exterior radius satisfies
\[
  |1-1/\rho|^2-1={1-2\beta\over \beta^2+\gamma^2},
\]
so exterior excess tends uniformly to zero as \(|\gamma|\to\infty\).  Hence
any off-line zeta zero produces a finite maximal exterior shell.  The
zero-side infinite-support caveat is therefore removed for zeta; the open
problem is not the zero-side implication but the arithmetic proof of Li/A1
positivity.

Consequently the zero-side criterion is closed in this phase:
\[
  \lambda_n\ge0\quad(n\ge1)
  \Longleftrightarrow
  \hbox{critical-line support}.
\]
The remaining load is to prove the left side from Euler--Gamma data.

On the arithmetic side, the exact coefficient object is
\[
  \mathcal L(z)=z{d\over dz}\log\xi\!\left({1\over1-z}\right)
  =
  \mathcal A(z)+\mathcal P(z),
\]
where \(\mathcal P\) keeps the pole \(1/(s-1)\) paired with
\(\zeta'/\zeta(s)\).  A1 is the compact signed form of coefficient
positivity for this Euler--Gamma generator after A0.

The phase has not yet proved any item in this list.  It has proved the
formal implications from each item to Omega7 and eliminated the circular
versions of the same items.
