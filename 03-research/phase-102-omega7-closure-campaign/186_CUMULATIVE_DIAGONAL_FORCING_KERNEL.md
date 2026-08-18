# Cumulative diagonal forcing kernel

## Purpose

`183_EXACT_CUMULATIVE_FORCING_REPRESENTATION.md` gives the weighted
cumulative induction inequality, and
`185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md` writes each diagonal forcing as
one signed integral.

This note combines them.  The A1 induction route becomes a single
cumulative signed pairing
\[
  \int_0^\infty E(e^u)e^{-u}\mathcal H_n(u)\,du
\]
plus explicit finite archimedean and base terms.

## Cumulative weights

For \(n\ge9\) and \(8\le k\le n-1\), define
\[
  w_{n,k}
  =
  {1\over2}
  \left({n(n+1)\over k(k+1)}-1\right).
\tag{1}
\]

These are positive:
\[
  w_{n,k}>0
  \qquad(8\le k\le n-1).
\tag{2}
\]

The exact A1 induction inequality from `183` and `185` is
\[
\begin{aligned}
  0\le \mathcal S_n
  &:=
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast \\
  &\quad+
  \sum_{k=8}^{n-1}
  w_{n,k}
  \left[
    1+{3\over4}D_k^{\rm arch}
    +
    \int_0^\infty E(e^u)e^{-u}\mathcal K_k(u)\,du
  \right].
\end{aligned}
\tag{3}
\]

## Cumulative kernel

Define
\[
  \boxed{
  \mathcal H_n(u)
  =
  \sum_{k=8}^{n-1}w_{n,k}\mathcal K_k(u).
  }
\tag{4}
\]

Then (3) becomes
\[
\boxed{
\begin{aligned}
  \mathcal S_n
  &=
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right)\\
  &\quad+
  \int_0^\infty E(e^u)e^{-u}\mathcal H_n(u)\,du.
\end{aligned}
}
\tag{5}
\]

Thus diagonal-induction A1 is equivalent to
\[
  \mathcal S_n\ge0\qquad(n\ge9),
\tag{6}
\]
together with the base condition \(C_8^\ast\ge0\).

## Support of the cumulative kernel

Since each \(\mathcal K_k\) is supported in
\[
  [0,T_{k+1}],
\]
the cumulative kernel \(\mathcal H_n\) is supported in
\[
  [0,T_n].
\tag{7}
\]

Therefore the diagonal induction route is genuinely compact: it only uses
prime-power data up to \(e^{T_n}\), matching the A1 compact core.

## Expanded form

Using `185`, one has
\[
\begin{aligned}
  \mathcal H_n(u)
  &=
  \sum_{k=8}^{n-1}w_{n,k}
  \bigg[
  uL_{k-1}^{(2)}(u)1_{[0,T_k]}(u)\\
  &\qquad
  -kL_k^{(2)}(u)1_{[T_k,T_{k+1}]}(u)
  +(k+1)L_{k-2}^{(2)}(u)1_{[T_{k-1},T_k]}(u)
  \bigg].
\end{aligned}
\tag{8}
\]

This formula is finite for each \(n\).  It is therefore a concrete finite
prime-power certificate target:
\[
  \int_0^{T_n}E(e^u)e^{-u}\mathcal H_n(u)\,du
\]
can be expanded into finite sums over \(m\le e^{T_n}\) plus elementary
exponential-polynomial integrals.

## Why cumulative positivity is not automatic

Although \(w_{n,k}>0\), the kernels \(\mathcal K_k\) are not
nonnegative.  They are built from Laguerre polynomials of adjacent degrees
and inherit their oscillatory lobes.

Consequently,
\[
  \mathcal H_n(u)\ge0
\]
does not follow from the construction.  In fact, because the highest-degree
piece near the last interval includes
\[
  -w_{n,n-1}(n-1)L_{n-1}^{(2)}(u)
  \qquad(T_{n-1}<u<T_n),
\tag{9}
\]
the cumulative kernel retains the final Laguerre oscillation unless the
chosen cutoffs force a special cancellation.  No such cancellation is part
of the current A0 construction.

Thus the following shortcut is invalid:
\[
  w_{n,k}>0
  \quad\Longrightarrow\quad
  \mathcal H_n\hbox{ is a positive kernel}.
\tag{10}
\]

The sign problem is still the signed pairing of \(E(e^u)\) with
\(\mathcal H_n\), plus the explicit archimedean correction.

## Exact theorem needed

The cumulative diagonal induction theorem is:

For every \(n\ge9\),
\[
\boxed{
\begin{aligned}
  &C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right)\\
  &\quad+
  \int_0^{T_n}E(e^u)e^{-u}\mathcal H_n(u)\,du
  \ge0.
\end{aligned}
}
\tag{11}
\]

Together with \(C_8^\ast\ge0\), (11) implies A1.

## Status

Closed as a cumulative-kernel normal form.  A1 remains open.

The live local target is the signed finite inequality (11), not positivity
of the cumulative kernel alone.
