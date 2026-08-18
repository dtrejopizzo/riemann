# 106.205 — Absolutely continuous completion no-go

## 1. Purpose

The charged closure identity of 106.200 was left as the last condition
for pulling the positive pushout polarization to CCM degree one.  Before
trying to prove that identity, one must test the spectral type of the
candidate target.

The test is decisive.  The Cauchy coefficient representation, every
charge shift, the Gamma gradient, the covariant mixing of 106.204, and
their cofinal Hilbert completion all have absolutely continuous scale
spectrum.  The CCM degree-one object contains nonzero resonant
eigenclasses at the known critical zeros.  Consequently no
scale-equivariant map from CCM degree one to this Hilbert completion can
be injective.

Thus the closure identity 106.200(24), for this concrete target, is
false.  The positive source object remains valid, but it is not the
missing CCM polarization.

## 2. The operator-valued multiplier test

Let \((X,\mu)\) be sigma finite, let \(\mathfrak h\) be separable, and
let

\[
 M(x):\mathfrak h\longrightarrow\mathfrak h
\tag{1}
\]

be a measurable field of closed densely defined operators.  Denote by
\(\mathcal M\) its maximal decomposable multiplication operator on
\(L^2(X,\mu;\mathfrak h)\).

### Lemma 2.1 — Dense range criterion for operator-valued multipliers

\[
 \boxed{
 \overline{\mathrm{Ran}\,\mathcal M}
 =L^2(X,\mu;\mathfrak h)
 \quad\Longleftrightarrow\quad
 \ker M(x)^*=0\ \text{for almost every }x.}
\tag{2}
\]

If \(M(x)^*M(x)\succeq\kappa I\) almost everywhere for one
\(\kappa>0\), then \(\mathcal M\) has closed range and is bounded below;
if (M(x)) is self-adjoint, it is boundedly invertible.

#### Proof

The adjoint of a maximal decomposable operator is the decomposable
operator with fibers (M(x)^*).  Hence

\[
 (\overline{\mathrm{Ran}\,\mathcal M})^\perp
 =\ker\mathcal M^*
 =\int_X^\oplus\ker M(x)^*\,d\mu(x).
\tag{3}
\]

This proves (2).  The uniform lower bound gives the remaining claims by
the closed-range theorem and the spectral calculus. \(\square\)

Apply the lemma to

\[
 K_{\Gamma,Q}
 =\kappa_\infty I+
   \bigoplus_{q\in Q}m_\Gamma(A-\log q).
\tag{4}
\]

Since \(m_\Gamma\ge0\) and \(\kappa_\infty>0\),

\[
 \boxed{K_{\Gamma,Q}\succeq\kappa_\infty I.}
\tag{5}
\]

Therefore the charged Gamma block loses rank on no spectral set at all.
If the scalar finite part is omitted, the zero set of
\(m_\Gamma(\gamma-\log q)\) is contained in the countable set
\(\{\log q:q\in Q\}\), hence is null; the range is still dense.

The spectral translations (S_{\log q}) of 106.204 are unitary.
Unitary left or right mixing preserves kernels of adjoints, closure of
ranges, and spectral type.  Thus the non-diagonal charge mixing does not
alter this conclusion.

## 3. Absolute continuity of the complete pushout

Let (U_t=e^{itA}) be the normalized scale group on the Cauchy
coefficient space

\[
 \mathscr K_C=L^2(\mathbb R,w_C(\gamma)d\gamma),
 \qquad w_C(\gamma)>0.
\tag{6}
\]

Its spectral measure is equivalent to Lebesgue measure.  In particular,
it has no eigenvectors.

### Lemma 3.1 — Stability of absolute continuity

The following operations preserve absolute continuity of a unitary
representation of \(\mathbb R\):

1. countable orthogonal sums and finite tensoring;
2. shifts of the generator by real constants;
3. unitary conjugacy, including the (S_\ell\) of 106.204;
4. invariant closed subspaces;
5. graph embeddings formed from closed equivariant operators;
6. completion of an increasing union of invariant Hilbert subspaces
   when every inclusion is isometric.

#### Proof

Items 1--4 follow directly from the spectral theorem.  For item 5, the
graph is an invariant closed subspace of a direct sum of absolutely
continuous representations.  For item 6, let (E(B)) be the limiting
spectral projection of a Lebesgue-null Borel set (B).  It vanishes on
every finite-level subspace, hence on their dense union, and therefore
on the completion. \(\square\)

