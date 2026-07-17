# E74.18 - Schur-transfer invariants and compression criterion

Date: 2026-07-16.

## Exact reduction

Set

```text
G=QQ*,
A=QHQ*,
K=mu G-A,
T=K G^(-1).
```

Then

```text
det(T)=det(K)/det(G),
T^(-1)=G K^(-1).
```

Although `T` need not be Hermitian in Euclidean coordinates, it is similar
to the Hermitian matrix

```text
mu I-G^(-1/2) A G^(-1/2).
```

Consequently its invertibility is governed by the generalized compression
of `H` to `Row(Q)`.

## Compression criterion

Suppose uniformly for admissible windows that

```text
G^(-1/2) A G^(-1/2) >= c L I_2,
|mu| <= (c/2)L,
kappa(G) <= L^B.
```

Then

```text
||T^(-1)|| <= C L^(B-1),
||T|| <= L^C
```

provided the corresponding polynomial upper bound for the compression holds.
Thus E74.17's polynomial-conditioning hypothesis reduces to a two-dimensional
compression estimate and polynomial conditioning of the Cauchy Gram matrix.

## Probe result

`E74_018_transfer_invariants_probe.py` computes the basis-independent
compression eigenvalues.  Once the Fourier mesh reaches the critical height,

```text
mu/L       approximately 0,
spec(G^(-1/2) A G^(-1/2))/L approximately [0.97,1.02],
spec(T/L)  approximately [-1.02,-0.97].
```

The small-window failures occur when the critical height is outside or near
the edge of the truncated pole mesh.  They are truncation failures, not an
asymptotic singular direction of `T`.

## Proof obligation and circularity warning

The remaining transfer theorem is:

```text
CAUCHY-COMP:
cL QQ* <= QHQ* <= CL QQ*
```

on the admissible critical planes, together with polynomial Gram bounds and
`|mu|=o(L)`.  A proof of `CAUCHY-COMP` cannot invoke global positivity of the
Weil form or an equivalent zero-free theorem.  It must use the explicit
two-row Gamma-prime/cell calculation.  This is the next audit boundary.

## Status

```text
proved: determinant, inverse, similarity, and conditional compression lemma;
supported numerically: T/L -> -I on resolved critical windows;
open: non-circular CAUCHY-COMP, Gram bounds, and a uniform truncation regime.
```
