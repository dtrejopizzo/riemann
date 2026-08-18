# Explicit archimedean upper input for the Fejer route

## Purpose

`259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` assumes an explicit upper input
\[
  A_n=\lambda_n^{\rm arch}
  \le {1\over2}n\log n+B_A n.
\]

This note supplies such a bound directly from the phase-102 archimedean
formula.  The constant is deliberately coarse; the important point is the
sharp leading coefficient \(1/2\), which matches the strong-margin Fejer
threshold.

## Archimedean formula

The phase split uses
\[
  A_n
  =
  1-{n\over2}\bigl(\gamma+\log(4\pi)\bigr)
  +
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^n-1+{n\over r}
  \right].
\tag{1}
\]

Let
\[
  q_n(x)=(1-x)^n-1+nx.
\]

For \(0\le x\le1\),
\[
  0\le q_n(x)\le nx
\tag{2}
\]
and, by Taylor's formula,
\[
  q_n(x)
  =
  n(n-1)\int_0^x (x-t)(1-t)^{n-2}\,dt
  \le {n(n-1)\over2}x^2.
\tag{3}
\]

Thus
\[
\boxed{
  q_n(x)\le \min\left(nx,{n(n-1)\over2}x^2\right).
}
\tag{4}
\]

## Odd harmonic upper bound

Let
\[
  m=\left\lfloor {n+1\over2}\right\rfloor.
\]
Then
\[
  \sum_{\substack{1\le r\le n\\ r\ {\rm odd}}}{1\over r}
  =
  \sum_{j=1}^{m}{1\over 2j-1}.
\]

Using
\[
  \sum_{j=1}^{m}{1\over 2j-1}
  =
  H_{2m}-{1\over2}H_m
\]
and the elementary bounds
\[
  H_{2m}\le 1+\log(2m),
  \qquad
  H_m\ge\log(m+1),
\]
we get
\[
\begin{aligned}
  \sum_{j=1}^{m}{1\over 2j-1}
  &\le
  1+\log(2m)-{1\over2}\log(m+1)\\
  &\le
  {1\over2}\log n+2
  \qquad(n\ge2).
\end{aligned}
\tag{5}
\]

The last inequality is intentionally coarse and follows from
\(m\le(n+1)/2\) and \(n\ge2\).

## Tail over odd indices

By (4), for the low range \(r\le n\),
\[
  \sum_{\substack{1\le r\le n\\ r\ {\rm odd}}}
  q_n(1/r)
  \le
  n\sum_{\substack{1\le r\le n\\ r\ {\rm odd}}}{1\over r}
  \le
  {1\over2}n\log n+2n.
\tag{6}
\]

For the high range \(r>n\), again from (4),
\[
\begin{aligned}
  \sum_{\substack{r>n\\ r\ {\rm odd}}}q_n(1/r)
  &\le
  {n(n-1)\over2}\sum_{r>n}{1\over r^2}\\
  &\le
  {n(n-1)\over2}\cdot {1\over n}
  \le {n\over2}.
\end{aligned}
\tag{7}
\]

Combining (6)--(7),
\[
\boxed{
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}q_n(1/r)
  \le
  {1\over2}n\log n+{5\over2}n
  \qquad(n\ge2).
}
\tag{8}
\]

## Explicit upper bound

The linear gamma/pole term in (1) is negative because
\[
  \gamma+\log(4\pi)>0.
\]
Dropping it only increases the upper bound.  Therefore, for \(n\ge2\),
\[
  A_n
  \le
  1+{1\over2}n\log n+{5\over2}n
  \le
  {1\over2}n\log n+3n.
\]

Hence
\[
\boxed{
  \lambda_n^{\rm arch}
  \le
  {1\over2}n\log n+3n
  \qquad(n\ge2).
}
\tag{9}
\]

Thus the Fejer closure theorem may take
\[
\boxed{
  B_A=3,\qquad N_A=2.
}
\tag{10}
\]

## Consequence for `259`

In the notation of `259`, if
\[
  \int F_n\,d\nu_g
  \ge
  \left({1\over2}+\eta\right)\log n-B_F,
\]
then strong margin follows for all
\[
  n\ge
  \max\left(
    N_F,\,
    \left\lceil\exp\left({3+B_F\over\eta}\right)\right\rceil
  \right),
\]
with the finite remaining range checked separately.

In the log-density alternative using `260` and `263`,
\[
  B_F=a+B_h^\ast,\qquad \eta=a-\frac12.
\]

## Status

Closed as the explicit archimedean upper input for the Fejer/log-density
route.

A1 remains open.  The unresolved inputs in this route are now exactly the
positive increment measure and the effective Fejer/log-density lower
theorem, plus the finite verification below the resulting threshold.
