# E73.177 results - stable divisor bridge

Date: 2026-07-14.

Script:

```text
E73_177_stable_divisor_bridge_probe.py
```

## Output

```text
E73.177 stable-divisor bridge probe
Compares raw critical nodal smallness ||G|| with quotient smallness ||P_Q G||.
 lam     L imageRel rawB quotB ratioB maxNodeB
   8   4.159  4.0e-06 -13.56 -13.67  -0.11   -13.74
  10   4.605  1.9e-07 -13.79 -13.81  -0.02   -13.84
  12   4.970  1.8e-06 -12.70 -12.71  -0.00   -12.80
  14   5.278  9.5e-06 -10.86 -10.92  -0.06   -10.90
  16   5.545  1.8e-04 -10.74 -10.75  -0.01   -10.75
  20   5.991  5.2e-02 -10.89 -10.89   0.00   -10.92
  24   6.356  2.6e-01 -12.56 -12.56   0.00   -12.56
  32   6.931  3.3e-02 -17.17 -17.17   0.00   -17.19
```

## Reading

In trusted rows, the quotient norm and raw norm have essentially the same
scale:

```text
||P_QG|| ~= ||G||.
```

Therefore the quotient projection is not the source of the exponential
smallness.  The smallness is already present in the raw nodal values
`G_L(i gamma_j)`.

## Endpoint

The current proof-facing target is:

```text
SDI-node:
G_L(i gamma_j)=O(L^B e^(-alpha L))
```

for fixed critical zeros.  This is the local nodal form of CCM stable divisor
identification.
