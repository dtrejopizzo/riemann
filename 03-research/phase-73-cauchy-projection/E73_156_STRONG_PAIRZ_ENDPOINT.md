# E73.156 - Strong PAIR-Z endpoint for RCE

Date: 2026-07-12.

## 1. Purpose

E73.155 identifies the active residual cancellation as

```text
SCRCE_17:
rho_model(w)xi_L - rho_prime(w)xi_L = O(L^(-17-a)).
```

Auditing Phase 72 shows that this is not a new route.  It is the critical
natural-height strengthening of the transformed Cauchy-packet route:

```text
E72.317  transformed eigenvector equation,
E72.318  closed transformed cell kernel,
E72.319  endpoint-sensitive Abel identity,
E72.320  scalar packet factor form,
E72.321  symmetric zero-pair reduction.
```

The purpose of this note is to state the exact strengthened endpoint.

## 2. Phase 72 packet equation

E72.320 proves, for the complete-mesh transformed packet,

```text
M_z(w)
= [ ((w+z)+e^(zL)(w-z))G_x(w) - 2wG_x(z) ]
   /(w^2-z^2).
```

E72.321 pairs the shifted Xi-divisor by `{w,-w}` and cancels the `G_x(z)`
coefficient exactly.  The paired contribution is

```text
Pair_z(w)
= G_x(w)/(w^2-z^2)
   [ w(1+e^(zL))(1-e^(-wL))
     + z(1-e^(zL))(1+e^(-wL)) ].
```

The transformed equation is

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_{w in Div(Z)/+-} Pair_z(w)
  - Lcal(B_z^tail).                                  (1)
```

Phase 72 needed only polynomial strip control of the right side.

## 3. Phase 73 strengthening

For the standard-box route, polynomial strip control is too weak.  At the
critical natural nodes

```text
z = w_gamma = -i gamma,
```

after subtracting the two-dimensional Cauchy principal part as in E73.154,
we need the exponent-level statement

```text
Strong-PAIRZ_17:

| sum_{w in Div(Z)/+-} Pair_{w_gamma}(w)
  - Lcal(B_{w_gamma}^tail)
  - Principal_2(w_gamma) |
<= C L^(-17-a).                                      (2)
```

Here `Principal_2` is the explicit Cauchy-plane projection term encoded by
the matrix `A(w_gamma)` in E73.154.  Equivalently, (2) is exactly
`SCRCE_17`.

## 4. Why the principal part matters

Without subtracting the Cauchy plane, the transformed packet equation is a
global `PW-Cauchy` statement.  With the principal part subtracted, the
remaining residual is the evaluated Cauchy-plane residual:

```text
rho(w_gamma)xi_L.
```

Numerically E73.155 shows:

```text
rho_model xi_L and rho_prime xi_L are ordinary size,
rho_model xi_L-rho_prime xi_L is L^-16 to L^-19.
```

Thus the strong endpoint is a signed Abel/PAIR-Z cancellation, not a termwise
bound.

## 5. Current chain

```text
Strong-PAIRZ_17 + Tail_17 + CPINV
=> SCRCE_17 + CPINV
=> RCE_17
=> H0-DIV_17
=> LDIV_17
=> CSV_17
=> Uniform GATE-73
=> scalar WRL
=> Omega_7.
```

The finite tail term must be kept; dropping it would repeat the incomplete
complete-mesh shortcut from Phase 72.

## 6. What is proved and what is open

proved:

```text
E72.320 factor formula for M_z(w);
E72.321 exact cancellation of the G_x(z) zero-pair term;
E73.153 forced-row collapse to Cauchy divisor;
E73.154 Cauchy-plane residual equation;
E73.155 numeric strong cancellation model-prime.
```

open:

```text
prove Strong-PAIRZ_17 and Tail_17 with the principal Cauchy-plane part
subtracted.
```

This is the sharp finite identity now left.  It is stronger than the old
Phase 72 polynomial `PAIR-Z`; it is exactly the exponent-level statement
needed by the Ω7 route.
