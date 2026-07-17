# E73.238 results - curvature weight quotient

Command:

```text
python3 E73_238_curvature_weight_quotient_probe.py
```

## 1. Output

```text
E73.238 curvature weight quotient
Checks original weights equal curvature quotient on admissible coefficients.
 lam      L gamma row centerB quotientB diffB fstarB BpB
  12    4.970  14.13   0   -21.26    -21.26 -430.82 -430.82  -10.41
  12    4.970  14.13   1   -21.15    -21.15 -430.82 -430.82  -10.41
  12    4.970  21.02   0   -20.43    -20.43 -430.82 -430.82  -10.59
  12    4.970  21.02   1   -19.87    -19.87 -430.82 -430.82  -10.59
  16    5.545  14.13   0   -18.85    -18.85 -403.27 -403.27   -9.78
  16    5.545  14.13   1   -20.07    -20.07 -403.27 -403.27   -9.78
  16    5.545  21.02   0   -18.21    -18.21 -403.27 -403.27   -9.55
  16    5.545  21.02   1   -19.12    -19.12 -403.27 -403.27   -9.55
  20    5.991  14.13   0   -18.46    -18.46 -385.84 -385.84  -11.10
  20    5.991  14.13   1   -18.36    -18.36 -385.84 -385.84  -11.10
  20    5.991  21.02   0   -18.23    -18.23 -385.84 -385.84   -9.54
  20    5.991  21.02   1   -18.80    -18.80 -385.84 -385.84   -9.54
```

## 2. Interpretation

The balanced-ramp quotient is exact at arithmetic floor:

```text
F_L[r_*]=0,
```

so the original coefficient/weight center equals the curvature quotient
center:

```text
sum c W + sum l V
=sum c U^bal + sum l Z^bal.
```

This probe is not a new decay estimate.  It confirms that the correct
second-Abel finite object is the same scalar center in quotient coordinates.

## 3. Consequence

The next theorem cannot be a generic estimate of `K_L`; E73.194 already showed
that route is numerically ill-conditioned and analytically too crude.  The
proof target is the signed finite pairing:

```text
< (c,l), (U^bal,Z^bal) > = O_M(L^-M),
```

using the special algebraic structure of the Cauchy-balanced coefficient
vector.

