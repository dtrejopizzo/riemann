# Quarter-margin plus nonpositive-tail gate

## Purpose

`244_A0_TAIL_IMPROVEMENT_REQUIREMENT.md` shows that compact A1 is exactly
the normalized comparison
\[
  \eta_n\ge d_n.
\]

This note isolates the simplest non-strong-margin special case: a quarter
Li margin together with a nonpositive signed tail.

## Exact decomposition

Let
\[
  A_n=\lambda_n^{\rm arch},
  \qquad
  Q_n=\lambda_n-\frac14A_n.
\]

The compact coefficient is
\[
\boxed{
  C_n(T_n)
  =
  \lambda_n-\frac14A_n-R_n(T_n)
  =
  Q_n-R_n(T_n).
}
\tag{1}
\]

Therefore the following two inequalities imply A1:
\[
\boxed{
  Q_n\ge0
  \qquad\hbox{and}\qquad
  R_n(T_n)\le0.
}
\tag{2}
\]

In original notation,
\[
\boxed{
  \lambda_n\ge\frac14\lambda_n^{\rm arch}
}
\tag{3}
\]
and
\[
\boxed{
  R_n(T_n)\le0.
}
\tag{4}
\]

Then \(C_n(T_n)\ge0\) follows immediately from (1).

## Normalized form

The deficit ratio of `244` is
\[
  d_n=\max\left(0,\frac12-{\lambda_n\over A_n}\right).
\]

The quarter margin (3) gives
\[
  d_n\le\frac14.
\tag{5}
\]

The nonpositive tail (4) gives
\[
  \eta_n
  =
  \frac14-{R_n(T_n)\over A_n}
  \ge\frac14.
\tag{6}
\]

Thus (5)--(6) imply
\[
  \eta_n\ge d_n,
\]
which is A1.

## Signed-tail integral version

Using
\[
  R_n(T_n)
  =
  -\int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du,
\]
condition (4) is exactly
\[
\boxed{
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge0.
}
\tag{7}
\]

So the quarter-margin route requires:

1. the arithmetic margin
   \[
     \lambda_n\ge\frac14A_n;
   \]
2. the one-sided signed Chebyshev--Laguerre tail sign
   \[
     \int_{T_n}^{\infty}
       E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du\ge0.
   \]

## Why A0 is insufficient for this route

A0 gives
\[
  R_n(T_n)\le\frac14A_n,
\]
or \(\eta_n\ge0\).  It does not imply \(R_n(T_n)\le0\).

Even under the quarter margin, A0 alone gives only
\[
  C_n(T_n)
  =
  Q_n-R_n(T_n)
  \ge
  -R_n(T_n),
\]
which can still be negative if \(0<R_n(T_n)\le A_n/4\).  Thus the required
tail input is genuinely one-sided, not absolute.

## Strength of the quarter margin

The quarter margin (3) implies
\[
  \lambda_n>0
\]
for every \(n\ge8\), because \(A_n>0\).  Together with the finite
\(1\le n\le7\) certificate, it implies all Li coefficients are positive and
therefore implies RH by Li's theorem.

Thus the quarter-margin route is still RH-strength.  It is weaker than the
strong margin
\[
  \lambda_n\ge\frac12A_n,
\]
but it is not a consequence of bare Euler--Gamma algebra or A0.

## Status

Closed as a sufficient special gate.

A1 remains open.  This route would close A1 if one proves both quarter
margin and nonpositive signed tail for all \(n\ge8\).  Neither statement is
currently supplied by A0, VK absolute estimates, or symmetric Chebyshev
envelopes.
