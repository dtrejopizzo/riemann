# E73.240 results - eigen-coefficient branch audit

Command:

```text
python3 E73_240_eig_coeff_branch_audit.py
```

## 1. Output

```text
E73.240 eigen-coefficient branch audit
Checks QH(I-P)xi = (mu I-A)Qxi and exposes h-dependence.
 lam      L gamma row centerB branchB errB hB muB opAB
   8    4.159  14.13   0   -21.68   -21.68  -27.79  -19.03  -24.84   -0.73
   8    4.159  14.13   1   -21.46   -21.46  -29.21  -19.03  -24.84   -0.73
   8    4.159  21.02   0   -15.76   -15.76  -29.32  -13.24  -24.84   -0.73
   8    4.159  21.02   1   -15.79   -15.79  -28.89  -13.24  -24.84   -0.73
  10    4.605  14.13   0   -18.50   -18.50  -25.04  -17.91  -21.82   -0.36
  10    4.605  14.13   1   -18.51   -18.51  -25.09  -17.91  -21.82   -0.36
  10    4.605  21.02   0   -14.98   -14.98  -25.44  -14.40  -21.82   -0.35
  10    4.605  21.02   1   -14.98   -14.98  -25.16  -14.40  -21.82   -0.35
  12    4.970  14.13   0   -20.64   -20.64  -25.28  -19.10  -20.55   -0.48
  12    4.970  14.13   1   -20.34   -20.35  -24.13  -19.10  -20.55   -0.48
  12    4.970  21.02   0   -16.61   -16.61  -24.75  -15.28  -20.55   -0.43
  12    4.970  21.02   1   -16.84   -16.84  -28.10  -15.28  -20.55   -0.43
  16    5.545  14.13   0   -19.32   -19.10  -19.78  -20.04  -18.67    1.00
  16    5.545  14.13   1   -19.96   -19.57  -19.99  -20.04  -18.67    1.00
  16    5.545  21.02   0   -18.18   -18.17  -20.60  -19.12  -18.67    0.98
  16    5.545  21.02   1   -19.03   -19.07  -20.65  -19.12  -18.67    0.98
  20    5.991  14.13   0   -18.89   -20.23  -18.94  -19.29  -17.46    1.00
  20    5.991  14.13   1   -18.33   -18.29  -19.81  -19.29  -17.46    1.00
  20    5.991  21.02   0   -17.68   -17.67  -19.89  -18.50  -17.46    1.01
  20    5.991  21.02   1   -17.79   -17.72  -18.85  -18.50  -17.46    1.01
```

## 2. Interpretation

The exact identity is:

```text
QH(I-P)xi=(mu I-A)Qxi.
```

For `lambda=8,10,12`, the double-precision audit verifies it several powers
below the center.  For larger windows the branch computation becomes
conditioning-limited: `A` is order `L^1`, `h=Qxi` is tiny, and the product is
at the same small scale as the center.  The exact algebra remains valid, but
this branch is not a proof-facing numerical certificate.

More importantly, the right side depends on:

```text
h=Qxi.
```

Thus it proves the center small only if the characteristic divisor is already
small.  This is exactly the circular branch E73.188 warned about.

## 3. Consequence

The valid eigen-coefficient target is not:

```text
center=(mu I-A)h.
```

The valid target is:

```text
CURV-COB:
the curvature quotient source is a structured coefficient coborder modulo
fixed endpoint residual slots.
```

This imports the non-tautology rules from E73.162 but applies them to the
curvature source from E73.238.

