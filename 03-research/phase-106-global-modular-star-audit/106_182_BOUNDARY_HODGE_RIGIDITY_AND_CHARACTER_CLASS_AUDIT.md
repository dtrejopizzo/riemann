# 106.182 — Boundary Hodge rigidity and the character-class audit

## 1. Purpose

The matched-cutoff theorem of 106.181 constructs on the actual CCM
degree-one quotient the Hermitian form

\[
 \mathfrak h_{\rm Ros}(u,v)=\tau(f*g^\sharp),
 \qquad u=[f],\quad v=[g].                                  \tag{1}
\]

It is tempting to describe the remaining step as the construction of a
new boundary Hodge star.  This description leaves an apparent freedom
which is not present.  Once the alternating form and the Hermitian
intersection form are fixed, the compatible complex structure is unique.
For the CCM form it is already ordinary multiplication by \(i\).

This note proves that rigidity.  It then checks two possible sources of a
new positive class—the Chern character of the zeta spectral triples and a
Quillen metric on the primitive determinant line—and shows exactly what
they do and do not supply.  The conclusion is a sharper target: the
remaining theorem is a Hodge-index sign theorem for the already constructed
relative intersection form, not the construction of another star,
renormalization, or determinant metric.

## 2. The descended real data

Let

\[
 H=H^1_{\rm Ros}
\tag{2}
\]

be the separated nonreduced CCM degree one of 106.157 and 106.181.  Regard
\(H\) as a real vector space and write

\[
 g(u,v)=\mathrm{Re}\,\mathfrak h_{\rm Ros}(u,v),
 \qquad
 \Omega(u,v)=-\mathrm{Im}\,\mathfrak h_{\rm Ros}(u,v).
\tag{3}
\]

The radical of the Hermitian form has already been divided out.  Hence the
pair \((g,\Omega)\) is jointly nondegenerate: if both forms pair \(u\)
trivially with every \(v\), then \(u=0\).  Let

\[
 J_0u=iu.
\tag{4}
\]

Sesquilinearity gives the exact compatibility identity

\[
 \boxed{g(u,v)=\Omega(u,J_0v).}                              \tag{5}
\]

No spectral value or zero divisor occurs in (2)--(5).

## 3. Rigidity of the compatible star

The relevant uniqueness statement does not require a Hilbert completion.

### Theorem 3.1 — No second boundary Hodge star

Suppose \(J:H_{\mathbb R}\to H_{\mathbb R}\) is real linear and satisfies

\[
 \Omega(u,Jv)=g(u,v)
 \qquad(u,v\in H_{\mathbb R}).                              \tag{6}
\]

Then

\[
 \boxed{J=J_0.}                                             \tag{7}
\]

In particular, requiring additionally \(J^2=-I\), symplecticity, scaling
equivariance, or continuity does not create a second choice.

#### Proof

Subtract (5) from (6).  For every \(u,v\),

\[
 \Omega\bigl(u,(J-J_0)v\bigr)=0.                            \tag{8}
\]

The alternating form induced by a nondegenerate Hermitian form is
nondegenerate as a real form.  Indeed, if \(\Omega(u,w)=0\) for every
\(u\), then the same hypothesis applied with first argument \(J_0u\)
and complex linearity in that argument give

\[
 \Omega(J_0u,w)
 =-\mathrm{Im}\,\bigl(i\mathfrak h_{\rm Ros}(u,w)\bigr)
 =-g(u,w)=0
\]

for every \(u\), and joint nondegeneracy gives \(w=0\).  Apply this to
\(w=(J-J_0)v\) in (8).  Thus \((J-J_0)v=0\) for every \(v\), proving
(7). \(\square\)

### Corollary 3.2 — The remaining condition is only the index sign

The triple \((\Omega,J_0,g)\) is a positive polarization if and only if

\[
 \boxed{
 \mathrm{Re}\,\tau(f*f^\sharp)\geq0
 \quad\text{for every }[f]\in H.}                           \tag{9}
\]

Therefore a proposed ``new star'' can close the construction only by
changing either the descended Rosati form or the quotient.  If it retains
both, Theorem 3.1 forces it to be \(J_0\), and its positivity is precisely
(9).

This also clarifies the role of the finite Julia star.  Documents
106.178--106.181 use it to derive, normalize, and descend the physical
form (1).  After descent its complex structure is not an additional
variable: it has become (4).

## 4. Factorization rigidity

Let \(\mathscr K\) be a complex Hilbert space and let
\(D:H\to\mathscr K\) be linear on the nuclear core.

### Proposition 4.1 — A positive factorization contains the complete sign

An identity

\[
 \mathfrak h_{\rm Ros}(u,v)=\langle Du,Dv\rangle_{\mathscr K}
\tag{10}
\]

holds for a faithful \(D\) if and only if the form (1) is positive
definite on the separated quotient and its induced pre-Hilbert completion
embeds through \(D\).

#### Proof

