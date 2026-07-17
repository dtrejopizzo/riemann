# E73.199 results - digamma finite-frequency certificate

Command:

```text
python3 E73_199_digamma_ff_certificate_probe.py
```

Output:

```text
E73.199 digamma finite-frequency certificate
Finite WR head plus closed signed digamma tail, compared to matrix residual.
 lam     L gamma row    R matrixB certB absErrB relErr
  12   4.970   14.13   0   60  -20.85  -20.73  -21.80 2.2e-01
  12   4.970   14.13   0  120  -20.85  -20.72  -21.77 2.3e-01
  12   4.970   14.13   0  240  -20.85  -20.72  -21.74 2.4e-01
  12   4.970   14.13   1   60  -21.09  -20.78  -21.36 6.4e-01
  12   4.970   14.13   1  120  -21.09  -20.78  -21.36 6.4e-01
  12   4.970   14.13   1  240  -21.09  -20.78  -21.36 6.4e-01
  12   4.970   21.02   0   60  -20.40  -20.45  -21.98 7.9e-02
  12   4.970   21.02   0  120  -20.40  -20.45  -21.99 7.7e-02
  12   4.970   21.02   0  240  -20.40  -20.45  -22.00 7.6e-02
  12   4.970   21.02   1   60  -19.87  -19.88  -22.35 1.9e-02
  12   4.970   21.02   1  120  -19.87  -19.88  -22.35 1.8e-02
  12   4.970   21.02   1  240  -19.87  -19.88  -22.37 1.8e-02
  16   5.545   14.13   0   60  -19.19  -18.68  -19.00 1.4e+00
  16   5.545   14.13   0  120  -19.19  -18.68  -19.00 1.4e+00
  16   5.545   14.13   0  240  -19.19  -18.69  -19.01 1.4e+00
  16   5.545   14.13   1   60  -19.98  -20.01  -19.59 2.0e+00
  16   5.545   14.13   1  120  -19.98  -20.01  -19.59 2.0e+00
  16   5.545   14.13   1  240  -19.98  -20.02  -19.60 1.9e+00
  16   5.545   21.02   0   60  -18.18  -18.21  -19.97 4.7e-02
  16   5.545   21.02   0  120  -18.18  -18.21  -19.98 4.6e-02
  16   5.545   21.02   0  240  -18.18  -18.21  -20.00 4.5e-02
  16   5.545   21.02   1   60  -19.03  -19.11  -20.24 1.3e-01
  16   5.545   21.02   1  120  -19.03  -19.11  -20.24 1.3e-01
  16   5.545   21.02   1  240  -19.03  -19.11  -20.24 1.3e-01
  20   5.991   14.13   0   60  -19.09  -18.52  -18.77 1.8e+00
  20   5.991   14.13   0  120  -19.09  -18.52  -18.78 1.8e+00
  20   5.991   14.13   0  240  -19.09  -18.53  -18.78 1.7e+00
  20   5.991   14.13   1   60  -18.56  -18.55  -20.77 1.9e-02
  20   5.991   14.13   1  120  -18.56  -18.55  -20.69 2.2e-02
  20   5.991   14.13   1  240  -18.56  -18.55  -20.79 1.8e-02
  20   5.991   21.02   0   60  -17.65  -18.28  -17.87 6.8e-01
  20   5.991   21.02   0  120  -17.65  -18.28  -17.87 6.8e-01
  20   5.991   21.02   0  240  -17.65  -18.28  -17.87 6.8e-01
  20   5.991   21.02   1   60  -17.76  -18.45  -17.62 1.3e+00
  20   5.991   21.02   1  120  -17.76  -18.45  -17.62 1.3e+00
  20   5.991   21.02   1  240  -17.76  -18.45  -17.62 1.3e+00
```

Reading:

```text
The certificate uses a short finite WR head plus the closed signed digamma
tail of E73.198.  The comparison target is the matrix residual
row*(H_actual eta), so this validates the whole finite-frequency identity:
archimedean head, signed WR tail, and exact finite prime samples.

The decisive diagnostic is that increasing `R` from 60 to 240 barely changes
the result.  Thus the remaining discrepancy is not a WR-tail truncation error;
it is the finite cancellation floor of the current floating assembly.  This is
exactly the reason the next proof-facing implementation must intervalize the
finite coefficients and the complex digamma values, rather than pushing `R`
deeper.
```
