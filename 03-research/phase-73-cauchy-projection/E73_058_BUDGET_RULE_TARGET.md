# E73.058 - Budget rule target

## 1. Purpose

E73.056 gives a finite certificate schema.  E73.057 suggests concrete budget exponents.

This document states the current sharp uniform theorem in budget form.

## 2. Definitions

For a natural-height off-line cluster `A=(a,m)`, define

```text
T_k(A,L)=
e^(alpha L)G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

Let `D_3(A,L)` be the top three FAR nodes.

Define:

```text
Main_3(A,L) := sum_{k in D_3(A,L)} T_k(A,L),
Tail_3(A,L) := sum_{k notin D_3(A,L)} T_k(A,L).
```

## 3. Candidate uniform budget

The candidate theorem is:

```text
BUD-5/9:
There exist constants C_main,C_tail and L0 such that for every L>=L0 and every natural-height
off-line cluster A,

Main_3(A,L) <= C_main L^(-5),
Tail_3(A,L) <= C_tail L^(-9).
```

Then:

```text
WCS(A,L) <= C_main L^(-5)+C_tail L^(-9).
```

In particular, for any fixed `B>=0` and large enough `L`,

```text
WCS(A,L) <= L^B.
```

The Phase 73 gate only needs polynomial boundedness, so this budget is far stronger than required.

## 4. Proof of sufficiency

Assume `BUD-5/9`.  Then:

```text
sum_k T_k
= Main_3 + Tail_3
<= C_main L^(-5)+C_tail L^(-9).
```

For `L>=L1(C_main,C_tail,B)`,

```text
C_main L^(-5)+C_tail L^(-9) <= L^B.
```

Thus `WCS` holds.  By E73.042:

```text
WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

## 5. What must be proved

The remaining analytic work is now split into two estimates:

```text
MAIN:
the three FAR-selected rational nodes have total contribution O(L^-5);

TAIL:
all remaining FAR-protected nodes have total contribution O(L^-9).
```

Both estimates are finite rational inequalities built from `P_x/D_x`.

## 6. Why this is useful

The previous endpoint was:

```text
prove WCS.
```

The new endpoint is sharper:

```text
prove BUD-5/9 for FAR3 main and tail.
```

This separates the dangerous finite nodes from the protected tail and supplies explicit exponents
with slack from numerical evidence.
