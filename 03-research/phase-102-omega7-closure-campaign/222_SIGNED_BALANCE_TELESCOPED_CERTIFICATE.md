# Signed balance telescoped certificate

## Purpose

`219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md` collapses the cumulative
kernel \(\mathcal H_n\).  This note pushes that collapse through the signed
balance identity of `187` and the finite certificate of `190`.

The result is a much smaller signed A1 target: after telescoping, the
integrated kernel has only two cutoff jumps, at \(T_7\) and \(T_8\).  All
intermediate jumps \(T_9,\ldots,T_{n-1}\) vanish.

This is the natural route left after `221` rules out the VK absolute
\(L^1\) strategy.

## Collapsed interval form

From `219`, for \(n\ge9\),
\[
\boxed{
\mathcal H_n(u)=
\begin{cases}
 -L_{n-1}^{(2)}(u)+L_7^{(2)}(u)+\beta_nL_7^{(1)}(u),
   &0<u<T_7,\\[1mm]
 -L_{n-1}^{(2)}(u)+\alpha_nL_7^{(2)}(u),
   &T_7<u<T_8,\\[1mm]
 -L_{n-1}^{(2)}(u),
   &T_8<u<T_n,
\end{cases}
}
\tag{1}
\]
where
\[
\boxed{
  \alpha_n={n(n+1)-56\over16},
  \qquad
  \beta_n={n(n+1)-72\over16}.
}
\tag{2}
\]

Equivalently, \(\alpha_n=\beta_n+1\).

## Raised derivative kernel

Let
\[
  G_n(u)=e^{-u}\mathcal H_n(u).
\]
Using
\[
  {d\over du}\left(e^{-u}L_m^{(\alpha)}(u)\right)
  =
  -e^{-u}L_m^{(\alpha+1)}(u),
\tag{3}
\]
we get
\[
  G_n'(u)=e^{-u}\mathcal R_n^{\rm tel}(u),
\]
where
\[
\boxed{
\mathcal R_n^{\rm tel}(u)=
\begin{cases}
 L_{n-1}^{(3)}(u)-L_7^{(3)}(u)-\beta_nL_7^{(2)}(u),
   &0<u<T_7,\\[1mm]
 L_{n-1}^{(3)}(u)-\alpha_nL_7^{(3)}(u),
   &T_7<u<T_8,\\[1mm]
 L_{n-1}^{(3)}(u),
   &T_8<u<T_n.
\end{cases}
}
\tag{4}
\]

Thus the raised kernel also has only the terminal Laguerre family plus
fixed degree-7 corrections.

## Jump collapse

The jumps of \(\mathcal H_n\) are now immediate from (1).

At \(T_7\),
\[
\begin{aligned}
  \Delta\mathcal H_n(T_7)
  &=
  \left[-L_{n-1}^{(2)}+\alpha_nL_7^{(2)}\right](T_7)
  -
  \left[-L_{n-1}^{(2)}+L_7^{(2)}+\beta_nL_7^{(1)}\right](T_7)\\
  &=
  \beta_n\left(L_7^{(2)}(T_7)-L_7^{(1)}(T_7)\right).
\end{aligned}
\]
Since
\[
  L_7^{(2)}-L_7^{(1)}=L_6^{(2)},
\]
\[
\boxed{
  \Delta\mathcal H_n(T_7)=\beta_nL_6^{(2)}(T_7).
}
\tag{5}
\]

At \(T_8\),
\[
\boxed{
  \Delta\mathcal H_n(T_8)=-\alpha_nL_7^{(2)}(T_8).
}
\tag{6}
\]

For every \(9\le j\le n-1\),
\[
\boxed{
  \Delta\mathcal H_n(T_j)=0.
}
\tag{7}
\]

This eliminates the long jump sum from `187`.

## Telescoped signed balance identity

Let
\[
  B(U)=\int_0^U(\psi(e^v)-e^v)\,dv.
\]
The exact integration-by-parts identity of `187` becomes
\[
\boxed{
\begin{aligned}
  J_n
  &=
  -B(T_n)e^{-T_n}L_{n-1}^{(2)}(T_n)\\
  &\quad
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n^{\rm tel}(u)\,du\\
  &\quad
  -
  B(T_7)e^{-T_7}\beta_nL_6^{(2)}(T_7)
  +
  B(T_8)e^{-T_8}\alpha_nL_7^{(2)}(T_8).
\end{aligned}
}
\tag{8}
\]

