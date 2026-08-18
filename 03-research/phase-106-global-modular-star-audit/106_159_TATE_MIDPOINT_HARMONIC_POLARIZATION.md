# 106.159 — Tate-midpoint harmonic polarization of the prime fibres

## 1. Purpose

The positive Poisson modules of 106.152 and the Cauchy coefficient process
of 106.154 were constructed analytically.  The absolute-geometry model of
Connes--Consani supplies their missing geometric origin.  For every prime
\(p\), it constructs the rectangular Tate curve

\[
 E_p=\mathbb C^\times/p^{\mathbb Z}
 \cong C_p\times\widetilde{\mathcal X}_\infty,
 \qquad
 \tau_p=i\frac{\log p}{2\pi},                     \tag{1}
\]

with holomorphic differential

\[
 \omega_p=\frac{d\lambda}{\lambda}+i\,d\theta.   \tag{2}
\]

This note proves that the ordinary-prime factor \(p^{-|k|/2}\) is the
harmonic transfer to the self-dual midpoint of the logarithmic Tate
fundamental domain.  Thus the local coefficient polarization is the
boundary Hodge polarization of the geometric prime fibre, not an imposed
probability model.

The result is local.  It does not assert that the direct sum of the prime
fibre polarizations descends to CCM degree one; the global zero-winding and
archimedean completion remain essential.

## 2. The logarithmic cylinder and its complex structure

Write

\[
 \ell_p=\log p,
 \qquad z=e^{-x+i\theta},
 \qquad x\in\mathbb R,quad\theta\in\mathbb R/2\pi\mathbb Z.
 \tag{3}
\]

Multiplication by \(p\) translates \(x\) by \(-\ell_p\).  A logarithmic
fundamental domain therefore has width \(\ell_p\), and its self-dual
midpoint is \(x=\ell_p/2\).  The complex coordinate (3) converts (2), up
to the harmless sign of \(x\), into the standard complex differential on
the cylinder.

Let

\[
 |D|e^{ik\theta}=|k|e^{ik\theta},
 \qquad
 P_x=e^{-x|D|}.                                    \tag{4}
\]

\(P_x\) is the harmonic Poisson semigroup of the disk/cylinder obtained by
adjoining the trivial point \(z=0\).

### Theorem 2.1 — Tate-midpoint transfer

At the midpoint of the \(p\)-fundamental domain,

\[
 \boxed{
 P_{\ell_p/2}e^{ik\theta}
 =p^{-|k|/2}e^{ik\theta}.}                         \tag{5}
\]

Its integral kernel is the Poisson density

\[
 \boxed{
 P_{p^{-1/2}}(\theta-\phi)
 =\frac{1-p^{-1}}
 {1-2p^{-1/2}\cos(\theta-\phi)+p^{-1}}.}          \tag{6}
\]

#### Proof

The harmonic extension of the boundary Fourier mode \(e^{ik\theta}\) to
radius \(r=e^{-x}\) is \(r^{|k|}e^{ik\theta}\).  At
\(x=\ell_p/2\), \(r=e^{-\ell_p/2}=p^{-1/2}\), proving (5).  Summing the
absolutely convergent Fourier series

\[
 \sum_{k\in\mathbb Z}r^{|k|}e^{ik(\theta-\phi)}
\]

gives (6). □

Hence the moments used in every ordinary-prime tower are exactly harmonic
transfer coefficients on the geometric Tate fibre.

## 3. Boundary Hodge factorization

Let \(H^2(\mathbb D)\) be the Hardy space of the disk and let

\[
 a_r(z)=\frac{\sqrt{1-r^2}}{1-rz}.                 \tag{7}
\]

The boundary vector \(a_r\) is the normalized Szegő kernel at the point
\(r\in(0,1)\), and

\[
 |a_r(e^{i\theta})|^2=P_r(\theta).                 \tag{8}
\]

For a trigonometric polynomial \(F\), define its midpoint observation by

\[
 \mathcal O_pF
 :=F\,a_{p^{-1/2}}
 \in L^2(\mathbb T,d\theta/2\pi).                 \tag{9}
\]

### Theorem 3.1 — Positive local polarization from the Tate fibre

The form

\[
 g_p(F,G)
 :=\log p\,\langle\mathcal O_pF,\mathcal O_pG\rangle_{L^2(\mathbb T)}
 \tag{10}
\]

is positive definite, and its Toeplitz matrix in the character basis is

