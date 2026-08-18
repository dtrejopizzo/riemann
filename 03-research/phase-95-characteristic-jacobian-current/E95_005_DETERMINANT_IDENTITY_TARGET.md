# E95.005 - Determinant identity target

## 1. Exact integrated defect

On a simple-chart subdivision, define

```text
DEF_(L,N)(s;s_*)
 =BASE_(L,N)(s;s_*)
  +integral_0^1 AJ_t(s;s_*)dt,                       (1.1)
```

where `BASE` is the projective defect between the archimedean bordered
determinant and the independent archimedean product.  The deformation identity
gives exactly

```text
DEF_(L,N)(s;s_*)
 =log R_(L,N,1)(s;s_*),                              (1.2)
```

with the normalization chosen so that the initial relative ratio is included
in `BASE`.

## 2. Remaining theorem

The direct anchor is equivalent to

```text
CHARACTERISTIC-JACOBIAN-ANCHOR:
DEF_(L_alpha,N_alpha)(s;s_*) ->0                     (2.1)
```

locally uniformly on the safe domain along one resolved directed family.

Equation (2.1) is a single signed determinant identity.  It includes the
archimedean base, the moving-level response, every prime cell and the explicit
Euler current.

## 3. What has been closed

The following objects no longer occur in the statement:

```text
dot mu_t;
the selected eigenvector;
an inner inverse;
a resonant eigenvalue scale;
a matched endpoint layer.                            (3.1)
```

## 4. What remains force-bearing

The numerator of the current is the determinant Jacobian

```text
Jac(P,chi).                                           (4.1)
```

Proving its signed integral equals the independent Euler current is exactly
the new mathematics required by the direct route.  Entrywise Gamma--prime
formulas alone do not evaluate this nonlinear Jacobian.

## 5. Status

```text
closed:
  moving-level elimination;
  exact inverse-free local current;

open:
  CHARACTERISTIC-JACOBIAN-ANCHOR, equivalently DIRECT-BORDERED-ANCHOR.
```

