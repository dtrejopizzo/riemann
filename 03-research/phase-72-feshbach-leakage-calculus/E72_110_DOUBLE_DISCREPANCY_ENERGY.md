# E72.110 -- Double discrepancy energy for the quadratic flux

**Date:** 2026-07-09.
**Role:** expand the quadratic flux certificate as an explicit Chebyshev-discrepancy energy.

## 0. Input

From E72.106:

```text
Z_x^{pm}(tau)=(2/(L sqrt(x)))K_x^E(tau)k_x,
K_x^E(tau)=int_0^L exp(-i tau r)Lo_r dE_x^leftarrow(r).
```

From E72.109:

```text
Mass_x(H,tau)=1_H^TW_HB_xC_E^(-1)c_{x,H}^{pm}(tau),

Flux_x(H,tau)^2
 = ||T_HP_H^0W_HB_xC_E^(-1)c_{x,H}^{pm}(tau)||_2^2.
```

This note opens both expressions as integrals against:

```text
dE_x^leftarrow(r)=dPsi_x^leftarrow(r)-xexp(-r)dr.
```

## 1. Mass kernel

Set:

```text
b_H:=B_x^*W_H^T1_H,
w_{x,H}:=P_HB_xC_E^(-1)b_H.
```

Then:

```text
Mass_x(H,tau)
 = (2/(L sqrt(x)))int_0^L exp(-i tau r)
    <w_{x,H},Lo_rk_x> dE_x^leftarrow(r).                    (MINT)
```

### Proof

By definition:

```text
Mass = b_H^*C_E^(-1)c_pm
     = (2/(L sqrt(x)))b_H^*C_E^(-1)B_x^*P_HK_x^E(tau)k_x.
```

Move the adjoint factors to the first vector and insert the integral defining `K_x^E(tau)`. `QED`

## 2. Flux energy kernel

Define the positive finite matrix:

```text
A_{x,H}
 := P_HB_xC_E^(-1)B_x^*W_H^*(P_H^0)^*T_H^*T_HP_H^0W_H
    B_xC_E^(-1)B_x^*P_H.                                    (A)
```

Then:

```text
Flux_x(H,tau)^2
 = (4/(L^2x))int_0^Lint_0^L exp(i tau r)exp(-i tau r')
    G_{x,H}(r,r') dE_x^leftarrow(r)dE_x^leftarrow(r'),       (EINT)
```

where:

```text
G_{x,H}(r,r'):=<Lo_rk_x,A_{x,H}Lo_{r'}k_x>.
```

The kernel `G_{x,H}` is positive in the sense that for any finitely supported coefficients `c_a` and
points `r_a`:

```text
sum_{a,b} conjugate(c_a)c_b G_{x,H}(r_a,r_b) >= 0.
```

### Proof

Write:

```text
Flux^2
 = ||T_HP_H^0W_HB_xC_E^(-1)B_x^*P_HZ_x^{pm}(tau)||_2^2
 = <Z_x^{pm}(tau),A_{x,H}Z_x^{pm}(tau)>.
```

Insert:

```text
Z_x^{pm}(tau)
 = (2/(L sqrt(x)))int_0^L exp(-i tau r)Lo_rk_x dE_x^leftarrow(r).
```

Expanding the square gives `(EINT)`. Positivity follows from the form
`A_{x,H}=R^*R`. `QED`

## 3. Exact arithmetic target

E72.109 is now equivalent to:

```text
(MASS-INT)
 (2/(L sqrt(x)))int exp(-i tau_j r)
    <w_{x,H},Lo_rk_x>dE_x^leftarrow(r) -> 0,

(ENERGY-INT)
 (4/(L^2x))int int exp(i tau_j(r-r'))
    G_{x,H}(r,r')dE_x^leftarrow(r)dE_x^leftarrow(r') = O(1),
```

uniformly for finite root-height windows and fixed physical `H`.

This is the exact arithmetical inequality left by the Phase 72 route after all model background,
absolute HPAC, and root-current artifacts have been removed.

## 4. Why this is sharper than PNT

PNT controls `dE_x^leftarrow` against fixed smooth tests.  Here the tests depend on `x` through:

```text
Lo_r,
k_x,
C_E^(-1),
B_x,
the physical band H.
```

The energy kernel is nevertheless not arbitrary.  It is positive and built from:

```text
endpoint reflection,
Feshbach shorting,
centered spectral divergence.
```

Thus the remaining theorem is not a generic discrepancy estimate.  It is a structured
Loewner-Feshbach discrepancy energy bound.

## 5. Closure statement

### Theorem 72.110

For each fixed physical band `H`, suppose `(MASS-INT)` and `(ENERGY-INT)` hold uniformly on finite
root-height windows, and likewise for the one `s`-derivative channel.  Then the post-main finite-band
root transport condition of E72.105 holds.  Together with the Cauchy-channel tail condition, scalar
WRL resonance annihilation follows.

### Proof

`(MASS-INT)` is exactly `(QMASS)`.  `(ENERGY-INT)` is exactly `(QFLUX)`.  Apply E72.109, then E72.105.
`QED`

## 6. Status

```text
proved: Mass and Flux are explicit single/double Chebyshev-discrepancy integrals;
proved: the flux kernel is positive and finite;
open:   prove the MASS-INT and ENERGY-INT bounds from the structured kernel.
```
