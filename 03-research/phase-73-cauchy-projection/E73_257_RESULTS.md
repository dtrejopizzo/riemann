# E73.257 results - `Q eta=0` is not enough

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_257_kernel_constraint_no_go.py
```

Result:

```text
KER-Q-DIV rejected.
EIGEN-KER-DIV retained.
```

The restriction of `q_aH_L` to `ker Q_w` is much larger than its value on the
actual transverse vector `eta_w=(I-P_w)xi_L`.

Representative table:

```text
 lam      L gamma row kerDim actualB opKerB sampleMaxB sampleMeanB gapActualToOpB qetaB
   8    4.159  14.13   0     11   -21.68   -3.18      -3.51       -4.02          18.50  -26.80
  10    4.605  21.02   0     15   -14.98   -3.16      -3.43       -3.89          11.82  -25.20
  12    4.970  14.13   0     19   -20.64   -1.47      -1.66       -2.21          19.17  -23.58
  16    5.545  21.02   0     39   -18.18   -0.68      -1.21       -1.76          17.50  -22.04
  20    5.991  21.02   0     47   -17.65    1.18       0.88        0.27          18.84  -21.39
```

Interpretation:

```text
Endpoint/Cauchy constraints explain B(0)=B(L)=0 and the rank-one derivative
source, but not the rapid scalar cancellation. The remaining theorem must use
the special eigenvector origin of eta_w.
```

Current scalar theorem:

```text
EIGEN-KER-DIV:
H_Lxi_L=mu_Lxi_L,
eta_w=(I-P_w)xi_L,
Q_weta_w=0
  =>
q_aH_Leta_w=O_M(L^-M).
```

