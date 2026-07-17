# E73.225 results - weight radius budget

Command:

```text
python3 E73_225_weight_radius_budget.py
```

Output:

```text
E73.225 weight radius budget
Estimates sum |c|rad(W)+sum |l|rad(V) using finite rounding plus Bernoulli tails.
 lam     L    N gamma row csec radWB radVB sumCradWB sumLradVB totalB centerScaleB ratio
   8   4.159    6   14.13   0  1.0  -84.48  -86.06     -85.92     -88.80  -85.91        -1.33  4.5e-53
   8   4.159    6   14.13   0 1.0e+6  -74.78  -76.37     -76.22     -79.11  -76.21        -1.33  4.5e-47
  10   4.605    8   14.13   0  1.0  -78.84  -80.32     -79.27     -81.79  -79.25        -0.30  4.3e-53
  10   4.605    8   14.13   0 1.0e+6  -69.79  -71.27     -70.22     -72.74  -70.21        -0.30  4.3e-47
  12   4.970   10   14.13   0  1.0  -75.09  -76.50     -75.80     -78.48  -75.79        -0.62  4.5e-53
  12   4.970   10   14.13   0 1.0e+6  -66.47  -67.88     -67.18     -69.86  -67.17        -0.62  4.5e-47
```

Representative rows are shown.  The script checks both Cauchy rows and both
heights in all listed windows.

Interpretation:

Weight radii are not the limiting finite uncertainty.  The dominant certified
finite uncertainty remains the eigenline/projection radius propagated in
E73.219.
