# E72.137 -- Model coercivity by Gershgorin

**Date:** 2026-07-09.
**Role:** convert model complement coercivity into explicit entrywise inequalities.

## 0. Entrywise theorem

Let `C_model` be the model shorted complement matrix in the orthonormal even complement basis.  Suppose
that for fixed physical band and window there is `a_H>0` such that every row satisfies:

```text
C_model(i,i) - sum_{j!=i}|C_model(i,j)| >= a_H L.           (GCOER)
```

Then:

```text
C_model >= a_H L I.                                        (MCOER)
```

### Proof

By the Gershgorin circle theorem, every eigenvalue of the Hermitian matrix `C_model` lies in the union
of intervals:

```text
[C_model(i,i)-sum_{j!=i}|C_model(i,j)|,
 C_model(i,i)+sum_{j!=i}|C_model(i,j)|].
```

If `(GCOER)` holds, all intervals lie in `[a_HL,infty)`.  Hence:

```text
lambda_min(C_model)>=a_HL.
```

This is `(MCOER)`. `QED`

## 1. Updated route

Combining E72.134 and this theorem:

```text
GCOER + RCOER => COER.
```

Then E72.132 gives:

```text
COER + MSB => MG.
```

Then E72.127 gives:

```text
CGE-K + ROP + MG => scalar WRL.
```

Thus:

```text
CGE-K + ROP + GCOER + RCOER + MSB
=> scalar WRL resonance annihilation.
```

## 2. Status

```text
proved: GCOER implies MCOER;
proved: CGE-K + ROP + GCOER + RCOER + MSB imply scalar WRL;
open:   prove GCOER, RCOER, MSB, ROP, and CGE-K as explicit finite inequalities.
```
