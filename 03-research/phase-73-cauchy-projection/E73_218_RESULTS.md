# E73.218 results - eta projection budget

Command:

```text
python3 E73_218_eta_projection_budget.py
```

Output:

```text
E73.218 Cauchy projection radius budget
Propagates certified eigenline radius through eta=(I-P_w)xi.
 lam     L    N  dim Csec gamma  ||I-P||B rhoXiB rhoEtaB
   8   4.159    6   13    1   14.13     0.00  -55.67   -55.67
   8   4.159    6   13    1   21.02     0.00  -55.67   -55.67
   8   4.159    6   13  1e6   14.13     0.00  -45.98   -45.98
   8   4.159    6   13  1e6   21.02     0.00  -45.98   -45.98
  10   4.605    8   17    1   14.13     0.00  -52.16   -52.16
  10   4.605    8   17    1   21.02     0.00  -52.16   -52.16
  10   4.605    8   17  1e6   14.13     0.00  -43.11   -43.11
  10   4.605    8   17  1e6   21.02     0.00  -43.11   -43.11
  12   4.970   10   21    1   14.13     0.00  -49.87   -49.87
  12   4.970   10   21    1   21.02     0.00  -49.87   -49.87
  12   4.970   10   21  1e6   14.13     0.00  -41.26   -41.26
  12   4.970   10   21  1e6   21.02     0.00  -41.26   -41.26
```

Interpretation:

```text
||I-P_w||=1
```

to displayed `L`-exponent accuracy in every tested window.  Thus the Cauchy
projection does not enlarge the certified eigenline ball:

```text
rho_eta <= rho_xi.
```

The chain now has a certified finite radius for the projected vector
`eta_w=(I-P_w)xi`.  The remaining local finite step is to propagate this ball
through the scalar `TRANS-CELL` functional.
