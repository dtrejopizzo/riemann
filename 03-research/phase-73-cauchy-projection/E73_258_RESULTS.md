# E73.258 results - transverse eigen-residual audit

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_258_transverse_eigen_residual_probe.py
```

Result:

```text
TRANS-EIG-AUTO rejected.
ETA-DIV / explicit model-prime coefficient identity retained.
```

The exact identity is:

```text
R(H_L-mu_LI)eta_w = -R(H_L-mu_LI)P_wxi_L.
```

Thus any transverse small-residual proof passes through `P_wxi_L`, equivalently
through `h=Q_wxi_L`.  That is the circular Cauchy-divisor branch if used as the
source of smallness.

Representative output:

```text
 lam      L gamma etaB hB PxiB transResB forceB force/PxiB scalarMaxB scalar/transB
   8    4.159  14.13   0.00 -19.03  -17.93     -23.20  -23.20      -5.27     -21.46          1.74
  10    4.605  21.02   0.00 -14.40  -13.64     -15.83  -15.83      -2.19     -14.98          0.85
  12    4.970  14.13  -0.00 -19.10  -18.94     -21.75  -21.75      -2.81     -20.35          1.40
  20    5.991  21.02   0.00 -18.50  -20.19     -18.32  -20.66      -0.47     -17.66          0.66
```

Interpretation:

```text
The eigenvector origin is necessary but not, in this abstract projected form,
a non-circular forcer. The proof must return to the explicit finite
Gamma-prime coefficient identity from E73.235.
```

