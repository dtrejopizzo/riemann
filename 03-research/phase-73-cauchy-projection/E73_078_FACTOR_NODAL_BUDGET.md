# E73.078 - Factor nodal budget

## 1. Purpose

E73.075 proves exact complete-mesh pair divisibility:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

This note rewrites the remaining FAR3 nodal budget using that factorization.

## 2. Coefficients

The exact coefficients are:

```text
A_L(z,w)
= i[(e^(wL)-1)+e^(zL)(e^(-wL)-1)]/(w-z),
```

and

```text
B_L(z,w)
= -i[e^(zL)(e^(wL)-1)+(e^(-wL)-1)]/(w+z).
```

For fixed shifted windows away from collisions `w=+-z`, these coefficients are explicit elementary
functions.

## 3. Complete-mesh factor budget

Let `Z_T` be the finite paired zero-node window and let `z_k=i gamma_k` be the FAR3 evaluation nodes.
Define

```text
CoeffBudget_k
:= sum_{w in Z_T/+-}
   ( |A_L(z_k,w)||H_0(w)| + |B_L(z_k,w)||H_0(-w)| ).
```

Then by E73.075,

```text
sum_{w in Z_T/+-}|Pair_{z_k}^infty(w)|
<= CoeffBudget_k.                                    (1)
```

Thus the complete-mesh part of `FAR3-NODAL-BUDGET` follows from:

```text
FACTOR-MAIN-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L) CoeffBudget_k
<= C L^-5.                                           (2)
```

## 4. Tail part

E73.076 imports E72.391--E72.392:

```text
Tail_z = TailOperator_z({G_x(w)}).
```

Therefore the tail contribution is controlled by:

```text
TAIL-NODAL-5:
sum_{gamma_k in FAR3(A,L)}
W_k(A,L)|TailOperator_{z_k}({G_x(w)})|
<= C L^-5.                                           (3)
```

At polynomial active cutoff `M>=L^(1+epsilon)`, E72.392 shows this is lower order relative to the
same nodal vector budget.

## 5. Updated sufficient theorem

The current fully factored endpoint is:

```text
FACTOR-MAIN-5 + TAIL-NODAL-5 + Tail_3<=C_tail L^-9
=> BUD-5/9
=> WCS
=> scalar WRL.
```

All terms in `FACTOR-MAIN-5` are finite and explicit:

```text
finite nodes w,
finite poles d_n,
finite eigenline xi_n,
elementary coefficients A_L,B_L,
Cauchy divisor values H_0(+-w).
```

## 6. Meaning

The remaining difficulty has been localized to producing uniform bounds for the finite Cauchy
divisor values:

```text
H_0(w), H_0(-w)
```

on the selected zero-node window, with explicit coefficient weights.

This is a sharper version of the old `FAR3-NODAL-BUDGET`: the complete-mesh Mellin spectral
divisibility has been proved, so the only nodal smallness left is the Cauchy divisor itself and the
absorbed finite tail.

## 7. Status

```text
proved: exact complete-mesh factorization;
reduced: complete-mesh FAR3 budget to FACTOR-MAIN-5;
open: prove FACTOR-MAIN-5 and TAIL-NODAL-5 uniformly.
```
