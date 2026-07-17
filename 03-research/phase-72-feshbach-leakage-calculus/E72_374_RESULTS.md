# E72.374 Results - Right-wall compression

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_374_right_wall_compression_probe.py
```

## Output

```text
E72.374 right-wall compression probe
 L    c    T      relCompress     pairFull          pairCompressed
3.0  1.8  4.5      8.110e-16 1.03780209e+01-1.21074359e+01j 1.03780209e+01-1.21074359e+01j
4.0  1.7  4.8      1.025e-15 1.44837041e+01-7.23011205e+00j 1.44837041e+01-7.23011205e+00j
5.0  2.0  5.0      1.724e-15 -5.00198723e+01+1.00309577e+02j -5.00198723e+01+1.00309577e+02j
```

## Reading

The probe uses an artificial even divisor and the same even test kernel structure as E72.373.  It
compares the full symmetric contour with

```text
2 * right wall + top + bottom.
```

The relative discrepancy is roundoff-scale.  This certifies the orientation and parity constants in
E72.374:

```text
PAIR-Z_{c,T}(z)
=1/(2pi) int_{-T}^{T} H_z(c+it)L_Z(c+it)dt
 + 1/(4pi i)Horiz_{c,T}(z).
```

The computation does not use zeta data; it verifies the contour-compression algebra.

## Status

```text
validated: full symmetric contour compresses to one right wall plus horizontals;
proved in E72.374: right-wall explicit formula ArchPolar - PrimeWall;
open: prove polynomial bounds for the explicit right-wall identity and tails.
```
