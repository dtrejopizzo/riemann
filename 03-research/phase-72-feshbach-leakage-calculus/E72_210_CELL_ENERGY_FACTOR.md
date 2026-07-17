# E72.210 - Cell energy factorization

## Purpose

E72.209 gives the resonant pair identity

```text
Res_2 = 2 sum_n ||A_n^+||_HS^2.
```

This note factors each cell into its arithmetic weight and a pure Feshbach-geometric factor.

For `n=p^m`, write

```text
beta_n = Lambda(n)n^(-1/2),       y_n=log n.
```

Since

```text
A_n^+ = - beta_n C_x^(-1/2)B_x^*U_{y_n}B_xC_x^(-1/2),
```

we have the exact factorization

```text
2||A_n^+||_HS^2
 =
2 (Lambda(n)^2/n) Geom_x(log n),                (CEF)
```

where

```text
Geom_x(y)=||C_x^(-1/2)B_x^*U_yB_xC_x^(-1/2)||_HS^2.
```

Thus

```text
Res_2(S_j)
 =
2 sum_{n in S_j(x)} (Lambda(n)^2/n) Geom_x(log n).
```

This is a finite zero-free local cell-energy identity.

## Diagnostic

Script:

```text
E72_210_cell_energy_factor_probe.py
```

Output:

```text
E72.210 cell energy factor probe
Res2 cell = 2 (Lambda(n)^2/n) * Geom_x(log n)
lam block cells Res2 beta2Sum geomMean geomMax topCell topFrac
 12     0    12 7.506459e-01 4.003118e+00 9.375764e-02 1.406718e-01    5@0.324 0.151
 12     1    35 3.723544e-01 7.155516e+00 2.601870e-02 5.757232e-02   23@0.631 0.132
 16     0    15 5.903247e-01 4.578881e+00 6.446168e-02 9.567751e-02    5@0.290 0.135
 16     1    55 3.676131e-01 9.487625e+00 1.937329e-02 4.157847e-02   29@0.607 0.088
 20     0    18 5.066864e-01 5.365280e+00 4.721901e-02 7.021695e-02    5@0.269 0.119
 20     1    79 3.181675e-01 1.125603e+01 1.413320e-02 3.099858e-02   37@0.603 0.069
 24     0    21 4.667205e-01 6.383026e+00 3.655951e-02 5.617104e-02    5@0.253 0.103
 24     1   105 2.615648e-01 1.240436e+01 1.054326e-02 2.393812e-02   47@0.606 0.058
```

Top cells for `lambda=24`:

```text
rank n y/L block beta2 geom cellRes fracTotal
 1    5 0.253 0 5.181e-01 4.655e-02 4.823e-02 0.066
 2    7 0.306 0 5.409e-01 4.317e-02 4.671e-02 0.064
 3    3 0.173 0 4.023e-01 5.179e-02 4.167e-02 0.057
 4   11 0.377 0 5.227e-01 3.872e-02 4.048e-02 0.056
 5   13 0.404 0 5.061e-01 3.700e-02 3.745e-02 0.051
 6   17 0.446 0 4.722e-01 3.446e-02 3.254e-02 0.045
 7   19 0.463 0 4.563e-01 3.369e-02 3.074e-02 0.042
 8   23 0.493 0 4.274e-01 3.157e-02 2.699e-02 0.037
 9    2 0.109 0 2.402e-01 5.617e-02 2.699e-02 0.037
10   29 0.530 0 3.910e-01 2.866e-02 2.241e-02 0.031
11   31 0.540 0 3.804e-01 2.798e-02 2.128e-02 0.029
12   37 0.568 0 3.524e-01 2.626e-02 1.851e-02 0.025
13   41 0.584 0 3.364e-01 2.518e-02 1.694e-02 0.023
14   43 0.592 0 3.290e-01 2.473e-02 1.627e-02 0.022
15   47 0.606 1 3.154e-01 2.394e-02 1.510e-02 0.021
16   53 0.625 1 2.974e-01 2.271e-02 1.351e-02 0.019
```

## Reading

The resonant pair energy is not dominated by one exceptional cell. The largest cell fraction drops
from about `15%` at `lambda=12` to about `6%` at `lambda=24`.

The geometric factor decreases across the window:

```text
Geom_x(y) is largest near the early cells and smaller in the high block.
```

The arithmetic weight sum `sum Lambda(n)^2/n` grows with the number of prime powers, but the average
geometric factor decreases. This balance is the mechanism behind the stable size of `Res_2`.

## Candidate local bound

The resonant even sublemma can now be stated as:

```text
2 sum_{n in S_j(x)} (Lambda(n)^2/n) Geom_x(log n) <= B_j(x),
```

with `B_j(x)` chosen from the LM8/NTC energy budget.

This is an explicit finite inequality with no zeros and no spectral projection. The remaining work is
to prove an analytic envelope for `Geom_x(y)` strong enough to sum against `Lambda(n)^2/n`.

## Status

Reduced:

```text
resonant pair energy -> weighted prime-square sum with geometric Feshbach envelope.
```

Open:

```text
prove a uniform envelope for Geom_x(y) and sum it over prime powers.
```
