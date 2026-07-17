# E73.142 Results - Two-Row Local Divisor Conditioning

Date: 2026-07-12.

Script:

```text
E73_142_local_divisor_condition_probe.py
```

Purpose:

Test whether the two coefficient rows in

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w)
```

can be inverted with only polynomial loss.

Output:

```text
 lam     L gamma        hsumB    condB     ampB   reconRel
  16   5.545   14.13    -19.855    3.012    1.256   7.16e-15
  16   5.545   21.02    -19.024    2.832    1.079   4.30e-16
  16   5.545   25.01    -13.443    2.681    1.786   1.73e-16
  20   5.991   14.13    -19.272    2.539    0.785   1.37e-16
  20   5.991   21.02    -18.304    2.983    2.309   1.95e-14
  20   5.991   25.01    -18.092    2.667    1.352   1.78e-17
  24   6.356   14.13    -17.575    2.490    0.851   8.19e-16
  24   6.356   21.02    -18.720    2.643    1.050   1.17e-14
  24   6.356   25.01    -19.505    2.560    0.919   2.46e-16
  28   6.664   14.13    -16.816    2.516    2.725   1.99e-16
  28   6.664   21.02    -16.916    2.780    1.138   6.80e-15
  28   6.664   25.01    -17.661    2.497    0.744   2.96e-16
  32   6.931   14.13    -18.078    2.545    0.810   4.65e-15
  32   6.931   21.02    -17.615    2.703    1.239   9.44e-15
  32   6.931   25.01    -17.311    2.615    0.880   1.94e-16
```

Here

```text
condB = log_L cond(M_L),
ampB  = log_L ||M_L^{-1}||.
```

## Reading

The two-row divisor matrix is not exponentially singular.  The observed
inverse loss is polynomial and stays below `L^3` in the tested rows.

Therefore an analytic theorem of the form

```text
|Pair_{z_j}^M(w)| + |TailPair_{z_j}^M(w)| <= C L^-20
```

is strong enough to force

```text
|H_0(w)|+|H_0(-w)| <= C L^-17.
```

This is the first local forcer that directly targets the Cauchy divisor
values rather than a cell residual multiplied by a tiny eigenvalue.
