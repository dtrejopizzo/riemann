# E72.91 -- Low-band cofactor identity

**Date:** 2026-07-09.
**Role:** factor finite-band root transport through a single transported cofactor vector.

## 0. Transport vector

E72.90 showed that finite-band root transport is not visibly killed by truncation alone. The residual
inside the band is:

```text
R_{x,H}(s;tau)
 = i C_{P_Hg,k}(tau)
   -(exp(i tau L)-1)L^(-1)C_{P_Hg,1}(tau)M_k(tau).
```

Define:

```text
Z_x(tau)
 := iS_tau k_x
    -(exp(i tau L)-1)L^(-1)M_k(tau)S_tau1,                  (Z)
```

where:

```text
S_tau=2tau(tau^2I-D^2)^(-1),
M_k(tau)=<(tau I-D)^(-1)1,k_x>.
```

Then:

```text
R_{x,H}(s;tau)=<P_Hg_{x,s},Z_x(tau)>.
```

## 1. Cofactor form

Recall:

```text
g_{x,s}=B_xC_E^(-1)B_x^*r_s^even.
```

Let:

```text
a_x(s):=B_x^*r_s^even,
c_{x,H}(tau):=B_x^*P_HZ_x(tau).
```

Then:

```text
R_{x,H}(s;tau)
 = <C_E^(-1)a_x(s),c_{x,H}(tau)>
 = <a_x(s),C_E^(-1)c_{x,H}(tau)>.                            (LBC)
```

Equivalently, define the transported low-band cofactor:

```text
phi_{x,H,tau}:=B_xC_E^(-1)c_{x,H}(tau).
```

Then:

```text
R_{x,H}(s;tau)=<r_s^even,phi_{x,H,tau}>.                      (LBC-phi)
```

Thus `(FBRT)` is exactly the Cauchy invisibility of `phi_{x,H,tau_j}` at finite Weyl roots.

## 2. Meaning

The residual is no longer hidden in:

```text
P_Hg_{x,s}
```

or in a root interpolation remainder. It is the Cauchy transform of one explicit vector:

```text
phi_{x,H,tau_j}.
```

The next question is whether:

```text
||phi_{x,H,tau_j}|| -> 0
```

or only:

```text
<r_s^even,phi_{x,H,tau_j}> -> 0.
```

The first would give a norm proof. The second requires a finite moment/Cauchy identity.

## 3. Numerical verification

The companion script:

```text
E72_91_low_band_cofactor_probe.py
```

compares direct finite-band transport against both cofactor forms in `(LBC)`.

Representative differences:

```text
lambda=12, tau=0.825:  |direct|=3.092e-03, diff=2.44e-17
lambda=16, tau=2.077:  |direct|=1.561e-02, diff=1.39e-17
lambda=20, tau=0.241:  |direct|=3.137e-02, diff=5.29e-17
lambda=24, tau=8.020:  |direct|=6.204e-03, diff=1.73e-18
```

## 4. Status

```text
proved: finite-band transport equals Cauchy pairing with phi_{x,H,tau};
open:   decide whether phi is norm-small or only Cauchy-invisible.
```
