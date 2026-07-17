# E72.179 -- Adaptive SRP degree audit

**Date:** 2026-07-09.
**Role:** correct the fixed-degree SRP statement and identify the right uniform scale.

## 0. Issue

E72.175/E72.176 use fixed degree `D=28` polynomials with errors:

```text
eps_0=6.802249139526e-03,
eps_1=3.886999508300e-03.
```

The SRP bound contains:

```text
sqrt(d_x)(eps_0+eps_1).
```

Therefore a fixed nonzero error cannot be a uniform theorem if the finite-section dimension `d_x`
grows. The correct uniform statement must use a degree `D_x` depending on the dimension, with:

```text
sqrt(d_x)(eps_0(D_x)+eps_1(D_x)) <= epsilon_margin.
```

The identity remains finite for each `x`, but the maximum cycle length becomes `2D_x` instead of `56`.

## 1. Chebyshev implementation

The companion script:

```text
E72_179_adaptive_srp_degree_probe.py
```

evaluates `g_j(K_j)` using Chebyshev recurrence directly on matrices. This avoids the large monomial
coefficients seen in E72.175 and is the right numerical model for an adaptive-degree certificate.

## 2. Output

```text
E72.179 adaptive SRP degree probe
Chebyshev matrix evaluation; intervals K0=[-0.9,0.9], K1=[-0.6,0.6]
prepared lambda=12 dim=32 op0=0.439 op1=0.445
prepared lambda=14 dim=36 op0=0.429 op1=0.445
prepared lambda=16 dim=40 op0=0.399 op1=0.437
prepared lambda=18 dim=44 op0=0.362 op1=0.313
prepared lambda=20 dim=48 op0=0.356 op1=0.449
prepared lambda=22 dim=52 op0=0.326 op1=0.500
prepared lambda=24 dim=56 op0=0.349 op1=0.508
prepared lambda=26 dim=60 op0=0.335 op1=0.369
prepared lambda=28 dim=64 op0=0.346 op1=0.482
 deg   err0     err1   maxBound  worstLam  per-window
  28 6.802e-03 3.887e-03    0.984       12 12:0.984 14:0.952 16:0.934 18:0.907 20:0.920 22:0.938 24:0.927 26:0.768 28:0.829
  40 4.834e-03 2.762e-03    0.965       12 12:0.965 14:0.933 16:0.912 18:0.885 20:0.897 22:0.915 24:0.904 26:0.745 28:0.806
  56 3.488e-03 1.993e-03    0.952       12 12:0.952 14:0.919 16:0.899 18:0.870 20:0.882 22:0.900 24:0.887 26:0.728 28:0.788
  80 2.461e-03 1.406e-03    0.943       12 12:0.943 14:0.909 16:0.888 18:0.859 20:0.870 22:0.888 24:0.875 26:0.715 28:0.775
 112 1.767e-03 1.010e-03    0.936       12 12:0.936 14:0.902 16:0.881 18:0.852 20:0.863 22:0.880 24:0.866 26:0.706 28:0.766
```

## 3. Reading

The interval bounds:

```text
||K_0||<=0.90,
||K_1||<=0.60
```

survive through `lambda=28` in this stress test.

Increasing the degree reduces the certified error term and improves the SRP bound. The worst tested
window remains `lambda=12`, not the larger dimensions, so the stable regime is not visibly drifting
toward failure in this range.

## 4. Corrected stable statement

Replace fixed `Stable-SRP` by adaptive `Stable-SRP(D_x)`:

```text
Choose D_x such that
sqrt(d_x)(eps_0(D_x)+eps_1(D_x)) <= m_x,
```

and prove:

```text
||g_{0,D_x}(K_0)+g_{1,D_x}(K_1)||_HS + m_x < 1.
```

Equivalently:

```text
Tr(G_{x,D_x}^2) < (1-m_x)^2.
```

This is still a finite explicit identity for each `x`, but the mixed cycle length is at most `2D_x`.

## 5. New open theorem

The uniform theorem is:

```text
Adaptive-Stable-SRP:
There exists a degree schedule D_x and margin m_x<1 such that:
  ||K_0||<=0.90,
  ||K_1||<=0.60,
  sqrt(d_x)(eps_0(D_x)+eps_1(D_x))<=m_x,
  ||G_{x,D_x}||_HS + m_x < 1.
```

The finite-cycle reduction remains valid with maximum cycle length `2D_x`.
