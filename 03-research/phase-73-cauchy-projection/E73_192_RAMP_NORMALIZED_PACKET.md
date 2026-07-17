# E73.192 - Ramp-normalized transverse packet

Date: 2026-07-14.

## 1. Purpose

E73.191 isolated the first endpoint derivative:

```text
B_a'(0)=-(2/L)S_q(a)S_eta.
```

Because earlier Phase 72 work falsified literal rank-one endpoint suppression,
the correct move is not to assume this derivative is negligible.  This note
defines an explicit ramp subtraction and reduces the remaining packet to a
double-zero object.

## 2. Ramp

Use

```text
r_0(y)=y(1-y/L).
```

Then

```text
r_0(0)=0,       r_0'(0)=1,       r_0(L)=0.
```

For each transverse packet set

```text
B_a^rem(y)=B_a(y)-B_a'(0)r_0(y).
```

Then

```text
B_a^rem(0)=0,
(B_a^rem)'(0)=0,
B_a^rem(L)=0.
```

## 3. Exact decomposition of TRANS-CELL

Linearity gives

```text
A_L[B_a]-P_L[B_a]
= B_a'(0)(A_L[r_0]-P_L[r_0])
  + A_L[B_a^rem]-P_L[B_a^rem].                   (1)
```

Thus `TRANS-CELL` is equivalent to proving:

```text
RAMP-MATCH:
B_a'(0)(A_L[r_0]-P_L[r_0]) is controlled or included in the main term;

DOUBLE-ZERO-MATCH:
A_L[B_a^rem]-P_L[B_a^rem]=O_R(L^-R).
```

The second packet has a double zero at the singular endpoint of the WR kernel,
so it is the right object for integration by parts and Taylor-tail estimates.

## 4. Why this is not a retreat

The ramp is explicit and independent of the zeros.  It does not use `Q_wxi_L`
smallness.  It only removes the rank-one endpoint source already proved in
E73.190.  This is exactly the correction demanded by E72.58: rank-one endpoint
terms must be treated as model-main terms, not wished away.

## 5. Status

```text
proved: linear ramp decomposition (1);
verified next: size of ramp contribution versus total signed residual;
open: prove RAMP-MATCH and DOUBLE-ZERO-MATCH analytically.
```
