# Tail-sign Laguerre zero partition gate

## Purpose

`247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md` shows that compact A1 follows
from a quarter Li margin plus the signed tail condition
\[
  R_n(T_n)\le0.
\]

This note writes that tail condition in the canonical Laguerre-zero
partition.  It is the tail analogue of the compact lobe partition in
`144_LAGUERRE_CORE_SIGN_PARTITION.md`.

## Tail sign condition

The paired tail is
\[
  R_n(T_n)
  =
  -\int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du,
\]
where \(E(x)=\psi(x)-x\).  Therefore
\[
\boxed{
  R_n(T_n)\le0
}
\tag{1}
\]
is exactly
\[
\boxed{
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge0.
}
\tag{2}
\]

This is a signed tail theorem, not an A0 consequence.

## Zero partition of the tail

Let
\[
  0<\tau_{n,1}<\tau_{n,2}<\cdots<\tau_{n,n-1}
\]
be the positive zeros of \(L_{n-1}^{(2)}\).  Let
\[
  \tau_{n,r_0}\le T_n<\tau_{n,r_0+1}
\]
with the conventions \(r_0=0\) if \(T_n<\tau_{n,1}\), and
\(r_0=n-1\) if \(T_n\ge\tau_{n,n-1}\).

Define the tail breakpoints
\[
  b_0=T_n,
  \qquad
  b_j=\tau_{n,r_0+j}\quad(1\le j\le n-1-r_0),
\]
and
\[
  b_{N_n+1}=\infty,
  \qquad
  N_n=n-1-r_0.
\]

On each interval
\[
  J_{n,j}=(b_j,b_{j+1})
  \qquad(0\le j\le N_n),
\]
the sign of \(L_{n-1}^{(2)}\) is constant.  Let
\[
  \sigma_{n,j}=\mathrm{sgn}\,L_{n-1}^{(2)}(u)
  \qquad(u\in J_{n,j}).
\]

Define the signed lobe moments
\[
\boxed{
  \mathcal E_{n,j}
  =
  \int_{J_{n,j}}
    E(e^u)e^{-u}\left|L_{n-1}^{(2)}(u)\right|\,du.
}
\tag{3}
\]

Then
\[
\boxed{
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  =
  \sum_{j=0}^{N_n}\sigma_{n,j}\mathcal E_{n,j}.
}
\tag{4}
\]

Consequently the nonpositive-tail theorem is exactly
\[
\boxed{
  \sum_{j=0}^{N_n}\sigma_{n,j}\mathcal E_{n,j}\ge0.
}
\tag{5}
\]

The last interval \(J_{n,N_n}\) may be an infinite ray.  It is harmless
analytically because the kernel has the factor \(e^{-u}\) and
\(L_{n-1}^{(2)}\) is polynomial.

## Final-ray reduction

If the A0 cutoff satisfies
\[
  T_n\ge\tau_{n,n-1},
\tag{6}
\]
then there are no remaining Laguerre zeros in the tail and (5) reduces to
one weighted Chebyshev tail sign:
\[
\boxed{
  \sigma_{n,0}
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}
    \left|L_{n-1}^{(2)}(u)\right|\,du
  \ge0.
}
\tag{7}
\]

Since the sign is constant on the final ray, this is equivalent to a
one-sided weighted average of \(E(e^u)\) on that ray.  No known symmetric
PNT or A0 estimate determines this sign.

If instead \(T_n<\tau_{n,n-1}\), then (5) is an alternating finite lobe
balance plus the final ray.  Any proof must pair the lobes before taking
absolute values, just as in the compact lobe theorem of `144`.

## Relation to the quarter-margin route

Combining `247` with (5), compact A1 follows from
\[
  \lambda_n\ge {1\over4}A_n
\tag{8}
\]
and
\[
  \sum_{j=0}^{N_n}\sigma_{n,j}\mathcal E_{n,j}\ge0.
\tag{9}
\]

The first condition is RH-strength by `248`.  The second is the exact
signed tail condition.  Neither condition is supplied by A0:
A0 gives only
\[
  R_n(T_n)\le {1\over4}A_n,
\]
which is the lower bound
\[
  \sum_{j=0}^{N_n}\sigma_{n,j}\mathcal E_{n,j}
  \ge
  -{1\over4}A_n,
\]
not the nonnegative sign (9).

## Status

Closed as the tail-sign Laguerre zero partition gate.

A1 remains open.  The new exact target for the nonpositive-tail route is
the signed lobe inequality (5), possibly after proving that the cutoff lies
past enough Laguerre zeros to simplify the tail geometry.
