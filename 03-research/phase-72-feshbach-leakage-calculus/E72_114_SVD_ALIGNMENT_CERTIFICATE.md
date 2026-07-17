# E72.114 -- SVD alignment certificate for the direct energy

**Date:** 2026-07-09.
**Role:** replace the coarse operator split by an exact singular-mode energy identity.

## 0. Setup

For fixed `x,H`, let:

```text
R_x:=R_{x,H}
```

be the shorted pushforward operator of E72.112, and let:

```text
Y_j:=Y_x(tau_j)
```

be the finite Chebyshev Fourier packet at a finite CCM root.

Take the singular value decomposition:

```text
R_x = sum_l sigma_l u_l v_l^*,
sigma_1>=sigma_2>=...
```

Then the direct quadratic energy is exactly:

```text
||R_xY_j||_2^2
 = sum_l sigma_l^2 |<Y_j,v_l>|^2.                         (SVD-E)
```

This identity is finite and contains no limiting zero input.

## 1. Rank-q alignment gate

### Theorem 72.114

Fix a physical band `H`, a finite root-height window `T`, and an integer `q>=1`.  Suppose:

```text
sup_{tau_j<=T} sum_{l<=q} sigma_l^2 |<Y_j,v_l>|^2 = O(1),     (TOP-q)
```

and:

```text
sigma_{q+1}^2 sup_{tau_j<=T}||Y_j||_2^2 = O(1).              (TAIL-q)
```

Then:

```text
sup_{tau_j<=T}||R_xY_j||_2=O(1),
```

so `(QFLUX)` of E72.109 holds.

### Proof

Split `(SVD-E)`:

```text
sum_l sigma_l^2 |<Y_j,v_l>|^2
 = sum_{l<=q} sigma_l^2 |<Y_j,v_l>|^2
   + sum_{l>q} sigma_l^2 |<Y_j,v_l>|^2.
```

The first term is `(TOP-q)`.  The second is bounded by:

```text
sigma_{q+1}^2 sum_{l>q}|<Y_j,v_l>|^2
 <= sigma_{q+1}^2||Y_j||_2^2,
```

which is `(TAIL-q)`. `QED`

## 2. Meaning

E72.112 used the coarse bound:

```text
||R_xY_j|| <= sigma_1||Y_j||.
```

E72.114 says that the real finite target can be strictly smaller:

```text
control finitely many bad singular directions,
use sigma_{q+1} for the tail.
```

This matters because the numerical shorted pushforward is nearly low-rank.

## 3. Diagnostic

The companion script:

```text
E72_114_svd_alignment_probe.py
```

reports the stable rank, the ratio:

```text
||RY||/(||R||||Y||),
```

and the fraction of the direct energy carried by the first 1 and 3 singular modes.

Representative output:

```text
E72.114 SVD alignment probe
 lam   N roots    smax    stableRank  maxFlux  maxRatio  maxTop1Frac  maxTop3Frac
   6  18     3 2.58e-02   1.402e+00 5.50e-02 5.76e-02    7.775e-01    9.935e-01
   8  24     4 1.88e-02   1.172e+00 6.29e-02 6.19e-02    9.618e-01    9.947e-01
  10  28     3 9.90e-03   1.221e+00 3.93e-02 4.94e-02    8.550e-01    9.949e-01
  12  32     4 8.45e-03   1.195e+00 2.29e-02 2.50e-02    9.534e-01    9.967e-01
  14  36     4 4.61e-03   1.228e+00 2.31e-02 3.86e-02    9.590e-01    9.982e-01
```

The operator is almost rank one in these windows, and the actual packet is far from saturating the
operator norm.  Thus the sharper proof target is a finite singular-alignment estimate, not only the
coarse operator product.

## 4. Updated endpoint

The energy side of E72.113 may now be replaced by:

```text
TOP-q + TAIL-q
```

for any fixed `q` that can be proved uniformly.  The current numerics suggest `q=3` is already enough
to capture more than `99%` of the direct energy in the tested windows.

## 5. Status

```text
proved: exact SVD energy identity for DQF;
proved: TOP-q + TAIL-q imply QFLUX;
observed: shorted pushforward is numerically nearly low-rank;
open:   prove TOP-q and TAIL-q uniformly, and prove the mass condition.
```
