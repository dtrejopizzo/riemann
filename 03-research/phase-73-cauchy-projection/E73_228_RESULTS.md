# E73.228 results - total scalar interval ledger

Command:

```text
python3 E73_228_total_scalar_interval_ledger.py
```

Output:

```text
E73.228 total scalar interval ledger
Combines R_etaH + R_coeff + R_weight around the closed center.
 lam     L    N Csec gamma row centerB RetaHB RcoeffB RweightB RtotalB ratio dominant
   8   4.159    6    1   14.13   0  -21.68  -57.20   -56.01   -85.91   -55.89  6.7e-22 coeff
   8   4.159    6  1e6   14.13   0  -21.68  -47.51   -46.32   -76.21   -46.20  6.6e-16 coeff
  10   4.605    8    1   14.13   0  -18.50  -53.06   -51.33   -79.25   -51.28  1.8e-22 coeff
  10   4.605    8  1e6   14.13   0  -18.50  -44.01   -42.28   -70.21   -42.23  1.8e-16 coeff
  12   4.970   10    1   14.13   0  -20.62  -50.53   -49.05   -75.79   -49.00  1.7e-20 coeff
  12   4.970   10  1e6   14.13   0  -20.62  -41.92   -40.44   -67.17   -40.39  1.7e-14 coeff
```

Representative rows are shown.  The command checks both Cauchy rows and both
heights for all listed windows.

Interpretation:

The complete scalar interval ledger is dominated by coefficient uncertainty
transported through weight centers.  The worst inflated-sector total ratio is
`1.7e-14`, so the finite local scalar interval has large margin.
