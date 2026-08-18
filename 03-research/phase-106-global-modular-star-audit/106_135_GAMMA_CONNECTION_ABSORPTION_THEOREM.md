# 106.135 — Gamma absorption of the physical Abel connection

## 1. Result

Let

\[
 h(x)=\cosh(x/2),\qquad c_K=\frac12,
 \qquad a(x)=\frac{K(x)}{h(x)},
\]

and let

\[
 \mathcal C=T_{K'+K/2}M_a
\]

be the physical Abel connection of 106.131 and 106.133.  Put

\[
 r_\Gamma(u)=\frac{e^{-5u/2}}{1-e^{-2u}},\qquad u>0.
\]

This note proves the part of the physical passivity estimate which couples
the completed Gamma remainder to the radical connection.  The result is
global: it does not require a frequency cutoff, a finite radical block, or
mean periodicity.

### Theorem 1 — Pointwise theta--Gamma margin

In the normalization \(\widehat K=\Xi\), one has

\[
 \boxed{
  2K(u)<\frac{1501}{2000}\,r_\Gamma(u)
  \qquad(u>0).}
 \tag{1}
\]

Consequently

\[
 w_\Gamma(u):=r_\Gamma(u)-2K(u)
 \ge \frac{499}{2000}r_\Gamma(u)>0.
 \tag{2}
\]

### Theorem 2 — Exact Gamma--connection factorization

For every complex multiplier \(q\) in the common form core, put \(F=hq\).
Then

\[
\boxed{
\begin{aligned}
 &\mathfrak b_{\Gamma,*}(q)
 +2\mathrm{Re}\,\langle F,\mathcal CF\rangle_{\omega_K}
 \\
 &\qquad=\mathfrak b_{w_\Gamma}(q)
 +2\int_{\mathbb R}(K*K)(x)K(x)|q(x)|^2\,dx.
\end{aligned}}
\tag{3}
\]

Both terms on the right are nonnegative.  More precisely,

\[
 \boxed{
 \mathfrak b_{\Gamma,*}(q)
 +2\mathrm{Re}\,\langle F,\mathcal CF\rangle_{\omega_K}
 \ge \frac{499}{2000}\mathfrak b_{\Gamma,*}(q).}
 \tag{4}
\]

For every \(0\le\eta\le1\), therefore,

\[
\boxed{
 \mathfrak b_{\Gamma,*}(q)
 +2\eta\mathrm{Re}\,\langle F,\mathcal CF\rangle_{\omega_K}
 \ge
 \left(1-\frac{1501}{2000}\eta\right)
 \mathfrak b_{\Gamma,*}(q)\ge0.}
\tag{5}
\]

Thus the real connection kernel isolated in 106.133 is completely
absorbed by the positive completed Gamma remainder, with a fixed explicit
margin.  This proves the Gamma--connection part of the heat/hybrid
passivity problem.  It does not assign a sign to the remaining common
outgoing/incoming PNT power.

## 2. Exact normalization of the theta kernel

For \(u\ge0\), the full-line Fourier normalization
\(\widehat K=\Xi\) gives

\[
 K(u)=2\pi e^{5u/2}
 \sum_{m\ge1}m^2\bigl(2\pi m^2e^{2u}-3\bigr)
 e^{-\pi m^2e^{2u}}.
 \tag{6}
\]

The factor \(2\) in (6) is forced by

\[
 \int_{\mathbb R}\cosh(x/2)K(x)\,dx
 =\widehat K(i/2)=\Xi(i/2)=\xi(0)=\frac12.
 \tag{7}
\]

For a direct check, let \(K_0\) denote the right-hand side of (6) with
the initial factor \(2\) removed and set \(a_m=\pi m^2\).  Termwise
integration, with \(y=e^u\), gives

\[
\begin{aligned}
 \int_{\mathbb R}\cosh(u/2)K_0(u)\,du
 &=\pi\sum_{m\ge1}m^2
 \int_1^\infty (y^2+y)(2a_my^2-3)e^{-a_my^2}\,dy\\
 &=\sum_{m\ge1}\left(2\pi m^2-\frac12\right)e^{-\pi m^2}.
\end{aligned}
\]

If \(\vartheta(t)=\sum_{m\in\mathbb Z}e^{-\pi m^2t}\), differentiating
\(\vartheta(t)=t^{-1/2}\vartheta(1/t)\) at \(t=1\) yields
\(\pi\sum_{m\in\mathbb Z}m^2e^{-\pi m^2}=\vartheta(1)/4\).
The last displayed sum is therefore \(1/4\), so (7) multiplies \(K_0\)
by exactly \(2\), as asserted.

In particular every summand in (6) is positive.

Set

\[
 t=e^{2u}\ge1.
\]

Multiplying (6) by \(2/r_\Gamma(u)\) gives the exact scalar series

\[
 \frac{2K(u)}{r_\Gamma(u)}
 =4\pi t^{3/2}(t-1)
 \sum_{m\ge1}m^2(2\pi m^2t-3)e^{-\pi m^2t}.
 \tag{8}
\]

We now bound (8) without floating-point input.

## 3. The first theta atom

Write the \(m=1\) part of (8) as

\[
 R_1(t)=4\pi t^{3/2}(t-1)(2\pi t-3)e^{-\pi t}.
 \tag{9}
\]

Its logarithmic derivative is

\[
 d(t)=\frac{3}{2t}+\frac1{t-1}
 +\frac{2\pi}{2\pi t-3}-\pi.
 \tag{10}
\]

Moreover

\[
 d'(t)=-\frac{3}{2t^2}-\frac1{(t-1)^2}
 -\frac{(2\pi)^2}{(2\pi t-3)^2}<0.
 \tag{11}
\]

Hence \(R_1\) has one global maximum.  Using

\[
 \frac{333}{106}<\pi<\frac{355}{113}
\]

and observing that the expression in (10) is decreasing in \(\pi\),
direct rational arithmetic gives

\[
 d(169/100)>
 \frac{226593655}{11344019037}>0,
\]

and

\[
 d(17/10)<-\frac{215749}{17117198}<0.
\]

The maximizer therefore lies in \((169/100,17/10)\).  On that interval,

\[
 t^{3/2}<\frac{17}{10}\frac{163}{125},
 \qquad t-1<\frac7{10},
\]

because \((163/125)^2>17/10\).  Also

\[
 e^{-\pi t}
 <e^{-56277/10600}<\frac1{200}.
\]

The last inequality has comfortable rational slack: retaining the terms
through degree (11) in the positive Taylor series for
\(e^{56277/10600}\) already gives a rational sum exceeding \(200\).
Therefore

\[
\begin{aligned}
 R_1(t)
 &<4\frac{355}{113}\frac{17}{10}\frac{163}{125}
      \frac7{10}
 \left(2\frac{355}{113}\frac{17}{10}-3\right)\frac1{200}
 \\
 &=\frac{298849579}{399031250}<\frac34.
\end{aligned}
 \tag{12}
\]

## 4. All remaining theta atoms

For \(m\ge2\), discard the negative term \(-3\) in (8).  Then

\[
 R_{\ge2}(t)
 \le8\pi^2t^{5/2}(t-1)
 \sum_{m\ge2}m^4e^{-\pi m^2t}.
 \tag{13}
\]

The ratio of consecutive summands satisfies

\[
 \frac{(m+1)^4e^{-\pi(m+1)^2t}}
      {m^4e^{-\pi m^2t}}
 \le\left(\frac32\right)^4e^{-5\pi}<10^{-5}.
\]

Thus

\[
 \sum_{m\ge2}m^4e^{-\pi m^2t}<17e^{-4\pi t}.
 \tag{14}
\]

Writing \(s=t-1\), the elementary bound
\((1+s)^{5/2}\le e^{5s/2}\) yields

\[
 t^{5/2}(t-1)e^{-4\pi t}
 \le e^{-4\pi}s e^{-(4\pi-5/2)s}
 \le\frac{e^{-4\pi}}{e(4\pi-5/2)}.
 \tag{15}
\]

Using only \(\pi^2<10\), \(\pi>3\), \(e>2\), and
\(e^{4\pi}>e^{12}>160000\), equations (13)--(15) give

\[
 R_{\ge2}(t)
 <\frac{1360}{19\cdot160000}<\frac1{2000}.
 \tag{16}
\]

Equations (12) and (16) imply

\[
 \frac{2K(u)}{r_\Gamma(u)}
 <\frac34+\frac1{2000}=\frac{1501}{2000},
\]

which proves Theorem 1.

## 5. Form-level factorization

Extend \(r_\Gamma\), \(w_\Gamma\), and \(K\) evenly in the displacement
variable.  For any nonnegative even displacement density \(v\), write

\[
 \mathfrak b_v(q)
 =\frac12\iint_{\mathbb R^2}
 v(x-y)K(x)K(y)|q(x)-q(y)|^2\,dx\,dy.
 \tag{17}
\]

This convention agrees with the one-sided displacement form.  Since
\(r_\Gamma=w_\Gamma+2K\),

\[
 \mathfrak b_{\Gamma,*}(q)
 =\mathfrak b_{w_\Gamma}(q)+2\mathfrak b_K(q).
 \tag{18}
\]

Put \(f=Kq=aF\).  The adjoint calculation of 106.133 and \(c_K=1/2\)
give

\[
 \mathrm{Re}\,\langle F,\mathcal CF\rangle_{\omega_K}
 =\langle f,T_Kf\rangle_2
 =\iint K(x-y)K(x)K(y)
       \mathrm{Re}\,\{\overline{q(x)}q(y)\}\,dx\,dy.
 \tag{19}
\]

Expanding the difference square in \(\mathfrak b_K\) gives the exact
identity

\[
 \mathfrak b_K(q)+\langle f,T_Kf\rangle_2
 =\int_{\mathbb R}(K*K)(x)K(x)|q(x)|^2\,dx.
 \tag{20}
\]

Combining (18)--(20) proves (3).  Equations (2), (17), and (3) give (4).
Finally,

\[
 \mathfrak b_{\Gamma,*}+2\eta\mathrm{Re}\,\langle F,\mathcal CF\rangle
 =(1-\eta)\mathfrak b_{\Gamma,*}
 +\eta\bigl(\mathfrak b_{\Gamma,*}
 +2\mathrm{Re}\,\langle F,\mathcal CF\rangle\bigr),
\]

which proves (5).

The argument is performed entirely at the difference-form level.  It does
not split the singular Gamma kernel into separately divergent diagonal and
convolution operators.

## 6. Consequence for the physical-surplus program

There are two different connection statements in this part of the ledger,
and they must not be conflated.  Equation (4) absorbs the **linear
Hermitian power**

\[
 2\mathrm{Re}\,\langle F,\mathcal CF\rangle_{\omega_K}
\]

inside the connection-corrected KYP supply.  By contrast, the Douglas
gate of 106.136 asks for the **quadratic relative amplitude**

\[
 \mathcal C^\sharp\mathcal C\preceq\widetilde A.
\]

The second statement controls a Schur cost and is not a consequence of
the first.  Conversely, it is a sufficient gate for a particular
factorized realization; it is not an exact rewriting of the original
physical form.

With that distinction fixed, the linear connection sign identified in
106.131 and 106.133 is no longer open.  On every heat row, every hybrid
row, and indeed every common-core row, the completed Gamma remainder
absorbs its full Hermitian power with the fixed margin (4).  The \(K'\)
part was already exactly skew-adjoint.

For the original physical theorem, the unresolved sign is therefore the
joint form \(\mathfrak P_{\rm PNT}+\mathfrak b_{\Gamma,*}\).  In the
augmented KYP coordinate, the remaining contribution is the common
ordinary-prime power: the outgoing PNT quadrature and its incoming Abel
realization must still be kept together.  The next estimate may spend the
explicit Gamma margin in (4), but it cannot estimate the PNT discrepancy
by total variation.
