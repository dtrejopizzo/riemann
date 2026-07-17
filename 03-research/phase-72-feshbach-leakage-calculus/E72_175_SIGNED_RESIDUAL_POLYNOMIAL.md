# E72.175 -- Signed residual polynomial gate

**Date:** 2026-07-09.
**Role:** remove the `cross_+` correction by approximating the signed residual itself.

## 0. Signed residual function

For the fixed weights:

```text
a_0=0.70,
a_1=0.60,
```

define the scalar signed residual function:

```text
f_a(t)=t                  for t<0,
f_a(t)=(1-a)t             for t>=0.
```

Then the exact F2B residual is:

```text
R=f_{a_0}(K_0)+f_{a_1}(K_1).
```

This identity packages all sign pieces at once:

```text
f_a(K)=(1-a)K^+ + K^-.
```

## 1. Polynomial replacement

Choose degree-28 polynomials `g_0,g_1` such that:

```text
|g_0(t)-f_{a_0}(t)| <= eps_0    on [-0.90,0.90],
|g_1(t)-f_{a_1}(t)| <= eps_1    on [-0.60,0.60].
```

If:

```text
||K_0||<=0.90,
||K_1||<=0.60,
```

then functional calculus gives:

```text
||f_{a_j}(K_j)-g_j(K_j)||_op <= eps_j.
```

Therefore, in dimension `d`:

```text
||R||_HS
 <= ||g_0(K_0)+g_1(K_1)||_HS + sqrt(d)(eps_0+eps_1).       (SRP)
```

So `F2B-PSD` follows from:

```text
||g_0(K_0)+g_1(K_1)||_HS + sqrt(d)(eps_0+eps_1) < 1.
```

No `cross_+` term appears.

## 2. Diagnostic output

The companion script:

```text
E72_175_signed_residual_polynomial_probe.py
```

reports:

```text
E72.175 signed residual polynomial probe
degree=28; intervals K0=[-0.9,0.9], K1=[-0.6,0.6]
uniform_errors err0=6.802e-03, err1=3.887e-03
 lam    L  dim  exactR  polyR  errHS  bound  margin  pass
  12  4.97   32   0.920  0.924  0.060  0.984   0.031 YES
  14  5.28   36   0.885  0.888  0.064  0.952   0.093 YES
  16  5.55   40   0.863  0.867  0.068  0.934   0.127 YES
  18  5.78   44   0.833  0.836  0.071  0.907   0.177 YES
  20  5.99   48   0.843  0.846  0.074  0.920   0.154 YES
  22  6.18   52   0.859  0.861  0.077  0.938   0.120 YES
  24  6.36   56   0.845  0.847  0.080  0.927   0.140 YES
worst_bound=0.984 at lambda=12
```

## 3. Consequence

`SRP` is stronger and cleaner than `PTC`:

```text
SRP => F2B-PSD
```

directly, while `PTC` needed the auxiliary `cross_+` correction.

The stable arithmetic route can now be restated as:

```text
Finite-F2B for lambda=6,8,10,
Stable-SRP for lambda>=12.
```

This is the current best Phase 72 arithmetic gate.
