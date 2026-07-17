# E72.102 -- Matched-roots audit

**Date:** 2026-07-09.
**Role:** test whether the model `D2` defect is caused by evaluating the model complement at actual
finite roots instead of model finite roots.

## 0. Question

E72.101 shows that `D2` is already present in the prolate/archimedean model complement. A possible
explanation is root mismatch:

```text
C_model is being tested at actual roots tau_j(xi), not at model roots tau_j(k).
```

If so, one would expect:

```text
D2_model(tau_j(k)) approx 0.
```

## 1. Probe

The companion script:

```text
E72_102_matched_roots_probe.py
```

compares:

```text
actual@A = C_actual tested at actual roots,
model@A  = C_model  tested at actual roots,
model@M  = C_model  tested at model roots.
```

## 2. Result

For `s=10+0.2i`, `H=18`, roots below height `10`:

```text
lambda  rootsA rootsM  max actual@A  max model@A  max model@M
8          6      3      1.904e-02    1.639e-02    2.409e-02
12         5      4      1.566e-02    1.557e-02    1.004e-02
16         8      7      2.656e-02    2.572e-02    2.845e-02
20         7      6      3.137e-02    1.246e-02    1.104e-02
24         4      3      9.460e-03    9.295e-03    1.465e-02
```

## 3. Conclusion

The model defect does not disappear when tested at model roots. Therefore the obstruction is not merely:

```text
actual roots versus model roots.
```

It is intrinsic to the finite-band transport certificate:

```text
R_{x,H}(s;tau)=<r_s^even,B_xC_E^(-1)B_x^*P_HZ_x(tau)>.
```

## 4. Status

```text
rejected: root mismatch as the explanation of D2;
kept:     D2 as an intrinsic finite-band transport defect;
open:     either prove D2 by a full determinant identity or change the finite-band normalization.
```
