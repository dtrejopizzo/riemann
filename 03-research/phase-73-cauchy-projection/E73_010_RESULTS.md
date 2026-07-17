# E73.010 results - structured image subspace

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_010_subspace_image_probe.py
```

## Output

```text
E73.010 structured image subspace probe
 lam     L   dim  pwr  cols rank    condImg      relDist    eigSrc     expEig
   8   4.159    25    1    15    8   7.68e+08   5.54e-07  1.18e-10  2.71e-10
   8   4.159    25    2    30    8   3.82e+08   4.90e-07  1.18e-10  2.71e-10
   8   4.159    25    3    45    8   3.82e+08   4.90e-07  1.18e-10  2.71e-10
  10   4.605    29    1    15    8   2.69e+08   2.25e-06  1.18e-10  2.96e-10
  10   4.605    29    2    30    9   5.45e+09   6.08e-07  1.18e-10  2.96e-10
  10   4.605    29    3    45    9   5.44e+09   6.08e-07  1.18e-10  2.96e-10
  12   4.970    33    1    15    8   1.27e+08   3.28e-06  3.39e-12  9.17e-12
  12   4.970    33    2    30    9   5.07e+09   7.90e-07  3.39e-12  9.17e-12
  12   4.970    33    3    45    9   5.06e+09   7.90e-07  3.39e-12  9.17e-12
  14   5.278    37    1    15    8   7.89e+08   3.99e-06  9.05e-11  2.60e-10
  14   5.278    37    2    30    9   1.40e+09   1.19e-06  9.05e-11  2.60e-10
  14   5.278    37    3    45    9   1.40e+09   1.19e-06  9.05e-11  2.60e-10
```

## Interpretation

The structured image has small effective rank (`8--9`) and captures the source to relative distance
around `10^-6`.  Adding powers beyond `p=2` does not materially improve the subspace, so the useful
object is a low-rank image identity rather than a large coefficient expansion.

The image basis is ill-conditioned.  This explains why E73.009 did not show stable raw coefficients.

## Status

```text
verified: S_b is very close to a low-rank structured image subspace;
not closed: distance is not zero and eigenline residual remains NAT-SRC;
next: identify the rank 8--9 image generators symbolically.
```

