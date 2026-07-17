# E73.259 - ETA adjugate certificate

## 1. Purpose

E73.256--E73.258 remove three false scalar mechanisms:

```text
1. quotient projection cancellation;
2. Q_weta=0 / endpoint constraints alone;
3. autonomous transverse eigen-residual smallness.
```

The remaining scalar theorem is the explicit coefficient identity `ETA-DIV`.
This note records the exact finite algebraic detector for that theorem in the
current Phase 73 variables.

## 2. Reduced adjugate identity

Let

```text
E_L=H_L-mu_L I,
E_L xi_L=0,
dim ker E_L=1.
```

Let `Adj_red(E_L)` denote the reduced adjugate at the simple ground eigenvalue.
Equivalently, if the nonzero eigenvalues of `E_L` are `lambda_1,...,lambda_n`,

```text
Adj_red(E_L)
= (prod_j lambda_j) xi_L xi_L^*                 (1)
```

up to the normalization `||xi_L||=1`.

For the transverse residual row

```text
rho_{a,w}=q_aH_L(I-P_w),
```

we have

```text
rho_{a,w} Adj_red(E_L)
= (prod_j lambda_j)(rho_{a,w}xi_L) xi_L^*.       (2)
```

Therefore:

```text
rho_{a,w}xi_L=0
<=> rho_{a,w}Adj_red(E_L)=0.                     (3)
```

For asymptotic divisibility:

```text
rho_{a,w}xi_L=O_M(L^-M)
```

is equivalently the normalized adjugate defect

```text
||rho_{a,w}Adj_red(E_L)|| / ||Adj_red(E_L)||
=O_M(L^-M).                                      (4)
```

## 3. Finite determinant form

Equation (3) can be written without eigenvectors as row-replacement
determinants.  Since `E_L` has rank `n-1`, a row `rho` belongs to `Row(E_L)`
iff every replacement determinant vanishes:

```text
det ReplaceRow(E_L; j, rho) = 0
```

for all rows `j`, equivalently

```text
rho Adj_red(E_L)=0.
```

Thus the exact zero-free finite identity for `ETA-DIV` is:

```text
ETA-ADJ:
rho_{a,w} Adj_red(H_L-mu_LI)=O_M(L^-M)||Adj_red(H_L-mu_LI)||.
```

All entries are finite Gamma-prime quantities:

```text
H_L = H_model,L - Prime_L,
rho_{a,w}=q_aH_L(I-P_w).
```

## 4. Anti-tautology warning

This is a detector, not a forcer by itself.  The program already audited
adjugate/cofactor routes in Phase 72:

```text
E72.34--E72.35: cofactor divisibility is exact but adjugate construction can
                be tautological;
E72.352: adding rowspace rows does not change the null defect;
E73.253--E73.254: Cramer/Laplace identities locate, but do not create,
                  cancellation.
```

So `ETA-ADJ` is valid only as the finite identity to prove from the explicit
Gamma-prime formula.  It is not acceptable to prove it by projecting `rho`
onto `Row(E_L)` or by constructing `Adj_red(E_L)` from the already-known
ground vector and declaring victory.

## 5. What this buys

The scalar branch now has two equivalent proof-facing forms:

```text
ETA-DIV / coefficient form:
sum c_omega(eta_w)W_omega
+sum l_omega(eta_w)V_omega
+E_exp = O_M(L^-M).

ETA-ADJ / determinant form:
rho_{a,w}Adj_red(E_L)
=O_M(L^-M)||Adj_red(E_L)||.
```

The coefficient form is better for analytic cancellation.
The adjugate form is better for exact finite verification and row-ideal
certificates.

## 6. Status

```text
proved: ETA-DIV <=> normalized ETA-ADJ;
verified numerically: normalized adjugate defect equals rho xi in stable rows;
open: prove ETA-ADJ or ETA-DIV from explicit Gamma-prime entries without
      using the eigenvector/null defect as input.
```

