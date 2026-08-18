# Euler--Gamma remainder bad-set certificate schema

## Purpose

The Abel--Fejer route now has three pieces:

1. `291` gives the constant threshold for the defect
   \[
     D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+.
   \]
2. `312`--`315` compute and optimize the canonical logarithmic-kernel
   contribution.
3. `296` gives a weighted Carleson sufficient condition for bad-set mass.

This note combines them into a single certificate schema for the remaining
Euler--Gamma part.  It specifies exactly what must be proved about the
non-logarithmic remnant in order to close the Abel--Fejer strong-margin
route.

## Decomposition input

Assume a non-circular construction of the positive increment measure gives
\[
\boxed{
  d\nu_g=aL\,dm+d\rho,
  \qquad
  0<a\le1,\qquad
  \rho\ge0,
}
\tag{1}
\]
where
\[
  L(e^{i\theta})=-\log|2\sin(\theta/2)|.
\]
The case with an additional bounded absolutely continuous component is
included in \(\rho\); by `295` it contributes no logarithmic bad-set
coefficient, and may be removed from the obstruction if desired.

Assume also the effective Abel lower bound for the full measure:
\[
\boxed{
  \int P_{1-1/n}\,d\nu_g\ge \log n-B_P
  \qquad(n\ge N_P).
}
\tag{2}
\]

## Log-kernel defect contribution

For fixed \(0<\alpha<2\), `312` gives the leading coefficient
\[
\boxed{
  \int D_{n,\alpha}\,L\,dm
  =
  \kappa_\alpha\log n+o_\alpha(\log n).
}
\tag{3}
\]
An effective certificate must replace this by a concrete inequality
\[
\boxed{
  \int D_{n,\alpha}\,L\,dm
  \le
  \kappa_\alpha^+\log n+B_L
  \qquad(n\ge N_L),
}
\tag{4}
\]
where \(\kappa_\alpha^+\) is an explicit certified upper coefficient.

Then the logarithmic component contributes
\[
  a\kappa_\alpha^+\log n+aB_L.
\]

## Remainder certificate, direct form

The most direct remainder input is
\[
\boxed{
  \int D_{n,\alpha}\,d\rho
  \le e_\alpha\log n+B_\rho
  \qquad(n\ge N_\rho).
}
\tag{5}
\]

Combining (4)--(5),
\[
\boxed{
  \int D_{n,\alpha}\,d\nu_g
  \le
  d_\alpha\log n+B_D,
  \qquad
  d_\alpha=a\kappa_\alpha^+ + e_\alpha,
}
\tag{6}
\]
with \(B_D=aB_L+B_\rho\).

By `291`, this closes the eventual strong-margin range whenever
\[
\boxed{
  a\kappa_\alpha^+ + e_\alpha < 1-{\alpha\over2}.
}
\tag{7}
\]

## Remainder certificate, weighted bad-set form

Instead of (5), it is enough to prove the `292` bad-set bound for
\(\rho\).  Fix \(\tau>0\), and put
\[
  B_{n,\tau}=\{F_n<\tau P_{1-1/n}\}.
\]
Assume
\[
\boxed{
  \int_{B_{n,\tau}}P_{1-1/n}\,d\rho
  \le b_{\rho,\tau}\log n+B_B
}
\tag{8}
\]
and a Poisson upper scale for the remnant
\[
\boxed{
  \int P_{1-1/n}\,d\rho
  \le c_\rho^+\log n+B_\rho^+
}
\tag{9}
\]
for all \(n\ge N_\rho\).

Then `292` gives
\[
\boxed{
  e_\alpha
  =
  b_{\rho,\tau}+(1-\alpha\tau)_+c_\rho^+.
}
\tag{10}
\]
Thus the closure condition becomes
\[
\boxed{
  a\kappa_\alpha^+
  +b_{\rho,\tau}
  +(1-\alpha\tau)_+c_\rho^+
  <
  1-{\alpha\over2}.
}
\tag{11}
\]

Finally, `296` supplies a sufficient way to prove (8): if root windows
\(I_{n,k}(\tau)\) cover \(B_{n,\tau}\) and
\[
\boxed{
  \sum_{k=0}^{n-1}
  {n\,\rho(I_{n,k}(\tau))\over1+\kappa(k)^2}
  \le
  \beta_{\rho,\tau}\log n+B_\beta,
}
\tag{12}
\]
then
\[
\boxed{
  b_{\rho,\tau}=C_\tau\beta_{\rho,\tau}
}
\tag{13}
\]
is admissible, with the explicit geometric constant \(C_\tau\) from the
cover/Poisson comparison.

## Effective threshold

Let
\[
  q_\alpha= {1-d_\alpha\over\alpha},
  \qquad
  B_\alpha=B_P+B_D.
\]
If \(d_\alpha<1-\alpha/2\), then \(q_\alpha>1/2\), and the strong-margin
range starts at
\[
\boxed{
  N_\infty(\alpha)
  =
  \max\left(
    N_P,N_L,N_\rho,2,
    \left\lceil
      \exp\left({3+B_\alpha/\alpha\over q_\alpha-1/2}\right)
    \right\rceil
  \right).
}
\tag{14}
\]
Equivalently, using the notation of `291`, one may set
\[
  B_{\rm Fejer}={B_P+B_D\over\alpha}
\]
and write the last exponential as
\[
  \exp\left({3+B_{\rm Fejer}\over q_\alpha-1/2}\right).
\]

For \(n\ge N_\infty(\alpha)\), strong margin holds.  The remaining finite
range
\[
  8\le n<N_\infty(\alpha)
\]
must be closed by the interval certificate of `261`.

## Status

Closed as the Euler--Gamma remainder certificate schema for the Abel--Fejer
route.  A1 remains open until the decomposition (1), the effective log
defect bound (4), and either the direct remnant defect estimate (5) or the
weighted bad-set estimate (12) are proved with constants satisfying
(7) or (11), plus the finite remainder.
