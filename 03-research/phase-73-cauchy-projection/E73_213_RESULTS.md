# E73.213 results - BALL-ENTRY-CERT v0

Command:

```text
python3 E73_213_ball_entry_cert_probe.py
```

Output:

```text
E73.213 BALL-ENTRY-CERT v0
Checks component entry radii against E73.209 per-entry targets.
 lam     L    N  dim targetB maxTotB maxPsiB maxRndB maxExpB slack
   8   4.159    6   13   -56.26   -67.62   -67.62  -120.20  -468.34  1.08e+07 worst=(0, 0)
  10   4.605    8   17   -51.93   -63.11   -63.11  -111.99  -452.32  2.60e+07 worst=(0, 0)
  12   4.970   10   21   -48.94   -60.11   -60.11  -106.48  -430.82  6.01e+07 worst=(0, 0)
```


Reading:

```text
BALL-ENTRY-CERT v0 passes the per-entry target in all tested windows.  The
worst entry is (0,0), and the total radius is dominated by the Bernoulli
psi/psi_1 tail, still about 10^7 below target.  Finite elementary rounding and
exponential corrections are far smaller.

Thus the finite entry certificate is quantitatively closed modulo replacing
the rounding audit by actual outward-rounded ball arithmetic.  The dominant
component is already analytic and explicitly bounded.
```

Extra stress with extrapolated targets:

```text
extra BALL-ENTRY-CERT stress
 lam L N dim targetB maxTotB maxPsiB maxRndB slack worst
  16   5.545  12  25  -46.00   -56.27   -56.27   -99.41  4.35e+07 (0, 0)
  20   5.991  14  29  -44.00   -53.84   -53.84   -94.89  4.44e+07 (0, 0)
```

The same structural pattern persists: the diagonal zero-frequency entry `(0,0)`
dominates, and the finite rounding audit remains far below the special-function
radius.
