# E72.12 -- One-dimensional formula for the Doob-Poisson primitive

**Date:** 2026-07-08.
**Role:** turn DPS from an abstract model inverse into an explicit cumulative-force estimate.

## 0. Starting point

E72.11 reduced the new proof target to:

```text
D_x h_x = S_x,
S_x := F_x/k_x,
F_x := Q_x(H_x-H_x^0)k_x,
```

where

```text
D_x h = - k_x^{-2} partial_theta( p_x k_x^2 partial_theta h )
```

on the mean-zero subspace of `L^2(dpi_x)`, with

```text
dpi_x = k_x^2 dtheta.
```

This document solves that equation explicitly in one dimension.

## 1. Notation

Let the prolate boundary interval be

```text
I_x = [a_x,b_x].
```

Write

```text
m_x(theta) := k_x(theta)^2,
rho_x(theta) := p_x(theta) k_x(theta)^2.
```

Then

```text
D_xh = -m_x^{-1} partial_theta( rho_x h' ).
```

The Poisson equation is

```text
-(rho_x h_x')' = m_x S_x.                       (P)
```

The solvability condition is

```text
int_{I_x} S_x m_x dtheta = 0,
```

which holds because `F_x` is orthogonal to `k_x`.

## 2. Cumulative force

Define the cumulative residual force

```text
G_x(theta) := int_{a_x}^{theta} S_x(t)m_x(t) dt.
```

Since the total mean is zero,

```text
G_x(a_x)=G_x(b_x)=0.
```

Integrating (P) once gives

```text
rho_x(theta) h_x'(theta) = -G_x(theta).          (1)
```

Therefore

```text
h_x'(theta) = -G_x(theta)/rho_x(theta).          (2)
```

Integrating again,

```text
h_x(theta) = c_x - int_{theta_0}^{theta} G_x(u)/rho_x(u) du,
```

where `c_x` is chosen by the mean-zero normalization

```text
int_{I_x} h_x(theta)m_x(theta)dtheta = 0.
```

This is the explicit model primitive. No actual inverse `C_x^{-1}` appears.

## 3. Energy identity

Multiplying (P) by `h_x` and integrating by parts yields:

```text
int rho_x |h_x'|^2 dtheta
  = int S_x h_x m_x dtheta.
```

Using (2),

```text
int rho_x |h_x'|^2 dtheta
  = int |G_x(theta)|^2/rho_x(theta) dtheta.       (E)
```

Thus the model energy of the primitive is exactly the weighted square norm of the cumulative residual
force.

## 4. L2 control by weighted Hardy

Let `lambda_{x,1}^D` be the first positive eigenvalue of the Doob generator `D_x` on mean-zero functions.
Then the Poincare inequality gives:

```text
||h_x||_{L^2(dpi_x)}^2
  <= (lambda_{x,1}^D)^(-1) int rho_x |h_x'|^2 dtheta.
```

Combining with (E):

```text
||h_x||_{L^2(dpi_x)}^2
  <= (lambda_{x,1}^D)^(-1)
     int |G_x(theta)|^2/rho_x(theta) dtheta.      (H)
```

So DPS follows from:

```text
int |G_x(theta)|^2/rho_x(theta) dtheta = o(lambda_{x,1}^D).
```

If the model is normalized so that the first complement eigenvalue is bounded below, this becomes:

```text
int |G_x(theta)|^2/rho_x(theta) dtheta -> 0.
```

## 5. The new target: cumulative cancellation

The residual force itself may be large or oscillatory. What matters is its cumulative primitive:

```text
G_x(theta) = int_{a_x}^{theta} k_x(t) F_x(t) dt.
```

Because

```text
F_x = Q_x(H_x-H_x^0)k_x,
```

the target is:

```text
int_{I_x}
  | int_{a_x}^{theta} k_x(t) Q_x(H_x-H_x^0)k_x(t) dt |^2
  / (p_x(theta)k_x(theta)^2)
dtheta -> 0.                                     (CC)
```

This is the first completely explicit form of the one-vector PSC/DPS condition.

Call it:

```text
CC = cumulative cancellation.
```

## 6. Why CC is not the old wall

CC is not:

```text
||H_x-H_x^0|| -> 0.
```

It is not:

```text
sum |prime cells| -> 0.
```

It is not:

```text
uniform boundedness of all oscillatory Jacobi coefficients.
```

It is the statement that the **single residual force on the model ground vector** has a small weighted
cumulative primitive in the model Doob coordinate.

The distinction is essential:

```text
force may be large;
cumulative force after pole/ground projection must be small.
```

This is exactly the kind of cancellation that absolute-value methods miss.

## 7. How the pole short enters

Without `Q_x`, the solvability condition would fail:

```text
int S_x m_x = <k_x,(H_x-H_x^0)k_x> = a_x.
```

The projection subtracts the scalar component:

```text
F_x = (H_x-H_x^0)k_x - a_x k_x.
```

Thus

```text
int S_x m_x = <k_x,F_x> = 0.
```

This is exactly the mean-zero condition needed for the cumulative force to vanish at both endpoints.
So the Feshbach scalar recentering is not optional; it is the Fredholm condition for the Doob-Poisson
primitive.

## 8. Actual/model replacement

CC proves the model primitive is small:

```text
w_x = k_x h_x,
||w_x|| -> 0.
```

To finish PSC, one still needs:

```text
||C_x^{-1}V_xw_x|| -> 0.
```

A sufficient one-vector condition is:

```text
||V_xw_x||_{(C_x)^*} -> 0,
```

where

```text
||y||_{(C_x)^*} := ||C_x^{-1}y||.
```

This must be proved for this specific `w_x`, not uniformly for all complement vectors.

## 9. Theorem 72.12 -- CC implies DPS

Assume:

```text
(CC1) int |G_x|^2/rho_x = o(lambda_{x,1}^D);
(CC2) ||C_x^{-1}V_x(k_xh_x)|| -> 0,
```

where `h_x` is defined by the explicit formula above. Then DPS holds, hence MCC, PSC, reduced leakage,
and the Phase 71 stable-divisor conclusion.

### Proof

By (H), `(CC1)` gives:

```text
||h_x||_{L^2(dpi_x)} -> 0.
```

Thus

```text
||k_xh_x|| -> 0.
```

The equation `D_xh_x=S_x` implies:

```text
C_x^0(k_xh_x)=F_x=b_x
```

in the model complement, so DPS holds with no model error. `(CC2)` supplies the actual/model replacement
term. E72.11 then applies. `QED`

## 10. Status

```text
proved:   explicit Doob-Poisson primitive by cumulative force;
proved:   CC + actual/model one-vector replacement => DPS => PSC;
open:     prove cumulative cancellation CC for the actual residual force.
```

The proof target is now a single weighted integral estimate for a cumulative residual force.

