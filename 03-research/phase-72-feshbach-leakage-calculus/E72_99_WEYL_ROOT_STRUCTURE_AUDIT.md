# E72.99 -- Weyl root structure audit

**Date:** 2026-07-09.
**Role:** test whether the transport vector `Z_x(tau_j)` already contains a simple Weyl-root factor.

## 0. Question

At finite Weyl roots:

```text
M_xi(tau_j)=<r_-(tau_j),xi_x>=0.
```

The remaining finite-band defect is built from:

```text
Z_x(tau)
 := iS_tau k_x
    -(exp(i tau L)-1)L^(-1)M_k(tau)S_tau1.
```

A possible closure would be that `Z_x(tau_j)` is already orthogonal to some natural root direction,
for example:

```text
xi_x, k_x, 1,
```

or that its pairings reduce to a derivative of the Weyl equation.

## 1. Probe

The companion script:

```text
E72_99_weyl_derivative_probe.py
```

prints:

```text
|M_xi(tau_j)|,
|<xi,Z>|,
|<k,Z>|,
|<1,Z>|,
|M'_k(tau_j)|,
|M'_xi(tau_j)|.
```

## 2. Result

The finite-root condition is verified:

```text
|M_xi(tau_j)| ~ 1e-17--1e-12.
```

But the vector `Z_x(tau_j)` is not killed by the obvious directions. Representative values:

```text
lambda=12:
  tau=0.825  |<xi,Z>|=1.23e-02  |<k,Z>|=3.70e-01  |<1,Z>|=4.35e-01
  tau=2.135  |<xi,Z>|=9.80e-03  |<k,Z>|=2.64e-01  |<1,Z>|=5.84e-01

lambda=20:
  tau=0.241  |<xi,Z>|=1.83e-03  |<k,Z>|=1.35e+00  |<1,Z>|=2.68e+00
  tau=3.844  |<xi,Z>|=8.00e-04  |<k,Z>|=1.53e-01  |<1,Z>|=6.10e-01

lambda=24:
  tau=1.522  |<xi,Z>|=6.04e-02  |<k,Z>|=1.37e+00  |<1,Z>|=2.78e+00
  tau=9.167  |<xi,Z>|=3.34e-03  |<k,Z>|=1.13e-01  |<1,Z>|=1.31e-01
```

## 3. Conclusion

The Weyl-root factor:

```text
M_xi(tau_j)=0
```

does not act before Feshbach shorting as a simple orthogonality of `Z_x(tau_j)`.

Thus the root-specific identity is not:

```text
Z_x(tau_j) perpendicular xi_x, k_x, or 1.
```

It remains a shorted determinant identity involving:

```text
C_E^(-1)B_x^*P_HZ_x(tau_j).
```

## 4. Status

```text
rejected: simple pre-shorting Weyl-root orthogonality of Z_tau;
kept:     bordered determinant D2 as the correct finite object.
```
