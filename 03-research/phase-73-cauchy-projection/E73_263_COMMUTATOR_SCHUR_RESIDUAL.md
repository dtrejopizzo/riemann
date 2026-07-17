# E73.263 - Commutator-Schur residual form of UNIF-ETA

Date: 2026-07-14.

## 1. Purpose

E73.262 leaves the analytic theorem:

```text
UNIF-ETA:
|q_aH_L(I-P_w)xi_L| <= A_M L^-M.
```

This note rewrites the same scalar in the fixed Cauchy commutator/Schur form.
The point is to expose the exact finite row that must be controlled without
using `Q_wxi_L` as a small input.

## 2. Exact residual identity

Let

```text
Q=Q_w,
P=Q^*(QQ^*)^(-1)Q,
R=I-P,
q=q_a
```

where `q` is one row of `Q`.  Since `qP=q`, one has

```text
qR=0.                                             (1)
```

Therefore

```text
rho_{a,w}
=qH_LR
=qH_L-qH_LQ^*(QQ^*)^(-1)Q.                       (2)
```

Equivalently,

```text
rho_{a,w}
=-q[H_L,P].                                      (3)
```

Indeed,

```text
q[H_L,P]=qH_LP-qPH_L=qH_LP-qH_L=-qH_LR.
```

Thus the scalar center has the exact forms

```text
qH_LRxi_L
= [qH_L-qH_LQ^*(QQ^*)^(-1)Q]xi_L
= -q[H_L,P]xi_L.                                 (4)
```

No eigenvector smallness has been used.

## 3. Why this is useful but not enough

Equation (4) says the residual is the Cauchy-Schur interpolation error of the
row `qH_L`, or equivalently the commutator of `H_L` with the Cauchy projection.

The forbidden shortcut is to substitute

```text
QH_Lxi_L=mu_LQxi_L
```

and then bound through `Qxi_L`; that is the circular E73.240 branch.  The
non-circular problem is instead:

```text
prove that the fixed Schur residual row in (2), paired with xi_L, is rapidly
small from the explicit Gamma-prime construction.
```

This is exactly the coefficient-side `EIG-COEFF` requirement from E73.262.

## 4. Archimedean-prime split

Write

```text
H_L=H_L^A-H_L^P.
```

Then

```text
rho_{a,w}=rho^A_{a,w}-rho^P_{a,w},
rho^A_{a,w}=qH_L^AR,
rho^P_{a,w}=qH_L^PR.                              (5)
```

Thus `UNIF-ETA` requires the paired Schur residuals of the archimedean and
prime rows to match to rapid order:

```text
rho^A_{a,w}xi_L - rho^P_{a,w}xi_L = O_M(L^-M).   (6)
```

This is stronger and more precise than a row norm estimate.  The individual
rows may have large norm; only their paired Gamma-prime cancellation matters.

## 5. Numerical audit

The companion script checks:

```text
rho=qHR,
rho=qH-(qHQ*)GQ,
rho=-q[H,P],
```

and reports the archimedean/prime paired split.

Representative output:

```text
centerB  = exponent of |rho xi_L|
archB    = exponent of |rho^A xi_L|
primeB   = exponent of |rho^P xi_L|
rhoNormB = exponent of ||rho||
```

The expected diagnostic is:

```text
schurErrB, commErrB at roundoff;
rhoNormB not rapidly small;
centerB much smaller than generic row scale.
```

This would confirm that the remaining theorem is a paired commutator
cancellation, not an operator-norm or Schur-row smallness theorem.

## 6. Refined theorem target

The current analytic target can now be stated as:

```text
Schur-Commutator Eigenline Cancellation.
For the explicit Gamma-prime CCM matrix H_L, the Cauchy projection P_w, and
the normalized ground eigenline xi_L,

|q_a[H_L,P_w]xi_L| <= A_M L^-M
```

uniformly over admissible windows and rows.

Equivalently, in the arch/prime split:

```text
|q_aH_L^A(I-P_w)xi_L - q_aH_L^P(I-P_w)xi_L|
<= A_M L^-M.
```

Together with E73.262 this implies `UNIF-ETA`.

## 7. Status

```text
proved: UNIF-ETA center = fixed Cauchy-Schur row residual;
proved: same center = paired finite-rank commutator -q[H_L,P_w]xi_L;
proved: arch/prime paired split formula;
open: prove rapid paired cancellation from the Gamma-prime eigenline equation.
```

