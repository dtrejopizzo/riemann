# Point 08 - Sign preservation

## Problem

The lower bound needed for Li is one-sided:
\[
  \lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]
Replacing the paired integral by its absolute value loses the oscillatory
information of the Laguerre kernel and does not detect the mechanism that
would rule out an off-line zero.

## Exact surviving signed object

After A0, the sign-preserving object is
\[
  {\rm Core}(n)
  =
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy .
\]
Equivalently, in Stieltjes form,
\[
  {\rm Core}(n)
  =
  \int_1^{e^{T_n}} f_{n,0}(y)\,d(y-\psi(y))
  +
  {\rm Edge}(n,T_n),
\]
where the edge term is explicit after integration by parts. This form keeps
Lebesgue mass, prime powers and the boundary in one expression.

## Open theorem

Point 08 closes exactly when one proves
\[
  {\rm Core}(n)\ge -{3\over4}\lambda_n^{\rm arch}
  \qquad(n\ge8)
\]
by a decomposition that does not first estimate
\[
  \int |E(y)|\,|f'_{n,0}(y)|\,dy .
\]

No local prime shell is currently known to have this property. The minimal
unit is global in \(y\) for the fixed index \(n\).

## Status

Open. The phase has isolated the correct signed object and removed the far
tail, but it has not discovered a positive local unit or a global variational
identity proving the core inequality.
