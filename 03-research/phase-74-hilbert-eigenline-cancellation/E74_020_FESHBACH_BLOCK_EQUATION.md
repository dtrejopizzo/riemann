# E74.20 - Exact Feshbach block equation and bootstrap target

Date: 2026-07-16.

## Exact equation

Let `U=Q*G^(-1/2)` and let `V` be an isometry onto its orthogonal complement.
Write

```text
xi=Uu+Veta,
A=U*HU,
B=U*HV.
```

The projected eigenline equation is

```text
(A-mu I)u=-B eta.                 (FB-EIG)
```

Under `CAUCHY-COMP`, `A-mu I` has inverse of size `O(L^-1)`, hence

```text
||u|| <= O(L^-1)||B eta||.
```

## Probe result

`E74_020_feshbach_block_probe.py` finds

```text
||B||/gap approximately 0.03--0.11,
```

so ordinary block perturbation gives useful but only fixed-order
localization.  For the actual eigenline, however,

```text
||B eta|| approximately L^(-18) or smaller
```

in double-data exponents.  Random complement vectors do not have this
property.

## Meaning

The all-orders estimate cannot follow from the operator norm of `B` alone.
The surviving possible mechanism is an iterated regularity/bootstrap lemma:

```text
BOOT-CELL(r):
membership of eta in a fixed r-th Cauchy/Gamma regularity class
implies ||B eta|| <= C_r L^(-r).
```

If the eigenline equation preserves these classes and the constants are
controlled for every fixed `r`, then `(FB-EIG)` yields
`CAUCHY-EIG-LOC` to all orders.

This target is non-tautological only if the regularity classes and their
action estimates are defined without `xi`, HPR-DIV, or the final scalar.

## Status

```text
proved: exact two-block eigenline equation;
rejected: one-shot Davis--Kahan/operator-norm closure;
survives: iterated Cauchy/Gamma regularity bootstrap BOOT-CELL(r).
```

