# E73.107 results - box FAR-SLOPE probe

## 1. Purpose

E73.106 states the interval box certificate for `WEIGHTED-FAR-SLOPE`.
E73.107 tests the first box-level version by sampling:

```text
four corners + center
```

of natural cluster boxes around the first two tested heights.

This is not yet rigorous interval arithmetic, but it tests the two necessary box phenomena:

```text
1. FAR3 selected set stability;
2. C_main <= 1 across the box.
```

## 2. Output

```text
E73.107 box FAR-SLOPE probe
Samples box corners+center; reports possible FAR3 sets, worst L^5 main budget, FAR gap.
 lam     L alphaBox       tauBox          sets  CmainMax   farGap  status
  16   5.545 [0.18,0.22] [ 13.93, 14.33] 30.4,32.9,37.6     1.684e-01    4.442 PASS
  16   5.545 [0.15,0.25] [ 13.63, 14.63] 30.4,32.9,37.6     2.015e-01    4.334 PASS
  20   5.991 [0.15,0.25] [ 20.52, 21.52] 30.4,32.9,37.6     1.322e-01   27.449 PASS
  24   6.356 [0.15,0.25] [ 20.52, 21.52] 30.4,32.9,37.6     2.496e-01 62427271054566.328 PASS
  28   6.664 [0.15,0.25] [ 20.52, 21.52] 30.4,32.9,37.6     2.012e-01 1538422441117835.250 PASS
```

## 3. Diagnosis

For the tested boxes:

```text
selected FAR3 set = {30.4,32.9,37.6}
```

throughout the sampled corners and center.

The weighted main budget satisfies:

```text
CmainMax <= 0.25
```

even on the wider boxes:

```text
alpha in [0.15,0.25],
tau within +/-0.50.
```

Thus the proposed interval constant:

```text
C_main=1
```

has visible slack at box level.

## 4. Caveat

This is not a rigorous interval certificate yet.  It samples corners and center.  The rigorous
version must replace this by interval enclosures for:

```text
G_theta,m(a,i gamma_k)
```

over the full box, and interval lower/upper FAR score separation.

## 5. Consequence

The box certificate route is viable:

```text
box FAR3 stability + box Cmain<=1 => FAR3-MAIN-RAT on the box.
```

The next implementation step is true interval enclosure for the Hermite weight `W_k(B,L)`.

## 6. Status

```text
observed: FAR3 set stable on tested boxes;
observed: C_main=1 has large slack on tested boxes;
open: rigorous interval arithmetic for W_k(B,L).
```
