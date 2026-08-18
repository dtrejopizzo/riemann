# Row D — master goal and proof programme

## Objective

Prove, without using the zeros of \(\xi\), RH, or the sign of the Weil
form as input,

\[
 Q_T=-B_{{\rm nuc},T}^{\rm prim}\geq0
 \quad\text{for every }T>0,
\]

and pass from the localized statement to

\[
 B_{\rm nuc}(f,f)\leq0
 \qquad(f\in\mathcal T^0).
\]

The equality case, operator domains, supported-range conditions and passage
to the completed form domain are part of the theorem.  Numerical evidence is
never a substitute for any of these assertions.

## Audited baseline

The following items are already proved in the research ledger:

1. the complete prime--Gamma--Tate primitive operator \(Q_T\), including
   every prime power;
2. the initial full-space interval \(0<T\leq\log2\);
3. the threshold/cell Schur reduction and its sharp Douglas formulation;
4. the exact return identities and all-depth summability statements;
5. the Euler--Poisson one-state realization of each prime-power tower;
6. the dual Euler conservation identity and its complete Gamma completion;
7. the identification of \(Q_T\) with the localized logarithmic derivative
   of the semilocal cyclic metric;
8. the identification of the old/born coupling with the tangent block of a
   genuine support projection.

They do **not** prove the sign.  The two-projection identity controls a
second-order angle Gram, whereas row D requires the first-order Schur sign.

## The one carrying theorem

For each prime-power birth, let \(P_O\) and \(P_E\) be the old and born
support projections, let \(\Pi_T\) remove the two Tate characters, and put

\[
 A_O=P_O\Pi_TQ_T\Pi_TP_O,
 \quad
 X_{OE}=P_O\Pi_TQ_T\Pi_TP_E,
 \quad
 B_E=P_E\Pi_TQ_T\Pi_TP_E.
\]

The theorem to prove is the supported sharp Douglas inequality

\[
 \mathrm{Ran}\,X_{OE}\subseteq\mathrm{Ran}\,A_O^{1/2},
 \qquad
 X_{OE}^{*}A_O^{\dagger}X_{OE}\leq B_E.              \tag{D}
\]

Equivalently, construct from source data a contraction \(\Theta_E\) such
that

