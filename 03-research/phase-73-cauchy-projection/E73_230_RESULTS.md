# E73.230 results - closed scalar interval wrapper

Command:

```text
python3 E73_230_closed_scalar_interval_wrapper.py
```

Output:

```text
E73.230 closed scalar interval wrapper
Uses only the closed coefficient/weight representation: no matrix-route double counting.
 lam     L    N Csec gamma row centerB RcoeffB RweightB RprodB RclosedB ratio
   8   4.159    6    1   14.13   0  -21.68   -56.01   -85.91 -139.69   -56.01  5.6e-22
   8   4.159    6  1e6   14.13   0  -21.68   -46.32   -76.21 -120.31   -46.32  5.6e-16
  10   4.605    8    1   14.13   0  -18.50   -51.33   -79.25 -130.30   -51.33  1.7e-22
  10   4.605    8  1e6   14.13   0  -18.50   -42.28   -70.21 -112.20   -42.28  1.7e-16
  12   4.970   10    1   14.13   0  -20.62   -49.05   -75.79 -123.97   -49.05  1.6e-20
  12   4.970   10  1e6   14.13   0  -20.62   -40.44   -67.17 -106.75   -40.44  1.6e-14
```

Representative rows are shown.  The command checks both Cauchy rows and both
heights for all listed windows.

Interpretation:

The proof-facing closed scalar interval is dominated by coefficient uncertainty
and has worst tested ratio `1.6e-14` under `C_sec=1e6`.  No matrix-route radius
is added here, avoiding double counting of `eta` uncertainty.
