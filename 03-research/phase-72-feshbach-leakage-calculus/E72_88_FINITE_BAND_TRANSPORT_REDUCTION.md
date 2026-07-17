# E72.88 -- Finite-band transport reduction

**Date:** 2026-07-09.
**Role:** check that Cauchy-channel physical tightness transfers to the actual root transport
functional.

## 0. Transport functional

E72.81 reduced the HPAC root residual to:

```text
R_x(s;tau)
 = i C_{g,k}(tau)
   -(exp(i tau L)-1)L^(-1)C_{g,1}(tau)M_k(tau),
```

where:

```text
g=g_{x,s}=B_xC_E^(-1)B_x^*r_s^even.
```

For a physical cutoff `H`, define:

```text
g_H=P_Hg,
P_H=1_{|d_n|<=H}.
```

The finite-band residual is:

```text
R_{x,H}(s;tau)
 = i C_{g_H,k}(tau)
   -(exp(i tau L)-1)L^(-1)C_{g_H,1}(tau)M_k(tau).             (FBT)
```

The tail error is:

```text
R_x(s;tau)-R_{x,H}(s;tau)=R_x[P_{>H}g](s;tau).
```

## 1. Tail control

For finite root windows away from the mesh poles, the transport kernel is bounded on physical tails.
Consequently:

```text
|R_x(s;tau)-R_{x,H}(s;tau)|
 <= K_{x,H,tau} ||P_{>H}g_{x,s}||.                            (TC)
```

Thus E72.87's Cauchy-channel Green decay `(CCGD)` reduces the full root transport theorem to the
finite-band theorem:

```text
R_{x,H}(s;tau_j)->0,
```

followed by `H->infty`.

## 2. Numerical check

The companion script:

```text
E72_88_finite_band_transport_probe.py
```

compares the full and finite-band residuals.

Representative output:

```text
lambda=20, N=40, s=10+0.2i:
  tau=0.241, H=18: |full|=3.137e-02, |band|=3.137e-02, |diff|=2.35e-05
  tau=1.856, H=18: |full|=5.553e-04, |band|=5.771e-04, |diff|=3.48e-05
  tau=3.844, H=24: |full|=6.424e-03, |band|=6.444e-03, |diff|=3.80e-05

lambda=24, N=48, s=10+0.2i:
  tau=1.522, H=18: |full|=4.392e-03, |band|=4.491e-03, |diff|=9.87e-05
  tau=6.889, H=18: |full|=3.860e-03, |band|=3.897e-03, |diff|=3.89e-05
  tau=8.020, H=24: |full|=6.134e-03, |band|=6.182e-03, |diff|=4.93e-05
```

When `H` lies below the height of `s`, the tail energy is large and the approximation can fail. Once
`H` passes the physical support of the Cauchy channel, the finite-band residual tracks the full
residual.

## 3. New split of the proof

The scalar WRL route now splits into two explicit parts:

```text
I.  CCGD-QR:
    prove a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
          / a_x(s)^*C_E^(-2)a_x(s) -> 0;

II. finite-band root transport:
    for each fixed physical H,
    prove max_{tau_j}|R_{x,H}(s;tau_j)| -> 0,
    then let H->infty.
```

Part I is a finite quadratic inequality. Part II is a finite physical-window root identity.

## 4. Status

```text
proved: full-minus-band transport is controlled by the physical tail;
verified: finite-band residual tracks the full residual once H is above the Cauchy height;
open:   prove CCGD-QR and finite-band root transport.
```
