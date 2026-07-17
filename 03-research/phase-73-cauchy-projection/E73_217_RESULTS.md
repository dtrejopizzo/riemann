# E73.217 results - bordered Krawczyk certificate

Command:

```text
python3 E73_217_bordered_krawczyk_cert.py
```

Output:

```text
E73.217 bordered Krawczyk certificate from BALL-ENTRY-CERT
Uses epsH = dim * max_entry_radius and verifies the Krawczyk inequality.
 lam     L    N  dim Csec expH_B stepB Y_B rhoB ratio maxEntryB worst
   8   4.159    6   13  1.0   -82.17 -140.78  26.01 -55.67  0.500    -83.97 (0, 0)
   8   4.159    6   13 1.0e+6   -72.48 -140.78  26.01 -45.98  0.500    -74.28 (0, 0)
  10   4.605    8   17  1.0   -76.51 -131.24  23.90 -52.16  0.500    -78.37 (0, 0)
  10   4.605    8   17 1.0e+6   -67.47 -131.24  23.90 -43.11  0.500    -69.32 (0, 0)
  12   4.970   10   21  1.0   -72.75 -125.40  22.44 -49.87  0.500    -74.65 (0, 0)
  12   4.970   10   21 1.0e+6   -64.13 -125.40  22.44 -41.26  0.500    -66.03 (0, 0)
```


Reading:

```text
The bordered Krawczyk inclusion closes using epsH supplied by BALL-ENTRY-CERT.
With C_sec=1 the eigenpair ball radii are around L^-50--L^-56.  Even after
inflating the Bernoulli sector constant to C_sec=10^6, the inclusion still
closes with radii around L^-41--L^-46.

Thus the finite eigenline certification step is no longer merely a budget: it
is executed by the current artifacts, modulo the formal Bernoulli remainder
lemma used in the entry balls.
```
