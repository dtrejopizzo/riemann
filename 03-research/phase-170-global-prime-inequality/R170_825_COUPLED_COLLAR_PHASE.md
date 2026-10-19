# R170_825 — Phase of the coupled averaged collar

Continuation of R170_823. This note analyzes the block that
was left open there,

\[
 C_{a,w}:=\int_{\rho _0}^1w(\rho)\tau_{a/\rho}U_\rho\,d\rho,
 \qquad U_\rho=D_\rho^*\mathscr F D_\rho,
 \qquad a>0.                                                   \tag{1}
\]

The result is that, for each fixed arithmetic shift, coupling with the
local transform does not destroy the gain of the average: (1) gains at
least one derivative, and its compression to a finite window is
Hilbert--Schmidt. The possible stationary phase is confined to a finite
frequency band. The constants are not uniform as the shift ranges over an
infinite tail. No sign is obtained.

## 1. Exact multiplier--reflection

We use exactly the conventions of Paper 47:

\[
 (\tau_bf)(t)=f(t+b),\qquad
 \widehat{\tau_bf}(\xi)=e^{-ib\xi}\widehat f(\xi),\qquad
 \mathscr F=u_\infty(D)J,
\]

\[
 u_\infty(\xi)=e^{i\theta(\xi)},\qquad \theta'(\xi)=m(\xi),
 \qquad \widehat{Jf}(\xi)=\widehat f(-\xi).                     \tag{2}
\]

Conjugation by the dilation of R170_820 gives

\[
 U_\rho=u_\infty(D/\rho)J,
\]

and hence

\[
 \boxed{\
 \widehat{\tau_{a/\rho}U_\rho f}(\xi)
 =e^{-ia\xi/\rho}u_\infty(\xi/\rho)\widehat f(-\xi).\ }        \tag{3}
\]

Setting \(s=1/\rho\), \(S=\rho _0^{-1}\) and

\[
 \eta(s)=w(1/s)s^{-2}\in C_c^k((1,S)),                          \tag{4}
\]

we obtain

\[
 C_{a,w}=q_{a,w}(D)J,
 \qquad
 q_{a,w}(\xi)=\int_1^S\eta(s)e^{i\phi_{a,\xi}(s)}\,ds,          \tag{5}
\]

\[
 \phi_{a,\xi}(s)=\theta(s\xi)-as\xi,
 \qquad
 \partial_s\phi_{a,\xi}(s)=\xi\,[m(s\xi)-a].                 \tag{6}
\]

This sign matters: for the real collar \(\tau_{+a/\rho}U_\rho\) the
stationary equation is \(m=a\), not \(m=-a\).

## 2. Exact localization of the stationary region

Paper 47 proves, via the series

\[
 m(x)=m(0)+\sum_{n\ge0}
 \frac{x^2}{a_n(4a_n^2+x^2)},\qquad a_n=n+\tfrac14,             \tag{7}
\]

that \(m\) is even and strictly increasing on \([0,\infty)\): the
derivative of each summand of (7) is strictly positive for \(x>0\).
Moreover \(m(0)=-5.3721834\ldots\) and \(m(x)\to\infty\). For every
\(a>0\) there is, then, a unique

\[
 r_a=m^{-1}(a)>0.                                                \tag{8}
\]

From (6), a stationary point in \(s\in[1,S]\) exists exactly when

\[
 \boxed{\ \rho _0r_a\le |\xi|\le r_a.\ }                       \tag{9}
\]

Thus, for fixed \(a\), the stationary region is compact. There is no need
to invoke stationary phase to control the tail \(|\xi|\to\infty\).

Also recording the other orientation: a phase
\(\theta(s\xi)+as\xi\) would have derivative
\(\xi[m(s\xi)+a]\). This can vanish if and only if

\[
 0<a\le -m(0),                                                   \tag{10}
\]

with a unique positive root when the inequality is strict. Hence it is
not correct to claim in general that \(a+m\) never vanishes. For
\(a=\log k\), the possibility exists precisely while
\(\log k\le -m(0)\) (over the integers, \(2\le k\le215\)); it disappears
for \(k\ge216\). This observation concerns the plus-sign orientation, not
(1).

It is also worth not confusing that coupled orientation with the other PC
collar. Indeed,

\[
 \widehat{J\tau_{a/\rho}f}(\xi)
 =e^{+ia\xi/\rho}\widehat f(-\xi),                              \tag{10a}
\]

so that the block \(JH_\rho\) does not contain \(u_\infty\) and its phase
in \(s\) has constant derivative \(a\xi\). The phase
\(\theta(s\xi)+as\xi\), whose derivative contains \(m+a\), corresponds
instead to the collar coupled with the opposite translation
\(\tau_{-a/\rho}U_\rho\). If \(0<a<-m(0)\) and
\(r_a^-=m^{-1}(-a)\), its stationary points also lie in the compact band
\(\rho _0r_a^-\le|\xi|\le r_a^-\). Hence neither of the two coupled
orientations has stationary points in the frequency tail for fixed
\(a\).

## 3. Explicit non-stationary bound and one derivative of gain

Define

\[
 B_a:=2\pi e^{a+2},\qquad
 C_m:=\sup_{x\in\mathbb R}|xm'(x)|<\infty.                       \tag{11}
\]

