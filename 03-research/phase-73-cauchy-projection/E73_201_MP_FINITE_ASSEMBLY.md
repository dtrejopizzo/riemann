# E73.201 - Multiprecision finite assembly

Date: 2026-07-14.

## 1. Purpose

E73.200 shows that the final certificate is a cancellation between an
archimedean term and a prime term that are much larger than the final residual.
This note checks whether the remaining instability is caused by ordinary
floating summation of the finite-frequency formula.

## 2. Method

The script reuses the same finite coefficients from the Cauchy packet, but
assembles the certificate with `mpmath` at 100 decimal digits:

```text
A_L^digamma[B_a]-P_L[B_a].
```

The inputs `xi`, `row`, and the finite packet coefficients are still generated
from the existing double matrix engine.  Thus this is not yet a rigorous
interval proof.  It is a targeted diagnostic: does high-precision summation of
the finite formula change the certificate at the same scale as the E73.199
residual?

## 3. Status

```text
diagnostic: high-precision finite assembly;
not yet: interval proof, because packet coefficients are still point values.
```
