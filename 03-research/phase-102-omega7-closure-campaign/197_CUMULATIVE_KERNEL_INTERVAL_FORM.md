# Cumulative kernel interval form

## Purpose

`193_WEIGHTED_L1_KERNEL_CERTIFICATE.md` reduces the absolute diagonal route
to the sign partition of the piecewise polynomial kernel \(\mathcal H_n\).
This note writes those interval polynomials explicitly.

The result sharpens the \(L^1\) route: the final interval is controlled by a
single Laguerre polynomial, but every earlier interval contains a cumulative
Laguerre mixture.  Therefore standard interlacing for one Laguerre family
does not by itself supply the uniform \(L^1\) domination needed by `191`.

## Setup

Assume the A0 cutoffs are strictly increasing:
\[
  0<T_7<T_8<\cdots<T_n.
\]

For \(n\ge9\), recall
\[
  \mathcal H_n(u)
  =
  \sum_{k=8}^{n-1}w_{n,k}\mathcal K_k(u),
  \qquad
  w_{n,k}
  =
  {1\over2}\left({n(n+1)\over k(k+1)}-1\right).
\tag{1}
\]

From `185`,
\[
\begin{aligned}
  \mathcal K_k(u)
  &=
  uL_{k-1}^{(2)}(u)1_{[0,T_k]}(u)
  -kL_k^{(2)}(u)1_{[T_k,T_{k+1}]}(u)\\
  &\quad
  +(k+1)L_{k-2}^{(2)}(u)1_{[T_{k-1},T_k]}(u).
\end{aligned}
\tag{2}
\]

Endpoint values are irrelevant for \(L^1\) integrals, so all formulas below
are stated on open intervals.

## First interval

On \((0,T_7)\), only the first line of (2) contributes.  Therefore
\[
\boxed{
  \mathcal H_n(u)
  =
  u\sum_{k=8}^{n-1}w_{n,k}L_{k-1}^{(2)}(u),
  \qquad 0<u<T_7.
}
\tag{3}
\]

This is already a mixed Laguerre polynomial.  It is not one member of an
orthogonal Laguerre sequence.

## Interior cutoff intervals

Let \(7\le j\le n-2\).  On \((T_j,T_{j+1})\), the active pieces are:

- the first line of (2) for \(k\ge j+1\);
- the middle line for \(k=j\), when \(j\ge8\);
- the last line for \(k=j+1\).

Thus
\[
\boxed{
\begin{aligned}
  \mathcal H_n(u)
  &=
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)\\
  &\quad
  -1_{j\ge8}\,w_{n,j}\,j\,L_j^{(2)}(u)
  +
  w_{n,j+1}(j+2)L_{j-1}^{(2)}(u),
  \qquad T_j<u<T_{j+1}.
\end{aligned}
}
\tag{4}
\]

For \(j=7\), the middle term is absent and the final term is
\[
  9w_{n,8}L_6^{(2)}(u).
\]

Formula (4) is the exact interval polynomial used in the sign-partition
certificate of `193`.

## Last interval

On \((T_{n-1},T_n)\), only the middle line of \(\mathcal K_{n-1}\)
contributes.  Hence
\[
\boxed{
  \mathcal H_n(u)
  =
  -w_{n,n-1}(n-1)L_{n-1}^{(2)}(u),
  \qquad T_{n-1}<u<T_n.
}
\tag{5}
\]

Since
\[
  w_{n,n-1}
  =
  {1\over2}\left({n(n+1)\over (n-1)n}-1\right)
  =
  {1\over n-1},
\]
(5) simplifies to
\[
\boxed{
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u),
  \qquad T_{n-1}<u<T_n.
}
\tag{6}
\]

Thus the terminal interval retains the original Laguerre oscillation with
no damping from the cumulative weights.

## Consequence for the weighted \(L^1\) load

For a relative PNT profile \(R(u)=e^u\varepsilon(u)\),
\[
  W_n(\varepsilon)
  =
  \int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du.
\]

Using (3)--(6),
\[
\boxed{
\begin{aligned}
  W_n(\varepsilon)
  &=
  \int_0^{T_7}
  \varepsilon(u)
  \left|
    u\sum_{k=8}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)
  \right|du\\
  &\quad+
  \sum_{j=7}^{n-2}
  \int_{T_j}^{T_{j+1}}
  \varepsilon(u)
  \left|
    u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)
    -1_{j\ge8}w_{n,j}jL_j^{(2)}(u)
    +w_{n,j+1}(j+2)L_{j-1}^{(2)}(u)
  \right|du\\
  &\quad+
  \int_{T_{n-1}}^{T_n}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
\end{aligned}
}
\tag{7}
\]

The absolute diagonal theorem from `191` is exactly
\[
  \mathcal B_n\ge W_n(\varepsilon)\qquad(n\ge9).
\tag{8}
\]

## What standard Laguerre zero theory can and cannot do

On the terminal interval, (6) allows direct use of the zeros of
\[
  L_{n-1}^{(2)}.
\]
This controls the sign partition of the last integral in (7).

On the earlier intervals, however, the polynomials are not single Laguerre
polynomials.  They are cumulative mixtures of the form
\[
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}
  -1_{j\ge8}w_{n,j}jL_j^{(2)}
  +w_{n,j+1}(j+2)L_{j-1}^{(2)}.
\tag{9}
\]

Standard interlacing between zeros of
\[
  L_m^{(2)},\qquad L_{m+1}^{(2)}
\]
does not determine the zeros or signs of (9).  A proof of (8) needs one of
the following additional inputs:

1. a real-rootedness and zero-location theorem for the cumulative mixtures
   (9);
2. a direct \(L^1\) bound for (9) without locating all zeros;
3. a cancellation theorem returning to the signed pairing rather than the
   absolute route.

Thus the phrase "Laguerre interlacing" is not yet a theorem for the
cumulative kernel.  It becomes useful only after being upgraded to one of
the three statements above.

## Terminal lower-load warning

Because of (6),
\[
  W_n(\varepsilon)
  \ge
  \int_{T_{n-1}}^{T_n}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
\tag{10}
\]

Therefore any absolute proof must at least show
\[
  \mathcal B_n
  \ge
  \int_{T_{n-1}}^{T_n}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
\tag{11}
\]
for all \(n\ge9\), in addition to controlling the earlier mixed intervals.

If (11) fails for a proposed envelope and cutoff system, then the absolute
diagonal route fails for that proposal.  If (11) holds, it is only a
necessary condition; the mixed intervals in (7) remain.

## Status

Closed as an interval normal form for the cumulative kernel and its
weighted \(L^1\) load.

A1 remains open.  The absolute route now requires uniform control of the
explicit interval expression (7), not merely standard zero interlacing for
individual Laguerre polynomials.
