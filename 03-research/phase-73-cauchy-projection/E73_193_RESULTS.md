# E73.193 results - balanced ramp

Command:

```text
python3 E73_193_balanced_ramp_probe.py
```

Output:

```text
E73.193 balanced ramp
Builds r*=r0+c r1 with F[r*]=0 and checks F[B]=F[Bbal].
 lam     L gamma row F0B F1B cAbsB totalB balB errB bal0B balp0B balLB
  12   4.970   14.13   0  -1.83  -2.08   0.25  -20.85 -20.85 -430.82  -22.98  -19.13 -21.48
  12   4.970   14.13   1  -1.83  -2.08   0.25  -21.09 -21.09 -430.82  -24.09  -19.13 -22.05
  12   4.970   21.02   0  -1.83  -2.08   0.25  -20.40 -20.40 -430.82  -23.77  -19.31 -22.91
  12   4.970   21.02   1  -1.83  -2.08   0.25  -19.87 -19.87 -430.82  -24.43  -19.31 -23.19
  16   5.545   14.13   0  -1.90  -1.83  -0.07  -19.19 -19.19 -403.27  -21.11  -18.39 -19.72
  16   5.545   14.13   1  -1.90  -1.83  -0.07  -19.98 -19.98 -403.27  -21.68  -18.39 -20.08
  16   5.545   21.02   0  -1.90  -1.83  -0.07  -18.18 -18.18 -403.27  -21.47  -18.16 -20.75
  16   5.545   21.02   1  -1.90  -1.83  -0.07  -19.03 -19.03 -403.27  -22.27  -18.16 -20.37
  20   5.991   14.13   0  -1.75  -2.27   0.52  -19.09 -19.09 -385.84  -19.96  -18.72 -19.76
  20   5.991   14.13   1  -1.75  -2.27   0.52  -18.56 -18.56 -385.84  -19.91  -18.41 -19.27
  20   5.991   21.02   0  -1.75  -2.27   0.52  -17.65 -17.65 -385.84  -21.48  -17.06 -18.91
  20   5.991   21.02   1  -1.75  -2.27   0.52  -17.76 -17.76 -385.84  -23.10  -17.06 -19.50
```

Reading:

```text
F_L[r_0] and F_L[r_1] are ordinary nonzero scalar quantities.
The balancing coefficient c=-F[r_0]/F[r_1] is moderate.
F[B_bal]=F[B] to arithmetic precision because F[r_*]=0.
Endpoint values remain zero to endpoint precision.
The displayed finite-difference derivative of B_bal is not a proof object;
the derivative cancellation is exact algebraically and should be handled by
symbolic/Taylor coefficients in the proof.
```

Conclusion:

```text
The proof-facing packet can now be taken to satisfy

B(0)=0,      B'(0)=0,      B(L)=0,

without changing the model-prime functional F_L[B].
```

This removes the bad rank-one split found in E73.192.
