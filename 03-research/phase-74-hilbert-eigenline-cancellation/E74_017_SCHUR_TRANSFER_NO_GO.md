# E74.17 - Exact Schur-transfer identity and quotient no-go

Date: 2026-07-16.

## Exact identity

Let

```text
H xi = mu xi,
G=QQ*,
P=Q*G^(-1)Q,
R=I-P.
```

Then

```text
QHRxi
= QHxi-QHQ*G^(-1)Qxi
= (mu I_2-QHQ*G^(-1))Qxi.
```

Define

```text
T_{w,L}=mu_L I_2-Q_wH_LQ_w^*(Q_wQ_w^*)^(-1).
```

Therefore `HPR-DIV` is exactly the estimate

```text
T_{w,L} Q_w xi_L=O_M(L^(-M)).
```

## Conditional equivalence theorem

If uniformly in the admissible window

```text
||T_{w,L}|| <= L^B,
||T_{w,L}^(-1)|| <= L^B,
```

then

```text
HPR-DIV <=> Q_w xi_L=O_M(L^(-M)).
```

Only polynomial powers are lost, and those are absorbed by the all-orders
quantifier.

## Numerical audit

`E74_017_schur_transfer_probe.py` evaluates both singular values of `T`.  In
stable windows they scale close to `L^1`, usually with condition number near
one.  No small singular direction carrying the cancellation is visible.

This rejects the proposed quotient-lift route as an independent closure
mechanism.  The scalar is a well-conditioned two-dimensional transform of
`Q_w xi_L`, not a small quotient residual.

## Correct remaining target

The next theorem must independently prove Cauchy localization:

```text
CAUCHY-EIG-LOC:
For every admissible critical window w and every M,
||Q_w xi_L|| <= A_M L^(-M).
```

An admissible proof must derive this from the explicit Gamma-prime matrix
entries, a spectral gap or coercivity statement, and finite Cauchy geometry.
It cannot assume HPR-DIV, FINAL-ETA-ADJ, or the target zero-free statement.

## Status

```text
proved: exact Schur-transfer identity;
supported numerically: polynomial conditioning of T;
rejected: QLIFT-DIV as an independent endpoint;
open: theorem-grade polynomial bounds for T and CAUCHY-EIG-LOC.
```
