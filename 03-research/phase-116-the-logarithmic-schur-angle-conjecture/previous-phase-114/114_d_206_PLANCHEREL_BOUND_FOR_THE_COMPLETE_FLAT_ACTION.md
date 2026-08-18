# D.206 — Plancherel bound for the complete endpoint-flat action

## Verdict

The weighted derivative Gram in D.204--D.205 need not be assembled by
differentiating the cancellation-prone Hurwitz boundary formula.  The
completed row-D operator is the compression of one full-line Fourier
multiplier.  Therefore its local weighted derivative norm is bounded by a
single positive Plancherel integral containing the **complete** Gamma symbol
and every active prime power at once.

For the source-defined split at \(T=\tfrac12\log6\), use

\[
 S=\left\{(1-t^2/T^2)^{60}R(t):\deg R<80\right\}
 \cap\mathcal P_T.                                    \tag{0.1}
\]

It has dimension \(78\).  This avoids numerical singular-vector promotion.
The remaining obligation is a directed matrix enclosure of the integral
below and the corrected Schur complement; this note does not assert their
sign.

## 1. The complete multiplier

Let \(E_T\) be zero extension from \((-T,T)\), \(P_T\) restriction, and use
the Fourier convention

\[
 \widehat F(\tau)=\int_{\mathbb R}F(t)e^{-i\tau t}\,dt,
 \qquad
 \|F\|_2^2={1\over2\pi}\int_{\mathbb R}|\widehat F(\tau)|^2d\tau.
\]

The complete operator occurring in the row-D form is

\[
 A_T=P_TM_{W_T}E_T,                                   \tag{1.1}
\]

where

\[
 W_T(\tau)=
 \mathrm{Re}\,\psi\!\left({1\over4}+{i\tau\over2}\right)
 -\log\pi
 -2\sum_{p^k\le e^{2T}}{\log p\over p^{k/2}}
       \cos(k\tau\log p).                            \tag{1.2}
\]

At \(2T=\log6\), the finite sum consists exactly of
\(2,3,4,5\), with the coefficient of \(4\) equal to
\(\Lambda(4)/2=(\log2)/2\).  Formula (1.2) is the Fourier transform of the
complete oscillator expression of D.150: the Gamma sum is
\(\mathrm{Re}\,\psi(1/4+i\tau/2)-\psi(1/4)\), and subtraction of
\(m_0=\log\pi-\psi(1/4)\) leaves the first two terms of (1.2).

## 2. Weighted derivative domination

Let \(m=60\) and \(F\in S\).  Zero extension belongs to \(H^{60}(\mathbb
R)\), because the first fifty-nine endpoint jets vanish.  The logarithmic
growth of \(W_T\), together with one additional integration by parts in the
Fourier transform, implies

\[
 |\tau|^{60}W_T(\tau)\widehat F(\tau)\in L^2(\mathbb R).
\]

Consequently differentiation commutes with the full-line multiplier in the
weak sense and restriction gives

\[
\begin{aligned}
&\int_{-T}^{T}\left(1-{t^2\over T^2}\right)^{60}
 |(A_TF)^{(60)}(t)|^2dt\\
&\qquad\le \int_{\mathbb R}|D^{60}M_{W_T}E_TF|^2dt\\
&\qquad={1\over2\pi}\int_{\mathbb R}
 |\tau|^{120}|W_T(\tau)|^2|\widehat F(\tau)|^2d\tau.
                                                               \tag{2.1}
\end{aligned}
\]

The right side is positive and contains all cancellations inside the exact
scalar \(W_T\), rather than between enormous endpoint derivatives.

For a synthesis matrix \(S=(F_1,\ldots,F_s)\), define

\[
 \mathcal J_{ij}={1\over2\pi}\int_{\mathbb R}
 |\tau|^{120}|W_T(\tau)|^2
 \widehat F_i(\tau)\overline{\widehat F_j(\tau)}d\tau. \tag{2.2}
\]

