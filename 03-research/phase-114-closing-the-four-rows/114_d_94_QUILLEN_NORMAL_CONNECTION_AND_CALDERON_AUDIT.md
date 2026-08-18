# D.94 — Quillen normal connection and Calderon audit

## Status

There is an exact determinant-line origin for the full row-C multiplier.
On a finite Bloch local system the determinant of `I-p^(-s)U` has normal
logarithmic derivative equal to the complete `p^k` tower.  The zeta
determinant of the shifted harmonic oscillator has normal logarithmic
derivative equal to the complete Gamma multiplier, including its
finite-part constant.  Their product is the completed Euler determinant.

This proves a stronger geometric comparison than a coefficient Hessian:
`B_nuc` is the pullback of the normal connection one-form of the completed
local determinant line.  It also explains intrinsically why radial
differentiation removes the `1/k` in the logarithm and produces
`Lambda(p^k)` rather than `Lambda(p^k)/k`.

The same calculation identifies the remaining obstruction.  The local
determinant metrics are pluriharmonic away from their divisor, so their
Quillen curvature is zero there.  Their normal connection is sign
indefinite and is not a positive Dirichlet-to-Neumann operator.  After
global analytic continuation, the functional equation makes the regular
normal derivative vanish on the central line; the arithmetic boundary
distribution is balanced by the divisor current of zeros and poles.
Asserting that this divisor current is supported on the central line is
the RH localization, not an available positivity theorem.

Thus the determinant route derives every coefficient and both mass terms
without tuning, but it does not yet derive the Hodge sign.  A positive
Calderon realization of its normal connection would be equivalent to the
missing global polarization unless constructed independently of the
completed divisor.

No RH statement or sign of `B_nuc` is used.  The paper is not modified.

## 1. Finite-place determinant over Bloch local systems

Let `s=sigma+i tau`, `L=log p`, and let the holonomy of a one-dimensional
Bloch local system be `e^(i theta)`.  On that fibre put

\[
 D_p(s,\theta)=\det(1-p^{-s}e^{i\theta})
              =1-p^{-s}e^{i\theta}.                       \tag{1.1}
\]

For `sigma>0` its inverse determinant potential is

\[
 \begin{aligned}
 \Phi_p(\sigma,\tau,\theta)
 &:=-\log|D_p(s,\theta)|^2\\
 &=2\sum_{k\ge1}{p^{-k\sigma}\over k}
       \cos k(\theta-\tau L).                              \tag{1.2}
 \end{aligned}
\]

The series and all radial derivatives converge normally on
`sigma>=epsilon>0`.  Therefore

\[
 \boxed{
 -\partial_\sigma\Phi_p
 =2L\sum_{k\ge1}p^{-k\sigma}
       \cos k(\theta-\tau L).}                             \tag{1.3}
\]

Equivalently, with `r=p^(-sigma)` and the Poisson kernel `P_r`,

\[
 -\partial_\sigma\Phi_p
 =L\bigl(P_r(e^{i(\theta-\tau L)})-1\bigr).                \tag{1.4}
\]

At the central value `sigma=1/2` and trivial coefficient holonomy
`theta=0`, this is exactly

\[
 2\sum_{k\ge1}{\Lambda(p^k)\over\sqrt{p^k}}
       \cos(k\tau\log p).                                 \tag{1.5}
\]

The factor `1/k` in the determinant logarithm is removed by the normal
Euler derivative because

\[
 -\partial_\sigma {p^{-k\sigma}\over k}
 =L p^{-k\sigma}.                                         \tag{1.6}
\]

Thus the von Mangoldt coefficient is a connection coefficient of the
determinant family; it is not inserted after the fact.

For a general unitary finite-rank local system with holonomy `U`, the same
formula follows by diagonalizing `U`:

\[
 -\partial_\sigma[-\log|\det(I-p^{-s}U)|^2]
 =2L\operatorname{Re}\sum_{k\ge1}p^{-ks}{\operatorname{tr}U^k}.
                                                                    \tag{1.7}
\]

## 2. Gamma as a zeta determinant of the oscillator

For `a` off the nonpositive integers, the Hurwitz identity gives

