# Vaughan--Heath-Brown audit for the prime--Laguerre correlation

## Verdict

Vaughan's identity applies exactly to the direct A1 prime sum, but it does
not create a new oscillatory direction. In logarithmic coordinates every
factorisation variable enters the Laguerre phase only through their sum. The
phase Hessian therefore has rank one, independently of the number of
variables introduced by Vaughan or Heath--Brown.

In the central Laguerre bulk, a multiplicative dyadic block changes the
Plancherel--Rotach phase by only \(O(1)\), uniformly in the degree. Thus the
usual Type I/II decomposition does not turn A1 into a high-frequency
exponential sum on each arithmetic block. Any saving in the flat
factorisation directions would have to come from a new estimate for the
Möbius/von Mangoldt coefficients, not from the Laguerre oscillation.

There is also an exact Laguerre addition formula which separates a
rectangular bilinear block into \(N+1\) rank-one pieces. Without a new signed
estimate among those pieces, summing their magnitudes recreates the absolute
Laguerre load already ruled out in Phase 102.

Consequently the *plain* Vaughan/Heath--Brown proposal is discarded as a
closure mechanism. A viable successor would have to prove cancellation
jointly across many multiplicative shells; that is additional mathematics,
not a consequence of standard Type I/II machinery.

## 1. Exact interior sum

Put \(N=n-1\), \(X_N=e^{4N}\), and

\[
 W_N(r)={\bf1}_{r\le X_N}{1\over r}L_N^{(1)}(\log r).
\tag{1}
\]

The moving prime part of the direct A1 certificate, restricted to the
oscillatory range, is

\[
 S_N=\sum_{r\ge2}\Lambda(r)W_N(r).
\tag{2}
\]

The range past \(4N\) has no Laguerre sign changes and is handled separately
by the outer-tail estimates of `103_09`; it is not relevant to the Type I/II
phase question.

For \(U,V\ge1\), write

\[
 \mu_{\le U}(d)=\mu(d){\bf1}_{d\le U},\qquad
 \Lambda_{\le V}(e)=\Lambda(e){\bf1}_{e\le V}.
\]

The convolution identities \(\Lambda=\mu*\log\) and
\(\log=\Lambda*1\) give the exact Vaughan decomposition

\[
 \boxed{
 \Lambda
 =\mu_{\le U}*\log
  -\mu_{\le U}*\Lambda_{\le V}*1
  +\mu_{>U}*\Lambda_{>V}*1
  +\Lambda_{\le V}.}
\tag{3}
\]

Indeed, expand \(\mu*\log\), use \(\log=\Lambda*1\) in the
\(\mu_{>U}\) part, and replace
\(\mu_{>U}*\Lambda_{\le V}*1\) by
\(\Lambda_{\le V}-\mu_{\le U}*\Lambda_{\le V}*1\).

Pairing (3) with the finite weight (1) yields

\[
 S_N=S_{I,1}-S_{I,2}+S_{II}+S_0,
\tag{4}
\]

where

\[
\begin{aligned}
 S_{I,1}
 &=\sum_{d\le U}\mu(d)
   \sum_{\ell\le X_N/d}(\log\ell)W_N(d\ell),\\
 S_{I,2}
 &=\sum_{d\le U}\mu(d)
   \sum_{e\le V}\Lambda(e)
   \sum_{k\le X_N/(de)}W_N(dek),\\
 S_{II}
 &=\sum_{d>U}\mu(d)
   \sum_{e>V}\Lambda(e)
   \sum_{k\le X_N/(de)}W_N(dek),\\
 S_0&=\sum_{e\le V}\Lambda(e)W_N(e).
\end{aligned}
\tag{5}
\]

All sums are finite, so (4)--(5) require no limiting convention. Regrouping
\(r=ek\) in the third line gives the classical bilinear form

\[
 S_{II}=\sum_{\substack{d>U,\ r\ge1\\dr\le X_N}}
 \mu(d)b_V(r)W_N(dr),
 \qquad
 b_V(r)=\sum_{\substack{e\mid r\\e>V}}\Lambda(e).
\tag{6}
\]

Thus the proposed attack really reaches a Type II sum. The remaining
question is whether its weight supplies exploitable oscillation.

## 2. Exact separation and its cost

The Laguerre addition theorem gives

\[
 \boxed{
 L_N^{(1)}(x+y)
 =\sum_{j=0}^{N}L_j(x)L_{N-j}(y).}
\tag{7}
\]

Consequently, before the hyperbolic cutoff is imposed,

\[
 {1\over dr}L_N^{(1)}(\log d+\log r)
 =\sum_{j=0}^{N}
  {L_j(\log d)\over d}
  {L_{N-j}(\log r)\over r}.
\tag{8}
\]

