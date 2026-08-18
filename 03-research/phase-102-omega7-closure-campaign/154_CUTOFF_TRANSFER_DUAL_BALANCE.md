# Cutoff transfer dual balance

## Purpose

`153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md` gives the raw cutoff
transfer
\[
  C_n(T)-C_n(S)
  =
  -\int_S^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\]
This note integrates that transfer once, so the moving-cutoff gate is stated
in terms of accumulated prime-pole balance on \([S,T]\).

## Local balance between two cutoffs

For \(S\le u\le T\), define
\[
  B_S(u)=\int_S^u E(e^v)\,dv.
\tag{1}
\]

Then
\[
  B_S(S)=0
\]
and
\[
  B_S(T)
  =
  \int_S^T(\psi(e^v)-e^v)\,dv.
\tag{2}
\]

The finite arithmetic formula is
\[
\boxed{
\begin{aligned}
  B_S(u)
  &=
  (u-S)\psi(e^S)
  +
  \sum_{e^S<m\le e^u}\Lambda(m)(u-\log m)
  -
  e^u+e^S .
\end{aligned}
}
\tag{3}
\]

This is exact and finite.

## Dual transfer identity

Let
\[
  \Phi_n(u)=e^{-u}L_{n-1}^{(2)}(u).
\tag{4}
\]

The cutoff transfer is
\[
  C_n(T)-C_n(S)
  =
  -\int_S^T E(e^u)\Phi_n(u)\,du.
\tag{5}
\]

Since \(B_S'(u)=E(e^u)\), integration by parts gives
\[
\boxed{
  C_n(T)-C_n(S)
  =
  -B_S(T)\Phi_n(T)
  +
  \int_S^T B_S(u)\Phi_n'(u)\,du.
}
\tag{6}
\]

Using the raising identity
\[
  \Phi_n'(u)=-e^{-u}L_{n-1}^{(3)}(u),
\tag{7}
\]
this becomes
\[
\boxed{
  C_n(T)-C_n(S)
  =
  -B_S(T)e^{-T}L_{n-1}^{(2)}(T)
  -
  \int_S^T B_S(u)e^{-u}L_{n-1}^{(3)}(u)\,du.
}
\tag{8}
\]

This is the cutoff-transfer analogue of the raised hierarchy in `146`.

## Transfer theorem in dual form

Suppose an auxiliary cutoff \(S_n\) gives a margin
\[
  C_n(S_n)\ge M_n\ge0.
\tag{9}
\]

Then A1 at \(T_n\) follows if
\[
  C_n(T_n)-C_n(S_n)\ge -M_n.
\tag{10}
\]

By (8), the exact required dual inequality is
\[
\boxed{
  B_{S_n}(T_n)e^{-T_n}L_{n-1}^{(2)}(T_n)
  +
  \int_{S_n}^{T_n}B_{S_n}(u)e^{-u}L_{n-1}^{(3)}(u)\,du
  \le M_n.
}
\tag{11}
\]

This is the signed accumulated-balance theorem needed for cutoff transfer.

## Why this is sharper than an absolute flow estimate

An absolute estimate would replace \(B_S\) by \(|B_S|\) or \(E\) by \(|E|\).
That discards the only possible cancellation between:

1. the local prime-power accumulation in (3);
2. the endpoint term \(B_S(T)\Phi_n(T)\);
3. the raised Laguerre kernel \(L_{n-1}^{(3)}\).

Thus the dual transfer identity does not make the problem easier by itself.
It identifies the exact accumulated signed quantity that a transfer proof
must control.

## Status

Closed as a dual cutoff-transfer normal form.  A1 remains open.

The missing theorem is the signed accumulated transfer inequality (11), or a
stronger global positivity theorem implying it for all \(n\ge8\).
