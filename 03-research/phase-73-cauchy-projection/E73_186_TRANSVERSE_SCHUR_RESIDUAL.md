# E73.186 - Transverse Schur residual

Date: 2026-07-14.

## 1. Purpose

E73.181--E73.185 make the scalar explicit-formula residual finite and
certified.  This note identifies the same residual as a transverse Schur
term relative to the two-dimensional Cauchy plane.

The point is to stop treating

```text
A_L[B]-P_L[B]-principal_2D
```

as a large scalar subtraction.  It is exactly the action of `H_L` on the
component of `xi_L` transverse to the Cauchy plane.

## 2. Projection identity

Let

```text
Q_w=span{q_w,q_-w}
```

and let `P_w` be the orthogonal projection onto this row plane.  With

```text
q_jH_L = projection_{Q_w}(q_jH_L)+rho_j,
```

one has

```text
rho_j xi_L = q_j H_L (I-P_w)xi_L.              (1)
```

This is the Schur/transverse form of the principal residual.  The principal
subtraction in E73.180 is precisely the removal of the `P_w xi_L` component.

## 3. Model-prime transverse split

Since

```text
H_L=H_model,L-Prime_L,
```

(1) becomes

```text
rho_j xi_L
= q_j H_model,L (I-P_w)xi_L
 - q_j Prime_L   (I-P_w)xi_L.                 (2)
```

Thus the load-bearing theorem can be stated as:

```text
TRANS-SCRCE:
|q_j(H_model,L-Prime_L)(I-P_w)xi_L|
<= C L^(-R-a).
```

Together with `CPINV`, this implies `H0-DIV_R`.

## 4. Why this is useful

The old scalar form mixed three pieces:

```text
archimedean cell,
prime cell,
Cauchy principal correction.
```

The transverse form combines the principal correction into the vector

```text
xi_L^perp=(I-P_w)xi_L.
```

The remaining cancellation is between model and prime actions on a vector
already stripped of the dangerous Cauchy principal component.  This is a
cleaner finite theorem than estimating the raw packet.

## 5. Status

```text
proved:   rho_jxi_L = q_jH_L(I-P_w)xi_L for the orthogonal Cauchy projection;
verified: numerical equality with the E73.180 residual;
open:     prove TRANS-SCRCE uniformly from the explicit model/prime cells.
```
