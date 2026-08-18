# D.152 — Directed absorption of the rank-two Tate defect

## Verdict

At \(T=\frac12\log5\) and \(N=170\), the two primitive directions missed
by the graph-eliminated Legendre block are rigorously absorbed into the
Legendre-complement gap.  More precisely, if

\[
 y\in\mathcal P_T\cap V_{170}^{\perp},
\]

then

\[
 \boxed{\langle A_Ty,y\rangle>0.218\,\|y\|^2.}         \tag{0.1}
\]

This strengthens D.151 by supplying the missing operator bound on the
truncated Tate plane.  Therefore the rank-two defect is closed.  The full
endpoint still requires the Feshbach cross residual between
\(V_{170}\) and its now-positive complement.

All constants are evaluated by Arb intervals in
`114_d_152_tate_absorption_arb.py`.  No sign of the finite block or RH is
used.  The paper is not modified.

## 1. A uniform bound on the truncated Tate plane

Let

\[
 u_\pm=P_{L_N}e^{\pm t/2}
 =\sum_{n=0}^{N-1}g_n^\pm\phi_n(t).                    \tag{1.1}
\]

By reflection, \(|g_n^+|=|g_n^-|=g_n\), with \(g_n\) as in D.151.
For every \(r<N\), the endpoint derivative formula and the maximum
principle for derivatives of Legendre polynomials give

\[
 \sup_{|t|\le T}|u_\pm^{(r)}(t)|
 \le D_r:=\sum_{n=r}^{N-1}g_n
 \sqrt{{2n+1\over2T}}T^{-r}
 {(n+r)!\over2^r r!(n-r)!}.                            \tag{1.2}
\]

We use the positive upper bound (3.1) of D.151 for every \(g_n\); no
floating Bessel evaluation is needed.

For \(s>1\), the boundary layer of D.150 satisfies

\[
 0<H_s(x)\le H_s(0)=2^{-s}\zeta(s,1/4).                \tag{1.3}
\]

For \(s=1\), separate the \(j=0\) term and compare the rest with the
logarithmic series:

\[
\begin{aligned}
 H_1(x)
 &\le2+\sum_{j\ge1}{e^{-2jx}\over2j}\\
 &=2-\frac12\log(1-e^{-2x})\\
 &\le2+2T-\frac12\log(2x),\qquad0<x\le2T.             \tag{1.4}
\end{aligned}
\]

The last step uses \(1-e^{-2x}\ge2xe^{-2x}\) and \(x\le2T\).  If
\(L=2T\) and \(c=2+2T-\frac12\log2\), then the squared \(L^2(0,L)\)
norm of the last majorant is exactly

\[
 L\left[c^2-c(\log L-1)
 +\frac14\bigl((\log L)^2-2\log L+2\bigr)\right].      \tag{1.5}
\]

Applying the triangle inequality to the pointwise formula D.150 gives

\[
\begin{aligned}
 \|G_\Gamma u_\pm\|_2
 \le{}&2D_0\|2+2T-\tfrac12\log(2x)\|_{L^2(0,2T)}\\
 &+2\sqrt{2T}\sum_{r=1}^{N-1}D_rH_{r+1}(0)\\
 &+2\sqrt{2T}\sum_{\substack{2\le r<N\\r\ \mathrm{even}}}
 D_rH_{r+1}(0).                                       \tag{1.6}
\end{aligned}
\]

The last line is the interior derivative term and the second line contains
the two boundary layers.  For the completed operator

\[
 A_T=G_\Gamma-m_0I-
 \sum_{n=2,3,4}{\Lambda(n)\over\sqrt n}C_{\log n},     \tag{1.7}
\]

we use \(\|C_a\|\le2\) and
\(\|u_\pm\|\le\|e^{\pm t/2}\|=\sqrt{2\sinh T}\).
The resulting directed bound is

\[
 \|A_Tu_\pm\|<10^4.                                   \tag{1.8}
\]

## 2. Normalizing arbitrary vectors in the Tate plane

The Gram matrix of \(u_-,u_+\) is \(J_NJ_N^*\).  D.151 proves

\[
 \lambda_{\min}(J_NJ_N^*)
 \ge2(\sinh T-T)-2a_N>0.179.                           \tag{2.1}
\]

If \(u=c_-u_-+c_+u_+\), then

\[
 |c_-|+|c_+|
 \le{\sqrt2\over\sqrt{0.179}}\|u\|.                 \tag{2.2}
\]

Combining (1.8)--(2.2) gives the deliberately coarse but directed estimate

\[
 \boxed{\|A_Tu\|\le C_{170}\|u\|,qquad C_{170}<10^5.}               \tag{2.3}
\]

## 3. Absorption in the complement

Write \(y=u+q\) as in D.151.  The directed estimates are

\[
 \|u\|\le10^{-424}\|q\|,qquad
 \langle A_Tq,q\rangle>0.219\|q\|^2,qquad
 A_T\ge-8.315I.                                        \tag{3.1}
\]

Using (2.3),

\[
\begin{aligned}
 \langle A_Ty,y\rangle
 &\ge\left(0.219-2\cdot10^5\,10^{-424}
             -8.315\,10^{-848}\right)\|q\|^2\\
 &>0.218\,(1+10^{-848})\|q\|^2\\
 &\ge0.218\|y\|^2.                                    \tag{3.2}
\end{aligned}
\]

This proves (0.1).  Thus the complement used in the Feshbach criterion may
be taken to be the full primitive complement of \(V_{170}\), with the
explicit gap \(\delta=0.218\).

