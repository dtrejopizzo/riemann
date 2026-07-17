# E72.218 - Observed-constant resonant closure audit

## Purpose

E72.216 proposed the convenient envelope

```text
||B_x^*U_{uL}B_x||_HS^2 <= 0.75 L^2 sqrt(1-u).
```

E72.217 showed that the resulting arithmetic coefficient is stable. This note tests whether that
envelope, combined with the observed coercivity constant

```text
c_obs=lambda_min(C_x)/L^2,
```

is sharp enough to close the resonant pair budget.

## Diagnostic

Script:

```text
E72_218_observed_constant_closure_probe.py
```

It computes:

```text
Bound = (1.5/c_obs^2)L^(-2)
        sum (Lambda(n)^2/n)sqrt(1-log n/L).
```

Output:

```text
E72.218 observed-constant resonant closure probe
bound = (1.5/c_obs^2) L^-2 Sphi, c_obs=lambda_min(C)/L^2
lam block actual bound ratio c_obs Sphi
 12     0 7.506459e-01 1.976920e+00 2.63 0.305 3.022758e+00
 12     1 3.723544e-01 1.834405e+00 4.93 0.305 2.804849e+00
 16     0 5.903247e-01 1.443150e+00 2.44 0.345 3.519044e+00
 16     1 3.676131e-01 1.573313e+00 4.28 0.345 3.836440e+00
 20     0 5.066864e-01 1.102371e+00 2.18 0.396 4.127954e+00
 20     1 3.181675e-01 1.213779e+00 3.81 0.396 4.545135e+00
 24     0 4.667205e-01 9.365039e-01 2.01 0.439 4.869519e+00
 24     1 2.615648e-01 9.537853e-01 3.65 0.439 4.959377e+00
 28     0 4.259593e-01 7.950808e-01 1.87 0.479 5.395902e+00
 28     1 2.487475e-01 8.074233e-01 3.25 0.479 5.479666e+00
```

## Reading

The convenient `0.75 sqrt(1-u)` profile has the right scale but not enough sharpness. Even using the
observed coercivity constant, the bound loses:

```text
block 0: about 1.9--2.6,
block 1: about 3.2--4.9.
```

This is much worse than the direct profiled coercive bound from E72.215, which loses only:

```text
1.36--1.71.
```

Therefore the proof cannot close the resonant budget with the soft square-root envelope alone.

## Consequence

The resonant proof needs one of the following sharper inputs:

```text
1. prove the near-sharp raw profile directly, not just 0.75 sqrt(1-u);
2. use the exact profiled coercive sum 2 sum beta_n^2 rawHS(log n)/lambda_min(C)^2;
3. improve coercivity by using directional information rather than lambda_min(C_x).
```

The most honest next target is option 2:

```text
sum_{n in S_j} (Lambda(n)^2/n)
||B_x^*U_{log n}B_x||_HS^2
```

with the exact raw HS profile, then divide by `lambda_min(C_x)^2`.

## Status

Useful no-go:

```text
soft sqrt profile is too loose for the resonant budget.
```

Kept:

```text
near-sharp profiled coercive route.
```
