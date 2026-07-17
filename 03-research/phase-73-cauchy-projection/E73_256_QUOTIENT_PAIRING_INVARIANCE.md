# E73.256 - Quotient pairing invariance

## 1. Purpose

E73.245--E73.255 built the quotient defect

```text
delta_a = rho_a - Proj_{M_DD} rho_a,
M_DD = {Y^*E : Y in P_DD},
E = H_L - mu_L I.
```

The intended scalar target was

```text
delta_a xi_L = O_M(L^-M).
```

This note records a necessary correction: as a scalar pairing with the exact
ground eigenvector, quotienting by `M_DD` cannot create any new cancellation.

## 2. Exact lemma

Let `xi_L` be the exact normalized ground vector:

```text
E xi_L = 0.
```

For every row `m` in `M_DD`, there are finitely many primitives `Y_j` and
coefficients `c_j` such that

```text
m = sum_j c_j Y_j^* E.
```

Therefore

```text
m xi_L = sum_j c_j Y_j^* E xi_L = 0.                 (1)
```

Consequently, for the exact projection of `rho_a` onto `M_DD`,

```text
delta_a xi_L
= (rho_a - Proj_{M_DD}rho_a)xi_L
= rho_a xi_L.                                       (2)
```

Thus the quotient defect changes row geometry and coordinate conditioning, but
not the scalar obstruction.

## 3. Consequence

`BORDER-ROW-DIV` is exactly the principal residual theorem:

```text
delta_a xi_L = O_M(L^-M)
<=> rho_a xi_L = O_M(L^-M).
```

For a Cauchy row `q_a`, with `P=Q^*(QQ^*)^(-1)Q` and `R=I-P`,

```text
rho_a = q_a H_L R.
```

Therefore

```text
rho_a xi_L = q_a H_L R xi_L,
```

which is the E73.180--E73.181 explicit principal residual and the E73.234
`APR-U4` scalar:

```text
A_L[B_{a,w}] - P_L[B_{a,w}]
- sum_k (A^model_{ak}(w)-A^prime_{ak}(w)) H_k(w).
```

The quotient route does not replace `APR-U4`. It only supplies a coordinate
framework for nondegeneracy:

```text
QROW-INDEP => GRAM-NONDEG => MAXMIN-NONDEG.
```

The scalar divisibility must still be proved as the explicit principal
residual estimate.

## 4. Numerical certification and conditioning warning

The companion script verifies:

```text
deltaPair - rhoPair = - generatedPair,
generatedPair = (Proj_{M_DD}rho)xi_L.
```

In exact arithmetic `generatedPair=0`. In floating arithmetic it is controlled
by the eigensolver residual `E xi_L`, amplified by the conditioning of the SVD
basis for `M_DD`.

Representative stable rows:

```text
 lam      L pow gamma row rank rhoPairB genPairB deltaPairB invErrB ExiB
   8    4.159   0  14.13   0    5   -21.68   -24.76     -21.68   -24.76 -27.15
  10    4.605   0  21.02   0    5   -14.98   -22.51     -14.98   -22.51 -24.47
  12    4.970   0  21.02   1    5   -16.84   -20.95     -16.84   -20.95 -24.04
```

When high rational powers are added, the normalized SVD basis can amplify the
floating `E xi_L` residual and make `generatedPair` comparable to `rhoPair`.
Those changes are numerical contamination, not exact quotient structure.

## 5. Revised endpoint

The current proof-facing split is:

```text
Nondegeneracy side:
QROW-INDEP
=> GRAM-NONDEG
=> MAXMIN-NONDEG.

Scalar annihilation side:
APR-U4 / PRINCIPAL-RESIDUAL:
rho_a xi_L = O_M(L^-M)
for the four Cauchy quotient rows.

Together:
MAXMIN-NONDEG + APR-U4
=> CRAMER-NUM-DIV
=> MAXMIN-PIV-DIV
=> CURV-QUOT-DIV
=> scalar WRL.
```

Rejected as a separate scalar mechanism:

```text
quotient-projection cancellation.
```

Kept:

```text
quotient rows for nondegeneracy and coordinate selection;
explicit principal residual as the scalar theorem to prove.
```

