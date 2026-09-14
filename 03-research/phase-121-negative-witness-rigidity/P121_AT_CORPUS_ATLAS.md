# The `A_T` corpus atlas

## Status

This is a notation and mechanism audit, not a new positivity claim.
The corpus-wide search found 135 files containing an `A_T`-type spelling.
After removing the phase-116 snapshot of phase 114 and all phase-116 output
drafts, 93 canonical/live files remain.  The output drafts are not discarded
mathematically: in particular, the unique v109--v131 Witt-word and rational-
leakage campaign is included explicitly in Sections 3.8 and 4 below.  A second
semantic search for localized Weil
forms, primitive operators, first loss, first contact, least eigenvalues and
global squares finds further neighbours which do not use the symbol `A_T`.

The decisive fact is that the symbol has been reused for several different
objects.  The atlas below fixes the notation and prevents another apparent
mechanism from being manufactured by moving between those meanings.

## 1. Canonical notation

Write

\[
 \mathscr A_T=
 G_{\Gamma,T}-m_0I-
 \sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       (S_{\log n}+S_{-\log n})                       \tag{1.1}
\]

for the complete localized Weil operator before primitive compression, and
write

\[
 \Delta_T=P_T\mathscr A_TP_T                         \tag{1.2}
\]

on the two-Tate primitive space

\[
 \mathcal P_T=\ker M_+\cap\ker M_-.
\]

This is the object called `A_T` in paper 42, phase 118 and most of phase 120.
With the sign convention of paper 42,

\[
 \langle\Delta_TF,F\rangle=-B_{\rm nuc,T}(F,F),
 \qquad F\in\mathcal P_T.                            \tag{1.3}
\]

Thus row (d) is exactly

\[
 \Delta_T\succeq0\quad\hbox{for every }T>0.          \tag{1.4}
\]

No other object in this note will be denoted by `A_T`.

## 2. The notation collisions

| old spelling | object | canonical spelling here | warning |
|---|---|---|---|
| `A_T` in paper 42 / phase 118 | localized Weil operator | `mathscr A_T` | its primitive sign for all `T` is row (d) |
| `A_T=Y_TR_T^{-1/2}` in D.137--D.138 | comparison operator | `C_T` | `||C_T||<=1` is equivalent to the desired sign |
| `A_T=sum c_(p,k)` in D.55/D.58/D.68/D.132 | scalar prime mass | `a_T` | it is not an operator |
| `A_T=P_TM_(W_T)E_T` in D.206/D.208 | flat action map | `F_T^flat` | it is one block used in an endpoint certificate |
| `A_T^+-A_T^-` in D.163/D.165 | weighted prolate pair | `W_T^+-W_T^-` | positivity of the comparison is the open depth inequality |
| `A_T=K_(g,T)|_(H_T^0)` in D.53 | screw-kernel realization | `K_T^0` | its inertia is another presentation of the primitive sign |
| `A_T` in phase 72 | a CFIR row multiplier or zero window | retain local name | unrelated to the localized Weil operator |

This collision explains several false impressions of progress.  For example,
constructing the comparison operator `C_T` is easy on the range of the positive
bank; proving it is contractive is (1.4).  Likewise, positivity of either
weighted prolate compression separately says nothing about the sign of their
difference.

## 3. Exact atlases of the same form

The following identities are all established in the corpus.  They are useful
coordinates, but none supplies a sign by itself.

### 3.1 Explicit-formula coordinate

Phase 118 proves, on the real primitive core,

\[
 \langle\Delta_TF,F\rangle
   =\sum_\rho \widehat F(\gamma_\rho)
                    \widehat F(-\gamma_\rho).        \tag{3.1}
\]

Consequently (1.4) for every `T` is the Weil criterion, not an intermediate
estimate.

### 3.2 Balanced-bank coordinate

D.114.e.01 and paper 42 prove

\[
 \mathscr A_T=R_T-L_T=X_T^*X_T-Y_T^*Y_T.             \tag{3.2}
\]

Phase 120 eliminates the local Euler bank and obtains an exact reduced version
of (3.2).  The remaining transmission residual is zero exactly when the
chosen source-defined comparison maps the positive bank to the negative one.
Constructing that comparison by Douglas' lemma is equivalent to (1.4).

### 3.3 Signed Green coordinate

Phase 120 proves on the common core

\[
 \mathscr A_T=E_T^*(K_T^*QK_T-Q)E_T.                 \tag{3.3}
\]

