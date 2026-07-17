# E73.221 results - closed-center stability audit

Command:

```text
python3 E73_221_closed_center_stability.py
```

Output:

```text
E73.221 closed-center stability audit
Compares dps=80,100,140 for C_a=A_L^digamma-P_L.
 lam     L    N gamma row centerB diff80B diff100B rel80 rel100
   8   4.159    6   14.13   0  -21.68 -132.00  -164.20 5.1e-69  6.1e-89
   8   4.159    6   14.13   1  -21.46 -131.34  -163.70 9.7e-69  9.0e-89
   8   4.159    6   21.02   0  -15.76 -132.03  -164.64 1.1e-72  7.0e-93
   8   4.159    6   21.02   1  -15.79 -132.15  -164.73 9.5e-73  6.5e-93
  10   4.605    8   14.13   0  -18.50 -121.35  -152.51 6.0e-69  1.3e-89
  10   4.605    8   14.13   1  -18.51 -120.93  -151.96 1.2e-68  3.1e-89
  10   4.605    8   21.02   0  -14.98 -120.96  -152.02 5.2e-71  1.3e-91
  10   4.605    8   21.02   1  -14.98 -120.83  -152.89 6.2e-71  3.4e-92
  12   4.970   10   14.13   0  -20.62 -117.88  -146.35 1.9e-68  2.8e-88
  12   4.970   10   14.13   1  -20.34 -116.37  -145.00 1.4e-67  1.6e-87
  12   4.970   10   21.02   0  -16.61 -116.35  -146.14 3.5e-70  6.3e-91
  12   4.970   10   21.02   1  -16.84 -116.56  -146.69 3.6e-70  3.8e-91
```

Interpretation:

The closed center is stable far below every scalar radius budget currently
used in the certificate chain.  The remaining center issue is formal outward
rounding, not numerical precision.
