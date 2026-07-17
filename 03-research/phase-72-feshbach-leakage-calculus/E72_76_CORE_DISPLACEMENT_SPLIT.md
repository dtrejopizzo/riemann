# E72.76 -- Core/displacement split of the even coborder

**Date:** 2026-07-08.
**Role:** split the even coborder source into an actual-divisor core and a rank-one-corrected
model/actual displacement source.

## 0. Source from E72.75

For a finite root `tau_j`, E72.75 defines:

```text
W_j := iS_jk_x - (E_j-1)/L S_j1 <r_j,k_x-xi_x>,
```

where:

```text
S_j=2tau_j(tau_j^2I-D^2)^(-1),
r_j=(tau_jI-D)^(-1)1,
E_j=exp(i tau_jL),
h_x=k_x-xi_x.
```

## 1. Exact split

Write:

```text
W_j = W_j^core + W_j^disp,
```

with:

```text
W_j^core := iS_j xi_x,                                          (CORE-W)
```

and:

```text
W_j^disp := S_j( i h_x - (E_j-1)/L <r_j,h_x> 1 ).                (DISP-W)
```

Then:

```text
F_x(s;tau_j)/alpha_j
 = <Q r_s^even,C_even^(-1)QW_j^core>
   + <Q r_s^even,C_even^(-1)QW_j^disp>.                         (CD)
```

This is an identity.

## 2. Two separate certificates

The Even Coborder Certificate `(EVC)` follows from:

```text
max_j sup_s |<Q r_s^even,C_even^(-1)QW_j^core>| -> 0,            (CORE-C)
```

and:

```text
max_j sup_s |<Q r_s^even,C_even^(-1)QW_j^disp>| -> 0,            (DISP-C)
```

with the corresponding one-`s`-derivative estimates.

The first is an actual-divisor core identity. The second is the only remaining place where the
model/actual displacement `h_x=k_x-xi_x` enters.

## 3. Numerical signal

At `s=10+0.2i`, the finite harness shows that the core pairing is already much smaller than the
displacement pairing in most windows.

Representative values:

```text
lambda=8:
  tau=0.728  core |weyl|=3.86e-4   disp |weyl|=1.94e-2
  tau=2.708  core |weyl|=1.07e-3   disp |weyl|=1.39e-2

lambda=12:
  tau=0.825  core |weyl|=1.39e-4   disp |weyl|=3.08e-3
  tau=3.221  core |weyl|=2.55e-4   disp |weyl|=1.79e-4

lambda=20:
  tau=0.241  core |weyl|=2.62e-5   disp |weyl|=3.14e-2
  tau=4.351  core |weyl|=4.66e-5   disp |weyl|=2.36e-3
```

The raw norms are misleading: both pieces can have non-small raw size. The signal is only visible after
Feshbach shorting and Weyl testing.

## 4. Consequence

The Phase 72 target now splits cleanly:

```text
CORE-C: prove an actual finite-divisor identity for iS_jxi_x.
DISP-C: prove a reduced displacement estimate for
        S_j(ih_x - (E_j-1)L^(-1)<r_j,h_x>1).
```

This avoids asking for full convergence `k_x->xi_x`; only the rank-one-corrected displacement source
must be invisible in the even Weyl-Feshbach channel.

## 5. Status

```text
proved: EVC splits exactly into CORE-C plus DISP-C;
observed: CORE-C is already tiny in the finite harness;
open:   prove CORE-C algebraically and DISP-C as a reduced displacement estimate.
```
