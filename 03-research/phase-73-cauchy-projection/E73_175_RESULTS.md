# E73.175 results - boundary trace reduction

Date: 2026-07-14.

Script:

```text
E73_175_boundary_trace_probe.py
```

## Output

```text
E73.175 boundary trace identity
Checks B_r(0)=2 ell_r(G_L), since Q_L(0)=2I.
 lam     L imageRel form ellB B0B relErr q0DiagErr
   8   4.159  4.0e-06    0 -14.24 -13.75 0.0e+00   0.0e+00
   8   4.159  4.0e-06    1 -14.07 -13.59 0.0e+00   0.0e+00
   8   4.159  4.0e-06    2 -13.93 -13.45 0.0e+00   0.0e+00
  10   4.605  1.9e-07    0 -15.38 -14.93 0.0e+00   0.0e+00
  10   4.605  1.9e-07    1 -14.45 -13.99 0.0e+00   0.0e+00
  10   4.605  1.9e-07    2 -13.86 -13.41 0.0e+00   0.0e+00
  12   4.970  1.8e-06    0 -14.77 -14.34 0.0e+00   0.0e+00
  12   4.970  1.8e-06    1 -12.81 -12.38 0.0e+00   0.0e+00
  12   4.970  1.8e-06    2 -13.10 -12.67 0.0e+00   0.0e+00
  14   5.278  9.5e-06    0 -12.27 -11.86 0.0e+00   0.0e+00
  14   5.278  9.5e-06    1 -11.29 -10.87 0.0e+00   0.0e+00
  14   5.278  9.5e-06    2 -11.03 -10.62 0.0e+00   0.0e+00
  16   5.545  1.8e-04    0 -12.93 -12.53 0.0e+00   0.0e+00
  16   5.545  1.8e-04    1 -11.92 -11.51 0.0e+00   0.0e+00
  16   5.545  1.8e-04    2 -10.76 -10.35 0.0e+00   0.0e+00
```

## Reading

Both identities are exact in the finite harness:

```text
Q_L(0)=2I,
B_r(0)=2 ell_r(G_L).
```

The exponent shift between `ellB` and `B0B` is exactly the factor `2` in
base `L`.

## Endpoint

The active theorem can now be written:

```text
BT-QG:
|B_{r,L}(0)| <= L^B e^(-alpha L), r=1,2,3.
```

Together with `QPI`, this implies `QUOT-NORM`.
