# E73.260 results - row-replacement ETA-ADJ

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_260_row_replacement_eta_adjoint.py
```

Result:

```text
ETA-ADJ has a determinant-only form:

det ReplaceRow(E_L;i,rho_{a,w})
= scale*(rho_{a,w}xi_L)*conjugate(xi_{L,i}).
```

Thus:

```text
||det ReplaceRow(E_L;*,rho)||_2 / |scale|
= |rho_{a,w}xi_L|.
```

Representative output:

```text
 lam      L gamma row rhoPairB maxDetB l2DetB predMaxB predL2B detScaleLog gapB
   8    4.159  21.02   0   -15.84  -15.98  -15.70   -16.23  -15.84     -238.98 -25.71
  10    4.605  14.13   0   -18.49  -18.73  -18.49   -18.73  -18.49     -339.41 -22.21
  12    4.970  21.02   0   -16.59  -16.84  -16.63   -16.96  -16.59     -455.12 -21.76
  16    5.545  21.02   0   -18.95  -18.40  -17.90   -19.38  -18.95     -936.09 -19.70
```

Reading:

```text
rhoPairB: normalized scalar defect |rho xi|;
l2DetB:   direct row-replacement l2 determinant defect normalized by scale;
predL2B:  predicted normalized determinant defect from the adjugate identity.
```

For `lambda=8,10,12`, direct determinants match the identity at useful
precision.  For `lambda=16`, naive double determinant evaluation is already
ill-conditioned.  A rigorous certificate must use interval determinants or
the bordered-Krawczyk certified eigenline plus reduced adjugate formula.

