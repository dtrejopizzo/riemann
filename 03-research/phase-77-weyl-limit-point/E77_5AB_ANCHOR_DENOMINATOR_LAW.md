# E77.5ab - Anchor Denominator Law

## Statement

E77.5aa reduced the live object to the Schur anchor denominator:

```text
Tp/T = t0p/t0 - theta'/(1-theta).
```

This block tests whether the zeta regime can be closed by a simple magnitude
law for

```text
|1-theta_N|.
```

## Probe

File:

```text
E77_5ab_anchor_denominator_law_probe.py
```

Run:

```text
python3 E77_5ab_anchor_denominator_law_probe.py \
  --output E77_5ab_anchor_denominator_law_results.json
```

Inputs:

```text
E77_5aa_schur_logt_functional_zeta.json
E77_5aa_schur_logt_functional_plant.json
```

## Zeta Scaling

At `sigma=3.0`:

| mod4 | N | |1-theta| | N|1-theta| | Q_theta/Q_logT |
|---:|---:|---:|---:|---:|
| 0 | 8 | 0.213195 | 1.705556 | 1.227140 |
| 0 | 12 | 0.067872 | 0.814463 | 1.163663 |
| 0 | 16 | 0.032768 | 0.524296 | 1.121178 |
| 2 | 10 | 0.109809 | 1.098089 | 1.172330 |
| 2 | 14 | 0.044726 | 0.626165 | 1.124950 |
| 2 | 18 | 0.024192 | 0.435454 | 1.144263 |

Local denominator power slopes:

| mod4 | step | slope |
|---:|---|---:|
| 0 | 8 -> 12 | -2.8229 |
| 0 | 12 -> 16 | -2.5311 |
| 2 | 10 -> 14 | -2.6694 |
| 2 | 14 -> 18 | -2.4453 |

At `sigma=1.0`, the same denominator decrease appears:

```text
mod0: |1-theta| 0.237793 -> 0.0335879
mod2: |1-theta| 0.117523 -> 0.0246548
```

## Plant Falsifier

At `sigma=3.0`:

| mod4 | N | |1-theta| | N|1-theta| | Q_theta/Q_logT |
|---:|---:|---:|---:|---:|
| 0 | 8 | 6.883949 | 55.071595 | 0.092572 |
| 0 | 12 | 30.324780 | 363.897361 | -3.914414 |
| 0 | 16 | 5.568363 | 89.093814 | 2.301671 |
| 2 | 10 | 52.247770 | 522.477702 | 3.425973 |
| 2 | 14 | 5.849821 | 81.897489 | -0.088719 |
| 2 | 18 | 5.837219 | 105.069947 | 1.247822 |

The planted build is not near the anchor and does not have a stable
denominator scaling.

## Proof-Or-Falsifier

The near-anchor separation is real:

```text
zeta:  |1-theta| < 0.25 and decreasing in the tested rows;
plant: |1-theta| ranges from about 5.57 to 52.25.
```

But a simple denominator law does not close the zeta envelope.  Even on the
zeta rows, `N|1-theta|` is not stable; it continues to fall.  The local power
slopes drift from about `-2.8` toward `-2.45`, so replacing the denominator
by a fixed power law would be another finite-window extrapolation.

The denominator is necessary but not sufficient.  The live signed term is

```text
-theta'/(1-theta),
```

so the next reduction must keep numerator and denominator coupled.

## Status

```text
proved:
  zeta enters a near-anchor Schur regime and the planted build does not;
  the denominator magnitude alone is insufficient for closure.

refuted:
  ANCHOR-DENOMINATOR-LAW as a simple |1-theta| power law.

open:
  prove the coupled numerator/denominator law for theta'/(1-theta).
```

Reduced target:

```text
THETA-LOGDERIV-COUPLING:
  control the signed quantity -theta'/(1-theta) directly, including phase,
  denominator, and numerator together; isolate the finite residual that
  remains on the mod2 branch.
```
