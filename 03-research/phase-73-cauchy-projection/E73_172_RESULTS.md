# E73.172 results - QG scalar linear forms

Date: 2026-07-14.

Script:

```text
E73_172_qg_linear_forms_probe.py
```

## Output

```text
E73.172 QG scalar linear forms
Writes ||P_Q G|| as the l2 norm of three explicit scalar forms.
 lam     L inter imageRel qdim coeffOp coeffMax    qgB  formsB
   8   4.159     2  4.0e-06    3    1.00 8.90e-01  -13.67 -14.24,-14.07,-13.93
  10   4.605     2  1.9e-07    3    1.00 9.47e-01  -13.81 -15.38,-14.45,-13.86
  12   4.970     2  1.8e-06    3    1.00 9.84e-01  -12.71 -14.77,-12.81,-13.10
  14   5.278     2  9.5e-06    3    1.00 1.00e+00  -10.92 -12.27,-11.29,-11.03
  16   5.545     2  1.8e-04    3    1.00 9.77e-01  -10.75 -12.93,-11.92,-10.76
  20   5.991     0  5.2e-02    5    1.00 1.00e+00  -10.89 -18.94,-19.41,-19.35
  24   6.356     0  2.6e-01    5    1.00 1.00e+00  -12.56 -18.60,-18.87,-19.53
  32   6.931     0  3.3e-02    5    1.00 1.00e+00  -17.17 -18.22,-18.01,-17.19
```

## Reading

The trusted rows are the rows with `imageRel <= 1e-3`.  In those rows:

```text
inter = 2,
qdim = 3,
coeffOp = 1,
coeffMax = O(1).
```

Thus the passage from `QG` to three scalar linear forms does not introduce
an exponential coefficient loss.  The remaining estimates are genuinely the
three scalar cancellations:

```text
ell_{r,L}(G_L) = O(L^B e^(-alpha L)), r=1,2,3.
```

Rows with `imageRel > 1e-3` are not used as quotient evidence because the
coefficient-image computation is not stable there.
