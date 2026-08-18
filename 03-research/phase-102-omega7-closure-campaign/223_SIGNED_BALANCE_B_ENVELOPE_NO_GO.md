# Signed balance \(B\)-envelope no-go

## Purpose

`222_SIGNED_BALANCE_TELESCOPED_CERTIFICATE.md` reduces the viable signed
route to the integrated balance
\[
\mathcal S_n^{\rm tel}
  =
  \mathcal A_n
  -
  B(T_n)e^{-T_n}L_{n-1}^{(2)}(T_n)
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n^{\rm tel}(u)\,du
  +\hbox{two base jumps}.
\]

This note audits whether that route can be closed using only a two-sided
envelope for the cumulative error \(B\).  The answer is no.  A symmetric
bound on \(B\) again converts the signed problem into an absolute
Laguerre \(L^1\) problem, now for \(L_{n-1}^{(3)}\), and the same bulk
obstruction as `221` applies.

## Symmetric \(B\)-envelope loss

Let \(Y(u)\ge0\) be an envelope satisfying
\[
  |B(u)|\le Y(u)
  \qquad(0\le u\le T_n).
\tag{1}
\]

The integral term in `222` is
\[
  -\int_0^{T_n}B(u)e^{-u}\mathcal R_n^{\rm tel}(u)\,du.
\tag{2}
\]

If the proof uses only (1), then the worst admissible sign pattern gives
\[
\boxed{
  -\int_0^{T_n}B(u)e^{-u}\mathcal R_n^{\rm tel}(u)\,du
  \ge
  -\int_0^{T_n}Y(u)e^{-u}
    |\mathcal R_n^{\rm tel}(u)|\,du.
}
\tag{3}
\]

This is sharp in the same variational sense as `188`: equality is attained
formally by choosing \(B\) aligned with
\(\operatorname{sgn}\mathcal R_n^{\rm tel}\).  Therefore a proof using only
a symmetric \(B\)-envelope must dominate the absolute load
\[
\boxed{
  \int_0^{T_n}Y(u)e^{-u}
    |\mathcal R_n^{\rm tel}(u)|\,du.
}
\tag{4}
\]

## Bulk obstruction for the raised kernel

From `222`,
\[
  \mathcal R_n^{\rm tel}(u)=L_{n-1}^{(3)}(u)
  \qquad(T_8<u<T_n).
\tag{5}
\]

Plancherel--Rotach in the bulk gives, for any fixed \(0<a<b<4\),
\[
\boxed{
  \int_{aN}^{bN}|L_N^{(3)}(u)|\,du
  \ge
  c_{a,b}N^{-K_{a,b}}e^{aN/2}
}
\tag{6}
\]
for all sufficiently large \(N\).  The polynomial power is irrelevant; the
decisive factor is \(e^{u/2}\) on any fixed bulk interval.

For \(N=n-1\), the interval \([2N,3N]\) lies inside \((T_8,T_n)\) for all
large \(n\), by the cutoff scale of `208`.

## VK-scale \(B\)-envelopes still fail

A VK estimate for \(E(e^u)\) also gives a cumulative bound of the form
\[
  Y(u)e^{-u}
  \le
  C\exp(-\eta(u))
\]
with \(\eta(u)=O(u^\theta(\log u)^q)\), \(0<\theta<1\), on dyadic ranges.
Even if one grants the corresponding lower model scale on the proof
envelope over \(u\asymp n\), the absolute load (4) has size at least
\[
  \exp\!\left(cn-O(n^\theta(\log n)^q)\right),
\]
whereas all base and endpoint budget terms in `222` are at most polynomial
or explicitly finite-order in the recurrence budget.

Thus a VK-scale two-sided theorem for \(B\) cannot close (10) of `222`.

## What kind of signed theorem is actually needed

The signed balance route must prove that the actual arithmetic function
\[
  B(u)=\sum_{m\le e^u}\Lambda(m)(u-\log m)-e^u+1
\]
does not correlate with the negative oscillatory sign pattern of
\[
  e^{-u}\mathcal R_n^{\rm tel}(u)
\]
strongly enough to defeat \(\mathcal A_n\) and the two base jumps.

Equivalently, one must prove the finite prime-power inequality
\[
  \mathcal A_n+\Pi_n^{\rm tel}
  +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m)\ge0
\]
from the actual distribution of prime powers, not from a symmetric
PNT-size envelope.

## Status

Closed as a no-go for closing the telescoped signed balance with only a
two-sided \(B\)-envelope.

A1 remains open.  The signed route requires genuine arithmetic sign
correlation or another non-absolute theorem.
