# 106.162 — Principal-divisor symplectic reduction collapses

## 1. Purpose

The local Tate pages carry genuine positive weight-one polarizations.  A
natural global proposal is to take their restricted product and perform
symplectic reduction by principal arithmetic divisors.  This note proves
that the ordinary reduced construction cannot produce the zero-carrying
degree one.  It either collapses to zero or leaves only a finite
degree/polar component.  The resonant information survives only in the
non-Hausdorff, unreduced quotient used by CCM.

This is a structural test of the gluing mechanism, not a sign estimate.

## 2. The polarized divisor space

Let \(\mathcal P\) be the set of ordinary primes and let
\[
 K=\ell^2(\mathcal P,w)
 \tag{1}
\]
for arbitrary positive weights \(w_p\).  On
\[
 V=K\oplus K
 \tag{2}
\]
put
\[
\begin{aligned}
 g((x,y),(x',y'))&=\langle x,x'\rangle_K+
                    \langle y,y'\rangle_K,\\
 \Omega((x,y),(x',y'))&=
       \langle x,y'\rangle_K-\langle y,x'\rangle_K,\\
 J(x,y)&=(-y,x).
\end{aligned}
\tag{3}
\]
Then \(g=\Omega(\,\cdot\,,J\,\cdot\,)\) is positive and \(J^2=-I\).
The first copy of \(K\) is the divisor-position direction and the second
is its phase dual.

Let
\[
 L_0=c_{00}(\mathcal P)\oplus\{0\}.
 \tag{4}
\]
For \(\mathbb Q\), the finite valuation vectors of principal divisors span
\(c_{00}(\mathcal P)\): the divisor of \(p\) supplies the \(p\)-th basis
vector, with its archimedean degree component treated separately below.

## 3. Collapse theorem

### Theorem 3.1 — Reduced principal quotient is zero

The closure of \(L_0\) is
\[
 \overline{L_0}=K\oplus\{0\},
 \tag{5}
\]
this subspace is Lagrangian, and
\[
 \boxed{
 \overline{L_0}^{\,\Omega}/\overline{L_0}=\{0\}.}
 \tag{6}
\]

#### Proof

Finite sequences are dense in every weighted \(\ell^2\) space, proving
(5).  If \((x,y)\in V\) is symplectically orthogonal to every
\((a,0)\in K\oplus\{0\}\), then
\[
 0=\Omega((x,y),(a,0))=-\langle y,a\rangle_K
 \quad\text{for every }a\in K.
\]
Thus \(y=0\), and
\[
 (K\oplus\{0\})^\Omega=K\oplus\{0\}.
\]
The quotient is therefore zero. \(\square\)

### Proposition 3.2 — The unreduced algebraic quotient is not polarized

Before closure,
\[
 L_0^\Omega=K\oplus\{0\},
 \qquad
 L_0^\Omega/L_0\simeq K/c_{00}(\mathcal P).
 \tag{7}
\]
The induced alternating form on (7) is identically zero.  Hence this
unreduced quotient is non-Hausdorff and has no nondegenerate polarization
induced from (3).

#### Proof

Orthogonality to all finite coordinate vectors again forces \(y=0\).
Both arguments of the induced form then lie in the position copy of
\(K\), on which \(\Omega\) vanishes identically. \(\square\)

## 4. Adding the archimedean degree does not create \(H^1\)

Let
\[
 K_{\rm ar}=K\oplus\mathbb R e_\infty
 \tag{8}
\]
and represent the principal divisor of \(p\) by
\[
 \ell_p=e_p-(\log p)e_\infty.
 \tag{9}
\]
Write \(L_{\rm pr}\) for their finite linear span in the position copy of
\(K_{\rm ar}\).

The orthogonal complement of \(L_{\rm pr}\) in \(K_{\rm ar}\) consists of
vectors \((x,c)\) satisfying
\[
 w_px_p=c\log p
 \qquad(p\in\mathcal P).
\tag{10}
\]
Therefore its dimension is at most one; it is zero unless
\[
 \sum_p\frac{(\log p)^2}{w_p}<\infty.
\tag{11}
\]
Consequently the closed principal-divisor reduction can leave at most one
position direction and its phase dual.  This is the polar \(H^0/H^2\)
degree plane, not an infinite-dimensional \(H^1\).

For the direct-sum normalization used in 106.161 one has \(w_p=1\), so
condition (11) fails.  Thus even this exceptional degree direction is not
a Hilbert vector there before the separate polar completion.

## 5. Consequence for the global construction

The arithmetic Jacobian of Connes--Consani is an idempotent Picard monoid,
not a polarized abelian variety.  Linearizing its ordinary principal
divisor quotient and then taking a positive Hilbert completion recovers
the genus-zero collapse above.  It cannot recover the distributional
infinite genus carried by the zeta resonances.

The only surviving construction has to retain the dense range as a
complex rather than quotienting by its closure:
\[
 \boxed{
 \mathfrak C_{\rm der}
 =\operatorname{Cone}\bigl(
   \mathcal L_{\rm pr}\longrightarrow\mathcal V_{\rm loc}
  \bigr).}
\tag{12}
\]
This is the derived/nonreduced analogue of the CCM cyclic cokernel.
Its resonant \(H^1\) may be nonzero even though its reduced Hilbert
cohomology is zero.  A shifted symplectic form can exist on (12), but a
positive Hodge metric does not follow from the local Hilbert metric:
Theorem 3.1 shows that ordinary harmonic representatives have all
disappeared.

Thus principal-divisor isotropy is not the missing polarization theorem.
The remaining task is to construct a positive structure directly on the
derived resonant intersection and prove that its pullback equals the CCM
trace form.

## 6. Status

Proved:

* principal valuation directions form a dense Lagrangian in every
  positive weighted \(\ell^2\) completion;
* ordinary symplectic reduction is zero;
* the algebraic quotient has a degenerate alternating form;
* the archimedean degree can add at most the trivial polar plane.

Therefore a global polarization, if it exists, must be a polarization of
the derived resonant cone, not a Kähler quotient of the local Tate
polarizations.
