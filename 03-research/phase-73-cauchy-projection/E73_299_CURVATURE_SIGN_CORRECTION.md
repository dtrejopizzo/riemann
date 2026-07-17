# E73.299 - Curvature sign correction for the simple ramp

Date: 2026-07-16.

## 1. Correction

For the simple ramp `r_0(y)=y(1-y/L)`, the balanced curvature operator in
E73.297 would be

```text
Q_y''-(4/L^2)J,
```

not `Q_y''+(4/L^2)J`.

E73.301 supersedes this as the load-bearing endpoint: the actual neutral ramp
from E73.193 is `r_*=r_0+c_Lr_1`, so the final correction is
`alpha_L(y)J`, not just `-(4/L^2)J`.

## 2. Derivation

For the simple-ramp audit, let

```text
B(y)=qQ_yeta,          r_*(y)=y(1-y/L),
B^bal(y)=B(y)-B'(0)r_*(y).
```

The cell derivative at zero is

```text
Q_0'=-(2/L)J.
```

Indeed, on the diagonal this is immediate from

```text
Q_y(j,j)=2(1-y/L)cos(d_jy),
```

and off the diagonal

```text
d/dy [(sin(d_jy)-sin(d_by))/(pi(n_b-n_j))]_{y=0}
=(d_j-d_b)/(pi(n_b-n_j))=-2/L.
```

Therefore

```text
B'(0)=qQ_0'eta=-(2/L)qJeta.
```

Since

```text
r_*''(y)=-2/L,
```

we get

```text
(B^bal)''(y)
=B''(y)-B'(0)r_*''(y)
=qQ_y''eta+(2/L)B'(0)
=q[Q_y''-(4/L^2)J]eta.
```

## 3. Why the earlier numerical audit did not expose it

For the endpoint vector `eta=R_wxi_L`, the scalar `qJeta` is extremely small
in the tested channels.  Hence the difference between the two signs is nearly
invisible there.

A generic-vector check separates the signs:

```text
plus-sign absolute error   ~ 1.46
minus-sign absolute error  ~ 6.3e-5
```

Thus the corrected sign is not a cosmetic convention; it is the actual
balanced second derivative.

## 4. Superseded endpoint

The simple-ramp curvature form would be:

```text
CURV-ABEL:
int_0^L K_L(t) q[Q_t''-(4/L^2)J]R_wxi_L dt
=O_M(L^(-M)).
```

The load-bearing endpoint is the E73.301 neutral-ramp version:

```text
int_0^L K_L(t) q[Q_t''+alpha_L(t)J]R_wxi_L dt
=O_M(L^(-M)).
```

## 5. Status

```text
corrected: simple-ramp curvature sign;
verified: finite-difference audit and generic-vector sign separation;
superseded: final finite endpoint uses E73.301 neutral-ramp alpha_L(t).
```
