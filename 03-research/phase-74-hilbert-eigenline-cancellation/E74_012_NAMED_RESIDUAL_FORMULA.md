# E74.12 - Named residual formula after the quotient bridge

Date: 2026-07-16.

## Purpose

E74.11 falsifies the direct bridge from APR to the raw cauchy0 coefficients,
but supports a weaker and sharper statement: the APR principal residual lies in
the same abstract quotient `(C_L+M_L)/M_L`.

This note names the residual slot left by that result.

## Coefficient notation

Let `S_L` be the canonical source basis map from coefficient coordinates to
mesh rows, with principal part `S_L^pr`.  Let

```text
a(rho) = coefficient vector of rho=qH_L(I-P_w) in S_L,
M_L    = principal generated image of (H_L-mu_LI),
C_L    = cauchy0 coordinate embedding,
P_M    = projector onto M_L in principal coefficient space.
```

The principal APR class is

```text
apr_Q := (I-P_M)a(rho)^pr.
```

E74.11 shows `apr_Q` is numerically captured by `(I-P_M)C_L`.

## Quotient-lift residual slot

Define the residual slot:

```text
QLIFT_L = { S_L^pr C z : z in C^5 and (I-P_M)Cz represents a class in Q_L }.
```

The target residual is the quotient lift `R^Q_{a,w,L}` satisfying

```text
(I-P_M) coeff(R^Q_{a,w,L}) = apr_Q.
```

Equivalently,

```text
rho_{a,w}
= Y_{a,w,L}(H_L-mu_LI)
 + R^Q_{a,w,L}
 + E^coord_{a,w,L},
```

where `E^coord` is the finite coordinate extraction error.  A proof must remove
`E^coord` by an exact partial-fraction basis, not by numerical least squares.

## Why this is not the rejected primitive-span route

The row `Y(H_L-mu_LI)` still pairs to zero with `xi_L`.  It is bookkeeping
only.  The new content is the named quotient residual:

```text
R^Q_{a,w,L} in QLIFT_L.
```

E74.9 rejected adding more primitive rows because that cannot change the
scalar.  E74.12 instead isolates the part that survives all primitive rows.

## New theorem

The proof-facing statement is:

```text
QLIFT-DIV.
For the quotient-lift residual R^Q_{a,w,L},

R^Q_{a,w,L}xi_L=O_M(L^(-M)).
```

If `QLIFT-DIV` holds, then `RSLOT-O7` holds after the partial-fraction
coordinate errors are eliminated.

## Required algebraic upgrade

The current construction uses numerical orthogonal projectors.  Before a proof
claim, it must be upgraded to:

```text
1. an explicit two-dimensional basis of C_L cap M_L;
2. an explicit three-coordinate quotient basis for Q_L;
3. a closed formula for the APR quotient-lift coefficients z_{a,w,L};
4. a finite identity proving that the coordinate residual is exactly zero.
```

## Status

```text
named: QLIFT_L residual slot;
proved numerically: APR residual is close to this slot in trusted windows;
open: exact partial-fraction quotient basis and QLIFT-DIV.
```

