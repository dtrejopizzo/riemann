# E73.171 results - QG wedge identity

Date: 2026-07-14.

Script:

```text
E73_171_qg_wedge_probe.py
```

## Output

```text
E73.171 QG wedge identity probe
Uses the bilinear source convention from E73.003/E72.396.
Uses the stable Cauchy form of DD on the natural mesh d_m L=2*pi*m.
Validates ||P_Q G||^2 = det Gram(I_L,G) / det Gram(I_L).
 lam     L inter imageRel    ddRel herm/bilin   qgNorm   wedge relErr    qgB
   8   4.159     2  4.0e-06  1.3e-01   1.00e+00  3.44e-09  3.44e-09 1.7e-15  -13.67
  10   4.605     2  1.9e-07  2.1e+01   1.00e+00  6.92e-10  6.92e-10 3.0e-16  -13.81
  12   4.970     2  1.8e-06  6.0e-01   1.00e+00  1.42e-09  1.42e-09 7.3e-16  -12.71
  14   5.278     2  9.5e-06  1.2e+00   1.00e+00  1.28e-08  1.28e-08 1.9e-15  -10.92
  16   5.545     2  1.8e-04  1.2e+00   1.00e+00  1.00e-08  1.00e-08 1.2e-15  -10.75
  20   5.991     0  5.2e-02  2.9e+00   1.00e+00  3.42e-09  3.42e-09 0.0e+00  -10.89
  24   6.356     0  2.6e-01  4.7e+00   1.00e+00  8.22e-11  8.22e-11 0.0e+00  -12.56
  32   6.931     0  3.3e-02  1.1e+01   1.42e+00  3.68e-15  3.68e-15 0.0e+00  -17.17
```

## Reading

The identity

```text
||P_Q G||^2 = det Gram(I_L,G) / det Gram(I_L)
```

is verified to numerical precision in every tested row.

The rows with `imageRel <= 1e-3` are the trusted quotient rows.  In those rows
`inter=2`, hence the quotient has dimension `3`, matching E73.167.

The column `ddRel` is intentionally not a failure of the theorem.  It measures
the relative discrepancy between the direct floating-point `DD` summation and
the stable Cauchy formula after using `d_m L=2*pi*m`.  Because the critical
values are extremely small, roundoff in `e^(-i d_m L)-1` can dominate the
direct `DD` form.  The proof-facing definition is therefore the stable Cauchy
form:

```text
G_L(gamma)
= (1-e^(i gamma L)) sum_m xi_L(m)/(-gamma-d_m).
```

## Consequence

The current load-bearing target is the determinant smallness:

```text
det Gram(I_L,G_L)
<= L^(2B) e^(-2 alpha L) det Gram(I_L).
```

This is a finite scalar statement over five critical samples and two generated
intersection directions.
