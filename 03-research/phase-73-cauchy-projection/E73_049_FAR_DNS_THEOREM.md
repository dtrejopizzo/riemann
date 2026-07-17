# E73.049 - FAR-DNS theorem target

## 1. Purpose

E73.048 identifies a viable non-tautological arithmetic selector for dominant WCS nodes.

The selector uses the finite Cauchy divisor of `P_x`, but it does not use the final WCS term
`T_k`.

## 2. Definitions

Let

```text
C_x(t)=P_x(t)/D_x(t)
```

be the finite Cauchy transform from E73.038.

For a critical height `gamma_k`, define

```text
R_k := dist(-gamma_k, Div(P_x)).
```

For an off-line cluster `A=(a,m)`, define the geometric-mesh weight

```text
W_k(A,L)
:=
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|.
```

The FAR selector score is

```text
F_k(A,L) := W_k(A,L) R_k.
```

For a fixed integer `r`, define

```text
D_r(A,L) := the r critical indices with largest F_k(A,L).
```

This set is admissible: it uses the finite divisor `Div(P_x)`, but not the final value
`|C_x(i gamma_k)|`.

## 3. FAR-DNS statement

The finite FAR-DNS certificate consists of:

```text
FAR-main:
sum_{k in D_r(A,L)}
W_k(A,L)|C_x(i gamma_k)|
<= (1-epsilon)L^B,
```

and

```text
FAR-tail:
sum_{k notin D_r(A,L)}
W_k(A,L)|C_x(i gamma_k)|
<= epsilon L^B.
```

Then `WCS(A,L)` holds.

## 4. Proof

The WCS sum decomposes over the disjoint partition:

```text
sum_k W_k|C_x(i gamma_k)|
= sum_{k in D_r} W_k|C_x(i gamma_k)|
 + sum_{k notin D_r} W_k|C_x(i gamma_k)|.
```

Applying `FAR-main` and `FAR-tail` gives

```text
WCS(A,L) <= L^B.
```

By E73.042,

```text
WCS => PFD => DATA-HERM => CC-PROJ => NAT-PROJ => scalar WRL.
```

Thus

```text
FAR-DNS => scalar WRL.
```

## 5. Why `far` is the correct arithmetic direction

The finite divisor identity gives:

```text
C_x(t)=P_x(t)/D_x(t).
```

Near `Div(P_x)`, the numerator suppresses `C_x`.  Therefore dangerous critical nodes are expected
where the critical height is not protected by a nearby numerator zero.  E73.048 confirms this
mechanism numerically.

This is the opposite of the earlier root-covering attempt:

```text
root-covering proves smallness near roots;
FAR-DNS identifies the finitely many nodes not protected by roots.
```

## 6. Uniform theorem still needed

The remaining theorem is:

```text
Uniform FAR-DNS:
There exist B, epsilon, r, and L0 such that for all L>=L0 and every natural-height off-line
cluster A, FAR-main and FAR-tail hold.
```

The tested windows support `r=3`, but the proof must derive `r` from the spacing of the critical
mesh and the finite Cauchy divisor.

## 7. Finite identity form

For fixed `L`, `A`, and `r`, FAR-DNS is completely finite:

```text
1. compute Div(P_x) from the finite CCM pole-even vector;
2. rank critical heights by F_k=W_k dist(-gamma_k,Div(P_x));
3. certify FAR-main on the top r nodes;
4. certify FAR-tail on the remaining nodes.
```

No infinite zero input and no Cauchy matrix inverse remains.
