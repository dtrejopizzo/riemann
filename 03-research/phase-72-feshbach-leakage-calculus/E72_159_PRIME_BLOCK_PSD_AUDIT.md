# E72.159 -- Prime-block PSD audit

**Date:** 2026-07-09.
**Role:** test whether `PSD-DIST` is global over coherent prime-position blocks.

## 0. Block candidate

E72.158 rejects a PSD approximant made from a few individual prime-power cells.  The next natural
candidate is block-coherent.  Partition:

```text
0<=y=m log p<=L
```

into `B` bins and write:

```text
K_rel=sum_{b=1}^B K_b.
```

Test:

```text
P_B=sum_b (K_b)^+.
```

If:

```text
||K_rel-P_B||_HS<1,
```

then `PSD-DIST` has a finite block certificate.

## 1. Diagnostic

The companion script:

```text
E72_159_prime_block_psd_probe.py
```

tests `B=2,3,4,6` and reports the distance from `K_rel` to the sum of positive block parts.

Representative output:

```text
E72.159 prime-block PSD probe
 lam   L bins  distOpt  distBlocks  bestBins  blockNorms
-- nbins=2
   6  3.58    2    0.764      1.095 all 1.18,0.97
   8  4.16    2    0.800      1.019 all 1.08,0.85
  10  4.61    2    0.692      0.976 all 1.00,0.89
  12  4.97    2    0.782      0.984 all 0.98,0.79
-- nbins=3
   6  3.58    3    0.764      1.342 all 0.86,1.17,0.86
   8  4.16    3    0.800      1.238 all 0.77,1.15,0.68
  10  4.61    3    0.692      1.184 all 0.68,1.13,0.73
  12  4.97    3    0.782      1.185 all 0.77,0.92,0.67
```

The two-block candidate is close and succeeds for `lambda>=10` in this small audit, while finer
partitions are worse.  Thus the positive part is coherent over large endpoint regions, not local over
individual cells or fine bins.

## 2. Status

```text
observed: two coarse blocks nearly certify PSD-DIST; finer blocks destroy useful coherence;
next:     optimize the two-block positive approximant by scalar weights.
```
