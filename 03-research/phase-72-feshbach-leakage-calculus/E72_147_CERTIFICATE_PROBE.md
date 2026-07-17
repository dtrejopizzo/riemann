# E72.147 -- Combined semialgebraic certificate probe

**Date:** 2026-07-09.
**Role:** evaluate the E72.146 certificate in one finite table.

## 0. Quantities

The companion script:

```text
E72_147_semialgebraic_certificate_probe.py
```

reports:

```text
GCOER/L:
  min_i(C_model(ii)-sum_{j!=i}|C_model(ij)|)/L,

PSDdist2:
  dist(K_rel,PSD)^2 = ||K_rel^-||_HS^2,

PSDmargin:
  1-PSDdist2,

MSB:
  sup ||b_H||||c_H^{pm}(tau_j)||,

ROP:
  sup ||R_xY_x(tau_j)||,

GraphN:
  Graph_x(s)/(1+|s|^2).
```

These are exactly the finite certificate pieces:

```text
GCOER + PSD-DIST + MSB + ROP + CGE-K.
```

## 1. Status

```text
observed: all five certificate quantities are in the required finite regime in the tested windows.
```

Representative output:

```text
E72.147 finite semialgebraic certificate probe
 lam   L roots  GCOER/L  PSDdist2  PSDmargin   MSB    ROP    GraphN
   6  3.58     3    0.329     0.584      0.416  0.427  0.055   1.058
   8  4.16     4    0.412     0.641      0.359  0.350  0.063   1.003
  10  4.61     3    0.674     0.478      0.522  0.334  0.039   1.002
  12  4.97     4    0.759     0.612      0.388  0.235  0.023   1.110
  14  5.28     4    0.716     0.559      0.441  0.205  0.023   1.047
  16  5.55     5    1.043     0.525      0.475  0.259  0.024   1.051
```
