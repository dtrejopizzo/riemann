# E73.060 - CMAIN target

## 1. Purpose

E73.059 shows that `Main_3=O(L^-5)` should be proved by a product of:

```text
1. a geometric prefactor upper bound;
2. a finite Cauchy rational smallness bound.
```

This document states the next analytic target.

## 2. FAR3 main nodes

Let `D_3(A,L)` be the top three FAR nodes.

For `k in D_3(A,L)`, define:

```text
Pref_k(A,L)
:=
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|,
```

and

```text
C_k(L):=|C_x(-gamma_k)|=|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

Then:

```text
T_k=Pref_k C_k.
```

## 3. Sufficient theorem for MAIN

Assume:

```text
PREF-5:
Pref_k(A,L) <= C_pref L^5
for every k in D_3(A,L),
```

and

```text
CMAIN-10:
C_k(L) <= C_cauchy L^-10
for every k in D_3(A,L).
```

Then:

```text
Main_3(A,L) <= 3 C_pref C_cauchy L^-5.
```

## 4. Proof

For every `k in D_3`,

```text
T_k=Pref_k C_k
<= C_pref L^5 * C_cauchy L^-10
= C_pref C_cauchy L^-5.
```

Summing the three nodes:

```text
Main_3 <= 3 C_pref C_cauchy L^-5.
```

This is the `MAIN` half of `BUD-5/9`.

## 5. Interpretation

`PREF-5` is geometric and should follow from the explicit Taylor-Cauchy Hermite bound.

`CMAIN-10` is the arithmetic divisibility statement:

```text
|P_x(-gamma_k)|/|D_x(-gamma_k)| <= C L^-10
```

on the three FAR-selected critical heights.

This is now the main load-bearing estimate.

## 6. Remaining after CMAIN

To finish `BUD-5/9`, one still needs the tail half:

```text
Tail_3(A,L) <= C_tail L^-9.
```

But E73.051 and E73.057 show the tail has much more room than the main term in tested windows.
