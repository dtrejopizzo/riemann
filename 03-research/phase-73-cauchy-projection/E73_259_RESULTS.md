# E73.259 results - ETA adjugate certificate

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_259_eta_adjugate_certificate.py
```

Result:

```text
ETA-DIV is equivalent to normalized ETA-ADJ:
rho_{a,w}Adj_red(E_L)=O_M(L^-M)||Adj_red(E_L)||.
```

Representative output:

```text
 lam      L gamma row etaB rhoPairB adjNormB adjScaledB detScaleLog gapB errXiB
   8    4.159  14.13   0   0.00   -21.68  -189.35     -21.68     -238.98 -25.71   -3.72
   8    4.159  21.02   0  -0.00   -15.76  -183.43     -15.76     -238.98 -25.71   -3.72
  10    4.605  14.13   0  -0.00   -18.50  -240.74     -18.50     -339.41 -22.21   -3.85
  12    4.970  21.02   1  -0.00   -16.84  -300.69     -16.84     -455.12 -21.76   -4.51
  20    5.991  21.02   0   0.00   -17.66  -645.36     -17.66    -1123.78 -18.94    0.18
```

Reading:

```text
adjScaledB = rhoPairB
```

as predicted by

```text
Adj_red(E_L)=scale*xi_Lxi_L^*.
```

The column `adjNormB` is the unnormalized adjugate row norm and includes the
huge determinant scale.  The proof-facing quantity is the normalized defect
`adjScaledB`.

For `lambda=16,20`, `errXiB` shows the double eigensolver is no longer a good
authority for the ground line, matching the earlier Krawczyk/gap audits.  This
does not affect the exact identity; rigorous verification at those scales
requires the bordered eigenline interval certificate.

Current endpoint:

```text
Prove either:

ETA-DIV:
sum c_omega W_omega + sum l_omega V_omega + E_exp = O_M(L^-M),

or equivalently:

ETA-ADJ:
rho_{a,w}Adj_red(H_L-mu_LI)
=O_M(L^-M)||Adj_red(H_L-mu_LI)||,

from the explicit finite Gamma-prime entries.
```

