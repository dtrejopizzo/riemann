# E73.188 results - transverse eigen-branch

Command:

```text
python3 E73_188_transverse_eigen_branch_probe.py
```

Output:

```text
E73.188 transverse eigen-branch
Verifies QH(I-P)xi = (mu I - QHQ*(QQ*)^-1)Qxi and Q(I-P)xi=0.
 lam     L gamma  kerB directB branchB errB hB aNormB
  12   4.970   14.13 -23.24   -20.73   -20.61 -21.67 -21.62    1.01
  12   4.970   21.02 -24.10   -19.81   -19.81 -23.60 -20.01    0.36
  16   5.545   14.13 -23.04   -19.17   -19.05 -19.87 -20.04    1.00
  16   5.545   21.02 -22.04   -18.17   -18.16 -20.41 -19.12    0.98
  20   5.991   14.13 -20.43   -18.52   -18.29 -18.75 -19.29    1.00
  20   5.991   21.02 -21.39   -17.51   -17.50 -19.11 -18.50    1.01
  24   6.356   14.13 -19.61   -16.63   -16.62 -18.89 -17.62    1.01
  24   6.356   21.02 -20.12   -17.78   -17.87 -18.75 -18.86    1.00
  32   6.931   14.13 -19.26   -17.20   -17.24 -17.89 -18.24    1.00
  32   6.931   21.02 -19.77   -16.69   -16.78 -17.33 -17.77    1.01
```

Column meanings:

```text
kerB     = log_L ||Q(I-P)xi||
directB  = log_L ||QH(I-P)xi||
branchB  = log_L ||(mu I-A_Q)Qxi||
errB     = log_L error between direct and branch
hB       = log_L ||Qxi||
aNormB   = log_L ||A_Q||
```

Reading:

```text
Q(I-P)xi=0 to numerical precision.
The exact branch identity QH(I-P)xi=(mu I-A_Q)Qxi is verified.
The branch is not a proof of smallness because it uses Qxi, the quantity
that the divisor theorem is meant to prove small.
```

Conclusion:

```text
The anti-circular theorem is TRANS-CELL:

for eta=(I-P)xi with Qeta=0,

QH_model eta = QPrime eta + O_R(L^-R),

proved from the explicit archimedean and prime cells, not from Qxi small.
```
