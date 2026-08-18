# 106.156 — Fourier--Weyl cyclic polarization before cohomology

## 1. Purpose

The additive Fourier transform is not an automorphism of the pointwise
Schwartz algebra: it exchanges pointwise multiplication and convolution.
This is why applying Fourier independently to every tensor in the CCM
cyclic module does not define a cyclic chain map.  The repair is not an
estimate.  It is to retain both algebra structures and let Fourier exchange
them.

This document constructs that doubled mixed complex.  The construction is
performed before taking cokernels or spectral traces.  It provides an
alternating form, a compatible complex structure, positive chain metrics,
and exact scaling bookkeeping in every cyclic degree.

## 2. The two adelic Schwartz algebras

Let \(\mathbb A=\mathbb A_{\mathbb Q}\) with self-dual Haar measure.  On the
same nuclear real Schwartz space \(\mathcal S(\mathbb A)\), use the two
products

\[
 f\cdot g:x\longmapsto f(x)g(x),\qquad
 f*g:x\longmapsto\int_{\mathbb A}f(y)g(x-y)\,dy.               \tag{1}
\]

Write \(A_x=(\mathcal S(\mathbb A),\cdot)\) and
\(A_\xi=(\mathcal S(\mathbb A),*)\).  With the self-dual normalization,

\[
 \mathcal F:A_\xi\overset{\sim}{\longrightarrow}A_x,
 \qquad \mathcal F(f*g)=\mathcal Ff\cdot\mathcal Fg              \tag{2}
\]

is a continuous algebra isomorphism.  On even real functions
\(\mathcal F^{-1}=\mathcal F\).

Let \(\alpha_q^x f(x)=f(q^{-1}x)\) for \(q\in\mathbb Q^*\).  On the
convolution algebra use the Fourier-dual action

\[
 \alpha_q^\xi=\mathcal F^{-1}\alpha_q^x\mathcal F.              \tag{3}
\]

Thus Fourier extends to an algebra isomorphism of smooth crossed products

\[
 \widetilde{\mathcal F}:
 A_\xi\rtimes_{\alpha^\xi}\mathbb Q^*
 \overset{\sim}{\longrightarrow}
 A_x\rtimes_{\alpha^x}\mathbb Q^*.                             \tag{4}
\]

The modular normalization is contained in (3); no informal change of
variables in the crossed product is required.

## 3. Functorial passage to mixed complexes

For a complete locally convex algebra \(A\), denote its completed cyclic
chains by

\[
 C_n(A)=A^{\widehat\otimes(n+1)},
\]

with Hochschild boundary \(b\) and Connes operator \(B\).  Every continuous
algebra morphism \(\phi:A\to B\) induces

\[
 C_n(\phi)=\phi^{\widehat\otimes(n+1)},\qquad
 C(\phi)b=bC(\phi),\qquad C(\phi)B=BC(\phi).                  \tag{5}
\]

Put

\[
 \mathcal C_x=C_\bullet(A_x\rtimes\mathbb Q^*),\qquad
 \mathcal C_\xi=C_\bullet(A_\xi\rtimes\mathbb Q^*),
 \qquad \mathcal C_{\rm FW}=\mathcal C_x\oplus\mathcal C_\xi. \tag{6}
\]

Let \(F_\natural=C(\widetilde{\mathcal F})\).  Define in cyclic degree
\(n\)

\[
 J_{\rm FW}(a,b)=(-F_\natural b,F_\natural^{-1}a).              \tag{7}
\]

### Theorem 3.1 — Chain-level complex structure

On the full mixed complex,

\[
 \boxed{
 J_{\rm FW}^2=-I,\qquad [J_{\rm FW},b]=0,
 \qquad[J_{\rm FW},B]=0.}                                     \tag{8}
\]

#### Proof

The square follows directly from (7).  Both commutator identities follow
from (5), applied to the algebra isomorphism (4) and its inverse.  No
spectral statement is used. \(\square\)

## 4. Positive chain polarization

On the algebraic crossed-product core of finite sums
\(a=\sum_{q\in\mathbb Q^*}f_qU_q\), use the coefficient Hilbert norm

