# D.173 — Exact endpoint-log collapse

## Verdict

For every polynomial (F), the complete Gamma action has the form

\[
 \boxed{
 G_\Gamma F(t)=-\frac12F(t)\log(T^2-t^2)+R_F(t),}
                                                                    \tag{0.1}
\]

where (R_F) extends real-analytically across both endpoints.  After adding
the constant mass and the three translated contacts, the remainder is
analytic on each of the finitely many contact cells.  Thus the endpoint
singularities in the total Gram of D.172 are not a tower of unrelated Lerch
functions: they are one explicit polynomial times one logarithm.

## 1. Collapse of the left boundary tower

Recall

\[
 H_s(x)=\sum_{j\ge0}\frac{e^{-(2j+1/2)x}}{(2j+1/2)^s},
 \qquad H_{s+1}'=-H_s.                                \tag{1.1}
\]

The elementary closed form

\[
 H_1(x)=\operatorname {atanh}(e^{-x/2})
        +\arctan(e^{-x/2})                            \tag{1.2}
\]

shows that (H_1(x)+\tfrac12\log x) is analytic at zero.  Repeatedly
integrating (1.1) gives

\[
 H_{r+1}(x)=
 \frac{(-1)^{r+1}}{2r!}x^r\log x+A_r(x),             \tag{1.3}
\]

with (A_r) analytic at zero.  The left boundary series in D.150 therefore
has singular part

\[
 \begin{aligned}
 &\sum_{r=0}^{d}(-1)^rF^{(r)}(-T)
   \frac{(-1)^{r+1}}{2r!}x^r\log x\\
 &\qquad=-\frac12
 \left(\sum_{r=0}^{d}\frac{F^{(r)}(-T)}{r!}x^r\right)\log x
 =-\frac12F(-T+x)\log x.                             \tag{1.4}
 \end{aligned}
\]

The equality is exact because the Taylor series terminates.

## 2. Right endpoint and the complete action

With (y=T-t), the right boundary coefficients in D.150 contain no
alternating sign, while

\[
 F(T-y)=\sum_{r=0}^{d}\frac{(-1)^rF^{(r)}(T)}{r!}y^r.
\]

Combining this identity with (1.3) gives the right singular part
(-\tfrac12F(t)\log(T-t)).  The interior derivative term is polynomial.
Adding the two endpoints proves (0.1), since

\[
 \log(t+T)+\log(T-t)=\log(T^2-t^2).
\]

The translated zero extensions at (2,3,4) are polynomial on each contact
cell.  Hence they create break points but no additional endpoint
singularities.

## 3. Exact logarithmic moments

Set (x=(t+T)/(2T)) and (a=m+1).  The moments needed for the square of
(0.1) are

\[
\begin{aligned}
 \int_0^1x^m\log x\,dx&=-a^{-2},\\
 \int_0^1x^m\log^2x\,dx&=2a^{-3},\\
 \int_0^1x^m\log(1-x)\,dx&=-H_a/a,\\
 \int_0^1x^m\log^2(1-x)\,dx&=(H_a^2+H_a^{(2)})/a,\\
 \int_0^1x^m\log x\log(1-x)\,dx
 &=H_a/a^2-(\zeta(2)-H_a^{(2)})/a.                  \tag{3.1}
\end{aligned}
\]

They follow by differentiating
(B(\alpha,\beta)=\Gamma(\alpha)\Gamma(\beta)/
\Gamma(\alpha+\beta)) at ((\alpha,\beta)=(m+1,1)).
Since

\[
 \log(T^2-t^2)=\log(4T^2)+\log x+\log(1-x),          \tag{3.2}
\]

(3.1) integrates every polynomial--log and polynomial--log-squared term by
finite Arb arithmetic.  The remaining analytic cross terms can be enclosed
cellwise by a directed Chebyshev/Bernstein approximation.  This is the final
analytic preprocessing required for the five-dimensional endpoint Gram.