This closes the Green identity without residue.  Since `Q` is signed, (3.3)
is a conservation law, not a positive square.

### 3.4 Unified jump coordinate

The Gamma spectrum and every prime-power contact form one positive jump map
`J_T`, with

\[
 \langle\mathscr A_TF,F\rangle
       =\|J_TF\|^2-c_T\|F\|^2.                       \tag{3.4}
\]

An independently constructed contraction from `J_TF` to
`sqrt(c_T)F` would prove the sign.  Existence of some such contraction is again
Douglas-equivalent to (1.4).  The fixed-cutoff Cheeger/Poincare version has
zero expansion and the raw scalar deficit has leading order.

### 3.5 Wigner--Smith / scattering coordinate

Phase 115 identifies the primitive compression of a logarithmic scattering
delay with `Delta_T`.  Positivity of the delay, passivity of the required
transfer, or contractivity of its Julia operator is precisely the missing
sign unless the transfer is constructed from a separate source law.

### 3.6 A--B--C and jet coordinate

D.202 proves the exact pullback of the geometric A--B--C source form and
identifies its two ruling moments with the two Tate characters.  After the
pullback the remaining assertion is

\[
 P_{\ker J_T}\mathscr A_TP_{\ker J_T}\succeq0.       \tag{3.5}
\]

The source comparison is complete; the Hodge sign is not supplied by it.

### 3.7 Schur / output-defect coordinate

D.170 and D.114.e.01 reduce every threshold step to a unit output-capacity
condition.  Phase 116 records the source Schur angle and the physical output
defect.  Their signs are exact Schur complements of (1.2); proving a uniform
angle bound is another sufficient estimate for (1.4), not a new source of
sign.

### 3.8 Witt-word / rational-leakage coordinate

The phase-116 v109--v131 drafts already carry labelled words past the first
scalar contact.  They prove the fixed-depth Witt asymptotics, the two-
orientation word Gram, the newborn label-to-delay isometry, the exact
cross-only incidence column, the Gamma state pullback, the moving Tate states
and the aggregation on reduced rational labels.  The remaining sufficient
estimate was named `URGT_1`:

\[
 \|L_Ne\|^2\le \mathcal E_{\Gamma T,N}(e)             \tag{3.6}
\]

uniformly in every threshold cell and every admissible profile.  Its scalar
expansion and conditional cascade to row (d) are exact.  The estimate is open,
was not shown necessary for row (d), and the minimizer strategy stops at
uniform observability in moving arithmetic holes.  The v114 no-go also proves
that equality of the word Grams cannot turn the physical minus port into the
plus port: their primitive zeroth-order Grams differ.

## 4. What has already been tried on `mathscr A_T`

The corpus has already developed the operator through the following families.

1. **Direct coercivity and finite Schur complements.**  These give the full
   infinite-dimensional theorem for `0<T<=log 2`.  They do not form a cofinal
   mechanism, and the scalar comparison loses at leading order.
2. **Threshold and moving-window flows.**  Exact nesting makes the bottom of
   the spectrum nonincreasing.  The crossing form is an unsigned translated
   autocorrelation; prime births can move inertia in both directions.
3. **Pontryagin inertia and two Tate jets.**  The two boundary jets form a
   hyperbolic plane.  Inertia formulas type the desired Hodge theorem but do
   not exclude the additional bad direction.
4. **Gamma gaps, weighted prolate depth and Markov/Cheeger estimates.**  The
   separate positive pieces do not preserve the sharp cross-place
   cancellation.  Suzuki's unshifted positive metric requires the sign being
   proved.
5. **Balanced factorizations, Douglas contractions, Julia colligations and
   scattering.**  The positive banks are explicit.  Contractivity or exact
   intertwining carries the whole content of row (d).
6. **Fredholm determinants and Birman--Schwinger transforms.**  The natural
   resolvent is not trace class at the required level; where a determinant is
   defined, its no-zero assertion is the same first-crossing exclusion.
7. **Per-place, rank-one and tensor decompositions.**  They lose the
   cross-place Green phase or have the wrong local rank.  Positivity is not a
   sum of independent placewise signs.
8. **Hodge, Rosati, moment-map and stability packages.**  They correctly type
   the desired sign.  Their mixed-source/support clause is the primitive
   inequality itself, and the finite signature has no automatic persistence.
9. **Commutator, Mourre, virial and dilation arguments.**  The available
   commutators are unsigned or have zero diagonal on an eigenvector.  A strict
   estimate would already exclude the spectral subspace it is meant to rule
   out.
