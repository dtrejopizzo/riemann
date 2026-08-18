# 106.193 — The prime Poisson precision connection

## 1. Purpose

The thermal standard-form calculation of 106.192 shows that the apparent
left--right prime double collapses to one line.  It also reveals a
nontrivial direction which does not collapse: for each fixed gauge charge,
the common-valuation multiplicities have Gram kernel

\[
 K_p(h,k)=p^{-|h-k|/2},\qquad h,k\in\mathbb N_0.            \tag{1}
\]

This note factors the inverse of (1).  The result is an exact positive
first-order connection

\[
 x_{h+1}-p^{-1/2}x_h,                                      \tag{2}
\]

with a single boundary value at \(h=0\).  Thus the prime coefficient is
the Green kernel of a source-defined local Dirichlet operator.  This is
the off-diagonal multiplicity structure which a non-free Gamma--Euler
relative differential must preserve.

## 2. The fixed-charge Poisson space

Fix \(0<a<1\).  Let \(K_a\) be the operator on
\(\ell^2(\mathbb N_0)\) with matrix

\[
 (K_a)_{h,k}=a^{|h-k|}.                                    \tag{3}
\]

The Fourier symbol of the bilateral kernel is

\[
 P_a(e^{i\theta})
 =\frac{1-a^2}{1-2a\cos\theta+a^2},                        \tag{4}
\]

so compression to the half-line gives the operator bounds

\[
 \frac{1-a}{1+a}I\le K_a\le\frac{1+a}{1-a}I.              \tag{5}
\]

In particular \(K_a\) is bounded and boundedly invertible.

For a fixed charge in Theorem 3.1 of 106.192, take
\(a=p^{-1/2}\).  The synthesis vectors
\(E_h=E_{a_0+h,b_0+h}^{(p)}\) have Gram operator \(K_a\).

## 3. Exact Cholesky precision

Define \(B_a\) initially on finite sequences by

\[
 (B_ax)_0=x_0,
 \qquad
 (B_ax)_{h+1}
 =\frac{x_{h+1}-ax_h}{\sqrt{1-a^2}}.                       \tag{6}
\]

### Theorem 3.1 — Poisson precision factorization

The map \(B_a\) extends to a bounded invertible operator on
\(\ell^2(\mathbb N_0)\), and

\[
 \boxed{K_a^{-1}=B_a^*B_a.}                                \tag{7}
\]

Equivalently, for every \(x\in\ell^2(\mathbb N_0)\),

\[
 \boxed{
 \langle K_a^{-1}x,x\rangle
 =|x_0|^2+rac1{1-a^2}
   \sum_{h\ge0}|x_{h+1}-ax_h|^2.}                         \tag{8}
\]

#### Proof

Let \((\varepsilon_h)_{h\ge0}\) be an orthonormal basis and define the
lower-triangular operator \(L_a\) by

\[
 (L_a\varepsilon)_h
 =a^h\varepsilon_0
  +\sqrt{1-a^2}\sum_{j=1}^{h}a^{h-j}\varepsilon_j.         \tag{9}
\]

The covariance of the right side is

\[
 a^{h+k}+(1-a^2)
 \sum_{j=1}^{\min(h,k)}a^{h+k-2j}
 =a^{|h-k|}.                                               \tag{10}
\]

Hence

\[
 L_aL_a^*=K_a.                                             \tag{11}
\]

Solving (9) recursively gives

\[
 \varepsilon_0=x_0,
 \qquad
 \varepsilon_{h+1}
 =\frac{x_{h+1}-ax_h}{\sqrt{1-a^2}},                       \tag{12}
\]

so \(B_a=L_a^{-1}\).  Equations (5) and (11) show that both
operators extend boundedly and invertibly to \(\ell^2\).  Therefore

\[
 K_a^{-1}=(L_a^{-1})^*L_a^{-1}=B_a^*B_a,
\]

and (8) follows. \(\square\)

## 4. The local arithmetic connection

For a prime \(p\), put

\[
 a_p=p^{-1/2},qquad
 (\nabla_px)_h
 =\frac{x_{h+1}-p^{-1/2}x_h}{\sqrt{1-p^{-1}}},qquad
 \partial_px=x_0.                                         \tag{13}
\]

Then (8) becomes

\[
 \boxed{
 \langle K_p^{-1}x,x\rangle
 =|\partial_px|^2+\|\nabla_px\|_2^2.}                     \tag{14}
\]

The local Euler factor appears literally in the first-order difference:

\[
 \nabla_p=(1-p^{-1})^{-1/2}(S^*-p^{-1/2}I).                \tag{15}
\]

Thus \(p^{-k/2}\) is not merely a positive overlap.  It is the Green
propagator of the connection (15) with the boundary functional
\(\partial_p\).

### Corollary 4.1 — Exact local positive polarization

On the real double of the fixed-charge value space, let

\[
 \mathcal D_p x=(\partial_px,\nabla_px),                    \tag{16}
\]

and use the standard complex structure on two copies.  Then

\[
 g_p(x,y)=\langle\mathcal D_px,\mathcal D_py\rangle         \tag{17}
\]

is positive definite and has Green kernel (1).  It is defined entirely
from the ordinary prime \(p\).

## 5. Cofinal behavior

For each fixed prime, (14) is uniformly coercive.  Globally, however,

\[
 \sum_p a_p^2=\sum_p\frac1p=\infty.                        \tag{18}
\]

Consequently the infinite tensor product of the local changes of
coordinates \(B_{a_p}\) is not a bounded perturbation of the reference
tensor product.  This is the precision-side form of the white-light
transition of 106.164.

The divergence in (18) is scalar and logarithmic, but removing only its
scalar part does not determine the finite boundary sign.  The matched
cutoff theorem of 106.181 already proves that the scalar divergence
cancels against the Gamma--polar boundary.  What (14) adds is the exact
non-scalar connection which must be retained during that cancellation.

## 6. Required global coupling

Let \(E\) denote total energy and \(q\) an arithmetic charge.  Combining
106.192(24) with (13) forces the finite/infinite-place differential to
have the schematic form

\[
 \boxed{
 \mathcal D_{\rm rel}(E)
 =\bigoplus_p\sqrt{\log p}\,\nabla_p
  \;\widehat\oplus\;
  \Gamma_\infty(E-\log q)
  \;\widehat\oplus\;\partial_{\rm polar},}                \tag{19}
\]

but with a **shared** boundary component: the maps in (19) cannot be
orthogonally summed after separate completion.  Their scalar boundary
values must be identified before taking the norm, exactly as in the
matched-cutoff Green identity.

If they were summed orthogonally, positivity would be automatic but the
result would be the free/coisometric object excluded by 106.189.  The
remaining construction is therefore a boundary pushout of the local
connections (13) with the Gamma and polar trace maps.

## 7. Status

Proved without RH or zero input:

* exact inversion of the prime Poisson kernel;
* a first-order local arithmetic connection and boundary trace;
* a positive local Dirichlet factorization whose Green kernel is
  \(p^{-|h-k|/2}\);
* identification of the logarithmic cofinal obstruction;
* the precise boundary-pushout form required of the global relative
  differential.

Still required:

* construct the shared Gamma--Euler--polar boundary pushout in the
  nuclear category;
* prove that its Hilbert torsion is faithful on CCM degree one;
* verify uniform boundedness of normalized scaling and bounded weak
  nondegeneracy of the descended alternating form.

