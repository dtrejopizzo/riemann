# E73.056 - Finite certificate schema

## 1. Purpose

E73.055 gives an executable finite certificate for `FAR3-nodewise`.  This document records the
abstract schema.

## 2. Certificate data

For a fixed natural-height window and off-line cluster `A=(a,m)`, the certificate contains:

```text
1. finite poles d_n;
2. finite pole-even vector xi_n;
3. critical heights gamma_k;
4. numerator divisor proxy Div(P_x) used only to select FAR3;
5. FAR3 index set D_3;
6. rational node values |P_x(-gamma_k)|/|D_x(-gamma_k)|;
7. budgets b_k for k in D_3 and c_k for k notin D_3.
```

## 3. Verification steps

The verifier checks:

```text
V1. C_x(t)=P_x(t)/D_x(t) by product evaluation;
V2. D_3 consists of the three largest FAR scores;
V3. each nodewise inequality T_k <= budget_k;
V4. sum budget_k <= L^B.
```

If these hold, then:

```text
sum_k T_k <= L^B,
```

which is `WCS`.

## 4. Proof of sufficiency

By V3,

```text
T_k <= budget_k
```

for every critical node.  Summing:

```text
sum_k T_k <= sum_k budget_k.
```

By V4,

```text
sum_k budget_k <= L^B.
```

Thus `WCS` holds.  E73.042 gives:

```text
WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

## 5. What remains

The finite schema is complete for a fixed window.  The remaining analytic work is to produce a
uniform rule for the budgets:

```text
budget_k = budget_k(L,A,gamma_k,d,xi)
```

whose total is bounded by `L^B` for all natural-height windows.

This is the current sharp uniform theorem.
