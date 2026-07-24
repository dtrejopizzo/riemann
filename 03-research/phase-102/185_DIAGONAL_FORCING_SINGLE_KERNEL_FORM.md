# Diagonal forcing single-kernel form

## Purpose

`184_MOVING_DIAGONAL_RECURRENCE_DEFECT.md` gives the A1 diagonal forcing
\[
  F_n^{\rm diag}
  =
  F_n(T_n)
  +
  n\Phi_{n+1}(T_n,T_{n+1})
  -
  (n+1)\Phi_{n-1}(T_{n-1},T_n).
\]

This note rewrites \(F_n^{\rm diag}\) as one signed integral against a
single piecewise Laguerre kernel, plus the explicit archimedean correction.

The result is a compact target for the diagonal induction route.

## Starting point

From `184`,
\[
\begin{aligned}
  F_n^{\rm diag}
  &=
  M_n(T_n)+1+{3\over4}D_n^{\rm arch} \\
  &\quad
  -n\int_{T_n}^{T_{n+1}}
      E(e^u)e^{-u}L_n^{(2)}(u)\,du  \\
  &\quad
  +(n+1)\int_{T_{n-1}}^{T_n}
      E(e^u)e^{-u}L_{n-2}^{(2)}(u)\,du ,
\end{aligned}
\tag{1}
\]
where
\[
  M_n(T_n)=
  \int_0^{T_n}u\,E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{2}
\]

## Piecewise kernel

Define
\[
  \mathcal K_n(u)=
  \begin{cases}
    u\,L_{n-1}^{(2)}(u),
      &0\le u\le T_n,\\[4pt]
    -n\,L_n^{(2)}(u),
      &T_n<u\le T_{n+1},\\[4pt]
    (n+1)\,L_{n-2}^{(2)}(u),
      &T_{n-1}\le u<T_n,\\[4pt]
    0,
      &\hbox{otherwise},
  \end{cases}
\tag{3}
\]
where on the overlap \(T_{n-1}\le u\le T_n\) the first and third lines add.
Equivalently,
\[
\boxed{
\begin{aligned}
  \mathcal K_n(u)
  &=
  u\,L_{n-1}^{(2)}(u)\,1_{[0,T_n]}(u)\\
  &\quad
  -n\,L_n^{(2)}(u)\,1_{[T_n,T_{n+1}]}(u)\\
  &\quad
  +(n+1)L_{n-2}^{(2)}(u)\,1_{[T_{n-1},T_n]}(u).
\end{aligned}
}
\tag{4}
\]

Then
\[
\boxed{
  F_n^{\rm diag}
  =
  1+{3\over4}D_n^{\rm arch}
  +
  \int_0^\infty
  E(e^u)e^{-u}\mathcal K_n(u)\,du.
}
\tag{5}
\]

This is exact.

## Overlap simplification

On the overlap \(T_{n-1}\le u\le T_n\), the kernel is
\[
  uL_{n-1}^{(2)}(u)+(n+1)L_{n-2}^{(2)}(u).
\tag{6}
\]

Using the Laguerre recurrence
\[
  nL_n^{(2)}(u)
  =
  (2n+1-u)L_{n-1}^{(2)}(u)
  -(n+1)L_{n-2}^{(2)}(u),
\tag{7}
\]
we get
\[
  uL_{n-1}^{(2)}(u)+(n+1)L_{n-2}^{(2)}(u)
  =
  (2n+1)L_{n-1}^{(2)}(u)-nL_n^{(2)}(u).
\tag{8}
\]

Thus the kernel may also be written by intervals:
\[
\mathcal K_n(u)=
\begin{cases}
  uL_{n-1}^{(2)}(u),&0\le u<T_{n-1},\\[3pt]
  (2n+1)L_{n-1}^{(2)}(u)-nL_n^{(2)}(u),
    &T_{n-1}\le u\le T_n,\\[3pt]
  -nL_n^{(2)}(u),&T_n<u\le T_{n+1},\\[3pt]
  0,&\hbox{otherwise}.
\end{cases}
\tag{9}
\]

## Exact induction target

Combining `183` and (5), A1 follows if:

1. \(C_8^\ast\ge0\);
2. for every \(n\ge9\),
   \[
   C_8^\ast
   +
   {n(n+1)-72\over16}\Delta_8^\ast
   +
   {1\over2}
   \sum_{k=8}^{n-1}
   \left({n(n+1)\over k(k+1)}-1\right)
   F_k^{\rm diag}
   \ge0,
   \tag{10}
   \]
   with
   \[
   F_k^{\rm diag}
   =
   1+{3\over4}D_k^{\rm arch}
   +
   \int_0^\infty
   E(e^u)e^{-u}\mathcal K_k(u)\,du.
   \tag{11}
   \]

This is the current exact induction target in one-kernel form.

## Why the kernel does not give positivity by itself

The piecewise kernel \(\mathcal K_n\) is not sign-definite:

1. Laguerre polynomials \(L_{n-1}^{(2)}\) and \(L_n^{(2)}\) have positive
   zeros and alternating lobes;
2. the coefficients in (9) change the lobe weights but do not remove the
   oscillation;
3. \(E(e^u)=\psi(e^u)-e^u\) is also signed.

Therefore (5) does not close A1 by a positivity argument.  It packages the
entire diagonal forcing into a single signed pairing.

Any proof must show signed compensation between:

- the prime-error factor \(E(e^u)\);
- the piecewise Laguerre kernel \(\mathcal K_n\);
- the explicit archimedean term \(1+\frac34D_n^{\rm arch}\);
- the cumulative weights from (10).

## Status

Closed as a diagonal forcing normal form.  A1 remains open.

The live local induction theorem is a lower bound for the cumulative sums of
the one-kernel diagonal forcing (11).
