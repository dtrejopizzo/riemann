# E72.382 Results - Local weight scale

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_382_local_weight_scale_probe.py
```

## Output

```text
E72.382 local weight scale probe
 lam     L       Tmoderate  massMod  predMod   Texp       massExp  predExp
   6   3.584       50.0 2.560e+00 3.394e+00       36.0 3.003e+00 4.000e+00
   8   4.159       70.0 3.109e+00 3.825e+00       64.0 3.249e+00 4.000e+00
  10   4.605       90.0 3.527e+00 4.216e+00      100.0 3.347e+00 4.000e+00
  12   4.970      110.0 4.013e+00 4.577e+00      144.0 3.512e+00 4.000e+00
```

## Reading

The exact local mass

```text
int_0^L W_{L,delta}(r)dr
```

tracks the predicted scale

```text
4delta e^(L/2).
```

Taking the natural finite height

```text
T=e^L
```

makes `delta=e^(-L/2)` and keeps the local prime-window mass at constant scale.  This supports Route A
from E72.382: use the natural height of the prime cutoff, not a merely polynomial height in `L`.

## Status

```text
validated: local positive weight has scale delta e^(L/2);
validated: T=e^L neutralizes that mass in tested windows;
open: prove horizontal and finite-mesh tails remain polynomial at T=e^L.
```