10. **Exact Green, Poisson, co-Poisson, Abel, Hardy, Sonin and boundary
    identities.**  They determine the common germ and the symmetric boundary
    component.  They do not select the physical causal orientation or kill
    the antisymmetric incoming current.
11. **Finite endpoints and numerical spectral atlases.**  They can prove one
    fixed window but cannot establish (1.4) cofinally.  Criticality forces the
    lower spectral margin toward zero even if RH is true.
12. **Square roots, source metrics and completed connections.**  Any bounded
    solution of the corresponding Lyapunov/Sylvester equation blows up as a
    first contact is approached unless that contact is already excluded.
13. **Witt words, Fock reservoirs and correlated rational leakage.**  The
    word labels, all-depth return budget and physical delay synthesis have
    already been constructed.  Their terminal `URGT_1` domination is an open
    uniform inequality; the nearly constant profile is excluded, but the
    mean-zero moving-hole observability remains.  Rebuilding a labelled word
    Gram is therefore not a new route.

This list subsumes the routes in phases 114--120 and the relevant obstruction
ledger in paper 36.  A future proposal which lands in one of these twelve rows
is not new merely because its ambient category has changed.

## 5. The first-contact normal form

The certified initial interval and exact nesting give the only useful
contradiction setup.  If global positivity fails, there is a first parameter
`T_*` and a nonzero `F_* in P_(T_*)` such that

\[
 P_{T_*}\mathscr A_{T_*}F_*=0,                       \tag{5.1}
\]

or equivalently

\[
 \mathscr A_{T_*}F_*
   =\alpha e^{-t/2}+\beta e^{t/2}.                   \tag{5.2}
\]

Every global-square construction in the atlas either proves directly that
(5.1) has no nonzero solution or builds a positive object whose existence is
equivalent to that fact.

The phase-116 v94 audit reduced exclusion of (5.1) to the local annular arrow

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \mathfrak S_T^{\rm loc}F=0
       \text{ on }(e^{-T},e^T),                      \tag{5.3}
\]

because the local causal observation is `I+K_(T,+)` with nilpotent `K_(T,+)`
and hence an explicit finite Neumann inverse.  Thus (5.3) immediately gives
`F=0`.

Equation (5.3) is not a statement that the global co-Poisson observation is
undefined.  Phase 121 now proves:

* every first-contact vector lies in `H^s` for every `s<1/2`;
* it belongs to the maximal co-Poisson graph domain;
* the zeta observation and Gamma logarithmic generator strongly commute on
  their common product for that vector;
* the Abel white-light slope exists and equals
  `2||zeta(1/2+i.) Fhat||^2`;
* conservation, Real parity and the two Tate moments do not by themselves
  force the remaining boundary current to vanish.

Accordingly roughness, lack of a global observation and a formal commutator
domain are no longer possible explanations for the missing arrow.

## 6. Exact surviving gap after the audit

The search does not reveal another undeveloped model of `mathscr A_T`.  It
reveals one undeveloped **type of information**:

> an Euler-specific equality law for a first-contact vector which chooses the
> physical causal orientation and annihilates its incoming annular current,
> without being obtained by applying, conjugating, factoring, shorting or
> differentiating the equation `P_T mathscr A_T F=0`.

In the existing notation this is (5.3), equivalently the critical-port
implication v94 (700), equivalently vanishing of the negative port on the
first-loss kernel.  Phase 121's two-border no-go proves that a linear
conservation law cannot do it.  The missing input must therefore be a
source-level nonlinear equality case of the Euler product which survives the
scalar row-(c) trace and retains the cross-prime phase.

That is narrower than “construct a global square.”  Once such a law proves
(5.3), the already constructed nilpotent local inverse excludes first contact;
exact nesting then gives `Delta_T>=0` for every `T`, and the cofinal passage to
row (d) is already available.

## 7. Binding consequence for phase 121

Do not develop another representation of `mathscr A_T`.  In particular, do
not restart a balanced bank, contraction, scattering delay, Schur angle,
positive metric, Hodge package, determinant, commutator, finite endpoint,
co-Poisson domain construction, Witt-word Gram or rational-leakage domination.

The next admissible construction must act **before** the scalar trace which
forms (1.1), must retain labelled prime words long enough to obtain a
nonlinear equality law, and only then descend that equality to the physical
annular current.  Its kill condition is independent: if the proposed
source-level law is already a consequence of (5.1), or if it does not survive
the row-(c) trace, it is rejected before any global-square claim.