\[
 \det_\zeta(N+a)
 =\exp[-\zeta_H'(0,a)]={\sqrt{2\pi}\over\Gamma(a)}.       \tag{2.1}
\]

Consequently the archimedean local factor

\[
 D_\infty(s)=\pi^{-s/2}\Gamma(s/2)                         \tag{2.2}
\]

is, up to the displayed elementary normalization, the inverse zeta
determinant of the shifted oscillator `N+s/2`.  Its normal connection is

\[
 \begin{aligned}
 -\partial_\sigma\log|D_\infty(s)|^2
 &=\log\pi-\operatorname{Re}\psi(s/2).                    \tag{2.3}
 \end{aligned}
\]

On the central line this becomes

\[
 \boxed{
 m_\infty(\tau)
 =\log\pi-\operatorname{Re}\psi(1/4+i\tau/2).}           \tag{2.4}
\]

Writing `a_j=j+1/4`, the digamma difference formula gives the exact split

\[
 \begin{aligned}
 m_\infty(\tau)
 &=m_0-\ell_\infty(\tau),\\
 m_0&=\log\pi-\psi(1/4),\\
 \ell_\infty(\tau)
 &=\sum_{j\ge0}{1\over a_j}
       {\tau^2\over4a_j^2+\tau^2}.                        \tag{2.5}
 \end{aligned}
\]

This is precisely the `m_0 I-partial_infinity^* partial_infinity` block of
D.32.  In particular the Gamma mass is produced by the oscillator
determinant normalization and is not appended to the Dirichlet energy.

## 3. Exact completed pullback

In the half-plane `sigma>1`, where the Euler product converges absolutely,

\[
 \Lambda(s):=D_\infty(s)\prod_pD_p(s,0)^{-1}
 =\pi^{-s/2}\Gamma(s/2)\zeta(s).                          \tag{3.1}
\]

Combining (1.3) and (2.3) yields

\[
 \begin{aligned}
 -\partial_\sigma\log|\Lambda(s)|^2
 ={}&2\sum_{p,k\ge1}{\Lambda(p^k)\over p^{k\sigma}}
       \cos(k\tau\log p)\\
 &+\log\pi-\operatorname{Re}\psi(s/2).                   \tag{3.2}
 \end{aligned}
\]

The right side admits the row-C nuclear/distributional boundary value at
`sigma=1/2`.  Under Fourier transform in the logarithmic variable it is
exactly the multiplier of `B_nuc`; equivalently, for primitive Schwartz
tests `f,g`,

\[
 \boxed{
 B_{\rm nuc}(f,g)
 =\left\langle f,
   \left[-\nabla_\nu\log\|\lambda_{\rm comp}\|_Q^2
   \right]_{\sigma=1/2}g\right\rangle.}                  \tag{3.3}
\]

Here (3.3) means the boundary connection distribution obtained by pairing
(3.2) with the Schwartz correlation; it is not a pointwise convergent sum
of prime functions.  The two primitive jets are exactly

\[
 M_-(f)=\widehat f(-i/2),\qquad
 M_+(f)=\widehat f(i/2),                                  \tag{3.4}
\]

as established in D.32.  Thus (3.3) is the requested pullback on the
kernel of the two A--B--C Tate moments and includes every `p^k` and the
entire Gamma factor.

## 4. Connection is not curvature

For fixed Bloch holonomy, `D_p(s,theta)` is holomorphic and nonzero on the
local half-plane.  Hence

\[
 \partial_s\partial_{\bar s}\log|D_p(s,\theta)|^2=0        \tag{4.1}
\]

away from its divisor.  The same holds for `D_infinity(s)` away from the
Gamma poles.  Therefore the exact multiplier (3.2) is a **normal
connection coefficient**, not the value of a positive Quillen curvature
form.

This distinction is visible already at one prime.  The boundary symbol

\[
 L(P_r(e^{i\theta})-1)                                   \tag{4.2}
\]

is positive at `theta=0` and negative at `theta=pi`.  A positive
Calderon/Dirichlet-to-Neumann operator or the Schur complement of a
positive block operator is positive semidefinite.  It therefore cannot
equal (4.2) on the full Bloch boundary.

The Hardy evaluation covariance `P_r` is positive.  The desired operator
is the signed difference

\[
 P_r-I.                                                   \tag{4.3}
\]

Likewise the Gamma block is the signed difference

\[
 m_0I-\partial_\infty^*\partial_\infty.                  \tag{4.4}
\]

A positive Schur complement can produce neither signed difference before
the global two-jet restriction.  Making it do so by choosing an
indefinite ambient metric recovers the exact Krein factorization of D.32,
but supplies no Hodge sign.

## 5. Functional equation and the divisor current

Analytic continuation of the completed factor satisfies

\[
 \Lambda(s)=\Lambda(1-s).                                \tag{5.1}
\]

Reality of the coefficients implies

\[
 |\Lambda(\sigma+i\tau)|
 =|\Lambda(1-\sigma+i\tau)|.                             \tag{5.2}
\]

At every regular point of the central line,

\[
 \partial_\sigma\log|\Lambda(\sigma+i\tau)|^2
 \big|_{\sigma=1/2}=0.                                   \tag{5.3}
\]

There is no contradiction with (3.2): the Euler boundary connection is
not an ordinary pointwise Euler sum on the central line.  Under analytic
continuation it is balanced by the divisor current of zeros and poles.
In Poincare--Lelong language, curvature is concentrated on that divisor,
while the local determinant metrics are flat off it.

Therefore a proposed positive DtN theorem must specify its source terms.
If it assumes that all nontrivial divisor sources lie on the central line,
it assumes RH.  If it discards them, (5.3) leaves a zero regular normal
connection rather than (3.3).  If it retains them without localization,
the sign of the resulting boundary distribution is precisely the Weil
criterion to be proved.

## 6. Exact outcome and next gate

The determinant family establishes all of the following without a gap:

1. the two primitive jets are the two central Tate moments;
2. radial differentiation removes `1/k` and produces every
   `Lambda(p^k)/sqrt(p^k)`;
3. the oscillator zeta determinant produces the complete Gamma block and
   its mass `m_0`;
4. the pullback of the completed normal connection is exactly `B_nuc`.

It does **not** establish that this normal connection is the boundary form
of a positive bulk Laplacian.  The remaining noncircular gate is therefore
more precise:

\[
 \boxed{\text{construct a positive bulk object whose boundary source
 decomposition yields (3.3), including its divisor current, and prove
 that the primitive two-jet kernel selects its negative polarization.}}
                                                                    \tag{6.1}
\]

Any construction whose bulk Green function or Calderon projector is
defined using the sign of (3.3) merely restates row D.  The next admissible
test is whether the **canonical functional-equation double** of the
determinant line supplies such a positive bulk before the divisor is
localized.