\[
 \|a\|_2^2=\sum_q\|f_q\|_{L^2(\mathbb A)}^2.                  \tag{9}
\]

Fourier acts coefficientwise and is unitary for this norm.  Denote the two
coefficient completions by \(\mathscr L_x^2\) and \(\mathscr L_\xi^2\).
In degree \(n\), complete the finite cyclic-chain core in the Hilbert tensor
norm

\[
 \mathscr H_n=(\mathscr L_x^2)^{\otimes_2(n+1)}
             \oplus(\mathscr L_\xi^2)^{\otimes_2(n+1)}.        \tag{10}
\]

Plancherel implies that \(F_\natural\) is orthogonal on these completions.
The Hochschild operators are used first on the common nuclear chain core;
no boundedness of multiplication on the Hilbert completion is asserted.
Let \(g_n\) be the direct-sum real Hilbert metric and set

\[
 \Omega_n(u,v)=g_n(J_{\rm FW}u,v).                             \tag{11}
\]

### Theorem 4.1 — Positive polarization in every cyclic degree

For every \(n\),

\[
 \boxed{
 \Omega_n(v,u)=-\Omega_n(u,v),\qquad
 \Omega_n(u,J_{\rm FW}v)=g_n(u,v),\qquad g_n(u,u)>0\ (u\ne0).} \tag{12}
\]

Moreover \(b\) and \(B\) are complex-linear with respect to
\(J_{\rm FW}\).

#### Proof

The block matrix in (7) is orthogonal and skew-adjoint because
\(F_\natural\) is orthogonal.  Thus (11) is alternating and
\(\Omega_n(u,J_{\rm FW}v)=g_n(Ju,Jv)=g_n(u,v)\).  Complex linearity is
(8). \(\square\)

This is a genuine positive chain polarization; it has been defined before
forming any cohomology group and without reference to a zeta zero.

## 5. Algebraic scaling and the Tate-twist bookkeeping

Let \(\beta_t^x f(x)=f(a_t^{-1}x)\), where \(|a_t|=e^t\), and define
\(\beta_t^\xi=\mathcal F^{-1}\beta_{-t}^x\mathcal F\).  These are algebra
automorphisms.  On the doubled complex use

\[
 \mathbb\beta_t=C(\beta_t^x)\oplus C(\beta_{-t}^\xi).         \tag{13}
\]

Then \(J_{\rm FW}\mathbb\beta_t=\mathbb\beta_tJ_{\rm FW}\), and
\(\mathbb\beta_t\) commutes with \(b\) and \(B\).  On the regular
\(L^2\)-chain completion in cyclic degree \(n\), both summands scale the
squared norm by \(e^{(n+1)t}\).  Therefore

\[
 \boxed{
 g_n(\mathbb\beta_tu,\mathbb\beta_tv)
 =e^{(n+1)t}g_n(u,v),\qquad
 \Omega_n(\mathbb\beta_tu,\mathbb\beta_tv)
 =e^{(n+1)t}\Omega_n(u,v).}                                  \tag{14}
\]

One must not normalize every degree by hand and still call the result a
mixed-complex action: the factors \(e^{-(n+1)t/2}\) differ in adjacent
degrees and hence do not commute with \(b\).  The conversion of (13) to a
single weight-one action belongs to the Tate twist in the derived
degree-one realization.  Degree zero recovers the half-density
normalization of 106.155.  Proving that the CCM \(\mathrm{Tor}\,\)
realization supplies exactly this twist is part of the descent theorem,
not an identity available at chain level.

## 6. Relative cone and Poisson descent

Apply the same doubling to the CCM target cyclic module of trace-class
fields on \(C_{\mathbb Q}\).  Inversion
\(Ih(x)=h(x^{-1})\) exchanges the two normalized scaling directions.
Degree zero of the doubled restriction/summation morphism is the map \(E\)
of 106.155, and Poisson summation gives

\[
 E\mathcal F=IE.                                               \tag{15}
\]

Define the dual target and the dual restriction morphism by conjugating the
CCM target and \(\rho_x^\natural\) with Fourier and inversion.  The resulting
square commutes by construction; its degree-zero content is the
non-tautological identity (15).  Functoriality then gives a morphism of
doubled mixed complexes and a mapping cone

