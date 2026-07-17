# E72.373 Results - Pair trace residue normalization

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_373_pair_trace_residue_probe.py
```

## Output

```text
E72.373 pair trace residue probe
 L      z                  pairSum             contour            relErr
 3.0  (0.2+0.6j)         -5.54415820e-01-1.69449126e+01j -5.49868467e-01-1.69331586e+01j  7.434e-04
 4.0  (-0.1+0.8j)        8.85819612e+00-1.73482001e+01j 8.83500924e+00-1.73427135e+01j  1.223e-03
 5.0  (0.3+0.4j)         7.17821708e+01+1.30475161e+02j 7.18131346e+01+1.30513897e+02j  3.329e-04
```

## Reading

The probe uses an artificial even divisor and a test function satisfying the Phase 72 symmetry

```text
G(-w)=e^(-wL)G(w).
```

It compares:

```text
sum_{w in Div/+-, finite} H_z(w)
```

with

```text
1/(4pi i) int_Gamma H_z(w) Z'(w)/Z(w) dw.
```

The relative error is `10^-3`, consistent with a simple midpoint quadrature on a finite rectangle.
The test certifies the normalization and the factor of `1/2` between the full divisor trace and the
pair trace.  It does not use zeta data and does not prove `CTRACE`.

## Status

```text
validated: pair trace residue normalization;
validated: divisor-pair sum equals the half-residue trace numerically;
proved in E72.373: exact residue identity for symmetric finite contours;
open: prove the zeta contour compression bound CTRACE.
```
