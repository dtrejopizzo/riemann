# E73.062 - DEN-GAP target

## 1. Purpose

E73.061 shows that `CMAIN-10` is a denominator dominance statement.

This document states the exact finite target.

## 2. Definitions

For a FAR3 node `gamma_k`, define:

```text
P_k := P_x(-gamma_k),
D_k := D_x(-gamma_k).
```

Then:

```text
C_k=|C_x(-gamma_k)|=|P_k|/|D_k|.
```

## 3. DEN-GAP

The denominator gap theorem is:

```text
DEN-GAP-10:
|D_k| >= C_gap^(-1) L^10 |P_k|
```

for every FAR3 node `k`.

Equivalently:

```text
|P_k|/|D_k| <= C_gap L^-10.
```

This is exactly `CMAIN-10`.

## 4. Proof of equivalence

Starting from `DEN-GAP-10`,

```text
|D_k| >= C_gap^(-1)L^10|P_k|.
```

Divide by `|D_k|` and multiply by `C_gap L^-10`:

```text
|P_k|/|D_k| <= C_gap L^-10.
```

But `|P_k|/|D_k|=|C_x(-gamma_k)|`, hence `CMAIN-10`.

Conversely, `CMAIN-10` rearranges to `DEN-GAP-10`.

## 5. Finite product form

Since

```text
D_x(t)=prod_n(t-d_n),
P_x(t)=sum_n xi_n prod_{m != n}(t-d_m),
```

`DEN-GAP-10` is the finite inequality:

```text
prod_n |gamma_k+d_n|
>= C_gap^(-1)L^10
|sum_n xi_n prod_{m != n}(-gamma_k-d_m)|.
```

This is completely finite and uses no zero input.

## 6. Remaining analytic theorem

The load-bearing estimate is now:

```text
Uniform DEN-GAP:
There exist C_gap and L0 such that DEN-GAP-10 holds for every L>=L0 and every FAR3 node selected
from every natural-height off-line cluster.
```

Together with `PREF-5`, this proves the main half of `BUD-5/9`.