\[
 \mathfrak C_{\rm FW,rel}
 =\mathrm{Cone}(\rho_x^\natural\oplus\rho_\xi^\natural) \tag{16}
\]

carrying \(J_{\rm FW}\), algebraic scaling, and the chain forms (11).
The coefficient tensoring of 106.154 inserts all prime modules into this
same relative object, with the exact moments
\(p^{-|k|/2}\).

## 7. What this construction does and does not transfer

The mixed complex (16) is a Fourier--Poisson cyclic enhancement
of the degree-zero cone.  It corrects the category error in 106.155:
Fourier is used as an algebra isomorphism between dual products, so (8) is
literal rather than formal.

There remains a distinct descent issue.  The positive Hilbert tensor norms
in (9) produce **reduced** homology after closures are taken.  CCM instead
use a Schwartz/Meyer derived cokernel whose cyclic degrees and topology
retain the spectral realization.  The forgetful map

\[
 H_1(\mathfrak C_{\rm FW,rel})
 \longrightarrow H^1_{\rm CCM}\oplus H^{1,\vee}_{\rm CCM}      \tag{17}
\]

is algebraically defined, but its Hilbert completion need not be injective
or surjective.  Declaring it unitary would be invalid: if it were a
scaling-equivariant unitary isomorphism after the degree-one Tate twist,
the induced weight-one identity and the CCM trace formula
would already force RH.

Therefore the missing polarization is no longer a missing formula for
\(J\), \(\Omega\), or the prime coefficients.  Those have now been
constructed at chain level.  The remaining theorem is a **torsion-sensitive
Hodge descent**: construct a positive completion of the derived degree-one
classes for which (17) is faithful and the CCM trace pairing is the
induced Hermitian pairing.

## 8. Falsification controls

1. **No Euler product.**  The Fourier--Weyl double exists for any additive
   Poisson problem.  What fails without an Euler product is the coefficient
   descent of 106.154: there are no positive prime-orbit states with moments
   \(p^{-|k|/2}\).  Thus the chain symmetry alone does not claim RH for a
   Davenport--Heilbronn function.
2. **Degree-zero reduction.**  Replacing the derived cone by its reduced
   \(L^2\) cokernel can make degree one vanish.  Hence the construction does
   not smuggle in a positive spectral space by completion.
3. **Off-line test.**  If a hypothetical off-line spectral class is kept in
   the CCM topology, it cannot have finite positive norm compatible with
   the induced weight-one unitary normalization.  It must either be killed
   by the positive completion or make the
   descent map unbounded.  This is the exact test the torsion-sensitive
   descent must pass.

## 9. Status

Proved here:

* a Fourier complex structure on an actual cyclic mixed complex;
* commutation with both \(b\) and \(B\);
* positive alternating chain forms in all cyclic degrees;
* the exact degree-dependent scaling law and the required Tate-twist
  bookkeeping;
* a relative Fourier--Poisson cone compatible with the prime coefficient
  module constructed in 106.154.

Still required:

* a torsion-sensitive positive completion of derived degree one;
* faithfulness of the descent (17) on the CCM spectral cokernel;
* identification of the induced Hermitian form with the CCM trace pairing.

## 10. Primary inputs

* A. Connes, C. Consani, and M. Marcolli,
  [*The Weil proof and the geometry of the adeles class space*](https://arxiv.org/abs/math/0703392):
  the cyclic cokernel, its \(\mathrm{Tor}\,\) realization, scaling action,
  trace pairing, and the sharp involution.
* A. Connes and C. Consani,
  [*Weil positivity and Trace formula, the archimedean place*](https://arxiv.org/abs/2006.13771):
  the self-dual Fourier/inversion operator and the positive Sonin
  compression at the archimedean place.
* A. Connes and C. Consani,
  [*On the Jacobian of the arithmetic curve*](https://arxiv.org/abs/2602.15941):
  the arithmetic Jacobian, prime fibers, generic fiber, and geometric
  support of the Lefschetz trace.
