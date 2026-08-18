# Cumulative diagonal balance form

## Purpose

`186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md` reduces the diagonal induction
route to the compact signed pairing
\[
  J_n=\int_0^{T_n}E(e^u)e^{-u}\mathcal H_n(u)\,du .
\]

This note integrates that pairing once.  The result is an exact balance
formula involving the cumulative prime-pole error
\[
  B(U)=\int_0^U E(e^v)\,dv
\]
and a raised piecewise Laguerre kernel.

The important point is that \(\mathcal H_n\) is discontinuous at the moving
cutoffs.  Therefore the integration by parts contains explicit jump terms.
Those terms are signed and cannot be dropped.

## Convention

Assume the A0 cutoffs are strictly increasing:
\[
  0<T_7<T_8<\cdots<T_n.
\]
If two neighboring cutoffs coincide, the same formulas hold after coalescing
the repeated endpoint and adding the corresponding jumps.

For the Lebesgue integral, endpoint values of \(\mathcal H_n\) are
irrelevant.  For the balance formula, define
\[
  G_n(u)=e^{-u}\mathcal H_n(u)
\]
by its smooth values on the open intervals cut out by
\[
  T_7,T_8,\ldots,T_n.
\]
Write
\[
  G_n(a^-)=\lim_{u\uparrow a}G_n(u),
  \qquad
  G_n(a^+)=\lim_{u\downarrow a}G_n(u),
\]
and
\[
  \Delta G_n(a)=G_n(a^+)-G_n(a^-).
\tag{1}
\]

## Smooth derivative

For \(8\le k\le n-1\), define the smooth derivative kernel
\[
\begin{aligned}
  \mathcal R_k(u)
  &=
  \left[
    L_{k-1}^{(2)}(u)-uL_{k-1}^{(3)}(u)
  \right]1_{(0,T_k)}(u)\\
  &\quad
  +kL_k^{(3)}(u)1_{(T_k,T_{k+1})}(u)
  -(k+1)L_{k-2}^{(3)}(u)1_{(T_{k-1},T_k)}(u).
\end{aligned}
\tag{2}
\]

This follows from the raising identity
\[
  {d\over du}\left(e^{-u}L_m^{(\alpha)}(u)\right)
  =
  -e^{-u}L_m^{(\alpha+1)}(u)
\tag{3}
\]
and the product rule
\[
 {d\over du}\left(u e^{-u}L_{k-1}^{(2)}(u)\right)
 =
 e^{-u}\left[
   L_{k-1}^{(2)}(u)-uL_{k-1}^{(3)}(u)
 \right].
\tag{4}
\]

With the cumulative weights
\[
  w_{n,k}
  =
  {1\over2}\left({n(n+1)\over k(k+1)}-1\right),
\]
put
\[
  \boxed{
  \mathcal R_n(u)=\sum_{k=8}^{n-1}w_{n,k}\mathcal R_k(u).
  }
\tag{5}
\]

On every open interval avoiding the cutoffs,
\[
  G_n'(u)=e^{-u}\mathcal R_n(u).
\tag{6}
\]

## Jump formula

Using the interval form of `185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md`,
the jumps of a single \(\mathcal K_k\) are
\[
\begin{aligned}
  \Delta\mathcal K_k(T_{k-1})
  &=(k+1)L_{k-2}^{(2)}(T_{k-1}),\\
  \Delta\mathcal K_k(T_k)
  &=-(2k+1)L_{k-1}^{(2)}(T_k),\\
  \Delta\mathcal K_k(T_{k+1})
  &=kL_k^{(2)}(T_{k+1}).
\end{aligned}
\tag{7}
\]

All other jumps vanish.  Therefore, for \(7\le j\le n\),
\[
\boxed{
\begin{aligned}
  \Delta\mathcal H_n(T_j)
  &=
  1_{8\le j+1\le n-1}\,
  w_{n,j+1}(j+2)L_{j-1}^{(2)}(T_j)\\
  &\quad
  -1_{8\le j\le n-1}\,
  w_{n,j}(2j+1)L_{j-1}^{(2)}(T_j)\\
  &\quad
  +1_{8\le j-1\le n-1}\,
  w_{n,j-1}(j-1)L_{j-1}^{(2)}(T_j).
\end{aligned}
}
\tag{8}
\]

Since \(e^{-u}\) is continuous,
\[
  \Delta G_n(T_j)=e^{-T_j}\Delta\mathcal H_n(T_j).
\tag{9}
\]

The terminal point is best kept as a boundary term rather than as a jump:
\[
  G_n(T_n^-)=e^{-T_n}\mathcal H_n(T_n^-).
\tag{10}
\]

## Exact balance identity

On each open subinterval, \(B'(u)=E(e^u)\).  Integrating by parts on all
subintervals and summing gives
\[
\boxed{
\begin{aligned}
  J_n
  &=
  B(T_n)G_n(T_n^-)
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n(u)\,du\\
  &\quad
  -
  \sum_{j=7}^{n-1}
  B(T_j)e^{-T_j}\Delta\mathcal H_n(T_j).
\end{aligned}
}
\tag{11}
\]

There is no lower endpoint term because \(B(0)=0\).

Equivalently, inserting (10),
\[
\boxed{
\begin{aligned}
  J_n
  &=
  B(T_n)e^{-T_n}\mathcal H_n(T_n^-)
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n(u)\,du\\
  &\quad
  -
  \sum_{j=7}^{n-1}
  B(T_j)e^{-T_j}\Delta\mathcal H_n(T_j).
\end{aligned}
}
\tag{12}
\]

This is the once-integrated diagonal cumulative forcing identity.

## A1 induction in balance coordinates

Let
\[
\begin{aligned}
  \mathcal A_n
  &=
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right).
\end{aligned}
\tag{13}
\]

Then the cumulative diagonal induction condition from `186` is exactly
\[
\boxed{
\begin{aligned}
  0\le \mathcal S_n
  &=
  \mathcal A_n
  +
  B(T_n)e^{-T_n}\mathcal H_n(T_n^-)\\
  &\quad
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n(u)\,du\\
  &\quad
  -
  \sum_{j=7}^{n-1}
  B(T_j)e^{-T_j}\Delta\mathcal H_n(T_j).
\end{aligned}
}
\tag{14}
\]

Together with \(C_8^\ast\ge0\), (14) implies A1 by the exact recurrence
solution.

## Why the balance form is not a positivity proof

The transformation from \(J_n\) to (12) replaces the raw Chebyshev error by
the cumulative balance \(B\), but it creates two signed objects:

1. the raised piecewise kernel \(\mathcal R_n\);
2. the cutoff jump sum
   \[
     \sum_{j=7}^{n-1}
     B(T_j)e^{-T_j}\Delta\mathcal H_n(T_j).
   \]

Neither object is sign-definite.  The jump coefficients in (8) are
Laguerre values at the moving A0 cutoffs, not zeros chosen to cancel them.
Therefore the following inference is invalid:
\[
  \hbox{integrate once}
  \quad\Longrightarrow\quad
  \hbox{positive cumulative forcing}.
\tag{15}
\]

Any proof through the cumulative diagonal route must establish the signed
balance inequality (14) with all endpoint and jump terms included.

## Status

Closed as an exact balance normal form for the cumulative diagonal
induction route.

A1 remains open.  The sharpened local target is now the signed inequality
(14), including the raised-kernel integral and every cutoff jump in (8).
