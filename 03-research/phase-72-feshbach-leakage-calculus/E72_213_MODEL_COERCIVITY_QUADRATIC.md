# E72.213 - Quadratic model coercivity

## Purpose

E72.212 reduces the geometric envelope to two model estimates:

```text
MCOER2:   lambda_min(C_x) >= c_C L^2,
UHS:      ||B_x^*U_yB_x||_HS^2 <= C_U L^2 Phi(y/L).
```

This note audits the first estimate.

## Diagnostic

Script:

```text
E72_213_model_coercivity_quadratic_probe.py
```

Output:

```text
E72.213 model coercivity quadratic probe
tests lambda_min(C_model) scaling
lam L dim minC minC/L minC/L2 maxC cond
  6  3.58  37 2.614634e+00 7.296276e-01 2.036065e-01 7.084471e+00 2.710e+00
  8  4.16  49 4.124950e+00 9.918409e-01 2.384873e-01 1.056242e+01 2.561e+00
 10  4.61  57 5.622430e+00 1.220895e+00 2.651140e-01 1.231167e+01 2.190e+00
 12  4.97  65 7.526496e+00 1.514442e+00 3.047282e-01 2.092725e+01 2.780e+00
 16  5.55  81 1.060517e+01 1.912504e+00 3.448949e-01 2.711645e+01 2.557e+00
 20  5.99  97 1.419980e+01 2.370005e+00 3.955635e-01 3.629095e+01 2.556e+00
 24  6.36 113 1.775109e+01 2.792762e+00 4.393824e-01 4.632796e+01 2.610e+00
 28  6.66 129 2.126345e+01 3.190598e+00 4.787518e-01 4.476351e+01 2.105e+00
```

## Reading

The model complement has quadratic coercivity:

```text
lambda_min(C_x) / L^2 >= 0.20
```

through all tested windows, and the ratio improves with `lambda`.

The condition number remains small:

```text
cond(C_x) ~= 2--3.
```

So `C_x` behaves like a well-conditioned `L^2`-scale model operator on the even complement.

## Candidate lemma

The model coercivity lemma needed by E72.212 is:

```text
C_x >= c_C L^2 I
```

with any uniform `c_C < 0.20` in the tested range.

This is a purely archimedean/model statement, independent of primes and zeros.

## Status

Positive. `MCOER2` is a plausible closed analytic lemma.
