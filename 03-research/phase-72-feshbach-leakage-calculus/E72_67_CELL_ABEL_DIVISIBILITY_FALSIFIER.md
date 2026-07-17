# E72.67 -- Falsifier for cell-Abel-only divisibility

**Date:** 2026-07-08.
**Role:** test whether the unnormalized continuous Abel transform of the CCM overlap cell already
carries the finite spectral divisor.

## Correction note

E72.68 supersedes the interpretation of this falsifier. The actual scalar WRL cell contains the
half-power factor:

```text
L_x(s;e^y)=e^(-y/2)<v,Q_x(y)k>.
```

This document only falsifies the **unnormalized** overlap transform `<v,Q_x(y)k>`. It does not falsify
the half-power Abel concomitant of E72.68.

## 0. Tested object

For the unnormalized test:

```text
L_cell(y)=<v,Q_x(y)k>,
```

the continuous Abel resonance is:

```text
R_cell(rho)=L_cell(0)+rho int_0^L exp(rho y)L_cell(y)dy,
```

using `Q_x(L)=0`. With the height alignment:

```text
rho=1/2+i tau.
```

If overlap geometry alone carried the finite CCM divisor, then:

```text
R_cell(1/2+i tau_j)=0
```

for every finite Weyl root `P_x(tau_j)=0`.

## 1. Numerical falsifier

With the same finite data as E72.66:

```text
lambda=6, N=18:
  tau=1.0162   |R_cell|=1.281e-1
  tau=3.4414   |R_cell|=1.521e-1
  tau=5.9779   |R_cell|=1.432e-1
  tau=8.0360   |R_cell|=2.628e-1

lambda=8, N=24:
  tau=0.7284   |R_cell|=9.409e-2
  tau=2.7080   |R_cell|=1.986e-1
  tau=4.0531   |R_cell|=1.660e-1
  tau=5.9877   |R_cell|=1.429e-1

lambda=12, N=28:
  tau=0.8248   |R_cell|=5.376e-2
  tau=2.1349   |R_cell|=6.839e-2
  tau=3.2205   |R_cell|=4.351e-2
  tau=8.1177   |R_cell|=2.680e-1
```

The values are not zero at the finite divisor.

## 2. Consequence

The finite spectral divisor is not carried by:

```text
overlap geometry alone,
endpoint discrepancy alone,
or raw discrete Mellin cells.
```

The unnormalized overlap geometry is insufficient. The surviving divisibility target must at least use:

```text
1. the half-power normalization e^(-y/2),
2. Feshbach shorting through C_x^(-1)Q_x,
3. the Abel boundary-minus-bulk combination,
4. the actual arithmetic/model matching.
```

This is consistent with E72.32: the needed object is a half-power arithmetic scalar coborder, not this
unnormalized universal cell identity.

## 3. Status

```text
falsified: unnormalized cell-Abel-only divisibility by P_x;
open:      test and construct divisibility for the half-power WRL scalar kernel.
```
