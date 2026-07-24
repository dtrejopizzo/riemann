# Tail-surplus generator diagonal no-go

## Purpose

`238_TAIL_MARGIN_COMPENSATION_FRONTIER.md` introduces
\[
  M_n=\lambda_n-{1\over2}A_n,
  \qquad
  \delta_n={1\over4}A_n-R_n(T_n),
  \qquad
  A_n=\lambda_n^{\rm arch},
\]
and proves the exact compact identity
\[
  C_n(T_n)=M_n+\delta_n.
\]

`239_MARGIN_TAIL_THRESHOLD_LADDER.md` calibrates this as
\(\kappa_n-\rho_n\ge1/4\).  This note packages the same frontier in
generating-function form and records the precise obstruction to a proof
based only on isolated nonnegativity of the tail surplus.

## Fixed-cutoff surplus generator

Let
\[
  \mathcal A(z)=\sum_{n\ge1}A_nz^n,\qquad
  \mathcal L(z)=\sum_{n\ge1}\lambda_nz^n.
\]

For fixed \(T\), recall from `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`
that
\[
  \mathcal R_T(z)
  =
  -{z\over(1-z)^3}
  \int_T^\infty E(e^u)
  \exp\!\left(-{u\over1-z}\right)\,du
\]
has coefficients
\[
  [z^n]\mathcal R_T(z)=R_n(T)
  =
  -\int_T^\infty
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du .
\]

Define the fixed-cutoff tail surplus transform
\[
\boxed{
  \Delta_T(z)
  :=
  {1\over4}\mathcal A(z)-\mathcal R_T(z).
}
\tag{1}
\]

Then
\[
\boxed{
  \Delta_T(z)
  =
  {1\over4}\mathcal A(z)
  +
  {z\over(1-z)^3}
  \int_T^\infty E(e^u)
  \exp\!\left(-{u\over1-z}\right)\,du .
}
\tag{2}
\]

Coefficientwise,
\[
\boxed{
  [z^n]\Delta_T(z)
  =
  {1\over4}A_n-R_n(T)
  =:\delta_n(T).
}
\tag{3}
\]

In particular, the actual A0 diagonal surplus is
\[
\boxed{
  \delta_n=\delta_n(T_n)=[z^n]\Delta_{T_n}(z).
}
\tag{4}
\]

## Derivative form

Between prime-power jumps, differentiating (2) with respect to the cutoff
gives
\[
\boxed{
  {\partial\over\partial T}\Delta_T(z)
  =
  -{z\over(1-z)^3}E(e^T)
  \exp\!\left(-{T\over1-z}\right).
}
\tag{5}
\]

Taking coefficients gives
\[
\boxed{
  {d\over dT}\delta_n(T)
  =
  -E(e^T)e^{-T}L_{n-1}^{(2)}(T).
}
\tag{6}
\]

Thus the surplus flow is exactly the moving-cutoff transfer current already
identified in `235_MOVING_CUTOFF_DERIVATIVE_GATE.md` and
`237_CUTOFF_TRANSFER_TAIL_EQUIVALENCE.md`.

## Collapse with the strong-margin generator

Let the strong-margin transform be
\[
\boxed{
  \mathcal M(z)=\mathcal L(z)-{1\over2}\mathcal A(z).
}
\tag{7}
\]

Then, for every fixed \(T\),
\[
\begin{aligned}
  \mathcal M(z)+\Delta_T(z)
  &=
  \mathcal L(z)-{1\over2}\mathcal A(z)
  +{1\over4}\mathcal A(z)-\mathcal R_T(z)\\
  &=
  \mathcal L(z)-{1\over4}\mathcal A(z)-\mathcal R_T(z).
\end{aligned}
\]

By `150`, the right side is the compact fixed-cutoff generator
\[
\boxed{
  \mathcal C_T(z)
  =
  \mathcal L(z)-{1\over4}\mathcal A(z)-\mathcal R_T(z).
}
\tag{8}
\]

Therefore
\[
\boxed{
  \mathcal M+\Delta_T=\mathcal C_T.
}
\tag{9}
\]

On the moving diagonal this becomes
\[
\boxed{
  [z^n]\bigl(\mathcal M+\Delta_{T_n}\bigr)
  =
  M_n+\delta_n
  =
  C_n(T_n).
}
\tag{10}
\]

Consequently compact A1 is exactly
\[
\boxed{
  [z^n]\bigl(\mathcal M+\Delta_{T_n}\bigr)\ge0
  \qquad(n\ge8).
}
\tag{11}
\]

## Exact no-go for isolated surplus positivity

A0 gives
\[
  \delta_n=[z^n]\Delta_{T_n}\ge0.
\tag{12}
\]

However, (10) shows that isolated surplus positivity is insufficient unless
it is compared against the strong-margin coefficient \(M_n\).  The required
statement is not merely
\[
  [z^n]\Delta_{T_n}\ge0,
\]
but rather the sharp comparative inequality
\[
\boxed{
  [z^n]\Delta_{T_n}
  \ge
  -[z^n]\mathcal M
  =
  -M_n.
}
\tag{13}
\]

Equivalently,
\[
\boxed{
  \delta_n\ge -M_n.
}
\tag{14}
\]

The logical obstruction is exact.  From the two facts
\[
  \lambda_n\ge0,\qquad \delta_n\ge0,
\]
one only obtains
\[
  M_n=\lambda_n-{1\over2}A_n\ge-{1\over2}A_n,
\]
which allows the model values
\[
  M_n=-{1\over2}A_n,\qquad \delta_n=0.
\]
These values satisfy Li nonnegativity and A0 surplus nonnegativity but give
\[
  M_n+\delta_n<0.
\]

Thus no proof whose final input is only Li nonnegativity plus
\(\delta_n\ge0\) can close A1.  It must prove the comparative diagonal
inequality (13), strong margin \(M_n\ge0\), or an equivalent compact
positivity theorem.

## Status

Closed as the tail-surplus generator and diagonal no-go.

A1 remains open.  The missing theorem is the comparative coefficient bound
\[
  [z^n]\Delta_{T_n}\ge -[z^n]\mathcal M
\]
or a direct proof of
\[
  [z^n](\mathcal M+\Delta_{T_n})\ge0.
\]
