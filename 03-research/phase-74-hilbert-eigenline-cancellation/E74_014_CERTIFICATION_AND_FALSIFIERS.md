# E74.14 - Certification and falsifiers

Date: 2026-07-16.

## Purpose

The probe `E74_014_certification_falsifiers.py` checks whether the E74
cancellation is specific to both:

```text
1. the projected eigenline eta=(I-P_w)xi_L;
2. the closed Gamma-prime symbol W_L.
```

## Executed controls

The probe compares:

```text
zeta eta:
    HPR-DIV with eta=(I-P_w)xi_L and true W_L.

random ker(Q):
    same HPR-DIV with random vectors in ker(Q_w) of the same norm.

random symbol:
    same eta but random U/W weights in the Hilbert product-rule formula.
```

## Result

Command:

```text
python3 E74_014_certification_falsifiers.py
```

Representative output:

```text
 lam      L gamma row zetaB randKerMedB randSymMedB sepKer sepSym
  12  4.970 14.13   0 -21.29       -1.29       -1.01 -20.00 -20.28
  12  4.970 21.02   1 -19.87       -1.57       -1.81 -18.30 -18.06
  16  5.545 14.13   1 -20.16       -1.97       -0.88 -18.19 -19.28
  20  5.991 21.02   1 -19.20        0.14       -0.37 -19.34 -18.83
```

The zeta/eigenline scalar is smaller than both controls by roughly
`L^-16` to `L^-20` in the tested windows.

## Reading

The cancellation is not:

```text
1. a generic identity on ker(Q_w);
2. a generic Hilbert product-rule identity for arbitrary symbols;
3. a raw row-norm or primitive-span artifact.
```

It is specific to the combined eigenline plus Gamma-prime structure.

## Deferred controls

The Davenport-Heilbronn and planted off-line-zero controls are not wired into
the Phase 74 finite-cell harness yet.  The available planted controls live in
Phase 71's convergence-detector model, not in the current `H_L/Q_w/F_L` cell
pipeline.  Therefore they remain required before any closure claim:

```text
DH/planted harness must fail the E74.14 cancellation in the same HPR-DIV
coordinates.
```

## Status

```text
passed: random ker(Q) falsifier;
passed: random symbol falsifier;
pending: DH/planted off-line finite-cell falsifier;
open: QLIFT-DIV proof.
```

