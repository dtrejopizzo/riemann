# E72.95 -- Low-rank alignment audit

**Date:** 2026-07-09.
**Role:** test whether the transported cofactor vector `phi` lies near a small natural span.

## 0. Motivation

After E72.91, finite-band transport is:

```text
R_{x,H}(s;tau)=<r_s^even,phi_{x,H,tau}>.
```

E72.92 rejects norm-smallness, and E72.94 rejects low-moment cancellation as the direct mechanism.
Another possible shortcut is:

```text
phi_{x,H,tau} approx span{xi_x,h_x,1},
h_x=k_x-xi_x.
```

If true, the Cauchy pairing would reduce to a few Weyl functions:

```text
M_xi(s), M_h(s), M_1(s).
```

## 1. Probe

The companion script:

```text
E72_95_phi_alignment_probe.py
```

projects `phi` in the physical band `H=18` onto:

```text
span{xi,h,1},
span{h,1},
span{xi,h}.
```

## 2. Result

Representative relative residuals:

```text
lambda=12:
  tau=0.825  span{xi,h,1}=7.87e-01
  tau=2.135  span{xi,h,1}=6.88e-01

lambda=16:
  tau=0.485  span{xi,h,1}=9.79e-01
  tau=2.077  span{xi,h,1}=7.01e-01

lambda=20:
  tau=0.241  span{xi,h,1}=7.43e-01
  tau=1.856  span{xi,h,1}=9.91e-01

lambda=24:
  tau=6.889  span{xi,h,1}=6.79e-01
  tau=9.167  span{xi,h,1}=8.97e-01
```

The vector `phi` is not close to this low-dimensional natural span.

## 3. Consequence

The finite-band identity cannot be reduced to a few already-known Weyl transforms. The correct object
is the full finite-band Stieltjes transform:

```text
M_{phi_{x,H,tau_j}}(s).
```

This strengthens the conclusion of E72.94: the remaining identity is genuinely finite-dimensional but
not low-rank.

## 4. Status

```text
rejected: low-rank alignment with xi, h, and 1;
kept:     full finite-band Stieltjes identity as the current endpoint.
```