Then the derivative Gram of D.204 obeys \(H_{60}\le\mathcal J\) in Loewner
order.  Therefore

\[
 \|R_NA_TSB^{-1/2}\|^2
 \le { (N-60)!T^{120}\over(N+60)!}
 \lambda_{\max}(B^{-1/2}\mathcal J B^{-1/2}).          \tag{2.3}
\]

## 3. Directed tail formula

For \(|\tau|>0\), integration by parts sixty-one times is exact:

\[
\begin{aligned}
 (i\tau)^{61}\widehat F(\tau)
 ={}&F^{(60)}(-T)e^{i\tau T}
    -F^{(60)}(T)e^{-i\tau T}\\
 &+\int_{-T}^{T}F^{(61)}(t)e^{-i\tau t}dt .            \tag{3.1}
\end{aligned}
\]

All earlier boundary terms vanish by (0.1).  Hence, for any coefficient
vector \(z\),

\[
 |\tau|^{60}|\widehat{Sz}(\tau)|
 \le {1\over|\tau|}
 \left(| (Sz)^{(60)}(-T)|+|(Sz)^{(60)}(T)|
 +\sqrt{2T}\,\|(Sz)^{(61)}\|_2\right).                \tag{3.2}
\]

The required multiplier bound is elementary.  Put \(a=1/4\) and
\(y=|\tau|/2\).  The digamma difference has the positive series

\[
 G(y)=\mathrm{Re}\,\psi(a+iy)-\psi(a)
 =\sum_{j\ge0}{y^2\over(j+a)((j+a)^2+y^2)}.           \tag{3.3}
\]

For \(0\le y\le1\), monotonicity and a first-term-plus-integral bound give
\(G(y)<4.6\).  For \(y\ge1\), split at \(J=\lfloor y\rfloor\): the lower
part is at most \(4+\log(4(y+1))\), and the upper part at most \(3/2\).
Thus

\[
 G(y)<7+\log(1+|\tau|).                               \tag{3.4}
\]

Using \(\psi(1/4)=-\gamma-\pi/2-3\log2\), elementary outward bounds give
\(|\psi(1/4)-\log\pi|<5.377\).  Twice the absolute sum of the four contact
coefficients in (1.2) is smaller than \(4.4\).  Consequently

\[
 \boxed{|W_T(\tau)|<17+\log(1+|\tau|).}               \tag{3.5}
\]

For \(R\ge1\), put \(A_R=17+R^{-1}\).  Since
\(\log(1+\tau)\le\log\tau+R^{-1}\) on \([R,\infty)\),

\[
 \int_R^\infty{(17+\log(1+\tau))^2\over\tau^2}d\tau
 \le{(A_R+\log R)^2+2(A_R+\log R)+2\over R}.         \tag{3.6}
\]

Equations (3.2), (3.5), and (3.6) give a closed analytic tail majorant.

The compact integral \([0,R]\) in (2.2) can be enclosed cellwise with Arb,
using the exact finite polynomial Fourier transforms.  Equations
(3.1)--(3.6) supply an analytic remainder, so a finite frequency mesh is not
being mistaken for the whole integral.

## 4. Numerical scale and remaining test

At \(N=600,m=60\), the sharp coefficient before physical scaling is

\[
 {540!\over660!}=4.6281536951\ldots\times10^{-334},    \tag{4.1}
\]

and after multiplication by \(T^{120}\) it is

\[
 8.6173413007\ldots\times10^{-340}.                   \tag{4.2}
\]

Thus even a large directed enclosure of \(\mathcal J\) may leave useful
capacity below the complement gap.  To close the endpoint one must still
combine:

1. the directed rows \(200{:}600\);
2. the analytic remainder from (2.3)--(3.6);
3. the primitive graph correction;
4. the corrected \(D\)-block cross term of D.200.

Only the joint interval inequalities \(\kappa<\delta\) and positive final
Schur complement constitute the endpoint proof.
