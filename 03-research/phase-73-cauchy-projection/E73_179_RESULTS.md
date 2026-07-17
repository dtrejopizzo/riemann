# E73.179 results - Cauchy-plane cell residual

Command:

```text
python3 E73_179_cauchy_plane_cell_residual_probe.py
```

Output:

```text
E73.179 Cauchy-plane cell residual probe
Verifies (mu I-A)h=rho xi and compares zeta/arch residual channels.
errB is log_L absolute identity error; relative error is ill-conditioned in tiny zeta rows.
 lam     L gamma   hB_z   rB_z  invB_z  errB_z   hB_a   rB_a  invB_a  errB_a
  16   5.545   14.13 -20.04 -19.22   -0.98  -19.80   -1.39   0.11   -1.49  -20.03
  16   5.545   21.02 -19.12 -18.16   -0.96  -20.68   -1.40   0.11   -1.51  -19.17
  16   5.545   25.01 -13.57 -14.23    0.65  -21.45   -1.34   0.15   -1.49  -20.19
  20   5.991   14.13 -19.29 -18.50   -0.99  -18.84   -1.39   0.18   -1.57  -19.10
  20   5.991   21.02 -18.50 -17.53   -1.00  -18.88   -0.05   1.53   -1.58  -17.87
  20   5.991   25.01 -18.15 -17.16   -0.98  -19.58   -1.57   0.01   -1.59  -18.00
  24   6.356   14.13 -17.62 -16.63   -0.99  -18.88   -0.87   0.75   -1.62  -18.93
  24   6.356   21.02 -18.86 -17.77   -0.99  -18.70   -0.90   0.73   -1.63  -17.95
  24   6.356   25.01 -19.73 -18.63   -0.98  -19.50   -0.97   0.67   -1.64  -18.55
  28   6.664   14.13 -17.00 -16.03   -1.00  -16.96    1.09   2.76   -1.67  -16.44
  28   6.664   21.02 -17.07 -16.07   -0.99  -17.85   -0.96   0.72   -1.68  -17.48
  28   6.664   25.01 -17.90 -16.86   -0.99  -18.19   -1.42   0.27   -1.69  -17.51
  32   6.931   14.13 -18.24 -17.14   -1.00  -17.75   -2.76  -1.05   -1.72  -17.60
  32   6.931   21.02 -17.77 -16.66   -1.00  -17.23   -0.72   1.01   -1.72  -17.72
  32   6.931   25.01 -17.47 -16.47   -1.00  -19.48   -1.72   0.01   -1.73  -18.06
```

Reading:

```text
errB is at the same tiny absolute scale as the zeta residual:
the Cauchy-plane equation is exact algebraically, but relative error is not
the right floating diagnostic when both sides are around `L^-17`.

invB_z ~ -1 in stable rows:
the two-dimensional divisor system is not ill-conditioned.

rB_z is about one power of `L` larger than hB_z, and invB_z supplies that
one-power gain.  Arch/free residuals are only ordinary size:
the residual cancellation is arithmetic and zeta-coupled, not a geometric
Cauchy-plane artifact.
```

The remaining theorem is therefore not a matrix-conditioning theorem.  It is
`RCE-cell`: prove the small evaluated residual from the explicit
prime/Gamma cell formula.
