# E73.205 - Bordered eigenline conditioning audit

Date: 2026-07-14.

## 1. Purpose

E73.204 replaces the failed naive Davis-Kahan eigenline certificate by a
bordered nonlinear system.  This note measures the conditioning of that
bordered system with the current double matrix engine.

This is not a proof.  It is a precision-demand audit.

## 2. Bordered matrix

For a normalized approximate eigenpair `(mu,xi)`, choose a coordinate phase
functional `ell` with `ell^*xi=1` and form:

```text
J =
[ H-mu I   -xi ]
[ ell^*     0  ].
```

The reported values are:

```text
gap=lambda_1-lambda_0,
res=||F(mu,xi)||,
cond=cond(J),
step=||J^(-1)F(mu,xi)||.
```

## 3. Status

```text
diagnostic: tells how much precision a bordered Krawczyk certificate needs;
not yet: interval Krawczyk proof.
```
