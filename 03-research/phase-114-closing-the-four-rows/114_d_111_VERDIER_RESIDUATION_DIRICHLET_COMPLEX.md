# D.111 — Verdier/residuation duality and the sharp Dirichlet axiom

## Status

The stratified polar system of D.110 has a canonical two-term
Koszul--Jacobi complex.  Its Hilbert dual is induced by the residuation
adjoint, its Green operator is exactly the prime kernel
\(p^{-|r-s|/2}\), and its failure of perfect bilateral duality is a
rank-one boundary contact.  Tensor products give the expected Künneth
duality.

After adding all prime-power difference edges and the quarter-shift Gamma
heat module, one obtains a positive Dirichlet complex whose quadratic form
satisfies

\[
 \|\partial_XF\|^2-(2A_X+m_0)\|F\|^2=-B_{\rm nuc}(F,F).
\]

Thus every boundary term, including Gamma, is calculated independently of
the desired sign.

Verdier dualizability, enriched Yoneda, Day convolution and nuclearity do
not imply the required sharp lower bound.  They give adjoints, traces and
summability; closed range would give some positive Poincaré constant on a
fixed primitive window, but not the exact constant \(2A_X+m_0\).
The minimal additional assertion is a norm bound for the primitive Green
operator.  That assertion is algebraically equivalent to row D, so it may
be used as the next theorem to prove but not as an already available
consequence of A--B--C.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Local Koszul--Jacobi complex

For a prime \(p\), put \(\rho=p^{-1/2}\), let \(S\) be the unilateral shift
on \(H_p=\ell^2(\mathbb Z_{\geq0})\), and define

\[
 d_p={I-\rho S^*\over\sqrt{1-\rho^2}}:H_p\longrightarrow H_p.       \tag{1.1}
\]

This is the stationary limit of the lowering maps furnished by the polar
residuation correspondence of D.110.  Since \(\|\rho S^*\|<1\), it is
invertible.  The two-term complex

\[
 \mathcal K_p:\quad 0\longrightarrow H_p
 \xrightarrow{d_p}H_p\longrightarrow0                 \tag{1.2}
\]

is perfect at every finite depth and contractible after Hilbert completion.
Its Laplacian in degree zero is

\[
 \Delta_{p,0}=d_p^*d_p
 ={(I-\rho S)(I-\rho S^*)\over1-\rho^2}.                \tag{1.3}
\]

The Green operator is

\[
 \Delta_{p,0}^{-1}
 =(1-\rho^2)(I-\rho S^*)^{-1}(I-\rho S)^{-1},           \tag{1.4}
\]

and direct multiplication gives

\[
 \langle e_r,\Delta_{p,0}^{-1}e_s\rangle
 =\rho^{|r-s|}=p^{-|r-s|/2}.                            \tag{1.5}
\]

Thus the Green kernel is obtained before applying the row-C trace.

## 2. Duality and the prime boundary contact

The row-A ordered-frame metric identifies each finite cotangent with its
dual.  Under this identification, Verdier duality of (1.2) reverses the
arrow and replaces \(d_p\) by \(d_p^*\).  The degree-one Laplacian is

\[
 \Delta_{p,1}=d_pd_p^*.
\]

Using \(S^*S=I\) and \(SS^*=I-P_0\), where
\(P_0=|e_0\rangle\langle e_0|\), one finds

\[
 \Delta_{p,0}-\Delta_{p,1}
 =-{\rho^2\over1-\rho^2}P_0.                           \tag{2.1}
\]

This rank-one term is the boundary left by passing from the bilateral
depth orbit to the effective half-orbit.  Multiplication by the periodic
Haar/contact length \(\log p\) gives its arithmetic normalization.

For two primes, the stratified residual Jacobian is a tensor product and
its polar part is a tensor product.  Hence

\[
 \mathbb D(\mathcal K_p\widehat\otimes\mathcal K_q)
 \simeq\mathbb D\mathcal K_p\widehat\otimes
       \mathbb D\mathcal K_q,                           \tag{2.2}
\]

with the usual Koszul sign.  This is the Verdier/Künneth pairing supplied
by periodic Yoneda and Day convolution.

## 3. The positive global boundary differential

Return to logarithmic tests \(F\in C_c^\infty(\mathbb R)\).  For a finite
contact cutoff \(X\), define

\[
 (\partial_{{\rm fin},X}F)_n
 =\left({\Lambda(n)\over\sqrt n}\right)^{1/2}
   (F-S_{\log n}F),\qquad 2\leq n\leq X.                \tag{3.1}
\]

The coefficient in (3.1) is now source-derived in three steps:

1. D.110's residuation Green gives \(p^{-k/2}\);
2. the A--B reduced contact gives \(\log p\);
3. the cyclotomic contact is zero off prime powers.

At the real place use

\[
 (\partial_\infty F)(x,j,t)
 =2^{-1/2}e^{-x(j+1/4)/2}\bigl(F(t)-F(t-x/2)\bigr).     \tag{3.2}
\]

The completed positive differential is

\[
 \partial_X=\partial_{{\rm fin},X}\oplus\partial_\infty.           \tag{3.3}
\]

Its quadratic form is

\[
\begin{aligned}
 \|\partial_XF\|^2={}&
 \sum_{2\leq n\leq X}{\Lambda(n)\over\sqrt n}
       \|F-S_{\log n}F\|^2\\
 &+\int_0^\infty{e^{-r/2}\over1-e^{-2r}}
       \|F-S_rF\|^2\,dr.                               \tag{3.4}
\end{aligned}
\]

