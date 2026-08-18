# E77.5ad - U Phase Law

## Statement

E77.5ac reduced the live finite object to

```text
u_N(sigma) = -theta'_N(sigma)/(1-theta_N(sigma)).
```

This block tests the sector law:

```text
U-PHASE-LAW:
  zeta keeps u in a signed sector near +i, while the planted build exits it.
```

The sector margin used here is

```text
Im(u) - |Re(u)|.
```

Positive margin means `u` is inside the upper vertical cone.  This is not a
Weil-positivity claim; it is a finite Schur/cell diagnostic for the exact
log-transfer anchor.

## Probe

File:

```text
E77_5ad_u_phase_law_probe.py
```

Run:

```text
python3 E77_5ad_u_phase_law_probe.py \
  --output E77_5ad_u_phase_law_results.json
```

Inputs:

```text
E77_5ac_theta_logderiv_coupling_zeta.json
E77_5ac_theta_logderiv_coupling_plant.json
```

The signed vertical model is

```text
2 Re(iu) ~= -2|u|
```

when `u` is close to `+i|u|`.

## Zeta Sector

| sigma | mod4 | min sector margin | max |arg(u)-pi/2| | min Im(u)/|u| | max signed vertical error |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0 | 0.00539690 | 0.130522 | 0.991494 | 0.00857886 |
| 1.0 | 2 | 0.00296407 | 0.360901 | 0.935579 | 0.0688568 |
| 3.0 | 0 | 0.0176018 | 0.0440668 | 0.999029 | 0.000971727 |
| 3.0 | 2 | 0.0123552 | 0.125923 | 0.992082 | 0.00798101 |

The zeta rows all stay in the upper vertical cone.  The weakest tested zeta
margin is the live low-sigma mod2 branch:

```text
sigma=1.0, mod2, min margin = 0.00296407.
```

## Plant Falsifier

| sigma | mod4 | min sector margin | max |arg(u)-pi/2| | min Im(u)/|u| | max signed vertical error |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0 | -0.150273 | 4.69371 | -0.0469647 | 54.5437 |
| 1.0 | 2 | -0.103487 | 4.68425 | -0.0281356 | 151.635 |
| 3.0 | 0 | -0.0674397 | 4.43536 | -0.273495 | 76.7090 |
| 3.0 | 2 | -0.0545395 | 1.55109 | 0.0197063 | 49.7451 |

The plant exits the zeta sector decisively.  It lies near the real axis
instead of the upper imaginary sector.

## Proof-Or-Falsifier

This is the sharpest discriminant found in E77.5 so far:

```text
zeta:  Im(u) > |Re(u)| in all tested rows;
plant: Im(u) - |Re(u)| < 0 in all tested profiles.
```

Moreover, the signed vertical model reconstructs the zeta safe scalar well:
the largest zeta error in this window is `0.0688568`, and at `sigma=3` it is
below `0.008`.  The planted model fails by factors from about `49` to `152`.

This still does not close Omega7.  A proof would need a finite algebraic
certificate that the sector margin remains positive uniformly along the
cofinal path, with a quantitative lower bound strong enough to feed the
`Q_theta` envelope.

## Status

```text
proved numerically:
  zeta u-sector margin is positive in the tested window;
  planted u-sector margin is negative in the tested window;
  the signed vertical model is accurate for zeta and fails for planted.

open:
  theorem-grade sector certificate for Im(u)-|Re(u)| > 0.

reduced:
  U-PHASE-LAW -> SECTOR-CERTIFICATE.
```

Reduced target:

```text
SECTOR-CERTIFICATE:
  express Im(u)-|Re(u)| in finite Schur/cell algebra and prove a positive
  lower certificate on the zeta cofinal path; if this fails, isolate the
  exact signed residual in Re(u).
```
