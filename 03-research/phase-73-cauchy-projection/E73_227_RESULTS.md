# E73.227 results - native-ball weight radius budget

Command:

```text
python3 E73_227_native_ball_weight_radius.py
```

Output:

```text
E73.227 native-ball weight radius budget
Replaces E73.225 finite-rounding heuristic by native complex-ball propagation.
 lam     L    N gamma row csec maxFinWB maxPsiWB totalB scaleB ratio
   8   4.159    6   14.13   0  1.0   -156.02    -84.48  -85.91   -1.33  4.5e-53
   8   4.159    6   14.13   0 1.0e+6   -156.02    -74.78  -76.21   -1.33  4.5e-47
  10   4.605    8   14.13   0  1.0   -145.22    -78.84  -79.25   -0.30  4.3e-53
  10   4.605    8   14.13   0 1.0e+6   -145.22    -69.79  -70.21   -0.30  4.3e-47
  12   4.970   10   14.13   0  1.0   -137.98    -75.09  -75.79   -0.62  4.5e-53
  12   4.970   10   14.13   0 1.0e+6   -137.98    -66.47  -67.17   -0.62  4.5e-47
```

Representative rows are shown.  The full script checks both Cauchy rows and
both heights.

Interpretation:

The finite elementary/prime rounding part of the weight radii is negligible
under native complex-ball propagation.  The total is dominated by the
Bernoulli `psi/psi_1` remainder, exactly as in the matrix-entry certificate.
