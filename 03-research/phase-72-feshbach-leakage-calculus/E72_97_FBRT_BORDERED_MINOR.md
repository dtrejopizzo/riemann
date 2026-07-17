# E72.97 -- FBRT bordered minor

**Date:** 2026-07-09.
**Role:** express the finite-band Stieltjes defect as a single bordered determinant.

## 0. Input

E72.96 defines the finite-band root transport defect:

```text
Def_FBRT(x,H,s;tau_j)
 = <r_s^even,phi_{x,H,tau_j}>,
```

where:

```text
phi_{x,H,tau_j}=B_xC_E^(-1)c_{x,H}(tau_j),
c_{x,H}(tau_j)=B_x^*P_HZ_x(tau_j).
```

Let:

```text
a_x(s)=B_x^*r_s^even.
```

Then:

```text
Def_FBRT(x,H,s;tau_j)=<a_x(s),C_E^(-1)c_{x,H}(tau_j)>.
```

## 1. Bordered determinant formula

With the Hilbert convention linear in the second variable:

```text
<a,C_E^(-1)c>=a^*C_E^(-1)c.
```

Therefore:

```text
Def_FBRT(x,H,s;tau_j)
 = - det [ C_E       c_{x,H}(tau_j) ] / det(C_E).             (FB-BM)
         [ a_x(s)^*  0                ]
```

This is the same Schur complement identity as E72.79, now specialized to the finite-band transport
vector.

## 2. Current determinant endpoint

Combining E72.96 and E72.97, the Phase 72 finite certificate is:

```text
D1(x,H,s)
 = a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
   / a_x(s)^*C_E^(-2)a_x(s),

D2(x,H,s;tau_j)
 = - det[[C_E,c_{x,H}(tau_j)],[a_x(s)^*,0]] / det(C_E).
```

The closure statement is:

```text
D1 -> 0,
D2 -> 0 on finite Weyl roots.
```

This is a fully finite matrix/determinant formulation of the remaining scalar WRL divisibility
problem.

## 3. Numerical verification

The companion script:

```text
E72_97_fbrt_bordered_minor_probe.py
```

checks direct solves against `(FB-BM)` in small windows where determinants are stable.

Representative output:

```text
lambda=6, tau=2.903:  |solve|=2.545e-02, rel.diff=9.64e-16
lambda=8, tau=3.215:  |solve|=2.912e-02, rel.diff=9.07e-16
lambda=10,tau=6.227:  |solve|=3.792e-03, rel.diff=7.32e-16
lambda=12,tau=7.717:  |solve|=2.094e-02, rel.diff=8.28e-16
```

## 4. Status

```text
proved: FBRT/Stieltjes defect equals one bordered determinant ratio;
achieved: the remaining Phase 72 obstruction is finite, explicit, and directly verifiable;
open:   prove asymptotic vanishing of D1 and D2.
```
