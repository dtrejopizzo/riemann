# E73.155 - RCE as strong critical TPW

Date: 2026-07-12.

## 1. Purpose

E73.154 reduced `H0-DIV_17` to a two-dimensional Cauchy-plane residual
equation

```text
(mu I-A(w))h = rho(w)xi_L.
```

This note identifies the evaluated residual

```text
rho(w)xi_L
```

with the strong critical-node version of the transformed packet equation
from E72.317--E72.318.

## 2. Linear residual split

Write

```text
H_L = H_model,L - Prime_L,
H_model,L = W02_L - WR_L.
```

For the Cauchy plane

```text
Q_w=span{q_w,q_-w},
q_w(n)=1/(w+i d_n),
```

let `Pi_w` be the least-squares row projection onto `Q_w`.  Define

```text
rho_model,j := q_j H_model,L - Pi_w(q_j H_model,L),
rho_prime,j := q_j Prime_L   - Pi_w(q_j Prime_L).
```

Since projection is linear,

```text
rho_j = rho_model,j - rho_prime,j.
```

Therefore the decisive residual is

```text
rho_j xi_L
= rho_model,j xi_L - rho_prime,j xi_L.              (1)
```

The theorem needed for `H0-DIV_17` is the signed cancellation:

```text
SCRCE_17:
sum_j |rho_model,j xi_L-rho_prime,j xi_L|
<= C L^(-17-a),
```

where `a` is the exponent loss from `||(mu I-A)^(-1)||`.

## 3. Relation to E72.317--E72.318

E72.317 transformed the eigenvector equation by Cauchy multipliers and found
the remaining theorem:

```text
T_W02[xi] - T_WR[xi] - T_Prime[xi] small.
```

E72.318 computed the transformed cell kernel explicitly:

```text
KQ_z^infty(y;n)
= i/(z+i d_n)
   [ e^(z(L-y)) - e^(i d_n y)
     + e^(zL)e^(-i d_n y) - e^(zy) ].
```

E73.155 is the natural-height, projected, exponent-strong version of the
same theorem:

```text
rho_model xi_L - rho_prime xi_L small
```

at critical nodes `w=-i gamma`, with the Cauchy-plane principal part removed.

Thus `RCE_17` is not a new unrelated mechanism.  It is:

```text
strong critical TPW after Cauchy-plane principal-part subtraction.
```

## 4. Why this is useful

The old TPW target asked for polynomial strip growth.  That was enough for
the compact-root route but not sharp enough for the Phase 73 standard-box
gate.

The new target asks for high-order nodal cancellation, but after removing
the two-dimensional Cauchy principal part.  Numerically this principal-part
subtraction is essential: the residuals of model and prime remain ordinary
size separately, but their signed difference is tiny.

## 5. Current proof obligation

A non-circular proof must establish the finite identity

```text
rho_model,j(w)xi_L
= rho_prime,j(w)xi_L + O(L^(-17-a))
```

directly from the explicit transformed kernels and the finite prime orbit
sum.

Forbidden shortcuts:

```text
1. bound model and prime separately;
2. use H_0(w) small as input;
3. divide by the tiny ground eigenvalue mu;
4. replace the projected residual by a norm-small Cauchy-plane invariance
   statement.
```

## 6. Updated chain

```text
SCRCE_17 + CPINV
=> RCE_17
=> H0-DIV_17
=> LDIV_17
=> CSV_17
=> Uniform GATE-73
=> scalar WRL
=> Omega_7.
```

where `CPINV` is the polynomial/favorable invertibility of `mu I-A(w)`.

## 7. Status

proved:

```text
linear residual split;
connection with transformed Cauchy-packet TPW;
SCRCE_17 + CPINV implies the current endpoint.
```

open:

```text
prove SCRCE_17 analytically from the explicit finite kernels.
```
