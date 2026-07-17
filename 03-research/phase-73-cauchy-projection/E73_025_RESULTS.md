# E73.025 results - Pi Lebesgue cluster falsifier

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_025_pi_lebesgue_cluster_falsifier.py
```

Output:

```text
E73.025 Pi Lebesgue cluster falsifier
Shows PI-LEB needs node geometry; arbitrary positive-half-plane clusters can blow up.
   L   nO   sepScale       maxWeightedLebesgue
   5    3       0.00                5.667e+02
   5    3       0.50                8.603e+04
   5    3       1.00                1.277e+07
   5    3       1.50                1.896e+09
  10    3       0.00                1.541e+03
  10    3       0.50                3.473e+07
  10    3       1.00                7.653e+11
  10    3       1.50                4.250e+17
  15    3       0.00                4.188e+03
  15    3       0.50                1.401e+10
  15    3       1.00                1.155e+18
  15    3       1.50                7.539e+30
  20    3       0.00                1.138e+04
  20    3       0.50                5.655e+12
  20    3       1.00                2.702e+27
  20    3       1.50                3.407e+44
```

Conclusion:

```text
PI-LEB is false for arbitrary positive-half-plane off-line node clusters.
```

Any natural-height proof must include either:

```text
1. a node-geometry condition preventing exponentially tight off-line clusters;
2. a confluent/Hermite renormalization that absorbs cluster blow-up;
3. cancellation of g_cancelled data against the bad Cauchy directions.
```

Thus E73.024 is a valid sufficient split, but `PI-LEB-NH` is itself a serious finite theorem, not a
free geometric estimate.