\[
 X_{OE}=A_O^{1/2}\Theta_EB_E^{1/2},
 \qquad \|\Theta_E\|\leq1.                          \tag{D'}
\]

It is forbidden to define \(\Theta_E\) using the pseudoinverse in (D),
because that would merely rename the desired positivity.

In the return notation of D.214, the same theorem is

\[
 q_N^*D_N^\dagger q_N\leq\mathcal M_N,
 \qquad
 \mathcal M_N=I-y_N^*y_N-h_N^*D_Nh_N
     +2\mathrm{Re}(h_N^*q_N),                 \tag{D''}
\]

together with the supported-range condition.  Formulas (D), (D') and
(D'') are exact equivalent gates, not three independent projects.

## Selected route: localized dual-Euler curvature

Let

\[
 E_{S,\sigma}(\tau)=L_\infty(\sigma+i\tau)
 \prod_{p\in S}L_p(\sigma+i\tau),
 \qquad
 G_{S,\sigma}=M_{|E_{S,\sigma}|^2}.
\]

D.240 proves the scalar-form identity

\[
 Q_T=\Pi_TJ_T^*
 \left.\partial_\sigma\log G_{S,\sigma}
 \right|_{\sigma=1/2}J_T\Pi_T.                     \tag{1}
\]

It also proves the lossless dual conservation law between the Euler and
inverse-Euler embeddings.  The next theorem is therefore:

> **Localized dual-Euler boundary-defect theorem.**  After support cutoff
> and removal of the two Tate characters, the derivative at
> \(\sigma=1/2\) of the dual-Euler conservation law admits a positive
> boundary-defect factorization whose old/born block is exactly (D), with
> constant one.

The proof must be derived from the self-Fourier adelic vectors, the Sonin
projection, the support geometry and the Gamma factor.  It must retain the
exact cancellation between the identity part and the normalized Poisson
diagonals; separating those terms creates a false mass of order
\(\vartheta(N)\).

## Execution order

### I. Algebraic curvature reduction

1. Insert the isolated self-duality calculation of D.242: the
   \(\sigma\)-deformation is not a family of Sonin isomorphisms, and its
   exact first Fourier anomaly is
   \[
   -\sum_{p\in S}{\log p\over p}\,
   \sigma_{S\setminus\{p\}}\otimes w_p.
   \]
2. Write the localized dual conservation law and this anomaly as a block
   identity on
   \(H_O\oplus H_E\oplus H_R\).
3. Differentiate it on a common form core.
4. Short the old block before estimating anything.
5. Express the exact residual
   \[
   \mathscr R_E=B_E-X_{OE}^*A_O^\dagger X_{OE}
   \]
   in semilocal source variables.
6. Determine whether \(\mathscr R_E\) is the correctly Fisher-normalized
   anomaly boundary defect plus a nonnegative Gamma term.  D.242 rules out
   the unnormalized anomaly Gram: it is quadratic in \(\log p\), whereas
   the born score is first order.  The required expression must retain the
   cross term with the central self-dual vector or its canonical tangent
   normalization.
7. Carry domains and the \(\varepsilon\downarrow0\) regularization through
   the identity, thereby obtaining the range inclusion rather than assuming
   it.

D.244 supplies the candidate source Hodge form for step 6.  On a finite
prime set, after torsion normalization, it is

\[
 \left|\sum_p\sqrt{\log p}\,z_p\right|^2
 -\sum_p(\log p)|z_p|^2,
\]

with inertia \((1,|S|-1)\).  Its negative diagonal is exactly the reduced
row-B contact Gram and its positive completion has rank one.  The active
comparison theorem must prove that support compression, Gamma transport
and old-core shorting carry this finite tangent form to
\(\mathscr R_E\).  The finite inertia theorem itself is proved; the
comparison is not.

D.245--D.249 now supply the conservative source components behind that
comparison:

* even local tangents paired with dual central states give the exact
  first-order prime and Gamma scores;
* the prime tangent form extends to a conservative four-port colligation
  (odd plus degree versus even plus reduced contact);
* prime scores are relative delays of disk Blaschke colligations;
* the full Gamma channel is a renormalized orthogonal family of
  half-plane Blaschke delays.

Their orthogonal sum is conservative, but the balanced Redheffer wiring
that realizes the full row-D score is still open.  It may not be inferred
from equality of the local symbols.

D.252 proves that the naive local wiring cannot work: the relative prime
factor \(b_p(z)/z\) is boundary unitary but has a pole at the disk origin,
and its delay \(P_{p^{-1/2}}-1\) changes sign.  Thus it is not a causal
Schur defect.  Any successful transfer proof must retain the global
degree/contact, Tate and paired Gamma ports in one four-port feedback
system; local orthogonal sums are no longer an admissible closure claim.

D.250 proves that the tangent features cannot be inverted into the
balanced D.137 features: their exact intertwiners have boundary zeros.
Therefore step 6 must compare the **full four-port transfer colligation**
after state elimination.  A direct congruence of tangent Grams with
\(X_T,Y_T\) is impossible and is not part of the route.

The phase ends with exactly one of:

- an exact positive factorization of \(\mathscr R_E\);
- an exact signed residual strictly smaller than \(\mathscr R_E\);
- a counterexample inside the source-defined semilocal model, forcing the
  pivot below.

### II. Structural falsification

Test every proposed identity on an off-line Beurling surrogate.  A theorem
using only PNT, moment summability or unsigned coercivity and surviving
unchanged in that model cannot close row D.  The successful proof must use a
feature specific to \(\mathbb Q\): adelic Poisson summation, additive
self-duality, or the coupled archimedean Gamma factor.

No uniform strict gap is sought.  The sharp constants may converge to one;
all estimates must therefore be equality-critical.

### III. Uniform births

Order the prime powers \(q_j=p^k\) and set
\(\tau_j=\frac12\log q_j\).  Prove that the operator changes only at these
births.  Apply the factorization from Phase I uniformly to every sufficiently
large \(j\), retaining the exact weight
\((\log p)p^{-k/2}\).  Classify equality at the same time.

### IV. Finite remainder

Use interval arithmetic only for the finitely many births below the
effective uniform threshold.  Every certificate must include bases,
outward-rounded matrices, congruences, infinite-tail estimates, hashes and
a standalone verifier.  A finite compression and its complement are not an
endpoint proof unless their corrected coupling is included.

The ongoing \(T=\frac12\log6\) calculation is a laboratory for this phase,
not evidence for Phase III.

### V. Propagation and completion

Combine the initial interval, zero-extension nesting, exact birth identity,
uniform sharp factorization and finite certificates.  Pass to the closed
form domain.  Prove that the equality kernel on the primitive space contains
only the already identified radical modes.  Only then conclude the global
primitive inequality.

## Pivot rule

If Phase I produces a source-level counterexample, pivot once—not in
parallel—to the mixed theta--Riemann--Roch route.  Its carrying theorem would
be a Poisson-dual Gaussian Euler characteristic on the completed mixed
module with quadratic asymptotic

\[
 \chi_\theta(nD)=\frac{n^2}{2}B_{\rm nuc}(D,D)+O_D(n),
\]

plus effectivity and duality.  Merely defining this expression is circular;
the asymptotic and comparison with \(B_{\rm nuc}\) would have to be proved
from the lattice/nuclear construction.

## Rejected closure claims

The following do not close D:

- any finite number of positive endpoints;
- Galerkin convergence or high-precision numerics;
- all-depth summability without the unit bound;
- two Tate jets controlling an infinite boundary block;
- the generic two-projection identity;
- an assumed inner/causal completed zeta multiplier;
- a mixed section functor defined by the desired sign;
- a negative spectral subspace selected from the zeros;
- a published arithmetic Hodge theorem whose hypotheses have not been
  constructed for these mixed classes.

## Success criterion

Row D is complete only when (D) is proved source-first at every birth,
the finite remainder is rigorously certified, propagation covers all
windows, equality is classified, and the resulting closed-form inequality
is established on all of \(\mathcal T^0\).  Until then row D remains open.
