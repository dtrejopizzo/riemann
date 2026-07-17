# E72.215 - Resonant bound budget

## Purpose

E72.210--E72.214 reduce the resonant pair energy to a geometric envelope and a prime-square weighted
sum. This note measures which envelope constants are strong enough.

The exact energy is:

```text
Actual = 2 sum beta_n^2 Geom_x(log n).
```

The coercive profiled bound is:

```text
Coercive = 2 sum beta_n^2 ||B_x^*U_{log n}B_x||_HS^2 / lambda_min(C_x)^2.
```

A flat envelope would give:

```text
Flat(K)=2K L^(-2) sum beta_n^2.
```

## Diagnostic

Script:

```text
E72_215_resonant_bound_budget_probe.py
```

Output:

```text
E72.215 resonant bound budget probe
actual=2sum beta2*geom; coercive=2sum beta2*raw/minC^2
univ(K)=2*K/L^2 sum beta2 with K=3,6,12
lam block actual coercive ratio K3 K6 K12 beta2sum
 12     0 7.506459e-01 1.279065e+00 1.70 9.724551e-01 1.944910e+00 3.889820e+00 4.003118e+00
 12     1 3.723544e-01 6.376446e-01 1.71 1.738249e+00 3.476499e+00 6.952997e+00 7.155516e+00
 16     0 5.903247e-01 9.516911e-01 1.61 8.934694e-01 1.786939e+00 3.573878e+00 4.578881e+00
 16     1 3.676131e-01 5.959258e-01 1.62 1.851305e+00 3.702609e+00 7.405219e+00 9.487625e+00
 20     0 5.066864e-01 7.486171e-01 1.48 8.967629e-01 1.793526e+00 3.587052e+00 5.365280e+00
 20     1 3.181675e-01 4.727129e-01 1.49 1.881354e+00 3.762709e+00 7.525418e+00 1.125603e+01
 24     0 4.667205e-01 6.566820e-01 1.41 9.479716e-01 1.895943e+00 3.791887e+00 6.383026e+00
 24     1 2.615648e-01 3.715143e-01 1.42 1.842227e+00 3.684454e+00 7.368908e+00 1.240436e+01
 28     0 4.259593e-01 5.783996e-01 1.36 9.555180e-01 1.911036e+00 3.822072e+00 7.073118e+00
 28     1 2.487475e-01 3.408709e-01 1.37 1.856690e+00 3.713380e+00 7.426759e+00 1.374394e+01
```

## Reading

The profiled coercive bound is good:

```text
Coercive / Actual ~= 1.36--1.71.
```

The flat envelope is not good enough for sharp budgets, especially in the high block. Even `K=3` gives
high-block bounds around `1.8` while the actual high-block resonant energy is around `0.25--0.37`.

Thus the proof must retain the decreasing profile:

```text
Geom_x(y) <= L^(-2) K Phi(y/L),
```

not merely a flat `K L^(-2)` bound.

## Consequence

The resonant sublemma should be stated with a profiled weight:

```text
Res_2(S_j)
<= 2K L^(-2)
   sum_{n in S_j(x)} (Lambda(n)^2/n) Phi(log n/L).
```

The high block is won because `Phi(u)` is small for `u>0.60`, not because
`sum_{n in S_1} Lambda(n)^2/n` is small.

## Status

Positive, with a constraint:

```text
profiled envelope required;
flat envelope too coarse for the high block.
```
