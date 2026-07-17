# E72.148 -- RFBD uniform-gap stress test

**Date:** 2026-07-09.
**Role:** test whether the relative arithmetic gap is genuinely uniform or marginal.

## 0. Question

The finite route uses:

```text
C_actual >= theta_H C_model,        theta_H>0.               (RCOER)
```

Equivalently:

```text
eta_H=1-theta_H<1.
```

The critical risk is that:

```text
theta_H(x)->0
```

as `L=log x` grows.  If that happened, the finite certificate would be marginal and would re-enter the
old wall.  If `theta_H` stays bounded below, `RFBD` is a genuine relative coercivity gap.

## 1. Progressive probe

The companion script:

```text
E72_148_rfbd_gap_progressive_probe.py
```

computes:

```text
theta_H=lambda_min(C_model^(-1/2)C_actual C_model^(-1/2)),
eta_H=1-theta_H,
lambda_min(C_model)/L,
||C_actual-C_model||/L.
```

It uses progressive output and stops at `lambda=30`, because the larger `lambda=36` window is slow with
the current quadrature-based build.

Representative output:

```text
E72.148 RFBD progressive uniform-gap probe
 lam    L    dim   theta_H   eta_H  modelFloor/L  ||Delta||/L
   8  4.159     24    0.5109  0.4891        0.9918       1.2410
  12  4.970     30    0.4230  0.5770        1.4854       2.4130
  16  5.545     38    0.4218  0.5782        1.8867       3.0583
  20  5.991     46    0.6633  0.3367        2.3086       1.3877
  24  6.356     54    0.4804  0.5196        2.8789       3.3669
  30  6.802     66    0.6250  0.3750        3.3736       2.2669
```

The observed range is:

```text
theta_H in [0.4218,0.6633].
slope(theta_H vs L)=+0.0500.
```

So the gap does not show decay toward zero in this stress range.

## 2. Interpretation

The crude perturbation norm `||Delta||/L` is often larger than the model floor, so absolute Weyl
dominance is still false.  But the relative lower form bound remains robust.  This supports the
`PSD-DIST/NHS/RFBD` route rather than the failed operator-norm route.

## 3. Status

```text
observed: RFBD has a positive relative gap through lambda=30;
rejected: visible marginal decay of theta_H in this stress range;
open:     prove the uniform lower gap analytically, or extend the progressive probe after optimizing build.
```
