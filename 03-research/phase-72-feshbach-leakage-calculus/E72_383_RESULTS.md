# E72.383 Results - Natural-height BV gate

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_383_natural_height_bv_probe.py
```

## Output

```text
E72.383 natural-height BV probe
 lam    L      sigma    c      BVc        scaledBV    horizScale
   6   3.584    0.250  0.650  2.337e+01  2.593e-01  6.492e-01
   8   4.159    0.250  0.650  4.728e+01  2.693e-01  7.388e-01
  10   4.605    0.250  0.650  6.853e+01  2.358e-01  6.853e-01
  12   4.970    0.250  0.650  1.056e+02  2.426e-01  7.336e-01
  14   5.278    0.250  0.650  1.354e+02  2.219e-01  6.909e-01
```

## Reading

For `z=0.25+i`, `sigma=0.25`, and `c=0.65`, one has

```text
c+sigma=0.90<1.
```

The scaled quantity

```text
BVc / (e^((c+sigma)L)L)
```

stays stable around `0.22--0.27`, supporting the `BV-K` scale in E72.383.

The horizontal scale after natural height division,

```text
BVc/e^L,
```

also remains `O(1)` in the tested windows.  This is the numerical signature that the natural height

```text
T=e^L
```

can control the horizontal contour when `c+sigma<1`.

## Status

```text
validated: BV-K scaling for the actual packet in a shifted strip;
validated: natural-height horizontal scale is stable;
proved in E72.383: NHW implies FWB under c+sigma_K<1;
open: prove BV-K, signed FarWall, and finite-mesh tail uniformly.
```
