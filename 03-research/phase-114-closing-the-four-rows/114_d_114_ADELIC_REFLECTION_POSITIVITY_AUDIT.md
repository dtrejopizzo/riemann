# D.114 — Adelic reflection positivity and the missing Markov coupling

## Status

There is a genuine reflection-positive structure behind the transition
from the sum-depth contact of row B to the difference-depth Green kernel of
D.110.  At one prime, the Osterwalder--Schrader (OS) quotient of the
rank-one Hankel contact reconstructs the scalar contraction \(p^{-1/2}\);
its minimal isometric/unitary dilation has covariance
\(p^{-|r-s|/2}\).  The quarter-shift Gamma oscillator admits the same OS
construction mode by mode.  Direct sums, compositions and Künneth products
are positive and correctly typed.

This local reflection positivity does not prove row D.  The exact global
form is the difference of two positive OS preparation norms.  It becomes a
sum of squares if there is a contractive adelic conditional expectation
from the prime-identity/Gamma-energy boundary space to the
prime-Poisson/Gamma-mass preparation space.  Existence of that contraction
on the two-Tate primitive image is equivalent to D.

The source-defined OS product state is place-diagonal.  Its Markov
operators preserve each prime and oscillator-mode label; the prime block
needed in the proposed conditional expectation has norm greater than one.
Thus no tensor product or Day-convolution conditional expectation supplies
the required cross-place cancellation.  A new non-product adelic Markov
state, compatible with the product formula and both Tate jets, would be a
sufficient additional structure.  It is not currently constructed by
A--B--C.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. OS data on the positive depth semigroup

Let \(\mathbb Z\) carry the Real involution \(\vartheta(r)=-r\), and let
\(\mathbb Z_{\geq0}\) be the positive semigroup.  For a translation
invariant kernel \(C(r-s)\), the OS form on positive-time vectors is the
Hankel kernel

\[
 H(r,s)=C(r+s).                                         \tag{1.1}
\]

Reflection positivity means that every finite matrix
\((H(r_i,r_j))\) is positive semidefinite.  Its null quotient and completion
give the OS Hilbert space; positive translations reconstruct a contraction
semigroup there.

This is weaker than total positivity.  It asks only positivity of the
Hankel Gram, so the counterminors of D.113 do not obstruct it.

## 2. One prime: contact, reconstruction and dilation

Fix a prime \(p\) and put \(\rho=p^{-1/2}\).  The centrally normalized
sum-depth contact is

\[
 H_p(r,s)=\log p\,\rho^{r+s},qquad r,s\geq0.           \tag{2.1}
\]

For finitely supported coefficients \(a_r\),

\[
 \sum_{r,s}\overline{a_r}H_p(r,s)a_s
 =\log p\left|\sum_ra_r\rho^r\right|^2\geq0.          \tag{2.2}
\]

Thus the OS quotient is one-dimensional.  If \(\Omega_p\) denotes its unit
vector, positive depth translation reconstructs

\[
 T_p\Omega_p=\rho\Omega_p.                              \tag{2.3}
\]

The scalar \(T_p=\rho\) is a positive self-adjoint contraction.  Its
minimal isometric dilation is the unilateral shift \(S\) on \(H^2\), with
cyclic Szegő vector

\[
 h_p(z)={\sqrt{1-\rho^2}\over1-\rho z}.                \tag{2.4}
\]

Indeed

\[
 P_{\mathbb Ch_p}S^kh_p=\rho^kh_p,qquad
 \langle S^rh_p,S^sh_p\rangle=\rho^{|r-s|}.            \tag{2.5}
\]

Consequently

\[
 \boxed{
 \text{OS sum-depth contact}
 \longrightarrow T_p=p^{-1/2}
 \longrightarrow K_p(r,s)=p^{-|r-s|/2}.}              \tag{2.6}
\]

This is the conceptual bridge between row B and the stratified Green
kernel of D.110.  Multiplication by \(\log p\) gives every
\(\Lambda(p^k)/p^{k/2}\).

## 3. Gamma oscillator OS reconstruction

Let

\[
 A_\infty e_j=(j+\tfrac14)e_j,qquad j\geq0.           \tag{3.1}
\]

For \(r,s>0\), define the heat Hankel kernel

\[
 H_\infty(r,s)
 =\langle e^{-rA_\infty}\mathbf1,
          e^{-sA_\infty}\mathbf1\rangle
 =\sum_{j\geq0}e^{-(r+s)(j+1/4)}.                      \tag{3.2}
\]

Every finite matrix from (3.2) is a Gram matrix, so it is OS positive.
The OS quotient is the direct sum of the one-dimensional mode spaces, and
positive translation reconstructs the contraction semigroup

\[
 T_\infty(t)=e^{-tA_\infty}.                            \tag{3.3}
\]

Modewise minimal dilation has difference covariance
\(e^{-|r-s|(j+1/4)}\).  Moreover

\[
 \|e^{-rA_\infty}\mathbf1\|^2
 =\operatorname{Tr}(e^{-2rA_\infty})
 ={e^{-r/2}\over1-e^{-2r}},                            \tag{3.4}
\]

which is exactly the density in the Gamma boundary derivation.  Therefore
the full Gamma oscillator, not merely its asymptotic, has a source-defined
OS realization.  Its finite-part mass channel is the positive line
\(\sqrt{m_0}\,F\), with \(m_0=\log\pi-\psi(1/4)>0\).

## 4. Künneth and place typing

If \(H_1,H_2\) are OS-positive Hankel kernels, then

