# Cutoff-transfer tail equivalence

## Purpose

`235_MOVING_CUTOFF_DERIVATIVE_GATE.md` computes the derivative of the
compact cutoff quantity:
\[
  C_n'(T)=-(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T).
\]

`236_SINGLE_TRANSFORM_ZERO_SIDE_MARGIN_AUDIT.md` records the infinite-cutoff
identity
\[
  C_n(T_n)=\lambda_n-{1\over4}\lambda_n^{\rm arch}-R_n(T_n).
\]

This note makes explicit that these are the same gate.  Transferring
positivity from any other cutoff to \(T_n\) is exactly a signed tail theorem
for the Laguerre--Chebyshev pairing.

## Transfer between two finite cutoffs

By `235`, for any \(0<U<V\),
\[
\boxed{
  C_n(V)-C_n(U)
  =
  -\int_U^V E(e^t)e^{-t}L_{n-1}^{(2)}(t)\,dt.
}
\tag{1}
\]

Therefore, if \(U<T_n\), the implication
\[
  C_n(U)\ge0 \quad\Longrightarrow\quad C_n(T_n)\ge0
\]
requires
\[
\boxed{
  \int_U^{T_n}E(e^t)e^{-t}L_{n-1}^{(2)}(t)\,dt
  \le C_n(U).
}
\tag{2}
\]

If \(U>T_n\), it requires
\[
\boxed{
  \int_{T_n}^{U}E(e^t)e^{-t}L_{n-1}^{(2)}(t)\,dt
  \ge -C_n(U).
}
\tag{3}
\]

Both are signed Laguerre--Chebyshev correlation theorems.

## Transfer from the infinite cutoff

Formally sending \(U\to\infty\), using the full Li generator identity from
`150`, gives
\[
\boxed{
  C_n(\infty)=\lambda_n-{1\over4}\lambda_n^{\rm arch}.
}
\tag{4}
\]

The tail from \(T_n\) to infinity is
\[
\boxed{
  R_n(T_n)
  =
  -\int_{T_n}^{\infty}E(e^t)e^{-t}L_{n-1}^{(2)}(t)\,dt.
}
\tag{5}
\]

Thus
\[
\boxed{
  C_n(T_n)=C_n(\infty)-R_n(T_n).
}
\tag{6}
\]

Consequently compact A1 is equivalent to
\[
\boxed{
  R_n(T_n)
  \le
  \lambda_n-{1\over4}\lambda_n^{\rm arch}.
}
\tag{7}
\]

This is exactly the one-sided tail gate of `150`.

## Why symmetric estimates cannot transfer positivity

A symmetric estimate such as
\[
  |R_n(T_n)|\le {1\over4}\lambda_n^{\rm arch}
\]
gives
\[
  C_n(T_n)
  \ge
  \lambda_n-{1\over2}\lambda_n^{\rm arch}.
\tag{8}
\]

Therefore it closes A1 only under the strong margin
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}.
\tag{9}
\]

Without (9), or without the one-sided inequality (7), the transfer from
the infinite cutoff to the compact cutoff is not justified.

Likewise, transferring from a finite fixed cutoff through (1) requires
the sign of the actual integral, not just an absolute PNT-size bound.
Absolute bounds return to the bulk obstructions already recorded in
`221`, `223`, `232`, and `235`.

## Status

Closed as a cutoff-transfer equivalence.

A1 remains open.  Cutoff transfer is exactly the one-sided tail/sign
correlation problem; it is not a separate monotonicity principle.
