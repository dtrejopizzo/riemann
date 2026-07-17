# E72.348 RESULTS -- Row-ideal algebra validation

**Purpose.** Validate the finite algebra behind `CERT-CFIR` before inserting the full CFIR kernels.
This checks the equivalence between:

```text
row in Row(E),
row adj(E)=0,
all row-replacement determinants vanish,
zero projection onto ker(E).
```

It does not claim that the CFIR row `R_T` has been proved to satisfy the certificate.  It certifies the
finite algebraic test that will be applied to `R_T`.

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_348_cert_cfir_row_ideal_probe.py
```

## Probe design

For each size `n`, the script builds a Hermitian rank `n-1` matrix `E` with known one-dimensional
null vector `x`.  It then tests rows of the form

```text
row = rowspace_row + eps x^*.
```

Thus `eps=0` is exactly in `Row(E)`, while `eps>0` injects a controlled null component.

The reported quantities are:

```text
max|detReplace|  = maximum replacement determinant;
||r adj(E)||     = adjugate row-membership defect;
dist(row,RowE)   = exact null-component distance;
||row||          = row norm.
```

## Results

```text
 n  eps      max|detReplace|   ||r adj(E)||    dist(row,RowE)   ||row||
 4  0.0e+00     1.669250e-15   2.837592e-15    1.241267e-16 3.195523e+00
 4  1.0e-12     8.482149e-12   9.050624e-12    9.999224e-13 3.195523e+00
 4  1.0e-09     8.482139e-09   9.050671e-09    9.999999e-10 3.195523e+00
 4  1.0e-06     8.482139e-06   9.050672e-06    1.000000e-06 3.195523e+00
 4  1.0e-03     8.482139e-03   9.050672e-03    1.000000e-03 3.195523e+00
 6  0.0e+00     2.505770e-13   7.045489e-13    8.881784e-16 1.621912e+01
 6  1.0e-12     1.623728e-10   2.704041e-10    9.992011e-13 1.621912e+01
 6  1.0e-09     1.630002e-07   2.698083e-07    9.999992e-10 1.621912e+01
 6  1.0e-06     1.630001e-04   2.698075e-04    1.000000e-06 1.621912e+01
 6  1.0e-03     1.630001e-01   2.698074e-01    1.000000e-03 1.621912e+01
 8  0.0e+00     1.760371e-11   9.142147e-11    9.155134e-16 2.181514e+01
 8  1.0e-12     9.203455e-09   1.780165e-08    9.996448e-13 2.181514e+01
 8  1.0e-09     9.209257e-06   1.774966e-05    9.999996e-10 2.181514e+01
 8  1.0e-06     9.209257e-03   1.774960e-02    1.000000e-06 2.181514e+01
 8  1.0e-03     9.209257e+00   1.774960e+01    1.000000e-03 2.181514e+01
10  0.0e+00     1.062578e-09   4.048101e-09    9.930137e-16 2.693569e+01
10  1.0e-12     3.570198e-07   6.927021e-07    1.000535e-12 2.693569e+01
10  1.0e-09     3.562629e-04   6.967981e-04    9.999996e-10 2.693569e+01
10  1.0e-06     3.562628e-01   6.968026e-01    1.000000e-06 2.693569e+01
10  1.0e-03     3.562628e+02   6.968026e+02    1.000000e-03 2.693569e+01
```

## Interpretation

For `eps=0`, all determinant and adjugate defects are at floating-point roundoff.  For `eps>0`, the
exact distance to `Row(E)` is `eps`, and both determinant and adjugate defects grow linearly with
`eps` up to the expected cofactor scale.

This validates the algebraic detector:

```text
row in Row(E)
<=> replacement determinants vanish
<=> row adj(E)=0
<=> zero null projection.
```

## Status

```text
validated: finite row-ideal algebra used by CERT-CFIR;
validated: determinant and adjugate tests detect controlled null leakage;
not yet done: construct the full CFIR row R_T from E72.342--E72.343 and run this test on it.
```
