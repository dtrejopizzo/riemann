# E77.5t - Weighted Parity Cell

## Objective

E77.5s refuted raw four-node sine parity.  E77.5t measures the parity after
the weights that actually occur in the common-core Schur transfer:

```text
contribution_j = tau_j(i sigma) (S^{-1}k)_j.
```

This includes the common-core resolvent and the safe Cauchy row before any
absolute estimate.

## Probe

Artifacts:

```text
E77_5t_weighted_parity_cell_probe.py
E77_5t_weighted_parity_cell_zeta.json
E77_5t_weighted_parity_cell_plant_n18.json
```

Commands:

```bash
python3 E77_5t_weighted_parity_cell_probe.py --case zeta --dps 70 --output E77_5t_weighted_parity_cell_zeta.json
python3 E77_5t_weighted_parity_cell_probe.py --case plant --max-modes 18 --dps 60 --output E77_5t_weighted_parity_cell_plant_n18.json
```

The planted run is limited to `N<=16` because the full planted build is the
costliest part of this probe; it is still a real planted falsifier run.

## Normalized Weighted Ratios

For zeta:

| N | mod4 | Q(sigma=1) | odd/inserted s=1 | odd/total s=1 | Q(sigma=3) | odd/inserted s=3 | odd/total s=3 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 0.294 | 0.394 | 0.858 | 1.58 | 0.407 | 0.878 |
| 10 | 2 | -0.0589 | 0.511 | 0.924 | 0.360 | 0.520 | 0.930 |
| 12 | 0 | 0.415 | 0.606 | 0.952 | 1.66 | 0.613 | 0.955 |
| 14 | 2 | -0.252 | 0.706 | 0.968 | -0.416 | 0.711 | 0.970 |
| 16 | 0 | 0.383 | 0.776 | 0.977 | 1.42 | 0.780 | 0.978 |
| 18 | 2 | 1.11 | 0.861 | 0.983 | 3.56 | 0.865 | 0.983 |

For planted:

| N | mod4 | Q(sigma=1) | odd/inserted s=1 | odd/total s=1 | Q(sigma=3) | odd/inserted s=3 | odd/total s=3 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0 | -102 | 0.877 | 0.703 | -6.22 | 0.871 | 0.640 |
| 10 | 2 | -5.73 | 0.717 | 0.199 | 4.90 | 0.472 | 0.126 |
| 12 | 0 | 6.03 | 0.131 | 0.042 | 12.4 | 0.062 | 0.020 |
| 14 | 2 | -4.07 | 0.144 | 0.070 | 4.28 | 0.152 | 0.074 |
| 16 | 0 | 5.00 | 0.435 | 0.178 | 13.5 | 0.439 | 0.180 |

## Reading

The absolute weighted magnitudes are not the right invariant.  In zeta they
grow extremely large because the common-core response is highly amplified;
in planted they remain O(1) on the reduced window.  That magnitude mostly
measures conditioning/LP behavior, not the finite Q coefficient.

The normalized ratio is more informative.  For zeta,

```text
|odd weighted package| / |inserted weighted package|
```

increases smoothly from about `0.39` to `0.86`, and the mod2 spike at
`N=18` occurs when this ratio is highest.  Planted does not reproduce this
law; its ratios are erratic and disconnect from the sign of Q.

## Reduced Target

`WEIGHTED-PARITY-CELL` is reduced to:

```text
ODD-RATIO-LAW:
  prove the zeta weighted odd/inserted ratio has a controlled monotone
  profile, and derive how its high-ratio mod2 branch feeds Q_N.
```

This target is smaller than raw weighted parity: it discards absolute
amplification and keeps the normalized signed geometry.

## Status

```text
proved:    no delta-envelope theorem yet;
refuted:   absolute weighted parity magnitude as Q source;
observed:  zeta normalized odd/inserted ratio is coherent and increasing;
observed:  planted ratio is erratic and falsifies the same law;
reduced:   WEIGHTED-PARITY-CELL -> ODD-RATIO-LAW;
next:      E77.5u should model the odd/inserted ratio against Q_N and test
           whether subtracting the ratio profile removes the mod2 spike.
```
