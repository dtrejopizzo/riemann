# E73.292 - Loewner form of the kernel theorem

Date: 2026-07-14.

## 1. Purpose

E73.291 unified the closed-weight kernel with the Schur commutator row:

```text
sum_b eta_bK_b=qH_LR_wxi_L=-q[H_L,P_w]xi_L.
```

The rank-two Cauchy-plane expansion is exact but not admissible as a proof
source, by E73.266.  This note rewrites the kernel in the direction that
remains admissible: a Loewner divided-difference operator applied to the
closed Gamma-prime weight row.

## 2. Loewner operator

Let

```text
d_j=2*pi*n_j/L,
F_j=W^odd_j=W'_{d_j}-W'_{-d_j}.
```

Define the off-diagonal Loewner matrix

```text
Lambda_F(j,b)=
  (F_j-F_b)/(d_j-d_b),    j != b,
  0,                     j=b.
```

Since

```text
d_b-d_j = 2*pi(n_b-n_j)/L,
```

the off-diagonal part of `K-DIAGOFF` becomes

```text
sum_{j != b} r_j (F_j-F_b)/(2 i pi(n_b-n_j))
= -(1/(iL)) sum_j r_j Lambda_F(j,b).
```

Thus the kernel is

```text
K = r M_U - (1/(iL)) r Lambda_F,                 (L-K)
```

where

```text
M_U=diag(U^even_b).
```

Pairing with `eta=R_wxi_L` gives the exact endpoint

```text
r M_U eta - (1/(iL)) r Lambda_F eta = O_M(L^(-M)).
```

Call this `LOEWNER-KERNEL-DIV`.

## 3. Commutator interpretation

The Loewner matrix is the unique off-diagonal solution of

```text
[D,Lambda_F]_{jb}=F_j-F_b,       j != b,
```

where `D=diag(d_j)`.  Equivalently,

```text
[D,Lambda_F]=F 1^T - 1 F^T
```

off the diagonal.

Therefore the remaining scalar is not a generic Hilbert-transform bound.  It
is a paired commutator identity:

```text
r M_U eta - (1/(iL)) r Lambda_F eta.
```

The diagonal row `M_U` must be treated as the missing diagonal/derivative term
of the same Loewner calculus.  This is precisely the finite analogue of a
Fréchet derivative:

```text
off diagonal: divided difference of W^odd,
diagonal:     U^even.
```

## 4. The analytic lemma now needed

The next theorem should not estimate `Lambda_F` by norm.  That would lose the
same signed cancellation as earlier absolute-value routes.  The needed lemma is
directional:

```text
Directional Loewner Eigenline Cancellation.
For F=W^odd, U=U^even, r=q_a, eta=R_wxi_L,

| r( M_U-(1/(iL))Lambda_F )eta | <= A_M L^(-M)
```

uniformly over admissible rows/windows.

By E73.291, this is exactly the Schur-Commutator Eigenline Cancellation.

## 5. Why this is not the rejected rank-two route

Expanding `R_w=I-P_w` gives the exact two-dimensional identity

```text
qH_LR_wxi_L=(mu I-QH_LQ^*(QQ^*)^(-1))Qxi_L.
```

E73.266 rejects this as a proof source because it hides the theorem in
`Qxi_L`.  `LOEWNER-KERNEL-DIV` does not use `Qxi_L` as a small input.  It keeps
the full transverse vector

```text
eta=R_wxi_L
```

and exposes the operator acting on it:

```text
M_U-(1/(iL))Lambda_F.
```

This is the admissible analytic target.

## 6. Relation with earlier commutator work

E72.54 and E72.62 introduced Loewner commutators for CCM cells.  E73.292 is
not a repeat of those estimates.  It identifies the final closed-weight
Schur row itself as a Loewner derivative:

```text
K = r M_U - (1/(iL))r Lambda_{W^odd}.
```

This supplies the missing proof-facing normal form for the scalar WRL endpoint.

## 7. Status

```text
proved: KERNEL-FREQ-DIV has exact Loewner form LOEWNER-KERNEL-DIV;
rejected: rank-two Cauchy-plane expansion as proof source remains rejected;
new analytic target: directional Loewner eigenline cancellation.
```

## 8. Numerical certification

`E73_292_loewner_kernel_probe.py` checks the sign and the factor `1/(iL)`.
The vector identity is at roundoff:

```text
 lam     L gamma row relErr pairDirectB pairLoewB pairErrB
  12   4.970   14.13   0 3.8e-16      -20.89    -20.87   -22.91
  16   5.545   21.02   0 1.2e-15      -18.13    -18.16   -19.90
  20   5.991   21.02   1 2.4e-16      -17.90    -17.99   -18.97
```

The scalar pairing is much smaller than the row scale, so its displayed
agreement is sensitive to floating precision.  The certified object here is
the vector identity `K = rM_U-(1/(iL))r Lambda_F`, whose `relErr` is at
roundoff.
