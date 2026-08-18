# 106.184 — Equivariant Hilbert majorants and the alternative polarization branch

## 1. Purpose

The rigidity theorem of 106.182 fixes the compatible complex structure
only after both pieces

\[
 \Omega=-\mathrm{Im}\,\mathfrak h_{\rm Ros},
 \qquad g=\mathrm{Re}\,\mathfrak h_{\rm Ros}             \tag{1}
\]

have been prescribed.  It does not rule out a different complex structure
\(J'\) compatible with the same nondegenerate alternating form \(\Omega\),
with positive metric

\[
 g'(u,v)=\Omega(u,J'v)                                       \tag{2}
\]

different from \(g\).  This note isolates that genuinely different branch
and gives a constructive operator criterion for it.

The criterion requires no arithmetic surface and no factorization of the
Rosati form.  It requires instead a source-defined positive Hilbert
majorant on the actual nonreduced CCM degree one, faithful under the
scaling action.  Once such a majorant exists, polar decomposition produces
\(J'\) canonically.

## 2. Symplectic scaling data

Let \(H\) be the separated real CCM degree one and let \(\Omega\) be its
descended alternating form.  Write \(\vartheta_t\) for the weight-one
scaling action, so

\[
 \Omega(\vartheta_tu,\vartheta_tv)=e^t\Omega(u,v).            \tag{3}
\]

Set

\[
 U_t=e^{-t/2}\vartheta_t.                                   \tag{4}
\]

Then \(U_t\) preserves \(\Omega\).  A positive polarization independent
of Rosati is a real-linear operator \(J'\) such that

\[
 (J')^2=-I,qquad
 \Omega(J'u,J'v)=\Omega(u,v),qquad
 \Omega(u,J'u)>0\quad(u\ne0),                               \tag{5}
\]

and

\[
 J'U_t=U_tJ'.                                                \tag{6}
\]

Equations (3), (5), and (6) make \(g'\) in (2) positive and give

\[
 g'(\vartheta_tu,\vartheta_tv)=e^tg'(u,v).                  \tag{7}
\]

Thus the normalized scaling group is unitary for \(g'\).

## 3. Polar construction from a Hilbert majorant

Let \(g_0\) be a positive real Hilbert inner product on a completion
\(H_0\) of \(H\).  Assume:

1. the inclusion \(H\hookrightarrow H_0\) is faithful;
2. every \(U_t\) extends to a strongly continuous \(g_0\)-unitary group;
3. \(\Omega\) extends continuously to \(H_0\);
4. the representing operator of \(\Omega\) is boundedly invertible.

By Riesz representation there is a unique bounded operator \(A\) with

\[
 \Omega(u,v)=g_0(Au,v).                                     \tag{8}
\]

Alternation implies

\[
 A^*=-A.                                                     \tag{9}
\]

Consequently \(-A^2=A^*A\) is positive and boundedly invertible.  Put

\[
 |A|=(-A^2)^{1/2},qquad
 \boxed{J'=A|A|^{-1}.}                                      \tag{10}
\]

### Theorem 3.1 — Canonical alternative polarization

Under assumptions 1--4, (10) satisfies (5)--(6), and

\[
 \boxed{g'(u,v)=\Omega(u,J'v)=g_0(|A|u,v).}                 \tag{11}
\]

In particular, \(g'\) is positive definite and is defined before any
Rosati sign is assumed.

#### Proof

Since \(A\) is skew-adjoint, it is normal and commutes with \(|A|\).
Therefore

\[
 (J')^2=A^2|A|^{-2}=-I,qquad (J')^*=-J',qquad (J')^*J'=I. \tag{12}
\]

Thus \(J'\) is an orthogonal complex structure.  Using
\(A=J'|A|\),

\[
 \Omega(u,J'v)
 =g_0(Au,J'v)
 =g_0(J'|A|u,J'v)
 =g_0(|A|u,v),                                              \tag{13}
\]

which proves (11) and positivity.

Because \(U_t\) is \(g_0\)-unitary and preserves \(\Omega\), equations
(8) give

\[
 U_t^*AU_t=A.                                                \tag{14}
\]

Hence \(A\), \(|A|\), and \(J'\) commute with \(U_t\), proving (6).
Symplecticity of \(J'\) follows from (8), (12), and commutation of
\(J'\) with \(A\). \(\square\)

### Remark 3.2 — Weakly nondegenerate version

If \(A\) is injective but not bounded below, its polar part is nevertheless
unitary on the whole Hilbert space, because both its initial and final
spaces are dense and have zero orthogonal complement.  The weaker metric
in (11) is definite and its completion retains \(J'\), \(\Omega\), and
strongly continuous normalized scaling.  This is proved in 106.190.
Consequently bounded invertibility is sufficient but not necessary.

## 4. Converse and exact force of the criterion

### Proposition 4.1 — Every alternative polarization supplies a majorant

If a \(J'\) satisfying (5)--(6) exists, then \(g'\) from (2) is a positive
weight-one metric and its completion makes \(U_t\) unitary.  Relative to
\(g_0=g'\), the representing operator in (8) is \(A=J'\), up to the sign
convention of \(\Omega\).

Thus Theorem 3.1 is not merely sufficient at the level of existence: the
alternative-polarization problem is equivalent to constructing a faithful
scale-covariant Hilbert majorant for which \(\Omega\) is bounded and
weakly nondegenerate.

This equivalence is distinct from the GNS equivalence in 106.182.
It does not ask that

\[
 g'=\mathrm{Re}\,\mathfrak h_{\rm Ros}.                \tag{15}
\]

It asks for a new positive metric on the same symplectic degree one.
Nevertheless, by the CCM spectral realization, a faithful metric with
(6) would make the normalized scaling generator skew-adjoint and would
therefore exclude every off-line spectral exponent.  Its existence has
the full spectral consequence, even though it is not a factorization of
the Weil form.

## 5. What the existing chain metric supplies

The Fourier--Weyl doubled mixed complex of 106.155--106.156 already has a
source-defined positive chain metric, complex structure, and unitary
normalized scaling.  On its reduced Hilbert cohomology it satisfies all
four hypotheses of Section 3.

It does not yet produce \(g_0\) on the CCM degree one.  The reason is
precise:

\[
 \overline{\mathrm{Ran}\,\rho}^{\,L^2}
 =\text{the whole Hilbert target},                           \tag{16}
\]

whereas the nonreduced nuclear cokernel remains nonzero.  Passing to the
reduced Hilbert quotient therefore gives zero and loses the resonant
classes.  The matched-cutoff descent of 106.181 transports the *finite
Rosati pairing*, not the ambient positive chain norm.  These are different
operations.

Accordingly, the missing non-geometric theorem can be stated without a
factor \(D\):

> **Equivariant Hilbert-majorant theorem.**  The positive Fourier--Weyl
> chain metric admits a torsion-sensitive, faithful degree-one descent to
> the nonreduced CCM quotient, and the descended alternating form is
> bounded and weakly nondegenerate for that metric.

If proved, Theorem 3.1 constructs \(J'\) and (11) supplies the positive
polarization.  No equality with the Rosati metric is required.

## 6. Why a formal Hilbertization is insufficient

Every separable nuclear Frechet space can be injected into a Hilbert space
by choosing a countable separating family of continuous functionals and
rapidly decreasing weights.  Applied to the dense jet observation of
106.175, this gives many faithful positive Hilbert norms on the underlying
vector space.

Such an arbitrary Hilbertization does not satisfy the theorem.  It need
not make the normalized scaling uniformly bounded, much less unitary, and
\(\Omega\) need not be represented by a boundedly invertible operator.
Time-averaging the metric does not repair this: an exponentially growing
mode makes every two-sided invariant average divergent.  Hence the
arithmetic content is exactly the simultaneous validity of assumptions
2--4, not mere Hilbert embeddability.

## 7. Relation to an arithmetic surface

A Hodge-index theorem on an arithmetic square would produce the fixed
Rosati branch of 106.182.  It is sufficient, but it is not logically
necessary.  Theorem 3.1 gives a second possible source:

\[
 \boxed{
 \text{faithful equivariant Hilbert majorant}
 \Longrightarrow J'
 \Longrightarrow \text{positive polarization}.}           \tag{17}
\]

Thus one need not first construct a full
\(\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}
\mathrm{Spec}\,\mathbb Z\).  It is enough to construct the restricted
analytic shadow used in (17).  Conversely, a proposed non-geometric proof
must exhibit the majorant from the prime/root/Gamma source; defining it
from the zero divisor or from \(|\mathfrak h_{\rm Ros}|\) would reverse the
logical direction.

## 8. Status

Proved:

* the polar-decomposition construction of every alternative compatible
  complex structure from a faithful equivariant Hilbert majorant;
* positivity and scaling covariance of the resulting metric;
* the converse majorant supplied by any such polarization;
* the exact distinction between this branch and Rosati factorization.

Still required on this branch:

* a source-defined torsion-sensitive descent of the positive
  Fourier--Weyl chain metric to nonreduced CCM degree one;
* bounded weak nondegeneracy of \(\Omega\) in that descended metric.
