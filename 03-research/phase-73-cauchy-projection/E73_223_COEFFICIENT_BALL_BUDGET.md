# E73.223 - Packet coefficient ball budget

Date: 2026-07-14.

## 1. Purpose

E73.222 reduces the closed scalar center to

```text
C_a = sum_omega c_omega W_omega
    + sum_omega l_omega V_omega
    + E_exp.
```

This note certifies the first half of that reduction: the packet coefficient
balls for `c_omega,l_omega` induced by the certified vector ball `[eta_w]`.

## 2. Linear coefficient maps

For each fixed Cauchy row, frequency coefficients are linear in `eta`:

```text
c_omega = u_omega eta,
l_omega = v_omega eta.
```

These maps are read directly from the finite Weyl packet formula in
`packet_modes`.  If

```text
||eta-eta_0|| <= rho_eta,
```

then

```text
rad(c_omega) <= ||u_omega|| rho_eta,
rad(l_omega) <= ||v_omega|| rho_eta.             (1)
```

This is a finite Euclidean bound, not a sampling or cancellation estimate.

## 3. Result

The coefficient radii are tiny in all tested windows.  With the inflated
Bernoulli-sector budget `C_sec=10^6`, the worst displayed relative coefficient
radius is about

```text
7.6e-26.
```

The sums of coefficient radii remain around

```text
L^-40 ... L^-47
```

under `C_sec=10^6`, and around

```text
L^-49 ... L^-56
```

under `C_sec=1`.

## 4. Consequence

Coefficient uncertainty inherited from the certified eigenline is not a
bottleneck for the closed-center interval.  The remaining center-side audit is
the weight side:

```text
W_omega,V_omega
```

including elementary exponential integrals, prime samples, and the
`psi/psi_1` tail.

## 5. Status

```text
proved: coefficient radius formula (1);
verified: coefficient balls are negligible in tested windows;
next: weight-ball budget for W_omega,V_omega.
```
