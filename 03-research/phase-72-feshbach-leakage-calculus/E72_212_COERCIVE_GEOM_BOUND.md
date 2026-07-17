# E72.212 - Coercive geometric bound

## Purpose

E72.211 identified the needed geometric envelope:

```text
Geom_x(y)=||C_x^(-1/2)B_x^*U_yB_xC_x^(-1/2)||_HS^2.
```

This note checks whether the envelope can be proved from elementary coercivity:

```text
C_x >= lambda_min(C_x) I.
```

Then

```text
Geom_x(y)
<= ||B_x^*U_yB_x||_HS^2 / lambda_min(C_x)^2.     (CGB)
```

## Diagnostic

Script:

```text
E72_212_coercive_geom_bound_probe.py
```

Output:

```text
E72.212 coercive geometric bound probe
compares Geom to rawHS/lambda_min(C)^2
lam L dim minC minC/L u Geom rawHS crudeBound ratio
 12  4.97  65 7.526e+00 1.514e+00 0.10 1.463e-01 1.425e+01 2.515e-01 1.72e+00
 12  4.97  65 7.526e+00 1.514e+00 0.25 1.221e-01 1.187e+01 2.095e-01 1.72e+00
 12  4.97  65 7.526e+00 1.514e+00 0.50 8.098e-02 7.751e+00 1.368e-01 1.69e+00
 12  4.97  65 7.526e+00 1.514e+00 0.75 3.778e-02 3.641e+00 6.427e-02 1.70e+00
 12  4.97  65 7.526e+00 1.514e+00 0.90 1.383e-02 1.380e+00 2.436e-02 1.76e+00
 16  5.55  81 1.061e+01 1.913e+00 0.10 9.813e-02 1.791e+01 1.593e-01 1.62e+00
 16  5.55  81 1.061e+01 1.913e+00 0.25 8.211e-02 1.497e+01 1.331e-01 1.62e+00
 16  5.55  81 1.061e+01 1.913e+00 0.50 5.471e-02 9.812e+00 8.725e-02 1.59e+00
 16  5.55  81 1.061e+01 1.913e+00 0.75 2.621e-02 4.769e+00 4.240e-02 1.62e+00
 16  5.55  81 1.061e+01 1.913e+00 0.90 9.953e-03 1.840e+00 1.636e-02 1.64e+00
 20  5.99  97 1.420e+01 2.370e+00 0.10 7.113e-02 2.130e+01 1.056e-01 1.48e+00
 20  5.99  97 1.420e+01 2.370e+00 0.25 5.998e-02 1.795e+01 8.903e-02 1.48e+00
 20  5.99  97 1.420e+01 2.370e+00 0.50 3.978e-02 1.179e+01 5.847e-02 1.47e+00
 20  5.99  97 1.420e+01 2.370e+00 0.75 1.911e-02 5.728e+00 2.841e-02 1.49e+00
 20  5.99  97 1.420e+01 2.370e+00 0.90 7.266e-03 2.199e+00 1.090e-02 1.50e+00
 24  6.36 113 1.775e+01 2.793e+00 0.10 5.672e-02 2.525e+01 8.012e-02 1.41e+00
 24  6.36 113 1.775e+01 2.793e+00 0.25 4.700e-02 2.086e+01 6.621e-02 1.41e+00
 24  6.36 113 1.775e+01 2.793e+00 0.50 3.117e-02 1.375e+01 4.364e-02 1.40e+00
 24  6.36 113 1.775e+01 2.793e+00 0.75 1.461e-02 6.529e+00 2.072e-02 1.42e+00
 24  6.36 113 1.775e+01 2.793e+00 0.90 5.193e-03 2.360e+00 7.489e-03 1.44e+00
```

## Reading

The crude coercive bound is surprisingly sharp:

```text
rawHS/lambda_min(C)^2 ~= (1.4--1.8) * Geom_x(y).
```

Therefore the geometric envelope does not require delicate spectral alignment. It can plausibly be
proved from two model estimates:

```text
MCOER2:   lambda_min(C_x) >= c_C L^2,
UHS:      ||B_x^*U_yB_x||_HS^2 <= C_U L^2 Phi(y/L).
```

Together these imply

```text
Geom_x(y) <= (C_U/c_C^2) L^(-2) Phi(y/L).
```

This is exactly the envelope needed by E72.211.

## Updated resonant-pair route

The resonant even degree-2 sublemma reduces to:

```text
1. prove MCOER2 for the model complement;
2. prove UHS for the compressed one-sided overlap;
3. sum (Lambda(n)^2/n)L^(-2)Phi(log n/L).
```

The arithmetic sum is a prime-square weighted Chebyshev/PNT estimate, not an RH-strength statement.

## Status

Positive. The model coercive route is viable for the resonant pair energy.
