# E77.5aa - Schur LogT Functional

## Statement

E77.5z showed that the scalar coupling `Q_logT/Q_ext` is too coarse on the
live `N=2 mod 4` branch.  This block returns to the exact Schur formula.

For the common-core transfer,

```text
T = t0 - corr = t0(1-theta),
theta = corr/t0.
```

Therefore

```text
Tp/T = t0p/t0 - theta'/(1-theta).
```

Define the safe scalar parts

```text
logT     = 2 Re(i Tp/T),
logT_t0  = 2 Re(i t0p/t0),
logT_th  = 2 Re(i[-theta'/(1-theta)]).
```

Then, exactly,

```text
Delta logT = Delta logT_t0 + Delta logT_th,
Q_logT,N = Q_t0,N + Q_theta,N.
```

No Taylor truncation is used.

## Probe

File:

```text
E77_5aa_schur_logt_functional_probe.py
```

Runs:

```text
python3 E77_5aa_schur_logt_functional_probe.py \
  --case zeta --max-modes 22 --dps 70 --sigmas 1.0,3.0 \
  --output E77_5aa_schur_logt_functional_zeta.json

python3 E77_5aa_schur_logt_functional_probe.py \
  --case plant --max-modes 22 --dps 70 --sigmas 1.0,3.0 \
  --output E77_5aa_schur_logt_functional_plant.json
```

The probe verifies `Q_logT` against the independent E77.5y identity source.
The relative reference errors are roundoff-level, with the largest printed
zeta row at `3.11e-15` and planted rows around `1e-16`.

## Zeta Anatomy

At `sigma=3.0`:

| N | mod4 | Q_logT | Q_t0 | Q_theta | Q_theta/Q_logT | |1-theta| new |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 6.88555 | -1.56398 | 8.44953 | 1.227 | 0.21319 |
| 10 | 2 | 9.03968 | -1.55781 | 10.5975 | 1.172 | 0.10981 |
| 12 | 0 | 8.46186 | -1.38490 | 9.84676 | 1.164 | 0.067872 |
| 14 | 2 | 11.1079 | -1.38793 | 12.4958 | 1.125 | 0.044726 |
| 16 | 0 | 9.74017 | -1.18029 | 10.9205 | 1.121 | 0.032768 |
| 18 | 2 | 7.98492 | -1.15193 | 9.13685 | 1.144 | 0.024192 |

At `sigma=1.0`:

| N | mod4 | Q_logT | Q_t0 | Q_theta | Q_theta/Q_logT | |1-theta| new |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 2.52918 | -0.584910 | 3.11409 | 1.231 | 0.23779 |
| 10 | 2 | 3.19223 | -0.559794 | 3.75203 | 1.175 | 0.11752 |
| 12 | 0 | 2.95789 | -0.488675 | 3.44657 | 1.165 | 0.071085 |
| 14 | 2 | 3.81570 | -0.481859 | 4.29756 | 1.126 | 0.046229 |
| 16 | 0 | 3.33614 | -0.407253 | 3.74339 | 1.122 | 0.033588 |
| 18 | 2 | 2.73296 | -0.394419 | 3.12738 | 1.144 | 0.024655 |

The `t0` background is a negative, slowly varying correction.  The active
anchor term `Q_theta` carries the main profile and the mod2 crossing.

## Plant Falsifier

At `sigma=3.0`:

| N | mod4 | Q_logT | Q_t0 | Q_theta | Q_theta/Q_logT | |1-theta| new |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 14.6873 | 13.3276 | 1.35963 | 0.09257 | 6.8839 |
| 10 | 2 | 4.49747 | -10.9107 | 15.4082 | 3.426 | 52.248 |
| 12 | 0 | -2.24822 | -11.0487 | 8.80048 | -3.914 | 30.325 |
| 14 | 2 | 6.40882 | 6.97741 | -0.568584 | -0.08872 | 5.8498 |
| 16 | 0 | -2.38754 | 3.10780 | -5.49534 | 2.302 | 5.5684 |
| 18 | 2 | 5.40470 | -1.33940 | 6.74411 | 1.248 | 5.8372 |

At `sigma=1.0`, the same failure of the zeta regime appears: `|1-theta|`
ranges from `5.568` to `52.115`, and `Q_t0/Q_theta` alternates roles.

## Proof-Or-Falsifier

The exact Schur decomposition is certified:

```text
Q_logT = Q_t0 + Q_theta
```

and independently reconstructs the E77.5y `Q_logT` rows.

The direct closure still does not follow, but the live object is now smaller.
The zeta rows show a stable near-anchor regime:

```text
|1-theta| new:
0.21319, 0.10981, 0.067872, 0.044726, 0.032768, 0.024192
```

while the planted falsifier is far from the anchor:

```text
6.8839, 52.248, 30.325, 5.8498, 5.5684, 5.8372.
```

Thus the mod2 crossing is not a free scalar phenomenon.  It is carried by the
near-zero denominator in the exact active Schur anchor `1-theta`.

## Status

```text
proved:
  exact finite decomposition Tp/T = t0p/t0 - theta'/(1-theta);
  exact Q_logT decomposition into Q_t0 + Q_theta;
  zeta and planted builds are separated by the anchor regime |1-theta|.

refuted:
  closure from the scalar Q_logT/Q_ext profile alone.

open:
  prove the near-anchor zeta law and its signed second profile.
```

Reduced target:

```text
ANCHOR-DENOMINATOR-LAW:
  prove that the zeta Schur anchor 1-theta_N has the observed controlled
  approach to zero, with the signed theta-prime profile producing Q_theta;
  planted/off-line builds must stay outside this anchor regime or break the
  signed profile.
```
