# P75.016 - Final ledger

Date: 2026-07-16.

## Completed work

Phase 75 created the finite arithmetic numerator framework:

```text
D_L(z)=prod_n(z-d_n),
P_L(z)=sum_n xi_L(n) prod_{m != n}(z-d_m),
C_L(z)=P_L(z)/D_L(z).
```

It proved and probed:

```text
Q_gamma xi_L = fixed normalization of (C_L(gamma),C_L(-gamma)),
P_L(z)=-det [[diag(z-d),xi],[1^T,0]],
|P_L(z)|^2=|D_L(z)|^2 r_z^* adj(H_L-mu_L I)r_z/tr adj(H_L-mu_L I).
```

The adjugate identity is the main gain: it removes the explicit eigenvector
and makes the obstruction a phase-free finite minor.

## What failed

The Euler/Gamma determinant expansion did not produce a new all-orders
remainder.  Recombining the archimedean, WR, and prime sectors returns:

```text
EG_LOCK_L(gamma)=TPW/scalar-WRL endpoint.
```

Cutoff changes either break/rebuild the CCM chain or return to the same
signed remainder.  Schur conditioning remains numerically benign but
theorem-grade conditional on `CAUCHY-COMP`.

## Falsifiers

The P75 harness preserves the Phase 74 discrimination:

```text
zeta: locks at double precision;
planted: nodal values 1e-2--1e-1;
Davenport-Heilbronn: critical values about 4e-3 in resolved windows;
random symbol: no divisibility;
random ker(Q): cancels only the imposed row, not the next critical row.
```

## Endpoint

Omega7 is not closed by Phase 75.  The next theorem-grade object is:

```text
ADJ-ARITH-LOCK:
r_gamma^* adj(H_L-mu_L I) r_gamma
has the critical Xi divisor with O_M(L^-M) remainder.
```

This is equivalent to `ARITH-LOCK/CRIT-NUM-DIV/CCM-ROOT-LOCK` under the
polynomial derivative and Schur transfer hypotheses already isolated in
Phases 74-75.  It is more explicit than `EG_LOCK`, but proving it still
requires the missing signed arithmetic identity.

