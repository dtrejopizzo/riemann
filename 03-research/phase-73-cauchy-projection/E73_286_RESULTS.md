# E73.286 results - weight derivative bridge probe

Command:

```bash
python3 /Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection/E73_286_weight_derivative_bridge_probe.py
```

Output:

```text
E73.286 weight derivative bridge probe
Tests V_omega=(1/i)dW/domega and discrete integration-by-parts explanation of c/l cancellation.
dErr is finite-difference error for V; divErr tests c+(1/i)D^*l as effective W coefficient.
 lam     L gamma row nfreq dErrB pairB ibpB ibpErrB divNormB divPairB cancel
  12   4.970   14.13   0    33   0.02 -20.93  -0.77    -0.77    -0.78    -0.77  5.3e-15
  12   4.970   14.13   1    33   0.02 -21.14  -0.99    -0.99    -0.98    -0.99  4.6e-15
  12   4.970   21.02   0    33   0.02 -20.45  -2.52    -2.52    -1.29    -2.52  2.9e-13
  12   4.970   21.02   1    33   0.02 -19.86  -2.63    -2.63    -1.44    -2.63  7.7e-13
  16   5.545   14.13   0    41   0.05 -20.05   0.18     0.18     0.09     0.18  6.6e-16
  16   5.545   14.13   1    41   0.05 -19.96  -1.12    -1.12    -0.80    -1.12  7.5e-15
  16   5.545   21.02   0    41   0.05 -18.20  -2.03    -2.03    -0.70    -2.03  1.4e-12
  16   5.545   21.02   1    41   0.05 -19.11  -1.40    -1.40    -1.30    -1.40  7.1e-14
  20   5.991   14.13   0    49   0.06 -18.66  -0.20    -0.20    -0.06    -0.20  4.3e-15
  20   5.991   14.13   1    49   0.06 -18.55   0.09     0.09     0.13     0.09  3.1e-15
  20   5.991   21.02   0    49   0.06 -17.96  -0.80    -0.80    -0.36    -0.80  2.9e-14
  20   5.991   21.02   1    49   0.06 -18.43  -0.64    -0.64    -0.21    -0.64  9.5e-15
```
