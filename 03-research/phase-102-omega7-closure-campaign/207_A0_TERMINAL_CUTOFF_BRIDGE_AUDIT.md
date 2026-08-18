# A0 terminal-cutoff bridge audit

## Purpose

`201_TERMINAL_LAGUERRE_LOAD_GATE.md` shows that every absolute diagonal
proof must dominate the terminal load
\[
  \mathcal T_n(\varepsilon)
  =
  \int_{T_{n-1}}^{T_n}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
\]

This note asks whether the A0 cutoff definition itself automatically makes
that terminal load small.  The answer is almost, but not enough: the cutoff
for index \(n-1\) controls the interval \([T_{n-1},T_n]\) with a borderline
\((1+u)^{-1}\) loss.  Thus the terminal gate becomes an explicit
cutoff-ratio or surplus-decay condition, not a closed theorem.

## Laguerre size bound

The identity
\[
  L_{n-1}^{(2)}(u)=\sum_{j=0}^{n-1}L_j^{(1)}(u)
\]
and the elementary bound used in A0,
\[
  |L_j^{(1)}(u)|\le (j+1)(1+u)^j,
\]
give, for \(u\ge0\),
\[
\boxed{
  |L_{n-1}^{(2)}(u)|
  \le
  n^2(1+u)^{n-1}.
}
\tag{1}
\]

This is deliberately crude; it is the bound compatible with the A0
tail proof and therefore shows exactly what A0 alone can supply.

## A0 cutoff for the preceding index

Assume the relative PNT envelope
\[
  |E(e^u)|\le A e^u\exp(-\eta(u)),
  \qquad
  \varepsilon(u)=A\exp(-\eta(u)).
\tag{2}
\]

For index \(n-1\), A0 chooses \(T_{n-1}\) so that for every
\(u\ge T_{n-1}\),
\[
  \eta(u)
  \ge
  n\log(1+u)+\log {12A(n-1)^2\over B_{n-1}},
\tag{3}
\]
where \(0<B_{n-1}\le\lambda_{n-1}^{\rm arch}\).

Combining (1)--(3), for \(u\ge T_{n-1}\),
\[
\begin{aligned}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|
  &\le
  A\exp(-\eta(u))\,n^2(1+u)^{n-1}\\
  &\le
  {n^2\over12(n-1)^2}
  {B_{n-1}\over1+u}.
\end{aligned}
\tag{4}
\]

Therefore
\[
\boxed{
  \mathcal T_n(\varepsilon)
  \le
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
}
\tag{5}
\]

This is the exact A0-to-terminal bridge obtainable from the previous
cutoff and the elementary Laguerre bound.

## Consequence for the absolute route

The absolute diagonal route requires
\[
  \mathcal B_n\ge \mathcal T_n(\varepsilon).
\tag{6}
\]

By (5), A0 would imply the terminal gate if one also proved
\[
\boxed{
  \mathcal B_n
  \ge
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}
  \qquad(n\ge9).
}
\tag{7}
\]

This is a new explicit sufficient bridge, but it is not automatic from A0.
The A0 theorem controls the tail beyond \(T_{n-1}\) with the kernel degree
of index \(n-1\).  The terminal Laguerre load for index \(n\) has one more
degree, and that extra degree is exactly what leaves the nonintegrable
\((1+u)^{-1}\) factor in (4).

## One-degree surplus variant

If the cutoff \(T_{n-1}\) were chosen with one extra power of surplus, namely
\[
  \eta(u)
  \ge
  (n+1)\log(1+u)+\log {12A(n-1)^2\over B_{n-1}}
  \qquad(u\ge T_{n-1}),
\tag{8}
\]
then the same calculation would give
\[
  \varepsilon(u)|L_{n-1}^{(2)}(u)|
  \le
  {n^2\over12(n-1)^2}
  {B_{n-1}\over(1+u)^2},
\]
and hence
\[
\boxed{
  \mathcal T_n(\varepsilon)
  \le
  {n^2\over12(n-1)^2}
  {B_{n-1}\over1+T_{n-1}}.
}
\tag{9}
\]

Thus an intentionally overpowered cutoff can make the terminal load small
without a cutoff-ratio loss.  This does not close A1, because:

1. the diagonal compact interval grows when \(T_n\) is enlarged;
2. the earlier mixed intervals of \(\mathcal H_n\) still remain;
3. the base comparison \(\mathcal B_n\ge\mathcal T_n\) must still be proved
   with explicit constants.

## No automatic signed gain

The bridge (5) is an absolute estimate.  It does not use the sign of
\[
  E(e^u)L_{n-1}^{(2)}(u)
\]
on the terminal interval.  Therefore it cannot replace the signed A1
mechanism.  It only says what the existing A0 decay can buy if the program
chooses to pursue the absolute \(L^1\) route.

In particular, the statement
\[
  u\ge T_{n-1}
\]
alone is insufficient: without the cutoff-ratio condition (7), a long
interval \([T_{n-1},T_n]\) can consume the available terminal budget through
the logarithmic factor in (5).

## Exact remaining theorem

The terminal absolute route is now reduced to:

1. prove the cutoff-ratio bridge (7), or choose cutoffs with surplus (8) and
   prove the resulting bound (9) is below \(\mathcal B_n\);
2. then dominate the earlier mixed-interval loads from
   `197_CUMULATIVE_KERNEL_INTERVAL_FORM.md`;
3. or abandon the absolute route and prove one of the signed A1 closure
   theorems listed in `196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md`.

## Status

Closed as an A0-to-terminal bridge audit.

A1 remains open.  The A0 cutoff gives a useful terminal estimate, but only
with an explicit cutoff-ratio or surplus-decay condition; it does not
automatically close the absolute diagonal route.
