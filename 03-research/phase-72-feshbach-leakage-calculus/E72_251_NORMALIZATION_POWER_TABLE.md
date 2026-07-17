# E72.251 - Normalization power table

## Purpose

This note freezes the current normalizations and audits the powers of `L`.

## Diagnostic

Script:

```text
E72_251_normalization_power_table.py
```

Output:

```text
E72.251 normalization/power table
All quantities use model-relative compression. tailFull=||D||op(TrD2+3||C||HS2).
lam L dim minC minC/L minC/L2 tB tB*L sB sB*L low low*L low*L2 tailFull tail*L tail*L2
 12 4.969813  32 7.526496e+00 1.514442e+00 3.047282e-01 -2.018045e-01 -1.002931e+00 4.716908e-02 2.344215e-01 1.094348e-02 5.438707e-02 2.702936e-01 7.593378e-03 3.773767e-02 1.875492e-01
 16 5.545177  40 1.060517e+01 1.912504e+00 3.448949e-01 -1.908920e-01 -1.058530e+00 4.745727e-02 2.631590e-01 1.022382e-02 5.669288e-02 3.143721e-01 6.002100e-03 3.328271e-02 1.845585e-01
 20 5.991465  48 1.419980e+01 2.370005e+00 3.955635e-01 -2.119065e-01 -1.269630e+00 4.919967e-02 2.947781e-01 1.124246e-02 6.735880e-02 4.035778e-01 4.826362e-03 2.891697e-02 1.732550e-01
 24 6.356108  56 1.775109e+01 2.792762e+00 4.393824e-01 -2.375759e-01 -1.510058e+00 6.369185e-02 4.048322e-01 1.636695e-02 1.040301e-01 6.612265e-01 4.250174e-03 2.701456e-02 1.717075e-01
 28 6.664409  64 2.126345e+01 3.190598e+00 4.787518e-01 -2.162864e-01 -1.441421e+00 5.773067e-02 3.847408e-01 1.386423e-02 9.239691e-02 6.157708e-01 3.962054e-03 2.640475e-02 1.759720e-01
 32 6.931472  72 2.584119e+01 3.728096e+00 5.378506e-01 -1.153524e-01 -7.995621e-01 1.627185e-02 1.127879e-01 2.622823e-03 1.818002e-02 1.260143e-01 3.211498e-03 2.226041e-02 1.542974e-01
 36 7.167038  80 2.841766e+01 3.965049e+00 5.532340e-01 -2.388454e-01 -1.711814e+00 6.387046e-02 4.577620e-01 1.636806e-02 1.173105e-01 8.407687e-01 2.139203e-03 1.533175e-02 1.098832e-01
```

## Reading

In the current model-relative normalization:

```text
lambda_min(C_model) ~ L^2.
```

The column `minC/L2` is the stable one, rising toward `0.55` in the tested range.

The low block does not yet show a clean monotone power because the arithmetic sampling has finite
dips, especially at `lambda=32`. The right statement is therefore not just:

```text
lowMargin >= c/L.
```

It should be stated through the kernel-average mechanism of E72.245--E72.246, with finite exceptional
windows.

The nonspectral tail is smaller and smoother. The columns `tail*L` and `tail*L2` suggest that a
`O(L^-2)` or better bound may be available after the model Green estimates are proved.

## Corrected Normalization Table

```text
object                         current scale / status
C_model minimum                 ~ L^2
G=C_model^{-1}                  ~ L^-2 on the complement floor
t_B                             order 1/L, with arithmetic dips
s_B                             order 1/L, with arithmetic dips
lowMargin                       kernel-average controlled, not pure power yet
tailFull                        smoother; compatible with <= C/L^2 in tested range
HOC3 finite proof               lowMargin > tail, with lambda=32 exceptional
```

## Consequence

Future statements should not mix `C_model>=cL I` with the current relative-complement normalization.
For the objects used in E72.210--E72.251, the working coercivity target is:

```text
lambda_min(C_model) >= c_C L^2.
```
