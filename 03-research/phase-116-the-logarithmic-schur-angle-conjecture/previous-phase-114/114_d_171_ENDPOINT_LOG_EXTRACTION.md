# D.171 — Exact endpoint-log extraction for the contracted spatial Gram

## Purpose and scope

The remaining endpoint calculation needs the fifteen entries of

\[
 H_X=(\langle A X_a,A X_b\rangle)_{1\leq a,b\leq5}
\]

for the five post-Schur graph columns of D.166.  This note removes the only
non-analytic endpoint terms from the pointwise Gamma formula.  It is an exact
identity, not yet the directed numerical enclosure of (H_X).

## The elementary (H_1) identity

Put (b_j=2j+\tfrac12) and

\[
 H_s(x)=\sum_{j\geq0}{e^{-b_jx}\over b_j^s},\qquad x>0.
\]

Writing (y=e^{-x/2}), one obtains

\[
 H_1(x)=2\sum_{j\geq0}{y^{4j+1}\over4j+1}
       =\operatorname {arctanh}y+\arctan y.             \tag{1}
\]

Consequently

\[
 H_1(x)=-\frac12\log x+R_1(x),                         \tag{2}
\]

where (R_1) is real analytic at (x=0).  Indeed,

\[
 \operatorname {arctanh}(e^{-x/2})+\frac12\log x
 =\frac12\log\!\left(
 {x(1+e^{-x/2})\over1-e^{-x/2}}
 \right),                                             \tag{3}
\]

and the argument of the logarithm is analytic and nonzero at zero.

## All higher endpoint singularities

Termwise differentiation gives (H_s'=-H_{s-1}).  Induction from (2)
therefore yields

\[
 H_{r+1}(x)=
 {(-1)^{r+1}\over2r!}x^r\log x+R_{r+1}(x),            \tag{4}
\]

with (R_{r+1}) real analytic at zero.  The induction is exact because an
antiderivative of (x^{r-1}\log x) is

\[
 {x^r\over r}\log x-{x^r\over r^2},
\]

and the second term is analytic.

## Collapse of the full derivative tower

For a polynomial (F), D.150 writes the two boundary parts of its complete
Gamma action as

\[
 B_-F(t)=\sum_{r\geq0}(-1)^rF^{(r)}(-T)H_{r+1}(t+T),
\]

\[
 B_+F(t)=\sum_{r\geq0}F^{(r)}(T)H_{r+1}(T-t).
\]

Using (4) and Taylor's identity gives, without a remainder,

\[
 (B_-F)_{\rm sing}(t)
 =-\frac12\sum_{r\geq0}{F^{(r)}(-T)\over r!}(t+T)^r
   \log(t+T)
 =-\frac12F(t)\log(t+T),                              \tag{5}
\]

and likewise

\[
 (B_+F)_{\rm sing}(t)=-\frac12F(t)\log(T-t).          \tag{6}
\]

Thus the complete contracted primitive action has the form

\[
 \boxed{
 A F(t)=-\frac12F(t)\log(T^2-t^2)+U_F(t),
 }                                                      \tag{7}
\]

where (U_F) is analytic on each of the finitely many contact cells.  The
only changes of analytic formula occur at the endpoints of the translated
supports for (n=2,3,4).  The Tate projection adds two entire exponentials
and therefore does not change (7).

Equation (7) is important computationally: one must never evaluate the 200
large endpoint derivatives separately near an endpoint.  Their singular
parts cancel to the single explicit expression in (7).

There is also a cancellation-free formula for the analytic remainder.  Put

\[
 q(z)=zK(z)={ze^{z/2}\over2\sinh z},\qquad q(0)=\frac12,
\]

and

\[
 R_1(x)=H_1(x)+\frac12\log x
 =\frac12\log\!\left({x(1+e^{-x/2})\over1-e^{-x/2}}\right)
  +\arctan(e^{-x/2}),                                 \tag{7a}
\]

so that (R_1(0)=\log2+\pi/4).  Both are analytic at zero.  If
(operatorname {DD}_F(t,s)=(F(t)-F(s))/(t-s)), then

\[
\begin{aligned}
 U_F(t)={}&
 \int_{-T}^{t}q(t-s)\operatorname {DD}_F(t,s)\,ds
 -\int_t^Tq(s-t)\operatorname {DD}_F(t,s)\,ds\\
 &+\{R_1(t+T)+R_1(T-t)\}F(t)
   -m_0F(t)-\text{the three contact translations}.    \tag{7b}
\end{aligned}
\]

The optional Tate projection only subtracts two entire exponentials.  For a
polynomial (F(t)=\sum_{k=0}^dc_kt^k), its divided difference is evaluated
without subtraction by the Horner recurrence

\[
 P=c_d, D=0;\qquad D\leftarrow P+sD,quad
 P\leftarrow c_k+tPquad(k=d-1,\ldots,0).             \tag{7c}
\]

At termination (D=\operatorname {DD}_F(t,s)).  The nearest poles of
(q) are at (pm\pi i), leaving a wide Bernstein ellipse on every
contact cell at the present value (2T=\log5).

## Exact log-square moments

The purely singular contribution to (H_X) is algebraic in polynomial
coefficients and standard special values.  After (t=Tu), for (a=k+1/2),

\[
 \int_{-1}^{1}u^{2k}\log^2\!\bigl(T^2(1-u^2)\bigr)\,du
 ={1\over a}\left[
 L^2+2L\{\psi(1)-\psi(a+1)\}
 +\{\psi(1)-\psi(a+1)\}^2
 +\psi_1(1)-\psi_1(a+1)
 \right],                                             \tag{8}
\]

where (L=\log T^2).  Odd moments vanish.  Formula (8) follows by taking
the first two derivatives in the second argument of

\[
 B(a,b)=\int_0^1y^{a-1}(1-y)^{b-1}\,dy
\]

at (b=1).  Hence the log-square block requires no numerical quadrature.

For implementation it is cleaner to put (x=(t+T)/(2T)).  Then

\[
 \log(T^2-t^2)=\log(4T^2)+\log x+\log(1-x).
\]

Writing (a=m+1), (H_a=\sum_{j=1}^a j^{-1}), and
(H_a^{(2)}=\sum_{j=1}^a j^{-2}), all required monomial moments are

\[
\begin{aligned}
 \int_0^1x^m\log x\,dx&=-a^{-2},&
 \int_0^1x^m\log^2x\,dx&=2a^{-3},\\
 \int_0^1x^m\log(1-x)\,dx&=-H_a/a,&
 \int_0^1x^m\log^2(1-x)\,dx&=(H_a^2+H_a^{(2)})/a,\\
 \int_0^1x^m\log x\log(1-x)\,dx
 &=H_a/a^2-\{\zeta(2)-H_a^{(2)}\}/a.
\end{aligned}                                                   \tag{9}
\]

They follow from the first and mixed second derivatives of (B(a,b)).
Thus every singular--singular entry is a finite Arb sum of rational
numbers, (log(4T^2)), and (zeta(2)).

## Remaining directed computation

After (8), only the analytic--analytic and explicit log--analytic cross
terms remain.  They are to be enclosed cell by cell by a directed
Gauss--Bernstein rule.  A complete certificate must then prove

\[
 K_{\rm final}-0.218^{-1}H_X>0                         \tag{10}
\]

by interval congruence.  The stable, non-directed D.169 diagnostic gives
the centre eigenvalues

\[
 2.78\,10^{-12},\quad5.48\,10^{-10},\quad
 2.88\,10^{-7},\quad2.79\,10^{-5},\quad1.99\,10^{-3}
\]

for (10).  These values size the required enclosure but are not used as a
proof.
