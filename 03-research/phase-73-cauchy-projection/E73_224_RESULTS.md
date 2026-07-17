# E73.224 results - weight amplification budget

Command:

```text
python3 E73_224_weight_amplification_budget.py
```

Output:

```text
E73.224 weight amplification budget
Uses W,V centers to measure sum |W|rad(c)+sum |V|rad(l).
 lam     L    N Csec gamma row maxWB maxVB sumWradCB sumVradLB totalB centerB ratio
   8   4.159    6    1   14.13   0  -0.43  -1.18    -56.07    -57.71  -56.01  -21.68  5.6e-22
   8   4.159    6  1e6   14.13   0  -0.43  -1.18    -46.38    -48.02  -46.32  -21.68  5.6e-16
  10   4.605    8    1   14.13   0   0.09   0.71    -51.65    -51.95  -51.33  -18.50  1.7e-22
  10   4.605    8  1e6   14.13   0   0.09   0.71    -42.60    -42.90  -42.28  -18.50  1.7e-16
  12   4.970   10    1   14.13   0  -0.01   0.55    -49.26    -49.84  -49.05  -20.62  1.6e-20
  12   4.970   10  1e6   14.13   0  -0.01   0.55    -40.65    -41.23  -40.44  -20.62  1.6e-14
```

Representative rows are shown; the script checks both Cauchy rows and both
heights for all listed windows.

Interpretation:

The exact closed-center weights do not turn the certified coefficient balls
into a large scalar radius.  The remaining center interval task is the weight
radius itself.
