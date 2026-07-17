# E73.052 - FAR3 tail certificate

## 1. Purpose

E73.048 identified FAR-DNS.
E73.050 showed that top-3 FAR selection is stable as the critical window grows.
E73.051 quantified the top-3 tail.

This document states the current finite certificate form.

## 2. FAR3 definitions

Let

```text
F_k(A,L)=
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|
dist(-gamma_k,Div(P_x)).
```

Let

```text
D_3(A,L)
```

be the three critical indices with largest `F_k(A,L)`.

The WCS term is

```text
T_k(A,L)=
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|
|C_x(i gamma_k)|.
```

## 3. FAR3 certificate

It is enough to prove:

```text
FAR3-main:
sum_{k in D_3(A,L)} T_k(A,L) <= (1-epsilon_L)L^B,
```

and

```text
FAR3-tail:
sum_{k notin D_3(A,L)} T_k(A,L) <= epsilon_L L^B.
```

Then `WCS(A,L)` holds.

## 4. Proof

The proof is the disjoint decomposition:

```text
sum_k T_k
= sum_{k in D_3} T_k + sum_{k notin D_3} T_k.
```

The two assumptions give:

```text
sum_k T_k <= L^B.
```

This is `WCS`, hence by E73.042:

```text
FAR3-main + FAR3-tail
=> WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

## 5. Finite identity form

For fixed `L` and `A`, FAR3 is fully finite:

```text
1. build P_x and compute Div(P_x);
2. compute F_k for the critical window;
3. select D_3;
4. certify the three main terms T_k;
5. certify the positive tail.
```

No off-line zero input and no Cauchy matrix inverse enter this certificate.

## 6. Uniform theorem remaining

The remaining uniform analytic theorem is:

```text
Uniform FAR3:
There exist B, L0, and an explicit epsilon_L<1 such that for every L>=L0 and every natural-height
off-line cluster A, FAR3-main and FAR3-tail hold.
```

E73.051 suggests that `epsilon_L` can be small and decreasing, but the proof must derive it from
the spacing of the critical mesh and the finite divisor `Div(P_x)`.
