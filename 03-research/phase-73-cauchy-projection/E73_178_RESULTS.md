# E73.178 results - characteristic node equivalence

Command:

```text
python3 E73_178_characteristic_node_probe.py
```

Output:

```text
E73.178 characteristic-node equivalence probe
Checks G_L(i gamma)=i sqrt(L) exp(i gamma L/2) Phi_L(-gamma).
 lam     L      maxRel      maxAbs    maxNodeB    maxPhiB    scaleB
   8   4.159   1.63e-16   4.14e-25    -13.74   -14.24    0.50
  10   4.605   1.97e-16   1.03e-25    -13.84   -14.34    0.50
  12   4.970   1.70e-16   2.07e-25    -12.80   -13.30    0.50
  14   5.278   1.86e-16   8.27e-25    -10.90   -11.40    0.50
  16   5.545   1.82e-16   1.85e-24    -10.75   -11.25    0.50
  20   5.991   2.04e-16   6.62e-25    -10.92   -11.42    0.50
  24   6.356   3.54e-16   1.45e-26    -12.56   -13.06    0.50
  32   6.931   3.67e-16   3.94e-31    -17.19   -17.69    0.50
```

Reading:

```text
maxRel ~ 1e-14: identity verified to floating precision.
scaleB = 0.50: |G_L(i gamma)| = L^(1/2)|Phi_L(-gamma)| exactly.
```

Therefore the current `SDI-node` theorem is exactly a finite characteristic nodal vanishing theorem,
with the expected square-root normalization factor.
