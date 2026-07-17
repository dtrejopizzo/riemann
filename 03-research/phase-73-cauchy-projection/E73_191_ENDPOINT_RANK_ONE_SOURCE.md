# E73.191 - Endpoint rank-one source

Date: 2026-07-14.

## 1. Purpose

E73.190 proved that the transverse Cauchy-Dirichlet packet satisfies

```text
B_a'(0)=-(2/L) S_q(a) S_eta,
S_q(a)=sum_m 1/(a+i d_m),
S_eta=sum_n eta_n.
```

This note isolates that source.  It is the first nonzero Taylor datum after
the endpoint value `B_a(0)=0`.

## 2. Consequence

Near zero,

```text
B_a(y)=-(2/L)S_q(a)S_eta * y + O(y^2).
```

Therefore the regularized WR term in the archimedean cell begins with

```text
e^(y/2)B_a(y)/(2sinh y) = -(1/L)S_q(a)S_eta + O(y).
```

Thus the endpoint contribution is not a double arithmetic sum.  It is a
rank-one scalar source.  Any proof of `TRANS-CELL` has two possible routes:

```text
1. show S_eta is small from the transverse ground-vector structure;
2. subtract the rank-one endpoint source explicitly and prove matching for
   the remainder B_a(y)-B_a'(0)y chi(y).
```

The second route is safer because E72.337 warned that generic endpoint
Dirichlet bounds do not close the problem.

## 3. Proof-facing decomposition

Choose a fixed smooth or finite Weyl-compatible ramp `r_0(y)` with

```text
r_0(0)=0,       r_0'(0)=1,       r_0(L)=0.
```

Then decompose

```text
B_a(y)=B_a'(0) r_0(y)+B_a^rem(y),
```

where

```text
B_a^rem(0)=0,       (B_a^rem)'(0)=0,       B_a^rem(L)=0.
```

The matching theorem becomes

```text
A_L[B_a^rem]-P_L[B_a^rem]
= -B_a'(0)(A_L[r_0]-P_L[r_0]) + O_R(L^-R).
```

If the scalar bracket `A_L[r_0]-P_L[r_0]` is computable and small, the
remaining packet has a double zero at the singular endpoint.  That is the
right object for integration by parts in the WR kernel.

## 4. Status

```text
proved: B_a'(0) is a rank-one endpoint source;
open: decide whether S_eta is structurally small or whether the ramp
      subtraction is the correct next normalization.
```

## 5. Prior-route audit

E72.58 already falsified literal rank-one endpoint suppression:

```text
<v,1><1,k> is not small in the endpoint channel.
```

E72.131 also warned that raw source masses can be only `O(1)`; smallness may
enter only after model subtraction or shorting.  Therefore `MASS-ZERO` should
not be treated as an available theorem merely because the present diagnostic
shows small `sum xi_L` in tested windows.

The robust next step is the explicit ramp subtraction:

```text
B_a = B_a'(0)r_0 + B_a^rem,
```

and then to prove model-prime matching separately for the rank-one ramp term
and the double-zero remainder.
