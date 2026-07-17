# E73.220 results - closed-center TRANS-CELL check

Command:

```text
python3 E73_220_closed_center_transcell.py
```

Output:

```text
E73.220 closed digamma center check
Compares C_a=A_L^digamma-P_L against q_a H eta at the E73.219 center.
 lam     L    N gamma row matrixB closedB errB relErr
   8   4.159    6   14.13   0  -21.68  -21.68  -26.30  1.4e-03
   8   4.159    6   14.13   1  -21.46  -21.46  -26.36  9.3e-04
   8   4.159    6   21.02   0  -15.76  -15.76  -26.95  1.2e-07
   8   4.159    6   21.02   1  -15.79  -15.79  -26.97  1.2e-07
  10   4.605    8   14.13   0  -18.50  -18.50  -23.43  5.3e-04
  10   4.605    8   14.13   1  -18.51  -18.51  -23.43  5.4e-04
  10   4.605    8   21.02   0  -14.98  -14.98  -23.89  1.2e-06
  10   4.605    8   21.02   1  -14.98  -14.98  -23.87  1.3e-06
  12   4.970   10   14.13   0  -20.64  -20.62  -22.97  2.4e-02
  12   4.970   10   14.13   1  -20.35  -20.34  -22.98  1.5e-02
  12   4.970   10   21.02   0  -16.61  -16.61  -24.11  5.9e-06
  12   4.970   10   21.02   1  -16.84  -16.84  -24.06  9.4e-06
```

Interpretation:

The closed finite-frequency center agrees with the matrix scalar at the
exponent level.  The relative error is too large to treat the legacy matrix
center as proof-facing in the most delicate rows.  Therefore the final
certificate must use the closed center itself and add only certified arithmetic
radii around that center.
