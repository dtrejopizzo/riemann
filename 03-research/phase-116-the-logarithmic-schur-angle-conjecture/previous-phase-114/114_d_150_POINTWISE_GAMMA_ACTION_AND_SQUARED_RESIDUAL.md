# D.150 — Pointwise Gamma action and the squared-multiplier residual

## Verdict

The remaining Feshbach matrix in D.149 involves \(A^2\), whereas D.147
computes only the linear compression of \(A\).  For every polynomial on a
bounded window, the action of the **complete** Gamma operator itself has an
exact finite formula: a polynomial interior term plus two Hurwitz--Lerch
boundary layers.  Consequently the squared-multiplier matrix is an ordinary
finite collection of one-dimensional integrals; no double oscillator sum
and no Gamma truncation are needed.

Let

\[
 b_j=2j+\frac12,qquad
 (G_\Gamma F)(t)=\sum_{j\ge0}left({2\over b_j}F(t)
 -\int_{-T}^T e^{-b_j|t-s|}F(s)\,ds\right).             \tag{0.1}
\]

For a polynomial \(F\) of degree \(d\), define

\[
 H_s(x)=\sum_{j\ge0}{e^{-b_jx}\over b_j^s}
 =2^{-s}e^{-x/2}\Phi(e^{-2x},s,1/4),qquad x>0.         \tag{0.2}
\]

Then, for \(-T<t<T\),

\[
\boxed{
\begin{aligned}
 G_\Gamma F(t)={}&-2\sum_{\substack{2\le r\le d\\r\ \mathrm{even}}}
 2^{-(r+1)}\zeta(r+1,1/4)F^{(r)}(t)\\
 &+\sum_{r=0}^d(-1)^rF^{(r)}(-T)H_{r+1}(t+T)\\
 &+\sum_{r=0}^dF^{(r)}(T)H_{r+1}(T-t).
\end{aligned}}                                         \tag{0.3}
\]

The only endpoint singularity is logarithmic, from \(H_1(x)\); hence
\(G_\Gamma F\in L^2(-T,T)\).  Adding the constant Gamma mass and the
finitely many active translated contacts gives the pointwise completed
operator \(A_TF\).  Thus

\[
 (S^*A_T^2S)_{mn}=\int_{-T}^T
 (A_TS e_m)(t)\overline{(A_TS e_n)(t)}\,dt              \tag{0.4}
\]

is a directed quadrature problem with explicit logarithmic endpoint
majorants.  Equations (0.3)--(0.4) are the missing analytic input for the
residual majorant in D.149.  They do not assert its final sign.  The paper
is not modified.

## 1. One oscillator

Put

\[
 K_bF(t)=\int_{-T}^Te^{-b|t-s|}F(s)\,ds=L_bF(t)+R_bF(t),             \tag{1.1}
\]

where the two terms integrate over \([-T,t]\) and \([t,T]\).  Set

\[
 Q_+(t)=\sum_{r=0}^d{(-1)^rF^{(r)}(t)\over b^{r+1}},qquad
 Q_-(t)=\sum_{r=0}^d{F^{(r)}(t)\over b^{r+1}}.          \tag{1.2}
\]

Direct differentiation gives

\[
 (\partial_t+b)Q_+=F,qquad(-\partial_t+b)Q_-=F.        \tag{1.3}
\]

Imposing the two endpoint conditions yields

\[
\begin{aligned}
 L_bF(t)&=Q_+(t)-e^{-b(t+T)}Q_+(-T),\\
 R_bF(t)&=Q_-(t)-e^{-b(T-t)}Q_-(T).                    \tag{1.4}
\end{aligned}
\]

Adding (1.4), the odd derivatives cancel and the zeroth derivative is
\(2F/b\).  Therefore

\[
\begin{aligned}
 {2F(t)\over b}-K_bF(t)
={}&-2\sum_{\substack{r\ge2\\r\ \mathrm{even}}}{F^{(r)}(t)\over b^{r+1}}\\
 &+e^{-b(t+T)}\sum_{r=0}^d{(-1)^rF^{(r)}(-T)\over b^{r+1}}\\
 &+e^{-b(T-t)}\sum_{r=0}^d{F^{(r)}(T)\over b^{r+1}}.  \tag{1.5}
\end{aligned}
\]

This identity is pointwise and contains no limiting operation.

## 2. Summing every quarter-shift oscillator

For \(s>1\),

\[
 \sum_{j\ge0}b_j^{-s}=2^{-s}\zeta(s,1/4).              \tag{2.1}
\]

For \(x>0\), absolute convergence gives (0.2), including \(s=1\).
Substitution of (2.1)--(0.2) into (1.5) proves (0.3).  The interchange is
finite in the derivative index.  On compact subsets of \((-T,T)\), every
boundary series converges normally.

As \(x\downarrow0\), comparison with
\(\sum_{j\ge0}e^{-2jx}/(2j+1/2)\) gives

\[
 H_1(x)=-\frac12\log x+O(1),                           \tag{2.2}
\]

while \(H_s(x)\to2^{-s}\zeta(s,1/4)\) for \(s>1\).
Hence (0.3) has at worst logarithmic singularities at the endpoints and is
square-integrable.

## 3. Completed operator and exact residual

At \(T=\frac12\log5\), put

\[
 m_0=\log\pi-\psi(1/4),qquad
 (C_aF)(t)=\widetilde F(t+a)+\widetilde F(t-a).         \tag{3.1}
\]

The complete row-D operator is

\[
 A_TF=G_\Gamma F-m_0F-
 \sum_{n\in\{2,3,4\}}{\Lambda(n)\over\sqrt n}
 C_{\log n}F.                                          \tag{3.2}
\]

For the projected finite synthesis \(S_N=P_T\Phi_N\), its columns are a
polynomial plus fixed multiples of \(e^{-t/2}\) and \(e^{t/2}\).  Formula
(0.3) applies directly to the polynomial part.  The exponential parts may
be obtained either by the same one-oscillator resolvent before summation or,
more efficiently, by their superfactorially convergent Legendre expansions.
The coefficients are the exact Tate--Bessel moments already used in D.148.

Once an outward-rounded enclosure \(C\ge S_N^*A_T^2S_N\) is available, the
safe residual matrix is

\[
 \widetilde R=C-BG_N^{-1}B,                             \tag{3.3}
\]

and the complete Feshbach test is

\[
 B-\delta^{-1}\widetilde R\ge0.                        \tag{3.4}
\]

All entries in (3.3) come from the same source-derived multiplier as
\(B_{\rm nuc}\); (3.3) introduces no spectral zero and no assumed sign.