On a rectangular dyadic block contained in \(dr\le X_N\), (8) separates
the Type II matrix into at most \(N+1\) rank-one matrices. Rectangles meeting
the hyperbola can be handled by the usual smooth subdivision; that does not
change the following sign issue.

Formula (8) is an identity, not an estimate. Applying the triangle
inequality term by term in \(j\) removes the relative signs of the
\(N+1\) components and returns to an absolute load. That route is discarded.

Cauchy--Schwarz in the *degree variable* is different: it produces finite
Laguerre coefficient norms, not immediately the pointwise absolute kernel.
Section 4 below gives their exact Hardy-space representation.  The
nonduplication audit 103_71 shows, however, that this representation is the
fixed-cutoff transform of Phase 102/233 and the classical Laguerre--Laplace
disk transform.  It is therefore a known coordinate, not a new input.

## 3. Phase geometry on multiplicative blocks

Let \(\Theta_N(u)\) denote the oscillatory Plancherel--Rotach phase of
\(L_N^{(1)}(u)\). The zero density recorded in `103_03` is

\[
 \rho_N(u)={1\over2\pi}\sqrt{{4N-u\over u}}.
\tag{9}
\]

Since consecutive zeros correspond to a phase increment \(\pi\), in every
closed central bulk range \(\delta N\le u\le(4-\delta)N\) one has, to
leading order uniformly there,

\[
 \Theta_N'(u)={1\over2}\sqrt{{4N-u\over u}}+o_\delta(1)
 =O_\delta(1).
\tag{10}
\]

If \(m\in[M,2M]\), then \(u=\log m\) varies by only \(\log2\). Hence

\[
 \sup_{M\le m_1,m_2\le2M}
 |\Theta_N(\log m_1)-\Theta_N(\log m_2)|
 =O_\delta(1).
\tag{11}
\]

There is no frequency parameter tending to infinity within a central
multiplicative block. The hard edge can have a larger phase derivative, but
the direct A1 obstruction contains the whole central bulk and soft edge, so
a hard-edge saving alone cannot close it.

For bilinear variables \(x=\log d\), \(y=\log r\), the phase is exactly

\[
 \phi_N(x,y)=\Theta_N(x+y).
\tag{12}
\]

Its Hessian is

\[
 \nabla^2\phi_N
 =\Theta_N''(x+y)
 \begin{pmatrix}1&1\\1&1\end{pmatrix},
 \qquad \det\nabla^2\phi_N=0.
\tag{13}
\]

More generally, after a \(k\)-fold Heath--Brown decomposition the phase is
\(\Theta_N(x_1+\cdots+x_k)\), whose Hessian is
\(\Theta_N''\mathbf1\mathbf1^T\): it has rank at most one and \(k-1\)
exactly flat directions. Adding convolution variables therefore does not
add oscillatory curvature.

## 4. The surviving degree--Hardy transform

For an arbitrary finitely supported arithmetic sequence \(a=(a_m)\), define

\[
 A_j(a)=\sum_m {a_m\over m}L_j(\log m).
\tag{14}
\]

The ordinary Laguerre generating function gives the exact identity

\[
 \boxed{\quad
 \sum_{j\ge0}A_j(a)z^j
 ={1\over1-z}\sum_m a_m\,m^{-1/(1-z)},
 \qquad |z|<1.
 \quad}
\tag{15}
\]

Indeed,

\[
 \sum_{j\ge0}L_j(\log m)z^j
 ={1\over1-z}
 \exp\!\left(-{\log m\,z\over1-z}\right),
\]

and multiplication by \(m^{-1}\) changes the exponent to
\(-\log m/(1-z)\).

For \(0<r<1\), Parseval on the circle gives

\[
 \boxed{\quad
 \sum_{j\ge0}|A_j(a)|^2r^{2j}
 ={1\over2\pi}\int_{-\pi}^{\pi}
 {1\over|1-re^{it}|^2}
 \left|\sum_m a_m m^{-s_r(t)}\right|^2dt,
 \quad
 s_r(t)={1\over1-re^{it}}.
 \quad}
\tag{16}
\]

The curve in (16) lies strictly in \(\Re s>1/2\). Moreover,

\[
 \sum_{j=0}^{N}|A_j(a)|^2
 \le r^{-2N}{1\over2\pi}\int_{-\pi}^{\pi}
 {1\over|1-re^{it}|^2}
 \left|\sum_m a_m m^{-s_r(t)}\right|^2dt.
\tag{17}
\]

Taking \(r=e^{-1/N}\) makes the prefactor \(r^{-2N}=e^2\).

Now restrict (6) to a rectangular block \(d\in D\), \(r\in R\) lying
inside \(dr\le X_N\), and put

\[
 a_d=\mu(d){\bf1}_D(d),\qquad c_r=b_V(r){\bf1}_R(r).
\]

