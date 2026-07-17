# E72.171 -- Fixed polynomial trace certificate

**Date:** 2026-07-09.
**Role:** replace the sign-energy gate by fixed trace polynomial majorants.

## 0. Idea

For each block, choose a polynomial `p_j` such that:

```text
p_j(t) >= t^2                 for -M_j <= t <= 0,
p_j(t) >= (1-a_j)^2t^2        for 0 <= t <= M_j.
```

Then for every self-adjoint `K_j` with `||K_j||<=M_j`:

```text
E_{a_j}(K_j) <= Tr p_j(K_j).
```

Thus:

```text
BSE <= Tr p_0(K_0)+Tr p_1(K_1).
```

This removes the spectral projections `K_j^+`,`K_j^-` from the proof target.

## 1. Fixed intervals

The tested stable range supports:

```text
||K_0|| <= 0.90,
||K_1|| <= 0.60.
```

The LP probe constructs degree-10 majorants on:

```text
K0 interval: [-0.90,0.90], a0=0.70,
K1 interval: [-0.60,0.60], a1=0.60.
```

## 2. Diagnostic output

The companion script:

```text
E72_171_polynomial_majorant_probe.py
```

reports:

```text
E72.171 fixed polynomial majorant probe
degree=10; intervals K0=[-0.9,0.9], K1=[-0.6,0.6]
 lam    L   exact0   poly0  exact1   poly1  polySum  exactSum
  12  4.97    0.565   0.577   0.333   0.339    0.916    0.898
  14  5.28    0.511   0.522   0.332   0.339    0.860    0.843
  16  5.55    0.457   0.465   0.337   0.344    0.809    0.794
  18  5.78    0.447   0.455   0.213   0.220    0.675    0.660
  20  5.99    0.403   0.413   0.332   0.339    0.752    0.735
  22  6.18    0.381   0.393   0.377   0.385    0.778    0.759
  24  6.36    0.372   0.386   0.368   0.377    0.763    0.740
worst_poly_sum=0.916 at lambda=12
```

After adding the `2e-5` constant buffer certified in E72.172, the worst tested trace bound remains
below `0.92`.

## 3. New gate

Define `PTC`:

```text
PTC-1: ||K_0||<=0.90 and ||K_1||<=0.60,
PTC-2: Tr p_0(K_0)+Tr p_1(K_1)<=0.92,
PTC-3: cross_+<=0.04.
```

Then:

```text
PTC => BSE+cross_+ <= 0.96 < 1 => F2B-PSD.
```

This is the cleanest current form of the arithmetic gate: it is finite, explicit, non-spectral in the
sign sense, and built from traces of powers of the exact discrete von Mangoldt blocks.

## 4. Proof direction

For:

```text
p_j(t)=sum_{r=0}^{10} c_{j,r}t^r,
```

the trace term is:

```text
Tr p_j(K_j)=sum_{r=0}^{10} c_{j,r}Tr(K_j^r).
```

Each `Tr(K_j^r)` expands into a finite `r`-cycle sum over prime-power positions and overlap kernels.
Therefore the remaining proof no longer asks for positivity of a Weil form. It asks for explicit
cycle-trace estimates for two broad prime-position blocks.
