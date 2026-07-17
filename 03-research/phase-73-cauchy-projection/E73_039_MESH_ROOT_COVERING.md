# E73.039 - Mesh-root covering theorem

## 1. Purpose

E73.036 reduces the endpoint to the positive factor budget `PFD`.
E73.037 removes the Hermite inverse.
E73.038 factors the finite Cauchy transform through its finite divisor.

This document gives the next analytic reduction: `PFD` follows from a mesh-root covering estimate.

## 2. Local divisor bound

Let

```text
C_x(t)=P_x(t)/D_x(t)
```

and let `rho` be a simple zero of `P_x`.  On an interval `I` containing `rho` and no pole `d_n`,
write

```text
P_x(t)=(t-rho)P_{x,rho}(t).
```

Then for `t in I`,

```text
|C_x(t)| <= S_x(I,rho)|t-rho|,
```

where the explicit local slope envelope is

```text
S_x(I,rho)
:= sup_{t in I} |P_{x,rho}(t)/D_x(t)|.
```

This is exact finite algebra.  No zeros of `Xi` are used.

## 3. Critical covering

Let each critical height `gamma_k` in the natural-height window be assigned either:

```text
1. a finite Cauchy root rho(k), with gamma_k in I_k;
2. or no root, in which case use the trivial bound for |C_x(gamma_k)|.
```

Define the local root defect

```text
R_k := S_x(I_k,rho(k)) |gamma_k-rho(k)|
```

when a root is assigned, and otherwise

```text
R_k := |C_x(gamma_k)|.
```

Then always

```text
|C_x(gamma_k)| <= R_k.
```

## 4. Mesh-root covering estimate

For an off-line Hermite cluster `A` centered at `a=alpha+i tau`, define

```text
W_A(k) := G_theta,m(a,i gamma_k)
```

from E73.037 and

```text
M_k := |1-exp(i gamma_k L)|.
```

Assume the finite covering estimate

```text
MRC(A,L):
e^(alpha L) sum_{gamma_k in K_L} W_A(k) M_k R_k <= L^B.
```

Then `PFD(A,L)` holds.

## 5. Proof

By the local divisor bound,

```text
|C_x(gamma_k)| <= R_k
```

for every critical node.  Hence

```text
e^(alpha L) sum_k W_A(k)M_k|C_x(gamma_k)|
<=
e^(alpha L) sum_k W_A(k)M_kR_k.
```

The right-hand side is at most `L^B` by `MRC(A,L)`.  This is exactly `PFD(A,L)`.

Combining earlier steps,

```text
MRC => PFD => DATA-HERM => NAT-PROJ => scalar WRL.
```

## 6. Interpretation

The remaining problem has become a covering statement:

```text
Every critical height that has large Hermite coupling to a hypothetical off-line cluster must be
covered by either

1. mesh smallness: |1-exp(i gamma L)| is small;
2. divisor smallness: gamma is close to a finite Cauchy root;
3. or both.
```

This is sharper than the earlier `FINROOT/MESH` language because it supplies the exact local
constant `S_x(I,rho)` and a finite sufficient inequality.

## 7. Endpoint

The current minimal analytic theorem is:

```text
Uniform MRC:
There exist B and L0 such that for every L>=L0 and every natural-height off-line Hermite cluster A,
the mesh-root covering estimate MRC(A,L) holds.
```

This theorem is stronger than needed but is now positive, scalar, finite, and completely explicit.
