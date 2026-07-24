# E77.5ac - Theta Log-Derivative Coupling

## Statement

E77.5ab showed that `|1-theta|` alone is not enough.  The finite Schur object
must keep numerator and denominator coupled:

```text
u_N(sigma) = -theta'_N(sigma)/(1-theta_N(sigma)).
```

The safe contribution is

```text
2 Re(i u_N),
```

and `Q_theta` is its second drift coefficient.

## Probe

File:

```text
E77_5ac_theta_logderiv_coupling_probe.py
```

Runs:

```text
python3 E77_5ac_theta_logderiv_coupling_probe.py \
  --case zeta --max-modes 22 --dps 70 --sigmas 1.0,3.0 \
  --output E77_5ac_theta_logderiv_coupling_zeta.json

python3 E77_5ac_theta_logderiv_coupling_probe.py \
  --case plant --max-modes 22 --dps 70 --sigmas 1.0,3.0 \
  --output E77_5ac_theta_logderiv_coupling_plant.json
```

The probe records complex `theta`, `theta'`, `1-theta`, and
`u=-theta'/(1-theta)`.  Magnitudes are diagnostics only; the object itself is
complex and signed.

## Zeta Results

At `sigma=3.0`:

| N | mod4 | Q_theta | |u| new | arg(u) | arg(u)-pi/2 |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 8.44953 | 0.0800238 | 1.550088 | -0.020708 |
| 10 | 2 | 10.5975 | 0.0502917 | 1.498356 | -0.072440 |
| 12 | 0 | 9.84676 | 0.0343481 | 1.536524 | -0.034272 |
| 14 | 2 | 12.4958 | 0.0246726 | 1.492962 | -0.077835 |
| 16 | 0 | 10.9205 | 0.0184316 | 1.526730 | -0.044067 |
| 18 | 2 | 9.13685 | 0.0142589 | 1.444873 | -0.125923 |

At `sigma=1.0`:

| N | mod4 | Q_theta | |u| new | arg(u) | arg(u)-pi/2 |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 3.11409 | 0.0279991 | 1.509876 | -0.060920 |
| 10 | 2 | 3.75203 | 0.0176181 | 1.360573 | -0.210223 |
| 12 | 0 | 3.44657 | 0.0117454 | 1.469432 | -0.101365 |
| 14 | 2 | 4.29756 | 0.00854902 | 1.342857 | -0.227940 |
| 16 | 0 | 3.74339 | 0.00626568 | 1.440275 | -0.130522 |
| 18 | 2 | 3.12738 | 0.00508887 | 1.209895 | -0.360901 |

## Plant Falsifier

At `sigma=3.0`:

| N | mod4 | Q_theta | |u| new | arg(u) | distance to pi-axis |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 1.35963 | 0.0545908 | -2.864568 | 0.277024 |
| 10 | 2 | 15.4082 | 0.0556469 | 3.121885 | 0.019708 |
| 12 | 0 | 8.80048 | 0.0186373 | 3.044502 | 0.097091 |
| 14 | 2 | -0.568584 | 0.0143097 | 3.111765 | 0.029827 |
| 16 | 0 | -5.49534 | 0.0134039 | 3.128724 | 0.012869 |
| 18 | 2 | 6.74411 | 0.00909796 | 3.101397 | 0.040196 |

At `sigma=1.0`, the plant is again near the real negative axis:

```text
distance to pi-axis:
0.045972, 0.051128, 0.046982, 0.028139, 0.018677, 0.006552.
```

## Proof-Or-Falsifier

The coupled object gives a cleaner discriminator than denominator magnitude:

```text
zeta:  arg(u) near +pi/2;
plant: arg(u) near +/-pi.
```

This is not yet a closure theorem.  The zeta mod2 branch still has visible
phase drift, especially at `sigma=1`, where `arg(u)-pi/2` reaches
`-0.360901` at `N=18`.  A closure would need a finite proof that the phase
stays in the signed sector that makes `2 Re(iu)` deliver the required
`Q_theta` profile with a summable defect.

The magnitude-only residuals are refuted as carriers: `Q_den_abs` and
`Q_theta_prime_abs` are large and sign-insensitive, while `Q_theta` is a
signed second profile.

## Status

```text
proved:
  the smallest current object is the coupled complex u=-theta'/(1-theta);
  zeta and planted builds separate sharply by phase of u;
  magnitude-only numerator/denominator diagnostics are insufficient.

refuted:
  THETA-LOGDERIV-COUPLING as a solved magnitude law.

open:
  prove the zeta u-phase sector and the resulting signed Q_theta envelope.
```

Reduced target:

```text
U-PHASE-LAW:
  prove from the finite Schur/cell algebra that u=-theta'/(1-theta) remains
  in the zeta signed sector near +i, with quantitative drift small enough
  for the Q_theta envelope; planted/off-line builds must exit that sector.
```
