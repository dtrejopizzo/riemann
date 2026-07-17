# E73.261 results - reduced-adjugate certified budget

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_261_reduced_adjoint_budget.py
```

Result:

```text
The normalized ETA-ADJ interval radius is exactly the scalar TRANS-CELL radius
from E73.219. It is tiny compared with the finite center in all tested windows.
```

Representative table:

```text
 lam     L    N  dim Csec gamma row etaAdjB radB certB ratio verdict
   8   4.159    6   13    1   14.13   0   -21.68 -57.20  -21.68  1.0e-22 radius-small
   8   4.159    6   13  1e6   21.02   0   -15.76 -47.89  -15.76  1.3e-20 radius-small
  10   4.605    8   17    1   21.02   0   -14.98 -53.49  -14.98  2.9e-26 radius-small
  12   4.970   10   21  1e6   14.13   0   -20.64 -41.92  -20.64  1.5e-15 radius-small
```

Interpretation:

```text
The finite certification pipeline is now coherent:
entry balls -> Krawczyk eigenline -> eta projection -> normalized ETA-ADJ.
```

Remaining open theorem:

```text
UNIF-ETA:
|q_aH_L(I-P_w)xi_L| = O_M(L^-M)
```

uniformly, from the explicit Gamma-prime construction.

