# E72.375 Results - Finite right-wall identity

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_375_finite_right_wall_probe.py
```

## Output

```text
E72.375 finite right-wall identity probe
 L    c    T   N       direct              split               relErr
3.0  1.7  4.0  80 2.50086722e-01+5.22394737e-01j 2.50086722e-01+5.22394737e-01j  9.381e-15
4.0  1.8  4.5 120 -2.73990304e-01-1.53645767e-01j -2.73990304e-01-1.53645767e-01j  7.501e-15
5.0  1.9  5.0 160 -6.27526743e-01+9.49754941e+00j -6.27526743e-01+9.49754941e+00j  8.610e-15
```

## Reading

The probe compares two finite quantities on the right wall:

```text
direct =
1/(2pi) int H_z(c+it)
 [A_c(t)-sum_{n<=N} Lambda(n)n^(-1/2-c-it)] dt,
```

and

```text
split =
ArchPolar_{c,T}(z)-PrimeWall_{c,T}^{<=N}(z).
```

The relative discrepancy is `~1e-14`, so the finite identity is normalized correctly.

This validates only the algebraic split and finite Fourier form.  The open estimate is still the
uniform polynomial bound for:

```text
ArchPolar - PrimeWall^{<=N}
+ horizontal contour term
+ prime cutoff tail
+ finite Fourier-mesh tail.
```

## Status

```text
validated: finite right-wall identity;
validated: finite von Mangoldt truncation enters exactly through Fourier coefficients of H_z;
proved in E72.375: explicit prime-tail certificate;
open: prove the uniform bound for the finite identity in the Phase 72 order of limits.
```
