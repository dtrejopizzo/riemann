# E73.128 Results - Phi Root-Proximity Probe

Date: 2026-07-12.

Script:

```text
E73_128_phi_root_proximity_probe.py
```

Purpose:

Test whether characteristic CSV is merely a consequence of finite roots of
`Phi_N` lying very close to the critical ordinates:

```text
Phi_N(-gamma) ~= Phi_N'(root) * dist(-gamma,root).
```

Output:

```text
E73.128 Phi root-proximity probe
Tests Phi(-gamma) ~= Phi'(root)*(distance to nearest Cauchy root).
 lam     L gamma      rootDistB    phiB  phiPrimeB predictedB ratio
  16   5.545   14.13    -19.423 -20.630     -1.124    -20.547   0.868
  16   5.545   21.02    -17.675 -20.107     -2.423    -20.098   0.985
  16   5.545   25.01      0.808 -15.240     -2.423     -1.615   0.000
  20   5.991   14.13    -18.072 -19.440      0.162    -17.910   0.065
  20   5.991   21.02    -18.197 -19.911     -1.691    -19.887   0.958
  20   5.991   25.01    -16.410 -19.848     -3.448    -19.857   1.018
  24   6.356   14.13    -16.583 -19.101     -2.515    -19.098   0.995
  24   6.356   21.02       -inf -19.366     -0.527       -inf huge
  24   6.356   25.01    -17.240 -20.031     -1.567    -18.807   0.104
  28   6.664   14.13       -inf -19.276     -0.821       -inf huge
  28   6.664   21.02      0.392 -17.775     -0.941     -0.548   0.000
  28   6.664   25.01    -16.515 -18.261      0.069    -16.446   0.032
  32   6.931   14.13    -17.543 -18.747     -0.688    -18.231   0.368
  32   6.931   21.02       -inf -18.510     -0.393       -inf huge
  32   6.931   25.01      0.176 -17.693     -0.764     -0.588   0.000
```

## Reading

Root proximity explains some rows:

```text
ratio ~= 1
```

for several entries, especially low `lambda` and some locked rows.

But it does not explain all rows.  There are rows where the nearest-root
distance is order one, while `Phi_N(-gamma)` remains about `L^-17`.

Therefore characteristic CSV is not equivalent to finite root locking.
Root locking is one mechanism, but the uniform theorem must prove the
small value directly.

## Correct target after E73.128

Do not reduce CSV to:

```text
dist(-gamma, zero(Phi_N)) small.
```

The viable target is:

```text
Characteristic Interpolation CSV:
Phi_N(-gamma) is small at the critical ordinates,
regardless of whether a nearby finite root accounts for it.
```

This preserves the E71 connection but stays weaker than global convergence:
only interpolation values at the Phase 73 critical rows are needed.

