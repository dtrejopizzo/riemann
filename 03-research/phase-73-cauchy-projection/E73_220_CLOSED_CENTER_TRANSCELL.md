# E73.220 - Closed-center TRANS-CELL check

Date: 2026-07-14.

## 1. Purpose

E73.219 shows that the scalar radius propagated from `[H]` and `[eta]` is
small.  The remaining finite issue is the scalar center:

```text
C_a=A_L^digamma[B_a]-P_L[B_a].
```

This note compares the closed finite-frequency center against the diagnostic
matrix center

```text
q_aHeta.
```

## 2. Result

The closed center and the matrix center agree in logarithmic scale in all
tested windows.  The relative discrepancy is small but not negligible in the
most delicate row:

```text
max relative discrepancy = 2.4e-2.
```

This is consistent with E73.206/E73.200: the final scalar is a cancellation of
larger archimedean and prime terms, so a legacy matrix center is not the right
authority for the final outward interval.

## 3. Consequence

The final finite certificate should be organized as:

```text
center  = outward-rounded closed A_L^digamma-P_L evaluation,
radius  = E73.219 scalar propagation radius
          + closed-center arithmetic radius.
```

It should not use the legacy matrix center except as a diagnostic comparison.

## 4. Status

```text
verified: closed-center exponents match the matrix scalar exponents;
identified: legacy center discrepancy can be percent-level in delicate rows;
next: package closed-center arithmetic radius with E73.219 scalar radius.
```
