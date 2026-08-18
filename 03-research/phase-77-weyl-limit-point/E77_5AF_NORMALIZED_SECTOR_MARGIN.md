# E77.5af - Normalized Sector Margin

## Statement

E77.5ae identified the robust sector object:

```text
M_N(sigma) = (Im(u_N)^2 - Re(u_N)^2)/|u_N|^2,
u_N = -theta'_N/(1-theta_N).
```

The cone certificate is

```text
Im(u_N)>0,
M_N(sigma)>0.
```

This block measures whether `M_N` is bounded away from zero on zeta and
negative on the planted falsifier.

## Probe

File:

```text
E77_5af_normalized_sector_margin_probe.py
```

Run:

```text
python3 E77_5af_normalized_sector_margin_probe.py \
  --output E77_5af_normalized_sector_margin_results.json
```

Input:

```text
E77_5ae_sector_certificate_results.json
```

## Zeta Margins

| sigma | mod4 | first -> last margin | min margin | relative drift |
|---:|---:|---:|---:|---:|
| 1.0 | 0 | 0.992586657 -> 0.881683384 | 0.881683384 | -0.111731578 |
| 1.0 | 2 | 0.912906644 -> 0.750616233 | 0.750616233 | -0.177773283 |
| 3.0 | 0 | 0.999142450 -> 0.986013700 | 0.986013700 | -0.013140018 |
| 3.0 | 2 | 0.989523153 -> 0.968454131 | 0.968454131 | -0.021292096 |

Worst tested zeta row:

```text
sigma=1.0, mod2, N=18, M=0.750616233.
```

## Plant Falsifier

| sigma | mod4 | first -> last margin | min margin | relative drift |
|---:|---:|---:|---:|---:|
| 1.0 | 0 | -0.995776056 -> -0.999998341 | -0.999998341 | 0.004240195 |
| 1.0 | 2 | -0.994776435 -> -0.999914154 | -0.999914154 | 0.005164697 |
| 3.0 | 0 | -0.850401285 -> -0.999454440 | -0.999668803 | 0.175273907 |
| 3.0 | 2 | -0.999223321 -> -0.996770368 | -0.999223321 | -0.002454860 |

Worst planted row:

```text
sigma=1.0, mod0, N=20, M=-0.999998341.
```

## Proof-Or-Falsifier

The normalized margin is a much stronger finite certificate than the raw cone
numerator.  In the tested window:

```text
zeta:  M_N >= 0.750616233;
plant: M_N <= -0.850401285 profile-wise, with worst rows near -1.
```

The live branch is still `sigma=1.0, mod2`, where the margin drifts downward
from `0.912906644` to `0.750616233`.  This is not enough to claim a theorem
for all cofinal sections, but it gives the first concrete lower-bound target:

```text
M_N(sigma) >= 1/2
```

on the safe zeta sector.

## Status

```text
proved numerically:
  normalized sector margin separates zeta and planted strongly;
  zeta margin stays above 0.75 in the tested window.

open:
  finite algebraic lower-bound proof for M_N >= 1/2, or a sharper certified
  lower envelope if the 1/2 threshold fails at larger N.

reduced:
  NORMALIZED-SECTOR-MARGIN -> MARGIN-LOWER-BOUND.
```

Reduced target:

```text
MARGIN-LOWER-BOUND:
  prove M_N(sigma) >= 1/2 for the zeta cofinal path on the safe sigma
  compact, using only finite Schur/cell algebra; if false, name the first
  row or residual that breaks the threshold.
```
