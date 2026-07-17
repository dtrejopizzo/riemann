# E72.182 -- Adaptive margin certificate

**Date:** 2026-07-09.
**Role:** instantiate the Chebyshev adaptive SRP gate with a concrete margin.

## 0. Fixed margin

Set:

```text
m_*=0.05.
```

The approximation schedule from E72.181 requires:

```text
D_x+1 >= 0.99 sqrt(d_x)/(pi m_*),
```

with `D_x` even. Then:

```text
sqrt(d_x)(eps_0(D_x)+eps_1(D_x)) <= 0.05.
```

Thus it is enough to prove:

```text
||G_{x,D_x}||_HS < 0.95,
```

or equivalently:

```text
Tr(G_{x,D_x}^2) < 0.9025.                         (ASRP-0.05)
```

This is the concrete adaptive mixed-cycle inequality.

## 1. Diagnostic output

The companion script:

```text
E72_182_adaptive_margin_probe.py
```

chooses `D_x` automatically from the schedule and reports:

```text
E72.182 adaptive margin SRP probe
margin m*=0.050; require ||G_D||_HS < 0.950
 lam    L dim   D   epsHS  ||G_D||  final  margin2 pass
  12  4.97  32  36   0.048    0.922  0.970   0.058 YES
  14  5.28  36  38   0.048    0.887  0.936   0.124 YES
  16  5.55  40  40   0.049    0.864  0.913   0.167 YES
  18  5.78  44  42   0.049    0.835  0.883   0.220 YES
  20  5.99  48  44   0.049    0.845  0.893   0.202 YES
  22  6.18  52  46   0.048    0.860  0.909   0.174 YES
  24  6.36  56  48   0.048    0.846  0.894   0.200 YES
  26  6.52  60  48   0.050    0.686  0.736   0.459 YES
  28  6.66  64  50   0.049    0.745  0.794   0.369 YES
worst_final=0.970 at lambda=12
```

## 2. Interpretation

The tested stable windows satisfy the concrete split:

```text
approximation error <= 0.05,
cycle norm          < 0.95,
total residual      < 1.
```

The worst case remains the first stable window `lambda=12`, not the larger tested dimensions.

## 3. Current final arithmetic target

With `m_*=0.05`, the exact open theorem is:

```text
For all sufficiently large x:
  ||K_0|| <= 0.90,
  ||K_1|| <= 0.60,
  D_x even and D_x+1 >= 0.99 sqrt(d_x)/(0.05 pi),
  Tr(G_{x,D_x}^2) < 0.9025.
```

Here `Tr(G_{x,D_x}^2)` is the finite mixed von Mangoldt cycle sum from E72.177/E72.181, with cycle
length at most:

```text
2D_x = O(sqrt(d_x)).
```

This is the most concrete current zero-free Phase 72 arithmetic inequality.

E72.183 further replaces the two operator-norm inequalities by trace-power certificates:

```text
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.
```