Both summands are positive and defined without \(B_{\rm nuc}\).

## 4. Exact boundary expansion

Put

\[
 A_X=\sum_{2\leq n\leq X}{\Lambda(n)\over\sqrt n},
 \qquad m_0=\log\pi-\psi(1/4).                         \tag{4.1}
\]

Expanding each finite difference gives

\[
\begin{aligned}
 \|\partial_{{\rm fin},X}F\|^2
 ={}&2A_X\|F\|^2\\
 &-2\operatorname{Re}
   \sum_{2\leq n\leq X}{\Lambda(n)\over\sqrt n}
       \langle F,S_{\log n}F\rangle.                   \tag{4.2}
\end{aligned}
\]

The heat trace of \(j+1/4\) and the digamma difference formula give

\[
 \|\partial_\infty F\|^2
 =m_0\|F\|^2-G_\infty(F,F).                            \tag{4.3}
\]

For \(X\) large enough for the paired support, the explicit-formula
assembly of A--B--C identifies the remaining correlations in (4.2) and
(4.3).  Therefore

\[
 \boxed{
 \|\partial_XF\|^2-(2A_X+m_0)\|F\|^2
 =-B_{\rm nuc}(F,F).}                                   \tag{4.4}
\]

Equation (4.4) is an equality of boundary terms, not a positivity claim.

## 5. Primitive trace complex

Let

\[
 \operatorname{Tr}_{\rm Tate}F=(M_-(F),M_+(F)),qquad
 \mathcal P=\ker\operatorname{Tr}_{\rm Tate}.           \tag{5.1}
\]

At a fixed support window, the moments are continuous and \(\mathcal P\)
is closed.  The relevant three-term complex is

\[
 0\longrightarrow\mathcal P
 \longrightarrow\operatorname{Dom}(\partial_X)
 \xrightarrow{\operatorname{Tr}_{\rm Tate}}\mathbb C^2
 \longrightarrow0,                                    \tag{5.2}
\]

together with the positive differential \(\partial_X|_{\mathcal P}\).
Write

\[
 H_X=(\partial_X|_{\mathcal P})^*
       (\partial_X|_{\mathcal P}).                     \tag{5.3}
\]

Row D is the sharp lower bound

\[
 H_X\geq(2A_X+m_0)I_{\mathcal P}.                       \tag{5.4}
\]

Whenever the primitive differential has closed range and trivial kernel,
its Green operator \(G_X=H_X^{-1}\) exists as a bounded positive operator.
But closed range proves only

\[
 H_X\geq c_XI
\]

for some \(c_X>0\).  The required assertion is the precise norm estimate

\[
 \boxed{\|G_X\|\leq(2A_X+m_0)^{-1}.}                   \tag{5.5}
\]

Equations (4.4) and (5.1) show that (5.4), (5.5) and
\(B_{\rm nuc}|_{\mathcal P}\leq0\) are equivalent.

## 6. What the existing categorical structures imply

The A--B--C structures prove the following.

* **Periodic Yoneda:** the section objects and their multiplication are
  internal, and representables have the expected derived Hom.
* **Day convolution:** external products and the Künneth maps are
  associative and symmetric monoidal.
* **Residuation polar duality:** the finite-depth raising maps have candid
  metric adjoints, giving (1.2)--(2.2).
* **Nuclearity:** the global character and the required operator traces are
  summable in the declared Fréchet category.

None of these is an order theorem.  Dualizability produces a nondegenerate
evaluation pairing, not a positive Hodge--Riemann polarization.  A
nuclear/compact map of infinite rank is not forced to have closed range;
in Hilbert space, a compact operator with closed range has finite rank.
Even when closed range is separately known, its smallest singular value is
not fixed by monoidality or trace class.

The finite-dimensional countermodel is decisive.  Every finite-dimensional
real vector space is dualizable and nuclear, ordinary tensor product is a
Day-convolution model, and standard duality is positive.  Nevertheless,
for

\[
 S=2I,\qquad B=I,                                       \tag{6.1}
\]

one has closed range for both maps but

\[
 \|Sx\|^2-\|Bx\|^2=3\|x\|^2>0.                         \tag{6.2}
\]

Thus those formal properties cannot imply the orientation or the sharp
constant in (5.4).

## 7. The minimal additional Hodge axiom

The exact extra datum can be stated without mentioning zeta zeros.

> **Primitive Green contraction.**  For every compatible support/contact
> cutoff \(X\), the primitive Dirichlet complex (5.2) has a Green operator
> and its norm satisfies (5.5), compatibly under restriction and cofinal
> passage.

Equivalently, by Douglas factorization, on every finite window there is a
contraction \(C_X\) such that

\[
 \sqrt{2A_X+m_0}\,I_{\mathcal P}
 =C_X\,\partial_X|_{\mathcal P}.                        \tag{7.1}
\]

This is the minimal Hodge polarization missing from the currently
constructed Verdier object.  It is exactly strong enough to prove row D
by (4.4), and no stronger spectral or Chow assertion is required.

The next viable route is therefore not another formal duality.  It must
construct \(C_X\) geometrically -- for example as a norm-one boundary
Poisson/Calderón map forced by the stratified section object -- and prove
its compatibility with both Tate traces.  Defining \(C_X\) by the polar
decomposition of \(\partial_X\) would be circular unless the norm bound
(5.5) is proved independently.

