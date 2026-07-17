# E72.44 -- Adjoint Green pairing for Endpoint Doob-Weyl smallness

**Date:** 2026-07-08.
**Role:** replace the vague requirement

```text
<Q_xr_{x,s},w_x(z)> -> 0
```

by an exact mixed cumulative-energy identity.

## 0. Doob model

Use the one-dimensional Doob operator from E72.12:

```text
D_x h = -m_x^(-1) partial_theta( rho_x partial_theta h ),
m_x=k_x^2,
rho_x=p_xk_x^2.
```

All functions are mean-zero in `L^2(m_xdtheta)`.

For a source `F`, write:

```text
D_x h_F = F,
G_F(theta)=int_a^theta F(t)m_x(t)dt.
```

Then:

```text
h_F'(theta) = -G_F(theta)/rho_x(theta).
```

## 1. Green pairing identity

### Lemma 72.44

For two mean-zero sources `F` and `H`, let

```text
h_F=D_x^+F,
h_H=D_x^+H.
```

Then:

```text
<H,h_F>_{m_x}
 = int_a^b G_H(theta)G_F(theta)/rho_x(theta)dtheta.      (GP)
```

### Proof

Since `D_xh_H=H`,

```text
<H,h_F>_m = <D_xh_H,h_F>_m.
```

Integrating by parts in the Doob form gives:

```text
<D_xh_H,h_F>_m = int rho_x h_H' h_F' dtheta.
```

Using

```text
h_H'=-G_H/rho_x,
h_F'=-G_F/rho_x,
```

gives `(GP)`. `QED`

## 2. Apply to Endpoint Doob-Weyl smallness

Let the endpoint source be:

```text
F_z := Q_xS_x(z)k_x/k_x
```

in the Doob scalar coordinate, and let its primitive be:

```text
w_z=k_xD_x^+F_z.
```

Let the Weyl test source be the mean-zero scalar representative of the Cauchy vector:

```text
H_s := Q_xr_{x,s}/k_x.
```

Then:

```text
<Q_xr_{x,s},w_z>
 = <H_s,D_x^+F_z>_{m_x}
 = int G_{H_s}(theta)G_{F_z}(theta)/rho_x(theta)dtheta.  (DW)
```

This is exact in the model gauge.

## 3. Sufficient estimate

By Cauchy-Schwarz:

```text
|<Q_xr_{x,s},w_z>|
 <= ||G_{H_s}||_{rho^{-1}} ||G_{F_z}||_{rho^{-1}}.
```

Thus Endpoint Doob-Weyl Smallness follows from:

```text
sup_s ||G_{H_s}||_{rho^{-1}} = O(1),             (WT-energy)
sup_z ||G_{F_z}||_{rho^{-1}} -> 0.               (endpoint-energy)
```

This is stronger than the scalar mixed estimate, but it is a clean sufficient route.

## 4. Why this is useful

The old endpoint target was a mysterious vector pairing. E72.44 rewrites it as:

```text
mixed cumulative force of Weyl test and endpoint source.
```

Now the endpoint taper from E72.38 applies directly to `G_{F_z}`. The Cauchy test only needs a uniform
Doob-energy bound.

## 5. Status

```text
proved: exact Green pairing formula;
reduced: Endpoint Doob-Weyl Smallness follows from Weyl-test energy bound plus endpoint cumulative
         energy decay;
open:   prove endpoint cumulative energy decay for Q_xS_x(z)k_x.
```

The next estimate is therefore a cumulative endpoint-energy estimate, not a full vector estimate.
