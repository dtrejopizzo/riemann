# E74.16 - Precision-floor audit

Date: 2026-07-16.

## Purpose

The Phase 74 scalar is frequently between `1e-14` and `1e-17` in double
precision.  This audit asks whether that value is merely the residual of the
numerical eigenproblem.

`E74_016_precision_floor_probe.py` keeps the same finite CCM matrix entries
but recomputes its lowest eigenpair and the Cauchy projector with 80 decimal
digits.

## Result

The eigen-equation residual falls from about `1e-16` to about `1e-81`, while
the directional scalar remains at its double-data value.  For example:

```text
lam=8: eig64=1.25e-16, scalar64=1.37e-14,
       eigMP=1.56e-81, scalarMP=1.37e-14.
```

Thus the observed scalar is not produced solely by the eigensolver residual.
It is a real feature of the rounded finite matrix.  This still does not prove
an all-orders estimate, and double-data values at the precision floor cannot
be used to infer an asymptotic rate.

## Status

```text
rejected: eigensolver residual as the sole source of cancellation;
open: an exact structural explanation and an all-orders estimate.
```

