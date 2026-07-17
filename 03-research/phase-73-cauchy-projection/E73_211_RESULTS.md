# E73.211 results - elementary rounding budget

Command:

```text
python3 E73_211_rounding_budget_probe.py
```

Output:

```text
E73.211 elementary rounding budget
Heuristic outward-rounding digit budget for finite elementary sums.
 lam     L    N  dim digits maxRadB targetB slack maxOps
   8   4.159    6   13     80  -120.20   -56.26  3.77e+39    516
   8   4.159    6   13    100  -152.51   -56.26  3.77e+59    516
   8   4.159    6   13    120  -184.82   -56.26  3.77e+79    516
   8   4.159    6   13    140  -217.13   -56.26  3.77e+99    516
  10   4.605    8   17     80  -111.99   -51.93  6.82e+39    548
  10   4.605    8   17    100  -142.14   -51.93  6.82e+59    548
  10   4.605    8   17    120  -172.30   -51.93  6.82e+79    548
  10   4.605    8   17    140  -202.45   -51.93  6.82e+99    548
  12   4.970   10   21     80  -106.48   -48.94  1.17e+40    596
  12   4.970   10   21    100  -135.20   -48.94  1.17e+60    596
  12   4.970   10   21    120  -163.92   -48.94  1.17e+80    596
  12   4.970   10   21    140  -192.64   -48.94 1.17e+100    596
```


Reading:

```text
Finite elementary rounding is also not the bottleneck.  Even the crude audit
with 80 decimal digits gives roughly 40 orders of magnitude of slack relative
to the per-entry target.  Combined with E73.210, this indicates that the full
entry-radius certificate is feasible with ordinary high-precision ball
arithmetic.

The remaining implementation step is mechanical but load-bearing: replace the
heuristic rounding model by outward-rounded balls for elementary functions,
finite sums, and the Bernoulli-enclosed psi/psi_1 tail.
```
