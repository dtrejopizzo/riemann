# E73.256 results - quotient pairing invariance

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_256_quotient_pairing_invariance.py
```

Result:

```text
Exact theorem:
If E xi_L=0 and M_DD={Y^*E}, then every generated row m in M_DD satisfies
m xi_L=0. Hence delta_a xi_L=rho_a xi_L.
```

Interpretation:

```text
The DD-local quotient is useful for row geometry and nondegeneracy, but it
cannot be the source of scalar cancellation after pairing with the exact
eigenvector. The scalar theorem is the principal residual APR-U4.
```

Representative output:

```text
E73.256 quotient pairing invariance
Because M_DD={Y*E} and E xi=0, projection modulo M_DD cannot change row pairing with xi.
 lam      L pow gamma row rank rhoPairB genPairB deltaPairB invErrB ExiB rhoNormB deltaNormB
   8    4.159   0  14.13   0    5   -21.68   -24.76     -21.68   -24.76 -27.15    -3.18     -11.15
   8    4.159   0  21.02   0    5   -15.76   -23.12     -15.76   -23.12 -27.15    -4.54      -8.25
  10    4.605   0  14.13   0    5   -18.50   -22.94     -18.50   -22.94 -24.47    -2.13      -8.32
  10    4.605   0  21.02   0    5   -14.98   -22.51     -14.98   -22.51 -24.47    -3.16      -6.63
  12    4.970   0  14.13   0    5   -20.64   -22.11     -20.62   -22.12 -24.04    -1.47      -6.99
  12    4.970   0  21.02   1    5   -16.84   -20.95     -16.84   -20.95 -24.04    -2.56      -5.61
```

The columns `genPairB` and `invErrB` are the floating residual of the exact
zero `(Proj_MDD rho)xi_L`. With high rational powers, the SVD basis can amplify
`E xi_L`; those changes are conditioning artifacts.

Revised chain:

```text
QROW-INDEP
=> GRAM-NONDEG
=> MAXMIN-NONDEG

APR-U4:
rho_a xi_L = O_M(L^-M)

MAXMIN-NONDEG + APR-U4
=> CRAMER-NUM-DIV
=> MAXMIN-PIV-DIV
=> CURV-QUOT-DIV
=> scalar WRL.
```

