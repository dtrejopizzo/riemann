# E73.203 - Interval budget for the full certificate

Date: 2026-07-14.

## 1. Purpose

E73.202 states the full interval certificate.  This note measures the first
load-bearing radii:

```text
1. eigenline radius from residual/gap;
2. Cauchy-projected eta radius;
3. sensitivity of the full scalar certificate to eta.
```

This is not yet the final interval proof.  It is the feasibility audit for the
full interval path: if the eigenline radius transported by the scalar
functional is already larger than the center by many powers of `L`, the
certificate must be redesigned before implementing ball arithmetic.

## 2. Method

For the finite matrix `H`, compute:

```text
mu=lambda_0(H),        gap=lambda_1(H)-lambda_0(H),
eps_eig=||H xi-mu xi||,
rho_xi=2 eps_eig/gap.
```

For each Cauchy plane:

```text
eta=(I-P_w)xi,
rho_eta <= ||I-P_w|| rho_xi.
```

The scalar certificate is linear in `eta`.  By the E73.199 identity it is the
same functional as:

```text
eta -> q_a H eta.
```

Thus for the eigenline-radius budget one may use:

```text
S_a=||q_a H||_2,
rho_C <= S_a rho_eta.
```

The displayed `ratio` is `rho_C/|center|`.

## 3. Status

```text
diagnostic: finite sensitivity budget for eigenline uncertainty;
not yet: interval arithmetic for matrix-entry uncertainty or special functions.
```
