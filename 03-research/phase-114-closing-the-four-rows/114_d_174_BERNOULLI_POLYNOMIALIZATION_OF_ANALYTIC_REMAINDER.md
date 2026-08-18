# D.174 — Bernoulli polynomialization of the analytic remainder

## Verdict

The analytic remainder left by the exact endpoint-log extraction can be
enclosed without numerical quadrature.  Its only nonpolynomial kernel is

\[
 q(x):=xK(x)=\frac{x e^{3x/2}}{e^{2x}-1}.             \tag{0.1}
\]

The Taylor radius of (q) at zero is (pi), while the largest argument at
the endpoint under consideration is (L=2T=\log5<\pi).  A finite Bernoulli
expansion therefore turns every contracted Gamma column into an explicit
piecewise polynomial plus the single already-extracted logarithm, with a
uniform geometric remainder.  The total five-by-five Gram can consequently
be enclosed using only polynomial arithmetic and the beta moments of D.171.

## 1. One common Taylor series

The Bernoulli generating function gives

\[
 q(x)=\frac12
 \left(\sum_{n\ge0}B_n\frac{(2x)^n}{n!}\right)
 \left(\sum_{k\ge0}\frac{(3x/2)^k}{k!}\right).       \tag{1.1}
\]

Write (q(x)=\tfrac12+\sum_{n\ge1}c_nx^n).  Since

\[
 H_1'(x)=-K(x)=-\frac{q(x)}x,
\]

the analytic endpoint remainder
(r_1(x)=H_1(x)+\tfrac12\log x) satisfies

\[
 r_1(0)=\log2+\frac\pi4,
 \qquad
 r_1(x)=r_1(0)-\sum_{n\ge1}\frac{c_n}{n}x^n.         \tag{1.2}
\]

Thus the diagonal kernel and the endpoint correction are controlled by the
same coefficient list.

## 2. Polynomial formula for the contracted integral

For a polynomial (F), expand around (t):

\[
\begin{aligned}
 F(t)-F(t-x)&=\sum_{r\ge1}\frac{(-1)^{r+1}}{r!}
 F^{(r)}(t)x^r,\\
 F(t)-F(t+x)&=-\sum_{r\ge1}\frac1{r!}F^{(r)}(t)x^r.
\end{aligned}                                        \tag{2.1}
\]

Put

\[
 Q_m(a)=\int_0^a x^mq(x)\,dx
 =\sum_{n\ge0}\frac{c_n}{n+m+1}a^{n+m+1},           \tag{2.2}
\]

where (c_0=1/2).  The nonsingular integral in D.156 is exactly

\[
 I_F(t)=\sum_{r=1}^{\deg F}\frac{F^{(r)}(t)}{r!}
 \left((-1)^{r+1}Q_{r-1}(t+T)-Q_{r-1}(T-t)\right).   \tag{2.3}
\]

If (1.1) is truncated by total degree, (1.2)--(2.3) are polynomials.
Together with the piecewise-polynomial contacts, they give

\[
 A_TF(t)=-\frac12F(t)\log(T^2-t^2)+P_{F,M}(t)
          +\mathcal E_{F,M}(t),                      \tag{2.4}
\]

where (P_{F,M}) is explicit on every contact cell.

## 3. Explicit uniform Bernoulli tail

Let (M\ge4), (r=L/\pi<1), (u=3L/2), and
(J=\lceil M/2\rceil\ge2).  From

\[
 \frac{|B_{2m}|}{(2m)!}
 =\frac{2\zeta(2m)}{(2\pi)^{2m}}
\]

one obtains

\[
 A_{\rm tot}:=
 1+L+2\zeta(2)\frac{r^2}{1-r^2}                     \tag{3.1}
\]

as an upper bound for the absolute Bernoulli factor in (1.1) on
(|x|\le L), and

\[
 A_{\rm tail}(J)le
 2\zeta(2)\frac{r^{2\lceil J/2\rceil}}{1-r^2}.       \tag{3.2}
\]

For (J+1>u), the exponential tail satisfies

\[
 E_{\rm tail}(J)le
 \frac{u^J}{J!}\left(1-\frac{u}{J+1}\right)^{-1}.   \tag{3.3}
\]

Every product term of total degree at least (M) has either Bernoulli
degree at least (J) or exponential degree at least (J).  Hence

\[
 \boxed{
 \sup_{0\le x\le L}|q(x)-q_{<M}(x)|
 \le\frac12\left(e^uA_{\rm tail}(J)
                 +A_{\rm tot}E_{\rm tail}(J)\right)
 =:\varepsilon_M.}                                  \tag{3.4}
\]

The corresponding error in (1.2) is at most
(\(\varepsilon_M/M\)).  In (2.2), using that the tail starts at degree \(M\),

\[
 |Q_m(a)-Q_{m,<M}(a)|
 \le \varepsilon_M\frac{a^{m+M+1}}
 {L^M(m+M+1)},\qquad0\le a\le L.                   \tag{3.5}
\]

Substitution in the finite derivative sum (2.3) gives a directed uniform
bound for \(\mathcal E_{F,M}\).  No derivative of an unknown remainder and
no quadrature error occur.

For implementation, a sharper bound avoids the absolute condition number of
the derivative sum.  In the divided-difference form of D.156,

\[
 \left|\frac{F(t)-F(s)}{t-s}\right|
 \le\|F'\|_{L^\infty[-T,T]}.
\]

Since the coefficient tail starts at degree \(M\), it also satisfies

\[
 |q(x)-q_{<M}(x)|\le\varepsilon_M(x/L)^M.
\]

The two triangular integrals and the two endpoint remainders therefore obey

\[
 \boxed{
 \|\mathcal E_{F,M}\|_\infty
 \le2\varepsilon_M\left(
 \frac{L\|F'\|_\infty}{M+1}
 +\frac{\|F\|_\infty}{M}
 \right).}                                           \tag{3.6}
\]

Both suprema in (3.6) have elementary directed Legendre bounds.  This estimate
retains the cancellation of the polynomial divided difference and is the one
used in the final enclosure.

## 4. Gram enclosure

The Gram of the polynomial-log part of (2.4) is a finite combination of
the exact moments in D.171.  If

\[
 \|\mathcal E_{F_a,M}\|_\infty\le\eta_a,
 \qquad \|P^{\log}_{F_a,M}\|_2\le R_a,
\]

then the missing Gram entry is bounded by

\[
 |\Delta H_{ab}|
 \le\sqrt{2T}\left(\eta_aR_b+\eta_bR_a\right)
     +2T\eta_a\eta_b.                               \tag{4.1}
\]

Because (L/\pi\simeq0.512), (3.4) decreases geometrically.  Equations
(1.1)--(4.1) reduce the endpoint proof to finite Arb polynomial arithmetic
followed by the directed congruence

\[
 K_{\rm final}-0.218^{-1}H>0.
\]