Equation (10) immediately gives
\(\mathfrak h_{\rm Ros}(u,u)=\|Du\|^2\geq0\); faithfulness makes equality
possible only for \(u=0\).  Conversely, if the form is positive definite,
complete \(H\) in its own norm and use the canonical inclusion. \(\square\)

Thus a factorization is the correct *form* of a Hodge-index theorem, but
not an independent source of its sign.  The source must be a geometric or
arithmetic construction of \(D\) whose norm is known before (1) is used.
Defining the target norm by (1) would be circular.

## 5. Why the Chern character does not yet supply the factorization

The finite zeta spectral triples provide self-adjoint operators associated
with the semilocal Weil forms.  Their Chern characters are cyclic classes
and their pairings with \(K\)-theory are index pairings.  This has two exact
consequences.

1. A Chern character is functorial under the cyclic mapping-cone and Bott
   constructions already used in 106.156 and 106.171.  It can therefore
   orient the relative class and transport its index.
2. It does not make an arbitrary Hermitian trace functional positive.
   To obtain (10), one would need a chain map \(D\) whose JLO or resolvent
   pairing with the relative class equals \(\tau(f*g^\sharp)\) for every
   pair \(f,g\), not merely the equality of an index on idempotents or
   unitaries.

At finite semilocal cutoff the Weil operator is lower semibounded, not
canonically nonnegative; subtracting its lower edge is the shift already
audited in Paper 40.  Passing to the Chern character forgets this scalar
edge because bounded homotopies preserve the character.  Hence the
character cannot select the sign of (9).  The missing input would again be
a theorem identifying the *unshifted* relative quadratic form with a
positive JLO norm.  That theorem is exactly (10), not a formal consequence
of cyclicity.

This is compatible with 106.171: the Bott/Toeplitz class gives the correct
odd orientation and the prime Lefschetz minus sign, while its remaining
comparison was explicitly the Rosati metric identity.

## 6. Why a Quillen metric does not control the support

Document 106.168 constructs the primitive determinant connection
\(\nabla_{\rm pr}\) and proves that its interior residues are exactly the
nontrivial zero multiplicities.  Giving its determinant line a positive
Hermitian metric is not enough to force those residues to the critical
boundary.

This can be seen without an arithmetic example.  On a disk, take the
trivial Hermitian line with any smooth positive metric \(\|1\|^2=e^{-\phi}\).
For every point \(a\) in the disk, the section

\[
 s_a(z)=z-a                                                   \tag{11}
\]

has an interior zero at \(a\), while the curvature of the metric remains
the fixed form \(\partial\bar\partial\phi\), independent of \(a\).
Poincare--Lelong records

\[
 {i\over\pi}\partial\bar\partial\log\|s_a\|
 =[a]-c_1(L,\|\cdot\|),                                     \tag{12}
\]

but positivity of the metric does not constrain the support of \([a]\).
Therefore a Quillen metric can normalize the determinant and compute its
curvature; it cannot by itself prove that the residue current of
\(\nabla_{\rm pr}\) has no interior support.  A relative Hodge-index
theorem is still required.

## 7. Exact state of the construction

The following points are now closed without a zero input:

* the full prime-return coefficient modules and their exact masses;
* the finite Julia involution and the intrinsic selection of its negative
  graph;
* the Dirichlet weight that converts the inverse defect to the physical
  local Green energy;
* matched-cutoff cancellation of the white-light scalar;
* exact stabilization and scale covariance on the compact logarithmic
  core;
* descent through the closed CCM range;
* equality with the global Rosati pseudo-polarization;
* uniqueness of the compatible complex structure on that form.

The single force-bearing statement **within the fixed Rosati metric** is
(9).  It can no longer be assigned to a choice of branch, cutoff, anomaly
counterterm, Hodge star preserving that metric, cyclic orientation, Chern
character, or determinant metric.  A valid successor on this branch must
construct an arithmetic intersection operation on the relative pair whose
norm identity is (10) and whose positivity is proved before taking the CCM
trace.

Theorem 3.1 does not exclude a different compatible complex structure
\(J'\) for the same alternating form when the associated metric
\(g'(u,v)=\Omega(u,J'v)\) is allowed to differ from
\(\mathrm{Re}\,\mathfrak h_{\rm Ros}\).  That distinct unitarization
branch is developed in 106.184.  Its load-bearing input is a faithful,
scale-covariant positive Hilbert majorant on the nonreduced CCM degree one;
it is not another choice inside the Rosati identity.

## 8. Status

Proved:

* rigidity of the boundary Hodge star;
* equivalence between a faithful Hilbert factorization and the complete
  Rosati sign;
* exclusion of a formal Chern-character or Quillen-metric argument as the
  missing source of positivity.

Still required:

* a source-defined relative intersection map \(D\) satisfying (10), or an
  arithmetic Hodge-index theorem proving (9) directly, on the fixed-Rosati
  branch;
* alternatively, a faithful scale-covariant Hilbert majorant producing a
  different compatible complex structure as in 106.184.
