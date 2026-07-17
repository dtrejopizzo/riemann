# P75.010-P75.012 - Scaling, certification, and falsifier gates

## Harness

`P75_010_scaling_falsifier_harness.py` measures:

```text
normalized Cauchy nodal value;
local finite-root displacement;
Cauchy derivative at the transported root;
two-row Gram condition;
Schur transfer singular values when H is available;
falsifier response for zeta/planted/DH/random controls.
```

The harness is a discovery and regression tool.  It is not a proof.

## Certification standard

An interval-certified proof would still be required for:

```text
bordered determinant identity;
adjugate reconstruction;
Euler/Gamma sector expansion;
Gram condition;
Schur singular values;
sign and size of falsifier responses.
```

P75.002-P75.003 certify the algebraic identities structurally and by
roundoff probes.  P75 did not obtain a full interval-arithmetic certificate
for the Euler/Gamma remainder because the exact recombined remainder is the
unclosed `EG_LOCK`.

## Falsifier gate

A valid `ARITH-LOCK` candidate must pass:

```text
zeta: critical nodal values decay/lock;
planted off-line: planted height remains nonzero;
Davenport-Heilbronn: off-line nodal value remains nonzero;
random symbol: no critical divisibility;
random ker(Q): no eigenline-specific cancellation.
```

The Phase 74 falsifiers remain decisive.  P75 adds the determinant/adjugate
identity check: the finite identities are exact for the controls too, so only
the arithmetic divisibility can distinguish zeta.

## Result

No P75 candidate remainder passed the falsifier gate as a new theorem:

```text
candidate finite identities: exact for all cases, not discriminating;
candidate termwise tails: fail size or coupling;
candidate smooth cutoffs: change the chain or return to EG_LOCK;
candidate Schur bounds: require CAUCHY-COMP/global positivity.
```

