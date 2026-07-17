# P76.001 results - endpoint and finite-precision audit

Command:

```text
python3 P76_001_dependency_audit.py
```

## Algebraic result

The Phase-75 unnormalized `ADJ-ARITH-LOCK` is withdrawn.  The valid target is

```text
NORMALIZED-ARITH-LOCK:
A_L(gamma)
= r_gamma^* adj(H_L-mu_L I) r_gamma / tr adj(H_L-mu_L I)
= O_M(L^-M),
```

when `mu_L` is simple.  The multiplicity-safe target is

```text
r_gamma^* Pi_{mu_L} r_gamma=O_M(L^-M).
```

The positive resolvent convention is

```text
Pi_mu=Res_{lambda=mu}(lambda I-H)^(-1).
```

## Dependency result

The actual CCM builder uses only the cell kernel, the archimedean terms, and
prime powers.  It receives no zero ordinates.  The `GAMMAS` table is imported
only after `H_L` is built and is used as an evaluation set.  Thus the probe
does not insert the tested roots directly.

## Numerical result

At double precision, the five tested zeta matrices have apparent ranks

```text
dim:   17  21  25  33  49
rank:  11  11  12  14  20
```

and their two lowest reported eigenvalues are separated by only
`2e-16--7e-16`.  Consequently:

```text
1. the lowest eigenvector returned by eigh is not a numerically certified
   simple eigenline;
2. the adjugate identity cannot be evaluated on these CCM matrices in
   float64;
3. symmetrizing that vector does not repair the missing spectral resolution.
```

The apparent numerical kernel is selective.  Its normalized overlaps with
the first critical Cauchy row are `1e-14--1e-15`, while the overlap at
`gamma_1+0.125` grows from `1e-4` to `1.4e-1` across the tested truncations.
For the second critical row it reaches `4e-15`, while its displaced-row
overlap reaches `1.2e-1` in the largest case.

This selectivity is real evidence that the arithmetic matrix encodes the
critical ordinates without receiving their list.  It is not evidence for an
exact nullspace or an all-orders estimate.

## Reconciliation with Phase 62

Phase 62 already established that the apparent low rank is a threshold
artifact: the zeta spectrum forms an exponential cascade below machine
precision with no uniform spectral margin.  Therefore P76.001 does not call
the displayed nullity exact.  It proves instead that the Phase-75 lock sits
inside an unresolved spectral cluster.

The arbitrary-precision eigensolve in E74.016 is insufficient for this
question because its matrix entries were first constructed in float64.  It
can reduce the eigensolver residual but cannot recover the eigenvalues lost
when the CCM integrals were rounded.

## Gate decision

P76.001 is complete.  Before any resolvent/adjugate factorization can be
accepted, Phase 76 must:

```text
1. construct the CCM entries themselves at high precision;
2. resolve the cascade and test simplicity at that precision;
3. compare the simple-eigenline observable with threshold-independent
   spectral projectors;
4. vary precision separately from L and N.
```

Until that gate closes, the Phase-75 double-precision zeta lock is classified
as `unresolved arithmetic selectivity`, not as `CRIT-NUM-DIV`.
