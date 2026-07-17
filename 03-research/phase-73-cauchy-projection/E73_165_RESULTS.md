# E73.165 results - rank-3 delta transfer

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_165_delta_transfer_probe.py
```

Output:

```text
E73.165 canonical delta transfer probe
T maps original cauchy0/Pi coefficients to canonical delta coefficients.
 lam     L  erank       op   frob  distI  dist0   idem   herm  svals
   8   4.159      3 1.00e+00 1.73e+00 6.32e-01 7.75e-01 1.7e-05 1.5e-07 1.00e+00,1.00e+00,1.00e+00,6.08e-06,4.54e-09 align=nan
  10   4.605      3 1.00e+00 1.73e+00 6.32e-01 7.75e-01 8.3e-06 3.9e-07 1.00e+00,1.00e+00,1.00e+00,7.95e-06,1.44e-09 align=0.356
  12   4.970      3 1.00e+00 1.73e+00 6.32e-01 7.75e-01 4.0e-06 1.4e-07 1.00e+00,1.00e+00,1.00e+00,6.90e-06,1.06e-09 align=0.850
  14   5.278      3 1.00e+00 1.73e+00 6.32e-01 7.75e-01 1.0e-05 4.8e-08 1.00e+00,1.00e+00,1.00e+00,1.71e-05,9.78e-11 align=0.878
  16   5.545      3 1.00e+00 1.73e+00 6.32e-01 7.75e-01 8.9e-05 4.3e-06 1.00e+00,1.00e+00,1.00e+00,4.11e-06,6.22e-09 align=0.153
  20   5.991      3 1.00e+00 1.73e+00 6.32e-01 7.75e-01 1.5e-04 3.7e-05 1.00e+00,1.00e+00,1.00e+00,5.41e-06,6.76e-10 align=0.415
  24   6.356      3 1.00e+00 1.73e+00 6.32e-01 7.73e-01 4.6e-03 2.2e-07 1.00e+00,1.00e+00,9.92e-01,8.41e-06,4.32e-10 align=0.247
  32   6.931      3 1.00e+00 1.73e+00 6.32e-01 7.74e-01 1.2e-03 1.1e-06 1.00e+00,1.00e+00,9.98e-01,7.11e-06,9.49e-10 align=0.399
```

Reading:

```text
1. Effective rank is 3 in every tested window.

2. The singular values are three unit values and two near-zero values.

3. Frobenius norm is sqrt(3), and the distances to identity/zero match the
   rank-three orthogonal projector profile in dimension five.

4. Idempotence and Hermitian errors are small:
   ||T^2-T||/||T|| = 1e-5--1e-3,
   ||T-T*||/||T||  = 1e-7--1e-5.
```

Conclusion:

```text
The canonical cauchy0 defect is the projection of Pi onto a rank-three
quotient of the five-dimensional critical atom space.
```

