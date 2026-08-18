# D.79 supplement — convex trapezoid lower remainder for the Gamma tail

For `t>=0` set

\[
 f_t(x)={1\over x(x^2+t^2)},\qquad x>0.                 \tag{1}
\]

Then

\[
 f_t''(x)=
 {2(t^4+3t^2x^2+6x^4)\over x^3(x^2+t^2)^3}>0.         \tag{2}
\]

Consequently, for every `x_0>0`, convexity on each interval of length two
gives

\[
 \int_{x_0+2k}^{x_0+2k+2}f_t(x)\,dx
 \le f_t(x_0+2k)+f_t(x_0+2k+2).                        \tag{3}
\]

Summing (3) and using `f_t(x)->0` proves the directed lower bound

\[
 \boxed{
 \sum_{k=0}^{\infty}f_t(x_0+2k)
 \ge {1\over2}\int_{x_0}^{\infty}f_t(x)\,dx
      +{1\over2}f_t(x_0).}                             \tag{4}
\]

For `t>0`, the right side is explicitly

\[
 {1\over4t^2}\log\left(1+{t^2\over x_0^2}\right)
 +{1\over2x_0(x_0^2+t^2)}.                             \tag{5}

At `t=0` its continuous value is

\[
 {1\over4x_0^2}+{1\over2x_0^3}.                       \tag{6}

Applied after any finite prefix of the Gamma-resolvent series, (4) is
strictly stronger than the decreasing-function integral bound.  Every
quantity is positive, so interval endpoints can be chosen monotonically:
an upper endpoint for `t` lowers the finite terms and the remainder, while
the separately subtracted anchor is evaluated at the adverse lower
endpoint.

