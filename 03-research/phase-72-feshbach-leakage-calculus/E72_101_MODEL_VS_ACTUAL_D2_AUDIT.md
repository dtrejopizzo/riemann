# E72.101 -- Model versus actual D2 audit

**Date:** 2026-07-09.
**Role:** decide whether the finite-band determinant defect `D2` is arithmetic or already present in
the prolate/archimedean model.

## 0. Question

E72.97 reduces the hard obstruction to:

```text
D2=<a_x(s),C_E^(-1)c_{x,H}(tau_j)>.
```

Here `C_E` uses the actual arithmetic CCM matrix. A hopeful route would be:

```text
D2_model=0,
D2_actual-D2_model small by PNT/prime perturbation.
```

Then `D2` would be an arithmetic perturbation estimate.

## 1. Probe

The companion script:

```text
E72_101_model_vs_actual_d2_probe.py
```

uses the same:

```text
k_x, B_x, finite actual roots tau_j, transport vector Z_x(tau_j),
```

but compares:

```text
C_actual = Q(H_actual-e0_model)Q,
C_model  = Q(H_model -e0_model)Q.
```

It prints:

```text
|D2_actual|, |D2_model|, |D2_actual-D2_model|.
```

## 2. Result

Representative output:

```text
lambda=8:
  tau=0.728  |D2_actual|=1.904e-02  |D2_model|=1.639e-02  model/actual=8.61e-01
  tau=5.988  |D2_actual|=3.319e-03  |D2_model|=3.993e-03  model/actual=1.20e+00

lambda=16:
  tau=2.077  |D2_actual|=1.561e-02  |D2_model|=1.309e-02  model/actual=8.39e-01
  tau=4.691  |D2_actual|=3.111e-03  |D2_model|=2.904e-03  model/actual=9.33e-01

lambda=24:
  tau=6.889  |D2_actual|=3.897e-03  |D2_model|=3.938e-03  model/actual=1.01e+00
  tau=8.020  |D2_actual|=6.204e-03  |D2_model|=6.206e-03  model/actual=1.00e+00
```

## 3. Conclusion

The defect is already present in the model complement. Therefore:

```text
D2 is not primarily an arithmetic perturbation defect.
```

This rejects the simple route:

```text
prove D2 by PNT-smallness of C_actual-C_model.
```

The remaining cancellation, if it exists, must come from a further renormalization of the model
finite-band transport or from a different normalization of `D2`, not from the raw model/actual split.

## 4. Relative subtraction check

One can also test:

```text
D2_rel:=D2_actual-D2_model.
```

For `s=10+0.2i`, `H=18`, and roots below height `10`, a quick summary gives:

```text
lambda  roots  max|actual|  max|model|  max|relative|
8          6    1.904e-02   1.639e-02    2.915e-02
10         6    2.852e-02   3.382e-02    5.306e-03
12         5    1.566e-02   1.557e-02    1.042e-02
16         8    2.656e-02   2.572e-02    7.152e-03
20         7    3.137e-02   1.246e-02    2.033e-02
24         4    9.460e-03   9.295e-03    3.311e-03
```

The relative defect is sometimes smaller, but not monotonically or structurally enough to serve as the
closure mechanism by itself.

## 5. Status

```text
rejected: D2 vanishes in the prolate/archimedean model;
rejected: PNT perturbation of C_E as the main proof of D2;
rejected: raw D2_actual-D2_model subtraction as a complete mechanism;
open:     identify the missing model normalization or prove a different finite-band identity.
```
