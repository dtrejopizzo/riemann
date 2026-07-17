# E73.016 results - triangular local action probe

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_016_triangular_action_probe.py
```

Output:

```text
E73.016 triangular local action probe
For rat r, tight=source orders <=r, tri=source orders <=r+1.
 lam     L   dim   block cols tightRank   tightRel   triRank     triRel  fullRank    fullRel
   8   4.159    25    rat0   15         9   3.40e-02        14   2.54e-04        15   1.68e-07
   8   4.159    25    rat1   15        14   4.65e-04        15   2.14e-07        15   2.16e-07
   8   4.159    25    rat2   15        15   1.23e-07        15   1.24e-07        15   1.24e-07
   8   4.159    25   poly1    5        16   3.46e-08        15   8.32e-08        15   8.32e-08
  10   4.605    29    rat0   15         9   3.73e-02        14   5.22e-04        16   1.25e-08
  10   4.605    29    rat1   15        14   9.03e-04        16   2.95e-07        16   1.13e-08
  10   4.605    29    rat2   15        16   1.69e-07        16   6.34e-09        16   6.34e-09
  10   4.605    29   poly1    5        18   8.49e-07        16   1.05e-08        16   1.05e-08
  12   4.970    33    rat0   15         9   2.78e-02        15   5.87e-04        17   6.90e-08
  12   4.970    33    rat1   15        15   4.67e-04        17   1.00e-06        17   6.37e-08
  12   4.970    33    rat2   15        17   9.25e-07        17   5.67e-08        17   5.67e-08
  12   4.970    33   poly1    5        18   2.82e-06        17   5.19e-08        17   5.19e-08
  14   5.278    37    rat0   15         9   1.15e-02        15   8.91e-04        17   3.46e-07
  14   5.278    37    rat1   15        15   1.05e-03        17   1.94e-05        17   3.45e-07
  14   5.278    37    rat2   15        17   1.68e-05        17   3.18e-07        17   3.18e-07
  14   5.278    37   poly1    5        19   3.70e-05        17   1.94e-07        17   1.94e-07
  16   5.545    41    rat0   15         9   1.84e-02        15   3.16e-03        17   4.49e-06
  16   5.545    41    rat1   15        15   1.23e-02        17   1.01e-03        17   1.64e-05
  16   5.545    41    rat2   15        17   2.89e-04        17   4.80e-06        17   4.80e-06
  16   5.545    41   poly1    5        19   7.40e-05        17   1.13e-06        17   1.13e-06
```

Interpretation:

```text
STRICT-TRI r->r+1 is not exact.
FINITE-WIDTH r->3 plus endpoint polynomial terms is stable.
```

The failure is concentrated in the lower rational blocks.  For `rat0`, source orders up to
`r+1=1` leave residuals in the `1e-4..1e-3` range, while the full finite source class
`r<=3` reduces the defect to `1e-8..1e-6`.  Thus the previous symbolic rule must be
weakened.

The corrected certificate target is:

```text
LOCAL-FIN:
(C_E-mu I) I_{O,K}^{DD}
subset S_{O,K}^{(3,endpoint)} + Phase72Residual,
```

where

```text
S_{O,K}^{(3,endpoint)}
= span{ DD_gamma(d)/(d^2+beta^2)^j : j=0,1,2,3 }
  + span{ d^2 DD_gamma(d), d^4 DD_gamma(d) }.
```

This is still finite and algebraic.  It is weaker than strict triangularity, but it is the
right load-bearing statement: the action does not generate an unbounded pole tower.
