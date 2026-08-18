# Single-transform A1 frontier

## Purpose

`229_SMALL_T7_DIRECT_COEFFICIENT_REDUCTION.md` isolates the moving
arithmetic content of the telescoped signed route in the transform
\[
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m).
\]

This note writes the equivalent A1 frontier directly in those coordinates.
It reconciles the telescoped route with the original compact core of
`111_A1_SIGNED_CORE_REDUCTION.md` and the Mellin normal form of `113`.

## The moving transform

For \(n\ge8\) and \(T>0\), define
\[
\boxed{
  S_n(T)
  =
  \sum_{m\le e^T}{\Lambda(m)\over m}
  L_{n-1}^{(1)}(\log m).
}
\tag{1}
\]

Also put
\[
  X=e^T,\qquad E(X)=\psi(X)-X.
\tag{2}
\]

The compact A1 quantity from `111` is
\[
  C_n(T)
  =
  -n
  +
  E(X)X^{-1}L_{n-1}^{(1)}(T)
  -
  S_n(T)
  +
  \int_0^T L_{n-1}^{(1)}(u)\,du
  +
  {3\over4}\lambda_n^{\rm arch}.
\tag{3}
\]

Thus A1 at the moving cutoff \(T=T_n\) is exactly \(C_n(T_n)\ge0\).

## Explicit continuous counterpart

Use
\[
  {d\over du}L_n^{(0)}(u)=-L_{n-1}^{(1)}(u)
\tag{4}
\]
and \(L_n^{(0)}(0)=1\).  Then
\[
\boxed{
  \int_0^T L_{n-1}^{(1)}(u)\,du
  =
  1-L_n^{(0)}(T).
}
\tag{5}
\]

Substituting (5) into (3), A1 is equivalent to
\[
\boxed{
  S_n(T_n)
  \le
  E(e^{T_n})e^{-T_n}L_{n-1}^{(1)}(T_n)
  +
  1-L_n^{(0)}(T_n)
  +
  {3\over4}\lambda_n^{\rm arch}
  -
  n.
}
\tag{6}
\]

This is the single-transform frontier.

## Relation to the telescoped certificates

The route through `219`--`229` does not create a different theorem.  It
removes several misleading sufficient conditions and shows that all
absolute VK-size routes lose the Laguerre bulk.  After those reductions,
the moving arithmetic difficulty is again (6).

In particular:

1. `226` gives finite coefficients \(\Omega_n(m)\);
2. `227` removes the empty \(\log m<T_7\) block;
3. `228` isolates the high-block correlation;
4. `229` compresses the moving part to \(S_n(T_n)\);
5. (6) is the same signed compact A1 inequality in one-transform form.

## Why this is not closed by known size estimates

The kernel \(L_{n-1}^{(1)}(u)\) oscillates on the relevant range, so
\(S_n(T_n)\) is not controlled by positivity of \(\Lambda(m)\) alone.
Replacing the prime powers by a two-sided PNT envelope destroys the signed
correlation and returns to the bulk obstructions of `221` and `223`.

Therefore the remaining theorem is not a size bound.  It is the signed
sampling inequality (6) for every \(n\ge8\), at the moving cutoffs \(T_n\).

## Status

Closed as the single-transform frontier for A1.

A1 remains open.  The exact missing theorem is (6), or an equivalent
one-sided tail, strong-margin, comparative, or global theorem.
