# E72.121 -- Height-normalized CGE audit

**Date:** 2026-07-09.
**Role:** test and calibrate the natural height scale in the Cauchy graph-energy bound.

## 0. Motivation

E72.120 reduced `C-FIN` to:

```text
CGE:
Graph_x(s)=||Dg_{x,s}||^2/||g_{x,s}||^2=O_K(1)
```

on compact Cauchy windows.  Since the source:

```text
r_s^even(n)=s/(s^2-d_n^2)
```

is spectrally concentrated near physical height `|s|`, the first expected scale is:

```text
Graph_x(s) ~ |s|^2.
```

This note audits that expectation.

## 1. Height-normalized sufficient condition

For windows away from very low-height mesh effects, a natural strengthening of `CGE` is:

```text
HN-CGE:
Graph_x(s) <= C_K(1+|s|^2).                                (HN)
```

Clearly `(HN)` implies `CGE` on compact `K`.

More generally, the safe statement remains:

```text
Graph_x(s) <= C_K,
```

with `C_K` allowed to depend on the whole compact Cauchy window, including its imaginary height and
low physical heights.

## 2. Diagnostic

The companion script:

```text
E72_121_height_normalized_graph_probe.py
```

prints:

```text
Graph_x(s)/(1+|s|^2).
```

Representative output:

```text
E72.121 height-normalized graph energy probe
 lam   N      s   GraphE   Graph/(1+|s|^2)
  12  28    2.0 5.92e+01          1.174e+01
  12  28    5.0 2.82e+01          1.081e+00
  12  28   10.0 1.02e+02          1.008e+00
  12  28   15.0 2.29e+02          1.015e+00
  12  28   20.0 4.03e+02          1.006e+00
  24  48    2.0 9.50e+01          1.885e+01
  24  48    5.0 3.79e+01          1.454e+00
  24  48   10.0 1.01e+02          1.004e+00
  24  48   15.0 2.22e+02          9.811e-01
  24  48   20.0 3.93e+02          9.796e-01
```

The high physical heights follow the expected `|s|^2` law very closely.  The low-height channel can
have larger constants.  Therefore the correct theorem should be stated with a compact-window constant
`C_K`, not a universal height-normalized constant.

## 3. Updated interpretation of CGE

The current target is:

```text
For every compact Cauchy window K,
sup_{s in K}Graph_x(s) <= C_K uniformly in x.                (CGE-K)
```

The high-height evidence suggests the sharper asymptotic:

```text
Graph_x(s)/(1+|s|^2) = O(1)
```

once the window is away from the low-height transition.  But Phase 72 only needs `(CGE-K)`.

## 4. Status

```text
tested: height-normalized graph energy;
observed: high-height law Graph ~ |s|^2;
corrected: do not claim a universal height-normalized constant over low-height windows;
open: prove CGE-K uniformly on compact Cauchy windows.
```
