# E73.014 results - local action intertwiner

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_014_local_action_probe.py
```

## Output

```text
E73.014 local action closure probe
 lam     L   dim  primCols srcCols srcRank  srcCond   relImage  actRank
   8   4.159    25        50      70      15  6.8e+09   8.32e-08        7
  10   4.605    29        50      70      16  4.7e+09   1.05e-08        7
  12   4.970    33        50      70      17  8.3e+09   5.19e-08        7
  14   5.278    37        50      70      17  7.0e+09   1.94e-07        8
```

## Interpretation

With the enlarged local ideals, the operator image satisfies

```text
(C_E-mu I) PrimitiveIdeal ~= SourceIdeal
```

to relative error `10^-8`--`10^-7` in the tested windows.  The induced action has low rank `7--8`.

This is much better than the first local-action attempt without endpoint/polynomial generators, whose
defect rose to `10^-4`.

## Status

```text
verified: local action intertwiner is numerically strong after adding endpoint generators;
remaining: derive the inclusion symbolically from W02-WR-Prime.
```

