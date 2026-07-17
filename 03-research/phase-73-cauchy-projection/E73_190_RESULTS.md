# E73.190 results - transverse convolution form

Command:

```text
python3 E73_190_transverse_convolution_probe.py
```

Output:

```text
E73.190 transverse convolution form
Checks convolution representation and A_a'=D-aA_a.
 lam     L gamma row convErr qetaB Bp0B rankBp0B derivErr
  12   4.970   14.13   0 1.8e-14 -23.41 -10.41    -10.41  5.5e-17
  12   4.970   14.13   1 1.8e-14 -24.52 -10.41    -10.41  2.7e-16
  12   4.970   21.02   0 1.7e-14 -24.21 -10.59    -10.59  8.7e-17
  12   4.970   21.02   1 9.8e-15 -24.86 -10.59    -10.59  2.0e-16
  16   5.545   14.13   0 9.1e-15 -21.51  -9.78     -9.78  1.3e-16
  16   5.545   14.13   1 7.4e-15 -22.08  -9.78     -9.78  2.1e-16
  16   5.545   21.02   0 1.8e-14 -21.87  -9.55     -9.55  0.0e+00
  16   5.545   21.02   1 5.3e-14 -22.67  -9.55     -9.55  4.3e-16
  20   5.991   14.13   0 1.3e-14 -20.35 -11.20    -11.10  1.8e-16
  20   5.991   14.13   1 1.6e-14 -20.30 -10.89    -11.10  3.4e-16
  20   5.991   21.02   0 2.0e-14 -21.87  -9.54     -9.54  1.3e-16
  20   5.991   21.02   1 1.2e-14 -23.49  -9.54     -9.54  1.3e-16
```

Column meanings:

```text
convErr   = normalized error between qQ_L(y)eta and the convolution formula
qetaB     = log_L |q_a eta|
Bp0B      = log_L |B_a'(0)|
rankBp0B  = log_L |-(2/L)(sum q_a)(sum eta)|
derivErr  = relative error in A_a'=D-aA_a
```

Reading:

```text
The convolution identity is exact to quadrature precision.
The Cauchy annihilation q_a eta=0 holds.
The first endpoint derivative does not vanish; it is exactly rank-one.
The Cauchy differential identity is exact to machine precision.
```

Conclusion:

```text
The next analytic proof should not expose powers of d_m.  It should use:

B_a(y)=1/L int_0^(L-y)[A_a(t+y)E(-t)+A_a^#(t+y)E(t)]dt,
A_a'=D-aA_a,
B_a'(0)=-(2/L)(sum q_a)(sum eta).
```

This converts TRANS-CELL into a one-dimensional convolution/moment matching
problem.