The explicit lower bound of Paper 47 proves, for \(x\ge B_a\),

\[
 m(x)\ge \log\frac{x}{2\pi}-\frac1x-\frac1{2x^2}>a+1.          \tag{12}
\]

Consequently, if \(|\xi|\ge B_a\), then
\(|m(s\xi)-a|\ge1\) for all \(s\in[1,S]\). Integrating (5) once by
parts, with no boundary terms because \(\eta\) has compact support in the
open interval, gives

\[
 |q_{a,w}(\xi)|\le\frac{A_w}{|\xi|},\qquad |\xi|\ge B_a,         \tag{13}
\]

where the explicit constant

\[
 A_w:=\|\eta'\|_1+C_m\|\eta/s\|_1                              \tag{14}
\]

may be taken. Over the whole axis we also have
\(|q_{a,w}|\le\|\eta\|_1=\|w\|_1\).
Hence

\[
 \|q_{a,w}\|_2^2
 \le 2B_a\|w\|_1^2+\frac{2A_w^2}{B_a},                         \tag{15}
\]

and

\[
 \sup_\xi(1+\xi^2)^{1/2}|q_{a,w}(\xi)|
 \le\max\{(1+B_a^2)^{1/2}\|w\|_1,\sqrt2A_w\}.                \tag{16}
\]

Thus

\[
 \boxed{\ C_{a,w}:L^2(\mathbb R)\longrightarrow H^1(\mathbb R)
 \quad\hbox{is bounded}.\ }                                    \tag{17}
\]

The necessary conclusion here is the explicit gain of one derivative. A
higher-order iteration would require recording additional bounds for the
derivatives of the polygamma function; this is neither used nor claimed
in this note.

Band (9) explains why a global application of stationary phase would be
misleading. Near a nondegenerate stationary point, van der Corput yields,
uniformly over a family, only half a derivative. If a stationary band
persisted up to arbitrarily large frequencies, decay
\(|q(\xi)|\asymp|\xi|^{-1/2}\) would be the non-integrable borderline case
in dimension one: \(|q|^2\asymp|\xi|^{-1}\), which would not suffice for
local Hilbert--Schmidt. Here there is no such obstruction for fixed
\(a\), because every stationary point lies inside the finite interval
(9), while the tail satisfies (13).

## 4. Hilbert--Schmidt compression

Let \(P_T\) be multiplication by the indicator of \((-T,T)\). The
operator \(q(D)J\) has a kernel of the form \(\kappa(t+s)\), where
\(\widehat\kappa=q\).
With the Fourier normalization of Paper 47,

\[
 \|\kappa\|_2^2=\frac1{2\pi}\|q\|_2^2.
\]

Hence

\[
\begin{aligned}
 \|P_TC_{a,w}P_T\|_{\rm HS}^2
 &=\int_{-T}^T\int_{-T}^T|\kappa(t+s)|^2\,dt\,ds\\
 &\le2T\|\kappa\|_2^2\\
 &\le\frac{T}{\pi}
 \left(2B_a\|w\|_1^2+\frac{2A_w^2}{B_a}\right).
                                                                    \tag{18}
\end{aligned}
\]

This resolves the question left open in (18) of R170_823: the compression
of the averaged coupled collar is indeed Hilbert--Schmidt for each
nontrivial atom.

## 5. The arithmetic sum remains finite

For the exact tail of R170_820,

\[
 H_\rho U_\rho
 =\sum_{N<k\le MN}\frac{h_{M,N}(k)}{\sqrt k}
       \tau_{(\log k)/\rho}U_\rho,                               \tag{19}
\]

the sum is neither modified nor extended. Integrating and using (18),

\[
\boxed{
 \left\|P_T\!\int w(\rho)H_\rho U_\rho\,d\rho\,P_T\right\|_{\rm HS}
 \le\sum_{N<k\le MN}\frac{h_{M,N}(k)}{\sqrt k}\,
 \mathcal C_T(\log k,w),}                                       \tag{20}
\]

where

\[
 \mathcal C_T(a,w):=\left[\frac{T}{\pi}
 \left(2B_a\|w\|_1^2+\frac{2A_w^2}{B_a}\right)\right]^{1/2}.
                                                                    \tag{21}
\]

The triangle inequality loses possible cancellations between values of
\(k\), but proves compactness without altering the coefficients
\(h_{M,N}(k)\). Since \(B_{\log k}=2\pi e^2k\), this crude bound grows
like \(k^{1/2}\); combined with \(k^{-1/2}\) it is not uniform over an
infinite tail. This does not affect (19), which is a finite sum for each
\(M,N\), but it prevents extracting from (20) a statement uniform in the
cutoffs without additional work.

## 6. Scope of the piece

The coupled average that actually appears in PC has
multiplier--reflection (5), gains regularity, and is locally
Hilbert--Schmidt. The possible stationary point does not constitute an
obstruction because it is enclosed in (9). The half-derivative obstruction
would reappear only when requiring simultaneous uniformity over an
unbounded family of \(a\), where the stationary band moves toward
infinity.

This piece corrects the caution of R170_823 regarding
\(\langle H_\rho U_\rho\rangle_w\): its compressed compactness is indeed
proved. It does not give a sign to its quadratic form, does not by itself
control the other lines of interface (24) of R170_823, and does not prove
D nor RH.
