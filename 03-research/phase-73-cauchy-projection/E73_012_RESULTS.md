# E73.012 results - symmetric basis audit

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_012_symmetric_basis_probe.py
```

## Output

```text
E73.012 symmetric basis probe
 lam     L   dim  crits  cols rank    condImg      relDist
   8   4.159    25   end    10    4   3.28e+06   2.07e-04
   8   4.159    25   all    25    6   5.23e+09   2.16e-06
  10   4.605    29   end    10    5   9.65e+08   2.56e-04
  10   4.605    29   all    25    7   4.97e+09   3.76e-06
  12   4.970    33   end    10    5   1.78e+09   8.30e-05
  12   4.970    33   all    25    6   5.27e+08   3.33e-05
  14   5.278    37   end    10    5   1.37e+09   6.73e-04
  14   5.278    37   all    25    6   5.82e+07   8.84e-05
```

## Interpretation

The endpoint-critical symmetric basis loses accuracy compared with the separate off-node dictionary.
The full critical symmetric basis is better but still unstable and weaker than `RAT-DD_2` with
separate denominators.

## Status

```text
no-go: simple symmetric denominator product is not the right canonical basis;
next: formulate the image identity as a local Cauchy interpolation ideal with separate off-node
denominators.
```

