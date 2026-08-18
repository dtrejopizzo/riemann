# E77.5ag - Margin Lower Bound

## Statement

E77.5af proposed the concrete threshold

```text
M_N(sigma) >= 1/2,
M_N = (Im(u_N)^2-Re(u_N)^2)/|u_N|^2.
```

This block extends the weakest zeta branch and tests the threshold directly.

The threshold is algebraically equivalent to the cone pair

```text
Im(u_N)>0,
Im(u_N)^2 - 3 Re(u_N)^2 >= 0.
```

## Probe

Files:

```text
E77_5ag_margin_lower_bound_probe.py
E77_5ag_margin_lower_bound_zeta_sigma1_n24.json
E77_5ag_margin_lower_bound_results.json
```

Runs:

```text
python3 E77_5ac_theta_logderiv_coupling_probe.py \
  --case zeta --max-modes 24 --dps 70 --sigmas 1.0 \
  --output E77_5ag_margin_lower_bound_zeta_sigma1_n24.json

python3 E77_5ag_margin_lower_bound_probe.py \
  --output E77_5ag_margin_lower_bound_results.json
```

The extension targets the previously weakest branch: `sigma=1.0`, `N=2 mod
4`.

## Zeta Extension

At `sigma=1.0`:

| N | mod4 | M | M-1/2 | Re(u) | Im(u) |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 0.992586657 | 0.492586657 | 0.00170465 | 0.0279472 |
| 10 | 2 | 0.912906644 | 0.412906644 | 0.00367651 | 0.0172302 |
| 12 | 0 | 0.979520696 | 0.479520696 | 0.00118853 | 0.0116851 |
| 14 | 2 | 0.897874268 | 0.397874268 | 0.00193183 | 0.00832789 |
| 16 | 0 | 0.966121155 | 0.466121155 | 0.000815488 | 0.00621238 |
| 18 | 2 | 0.750616233 | 0.250616233 | 0.00179697 | 0.00476104 |
| 20 | 0 | 0.881683384 | 0.381683384 | 0.000962523 | 0.00383850 |
| 22 | 2 | 0.997514713 | 0.497514713 | 0.000107017 | 0.00303396 |

The prior worst row remains the worst row:

```text
sigma=1.0, N=18, mod2, M=0.750616233.
```

The new mod2 row at `N=22` recovers strongly:

```text
M=0.997514713.
```

## Plant Falsifier

At `sigma=1.0`, the planted build fails immediately:

| N | mod4 | M | M-1/2 | Re(u) | Im(u) |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | -0.995776056 | -1.495776056 | -0.157520 | 0.00724667 |
| 10 | 2 | -0.994776435 | -1.494776435 | -0.109068 | 0.00558130 |
| 12 | 0 | -0.995588640 | -1.495588640 | -0.00830299 | -0.000390378 |
| 14 | 2 | -0.998416776 | -1.498416776 | -0.0121421 | -0.000341761 |
| 16 | 0 | -0.999302389 | -1.499302389 | -0.0126608 | -0.000236498 |
| 18 | 2 | -0.999914154 | -1.499914154 | -0.00837193 | 0.0000548505 |
| 20 | 0 | -0.999998341 | -1.499998341 | -0.00745470 | -0.00000679042 |

First failure:

```text
sigma=1.0, N=8, mod0.
```

## Proof-Or-Falsifier

The candidate threshold survives the first extension beyond the previous
window:

```text
zeta-lam6: all tested sigma=1 rows through N=22 pass M>=1/2;
plant-lam6: fails from the first row.
```

This is not yet a theorem.  The result upgrades the live object from a
floating sector margin to a concrete quadratic cone certificate:

```text
Im(u)>0,
Im(u)^2 - 3 Re(u)^2 >= 0.
```

That pair is finite and rational in the Schur/cell data through
`u=-theta'/(1-theta)`.

## Status

```text
proved numerically:
  zeta passes M>=1/2 through the extended weakest branch;
  planted fails M>=1/2 immediately;
  the threshold is equivalent to a finite quadratic cone.

open:
  theorem-grade proof of Im(u)>0 and Im(u)^2-3Re(u)^2>=0.

reduced:
  MARGIN-LOWER-BOUND -> QUADRATIC-CONE-CERTIFICATE.
```

Reduced target:

```text
QUADRATIC-CONE-CERTIFICATE:
  express Im(u) and Im(u)^2-3Re(u)^2 as explicit finite Schur/cell rational
  forms and prove their signs on the zeta cofinal path; planted/off-line
  builds must fail at least one sign.
```
