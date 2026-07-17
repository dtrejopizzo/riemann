# E73.267 results - cell commutator formula

Command:

```text
python3 E73_267_cell_commutator_formula.py
```

## Output

```text
E73.267 prime cell commutator formula
Checks qH^P Rxi equals finite prime-cell sum of q Q_y Rxi.
 lam      L gamma row primeB cellB errB absCellB abs/prime archB centerB
   8    4.159  14.13   0    -1.52   -1.52  -25.98    -0.82  2.73e+00   -1.52   -21.68
   8    4.159  14.13   1    -1.50   -1.50  -26.75    -0.82  2.67e+00   -1.50   -21.46
   8    4.159  21.02   0    -2.18   -2.18 -484.67    -1.47  2.74e+00   -2.18   -15.76
   8    4.159  21.02   1    -2.15   -2.15  -27.72    -1.47  2.63e+00   -2.15   -15.79
  10    4.605  14.13   0    -0.14   -0.14  -23.60    -0.04  1.18e+00   -0.14   -18.50
  10    4.605  14.13   1    -0.14   -0.14  -24.06    -0.04  1.18e+00   -0.14   -18.51
  10    4.605  21.02   0    -0.42   -0.42  -24.06    -0.33  1.15e+00   -0.42   -14.98
  10    4.605  21.02   1    -0.42   -0.42  -23.60    -0.33  1.15e+00   -0.42   -14.98
  12    4.970  14.13   0    -1.32   -1.32  -23.21     0.12  1.01e+01   -1.32   -20.64
  12    4.970  14.13   1    -1.33   -1.33  -24.21     0.12  1.01e+01   -1.33   -20.35
  12    4.970  21.02   0    -2.09   -2.09  -24.21    -0.67  9.68e+00   -2.09   -16.61
  12    4.970  21.02   1    -2.10   -2.10  -24.64    -0.67  9.79e+00   -2.10   -16.84
  16    5.545  14.13   0    -4.02   -4.02  -21.17     1.41  1.09e+04   -4.02   -19.15
  16    5.545  14.13   1    -0.88   -0.88  -20.23     0.47  1.01e+01   -0.88   -20.06
  16    5.545  21.02   0    -1.91   -1.91  -21.16     0.61  7.45e+01   -1.91   -18.19
  16    5.545  21.02   1    -0.97   -0.97  -22.26     0.19  7.39e+00   -0.97   -19.04
```

## Reading

The prime cell formula is validated:

```text
qH_L^PR_wxi_L
=sum_{p^k<=e^L}(log p)p^(-k/2)qQ_{klog p}R_wxi_L.
```

The displayed `errB` is at the expected floating scale.

The important diagnostic is the incoherent ceiling:

```text
abs/prime ranges from about 1 to 1.09e4.
```

So even inside the prime part, termwise absolute values can lose several
orders of magnitude.  The final theorem must keep the signed cell sum coupled
to the archimedean functional:

```text
mathcal A_L[qQ_yR_wxi_L]
-sum_{p^k<=e^L}(log p)p^(-k/2)qQ_{klog p}R_wxi_L
=O_M(L^-M).
```

This is the finite explicit identity now carrying the scalar WRL gate.

## Status

```text
validated: finite prime-cell expansion of the commutator transport term;
confirmed: incoherent absolute cell bound is too weak;
kept: signed cell commutator transport matching as the analytic frontier.
```

