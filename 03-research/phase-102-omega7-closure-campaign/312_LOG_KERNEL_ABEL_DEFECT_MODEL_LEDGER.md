# Log-kernel Abel-defect model ledger

## Purpose

The Abel-defect route asks for a bound on
\[
  D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+
\]
against the actual Euler--Gamma increment measure.  The spike no-goes show
that this is not automatic for arbitrary positive measures.  This note
records the opposite calibration: for the canonical logarithmic density
\[
  L(e^{i\theta})=-\log|2\sin(\theta/2)|,
\]
the leading defect coefficient is an explicit one-dimensional constant.

Thus the Abel-defect obstruction is not created by the logarithmic kernel
itself.  The remaining problem is to prove that the actual increment
measure has no additional Poisson-visible remnant concentrated at the
moving Fejer zeros.

## Scaling theorem

Let \(dm=d\theta/(2\pi)\),
\[
  P_n=P_{1-1/n},
  \qquad
  F_n(e^{i\theta})
  =
  {1\over n}
  \left({\sin(n\theta/2)\over\sin(\theta/2)}\right)^2 .
\]
For fixed \(\alpha>0\), define
\[
\boxed{
  \kappa_\alpha
  =
  {1\over 2\pi}
  \int_{-\infty}^{\infty}
  \left(
    {2\over 1+u^2}
    -
    \alpha
    \left({2\sin(u/2)\over u}\right)^2
  \right)_+\,du .
}
\tag{1}
\]
The value at \(u=0\) is understood by continuity.  Then
\[
\boxed{
  \int_{\partial\mathbb D}
  (P_n-\alpha F_n)_+\,L\,dm
  =
  \kappa_\alpha\log n+o_\alpha(\log n).
}
\tag{2}
\]

## Proof

Put \(\theta=u/n\).  Uniformly for \(u\) in a fixed compact set,
\[
  {1\over n}P_{1-1/n}(e^{iu/n})
  \longrightarrow
  p(u):={2\over 1+u^2},
\]
because
\[
  1-(1-1/n)^2={2\over n}+O(n^{-2})
\]
and
\[
  |e^{iu/n}-(1-1/n)|^2
  ={1+u^2\over n^2}+O_R(n^{-3})
  \qquad(|u|\le R).
\]
Likewise
\[
  {1\over n}F_n(e^{iu/n})
  \longrightarrow
  f(u):=\left({2\sin(u/2)\over u}\right)^2 .
\]
Therefore, on every fixed interval \([-R,R]\),
\[
  {1\over n}(P_n-\alpha F_n)_+(e^{iu/n})
  \longrightarrow
  (p(u)-\alpha f(u))_+
\]
uniformly away from no exceptional set, since \(x\mapsto x_+\) is
Lipschitz.

On the same interval,
\[
  L(e^{iu/n})
  =
  \log n-\log|u|+O_R(n^{-1})
\]
with the usual locally integrable interpretation at \(u=0\).  Hence
\[
\begin{aligned}
&\int_{|u|\le R}
  (P_n-\alpha F_n)_+(e^{iu/n})
  L(e^{iu/n})\,{du\over 2\pi n}                  \\
&\qquad =
  {\log n\over 2\pi}
  \int_{|u|\le R}(p(u)-\alpha f(u))_+\,du
  +O_{\alpha,R}(1).
\end{aligned}
\tag{3}
\]

It remains to pass \(R\to\infty\).  The tails are uniform at the
coefficient level.  Indeed
\[
  P_{1-1/n}(e^{i\theta})
  \le
  {C n\over 1+n^2\theta^2},
\]
and
\[
  F_n(e^{i\theta})
  \le
  C n\min\left(1,{1\over n^2\theta^2}\right)
\]
on \(|\theta|\le\pi\).  Consequently the positive part is dominated, after
the change \(u=n\theta\), by an \(L^1\)-tail of size \(O_\alpha(R^{-1})\)
outside \(|u|\le R\), and \(L(e^{iu/n})\le \log n+O(\log(2+|u|))\) there.
After division by \(\log n\), the omitted tail contributes
\[
  O_\alpha(R^{-1})+o_{n\to\infty}(1).
\]
Letting first \(n\to\infty\) and then \(R\to\infty\) proves (2).

The integral in (1) is finite because both \(p(u)\) and \(f(u)\) are
\(O(u^{-2})\) at infinity.

## Calibration at \(\alpha=1\)

For \(\alpha=1\), the coefficient is
\[
  \kappa_1
  =
  {1\over 2\pi}
  \int_{\mathbb R}
  \left(
    {2\over1+u^2}
    -
    \left({2\sin(u/2)\over u}\right)^2
  \right)_+du.
\]
Numerical quadrature with the elementary tail bound
\[
  \int_{|u|>R}{2\over1+u^2}\,{du\over2\pi}
  \le {2\over \pi R}
\]
places this constant near
\[
  \kappa_1\approx 0.2443.
\]
The numerical value is only a calibration in this ledger; the rigorous
output needed by `291` is the exact constant formula (1) plus an eventual
certified upper bound for the actual Euler--Gamma measure.

## Consequence for the live route

If the actual positive increment measure admitted a decomposition
\[
  d\nu_g = aL\,dm+d\rho
\]
with \(a\le1\), \(\rho\ge0\), an effective version of (2), and an
independent defect estimate
\[
  \int D_{n,\alpha}\,d\rho
  \le e_\alpha\log n+O(1),
\]
then the leading defect coefficient would be bounded by
\[
  \int D_{n,\alpha}\,d\nu_g
  \le
  (a\kappa_\alpha+e_\alpha+o(1))\log n.
\]
The `291` strong-margin threshold would follow if
\[
\boxed{
  a\kappa_\alpha+e_\alpha < 1-{\alpha\over2}.
}
\tag{4}
\]

Thus the log-density route and the Abel-defect route are compatible but not
identical.  The canonical logarithmic density has a computable defect
coefficient; what remains open is the construction of \(\nu_g\) and the
control of any residual positive component \(\rho\) near the moving Fejer
zeros.

## Status

Closed as a model constant ledger for the Abel-defect route.  It does not
prove A1 by itself.  A1 still requires either the direct local log-density
theorem of `263`--`264`, or the actual Euler--Gamma bad-set/defect estimate
of `291`--`292`.
