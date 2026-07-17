# E72.96 -- Unified finite certificate

**Date:** 2026-07-09.
**Role:** package the current Phase 72 reduction into one explicit finite certificate.

## 0. Input

The scalar WRL route has been reduced to two defects:

```text
1. CCGD-QR: physical tightness of the Cauchy cofactor channel;
2. FBRT: root-specific Stieltjes invisibility in the finite physical band.
```

This note writes both defects using the same finite data:

```text
D, k_x, xi_x, C_E, B_x, finite roots tau_j, physical cutoff H.
```

No global zeta zero is inserted.

## 1. CCGD defect

For:

```text
a_x(s)=B_x^*r_s^even,
y_x(s)=C_E^(-1)a_x(s),
g_x(s)=B_xy_x(s),
K_H=B_x^*1_{|d|>H}B_x,
```

define:

```text
Def_CCGD(x,H,s)
 := a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
    / a_x(s)^*C_E^(-2)a_x(s).                              (D1)
```

This equals:

```text
||1_{|d|>H}g_x(s)||^2 / ||g_x(s)||^2.
```

## 2. FBRT/Stieltjes defect

For a finite Weyl root `tau_j`, define:

```text
Z_x(tau_j)
 := iS_tau_j k_x
    -(exp(i tau_jL)-1)L^(-1)M_k(tau_j)S_tau_j1,
```

and:

```text
phi_{x,H,tau_j}
 := B_xC_E^(-1)B_x^*1_{|d|<=H}Z_x(tau_j).
```

The finite-band root transport defect is:

```text
Def_FBRT(x,H,s;tau_j)
 := <r_s^even,phi_{x,H,tau_j}>.                            (D2)
```

Equivalently:

```text
Def_FBRT(x,H,s;tau_j)
 = M_{phi_{x,H,tau_j}}(conjugate(s)).
```

## 3. Unified closure statement

The current Phase 72 endpoint is:

```text
Unified finite certificate:
For every compact s-window K and finite root-height window T,

lim_{H->infty} limsup_{x->infty} sup_{s in K}
  Def_CCGD(x,H,s) = 0,

and for every fixed H,

lim_{x->infty} sup_{s in K, tau_j<=T}
  |Def_FBRT(x,H,s;tau_j)| = 0.                              (UFC)
```

Then:

```text
UFC
 => dual cofactor root transport
 => HPAC divisibility
 => scalar WRL resonance annihilation
 => Omega_7.
```

## 4. Numerical verifier

The companion script:

```text
E72_96_unified_certificate_probe.py
```

prints:

```text
CCGD       = Def_CCGD,
CCGDdiff   = difference between quadratic and direct tail,
maxFBRT    = max_j |Def_FBRT|,
rmsFBRT    = root RMS of |Def_FBRT|.
```

Representative output:

```text
lambda=20, N=40, s=10:
  H=12  CCGD=4.39e-02  CCGDdiff=6.2e-17  maxFBRT=3.141e-02
  H=18  CCGD=7.93e-03  CCGDdiff=1.2e-17  maxFBRT=3.137e-02
  H=24  CCGD=4.49e-03  CCGDdiff=1.6e-17  maxFBRT=3.137e-02

lambda=24, N=48, s=15:
  H=12  CCGD=9.74e-01  CCGDdiff=3.3e-16  maxFBRT=5.979e-03
  H=18  CCGD=1.07e-02  CCGDdiff=4.0e-17  maxFBRT=5.243e-03
  H=24  CCGD=2.47e-03  CCGDdiff=1.3e-17  maxFBRT=5.189e-03
```

## 5. Diagnosis

The unified certificate separates the two effects cleanly:

```text
CCGD improves when H passes the physical Cauchy height;
FBRT is largely unchanged by increasing H once the tail is gone.
```

Therefore the hard remaining identity is not physical tightness. It is the root-specific Stieltjes
defect:

```text
Def_FBRT(x,H,s;tau_j)->0.
```

## 6. Status

```text
proved: scalar WRL route reduces to the two finite defects (D1), (D2);
verified: the unified certificate reproduces direct computations to roundoff;
open:   prove the FBRT/Stieltjes defect, plus the CCGD-QR tightness inequality.
```
