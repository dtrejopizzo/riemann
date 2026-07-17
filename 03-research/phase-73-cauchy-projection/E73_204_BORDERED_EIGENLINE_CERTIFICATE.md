# E73.204 - Bordered eigenline certificate

Date: 2026-07-14.

## 1. Purpose

E73.203 shows that a naive Davis-Kahan certificate built from the current
double eigensolver is useless: the near-radical spectral gap is as small as the
floating eigen residual.  The full interval route therefore needs a different
source for the certified eigenline.

The correct replacement is a bordered nonlinear certificate for `(mu,xi)`.

## 2. Bordered system

Fix a phase vector `ell` with `ell^*xi_0=1`, for instance the coordinate of
largest absolute value in the numerical eigenvector.  Define

```text
F(mu,xi)=
(
  (H-mu I)xi,
  ell^*xi-1
).
```

The unknowns are `(mu,xi)` and the target is the simple ground eigenpair.
The Jacobian at an approximate solution `(mu_0,xi_0)` is the bordered matrix

```text
J_0 =
[ H-mu_0 I   -xi_0 ]
[ ell^*       0    ].
```

If `J_0` is invertible and an interval Newton/Krawczyk test maps a ball
`B((mu_0,xi_0),rho)` strictly into itself, then there is a unique eigenpair
inside that ball.

## 3. Why this is better than the naive gap bound

Davis-Kahan from double data uses only:

```text
rho_xi <= 2 ||Hxi_0-mu_0xi_0|| / gap.
```

When both numerator and denominator are near the double precision floor, this
is meaningless.  The bordered certificate instead asks for a high-precision
residual of the exact closed-form matrix entries:

```text
F(mu_0,xi_0)=O(precision).
```

The small spectral gap still appears in `||J_0^{-1}||`, but it is paid only
after the residual has been computed with enough precision.  This is exactly
the right arithmetic: to certify a branch with gap `L^-20`, the matrix/eigenpair
residual must be computed below that scale.

## 4. Krawczyk certificate

Let `[H]` be the interval matrix from E73.202 and let `[J]` be the induced
interval Jacobian on a box `X` around `(mu_0,xi_0)`.  Choose a numerical inverse
`Y approximate J_0^(-1)`.  The Krawczyk map is

```text
K(x_0,X)=x_0 - YF(x_0) + (I-Y[J])(X-x_0).
```

If

```text
K(x_0,X) subset int(X),
```

then there is a unique zero of `F` in `X`.  The resulting interval vector
`[xi]` replaces the Davis-Kahan ball in E73.202.

## 5. Consequence for the full certificate

The corrected full interval route is:

```text
closed-form interval matrix entries
=> bordered Krawczyk eigenline [xi]
=> Cauchy projection [eta_w]
=> finite packet coefficient intervals
=> A_L^digamma-P_L interval
=> TRANS-CELL.
```

This avoids the false-negative of E73.203 while still certifying the same exact
ground branch.

## 6. Minimal executable target

The next implementation target is:

```text
BORDER-EIG-CERT(lambda,N):
1. compute high-precision centers for H, mu_0, xi_0;
2. build J_0 and Y=J_0^(-1);
3. compute residual ||F(mu_0,xi_0)|| using closed-form entries;
4. report ||YF|| and ||I-YJ_0||;
5. then replace point arithmetic by interval entries.
```

The first four steps are a conditioning audit; step 5 is the rigorous
certificate.

## 7. Status

```text
replaces: naive Davis-Kahan from double eigensolver;
proved: bordered/Krawczyk implication for eigenline certification;
implemented next: high-precision closed-form matrix-entry centers (E73.206);
implemented: Krawczyk inclusion with BALL-ENTRY epsH (E73.217);
open: propagate certified [xi] through Cauchy projection and final scalar.
```
