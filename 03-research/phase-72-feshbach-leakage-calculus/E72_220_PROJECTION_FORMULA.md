# E72.220 - Projection formula for raw HS

## Purpose

E72.219 uses the raw compressed overlap

```text
||B_x^*U_yB_x||_HS^2.
```

This note removes the SVD basis `B_x` from the formula. Let:

```text
E = projection to the even sector,
k = model ground vector,
P = E - kk^*.
```

Since `B_x` is an orthonormal basis for `Ran(P)`,

```text
||B_x^*U_yB_x||_HS^2
 =
Tr(P U_y^* P U_y P).                              (PROJ)
```

## Diagnostic

Script:

```text
E72_220_projection_formula_probe.py
```

Output excerpt:

```text
E72.220 projection formula probe
checks ||B*UB||_HS^2 = Tr(P U* P U P), P=E-kk*
lam u direct proj relErr fullEven removed kk leak
 12 0.10 1.424944248e+01 1.424944248e+01 7.48e-16 1.481915250e+01 5.697100217e-01 2.113e-01 3.584e-01
 12 0.25 1.186581150e+01 1.186581150e+01 4.49e-16 1.246860735e+01 6.027958482e-01 1.018e-03 6.018e-01
 12 0.50 7.750712259e+00 7.750712259e+00 8.02e-16 8.250000000e+00 4.992877413e-01 7.123e-04 4.986e-01
 16 0.50 9.812423875e+00 9.812423875e+00 7.24e-16 1.025000000e+01 4.375761252e-01 6.242e-02 3.752e-01
 20 0.50 1.178906027e+01 1.178906027e+01 1.66e-15 1.225000000e+01 4.609397283e-01 3.906e-02 4.219e-01
 24 0.50 1.375208691e+01 1.375208691e+01 5.17e-16 1.425000000e+01 4.979130913e-01 2.087e-03 4.958e-01
```

## Reading

The identity `(PROJ)` holds to roundoff.

Moreover:

```text
||B_x^*U_yB_x||_HS^2
 =
||E U_y E||_HS^2 - removed_k(y),
```

where `removed_k(y)>=0` in the tested samples. Therefore

```text
||B_x^*U_yB_x||_HS^2 <= ||E U_y E||_HS^2.
```

This reduces the raw HS problem to an even-sector finite Fourier overlap plus a positive ground-line
removal.

## Consequence

The next estimate is the even-sector overlap:

```text
||E U_y E||_HS^2.
```

If this has a closed upper bound of size `L^2 Phi(y/L)`, then `Rraw_j` follows without using the
model ground vector `k` at all.