The signs in the last line come from subtracting the jump sum and using
(5)--(6).

## Signed A1 certificate

With the base-archimedean budget
\[
\mathcal A_n
  =
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right),
\tag{9}
\]
the cumulative diagonal target is
\[
\boxed{
\begin{aligned}
  \mathcal S_n^{\rm tel}
  &=
  \mathcal A_n
  -
  B(T_n)e^{-T_n}L_{n-1}^{(2)}(T_n)\\
  &\quad
  -
  \int_0^{T_n}B(u)e^{-u}\mathcal R_n^{\rm tel}(u)\,du\\
  &\quad
  -
  B(T_7)e^{-T_7}\beta_nL_6^{(2)}(T_7)
  +
  B(T_8)e^{-T_8}\alpha_nL_7^{(2)}(T_8)
  \ge0.
\end{aligned}
}
\tag{10}
\]

Together with the base condition already closed in `217`, (10) is
sufficient for A1 by the exact recurrence solution.

## Finite prime-power expansion

Expanding
\[
  B(U)=\sum_{m\le e^U}\Lambda(m)(U-\log m)-e^U+1
\tag{11}
\]
in (10) gives a finite prime-power certificate exactly as in `190`, but
with only the two jump endpoints \(T_7,T_8\) and the three interval kernels
from (4).

For \(m\le e^{T_n}\), the prime coefficient is
\[
\boxed{
\begin{aligned}
  \Xi_n^{\rm tel}(m)
  &=
  -(T_n-\log m)e^{-T_n}L_{n-1}^{(2)}(T_n)\\
  &\quad
  -
  \int_{\log m}^{T_n}
  (u-\log m)e^{-u}\mathcal R_n^{\rm tel}(u)\,du\\
  &\quad
  -1_{\log m\le T_7}
  (T_7-\log m)e^{-T_7}\beta_nL_6^{(2)}(T_7)\\
  &\quad
  +1_{\log m\le T_8}
  (T_8-\log m)e^{-T_8}\alpha_nL_7^{(2)}(T_8).
\end{aligned}
}
\tag{12}
\]

The pole coefficient is
\[
\boxed{
\begin{aligned}
  \Pi_n^{\rm tel}
  &=
  (e^{T_n}-1)e^{-T_n}L_{n-1}^{(2)}(T_n)\\
  &\quad
  +
  \int_0^{T_n}(e^u-1)e^{-u}\mathcal R_n^{\rm tel}(u)\,du\\
  &\quad
  +
  (e^{T_7}-1)e^{-T_7}\beta_nL_6^{(2)}(T_7)\\
  -
  (e^{T_8}-1)e^{-T_8}\alpha_nL_7^{(2)}(T_8).
\end{aligned}
}
\tag{13}
\]

Then the exact signed finite certificate is
\[
\boxed{
  \mathcal S_n^{\rm tel}
  =
  \mathcal A_n+\Pi_n^{\rm tel}
  +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m).
}
\tag{14}
\]

A1 follows if
\[
\boxed{
  \mathcal A_n+\Pi_n^{\rm tel}
  +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m)\ge0
  \qquad(n\ge9).
}
\tag{15}
\]

## What remains open

This is still a signed prime-power theorem, not a positivity proof.  The
coefficients \(\Xi_n^{\rm tel}(m)\) change sign, and no monotonicity of
\(\psi\) alone forces (15).

However, compared with `190`, the target is now much smaller:

1. only two cutoff jumps remain;
2. the raised kernel is a single \(L_{n-1}^{(3)}\) plus degree-7
   corrections;
3. the long off-diagonal structure has disappeared.

Thus the current signed route is exactly (15), not the larger raw
certificate of `190`.

## Status

Closed as the telescoped signed balance certificate.

A1 remains open.  The signed route has been reduced to the finite
prime-power inequality (15).
