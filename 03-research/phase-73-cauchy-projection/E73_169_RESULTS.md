# E73.169 results - quotient pair geometry

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_169_quotient_pair_geometry_probe.py
```

Output:

```text
E73.169 quotient pair geometry probe
Coordinates Pi_Q and G_Q in the 3D quotient basis and measures angular avoidance.
 lam     L inter imageRel  |Gq|     rows: cos(PiQ,GQ)/|PiQ|/scalar
   8   4.159     2  4.0e-06  3.4e-09 0.70/2.0e-01/3.2e-10  0.80/4.4e-04/3.7e-12  0.31/1.3e+00/8.5e-09
  10   4.605     2  1.9e-07  6.9e-10 0.30/4.1e-01/1.1e-10  0.49/4.6e-04/4.2e-13  0.80/6.2e-01/7.5e-10
  12   4.970     2  1.8e-06  1.4e-09 0.16/4.0e-01/2.4e-10  0.17/5.6e-04/3.7e-13  0.23/1.3e+00/1.1e-09
  14   5.278     2  9.5e-06  1.3e-08 0.30/9.5e-01/9.5e-09  0.40/4.9e-04/6.9e-12  0.22/1.3e+00/4.7e-09
  16   5.545     2  1.8e-04  1.0e-08 0.46/2.6e-01/3.1e-09  0.78/5.3e-04/1.3e-11  0.56/1.4e+00/2.7e-08
  20   5.991     0  5.2e-02  3.4e-09 0.01/2.0e+00/2.3e-10  0.39/7.5e-04/3.3e-12  0.35/2.1e+00/8.3e-09
  24   6.356     0  2.6e-01  8.2e-11 0.01/2.0e+00/7.0e-12  0.49/7.5e-04/1.1e-13  0.36/2.1e+00/2.3e-10
  32   6.931     0  3.3e-02  5.2e-15 0.33/2.0e+00/1.4e-14  0.10/7.5e-04/1.1e-18  0.32/2.1e+00/1.5e-14
```

Reading:

```text
1. No uniform angular avoidance is visible.  In trusted rows the cosine
   ranges from 0.16 to 0.80.

2. The quotient scalar is small because the quotient dual vector has small
   absolute size in these finite tests, not because of consistent angular
   cancellation.

3. The endpoint remains a quotient pairing or quotient norm theorem.
```

Conclusion:

```text
QUOT-PAIR is now the sharp finite target; QUOT-NORM is a clean sufficient
target if one wants a Cauchy-Schwarz route.
```

