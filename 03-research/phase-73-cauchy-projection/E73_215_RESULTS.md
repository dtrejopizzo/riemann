# E73.215 results - native ball entry certificate

Command:

```text
python3 E73_215_native_ball_entry_probe.py
```

Output:

```text
E73.215 native ball entry certificate
Propagates complex-ball radii for finite elementary entry pieces.
 lam     L    N  dim targetB maxTotB maxBallB maxPsiB maxExpB slack
   8   4.159    6   13   -56.26   -67.62  -155.92   -67.62  -468.34  1.08e+07 worst=(0, 0)
  10   4.605    8   17   -51.93   -63.11  -145.20   -63.11  -452.32  2.60e+07 worst=(0, 0)
  12   4.970   10   21   -48.94   -60.11  -138.03   -60.11  -430.82  6.01e+07 worst=(0, 0)
```


Reading:

```text
The native complex-ball propagation closes the finite elementary component.
The ball radius for elementary terms is around L^-138--L^-156, far below the
per-entry target and far below the Bernoulli psi/psi_1 radius.  The total entry
radius is unchanged from E73.213 because it is dominated by the analytic
special-function tail.

Thus BALL-ENTRY-CERT is no longer dependent on the heuristic rounding model for
finite elementary sums.  The remaining formal item is the Bernoulli remainder
lemma/citation for psi and psi_1.
```


K=16 proof-facing rerun:

```text
E73.215 native ball entry certificate
Propagates complex-ball radii for finite elementary entry pieces; K=16 for psi tail.
 lam     L    N  dim targetB maxTotB maxBallB maxPsiB maxExpB slack
   8   4.159    6   13   -56.26   -83.97  -155.92   -83.97  -468.34  1.42e+17 worst=(0, 0)
  10   4.605    8   17   -51.93   -78.37  -145.20   -78.37  -452.32  3.43e+17 worst=(0, 0)
  12   4.970   10   21   -48.94   -74.65  -138.03   -74.65  -430.82  7.94e+17 worst=(0, 0)
```

Reading:

```text
With K=16 the entry certificate has sector-constant slack around 10^17.  This
is now the preferred proof-facing configuration.  The finite elementary ball
radius remains far smaller than the special-function radius; the worst entry is
still (0,0).
```
