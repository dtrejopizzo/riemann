# E72.166 -- Residual sign-Gram decomposition

**Date:** 2026-07-09.
**Role:** expose the internal geometry of the fixed `F2B-PSD` residual.

## 0. Exact decomposition

For the fixed certificate:

```text
K_rel=K_0+K_1,
P_j=(K_j)^+,
a=0.70,
b=0.60,
```

the residual is:

```text
R=K_rel-aP_0-bP_1
 =(1-a)P_0+K_0^-+(1-b)P_1+K_1^-.
```

Thus:

```text
||R||_HS^2 = diagonal sign energy + cross sign energy.
```

This is an exact identity, not a fit.

## 1. Diagnostic output

The companion script:

```text
E72_166_residual_sign_gram_probe.py
```

reports:

```text
E72.166 residual sign-Gram probe
cut=0.60, a=0.70, b=0.60
 lam    L   dist  diagE  crossE  cancel  ||r0p|| ||n0|| ||r1p|| ||n1||  minCos maxCos
   6  3.58  0.962  1.204  -0.278   0.231   0.350  0.733   0.184  0.715  -0.557  0.222
   8  4.16  0.967  1.024  -0.089   0.087   0.285  0.748   0.201  0.586  -0.466  0.330
  10  4.61  0.889  0.975  -0.186   0.190   0.293  0.655   0.179  0.655  -0.518  0.301
  12  4.97  0.920  0.898  -0.052   0.058   0.266  0.703   0.160  0.554  -0.484  0.262
  14  5.28  0.885  0.843  -0.061   0.072   0.257  0.667   0.157  0.554  -0.505  0.258
  16  5.55  0.863  0.794  -0.049   0.062   0.240  0.632   0.159  0.558  -0.500  0.301
  18  5.78  0.833  0.660   0.034  -0.051   0.221  0.631   0.145  0.438  -0.494  0.284
  20  5.99  0.843  0.735  -0.025   0.034   0.226  0.593   0.144  0.558  -0.460  0.304
```

Additional larger-window rows:

```text
lambda=22: dist=0.859, diagE=0.759, crossE=-0.020
lambda=24: dist=0.845, diagE=0.740, crossE=-0.026
```

## 2. Structural reading

The first two windows still use cross-sign cancellation to stay below `1`. From `lambda=10` onward,
the diagonal sign energy is already below `1` before using cancellation:

```text
diagE < 1.
```

Therefore the asymptotic proof target is simpler than the original certificate:

```text
||(1-a)P_0||_HS^2 + ||K_0^-||_HS^2
+ ||(1-b)P_1||_HS^2 + ||K_1^-||_HS^2 <= 1-epsilon
```

for large `x`, plus a finite check for the initial windows. The residual no longer has to be proved
small by delicate phase cancellation in the asymptotic range.

## 3. Consequence for the route

The fixed arithmetic gate can be split into:

```text
RSG-eventual: diagonal sign energy <= 1-epsilon for L>=L_0,
RSG-finite:   direct certificate for L<L_0.
```

Then:

```text
RSG-eventual + RSG-finite => F2B-PSD => PSD-DIST.
```

This is the first version of the arithmetic gate whose asymptotic part is a one-sided norm estimate
rather than a cancellation identity.
