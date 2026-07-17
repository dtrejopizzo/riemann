# E73.208 - Krawczyk budget audit

Date: 2026-07-14.

## 1. Purpose

E73.207 shows that the bordered residual is tiny when the matrix entries are
computed from the closed high-precision formula.  This note turns that into an
explicit Krawczyk-radius budget.

## 2. Radius inequality

Let `J_0` be the bordered Jacobian at the high-precision center, and set

```text
Y=J_0^(-1),
step=||YF(x_0)||.
```

Assume the matrix interval has operator radius `epsH`, and the variable box has
radius `rho` in `(xi,mu)`.  A sufficient Euclidean Krawczyk inclusion is:

```text
step + ||Y|| epsH + ||Y|| (epsH+2rho)rho < rho.       (K)
```

The term `||Y||epsH` accounts for the residual uncertainty from `[H]`, while
`||Y||(epsH+2rho)rho` bounds the Jacobian variation over the box:

```text
Delta J =
[ Delta H - Delta mu I    -Delta xi ]
[ 0                         0       ].
```

## 3. Output

The script reports the largest `epsH` for which a radius `rho` satisfying `(K)`
is found, with a safety factor `lhs/rho <= 0.5`.

This is still not an outward-rounded proof.  It is the quantitative target for
the interval matrix-entry engine.

## 4. Status

```text
derived: explicit Krawczyk radius inequality for the bordered eigenline;
measured: admissible matrix-entry/operator radius in small windows;
open: prove the closed entry intervals have epsH below this budget.
```
