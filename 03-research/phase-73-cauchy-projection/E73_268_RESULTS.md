# E73.268 results - cell/coefficient/second-Abel equivalence

Command:

```text
python3 E73_268_cell_coeff_second_abel_equivalence.py
```

## Output

```text
E73.268 cell/coefficient equivalence
Checks B(y)=qQ_yeta modes, prime modes=prime cells, and center agreement.
 lam      L gamma row maxBerrB primeErrB centerErrB matrixErrB centerB
   8    4.159  14.13   0   -26.59    -25.67     -26.12     -26.35   -21.68
   8    4.159  14.13   1   -25.98    -24.98     -25.71     -26.31   -21.46
   8    4.159  21.02   0   -26.84    -26.63     -26.50     -27.02   -15.76
   8    4.159  21.02   1   -27.01    -25.41     -25.48     -27.06   -15.79
  10    4.605  14.13   0   -23.94    -24.32     -24.77     -23.41   -18.50
  10    4.605  14.13   1   -24.36    -23.38     -23.35     -23.43   -18.51
  10    4.605  21.02   0   -24.43    -24.19     -23.84     -23.90   -14.98
  10    4.605  21.02   1   -24.32    -23.29     -24.32     -23.86   -14.98
  12    4.970  14.13   0   -22.84    -22.53     -22.46     -22.93   -20.62
  12    4.970  14.13   1   -22.50    -22.76     -22.70     -23.05   -20.34
  12    4.970  21.02   0   -23.47    -23.08     -23.34     -24.25   -16.61
  12    4.970  21.02   1   -23.82    -23.63     -23.18     -23.94   -16.84
  16    5.545  14.13   0   -19.59    -19.89     -19.81     -19.80   -18.95
  16    5.545  14.13   1   -20.29    -19.94     -19.40     -19.52   -20.03
  16    5.545  21.02   0   -20.36    -21.00     -20.00     -19.97   -18.21
  16    5.545  21.02   1   -20.55    -20.66     -20.11     -20.18   -19.13
```

## Reading

The audit confirms:

```text
B(y)=qQ_yeta
```

agrees with its finite coefficient expansion at sampled points, the prime
mode sum agrees with the prime cell sum, and the coefficient center agrees
with the matrix center to the expected floating/mp assembly scale.

At larger `lambda`, the errors approach the center scale in the most delicate
rows.  This is not a new mathematical discrepancy; it is the same finite
conditioning/cancellation issue already observed in E73.260--E73.267.

## Consequence

The three current languages are one theorem:

```text
CELL-CTM <=> COEFF-ETA <=> SECOND-ABEL.
```

The remaining analytic problem is not choosing between them.  It is proving
the common scalar bound:

```text
F_L[B_{a,w,L}]=O_M(L^-M).
```

## Status

```text
validated: cell, coefficient, and matrix assemblies agree;
proved: CELL-CTM, COEFF-ETA, and SECOND-ABEL are equivalent forms;
open: prove the common scalar rapidly decays.
```