Equations (7)--(8) give exactly

\[
 S_{II}(D,R)=\sum_{j=0}^{N}A_j(a)A_{N-j}(c),
\tag{18}
\]

and hence

\[
 \boxed{\quad
 |S_{II}(D,R)|
 \le
 \left(\sum_{j=0}^{N}|A_j(a)|^2\right)^{1/2}
 \left(\sum_{j=0}^{N}|A_j(c)|^2\right)^{1/2}.
 \quad}
\tag{19}
\]

This exposes a possible *new estimate*, but not a new transform:

> **Laguerre--Hardy Type II bound.** Prove estimates for the two integrals
> in (17), uniform in the multiplicative blocks and in \(N\), which remain
> summable across the hyperbolic partition and cost at most \(O(N\log N)\).

The statement is finite and lives in \(\Re s>1/2\); it does not insert a
zero location.  But 103_71 shows that separate Cauchy norms discard the
cross-cancellation between the Moebius and positive divisor factors.  On a
central sign-consistent Laguerre lobe the positive factor already has a
coherent exponentially large coefficient.  Thus a useful product bound
would require a compensating estimate for the Moebius norm far beyond what
generic Dirichlet-polynomial mean values provide.  A generic diagonal
mean-square estimate is not enough. The elementary bound
\(b_V(r)\le\sum_{e\mid r}\Lambda(e)=\log r\) makes the second norm too
large in the central range if used without its average divisor structure.
The next viability test is therefore the true mean square of \(b_V\) on
dyadic blocks, together with the curved-contour mean value in (17).

That contour already shows why the ordinary Montgomery--Vaughan mean-value
theorem is not a free input.  The image of \(|z|=r\) under
\(s=1/(1-z)\) is the circle

\[
 \left(\sigma-{1\over1-r^2}\right)^2+\tau^2
 ={r^2\over(1-r^2)^2}.
\tag{20}
\]

Its maximal height is \(r/(1-r^2)\).  More importantly, writing
\(c=(1-r^2)^{-1}\), equation (20) gives

\[
 \tau^2=c(2\sigma-1)-\sigma^2.
\tag{21}
\]

For \(r=e^{-1/N}\), one has \(c\asymp N\).  On the part of the contour
with \(1/2<\sigma\le1\), therefore,

\[
 |\tau|\le\sqrt{c-1}=O(\sqrt N).
\tag{22}
\]

The central A1 blocks, however, contain integers of size
\(\exp(\Theta(N))\).  Hence (17) asks for mean values of Dirichlet
polynomials of exponential length on a near-critical spectral window of
only polynomial height.  The standard diagonal mean-value regime would
require a window comparable with the polynomial length; it is exponentially
out of range here.  Any useful estimate must exploit the special
Möbius/divisor coefficients and their coupling across shells.

## 5. Consequence for A1

Standard Vaughan/Heath--Brown identities remain available as bookkeeping,
and classical estimates for their coefficients recover PNT-type information.
What they do not supply here is a phase-driven Type I/II saving in the
central bulk. On each dyadic block the Laguerre factor is a bounded-frequency
smooth weight, while the cancellation demanded by A1 is the orientation of
many such blocks across \(0<u<4N\).

Thus a successful bilinear continuation would need a theorem of the form

\[
 \sum_{\text{many shells }B}
 \sum_{dr\in B}\mu(d)b_V(r)W_N(dr)
 \le {3\over8}N\log N+O(N),
\tag{23}
\]

with signs retained across shells. Neither (3) nor generic Type I/II
absolute estimates imply (14). Proving (14) would be a new global arithmetic
correlation theorem and must be tested directly against the A1 off-line
falsifier.

## Status

```text
proved:
  exact Vaughan decomposition of the finite prime--Laguerre sum;
  exact Laguerre rank-(N+1) separation;
  rank-one logarithmic phase geometry;
  O(1) phase variation on central multiplicative dyadic blocks;

discarded:
  ordinary phase-driven Type I/II estimates as an automatic A1 closure;
  triangle use of the Laguerre addition formula;

discarded after the nonduplication and scale audit in 103_71:
  degree-variable Cauchy with separate Laguerre--Hardy norms as a closure
  mechanism;

known coordinate, not progress:
  the exact Laguerre--Hardy transform, already present in Phase 102/233 and
  classical Laguerre--Laplace theory;

discarded as an off-the-shelf closure:
  Montgomery--Vaughan diagonal mean values, since the polynomial length
  is exp(Theta(N)) while the near-critical contour height is O(sqrt(N));

still open only with genuinely new input:
  a coupled signed Moebius--divisor theorem which retains cancellation
  jointly across multiplicative shells; this is not supplied by Vaughan's
  identity or by separate Hardy norms.
```
