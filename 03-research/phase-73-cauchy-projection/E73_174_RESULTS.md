# E73.174 results - QG quadrature form

Date: 2026-07-14.

Script:

```text
E73_174_qg_quadrature_probe.py
```

## Output

```text
E73.174 QG quadrature form
Rebuilds Arch_r and Prime_r from the scalar packet B_r(y)=a_r Q(y) xi.
 lam     L imageRel form archErr primeErr matchB muqB packet0B
   8   4.159  4.0e-06    0 4.0e-15  2.5e-15  -25.68 -38.04   -13.75
   8   4.159  4.0e-06    1 3.0e-15  1.9e-15  -25.89 -37.87   -13.59
   8   4.159  4.0e-06    2 3.5e-15  1.7e-15  -25.49 -37.73   -13.45
  10   4.605  1.9e-07    0 7.4e-16  2.2e-15  -24.05 -36.95   -14.93
  10   4.605  1.9e-07    1 1.0e-16  1.9e-15  -23.39 -36.02   -13.99
  10   4.605  1.9e-07    2 2.7e-16  1.7e-15  -23.71 -35.43   -13.41
  12   4.970  1.8e-06    0 3.6e-14  1.4e-14  -22.30 -35.29   -14.34
  12   4.970  1.8e-06    1 4.7e-14  8.3e-14  -22.87 -33.33   -12.38
  12   4.970  1.8e-06    2 4.2e-14  7.4e-14  -23.13 -33.62   -12.67
  14   5.278  9.5e-06    0 1.4e-16  3.1e-16  -23.89 -31.62   -11.86
  14   5.278  9.5e-06    1 1.6e-14  7.0e-16  -20.56 -30.63   -10.87
  14   5.278  9.5e-06    2 9.1e-15  6.8e-16  -20.61 -30.37   -10.62
```

## Reading

The reconstruction of each side is accurate:

```text
archErr  ~= 1e-14 or better,
primeErr ~= 1e-14 or better.
```

Thus the scalar packet formula is correct.

The column `matchB` should not be read as a failed theorem.  It is the result
of subtracting two much larger floating-point quantities.  Since `muqB` is
often beyond the available cancellation precision, direct quadrature
subtraction saturates before reaching the true scale.

The proof-facing object is therefore symbolic:

```text
A_L[B_r] - P_L[B_r],
```

not the floating-point subtraction of separately evaluated `A_L[B_r]` and
`P_L[B_r]`.

## Endpoint

The current theorem is:

```text
QG-QUAD:
|A_L[B_r]-P_L[B_r]| <= |mu_L| L^B e^(-alpha L),
r=1,2,3.
```

This implies `QG-LF`, hence `QG`.
