# Mixed A0 degree-mismatch audit

## Purpose

`211_MIXED_INTERVAL_OFFDIAGONAL_LOAD_GATE.md` isolates the mixed
off-diagonal load
\[
  \mathcal M_n(\varepsilon)
  =
  \sum_{j=7}^{n-2}
  \int_{T_j}^{T_{j+1}}\varepsilon(u)|\mathcal H_n(u)|\,du.
\]

This note checks the most direct idea: use the A0 decay available at the
left endpoint \(T_j\) on the interval \((T_j,T_{j+1})\), together with the
elementary polynomial Laguerre bound.  The result is a no-go for that crude
route.  The A0 cutoff at index \(j\) is calibrated to degree \(j\), while
the mixed kernel on \((T_j,T_{j+1})\) contains degrees up to \(n-2\).

Thus the mixed load cannot be dominated by A0 interval-by-interval without
an additional off-diagonal Laguerre theorem or cancellation inside the
cumulative mixture.

## Local A0 decay at \(T_j\)

For the relative PNT profile
\[
  |E(e^u)|\le e^u\varepsilon(u),
  \qquad
  \varepsilon(u)=A\exp(-\eta(u)),
\]
the A0 cutoff condition at index \(j\) gives, for \(u\ge T_j\),
\[
  \eta(u)
  \ge
  (j+1)\log(1+u)+\log {12Aj^2\over B_j}.
\tag{1}
\]

Therefore
\[
\boxed{
  \varepsilon(u)
  \le
  {B_j\over12j^2}(1+u)^{-(j+1)}
  \qquad(u\ge T_j).
}
\tag{2}
\]

This is exactly the decay scale A0 provides from the \(j\)-th cutoff.

## Off-diagonal Laguerre degree

On \((T_j,T_{j+1})\), the leading mixed part of \(\mathcal H_n\) is
\[
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u).
\tag{3}
\]

The elementary Laguerre bound gives
\[
\boxed{
  |L_{k-1}^{(2)}(u)|
  \le
  k^2(1+u)^{k-1}
  \qquad(u\ge0).
}
\tag{4}
\]

Combining (2) and (4), the crude A0-triangle estimate for a single
off-diagonal summand gives
\[
\boxed{
  \varepsilon(u)\,u\,|L_{k-1}^{(2)}(u)|
  \le
  {B_j\over12j^2}
  k^2u(1+u)^{k-j-2}.
}
\tag{5}
\]

For \(k\ge j+3\), the exponent \(k-j-2\) is positive.  Thus the elementary
estimate grows with \(u\) on the interval instead of producing decay.

This is the degree mismatch:
\[
  \hbox{A0 at }T_j\hbox{ supplies }(1+u)^{-(j+1)},
  \qquad
  L_{k-1}^{(2)}\hbox{ costs }(1+u)^{k-1}.
\]

The remaining factor is
\[
  (1+u)^{k-j-2}.
\]

## Consequence for the crude triangle route

The triangle route from `211`,
\[
\begin{aligned}
  &\sum_{j=7}^{n-2}
  \int_{T_j}^{T_{j+1}}
  \varepsilon(u)
  u\sum_{k=j+1}^{n-1}w_{n,k}|L_{k-1}^{(2)}(u)|\,du
  +\cdots,
\end{aligned}
\tag{6}
\]
cannot be closed from (2) and (4) alone.  The terms with \(k\gg j\) carry a
positive power of \(1+u\).  Therefore the A0 decay attached to \(T_j\) does
not see the higher degrees present in the same interval.

This does not prove that the mixed load is large.  It proves only that the
naive proof architecture
\[
  \hbox{A0 decay}+\hbox{elementary absolute Laguerre bound}
\]
is structurally insufficient.

## What kind of theorem is still needed

To close the mixed absolute route, one needs at least one of the following:

1. an off-diagonal Laguerre theorem improving (4) in the regime
   \(u\in(T_j,T_{j+1})\), \(k>j\);
2. cancellation inside the cumulative mixture
   \[
     u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)
     -1_{j\ge8}w_{n,j}jL_j^{(2)}(u)
     +w_{n,j+1}(j+2)L_{j-1}^{(2)}(u);
   \]
3. a different cutoff policy that supplies decay calibrated to the largest
   active degree \(n\) on every earlier interval;
4. a signed compact proof avoiding the absolute \(L^1\) route.

## Status

Closed as a no-go for the crude A0-plus-polynomial-bound mixed estimate.

A1 remains open.  The mixed intervals require a genuinely off-diagonal or
signed theorem; A0 cannot simply be recycled locally with elementary
Laguerre size bounds.
