# Cutoff comparison and monotonicity gate

## Purpose

The moving-diagonal generator shows that A1 requires
\[
  C_n(T_n)\ge0
\]
at cutoffs \(T_n\) chosen by A0.  This note gives the exact comparison
between two cutoffs and isolates the monotonicity theorem that would be
needed to move from any auxiliary cutoff to \(T_n\).

The conclusion is negative but useful: there is no formal monotonicity in
the cutoff.  Any monotonicity must be a new signed theorem.

## Collapsed cutoff derivative

Recall
\[
  C_n(T)
  =
  -n-\int_0^T
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  +{3\over4}\lambda_n^{\rm arch}.
\tag{1}
\]

Therefore
\[
  \boxed{
  {d\over dT}C_n(T)
  =
  -E(e^T)e^{-T}L_{n-1}^{(2)}(T).
  }
\tag{2}
\]

For any \(0\le S<T\),
\[
  \boxed{
  C_n(T)-C_n(S)
  =
  -\int_S^T
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
  }
\tag{3}
\]

This is the collapsed form of the boundary-current flow in
`127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md`.

## Lobe comparison

Let
\[
  0<\tau_{n,1}<\cdots<\tau_{n,n-1}
\]
be the zeros of \(L_{n-1}^{(2)}\).  On each interval between consecutive
zeros, the sign of \(L_{n-1}^{(2)}\) is constant and alternates.

Thus if \(S<T\), the flow (3) decomposes as
\[
  C_n(T)-C_n(S)
  =
  -\sum_j
  \int_{[S,T]\cap I_{n,j}}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{4}
\]

The sign of each summand depends both on the Chebyshev error \(E(e^u)\) and
on the Laguerre lobe.  Neither factor has a fixed sign on the whole compact
range.

## Monotonicity gate

A cutoff-transfer proof of A1 would have the following shape.

Find auxiliary cutoffs \(S_n\) for which
\[
  C_n(S_n)\ge M_n\ge0
\tag{5}
\]
is proved by a fixed-cutoff, finite-certificate, or local argument, and then
prove the one-sided flow bound
\[
  C_n(T_n)-C_n(S_n)\ge -M_n.
\tag{6}
\]

By (3), the second condition is
\[
  \boxed{
  \int_{S_n}^{T_n}
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \le M_n.
  }
\tag{7}
\]

This is the exact monotonicity/transfer theorem required to move positivity
to the A0 cutoff.

## Why global monotonicity is false as a formal principle

Equation (2) shows that formal monotonicity would require
\[
  -E(e^T)L_{n-1}^{(2)}(T)\ge0
\]
for all relevant \(T\).  This cannot be a structural identity:

1. \(L_{n-1}^{(2)}\) has \(n-1\) simple positive zeros and alternates sign;
2. \(E(e^T)=\psi(e^T)-e^T\) has jumps at prime powers and no fixed sign
   forced by the Euler product;
3. A PNT estimate bounds \(|E|\), not its phase relative to the Laguerre
   lobes.

Thus no proof may move a cutoff merely by saying the compact core improves
with \(T\).  The transfer must be a signed lobe theorem.

## Relation to previous normal forms

The cutoff comparison is equivalent to:

- the moving-flow density in `127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md`;
- the moving diagonal coefficient condition in
  `149_MOVING_DIAGONAL_A1_GENERATOR.md`;
- the tail identity
  \(C_n(T)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T)\) in
  `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`;
- the lobe compensation theorem in `144_LAGUERRE_CORE_SIGN_PARTITION.md`;
- the dual balance theorem in `145_LAGUERRE_LOBE_DUAL_BALANCE.md`.

The present note pins down the exact missing statement for any proof that
tries to prove A1 at one cutoff and transfer it to another.

## Status

Closed as a cutoff-comparison normal form.  A1 remains open.

The new live theorem is the signed cutoff-transfer inequality (7).  It is
not supplied by A0 or by ordinary PNT bounds.
