# E74.27 - Final research ledger after E74.17

Date: 2026-07-16.

## Objective audit

### Schur transfer

Proved exactly:

```text
QH(I-P)xi=TQxi,
T=mu I-QHQ*(QQ*)^(-1),
det T=det(mu QQ*-QHQ*)/det(QQ*).
```

The transfer is similar to the Hermitian compression

```text
mu I-(QQ*)^(-1/2)QHQ*(QQ*)^(-1/2).
```

Numerically, on resolved zeta windows, `T/L` is close to `-I` and is well
conditioned.  A theorem-grade uniform polynomial bound was not obtained,
because its lower bound reduces to the signed coupled estimate
`CAUCHY-COMP`.  The prime contribution is essential, and replacing the
coupled estimate by global Weil positivity would assume the target.

### CAUCHY-EIG-LOC

Proved equivalent forms:

```text
CAUCHY-EIG-LOC
<=> CRIT-NUM-DIV
<=> CCM-ROOT-LOCK
```

under explicit polynomial Gram/derivative separation hypotheses.  The
zeta finite roots lock at the double-data floor.  However, no independent
all-orders proof was obtained.

### Mechanism audits

Rejected by exact identities or direct probes:

```text
quotient lift / QLIFT,
one-shot gap and Davis--Kahan,
confluent regularity BOOT-CELL,
generic left-coborders,
termwise Euler/Gamma estimates.
```

The exact Euler/Gamma remainder is `EG_LOCK`, which is the same signed
`TPW/scalar-WRL` endpoint.

### Falsifiers

```text
random ker(Q): fails cancellation;
random symbol: fails cancellation;
planted off-line perturbation: nodal values 1e-2--1e-1 and displaced roots;
Davenport--Heilbronn: resolved off-line nodal value about 0.20 and mu<0;
zeta: nodal locking at the available numerical floor.
```

## Conclusion

Omega7 is not closed.  The proposed post-E74.17 closure mechanisms have been
exhausted to an explicit irreducible theorem:

```text
EG_LOCK / CCM-ROOT-LOCK:
derive, from a new signed arithmetic identity, superpolynomial divisibility
of the finite CCM Weyl numerator by the critical Xi divisor.
```

Phase 71 called this quantitative stable-divisor convergence; Phase 72 called
its transformed form `PW-Cauchy/TPW`; Phase 74 called its directional form
`HPR-DIV`.  The audits prove these are equivalent faces of the same missing
mathematics, not successive reductions.

This is the theorem-grade autopsy required when `CAUCHY-EIG-LOC` cannot be
proved by the allowed finite algebra.  Further progress requires a genuinely
new arithmetic identity for `EG_LOCK`; another projection, quotient, or
finite eigenline detector would only rename the endpoint.

