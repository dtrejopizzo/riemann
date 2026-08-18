# 106.190 — The weak polar-completion theorem

## 1. Purpose

The alternative-polarization criterion of 106.184 assumed that the
operator representing the alternating form was boundedly invertible.
That is stronger than necessary and would impose a uniform symplectic gap.
The global Riemann problem is expected to have no such uniform margin.

This note proves the correct threshold.  A bounded, injective
skew-adjoint representative is enough.  Its polar part is already a
unitary complex structure; the positive metric may be weaker than the
reference Hilbert metric, but its completion retains both the complex
structure and the normalized scaling group.

## 2. Weak symplectic Hilbert data

Let \((H_0,g_0)\) be a real Hilbert space and let
\(\Omega:H_0\times H_0\to\mathbb R\) be a bounded alternating form.  Its
Riesz representative is the unique bounded operator \(A\) satisfying

\[
 \Omega(u,v)=g_0(Au,v).                                     \tag{1}
\]

Alternation gives

\[
 A^*=-A.                                                     \tag{2}
\]

Assume only

\[
 \boxed{\ker A=\{0\}.}                                      \tag{3}
\]

No lower bound on \(|A|\) is imposed.

## 3. Polar complex structure without a gap

### Theorem 3.1 — Weak polar completion

Under (1)--(3), the polar decomposition of \(A\) has the form

\[
 \boxed{A=J|A|,\qquad J^2=-I,\qquad J^*=-J,\qquad J^*J=I.}  \tag{4}
\]

Moreover

\[
 \boxed{
 g_1(u,v):=\Omega(u,Jv)=g_0(|A|u,v)}                        \tag{5}
\]

is a positive-definite inner product on \(H_0\).  The operator \(J\)
extends to an orthogonal complex structure on the completion \(H_1\) of
\(H_0\) for \(g_1\), and

\[
 \Omega(u,v)=-g_1(u,Jv)                                     \tag{6}
\]

extends continuously to \(H_1\).

#### Proof

Since \(A\) is skew-adjoint, it is normal and

\[
 |A|=(A^*A)^{1/2}=(-A^2)^{1/2}.                             \tag{7}
\]

The initial space of the polar partial isometry is
\(\overline{\operatorname {Ran}|A|}=(\ker A)^\perp=H_0\).
Its final space is

\[
 \overline{\operatorname {Ran}A}
 =(\ker A^*)^\perp
 =(\ker A)^\perp=H_0.                                      \tag{8}
\]

Thus the polar part \(J\) is unitary on all of \(H_0\).  Functional
calculus for the skew-adjoint normal operator gives \(J^*=-J\) and
\(J^2=-I\).  Equivalently, write \(A=iB\) on the complexification, where
\(B\) is injective self-adjoint; then
\(J=i\,\operatorname {sgn}B\).

Using \(A=J|A|\),

\[
 \Omega(u,Jv)
 =g_0(J|A|u,Jv)
 =g_0(|A|u,v),                                              \tag{9}
\]

which proves (5).  If \(u\ne0\), injectivity of \(|A|\) gives
\(g_1(u,u)>0\).  Since \(J\) commutes with \(|A|\),

\[
 g_1(Ju,Jv)=g_1(u,v),                                      \tag{10}
\]

so \(J\) extends orthogonally to the \(g_1\)-completion.  Formula (6)
follows from \(J^2=-I\) and (5), and makes \(\Omega\) bounded in the
completed metric:

\[
 |\Omega(u,v)|=|g_1(u,Jv)|
 \le\|u\|_{g_1}\|v\|_{g_1}.                                \tag{11}
\]

Hence it extends to \(H_1\). \(\square\)

### Remark 3.2 — What degenerates

If \(0\) lies in the continuous spectrum of \(|A|\), the \(g_1\)-norm is
strictly weaker than \(g_0\), and the embedding \(H_0\to H_1\) need not
have closed range.  This is compatible with a torsion-sensitive
polarization and with the absence of a uniform spectral margin.  It does
not create a radical: (3) keeps \(g_1\) definite on the original space.

## 4. Equivariant version

Let \(U_t\) be a strongly continuous \(g_0\)-unitary group satisfying

\[
 \Omega(U_tu,U_tv)=\Omega(u,v).                              \tag{12}
\]

### Theorem 4.1 — Scaling survives weak completion

The operators \(U_t\) commute with \(A\), \(|A|\), and \(J\), are
\(g_1\)-unitary, and extend to a strongly continuous unitary group on
\(H_1\).

#### Proof

Equations (1) and (12), together with \(g_0\)-unitarity, give
\(U_t^*AU_t=A\).  Therefore \(U_t\) commutes with \(A\), its functional
calculus, and \(J\).  Equation (5) then gives

\[
 g_1(U_tu,U_tv)=g_1(u,v).                                   \tag{13}
\]

For strong continuity in \(H_1\), use

\[
 \|U_tu-u\|_{g_1}^2
 =\bigl\||A|^{1/2}(U_tu-u)\bigr\|_{g_0}^2
 =\bigl\|U_t|A|^{1/2}u-|A|^{1/2}u\bigr\|_{g_0}^2,           \tag{14}
\]

which tends to zero by strong continuity on \(H_0\).  Extend by density.
\(\square\)

For the weight-one CCM flow \(\vartheta_t=e^{t/2}U_t\), both \(g_1\) and
\(\Omega\) scale by \(e^t\), and its generator obeys
\(\Theta^\dagger+\Theta=I\) in the \(g_1\)-completion.

## 5. Corrected alternative-polarization target

The non-geometric branch no longer requires bounded strong
nondegeneracy.  It is enough to construct a source-defined Hilbert
majorant \(g_0\) on the separated nonreduced CCM degree one such that:

1. normalized scaling is \(g_0\)-unitary;
2. the descended alternating form \(\Omega_{\rm CCM}\) is \(g_0\)-bounded;
3. its representing skew-adjoint operator has zero kernel.

Condition 3 is weak nondegeneracy.  Algebraic nondegeneracy on a nuclear
core does not automatically imply it after Hilbert completion: a nonzero
class may be killed by the completion, and the bounded extension may gain
a kernel.  Faithfulness of the completion remains essential.

If 1--3 hold, Theorems 3.1 and 4.1 construct the desired positive
equivariant polarization without identifying its metric with Rosati and
without a uniform lower bound.

## 6. Relation to the current coefficient construction

The nuclear trace object of 106.188 supplies a faithful positive graph
form before CCM descent, but Section 5 there proves that it does not yet
carry the unitary real CCM action.  Free archimedean induction repairs the
action but becomes coisometric and loses the cokernel by 106.189.

The remaining non-free relative differential therefore needs only weak,
not strong, symplectic nondegeneracy after descent.  In particular, an
accumulation of singular values at zero is admissible.  What is forbidden
is an actual kernel or loss of a CCM class.

## 7. Status

Proved:

* polar construction of a unitary compatible complex structure from a
  bounded injective alternating form;
* positivity of the weaker metric and continuity after completion;
* preservation of normalized scaling under that completion;
* removal of the unnecessary uniform symplectic-gap requirement from
  106.184.

Still required:

* a faithful non-free Gamma--Euler--polar descent carrying a
  scale-unitary Hilbert majorant on CCM degree one;
* boundedness and weak nondegeneracy, rather than bounded invertibility,
  of the descended alternating form.
