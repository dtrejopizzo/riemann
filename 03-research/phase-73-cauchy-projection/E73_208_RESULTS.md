# E73.208 results - Krawczyk budget

Command:

```text
python3 E73_208_krawczyk_budget_probe.py
```

Output:

```text
E73.208 Krawczyk budget audit
Point high-precision center plus explicit radius inequality.
 lam     L    N  dim  stepB  YnormB  epsHmaxB   rhoB  ratio
   8   4.159    6   13 -140.78   26.01    -54.46 -27.47  0.500
  10   4.605    8   17 -131.24   23.90    -50.07 -25.26  0.500
  12   4.970   10   21 -125.40   22.44    -47.04 -23.74  0.500
```


Reading:

```text
The bordered Krawczyk audit has usable slack.  In the tested windows, an
operator-norm matrix radius around L^-47--L^-54 is still admissible.  This is
far above the 100-digit working precision used for the centers, so a rigorous
entry enclosure by finite WR head + digamma tail should have enough room.

The next load-bearing implementation is therefore not another spectral audit:
it is an outward-rounded bound proving ||[H]-H0||_op <= epsH below the displayed
budget.
```
