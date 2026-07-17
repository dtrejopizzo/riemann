# E73.011 results - image ablation

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_011_image_ablation_probe.py
```

## Output

```text
E73.011 image ablation probe
case             cols rank    condImg      relDist
all-p2            30    9   1.40e+09   1.19e-06
r1-only           15    8   7.89e+08   3.99e-06
r2-only           15    8   2.28e+08   2.46e-06
crit0              6    5   5.09e+08   6.88e-04
crit1              6    5   7.36e+06   1.85e-01
crit2              6    5   3.67e+06   2.58e-01
crit3              6    5   4.03e+06   3.32e-01
crit4              6    5   4.11e+06   3.59e-01
off0              10    7   5.46e+08   1.36e-05
off1              10    7   5.46e+08   1.31e-05
off2              10    7   6.40e+08   1.37e-05
crit0+4           12    9   6.37e+09   1.24e-06
off0+1            20    8   3.98e+08   3.42e-06
```

## Interpretation

The full `all-p2` dictionary reaches `relDist=1.19e-6`.  The two endpoint critical families
`crit0+4` reach `1.24e-6`, essentially the same distance.  This suggests that the active low-rank
image is controlled by endpoint critical divided differences rather than by the whole critical
window.

Off-node denominator choices are highly redundant: each individual off family already reaches
`~1.3e-5`.

## Status

```text
verified: endpoint-critical families preserve the image certificate;
next: replace redundant off-node denominators by a symmetric denominator product.
```