\[
 H_{1\boxtimes2}((r_1,r_2),(s_1,s_2))
 =H_1(r_1,s_1)H_2(r_2,s_2)                             \tag{4.1}
\]

is positive by the Schur product theorem.  The OS quotient is the Hilbert
tensor product and the reconstructed semigroup is \(T_1\otimes T_2\).
Direct sums over primes and oscillator modes are also positive.

Thus the OS construction is compatible with the row-A Künneth tensor and
the row-B composition law.  Unlike ordinary total positivity, it does not
require a total order on the product index set.

Crucially, all these operations preserve place labels.  The product OS
state is independent/place-diagonal; it does not create maps from one prime
sector to another or from Gamma modes to prime sectors.

## 5. Exact signed preparation from the OS spaces

At a finite prime/contact cutoff, define the two source-derived maps

\[
\begin{aligned}
 Y_-F&=left((\sqrt{\log p}\,A_pF)_p,\sqrt{m_0}F\right),\\
 Y_+F&=left((\sqrt{\log p}\,F)_p,\partial_\infty F\right),
\end{aligned}                                           \tag{5.1}
\]

where

\[
 A_p=\sqrt{1-p^{-1}}(I-p^{-1/2}U_p)^{-1}.              \tag{5.2}
\]

The first component of \(Y_-\) is the minimal dilation covariance from
(2.6); the last component of \(Y_+\) is (3.4).  Hence neither map is
defined from \(B_{\rm nuc}\).

The exact A--B--C comparison gives

\[
 \boxed{
 \langle Y_+F,Y_+G\rangle-
 \langle Y_-F,Y_-G\rangle=-B_{\rm nuc}(F,G).}          \tag{5.3}
\]

The separately divergent diagonal prime norms are understood by the same
finite-cutoff paired stabilization as in D.111.

## 6. Conditional expectation and square decomposition

Suppose there is a contraction

\[
 \mathbb E_X:\overline{Y_+(\mathcal P)}
 \longrightarrow\overline{Y_-(\mathcal P)},qquad
 Y_-F=\mathbb E_XY_+F                                   \tag{6.1}
\]

for every two-Tate primitive \(F\).  Then

\[
\begin{aligned}
 -B_{\rm nuc}(F,G)
 &=\langle Y_+F,(I-\mathbb E_X^*\mathbb E_X)Y_+G\rangle\\
 &=\langle D_XY_+F,D_XY_+G\rangle,                     \tag{6.2}
\end{aligned}
\]

where \(D_X=(I-\mathbb E_X^*\mathbb E_X)^{1/2}\).  This is the desired
reflection-positive decomposition into squares.

Conversely, the assignment

\[
 Y_+F\longmapsto Y_-F                                   \tag{6.3}
\]

extends to a contraction if and only if the Pick matrices

\[
 \left(
 \langle Y_+F_i,Y_+F_j\rangle-
 \langle Y_-F_i,Y_-F_j\rangle
 \right)_{i,j}                                         \tag{6.4}
\]

are positive for every finite primitive family.  By (5.3), this is exactly
matrix positivity of \(-B_{\rm nuc}\) on the primitive space.  Scalar
positivity and polarization already imply the matrix condition.

Thus existence of the linear contraction (6.1) is equivalent to D.  A
genuine conditional expectation between OS probability/operator algebras
would be stronger and would imply it automatically.

## 7. Why the product OS Markov structure does not supply it

The source product state gives only block-diagonal Markov maps.  On a prime
block, (6.1) would have to realize

\[
 F\longmapsto A_pF.
\]

But

\[
 \|A_p\|=\sqrt{{1+p^{-1/2}\over1-p^{-1/2}}}>1.         \tag{7.1}
\]

Hence no place-diagonal conditional expectation can implement (6.1).
The Gamma mass and Gamma energy blocks likewise point in opposite
directions and do not form a conditional expectation by themselves.

Tensor products and Day convolution preserve this block typing.  They
cannot turn an expanding local block into a global contraction because
they provide no off-diagonal prime--Gamma covariance.  The nuclear scalar
algebra labels the common actions and traces, but its constructed state is
not a positive adelic probability state coupling the places.

## 8. The missing adelic Markov datum

A noncircular sufficient structure would be:

> **Adelic OS--Markov coupling.**  A reflection-positive, non-product state
> on the completed prime--Gamma boundary algebra, together with a
> Real/Fourier covariant conditional expectation \(\mathbb E_X\) satisfying
> (6.1), preserving both Tate boundary characters and compatible with
> Künneth and cofinal restriction.

Conditional expectations in a positive state are contractions, so this
axiom would prove (6.2) without a separate spectral estimate.  But at the
two-point level its covariance condition is already (6.4), hence D.  To be
an independent proof, the state and expectation must be constructed from a
geometric Markov/product-formula mechanism before evaluating their
covariance.

The local OS systems do not determine such a non-product state.  Taking
their independent product gives zero cross-place covariance and fails
(7.1).  Defining the state by the kernel in (5.3) assumes the desired
positivity and is excluded.

## 9. Outcome

Reflection positivity supplies a genuine new conceptual identification:

\[
 \boxed{
 \Lambda(p^{r+s})p^{-(r+s)/2}
 \ \xrightarrow{\rm OS}\
 p^{-1/2}
 \ \xrightarrow{\rm dilation}\
 (\log p)p^{-|r-s|/2}.}
\]

The Gamma heat module has the same OS origin, and all local/Künneth typing
is complete.  What remains is not local reflection positivity but an
adelic conditional expectation mixing the places.  Its norm-one property
is equivalent to the row-D primitive sign unless a new geometric
product-formula construction forces it independently.