\[
 \boxed{
 g_p(e_k,e_j)
 =\log p\,p^{-|k-j|/2}.}                           \tag{11}
\]

#### Proof

Positivity follows directly from (10).  Equations (8) and (6) give

\[
 \langle e_k a_r,e_j a_r\rangle
 =\int e^{i(k-j)\theta}P_r(\theta)\frac{d\theta}{2\pi}
 =r^{|k-j|}.
\]

Set \(r=p^{-1/2}\) and multiply by \(\log p\). \(\square\)

On the underlying real boundary space, multiplication by \(i\) on the
Hardy double gives the compatible complex structure.  Equivalently, after
doubled positive/negative Fourier modes, the Hilbert transform supplies
the standard boundary complex structure.  Thus (10) is the metric part of
a genuine local polarization inherited from the complex curve \(E_p\).

## 4. Relation with the Cauchy process

The Poisson semigroup satisfies

\[
 P_xP_y=P_{x+y}.                                    \tag{12}
\]

Its Fourier exponent is (|k|), so it is the transition semigroup of the
circular Cauchy process.  Therefore the stochastic construction of
106.154 is the Markov realization of the harmonic propagation (4).  In
particular,

\[
 \mathbb E\,e^{ik(X_{\log p}-X_0)}
 =e^{-|k|\log p/2}
 =p^{-|k|/2},                                      \tag{13}
\]

after the normalization in which Cauchy time is half the logarithmic Tate
length.  The local analytic, stochastic, and absolute-geometric models are
the same polarization in three coordinates.

## 5. Rooted-divisor assembly

The arithmetic Jacobian records a rooted divisor by compatible finite
characters.  Tensor product of roots is multiplication of those
characters.  On boundary character vectors this is exactly

\[
 e_k(\theta)e_j(\theta)=e_{k+j}(\theta),           \tag{14}
\]

while harmonic propagation obeys (12).  Consequently the maps
\(\mathcal O_p\) are compatible with the monoid law before a Hilbert norm is
taken.  Distinct prime fibres are not to be declared orthogonal at this
stage; they meet through the universal phase circle
\(\widetilde{\mathcal X}_\infty\).

This identifies the correct global analysis map on a finite set \(S\) of
primes:

\[
 \mathcal O_SF
 =\bigl(\sqrt{\log p}\,F a_{p^{-1/2}}\bigr)_{p\in S},
 \tag{15}
\]

with all components evaluated on one common phase variable.  Its Gram form
is positive, but its diagonal mass is

\[
 \sum_{p\in S}\log p\,\|F\|^2,                   \tag{16}
\]

which diverges cofinally.  Equation (16) is precisely the geometric
zero-winding term found analytically in 106.152.

## 6. The global polarization equation

Let \(\mathcal O_\infty\) denote the still-required archimedean/trivial-point
analysis map.  The geometric construction must be performed before taking
the norm and must satisfy, on the common nuclear cyclic core,

\[
 \boxed{
 \Omega_{\rm CCM}(c,\star_{\rm ar}c)
 =\|\mathcal O_\infty c\|^2
  -\lim_{S\nearrow\mathcal P}
    \|\mathcal O_Sc\|^2_{\rm ren}
 =\|\mathfrak Dc\|^2.}                            \tag{17}
\]

The first equality is the exact local Lefschetz decomposition: Gamma and
the pole form the archimedean/trivial-point page, while the Tate midpoints
give every prime-power coefficient.  The second equality is the global
Hodge-index factorization.  Formula (17), unlike a scalar Euler regrouping,
requires one common phase variable and the rooted-divisor product before
renormalization.

Theorems 2.1 and 3.1 prove every finite-prime term in (17).  The missing
operation is now geometrically precise: construct the archimedean page and
its boundary gluing so that the cofinal cancellation of (16) is an
orthogonal quotient, not subtraction of two infinite numbers.  Faithfulness
must then be checked in the resonant topology of 106.158.

## 7. Status

Proved without zero input:

* the canonical complex and real structure of every Tate prime fibre;
* the exact midpoint identity \(p^{-|k|/2}\);
* the Szegő/Hardy factorization of every prime Toeplitz block;
* equality of the absolute-geometric, harmonic, and Cauchy realizations;
* compatibility with rooted-divisor character multiplication;
* identification of the global divergence with the zero-winding channel.

Still required:

* the archimedean page and the cofinal orthogonal gluing in (17);
* faithful descent of the resulting star to distributional CCM degree one.
