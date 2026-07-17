# E72.37 -- Normalized Mellin probe for scalar WRL divisibility

**Date:** 2026-07-08.
**Role:** test the corrected object suggested by E72.36: the Abel-normalized Mellin transform rather
than the raw `sum n^z` transform.

## 0. Normalized test

The raw diagnostic used

```text
sum n^z <v_s,T_nk>.
```

This is not the Abel resonance scale. The normalized boundary scale is

```text
sum (n/x)^z <v_s,T_nk>.
```

This is the finite-cell analogue of

```text
x^{-z} R_x^{WRL}(s;z).
```

## 1. Numerical signal

With the same finite CCM data as E72.36, the normalized values at finite Weyl roots are small:

```text
lambda=4, N=22, x=16:
  r=3.3606    |M_norm(r)|=6.58e-3
  r=7.2222    |M_norm(r)|=5.18e-3
  r=10.5697   |M_norm(r)|=2.57e-3
  r=14.1347   |M_norm(r)|=1.17e-3

lambda=5, N=22, x=25:
  r=1.6594    |M_norm(r)|=4.82e-3
  r=8.0256    |M_norm(r)|=3.24e-3
  r=14.1347   |M_norm(r)|=2.32e-3
  r=18.6599   |M_norm(r)|=1.63e-3

lambda=8, N=30, x=64:
  r=2.570     |M_norm(r)|=3.78e-3
  r=3.942     |M_norm(r)|=2.74e-3
  r=5.697     |M_norm(r)|=1.86e-3
  r=7.751     |M_norm(r)|=1.23e-3
  r=9.358     |M_norm(r)|=9.27e-4

lambda=12, N=24, x=144:
  r=1.816     |M_norm(r)|=3.64e-3
  r=3.375     |M_norm(r)|=1.58e-3
  r=5.051     |M_norm(r)|=7.64e-4
  r=6.203     |M_norm(r)|=5.04e-4
  r=8.025     |M_norm(r)|=2.97e-4
```

This is not exact finite divisibility, but it is compatible with asymptotic normalized divisibility.

## 2. Endpoint interpretation

Write the normalized finite transform as

```text
N_x(s;z)=sum_{n<=x} (n/x)^z l_x(s;n),
l_x(s;n)=<v_{x,s},T_{x,n}k_x>.
```

For `Re z>0`, the weight `(n/x)^z` damps cells away from the endpoint `n=x`. Thus a sufficient
condition is an endpoint tightness estimate:

```text
sum_{n<=x} (n/x)^sigma |l_x(s;n)| -> 0
```

for the relevant `sigma=Re z`, or the signed version:

```text
sum_{n<=x} (n/x)^z l_x(s;n) -> 0.
```

The numerics suggest the scalar Weyl-Feshbach kernel may be endpoint-small after pole-relative
compression, even though the raw Mellin transform explodes.

## 3. New estimate

### Endpoint Weyl-Feshbach Tightness

For two interior Cauchy heights and every compact spectral set `K`,

```text
sup_{z in K}
|sum_{n<=x} (n/x)^z <v_{x,s},T_{x,n}k_x>| -> 0.  (EWFT)
```

Together with the model-main Abel subtraction, `(EWFT)` implies normalized scalar WRL resonance
annihilation.

## 4. Why this is not the PNT ceiling

The estimate is on the compressed scalar kernel

```text
<C_x^(-1)Q_x(sI-D_x)^(-1)1_x, T_{x,n}k_x>,
```

not on the von Mangoldt discrepancy itself. It uses:

```text
Feshbach compression,
Cauchy current testing,
endpoint normalization.
```

These are absent from the Phase 70 Hardy-Euler ceiling.

## 5. Status

```text
falsified: raw Mellin divisibility;
observed:  normalized Mellin endpoint smallness;
open:      prove EWFT from compressed CCM/prolate kernel estimates.
```

The next step is to derive EWFT from resolvent bounds on `v_{x,s}` and endpoint decay of the cell
action `T_{x,n}k_x`.
