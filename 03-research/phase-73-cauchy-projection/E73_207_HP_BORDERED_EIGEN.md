# E73.207 - High-precision bordered eigen audit

Date: 2026-07-14.

## 1. Purpose

E73.205 showed that the bordered eigenline certificate fails with the legacy
double matrix because the residual is comparable to the near-radical gap.
E73.206 supplies closed high-precision matrix entries.  This note checks the
same bordered residual using those entries and a high-precision symmetric
eigensolver.

## 2. Tested quantities

For the closed high-precision arithmetic matrix:

```text
H=A_L^digamma-P_L,
H xi=mu xi,
gap=lambda_1-lambda_0,
res=||Hxi-mu xi||,
step=||J^(-1)F(mu,xi)||.
```

Here `J` is the bordered Jacobian of E73.204.

## 3. Status

```text
diagnostic: verifies that high-precision entries remove the double residual
            obstruction;
not yet: interval Krawczyk proof.
```
