# E73.054 - FAR3 nodewise rational certificate

## 1. Purpose

E73.053 shows that the FAR3 tail cannot be certified by a global quotient maximum.

The surviving certificate is nodewise and rational: evaluate the finite Cauchy transform through
its exact divisor identity.

## 2. Rational form of each WCS term

From E73.038,

```text
C_x(t)=P_x(t)/D_x(t),
```

where

```text
D_x(t)=prod_n(t-d_n),
P_x(t)=sum_n xi_n prod_{m != n}(t-d_m).
```

For each critical height `gamma_k`, the WCS term is exactly

```text
T_k(A,L)
=
e^(alpha L)G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

This is a finite expression involving only:

```text
1. the off-line cluster A;
2. the finite CCM poles d_n;
3. the finite CCM vector xi_n;
4. the critical height gamma_k;
5. elementary products.
```

## 3. FAR3-nodewise certificate

Let `D_3(A,L)` be the top three FAR nodes from E73.052.

Choose nonnegative budgets:

```text
b_k(A,L)      for k in D_3(A,L),
c_k(A,L)      for k notin D_3(A,L),
```

such that

```text
sum_{k in D_3} b_k + sum_{k notin D_3} c_k <= L^B.
```

If the finite rational inequalities

```text
T_k(A,L) <= b_k(A,L)      for k in D_3(A,L),
T_k(A,L) <= c_k(A,L)      for k notin D_3(A,L)
```

hold for every critical node in the natural-height window, then `WCS(A,L)` holds.

## 4. Proof

Summing the nodewise inequalities gives:

```text
sum_k T_k(A,L)
<= sum_{k in D_3} b_k + sum_{k notin D_3} c_k
<= L^B.
```

This is `WCS(A,L)`.  E73.042 then gives:

```text
WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

## 5. Why this is not tautological

The certificate is allowed to evaluate `P_x` and `D_x`, because these are finite objects produced
by the CCM pole-even model.  The non-tautological part is:

```text
1. D_3 is selected by FAR score, not by T_k;
2. the rational values are certified by products P_x/D_x, not by a matrix inverse;
3. the tail is a positive finite sum with explicit per-node budgets.
```

This is the finite verifiable identity form requested by the Phase 72 route.

## 6. Uniform theorem remaining

The remaining analytic task is to produce budgets `b_k,c_k` uniformly in natural height:

```text
Uniform FAR3-nodewise:
There exist B,L0 and explicit budget rules such that for all L>=L0 and every natural-height
off-line cluster A, the FAR3-nodewise inequalities hold and the budgets sum to at most L^B.
```

E73.051 shows that the tail budgets can be extremely small in the tested windows, but E73.053 shows
they must remain nodewise rather than using a global quotient maximum.
