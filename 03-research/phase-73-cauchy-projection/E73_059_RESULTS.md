# E73.059 results - FAR3 factor exponents

## 1. Purpose

E73.059 decomposes the FAR3 main terms into:

```text
T_k = prefactor_k * |C_x(-gamma_k)|,
```

where

```text
prefactor_k =
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|.
```

The goal is to identify which factor supplies the observed `L^-6` main budget.

## 2. Representative output

```text
E73.059 FAR3 factor exponent probe
 lam     L tau   gamma     prefB        cB     termB       pref       Cx       term
  16   5.545   14.13   37.59     4.217   -10.595    -6.378  1.372e+03 1.312e-08  1.800e-05
  16   5.545   14.13   32.94     3.602   -10.301    -6.699  4.782e+02 2.174e-08  1.039e-05
  18   5.781   14.13   30.42     2.280    -9.085    -6.805  5.464e+01 1.194e-07  6.526e-06
  20   5.991   14.13   37.59     4.046   -10.618    -6.572  1.400e+03 5.544e-09  7.763e-06
  24   6.356   14.13   37.59     2.919    -8.902    -5.983  2.212e+02 7.074e-08  1.565e-05
```

## 3. Diagnosis

The prefactor is not small:

```text
prefactor_k is roughly L^2 to L^4.5.
```

The main smallness comes from the finite Cauchy spectral defect:

```text
|C_x(-gamma_k)| is roughly L^-9 to L^-13 on FAR3 nodes.
```

Thus the main theorem should target the rational Cauchy values, not the Hermite-mesh geometry.

## 4. Consequence

A sufficient split for the FAR3 main budget is:

```text
PREF:
prefactor_k <= C_pref L^5 on FAR3 nodes;

CMAIN:
|C_x(-gamma_k)| <= C_cauchy L^-10 on FAR3 nodes.
```

Then each FAR3 main term satisfies:

```text
T_k <= C_pref C_cauchy L^-5.
```

Summing three nodes gives:

```text
Main_3 <= 3 C_pref C_cauchy L^-5.
```

This proves the `MAIN` half of `BUD-5/9`.

## 5. Status

```text
observed: geometry grows mildly;
observed: Cauchy rational values supply the divisibility;
next target: prove PREF + CMAIN.
```
