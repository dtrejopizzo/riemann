# E72.216 - Explicit profile for the raw HS envelope

## Purpose

E72.215 shows that a flat envelope is too coarse. We need a decreasing profile `Phi(u)` for

```text
||B_x^*U_{uL}B_x||_HS^2 / L^2.
```

This note tests simple explicit candidates.

## Diagnostic

Script:

```text
E72_216_phi_profile_fit_probe.py
```

It searches for `K` such that

```text
rawHS(u)/L^2 <= K Phi(u)
```

on the grid `u in [0.02,0.98]` and windows `lambda=12,16,20,24,28`.

Output:

```text
E72.216 Phi profile fit probe
finds K such that rawHS/L^2 <= K Phi(u) on grid u in [0.02,0.98]
kind maxK at lam,u meanK
sqrt   0.7184 at 24,0.020 0.4391
linear 0.7257 at 24,0.020 0.6475
mix    0.7185 at 24,0.020 0.5264
quad   33.4658 at 28,0.980 2.6436

Recommended envelope check: rawHS/L^2 <= 0.75 sqrt(1-u)
violations count and worst slack
no violations
```

## Reading

The simple envelope

```text
||B_x^*U_{uL}B_x||_HS^2 <= 0.75 L^2 sqrt(1-u)       (UHS-sqrt)
```

has no violations on the tested grid.

The quadratic profile `(1-u)^2` is too aggressive near the endpoint. A linear profile also works with
similar worst constant, but `sqrt(1-u)` has a better average fit and is safer near `u=1`.

## Resonant consequence

Combining `UHS-sqrt` with model coercivity

```text
lambda_min(C_x) >= c_C L^2
```

gives

```text
Geom_x(uL) <= (0.75/c_C^2) L^(-2) sqrt(1-u).
```

Therefore

```text
Res_2(S_j)
<= (1.5/c_C^2) L^(-2)
   sum_{n in S_j(x)} (Lambda(n)^2/n) sqrt(1-log n/L).
```

This is now a fully explicit finite arithmetic-geometric bound.

## Status

Positive. The resonant pair route now has a concrete profile:

```text
Phi(u)=sqrt(1-u).
```
