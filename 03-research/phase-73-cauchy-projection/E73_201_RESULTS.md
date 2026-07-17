# E73.201 results - multiprecision finite assembly

Command:

```text
python3 E73_201_mp_finite_assembly_probe.py
```

Output:

```text
E73.201 multiprecision finite assembly
Compares double and mp assembly of the same finite-frequency certificate.
 lam     L gamma row doubleB mpB dbl-mpB matrix-mpB
  12   4.970   14.13   0  -20.73  -21.29   -21.05     -21.28
  12   4.970   14.13   1  -20.78  -21.18   -21.25     -22.34
  12   4.970   21.02   0  -20.45  -20.43   -22.58     -22.29
  12   4.970   21.02   1  -19.88  -19.87   -22.55     -23.17
  16   5.545   14.13   0  -18.68  -18.95   -19.25     -19.60
  16   5.545   14.13   1  -20.01  -20.03   -21.92     -19.60
  16   5.545   21.02   0  -18.21  -18.21   -22.03     -20.00
  16   5.545   21.02   1  -19.11  -19.13   -21.28     -20.15
  20   5.991   14.13   0  -18.52  -18.43   -18.09     -18.28
  20   5.991   14.13   1  -18.55  -18.31   -18.03     -18.03
  20   5.991   21.02   0  -18.28  -18.24   -19.75     -17.89
  20   5.991   21.02   1  -18.45  -19.06   -18.67     -17.71
```


Reading:

```text
Multiprecision assembly changes several final certificates exactly at the
E73.199 residual scale.  This confirms the E73.200 diagnosis: the finite
formula is correct, but the residual is obtained after severe cancellation of
larger archimedean and prime terms.

The next certificate cannot merely intervalize the digamma tail.  It must
intervalize the whole finite object: eigenline xi, Cauchy projection eta,
packet coefficients, prime samples, finite WR head, and digamma tail.
```