### Theorem 3.2 — The charged pushout has purely continuous scale spectrum

Let \(\mathbb P_\infty^{\rm cov}\) be the cofinal Hilbert completion
constructed from the corrected metric 106.204(23).  Its normalized
scale representation is absolutely continuous and has empty point
spectrum:

\[
 \boxed{
 \mathbb P_\infty^{\rm cov,pp}=\{0\}.}
\tag{7}
\]

#### Proof

At each finite level, the Tate coefficient rows are finite sums of
copies of (6) with generators shifted by the lengths (k\log p).  The
Gamma gradient is a closed equivariant graph over the same absolutely
continuous representation.  The polar boundary contributes only the
finite scalar compliance inside that graph and adds no scale eigenline
to degree one.  The covariant charge mixing is unitary by 106.204.
Hence Lemma 3.1 applies at every finite level and then to the isometric
cofinal completion. \(\square\)

## 4. Conflict with the CCM resonant degree one

The CCM cyclic degree one is not the reduced (L^2) cokernel.  In each
compact-character sector its scaling spectrum is the divisor of the
corresponding completed (L)-function, with jets for multiplicities.
For the trivial character, every nontrivial zero

\[
 \rho=\frac12+i\gamma
\tag{8}
\]

on the critical line supplies a nonzero eigenclass (u_\rho\) for the
normalized scale action:

\[
 U_t^{\rm CCM}u_\rho=e^{it\gamma}u_\rho.
\tag{9}
\]

Existence of infinitely many such zeros is unconditional.

### Theorem 4.1 — No faithful equivariant descent to the pushout

Every scale-equivariant linear map

\[
 D:H^1_{\rm CCM}\longrightarrow\mathbb P_\infty^{\rm cov}
\tag{10}
\]

whose range vectors belong to the Hilbert target annihilates every
critical resonant eigenclass.  In particular, (D) is not injective.

#### Proof

For a class (9), equivariance gives

\[
 U_tD u_\rho=D U_t^{\rm CCM}u_\rho
 =e^{it\gamma}D u_\rho.
\tag{11}
\]

Thus (D u_\rho\) is either zero or an eigenvector of the target scale
group.  Equation (7) excludes the second alternative.  Since
\(u_\rho\ne0\), injectivity fails. \(\square\)

### Corollary 4.2 — The charged closure identity is false for this target

For the concrete covariant map and Hilbert completion of 106.200--106.204,

\[
 \boxed{
 (D_Q^{\rm cov})^{-1}
 \left(
  \overline{D_Q^{\rm cov}(\mathcal V)}^{\,\mathbb P_\infty^{\rm cov}}
 \right)\ne\mathcal V.}
\tag{12}
\]

Indeed, the class of every known critical zero belongs to the left side
after passing to the quotient but not to the CCM restriction range.

## 5. The exact dichotomy exposed by the test

The charge mixing does produce a structural transverse subspace at every
real frequency: quotienting a common co-diagonal in a charge fiber of
dimension at least two leaves a codimension-one complement.  This does
not rescue the CCM resonances.

* If that transverse field is retained, it is an absolutely continuous
  defect present for almost every frequency and for arbitrary charge
  lengths.  It is not the discrete CCM torsion.
* If it is removed to match the scalar CCM restriction map, the remaining
  completed multiplier has dense range and the reduced cokernel is zero.

Thus an absolutely continuous Hilbert completion gives either a spurious
continuous cokernel or no cokernel; it cannot give the discrete resonant
degree one.

## 6. Consequence for the polarization program

The following pieces remain valid source constructions:

* the finite Tate polarizations;
* the root-graph torsion identity;
* the Gamma determinant and gradient;
* the matched finite-part identity;
* the covariant charge-mixing boundary and its positive Schur metric.

But their ordinary Hilbert completion cannot be the missing global
polarization on the existing CCM object.  The next target must retain
point evaluations and jets at a discrete divisor before Hilbert
reduction.  Equivalently, it must be a resonant nuclear, reproducing-kernel,
or derived cyclic completion rather than an (L^2)-type direct integral.
Any positive scale-unitary completion of that resonant object would then
exclude off-line exponents and hence carry the full arithmetic content.
